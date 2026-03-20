# Common tech skills list
SKILLS_LIST = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "langchain", "faiss", "openai", "streamlit",
    "power bi", "pandas", "numpy", "scikit-learn", "xgboost",
    "random forest", "matplotlib", "seaborn", "git", "mlflow",
    "generative ai", "llm", "rag", "prompt engineering",
    "data analysis", "feature engineering", "tableau",
    "tensorflow", "keras", "pytorch", "docker", "aws",
    "mysql", "sql server", "jupyter", "data visualization"
]

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []
    for skill in SKILLS_LIST:
        if skill in text_lower:
            found_skills.append(skill)
    return found_skills

def get_skill_gap(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = [s for s in jd_skills if s in resume_skills]
    missing = [s for s in jd_skills if s not in resume_skills]

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched": matched,
        "missing": missing
    }