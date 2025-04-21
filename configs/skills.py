import os
from configs.kernel import create_function_from_template

# Define the directory for skills
skills_dir = "./skills"

# Load functions from prompt templates
resume_function = create_function_from_template(os.path.join(skills_dir, "resume_analyzer", "SummarizeResume.skprompt.txt"), "SummarizeResume")
jd_function = create_function_from_template(os.path.join(skills_dir, "jd_analyzer", "SummarizeJD.skprompt.txt"), "SummarizeJD")
question_function = create_function_from_template(os.path.join(skills_dir, "question_generator", "GenerateQuestions.skprompt.txt"), "GenerateQuestions")
feedback_function = create_function_from_template(os.path.join(skills_dir, "answer_evaluator", "EvaluateAnswer.skprompt.txt"), "EvaluateAnswer")
answer_function = create_function_from_template(os.path.join(skills_dir, "answer_generator", "AnswerGenerator.skprompt.txt"), "AnswerGenerator")
cover_letter_function = create_function_from_template(os.path.join(skills_dir, "cover_letter_generator", "CoverLetterGenerator.skprompt.txt"), "CoverLetterGenerator")
