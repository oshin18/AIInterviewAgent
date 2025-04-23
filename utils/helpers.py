import docx2txt
import PyPDF2
import re
from semantic_kernel.contents.chat_message_content import ChatMessageContent

def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        return docx2txt.process(uploaded_file)
    else:
        return str(uploaded_file.read(), "utf-8")

# Extract the final answer value from the skill prompts output
def extract_final_answer_from_kernel_result(result: ChatMessageContent) -> str:
    try:
        raw_content = result.items[0].text if result.items and result.items[0].text else result.inner_content

        if not raw_content:
            return "No content returned."

        # Remove surrounding markdown code fences if present
        cleaned = re.sub(r"^```(?:\w+)?\n|\n```$", "", raw_content.strip(), flags=re.MULTILINE)

        # Search for <final_answer>...</final_answer> content (robust to spacing)
        match = re.search(r"<final_answer>\s*(.*?)\s*</final_answer>", cleaned, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1).strip()
        else:
            return cleaned

    except Exception as e:
        return f"Error extracting final answer: {str(e)}"

def extract_skills_from_resume_summary(resume_summary: str) -> list:
    """
    Extracts the Skills section from a Semantic Kernel-formatted resume summary.

    Args:
        resume_summary (str): The full output from the resume analyzer skill, including <final_answer>.

    Returns:
        List of skills found under the "Skills" section.
    """

    # Extract the Skills line (assumes 'Skills:' is present)
    skills_match = re.search(r"Skills\s*:\s*(.+)", resume_summary, re.IGNORECASE)
    if not skills_match:
        return []

    skills_text = skills_match.group(1)

    # Split and clean up skills
    skills = [skill.strip() for skill in re.split(r",|;|\n", skills_text) if skill.strip()]
    return skills

