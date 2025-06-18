import streamlit as st
import pandas as pd
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tempfile
import os

st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("💼 AI Resume Ranker")

st.subheader("📝 Paste Job Description")
jd_text = st.text_area("Enter the job description here", height=200)

st.subheader("📤 Upload Resumes (PDFs)")
uploaded_files = st.file_uploader("Choose PDF resumes", type=["pdf"], accept_multiple_files=True)

if st.button("🚀 Rank Resumes"):
    if not jd_text.strip():
        st.error("Please enter a job description.")
    elif not uploaded_files:
        st.error("Please upload at least one resume.")
    else:
        resume_texts = []
        resume_names = []

        for uploaded_file in uploaded_files:
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    tmp_path = tmp_file.name

                text = ""
                with pdfplumber.open(tmp_path) as pdf:
                    for page in pdf.pages:
                        text += page.extract_text() or ""

                resume_texts.append(text)
                resume_names.append(uploaded_file.name)
                os.remove(tmp_path)

            except Exception as e:
                st.error(f"Error reading {uploaded_file.name}: {e}")

        documents = [jd_text] + resume_texts
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(documents)
        scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        df = pd.DataFrame({
            "Resume": resume_names,
            "Match (%)": (scores * 100).round(2)
        }).sort_values(by="Match (%)", ascending=False)

        st.success("✅ Ranking Complete!")
        st.dataframe(df)
