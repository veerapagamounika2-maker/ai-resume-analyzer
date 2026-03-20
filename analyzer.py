from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessor import preprocess

def get_score(resume_text, jd_text):
    # Step 1 — clean both texts
    cleaned_resume = preprocess(resume_text)
    cleaned_jd = preprocess(jd_text)

    # Step 2 — convert to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([cleaned_resume, cleaned_jd])

    # Step 3 — calculate cosine similarity
    score = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Step 4 — convert to percentage
    return round(score * 100, 2)