# 🎯 Metropolia AI Job Matcher

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-red?style=for-the-badge&logo=flask&logoColor=white)
![AI](https://img.shields.io/badge/AI-Llama%203%20(Groq)-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-POC%20Ready-success?style=for-the-badge)

> **R&D Coding Assignment:** An intelligent career assistant empowering Metropolia students to bridge the gap between their education and the Finnish job market using Large Language Models (LLMs).

---

## 🚀 Live Demo
Check out the live application hosted on Render:
**[👉 Open AI Job Matcher](https://metropolia-ai-job-matcher.onrender.com/)**

---

## 📖 The Problem (Why this tool?)
Students often face an **ill-defined problem**: *"Why is my CV not getting shortlisted?"*. Generic advice is not enough. They need personalized, data-driven feedback that compares their specific skills against actual market demands.

**This solution acts as a 24/7 AI Career Coach that:**
1.  Parses complex CV formats (PDF/DOCX).
2.  Understands the context of specific Job Descriptions (JD).
3.  Performs a "Gap Analysis" to highlight missing skills vs. matching strengths.

## ✨ Key Features

### 1. 🧠 Intelligent Context Awareness
* **Gap Analysis:** Unlike simple keyword matchers, this tool uses **Llama 3 (70b)** to understand *semantic* meaning. It knows that "React" is related to "Frontend Development" even if not explicitly stated.
* **Structured Output:** The AI engine is engineered to return strict **JSON** data, allowing for a visual dashboard instead of unstructured text blocks.

### 2. 🛡️ Smart Validation Layer (Robustness)
* **Anti-Hallucination:** Implemented a heuristic & AI-based filter to **reject non-CV documents** (e.g., course syllabi, random text, or empty files).
* **Security:** API keys are managed via environment variables and never exposed in the codebase.

### 3. 📊 Visual Feedback Dashboard
* **ATS Score:** A quantified match score (0-100%) to gamify the improvement process.
* **Actionable Advice:** Provides specific "Recommended Actions" tailored to the uploaded CV.

---

## 🛠️ Technical Stack

| Component | Technology | Role |
|-----------|------------|------|
| **Backend** | Python Flask | Handling requests, file processing, and API orchestration. |
| **AI Engine** | Groq API | Running **Llama-3-70b-versatile** for high-speed inference. |
| **Frontend** | Bootstrap 5 | Responsive, clean UI matching **Metropolia Brand Identity**. |
| **Parsing** | `pypdf` & `python-docx` | Extracting raw text from binary files. |
| **Deployment** | Gunicorn & Render | Production-ready WSGI server hosting. |

---

## ⚙️ Installation & Local Setup

To run this project locally on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/anasabdelrahim/metropolia-ai-job-matcher.git](https://github.com/anasabdelrahim/metropolia-ai-job-matcher.git)
    cd metropolia-ai-job-matcher
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**
    * Create a file named `.env` in the root folder.
    * Add your Groq API key:
      ```env
      GROQ_API_KEY=your_api_key_here
      ```

5.  **Run the App:**
    ```bash
    python app.py
    ```
    Visit `http://127.0.0.1:5000` in your browser.

---

## 🔮 R&D Roadmap (Future Improvements)

If selected for the Metropolia AI Development Project, I propose the following enhancements:

* **📈 Analytics Dashboard:** Store anonymized skill data to help the university identify curriculum gaps based on market demand.
* **🇫🇮 Finnish Language Support:** Implement a toggle to generate feedback in Finnish for local job applications.
* **🐳 Dockerization:** Containerize the application for secure and scalable deployment on Metropolia’s Azure cloud infrastructure.

---

## 👤 Author

**Anas Abdelrahim**
* **Role:** Electronics Engineering Student @ Metropolia UAS
* **Background:** 10+ Years in Data Analysis & Supply Chain Management
* **Focus:** Bridging Business Logic with Engineering Solutions.

---
*Built with ❤️ for the Metropolia R&D Recruitment Process - 2025.*