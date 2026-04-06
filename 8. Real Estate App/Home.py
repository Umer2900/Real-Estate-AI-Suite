import streamlit as st

st.set_page_config(page_title="Real Estate AI Suite", page_icon="🏠")

# ---------------- HEADER ---------------- #
st.markdown(
    "<h1 style='text-align:center; color:#1e40af; font-size:55px; font-weight:900;'>🏠 Real Estate AI Suite</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#555; font-size:20px; margin-bottom:40px;'>"
    "Your one-stop solution for smart property insights, predictions, and recommendations"
    "</p>",
    unsafe_allow_html=True
)

# ---------------- INTRO ---------------- #
st.markdown("### 👋 Welcome")

st.write(
"""
This application leverages **Machine Learning and Data Analytics** to help users make 
better real estate decisions. Whether you are a buyer, investor, or analyst, 
this platform provides powerful tools to explore, predict, and recommend properties.
"""
)

# ---------------- FEATURES ---------------- #
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🚀 Key Features")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("#### 💰 Price Predictor")
    st.write(
        """
        - Predict property prices using ML models  
        - Based on features like location, size, amenities  
        - Get accurate price range instantly  
        """
    )

with col2:
    st.markdown("#### 📊 Analysis Dashboard")
    st.write(
        """
        - Visualize real estate trends  
        - Sector-wise price insights  
        - Area vs price relationships  
        - Distribution & comparisons  
        """
    )

with col3:
    st.markdown("#### 🤖 Smart Recommendations")
    st.write(
        """
        - Find similar apartments  
        - Location-based search  
        - AI-powered similarity scoring  
        - Discover best matching properties  
        """
    )

# ---------------- HOW TO USE ---------------- #
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🧭 How to Use")

st.write(
"""
1. **Go to Price Predictor** → Enter property details to estimate price  
2. **Explore Analysis App** → Understand market trends visually  
3. **Use Recommendation System** → Find similar or nearby properties  
"""
)

# ---------------- FOOTER ---------------- #
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:#888;'>Built with ❤️ using Streamlit | Machine Learning Project</p>",
    unsafe_allow_html=True
)