# Resume Tailor AI

An AI-powered local app to **match your resume with any job description**, provide improvement suggestions, and generate tailored cover letters — all running locally with no cloud APIs.

---

## Features

- Upload your resume (PDF or TXT) and paste any job description  
- Calculate a semantic match score between your resume and the job spec  
- Get concrete suggestions to improve your resume using a local LLM (Mistral via Ollama)  
- Auto-generate a tailored cover letter based on your resume and the job description  
- Simple and interactive web UI built with Streamlit  

---

## Tech Stack

- [Streamlit](https://streamlit.io/) — frontend UI  
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) — PDF text extraction  
- [Sentence Transformers](https://www.sbert.net/) — semantic text embeddings  
- [Ollama](https://ollama.com/) — run local LLMs (Mistral model)  
- Python 3.8+

---

## Getting Started

### Prerequisites

- Install Ollama and pull the Mistral model locally:

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ollama pull mistral



### Clone this repository:
```bash
git clone https://https://github.com/qasimali000/Resume-Tailoring-Tool-Using-AI.git
cd rResume-Tailoring-Tool-Using-AI
(Optional) Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Install Python dependencies:
```bash
pip install -r requirements.txt
```


### Usage

Run the Streamlit app:

```bash
streamlit run app.py
```
Open the link provided (usually http://localhost:8501), upload your resume, paste the job description, and get your match score, improvement suggestions, and a tailored cover letter.

### Project Structure

app.py: Streamlit UI and app flow
|
utils.py: Helper functions for text extraction, scoring, and generating text with Ollama LLM
|
requirements.txt: Python dependencies

### How It Works

Extracts text from PDF or TXT resumes

Uses Sentence Transformers for semantic similarity scoring

Generates suggestions and cover letters via local Mistral LLM running on Ollama

Interactive UI via Streamlit for easy usage

### Future Improvements

Support for DOCX resume uploads

Compare multiple resumes simultaneously

More advanced LLM prompts with user-configurable tone/style

Export cover letters as PDF or email integration

## License
MIT License © 2025

## Acknowledgments
Sentence Transformers

Ollama and Mistral LLM

Streamlit community

