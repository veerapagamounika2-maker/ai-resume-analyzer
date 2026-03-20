import streamlit as st
from parser import extract_from_docx, extract_from_pdf
from analyzer import get_score
from skill_extractor import get_skill_gap

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")
st.title("📄 AI Resume Analyzer")
st.caption("Upload your resume and paste a job description to get your ATS score and skill gap analysis.")

# ── Resume Input ──────────────────────────────────────
st.subheader("Step 1 — Upload Your Resume")
resume_input = st.radio("Choose input method", 
                        ["Upload PDF/DOCX", "Paste Text"], 
                        horizontal=True)

resume_text = ""

if resume_input == "Upload PDF/DOCX":
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
    if resume_file:
        ext = resume_file.name.split(".")[-1].lower()
        if ext == "pdf":
            resume_text = extract_from_pdf(resume_file)
        else:
            resume_text = extract_from_docx(resume_file)
        st.success(f"✅ Resume loaded — {len(resume_text.split())} words found")
else:
    resume_text = st.text_area("Paste your resume here", height=200)

# ── JD Input ──────────────────────────────────────────
st.subheader("Step 2 — Enter Job Description")
jd_input = st.radio("Choose input method",
                    ["Paste Text", "Upload PDF/DOCX"],
                    horizontal=True)

jd_text = ""

if jd_input == "Paste Text":
    jd_text = st.text_area("Paste job description here", height=200)
else:
    jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx"])
    if jd_file:
        ext = jd_file.name.split(".")[-1].lower()
        if ext == "pdf":
            jd_text = extract_from_pdf(jd_file)
        else:
            jd_text = extract_from_docx(jd_file)
        st.success(f"✅ JD loaded — {len(jd_text.split())} words found")

# ── Analyze Button ────────────────────────────────────
st.divider()
if st.button("🔍 Analyze Resume", use_container_width=True, type="primary"):
    if not resume_text.strip():
        st.warning("Please provide your resume.")
    elif not jd_text.strip():
        st.warning("Please provide the job description.")
    else:
        with st.spinner("Analyzing..."):
            # Get ATS score
            score = get_score(resume_text, jd_text)

            # Get skill gap
            skills = get_skill_gap(resume_text, jd_text)

        # ── Results ───────────────────────────────────
        st.subheader("📊 Results")

        # ATS Score
        if score >= 70:
            st.success(f"ATS Score: {score}%")
        elif score >= 40:
            st.warning(f"ATS Score: {score}%")
        else:
            st.error(f"ATS Score: {score}%")

        st.progress(score / 100)

        st.divider()

        # Skills
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ Matched Skills")
            if skills["matched"]:
                for skill in skills["matched"]:
                    st.markdown(f"- {skill}")
            else:
                st.write("No matches found")

        with col2:
            st.markdown("### ❌ Missing Skills")
            if skills["missing"]:
                for skill in skills["missing"]:
                    st.markdown(f"- {skill}")
            else:
                st.success("No missing skills!")

        st.divider()

        # All resume skills
        st.markdown("### 📄 All Skills Found in Your Resume")
        st.write(", ".join(skills["resume_skills"]))