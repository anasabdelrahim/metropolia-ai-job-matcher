\# 🎯 Metropolia AI Job Matcher



> \*\*R\&D Coding Assignment:\*\* An intelligent tool empowering students to bridge the gap between their CVs and the Finnish job market using Large Language Models (LLMs).



\## 📖 Overview

This application addresses an ill-defined problem many students face: \*"Why is my CV not getting shortlisted?"\*. 



Instead of generic advice, this tool acts as a \*\*24/7 Career Coach\*\*. It utilizes \*\*Groq (Llama 3)\*\* to parse student CVs (PDF/DOCX), analyze them against specific Job Descriptions, and provide data-driven feedback on skills gaps, strengths, and ATS compatibility.



\## ✨ Key Features



\* \*\*📄 Universal Parsing:\*\* Extracts text from PDF and DOCX files using `pypdf` and `python-docx`.

\* \*\*🛡️ Smart Validation Layer:\*\* Implemented a heuristic and AI-based filter to \*\*reject non-CV documents\*\* (e.g., course syllabi or random text) to ensure data integrity and save API costs.

\* \*\*⚖️ Job Description Matching:\*\* Performs a "Gap Analysis" between the student's skills and a target job post, providing a match score (0-100%).

\* \*\*📊 Visual Dashboard:\*\* Displays structured data (JSON parsed) in a user-friendly UI with color-coded scores and actionable advice.

\* \*\*🚀 Modern Stack:\*\* Built with \*\*Python Flask\*\* and \*\*Bootstrap 5\*\*.



\## 🛠️ Tech Stack



\* \*\*Backend:\*\* Python 3, Flask

\* \*\*AI/LLM:\*\* Groq API (Llama-3-70b-versatile)

\* \*\*Frontend:\*\* HTML5, CSS3, Bootstrap 5

\* \*\*Data Processing:\*\* pypdf, python-docx, json



\## ⚙️ Installation \& Setup



1\.  \*\*Clone the repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/YOUR\_USERNAME/metropolia-ai-matcher.git](https://github.com/YOUR\_USERNAME/metropolia-ai-matcher.git)

&nbsp;   cd metropolia-ai-matcher

&nbsp;   ```



2\.  \*\*Create a virtual environment (Recommended):\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   # Windows:

&nbsp;   venv\\Scripts\\activate

&nbsp;   # Mac/Linux:

&nbsp;   source venv/bin/activate

&nbsp;   ```



3\.  \*\*Install dependencies:\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



4\.  \*\*Set up Environment Variables:\*\*

&nbsp;   \* Create a `.env` file in the root directory.

&nbsp;   \* Add your API Key:

&nbsp;       ```text

&nbsp;       GROQ\_API\_KEY=your\_api\_key\_here

&nbsp;       ```



5\.  \*\*Run the application:\*\*

&nbsp;   ```bash

&nbsp;   python app.py

&nbsp;   ```



6\.  \*\*Open in Browser:\*\*

&nbsp;   Go to `http://127.0.0.1:5000`



\## 🔮 Future R\&D Roadmap



If this project moves to production, I propose the following enhancements:



1\.  \*\*📊 Analytics Dashboard:\*\* Store anonymized scores in a database to help Metropolia identify common skill gaps across student batches.

2\.  \*\*🇫🇮 Finnish Language Support:\*\* Toggle output language to support students applying for local Finnish companies.

3\.  \*\*🐳 Containerization:\*\* Dockerize the application for secure deployment on Metropolia's cloud infrastructure (Azure/AWS).



\## 👤 Author



\*\*Anas Abdelrahim\*\*

\*Electronics Engineering Student @ Metropolia UAS\*

\*Data Analysis \& Supply Chain Professional\*



---

\*Built for the Metropolia AI Development Project Application.\*

