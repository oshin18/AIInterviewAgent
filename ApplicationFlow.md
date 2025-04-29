# 📘 ApplicationFlow

## 🎯 Purpose
This document outlines the end-to-end application flow for the **Interview Ignitor AI Agent**, guiding candidates from uploading their resume and job description to preparing for interviews using AI-powered tools.

---

## 🧭 Application Flow

### 1. 🏠 Homepage – Upload Resume and Job Description
- The user lands on the homepage.
- User uploads their **Resume (PDF/Docx)** and **Job Description (PDF/Docx)** using a drag-and-drop or file picker interface.
- Files are submitted to the backend for processing.

![HomePage](docs/ApplicationFlow/1_Homepage.png)

---

### 2. 🤖 Document Analysis by Interview Ignitor AI Agent
- Once uploaded, the **AI Agent** processes both documents.
- It extracts key information such as:
  - Candidate’s experience, skills, and education from the resume.
  - Job requirements, qualifications, and role expectations from the job description.

![Analyze Documents](docs/ApplicationFlow/2_AnalyzeDocs.png)

---

### 3. 📝 Summary Generation
- A summary is displayed to the user:
  - **Resume Summary**
  - **Job Description Summary**
  - **Identified Resume Skills**

![Documents Processed](docs/ApplicationFlow/3_DocsProcessed.png)

---

### 4. 📄 Cover Letter Generator
- User clicks on **“Cover Letter Generator”** in the sidebar.
- The AI Agent uses the generated summaries and skills to craft a **personalized cover letter** tailored to the job.

![Generate Cover Letter](docs/ApplicationFlow/4_GenerateCoverLetter.png)

![Cover Letter Generated](docs/ApplicationFlow/5.1_CoverLetterGenerated.png)

![Cover Letter Generated](docs/ApplicationFlow/5.2_CoverLetterGenerated.png)

---

### 5. 🧠 Mock Interview Bot
- User navigates to **“Mock Interview Bot”** in the sidebar.
- The bot initiates the mock interview experience.

![Mock Interview](docs/ApplicationFlow/6_MockInterview.png)

---

### 6. ❓ Question & Answer Interaction
- The AI generates a question:
  - Based on **Resume & Job Description** or just **Resume Skills** (randomly).
- Candidate submits an answer in the text box.

![Mock Interview Answer](docs/ApplicationFlow/7_MockInterviewAnswer.png)

---

### 7. 🧪 Evaluation
- The AI evaluates the submitted answer.
- It provides:
  - A **score from 1 to 10**
  - Constructive **feedback**
  - A **sample ideal answer** for learning purposes.

![Mock Interview Evaluation](docs/ApplicationFlow/8_EvaluatingAnswer.png)

![Feedback And Sample Answer](docs/ApplicationFlow/9_FeedbackAndSampleAnswer.png)

---

### 8. 🔁 Continue Mock Interview
- Candidate clicks **“Next Question”** to proceed.
- Steps 6–7 repeat, allowing continuous practice.

![Generate Next Question](docs/ApplicationFlow/10_GenerateNextQuestion.png)

![Mock Interview Continues](docs/ApplicationFlow/11_QuestionGenerated.png)

---

## ✅ Summary
The application provides a seamless experience for job seekers, combining resume analysis, personalized content generation, and interactive mock interviews — all driven by the Interview Ignitor AI Agent.
