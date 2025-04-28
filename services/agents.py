# Import AI agent configurations and a helper function to extract final answers
from configs.agents import (
    resume_agent,              # Agent to summarize the resume
    resume_skills_agent,       # Agent to extract skills from the resume summary
    jd_agent,                  # Agent to summarize the job description
    cover_letter_agent,        # Agent to generate a personalized cover letter
    question_agent,            # Agent to generate interview questions based on resume and JD
    feedback_agent,            # Agent to evaluate answers and provide feedback
    answer_agent,              # Agent to generate improved/sample answers
    skill_question_agent       # Agent to generate questions based on extracted skills
)
from utils.helpers import extract_final_answer_from_kernel_result  # Helper to extract meaningful response from AI output

# Generate a summary of the resume using the resume_agent
async def generate_resume_summary(resume_text):
    async for response in resume_agent.invoke(resume=resume_text):
        resume_summary = extract_final_answer_from_kernel_result(response.message)
    return resume_summary

# Extract relevant skills from the resume summary using the resume_skills_agent
async def extract_resume_skills(resume_summary):
    async for response in resume_skills_agent.invoke(resume_summary=resume_summary):
        resume_skills = extract_final_answer_from_kernel_result(response.message)
    return resume_skills

# Generate a summary of the job description using the jd_agent
async def generate_jd_summary(jd_text):
    async for response in jd_agent.invoke(jd=jd_text):
        jd_summary = extract_final_answer_from_kernel_result(response.message)
    return jd_summary

# Generate a tailored cover letter using both the resume and job description summaries
async def generate_cover_letter(resume_summary, jd_summary):
    context = f"Resume Summary:\n{resume_summary}\n\nJob Description Summary:\n{jd_summary}"
    async for response in cover_letter_agent.invoke(context=context):
        cover_letter = extract_final_answer_from_kernel_result(response.message)
    return cover_letter

# Generate a mock interview question using both resume and job description summaries
async def generate_question_based_on_resume_and_jd(resume_summary, jd_summary):
    context = f"Resume Summary:\n{resume_summary}\n\nJob Description Summary:\n{jd_summary}"
    async for response in question_agent.invoke(context=context):
        question = extract_final_answer_from_kernel_result(response.message)
    return question

# Generate a mock interview question based solely on the candidate's extracted skills
async def generate_question_based_on_skills(resume_skills):
    async for response in skill_question_agent.invoke(skills=resume_skills):
        question = extract_final_answer_from_kernel_result(response.message)
    return question

# Evaluate a candidate's answer to a question using context from the resume and JD
async def evaluate_answer(resume_summary, jd_summary, question, answer):
    context = f"Resume Summary:\n{resume_summary}\n\nJD Summary:\n{jd_summary}"
    input_str = f"Question: {question}\nAnswer: {answer}\n\nContext: {context}"
    async for response in feedback_agent.invoke(context=input_str):
        feedback = extract_final_answer_from_kernel_result(response.message)
    return feedback

# Generate a sample answer based on the original answer, context, and AI-generated feedback
async def generate_sample_answer(resume_summary, jd_summary, question, answer, feedback):
    context = f"Resume Summary:\n{resume_summary}\n\nJD Summary:\n{jd_summary}"
    input_str = f"Question: {question}\nAnswer: {answer}\nContext: {context}\nFeedback: {feedback}"
    async for response in answer_agent.invoke(context=input_str):
        sample_answer = extract_final_answer_from_kernel_result(response.message)
    return sample_answer
