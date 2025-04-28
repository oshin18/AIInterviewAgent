# Import necessary modules
import asyncio                      # For running asynchronous functions
import streamlit as st              # Streamlit for UI components
from services.agents import generate_cover_letter  # AI agent to generate a cover letter

# Configure the Streamlit page
st.set_page_config(page_title="Cover Letter Generator")

# Set the page title shown in the app
st.title("📄 Cover Letter Generator")

# Retrieve resume and job description summaries from session state (set on home page)
resume_summary = st.session_state.get("resume_summary", "")
jd_summary = st.session_state.get("jd_summary", "")

# If either summary is missing, prompt the user to go back and upload the documents
if not resume_summary or not jd_summary:
    st.warning("Please upload your resume and job description first from the home page.")
    st.stop()  # Stop further execution

# Initialize the session state for cover letter if it hasn't been set
if "cover_letter" not in st.session_state:
    st.session_state["cover_letter"] = ""

# Display a button to trigger cover letter generation
if st.button("Generate Cover Letter"):
    with st.spinner("Generating your personalized cover letter..."):
        # Call the async agent function synchronously using asyncio.run
        st.session_state["cover_letter"] = asyncio.run(
            generate_cover_letter(resume_summary, jd_summary)
        )

# If a cover letter has been generated, display it on the page
if st.session_state["cover_letter"]:
    st.subheader("✉️ Generated Cover Letter")
    st.markdown(st.session_state["cover_letter"])
