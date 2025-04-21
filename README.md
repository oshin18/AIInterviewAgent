# 🧠 AI Interview Agent

**AI Interview Agent** is a smart, modular assistant designed to help job seekers prepare for interviews with personalized mock sessions based on their **resume** and the **job description** of their target role.

Powered by **Azure OpenAI** and **Semantic Kernel**, this app analyzes a candidate’s profile, matches it with job requirements, generates tailored interview questions, evaluates responses, and provides actionable feedback — all in one streamlined tool.

---

## 🔍 Features

- **Resume Analyzer**  
  Parses and summarizes key insights from resumes using natural language understanding.

- **Job Description Analyzer**  
  Extracts required skills, responsibilities, and key expectations from job postings.

- **Question Generator**  
  Creates interview questions tailored to the candidate's experience and job requirements.

- **Answer Evaluator**  
  Analyzes candidate responses for clarity, relevance, and alignment with role expectations.

- **Feedback Provider**  
  Offers constructive, context-aware feedback to help candidates improve their answers.

- **Fully Modular**  
  Each component is built as a Semantic Kernel plugin, making it easy to extend, swap, or enhance.

---

## 💼 Ideal For

- Job seekers aiming for technical or behavioral interviews  
- Career coaches looking for smart tools to assist their clients  
- Developers building personalized AI interview prep platforms

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)  
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)  
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel)  
- Python 3.10+

---

## 📉 Architecture Overview

```plaintext
            +---------------------+
            |   Streamlit Frontend|
            +----------+----------+
                       |
                       v
         +-------------+--------------+
         |        app.py (Main UI)    |
         +-------------+--------------+
                       |
                       v
     +-----------------+--------------------+
     |   Semantic Kernel Skills (Plugins)   |
     |   - ResumeAnalyzerSkill              |
     |   - JDAnalyzerSkill                  |
     |   - QuestionGeneratorSkill           |
     |   - AnswerEvaluatorSkill             |
     +-----------------+--------------------+
                       |
                       v
               +-------+-------+
               |  Azure OpenAI |
               +---------------+
```

---

## 📂 Code Layout

```plaintext
ai-interview-agent/
│
├── app.py                    # Main Streamlit application
│
├── skills/
│   ├── resume_analyzer/      # Resume summarization skill
│   ├── jd_analyzer/          # Job description analysis skill
│   ├── question_generator/   # Dynamic question generation skill
│   └── answer_evaluator/     # Answer evaluation and feedback
│
├── utils/                    # Semantic Kernel setup helper
│
├── sample-docs/              # Example resume and job description files
│
├── .env                      # Environment variables (e.g., OpenAI key)
├── requirements.txt          # Python dependencies
└── README.md                 # You're here!
```

---

## 🚀 Getting Started

Clone the repo and follow the [Setup Guide](#setup-guide) to deploy locally or on the cloud.

```bash
git clone https://github.com/oshin18/AIInterviewAgent.git
cd ai-interview-agent
```

---

## ⚙️ Setup Guide

### 🔧 Prerequisites

- Python 3.9+
- Azure OpenAI Service (with GPT-4o or GPT-4 deployed)
- Get your Azure credentials from the [Azure Portal](https://portal.azure.com/):
  - `AZURE_OPENAI_APIKEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_DEPLOYMENT`

### 🛠️ Installation

```bash
# Clone the repository
$ git clone https://github.com/your-username/ai-interview-agent.git
$ cd ai-interview-agent

# (Optional) Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
$ pip install -r requirements.txt

# Set up environment variables
# Copy the example .env file and update it with your credentials
$ cp .env.example .env

# Open the .env file and add your Azure OpenAI API credentials
$ nano .env  # or use your preferred text editor

# Inside the .env file, add the following:
# AZURE_OPENAI_APIKEY=your-api-key
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
# AZURE_OPENAI_DEPLOYMENT=gpt-4  # or your deployment name

# Run the Streamlit application
$ streamlit run app.py
```

---

## 📀 Coming Soon

- Voice-based interview simulation  
- Analytics dashboard for progress tracking  
- Integration with ATS platforms
```
