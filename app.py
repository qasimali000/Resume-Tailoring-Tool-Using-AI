import streamlit as st
from utils import extract_text_from_file, calculate_match_score, generate_suggestions, generate_cover_letter

st.set_page_config(page_title="Resume Tailor AI", layout="centered")

st.title("📄 Resume Tailor AI")
st.caption("Upload your resume and paste a job description to get match score, suggestions, and a custom cover letter.")

uploaded_file = st.file_uploader("Upload your Resume (.pdf or .txt)", type=["pdf", "txt"])
job_description = st.text_area("Paste the Job Description here", height=250)

if uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_file(uploaded_file)
        match_score, matched_keywords = calculate_match_score(resume_text, job_description)
        suggestions = generate_suggestions(resume_text, job_description)
        cover_letter = generate_cover_letter(resume_text, job_description)

    st.subheader("✅ Match Score")
    st.metric("Score", f"{match_score:.2f}%", delta=None)
    st.markdown(f"**Matched Keywords:** {', '.join(matched_keywords)}")

    st.subheader("🛠 Suggestions for Improvement")
    st.write(suggestions)

    st.subheader("📬 Tailored Cover Letter")
    st.code(cover_letter, language="markdown")