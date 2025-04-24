import os
from configs.kernel import create_agent_from_template

# Define the directory for skills
skills_dir = "./skills"

# Define your agents
resume_agent = create_agent_from_template(
    os.path.join(skills_dir, "resume_analyzer", "SummarizeResume.skprompt.txt"),
    "ResumeAgent"
)
resume_skills_agent = create_agent_from_template(
    os.path.join(skills_dir, "skills_analyzer", "ExtractResumeSkills.skprompt.txt"),
    "ResumeSkillsAgent"
)
jd_agent = create_agent_from_template(
    os.path.join(skills_dir, "jd_analyzer", "SummarizeJD.skprompt.txt"),
    "JDAnalyzerAgent"
)
question_agent = create_agent_from_template(
    os.path.join(skills_dir, "question_generator", "GenerateQuestions.skprompt.txt"),
    "QuestionGeneratorAgent"
)
skill_question_agent = create_agent_from_template(
    os.path.join(skills_dir, "skill_question_generator", "GenerateQuestions.skprompt.txt"),
    "SkillQuestionGeneratorAgent"
)
feedback_agent = create_agent_from_template(
    os.path.join(skills_dir, "answer_evaluator", "EvaluateAnswer.skprompt.txt"),
    "AnswerEvaluatorAgent"
)
answer_agent = create_agent_from_template(
    os.path.join(skills_dir, "answer_generator", "AnswerGenerator.skprompt.txt"),
    "AnswerGeneratorAgent"
)
cover_letter_agent = create_agent_from_template(
    os.path.join(skills_dir, "cover_letter_generator", "CoverLetterGenerator.skprompt.txt"),
    "CoverLetterAgent"
)
