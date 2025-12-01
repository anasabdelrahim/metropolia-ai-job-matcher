import os
import json
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import pypdf
from docx import Document

# Load environment variables
load_dotenv()

app = Flask(__name__)

# --- CONFIGURATION ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file, filename):
    text = ""
    extension = filename.rsplit('.', 1)[1].lower()
    try:
        if extension == 'pdf':
            pdf_reader = pypdf.PdfReader(file)
            for page in pdf_reader.pages:
                text_page = page.extract_text()
                if text_page: text += text_page + "\n"
        elif extension == 'docx':
            doc = Document(file)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        elif extension == 'txt':
            text = file.read().decode('utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return text

def analyze_cv_with_groq(cv_text, job_desc=None):
    """
    Analyzes CV. If job_desc is provided, performs a GAP ANALYSIS.
    """
    
    # 1. Python Validation Layer (CV Check)
    bad_keywords = ["learning objectives", "ects credits", "teaching methods", "course unit", "evaluation criteria"]
    if any(k in cv_text.lower() for k in bad_keywords):
        return {
            "score": 0,
            "summary": "This document appears to be a Course Syllabus, NOT a personal CV.",
            "strengths": [],
            "weaknesses": ["Document contains academic course terms (e.g. 'ECTS')."],
            "improvements": ["Please upload a valid personal CV."]
        }

    # 2. Dynamic Prompt Construction
    if job_desc and len(job_desc.strip()) > 50:
        # --- MODE A: JOB MATCHING (مقارنة الوظيفة) ---
        system_prompt = f"""
        You are an expert ATS (Applicant Tracking System). 
        Task: Compare the Candidate's CV against the provided JOB DESCRIPTION (JD).
        
        JOB DESCRIPTION:
        "{job_desc[:2000]}"... (truncated)

        Calculate a MATCH SCORE (0-100) based on how well the CV fits this specific JD.
        - Strengths = Skills the candidate HAS that match the JD.
        - Weaknesses = Critical skills/keywords in the JD that are MISSING from the CV.
        - Improvements = Specific advice to tailor the CV for THIS job.
        
        Return JSON ONLY. Structure:
        {{ "score": int, "summary": "string", "strengths": [], "weaknesses": [], "improvements": [] }}
        """
    else:
        # --- MODE B: GENERAL AUDIT (تحليل عام) ---
        system_prompt = """
        You are an expert Tech Recruiter. Analyze this CV generally.
        Identify missing keywords, weak verbs, and formatting issues.
        Return JSON ONLY. Structure:
        { "score": int, "summary": "string", "strengths": [], "weaknesses": [], "improvements": [] }
        """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"CANDIDATE CV:\n{cv_text}"}
            ],
            temperature=0.1,
            max_tokens=1024
        )
        
        content = response.choices[0].message.content
        if "```" in content:
            content = content.replace("```json", "").replace("```", "")
        
        return json.loads(content.strip())

    except Exception as e:
        print(f"AI Error: {e}")
        return {
            "score": 0,
            "summary": "Error parsing AI response.",
            "strengths": [],
            "weaknesses": [],
            "improvements": ["System Error."]
        }

@app.route('/', methods=['GET', 'POST'])
def home():
    feedback = None
    cv_text = ""
    job_desc = ""
    error_msg = None
    
    if request.method == 'POST':
        # Get Job Description Text
        job_desc = request.form.get('job_desc', '')

        # Handle CV File
        if 'cv_file' in request.files and request.files['cv_file'].filename != '':
            file = request.files['cv_file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                extracted = extract_text_from_file(file, filename)
                if extracted and len(extracted.strip()) > 50:
                    cv_text = extracted
                else:
                    error_msg = "Could not read text from file."
            else:
                error_msg = "Invalid file type. PDF/DOCX only."

        # Handle CV Paste
        if not cv_text and 'cv_text' in request.form:
            cv_text = request.form.get('cv_text')

        # Process
        if cv_text and len(cv_text.strip()) > 20:
            feedback = analyze_cv_with_groq(cv_text, job_desc)
        elif not error_msg and request.method == 'POST':
            error_msg = "Please upload a CV to start."

    return render_template('index.html', feedback=feedback, cv_text=cv_text, job_desc=job_desc, error_msg=error_msg)

if __name__ == '__main__':
    app.run(debug=True)