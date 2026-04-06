import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="About",
    page_icon="👤",
    layout="centered"
)

# ---------------- HEADER ---------------- #
st.markdown(
    "<h1 style='text-align:center; color:#1e40af; font-size:48px; font-weight:900;'>👤 About Me</h1>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- NAME ---------------- #
st.markdown(
    "<h2 style='text-align:center; color:#111;'>Mohammad Umer Jan</h2>",
    unsafe_allow_html=True
)

# ---------------- CONTACT LINKS ---------------- #
st.markdown(
    """
    <p style='text-align:center; font-size:16px;'>
    📞 +91 8595353529 &nbsp; | &nbsp;
    📧 janumar2900@gmail.com &nbsp; | &nbsp;
    <a href="https://www.linkedin.com/in/mohammad-umer-jan-b41303261/" target="_blank">LinkedIn</a> &nbsp; | &nbsp;
    <a href="https://github.com/Umer2900" target="_blank">GitHub</a> &nbsp; | &nbsp;
    <a href="https://www.kaggle.com/mohammadumerjan" target="_blank">Kaggle</a>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# 🧾 SUMMARY
# =========================================================
st.markdown(
    "<h3 style='color:#1e40af;'>🧾 Summary</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
I am a B.Tech graduate in Computer Science Engineering from GCET Kashmir with experience in **Data Science, Machine Learning, and Data Analysis**.

Skilled in **data preprocessing, visualization, and predictive modeling** using Python, Pandas, NumPy, and Scikit-learn.

Passionate about building **data-driven solutions** and deploying **interactive ML applications** to solve real-world problems.
"""
)

# =========================================================
# 💼 EXPERIENCE
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='color:#1e40af;'>💼 Experience</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
**Data Science Intern — Sabudh Foundation (Remote)**  
*Jul 2025 – Dec 2025*

- Performed exploratory data analysis (EDA) and preprocessing to uncover patterns and trends  
- Applied supervised, unsupervised, and ensemble learning techniques  
- Worked with deep learning models including **MLP, CNN, and RNN**  
"""
)

# =========================================================
# 🛠️ SKILLS
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='color:#1e40af;'>🛠️ Technical Skills</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
**Languages**
- Python
- SQL
- C++

**Data Analysis**
- Pandas, NumPy
- Matplotlib, Seaborn
- Power BI
""")

with col2:
    st.markdown("""
**Machine Learning**
- Regression, Classification
- SVM, Random Forest, XGBoost
- Clustering

**Deep Learning**
- MLP, CNN, RNN
- NLP, LLM
""")

# =========================================================
# 🎓 EDUCATION
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='color:#1e40af;'>🎓 Education</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
**IIT Guwahati**  
Credit Linked Program in Data Science *(2025–2026)*

**GCET Kashmir**  
B.Tech in Computer Science Engineering *(CGPA: 7.1)*
"""
)

# =========================================================
# 🏆 CERTIFICATIONS
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='color:#1e40af;'>🏆 Certifications & Achievements</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
- Machine Learning Specialization — Stanford & DeepLearning.AI  
- Kaggle Notebook Expert  
"""
)

# =========================================================
# 🚀 FOOTER
# =========================================================
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)