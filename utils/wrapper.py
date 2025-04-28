import random
from services.agents import (
    generate_question_based_on_resume_and_jd,   # Agent to generate a question based on both resume and job description
    generate_question_based_on_skills           # Agent to generate a question based on extracted skills only
)

# Asynchronous wrapper function that randomly selects which question generation agent to use
async def random_question_agent_wrapper(resume_summary, jd_summary, resume_skills):
    """
    Randomly chooses between two question generation strategies:
    1. Based on both resume summary and job description summary
    2. Based on resume skills only

    Args:
        resume_summary (str): A summary of the candidate's resume
        jd_summary (str): A summary of the job description
        resume_skills (str): A comma seperated string for extracted skills from the resume

    Returns:
        str: A generated interview question
    """

    # Randomly decide whether to use the full resume + JD context or just the skills
    if random.choice([True, False]):
        print("🧠 Choose: Resume Summary + JD")  # Log the decision for debugging
        return await generate_question_based_on_resume_and_jd(resume_summary, jd_summary)
    else:
        print("🧠 Choose: Resume Skills Only")  # Log the decision for debugging
        return await generate_question_based_on_skills(resume_skills)
