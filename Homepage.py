import asyncio
import streamlit as st
from utils.helpers import extract_text, extract_final_answer_from_kernel_result
from configs.agents import resume_agent, jd_agent

st.set_page_config(page_title="Interview Ignite", layout="centered")

st.title("🔥 Interview Ignite")
st.subheader("Your ultimate launchpad for crafting tailored cover letters and preparing for interviews that align perfectly with your dream job!")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

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
    
    async for response in resume_agent.invoke(resume=resume_text):
        resume_summary = extract_final_answer_from_kernel_result(response.message)

    async for response in jd_agent.invoke(jd=jd_text):
        jd_summary = extract_final_answer_from_kernel_result(response.message)

    return resume_summary, jd_summary

if resume_file and jd_file:
    with st.spinner("Analyzing documents..."):
        resume_summary, jd_summary = asyncio.run(process_resume_and_jd(resume_file, jd_file))
        st.session_state["resume_summary"] = resume_summary
        st.session_state["jd_summary"] = jd_summary

    st.success("✅ Resume and JD processed successfully!")

    st.markdown("### 📄 Resume Summary")
    st.write(st.session_state["resume_summary"])

    st.markdown("### 🧾 Job Description Summary")
    st.write(st.session_state["jd_summary"])

    st.info("Now click **Cover Letter Generator** or **Mock Interview Bot** in the sidebar to begin with the magic.")
else:
    st.info("Please upload both your resume and job description to begin.")
