# Import required modules
import os
from configs.kernel import create_agent_from_template  # Function to create AI agents from prompt templates

# Define the base directory where skill prompt templates are stored
skills_dir = "./skills"

# Create an agent for summarizing resumes
resume_agent = create_agent_from_template(
    os.path.join(skills_dir, "resume_analyzer", "SummarizeResume.skprompt.txt"),  # Path to the resume summarization prompt
    "ResumeAgent"  # Name used to register or identify this agent
)

# Create an agent for extracting key skills from the resume summary
resume_skills_agent = create_agent_from_template(
    os.path.join(skills_dir, "skills_analyzer", "ExtractResumeSkills.skprompt.txt"),  # Path to the skills extraction prompt
    "ResumeSkillsAgent"
)

# Create an agent for summarizing job descriptions
jd_agent = create_agent_from_template(
    os.path.join(skills_dir, "jd_analyzer", "SummarizeJD.skprompt.txt"),  # Path to the job description summarization prompt
    "JDAnalyzerAgent"
)

# Create an agent for generating interview questions using both resume and job description summaries
question_agent = create_agent_from_template(
    os.path.join(skills_dir, "question_generator", "GenerateQuestions.skprompt.txt"),  # Path to general question generator prompt
    "QuestionGeneratorAgent"
)

# Create an agent for generating questions based solely on extracted resume skills
skill_question_agent = create_agent_from_template(
    os.path.join(skills_dir, "skill_question_generator", "GenerateQuestions.skprompt.txt"),  # Path to skill-specific question generator
    "SkillQuestionGeneratorAgent"
)

# Create an agent to evaluate candidate's answers based on context from resume and JD
feedback_agent = create_agent_from_template(
    os.path.join(skills_dir, "answer_evaluator", "EvaluateAnswer.skprompt.txt"),  # Path to answer evaluation prompt
    "AnswerEvaluatorAgent"
)

# Create an agent to generate improved or model answers based on the candidate's response and feedback
answer_agent = create_agent_from_template(
    os.path.join(skills_dir, "answer_generator", "AnswerGenerator.skprompt.txt"),  # Path to sample answer generation prompt
    "AnswerGeneratorAgent"
)

# Create an agent to generate tailored cover letters based on resume and job description summaries
cover_letter_agent = create_agent_from_template(
    os.path.join(skills_dir, "cover_letter_generator", "CoverLetterGenerator.skprompt.txt"),  # Path to cover letter generation prompt
    "CoverLetterAgent"
)
