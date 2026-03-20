# 📄 AI Resume Analyzer

An intelligent resume analyzer that compares your resume
with a job description and provides ATS score + skill gap analysis.

## 📌 Features

- Upload resume as PDF or DOCX
- Paste or upload job description
- Get ATS match score (0-100%)
- See matched and missing skills
- View all skills detected in resume

## 🛠 Tech Stack

- Python
- NLP (NLTK)
- Scikit-learn (TF-IDF + Cosine Similarity)
- Streamlit
- pdfplumber
- python-docx

## ⚙️ How It Works

1. Extract text from resume PDF/DOCX
2. Clean text using NLP preprocessing
3. Convert to TF-IDF vectors
4. Calculate cosine similarity score
5. Extract and compare skills
6. Display results in Streamlit UI

## 📦 Installation

```bash
git clone https://github.com/YOURUSERNAME/ai-resume-analyzer
cd ai-resume-analyzer
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure

```
ai-resume-analyzer/
├── app.py              # Streamlit UI
├── parser.py           # PDF/DOCX text extraction
├── preprocessor.py     # NLP text cleaning
├── analyzer.py         # TF-IDF + cosine similarity
├── skill_extractor.py  # Skill gap analysis
└── requirements.txt
```

## 🧠 What I Learned

- Text extraction from PDF and DOCX files
- NLP preprocessing with NLTK
- TF-IDF vectorization and cosine similarity
- Building interactive web apps with Streamlit
- Separating code into focused modules

## 👩‍💻 Author

Mounika Veerapaga

[GitHub](https://github.com/veerapagamounika2-maker)
[Click here to view the app](https://ai-resume-analyzer-hsen8ubf2mtfd2h9qdcmnn.streamlit.app)
