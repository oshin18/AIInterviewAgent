# Import necessary libraries
import asyncio                        # To run async functions synchronously
import streamlit as st                # Streamlit for building the UI
from services.agents import evaluate_answer, generate_sample_answer  # AI agents for feedback and answer generation
from utils.wrapper import random_question_agent_wrapper              # Wrapper to randomly choose a question generation strategy

# Set page configuration for Streamlit
st.set_page_config(page_title="Mock Interview Bot")

# Display the app title
st.title("🎤 Mock Interview Bot")

# Retrieve required data from session state
resume_summary = st.session_state.get("resume_summary", "")
jd_summary = st.session_state.get("jd_summary", "")
resume_skills = st.session_state.get("resume_skills", "")

# Ensure that both resume and job description summaries are present
if not resume_summary or not jd_summary:
    st.warning("Please upload your resume and job description first from the home page.")
    st.stop()

# Initialize session state variables if running for the first time
if "interview_step" not in st.session_state:
    st.session_state["interview_step"] = 0              # Tracks the number of questions asked
    st.session_state["chat_history"] = []               # Stores history of Q&A + feedback
    st.session_state["last_question"] = None            # Stores the current question
    st.session_state["answer_submitted"] = False        # Tracks whether user has submitted an answer
    st.session_state["user_input"] = ""                 # Stores user's typed answer

# Generate the first question if not already present
if st.session_state["last_question"] is None:
    with st.spinner("Generating first question..."):
        st.session_state["last_question"] = asyncio.run(
            random_question_agent_wrapper(resume_summary, jd_summary, resume_skills)
        )

# Display current question number and the question text
st.subheader(f"Question {st.session_state['interview_step'] + 1}")
st.write(st.session_state["last_question"])

# If the user hasn't submitted an answer yet, show the input field
if not st.session_state["answer_submitted"]:
    user_answer = st.text_area(
        "Your Answer",
        key="user_input",
        value=st.session_state.get("user_input", "")
    )

    # Handle submission of the user's answer
    if st.button("Submit Answer"):
        if not user_answer.strip():
            st.warning("Please enter an answer.")
            st.stop()

        # Evaluate the answer and generate sample response using AI agents
        with st.spinner("Evaluating your response..."):
            feedback = asyncio.run(
                evaluate_answer(resume_summary, jd_summary, st.session_state["last_question"], user_answer)
            )
            sample = asyncio.run(
                generate_sample_answer(resume_summary, jd_summary, st.session_state["last_question"], user_answer, feedback)
            )

        # Save the interaction in session history
        st.session_state["chat_history"].append({
            "question": st.session_state["last_question"],
            "answer": user_answer,
            "feedback": feedback,
            "sample": sample,
        })

        # Store evaluation result in session state
        st.session_state["feedback"] = feedback
        st.session_state["sample"] = sample
        st.session_state["answer_submitted"] = True  # Mark the answer as submitted

        st.rerun()  # Refresh the page to show feedback
else:
    # Show user's submitted answer
    st.markdown("**Your Answer:**")
    st.markdown(st.session_state["user_input"])

    # Display feedback from the AI
    st.success("💬 Feedback:")
    st.markdown(st.session_state.get("feedback", ""))

    # Display AI-generated sample answer
    st.info("💡 Sample Answer:")
    st.markdown(st.session_state.get("sample", ""))

    # Button to proceed to next question
    if st.button("Next Question"):
        st.session_state["interview_step"] += 1  # Increment the question number
        st.session_state["last_question"] = asyncio.run(
            random_question_agent_wrapper(resume_summary, jd_summary, resume_skills)
        )
        # Reset fields for the next question
        st.session_state["user_input"] = ""
        st.session_state["answer_submitted"] = False
        st.session_state["feedback"] = ""
        st.session_state["sample"] = ""
        st.rerun()
