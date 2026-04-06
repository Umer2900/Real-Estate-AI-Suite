import pickle
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Real Estate Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------- HEADER ---------------- #
st.markdown(
    "<h1 style='text-align:center; color:#1e40af; font-size:48px; font-weight:900;'>📊 Real Estate Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#555; font-size:18px; margin-bottom:40px;'>Explore property trends, pricing insights, and sector analytics</p>",
    unsafe_allow_html=True
)

# ---------------- LOAD DATA ---------------- #
new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

# ---------------- GROUP DATA ---------------- #
target_cols = ['sector', 'price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
group_df = new_df[target_cols].groupby('sector').mean(numeric_only=True).reset_index()



# =========================================================
# 🔷 1. MAP SECTION
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 🗺️ Sector Price per Sqft Geomap")

with st.container():
    fig_map = px.scatter_mapbox(
        group_df,
        lat="latitude",
        lon="longitude",
        color="price_per_sqft",
        size="built_up_area",
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        mapbox_style="open-street-map",
        height=600,
        hover_name="sector"
    )

    st.plotly_chart(fig_map, use_container_width=True)


# =========================================================
# 🔷 2. FEATURE INSIGHTS SECTION
# =========================================================

# 1. Define the Caching Function
@st.cache_data
def generate_wordcloud(text):
    if text and len(str(text).strip()) > 20:
        wc = WordCloud(
            width=500, 
            height=400, 
            background_color='white',
            stopwords={'s', 'furnished', 'available', 'property', 'features'},
            min_font_size=10
        ).generate(str(text))
        return wc
    return None


st.markdown("### 📌 Feature Insights")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")

# ☁️ COLUMN 1: WORDCLOUD (Cached)
with c1:
    st.markdown("#### ☁️ Overall Feature Wordcloud")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # This call is now lightning fast because of @st.cache_data
    cloud_obj = generate_wordcloud(feature_text)

    if cloud_obj:
        fig_wc, ax_wc = plt.subplots()
        ax_wc.imshow(cloud_obj, interpolation='bilinear')
        ax_wc.axis("off")
        plt.tight_layout(pad=0)
        st.pyplot(fig_wc)
    else:
        st.warning("Overall feature data is currently unavailable.")


# 📈 COLUMN 2: AREA VS PRICE
with c2:
    st.markdown("#### 📈 Area vs Price")
    st.markdown("<br>", unsafe_allow_html=True)
    
    scat_c1, scat_c2 = st.columns(2)
    with scat_c1:
        sector_options = sorted(new_df['sector'].unique().tolist())
        sector_options.insert(0, 'overall')
        selected_sector = st.selectbox('Select Sector', sector_options, key="scat_sector_val")
        
    with scat_c2:
        selected_type = st.selectbox('Property Type', ['both', 'flat', 'house'], key="scat_type_val")
        
    # --- Filtering Logic ---
    filtered_scat_df = new_df.copy()

    if selected_sector != 'overall':
        filtered_scat_df = filtered_scat_df[filtered_scat_df['sector'] == selected_sector]

    if selected_type == 'both':
        filtered_scat_df = filtered_scat_df[filtered_scat_df['property_type'].isin(['flat', 'house'])]
    else:
        filtered_scat_df = filtered_scat_df[filtered_scat_df['property_type'] == selected_type]
    
    # --- Plotting ---
    if not filtered_scat_df.empty:
        fig_scat, ax_scat = plt.subplots()
        sns.scatterplot(
            data=filtered_scat_df, 
            x='built_up_area', 
            y='price', 
            hue='bedRoom', 
            style='property_type' if selected_type == 'both' else None,
            palette='viridis',
            ax=ax_scat
        )
        ax_scat.set_title(f"Sector: {selected_sector.upper()} | Type: {selected_type.upper()}")
        st.pyplot(fig_scat)
    else:
        st.info(f"No listings found for this selection.")



# =========================================================
# 🔷 3. DISTRIBUTIONS
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 📊 Price Analysis")
st.markdown("<br>", unsafe_allow_html=True)

c3, c4 = st.columns(2, gap="large")

# COLUMN 1: 📉 Price Distribution ----
with c3:
    st.markdown("#### 📉 Price Distribution")

    fig_dist, ax_dist = plt.subplots()

    sns.histplot(
        data=new_df[new_df['property_type'] == 'house'],
        x='price',
        label='House',
        kde=True,
        ax=ax_dist,
        element="step"
    )

    sns.histplot(
        data=new_df[new_df['property_type'] == 'flat'],
        x='price',
        label='Flat',
        kde=True,
        ax=ax_dist,
        element="step"
    )

    ax_dist.legend()
    st.pyplot(fig_dist)

# COLUMN 2 :BHK Price Range ----
with c4:
    st.markdown("#### 🏠 BHK Price Range")

    fig_box, ax_box = plt.subplots()

    sns.boxplot(
        data=new_df[new_df['bedRoom'] <= 4],
        x='bedRoom',
        y='price',
        ax=ax_box
    )

    st.pyplot(fig_box)


# =========================================================
# 🔷 4. BHK DISTRIBUTION
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🧩 BHK Distribution")

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector = st.selectbox(
    'Select Sector',
    sector_options,
    key="pie_sector"
)

if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom')
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

st.plotly_chart(fig2, use_container_width=True)