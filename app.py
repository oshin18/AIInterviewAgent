import asyncio
import streamlit as st
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from utils.helpers import extract_text
from configs.kernel import kernel
from configs.skills import resume_function, jd_function, question_function, feedback_function, answer_function
from utils.helpers import extract_text, extract_final_answer_from_kernel_result

# Define the async function to process resume, JD, generate questions, and evaluate answers
async def process_interview(resume_file, jd_file):
    # Extract text from the uploaded files
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    if not resume_text or not jd_text:
        st.error("Failed to extract text from the uploaded files.")
        return

    # Analyze the resume and job description
    resume_sk_response = await kernel.invoke(resume_function, input_str=resume_text)
    jd_sk_response = await kernel.invoke(jd_function, input_str=jd_text)

    resume_summary = extract_final_answer_from_kernel_result(resume_sk_response.value[0])
    jd_summary = extract_final_answer_from_kernel_result(jd_sk_response.value[0])

    # Combine resume and JD summaries for context
    combined_context = f"Resume Summary:\n{resume_sk_response}\n\nJob Description Summary:\n{resume_sk_response}"

    # Generate questions based on the combined context
    question_sk_result = await kernel.invoke(question_function, input_str=combined_context)
    question = extract_final_answer_from_kernel_result(question_sk_result.value[0])
    
    return resume_summary, jd_summary, question

# Evaluate the candidate's answer to a question
async def evaluate_answer(question, user_answer, context):
    input_data = f"Question: {question}\nAnswer: {user_answer}\n\nContext: {context}"
    feedback_sk_response = await kernel.invoke(feedback_function, input_str=input_data)
    feedback = extract_final_answer_from_kernel_result(feedback_sk_response.value[0])
    return feedback

# Generator Sample Answer
async def generate_sample_answer(question, user_answer, context, feedback):
    input_data = f"Question: {question}\nAnswer: {user_answer}\n\nContext: {context}\n\nFeedback: {feedback}"
    answer_sk_response = await kernel.invoke(answer_function, input_str=input_data)
    sample_answer = extract_final_answer_from_kernel_result(answer_sk_response.value[0])
    return sample_answer

# Sample usage: Asynchronously run the mock interview process
def run_streamlit():
    st.title("Mock Interview App")

    # File upload for resume and job description
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
    jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

    if resume_file and jd_file:
        # Show a loading message while processing
        with st.spinner('Processing files...'):
            resume_summary, jd_summary, question = asyncio.run(process_interview(resume_file, jd_file))

            # Display results
            st.subheader("Resume Summary")
            st.write(resume_summary)

            st.subheader("Job Description Summary")
            st.write(jd_summary)

            st.subheader("Generated Interview Question")
            # for idx, question in enumerate(questions, 1):
            st.write(question)

            # Example answer evaluation (you can replace it with user input)
            user_answer = st.text_input("Sample Answer for Evaluation", "")
            if user_answer:
                with st.spinner('Processing Response...'):
                    feedback = asyncio.run(evaluate_answer(question, user_answer, f"{resume_summary}\n{jd_summary}"))
                    st.subheader("Answer Evaluation Feedback")
                    st.write(feedback)

                    sample_answer = asyncio.run(generate_sample_answer(question, user_answer, f"{resume_summary}\n{jd_summary}", feedback))
                    st.subheader("Sample Answer")
                    st.write(sample_answer)
    else:
        st.info("Please upload both a resume and a job description.")

if __name__ == "__main__":
    run_streamlit()