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

## 🚀 Getting Started

Clone the repo and follow the [Setup Guide](#) to deploy locally or on the cloud.

```bash
git clone https://github.com/oshin18/AIInterviewAgent.git
cd ai-interview-agent
```

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
├── utils/
│   └── kernel_setup.py       # Semantic Kernel setup helper
│
├── prompts/                  # Skill prompt templates
│
├── .env                      # Environment variables (e.g., OpenAI key)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 📀 Coming Soon

- Voice-based interview simulation  
- Analytics dashboard for progress tracking  
- Integration with ATS platforms

