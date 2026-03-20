from analyzer import get_score
from parser import extract_from_docx

# Your real resume
resume_text = extract_from_docx("entry level resume.docx")

# Paste any real job description here
jd_text = """
Looking for an entry level Data Scientist or AI Engineer.
Required skills: Python, SQL, Machine Learning, LangChain, 
FAISS, Scikit-learn, Power BI, Streamlit, NLP, 
Retrieval Augmented Generation, RAG, XGBoost, Random Forest,
Pandas, NumPy, data analytics, end-to-end pipelines,
Generative AI, LLMs, prompt engineering, text embeddings,
data visualization, Matplotlib, Seaborn, Jupyter, Git, MLflow.
Freshers and entry level candidates welcome.
"""

score = get_score(resume_text, jd_text)
print("ATS Match Score:", score, "%")