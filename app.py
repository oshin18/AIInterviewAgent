import streamlit as st
from configs.agents import resume_agent, jd_agent, question_agent, feedback_agent, answer_agent
from utils.helpers import extract_text

# Session state initialization
if 'resume_text' not in st.session_state:
    st.session_state.resume_text = None
if 'jd_text' not in st.session_state:
    st.session_state.jd_text = None
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []

# Sidebar for resume upload
st.sidebar.title("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Upload your resume (PDF)", type=["txt"])

if uploaded_file:
    st.session_state.resume_text = extract_text(uploaded_file)
    resume_summary = resume_agent.invoke(input_str=st.session_state.resume_text)
    st.write(resume_summary)
    st.sidebar.success("Resume processed")

# JD input
st.title("AI Interview Chat")
jd_input = st.text_area("Paste the job description here:", height=200)

if jd_input:
    st.session_state.jd_text = jd_input
    jd_summary = jd_agent.invoke(jd_input)
    st.success("Job description processed")

# Start interview
if st.session_state.resume_text and st.session_state.jd_text:
    if st.button("Start Interview"):
        q_input = f"Resume: {st.session_state.resume_text}\n\nJD: {st.session_state.jd_text}"
        questions = question_agent.invoke(q_input)
        st.session_state.questions = questions.strip().split("\n")
        st.session_state.current_question = st.session_state.questions.pop(0)
        st.session_state.chat_log.append(("assistant", st.session_state.current_question))

# Chat interface
if st.session_state.current_question:
    st.markdown("### Interview Q&A")
    for role, msg in st.session_state.chat_log:
        with st.chat_message(role):
            st.markdown(msg)

    user_input = st.chat_input("Your answer:")
    if user_input:
        # Save user input
        st.session_state.chat_log.append(("user", user_input))

        # Feedback and sample answer
        context = f"Question: {st.session_state.current_question}\nAnswer: {user_input}\nResume: {st.session_state.resume_text}\nJD: {st.session_state.jd_text}"
        feedback = feedback_agent.invoke(context)
        sample_answer = answer_agent.invoke(context)

        st.session_state.chat_log.append(("assistant", f"**Feedback:** {feedback.strip()}"))
        st.session_state.chat_log.append(("assistant", f"**Sample Answer:** {sample_answer.strip()}"))

        # Ask next question
        if st.session_state.questions:
            st.session_state.current_question = st.session_state.questions.pop(0)
            st.session_state.chat_log.append(("assistant", st.session_state.current_question))
        else:
            st.session_state.current_question = None
            st.session_state.chat_log.append(("assistant", "Interview complete! 🎉"))
