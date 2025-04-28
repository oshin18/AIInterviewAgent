# Import required libraries for file processing and text extraction
import docx2txt                       # For extracting text from Word documents
import PyPDF2                         # For reading and extracting text from PDFs
import re                             # For regular expression-based text processing
from semantic_kernel.contents.chat_message_content import ChatMessageContent  # For working with AI response content

# Function to extract text from uploaded files (PDF, DOCX, or TXT)
def extract_text(uploaded_file):
    """
    Extracts plain text from a file uploaded via Streamlit.

    Supports PDF, Word (DOCX), and plain text files.

    Args:
        uploaded_file: The uploaded file object.

    Returns:
        str: Extracted text from the file.
    """
    if uploaded_file.type == "application/pdf":
        # For PDFs, read all pages and join their extracted text
        reader = PyPDF2.PdfReader(uploaded_file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        # For Word documents, use docx2txt to process and extract text
        return docx2txt.process(uploaded_file)
    else:
        # For plain text files or fallback, decode the byte content
        return str(uploaded_file.read(), "utf-8")

# Function to extract the final answer enclosed in <final_answer> tags from an AI result
def extract_final_answer_from_kernel_result(result: ChatMessageContent) -> str:
    """
    Parses and extracts the final answer content from a Semantic Kernel AI response,
    optionally wrapped in <final_answer> tags.

    Args:
        result (ChatMessageContent): The AI-generated response content.

    Returns:
        str: Cleaned final answer text, or an error message if extraction fails.
    """
    try:
        # Prefer the first item text if available, otherwise fall back to inner_content
        raw_content = result.items[0].text if result.items and result.items[0].text else result.inner_content

        # Return a fallback message if no content is available
        if not raw_content:
            return "No content returned."

        # Remove surrounding markdown code fences (e.g., ```text```) if present
        cleaned = re.sub(r"^```(?:\w+)?\n|\n```$", "", raw_content.strip(), flags=re.MULTILINE)

        # Extract text between <final_answer> and </final_answer> tags
        match = re.search(r"<final_answer>\s*(.*?)\s*</final_answer>", cleaned, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1).strip()
        else:
            # If tags not found, clean up any unclosed tags and return content
            cleaned = cleaned.replace('<final_answer>', '')
            return cleaned

    except Exception as e:
        # Return error message if something goes wrong during processing
        return f"Error extracting final answer: {str(e)}"
