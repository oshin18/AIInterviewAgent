import asyncio
import streamlit as st
from utils.helpers import extract_text
from services.agents import generate_resume_summary, extract_resume_skills, generate_jd_summary

st.set_page_config(page_title="Interview Ignite", layout="centered")

st.title("🔥 Interview Ignite")
st.subheader("Your ultimate launchpad for crafting tailored cover letters and preparing for interviews that align perfectly with your dream job!")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "txt"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "txt"])

if "resume_summary" not in st.session_state:
    st.session_state["resume_summary"] = ""
if "jd_summary" not in st.session_state:
    st.session_state["jd_summary"] = ""

async def run_agent(agent, input_variables):
    async for response in agent.i(input_variables):
        return response.output  # return only the first response

async def process_resume_and_jd(resume_file, jd_file):
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)
    if not resume_text or not jd_text:
        st.error("Failed to extract text from files.")
        return None, None
    
    resume_summary = await generate_resume_summary(resume_text)

    jd_summary = await generate_jd_summary(jd_text)

    resume_skills = await extract_resume_skills(resume_summary)

    return resume_summary, jd_summary, resume_skills

if resume_file and jd_file:
    with st.spinner("Analyzing documents..."):
        resume_summary, jd_summary, resume_skills = asyncio.run(process_resume_and_jd(resume_file, jd_file))
        st.session_state["resume_summary"] = resume_summary
        st.session_state["jd_summary"] = jd_summary
        st.session_state["resume_skills"] = resume_skills

    st.success("✅ Resume and JD processed successfully!")

    st.markdown("### 📄 Resume Summary")
    st.write(st.session_state["resume_summary"])

    st.markdown("### 📄 Resume Skills")
    st.write(st.session_state["resume_skills"])

    st.markdown("### 🧾 Job Description Summary")
    st.write(st.session_state["jd_summary"])

    st.info("Now click **Cover Letter Generator** or **Mock Interview Bot** in the sidebar to begin with the magic.")
else:
    st.info("Please upload both your resume and job description to begin.")
