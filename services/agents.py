from configs.agents import resume_agent, resume_skills_agent, jd_agent, cover_letter_agent, question_agent, feedback_agent, answer_agent, skill_question_agent
from utils.helpers import extract_final_answer_from_kernel_result

async def generate_resume_summary(resume_text):
    async for response in resume_agent.invoke(resume=resume_text):
        resume_summary = extract_final_answer_from_kernel_result(response.message)
    return resume_summary

async def extract_resume_skills(resume_summary):
    async for response in resume_skills_agent.invoke(resume_summary=resume_summary):
        resume_skills = extract_final_answer_from_kernel_result(response.message)
    return resume_skills

async def generate_jd_summary(jd_text):
    async for response in jd_agent.invoke(jd=jd_text):
        jd_summary = extract_final_answer_from_kernel_result(response.message)
    return jd_summary

async def generate_cover_letter(resume_summary, jd_summary):
    context = f"Resume Summary:\n{resume_summary}\n\nJob Description Summary:\n{jd_summary}"
    async for response in cover_letter_agent.invoke(context=context):
        cover_letter = extract_final_answer_from_kernel_result(response.message)
    return cover_letter

async def generate_question_based_on_resume_and_jd(resume_summary, jd_summary):
    context = f"Resume Summary:\n{resume_summary}\n\nJob Description Summary:\n{jd_summary}"
    async for response in question_agent.invoke(context=context):
        question = extract_final_answer_from_kernel_result(response.message)
    return question

async def generate_question_based_on_skills(resume_skills):
    async for response in skill_question_agent.invoke(skills=resume_skills):
        question = extract_final_answer_from_kernel_result(response.message)
    return question

async def evaluate_answer(resume_summary, jd_summary, question, answer):
    context = f"Resume Summary:\n{resume_summary}\n\nJD Summary:\n{jd_summary}"
    input_str = f"Question: {question}\nAnswer: {answer}\n\nContext: {context}"
    async for response in feedback_agent.invoke(context=input_str):
        feedback = extract_final_answer_from_kernel_result(response.message)
    return feedback

async def generate_sample_answer(resume_summary, jd_summary, question, answer, feedback):
    context = f"Resume Summary:\n{resume_summary}\n\nJD Summary:\n{jd_summary}"
    input_str = f"Question: {question}\nAnswer: {answer}\nContext: {context}\nFeedback: {feedback}"
    async for response in answer_agent.invoke(context=input_str):
        sample_answer = extract_final_answer_from_kernel_result(response.message)
    return sample_answer