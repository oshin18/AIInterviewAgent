# Import necessary libraries and custom helper functions
import asyncio
import streamlit as st
from utils.helpers import extract_text  # Function to extract text from uploaded files
from services.agents import (
    generate_resume_summary,       # Async function to generate a summary of the resume
    extract_resume_skills,        # Async function to extract skills from the resume
    generate_jd_summary           # Async function to generate a summary of the job description
)

# Set the configuration for the Streamlit web page
st.set_page_config(page_title="Interview Ignite", layout="centered")

# Display the app title and a subheader to explain its purpose
st.title("🔥 Interview Ignite")
st.subheader("Your ultimate launchpad for crafting tailored cover letters and preparing for interviews that align perfectly with your dream job!")

# File upload widgets for the user to upload their resume and job description
resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

# Initialize session state variables to store processed data
if "resume_summary" not in st.session_state:
    st.session_state["resume_summary"] = ""
if "jd_summary" not in st.session_state:
    st.session_state["jd_summary"] = ""

# Utility function to run an agent asynchronously and return its output
async def run_agent(agent, input_variables):
    async for response in agent.i(input_variables):
        return response.output  

# Main function to extract and process resume and job description
async def process_resume_and_jd(resume_file, jd_file):
    # Extract text from the uploaded files
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    # If text extraction fails, display an error and exit
    if not resume_text or not jd_text:
        st.error("Failed to extract text from files.")
        return None, None
    
    # Generate summaries and skill list using async AI agents
    resume_summary = await generate_resume_summary(resume_text)

    jd_summary = await generate_jd_summary(jd_text)

    resume_skills = await extract_resume_skills(resume_summary)

    return resume_summary, jd_summary, resume_skills

# If both files are uploaded, start the processing
if resume_file and jd_file:
    with st.spinner("Analyzing documents..."):
        # Run the asynchronous processing function
        resume_summary, jd_summary, resume_skills = asyncio.run(process_resume_and_jd(resume_file, jd_file))

        # Store the results in Streamlit session state for later use
        st.session_state["resume_summary"] = resume_summary
        st.session_state["jd_summary"] = jd_summary
        st.session_state["resume_skills"] = resume_skills

    # Notify the user of successful processing
    st.success("✅ Resume and JD processed successfully!")

    # Display the processed summaries and skills on the UI
    st.markdown("### 📄 Resume Summary")
    st.write(st.session_state["resume_summary"])

    st.markdown("### 📄 Resume Skills")
    st.write(st.session_state["resume_skills"])

    st.markdown("### 🧾 Job Description Summary")
    st.write(st.session_state["jd_summary"])

    # Provide navigation instructions to the user
    st.info("Now click **Cover Letter Generator** or **Mock Interview Bot** in the sidebar to begin with the magic.")

# Show info message if both files are not uploaded
else:
    st.info("Please upload both your resume and job description to begin.")
