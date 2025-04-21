import asyncio
import streamlit as st
from configs.kernel import kernel
from configs.skills import cover_letter_function
from utils.helpers import extract_final_answer_from_kernel_result

st.set_page_config(page_title="Cover Letter Generator")

st.title("📄 Cover Letter Generator")

resume_summary = st.session_state.get("resume_summary", "")
jd_summary = st.session_state.get("jd_summary", "")

if not resume_summary or not jd_summary:
    st.warning("Please upload your resume and job description first from the home page.")
    st.stop()

if "cover_letter" not in st.session_state:
    st.session_state["cover_letter"] = ""

async def generate_cover_letter():
    context = f"Resume Summary:\n{resume_summary}\n\nJob Description Summary:\n{jd_summary}"
    result = await kernel.invoke(cover_letter_function, input_str=context)
    return extract_final_answer_from_kernel_result(result.value[0])

if st.button("Generate Cover Letter"):
    with st.spinner("Generating your personalized cover letter..."):
        st.session_state["cover_letter"] = asyncio.run(generate_cover_letter())

if st.session_state["cover_letter"]:
    st.subheader("✉️ Generated Cover Letter")
    st.markdown(st.session_state["cover_letter"])
