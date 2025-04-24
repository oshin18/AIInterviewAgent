import asyncio
import streamlit as st
from services.agents import generate_cover_letter

st.set_page_config(page_title="Cover Letter Generator")

st.title("📄 Cover Letter Generator")

resume_summary = st.session_state.get("resume_summary", "")
jd_summary = st.session_state.get("jd_summary", "")

if not resume_summary or not jd_summary:
    st.warning("Please upload your resume and job description first from the home page.")
    st.stop()

if "cover_letter" not in st.session_state:
    st.session_state["cover_letter"] = ""

if st.button("Generate Cover Letter"):
    with st.spinner("Generating your personalized cover letter..."):
        st.session_state["cover_letter"] = asyncio.run(generate_cover_letter(resume_summary, jd_summary))

if st.session_state["cover_letter"]:
    st.subheader("✉️ Generated Cover Letter")
    st.markdown(st.session_state["cover_letter"])
