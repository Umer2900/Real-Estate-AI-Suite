import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"   # ✅ Full width
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #dc2626;
        color: white;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
        height: 3em;
    }
    div.stButton > button:hover {
        background-color: #b91c1c;
        color: white;
    }
    </style> 
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #
with open('models/df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('models/pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# ---------------- HEADER ---------------- #
st.markdown(
    "<h1 style='text-align:center; color:#1e40af; font-size:48px; font-weight:900;'>🏠 House Price Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#555; font-size:18px; margin-bottom:40px;'>Enter property details to get AI-powered price estimation</p>",
    unsafe_allow_html=True
)

# ---------------- FORM ---------------- #
with st.form("prediction_form"):

    st.markdown("### 🧾 Property Details")

    # ✅ Added spacing between columns
    col1, col2 = st.columns(2, gap="large")

    with col1:
        property_type = st.selectbox('Property Type', ['flat', 'house'])
        sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
        bedrooms = float(st.selectbox('Bedrooms', sorted(df['bedRoom'].unique().tolist())))
        bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].unique().tolist())))
        balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

    with col2:
        property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

        # 🎚️ Slider input
        built_up_area = float(st.slider(
            'Built Up Area (sq ft)',
            min_value=500,
            max_value=10000,
            value=1500,
            step=100
        ))

        furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
        floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🏡 Additional Features")

    # ✅ Added spacing here too
    col3, col4, col5 = st.columns(3, gap="large")

    with col3:
        servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))

    with col4:
        store_room = float(st.selectbox('Store Room', [0.0, 1.0]))

    with col5:
        study_room = float(st.selectbox('Study Room', [0.0, 1.0]))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 🔴 Red Button
    submitted = st.form_submit_button("🔴 Predict Price", use_container_width=True)

# ---------------- PREDICTION ---------------- #
if submitted:

    with st.spinner("Predicting price..."):
        data = [[property_type, sector, bedrooms, bathroom, balcony, property_age,
                 built_up_area, servant_room, store_room, study_room,
                 furnishing_type, floor_category]]

        columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                   'agePossession', 'built_up_area', 'servant room', 'store room',
                   'study room', 'furnishing_type', 'floor_category']

        one_df = pd.DataFrame(data, columns=columns)

        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = base_price - 0.23
        high = base_price + 0.23

    # ---------------- OUTPUT ---------------- #
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='color:#1e40af;'>Estimated Price Range</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style='background-color:#fee2e2; padding:25px; border-radius:12px;
        border-left:6px solid #dc2626; font-size:22px; color:#b91c1c;
        font-weight:600; text-align:center;'>
        💰 {low:.2f} Cr — {high:.2f} Cr
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("Prediction based on provided property features")