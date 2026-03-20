from skill_extractor import get_skill_gap
from parser import extract_from_docx

resume_text = extract_from_docx("entry level resume.docx")

jd_text = """
Looking for Data Scientist with Python, SQL, Machine Learning,
LangChain, FAISS, Scikit-learn, Power BI, Streamlit, NLP,
RAG, XGBoost, Pandas, NumPy, Git, Tableau, Docker, AWS.
"""

result = get_skill_gap(resume_text, jd_text)

print("✅ Matched Skills:", result["matched"])
print("❌ Missing Skills:", result["missing"])
print("📄 Your Resume Skills:", result["resume_skills"])