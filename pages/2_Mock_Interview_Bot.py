import asyncio
import streamlit as st
from services.agents import evaluate_answer, generate_sample_answer
from utils.wrapper import random_question_agent_wrapper

st.set_page_config(page_title="Mock Interview Bot")

st.title("🎤 Mock Interview Bot")

resume_summary = st.session_state.get("resume_summary", "")
jd_summary = st.session_state.get("jd_summary", "")
resume_skills = st.session_state.get("resume_skills", "")

if not resume_summary or not jd_summary:
    st.warning("Please upload your resume and job description first from the home page.")
    st.stop()

if "interview_step" not in st.session_state:
    st.session_state["interview_step"] = 0
    st.session_state["chat_history"] = []
    st.session_state["last_question"] = None
    st.session_state["answer_submitted"] = False
    st.session_state["user_input"] = ""

# Ask question
if st.session_state["last_question"] is None:
    with st.spinner("Generating first question..."):
        st.session_state["last_question"] = asyncio.run(random_question_agent_wrapper(resume_summary, jd_summary, resume_skills))

st.subheader(f"Question {st.session_state['interview_step'] + 1}")
st.write(st.session_state["last_question"])

# Show text area only if answer hasn't been submitted
if not st.session_state["answer_submitted"]:
    user_answer = st.text_area(
        "Your Answer", 
        key="user_input", 
        value=st.session_state.get("user_input", "")
    )

    if st.button("Submit Answer"):
        if not user_answer.strip():
            st.warning("Please enter an answer.")
            st.stop()

        with st.spinner("Evaluating your response..."):
            feedback = asyncio.run(evaluate_answer(resume_summary, jd_summary, st.session_state["last_question"], user_answer))
            sample = asyncio.run(generate_sample_answer(resume_summary, jd_summary, st.session_state["last_question"], user_answer, feedback))

        st.session_state["chat_history"].append({
            "question": st.session_state["last_question"],
            "answer": user_answer,
            "feedback": feedback,
            "sample": sample,
        })

        st.session_state["feedback"] = feedback
        st.session_state["sample"] = sample
        st.session_state["answer_submitted"] = True

        st.rerun()  
else:
    st.markdown("**Your Answer:**")
    st.markdown(st.session_state["user_input"])

    st.success("💬 Feedback:")
    st.markdown(st.session_state.get("feedback", ""))

    st.info("💡 Sample Answer:")
    st.markdown(st.session_state.get("sample", ""))

    if st.button("Next Question"):
        st.session_state["interview_step"] += 1
        st.session_state["last_question"] = asyncio.run(random_question_agent_wrapper(resume_summary, jd_summary, resume_skills))
        st.session_state["user_input"] = ""
        st.session_state["answer_submitted"] = False
        st.session_state["feedback"] = ""
        st.session_state["sample"] = ""
        st.rerun()
