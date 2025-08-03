import os
import re
import fitz
import tempfile
from sentence_transformers import SentenceTransformer, util
from ollama import Client

model = SentenceTransformer('all-MiniLM-L6-v2')
ollama_client = Client()

def extract_text_from_file(file):
    ext = file.name.split('.')[-1]
    if ext == "pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            tmp.close()
            doc = fitz.open(tmp.name)
            return "\n".join(page.get_text() for page in doc)
    elif ext == "txt":
        return file.read().decode('utf-8')
    else:
        return ""

def calculate_match_score(resume_text, job_text):
    resume_sentences = [s.strip() for s in resume_text.splitlines() if s.strip()]
    job_sentences = [s.strip() for s in job_text.splitlines() if s.strip()]

    resume_embedding = model.encode(resume_sentences, convert_to_tensor=True)
    job_embedding = model.encode(job_sentences, convert_to_tensor=True)

    similarity_matrix = util.cos_sim(resume_embedding, job_embedding)
    best_matches = similarity_matrix.max(dim=1).values
    score = best_matches.mean().item() * 100

    resume_keywords = set(re.findall(r"\b\w+\b", resume_text.lower()))
    job_keywords = set(re.findall(r"\b\w+\b", job_text.lower()))
    matched = list(resume_keywords.intersection(job_keywords))
    return score, matched[:10]

def generate_suggestions(resume_text, job_text):
    prompt = f"""
You are a resume expert.

Here is a resume:
{resume_text}

Here is the job description:
{job_text}

Suggest concrete improvements to the resume to better align with the job description.
"""
    response = ollama_client.chat(model="mistral", messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]

def generate_cover_letter(resume_text, job_text):
    prompt = f"""
You are a professional career assistant.

Write a tailored cover letter based on the following resume and job description:

Resume:
{resume_text}

Job Description:
{job_text}
"""
    response = ollama_client.chat(model="mistral", messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]