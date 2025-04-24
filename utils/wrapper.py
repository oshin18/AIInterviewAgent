import random
from services.agents import generate_question_based_on_resume_and_jd, generate_question_based_on_skills

async def random_question_agent_wrapper(resume_summary, jd_summary, resume_skills):

    if random.choice([True, False]):
        print("🧠 Choose: Resume Summary + JD")
        return await generate_question_based_on_resume_and_jd(resume_summary, jd_summary)
    else:
        print("🧠 Choose: Resume Skills Only")
        return await generate_question_based_on_skills(resume_skills)
