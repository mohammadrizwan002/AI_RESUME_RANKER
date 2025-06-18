💼 AI Resume Ranker – Elevate Labs AIML Internship Project(2025)

This is my official internship project of the "AIML Internship Program" at "Elevate Labs".

This tool intelligently ranks resumes based on their similarity to a job description using natural language processing techniques.

---

🧠 Objective

To develop a smart, real-world application that automates the process of resume screening using TF-IDF and cosine similarity.

---

🧰 Tools Used

- Python  
- pdfplumber – for extracting text from PDF resumes  
- Scikit-learn – for TF-IDF vectorization & cosine similarity  
- Streamlit – for building the web app UI  
- Google Colab – for backend notebook development

---

🗂️ Folder Structure

```
AI_RESUME_RANKER/
├── resume_ranker.ipynb         # Jupyter notebook for core logic
├── ranked_output.csv           # Output file with match scores
├── project_report.pdf          # Final report for submission
├── README.md                   # This file
└── streamlit_app/
    └── app.py                  # Final working Streamlit application
```

---

⚙️ How It Works

1. The user pastes a job description
2. Uploads one or more PDF resumes
3. The system:
   - Extracts text from each resume using 'pdfplumber'
   - Vectorizes the text using 'TfidfVectorizer'
   - Compares with JD using cosine similarity
4. Shows a table of resumes ranked by match percentage

---

📊 Sample Output

| Resume             | Match (%) |
|--------------------|-----------|
| rizwan_resume.pdf  | 84.73     |
| sabiha_resume.pdf  | 72.15     |

---

🚀 How to Run the Web App Locally

```bash
# Install dependencies
pip install streamlit pdfplumber scikit-learn pandas

# Navigate to app folder
cd streamlit_app

# Run the Streamlit app
streamlit run app.py
```

---

📦 Project Deliverables

- ✅ `resume_ranker.ipynb` – model logic notebook  
- ✅ `app.py` – Streamlit user interface  
- ✅ `ranked_output.csv` – sample result  
- ✅ `project_report.pdf` – final report for Elevate Labs  
- ✅ `README.md` – project overview  

---

🧑‍💻 Author

**Mohammad Rizwan**  
AIML Intern – Elevate Labs  
Year: 2025  
