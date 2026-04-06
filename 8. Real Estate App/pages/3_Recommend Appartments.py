# import pickle
# import numpy as np
# import pandas as pd
# import streamlit as st

# # ---------------- PAGE CONFIG ---------------- #
# st.set_page_config(
#     page_title="Smart Apartment Recommender",
#     page_icon="🏠",
#     layout="centered"
# )

# # ---------------- LOAD DATA ---------------- #
# location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
# cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
# cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
# cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

# # ---------------- FUNCTION ---------------- #
# def recommend_properties_with_scores(property_name, top_n=5):
#     cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

#     sim_scores = list(enumerate(
#         cosine_sim_matrix[location_df.index.get_loc(property_name)]
#     ))

#     sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#     top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
#     top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

#     top_properties = location_df.index[top_indices].tolist()

#     return pd.DataFrame({
#         'PropertyName': top_properties,
#         'SimilarityScore': np.round(top_scores, 3)
#     })

# # ---------------- HEADER ---------------- #
# st.markdown(
#     "<h1 style='text-align:center; color:#1e40af; font-size:50px; font-weight:900;'>🏠 Smart Apartment Recommender</h1>",
#     unsafe_allow_html=True
# )

# st.markdown(
#     "<p style='text-align:center; color:#555; font-size:18px; margin-bottom:40px;'>Find nearby properties and get AI-powered recommendations</p>",
#     unsafe_allow_html=True
# )

# # ---------------- LOCATION SEARCH ---------------- #
# st.markdown("### 📍 Search Properties by Location")

# selected_location = st.selectbox(
#     "Select Location",
#     sorted(location_df.columns.to_list())
# )

# # 🎚️ Slider instead of number input
# st.markdown(
#     "<p style='font-size:16px; color:#555;'>🎚️ Adjust search radius</p>",
#     unsafe_allow_html=True
# )

# radius = st.slider(
#     "",
#     min_value=0.0,
#     max_value=20.0,
#     value=2.0,
#     step=0.5
# )

# if st.button("🔍 Search Nearby Properties", use_container_width=True, type="primary"):
#     if selected_location not in location_df.columns:
#         st.error("Location not found!")
#     else:
#         with st.spinner("Searching nearby properties..."):
#             result_ser = location_df[
#                 location_df[selected_location] <= radius
#             ][selected_location].sort_values()

#         st.markdown("<br>", unsafe_allow_html=True)

#         if result_ser.empty:
#             st.warning("No properties found in this radius")
#         else:
#             st.markdown(
#                 "<h3 style='color:#1e40af;'>Nearby Properties</h3>",
#                 unsafe_allow_html=True
#             )

#             result_df = result_ser.reset_index()
#             result_df.columns = ["Property", "Distance (KM)"]
#             result_df["Distance (KM)"] = result_df["Distance (KM)"].round(2)

#             st.dataframe(result_df, use_container_width=True)

# # ---------------- SPACING ---------------- #
# st.markdown("<br><br>", unsafe_allow_html=True)

# # ---------------- RECOMMENDATION ---------------- #
# st.markdown("### 🤖 Get Apartment Recommendations")

# selected_appartment = st.selectbox(
#     "Select an Apartment",
#     sorted(location_df.index.to_list())
# )

# num_recommend = st.number_input(
#     "Number of Recommendations",
#     min_value=1,
#     max_value=10,
#     value=5
# )

# if st.button("✨ Recommend Apartments", use_container_width=True, type="primary"):
#     with st.spinner("Finding best matches..."):
#         recommendation_df = recommend_properties_with_scores(
#             selected_appartment,
#             num_recommend
#         )

#     st.markdown("<br>", unsafe_allow_html=True)

#     st.markdown(
#         "<h3 style='color:#1e40af;'>Top Recommendations</h3>",
#         unsafe_allow_html=True
#     )

#     styled_df = recommendation_df.copy()
#     styled_df.index = np.arange(1, len(styled_df) + 1)

#     st.dataframe(styled_df, use_container_width=True)

#     st.caption(f"Based on: \"{selected_appartment}\"")





import pickle
import numpy as np
import pandas as pd
import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Smart Apartment Recommender",
    page_icon="🏠",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #
location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

# ---------------- FUNCTION ---------------- #
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    sim_scores = list(enumerate(
        cosine_sim_matrix[location_df.index.get_loc(property_name)]
    ))

    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    top_properties = location_df.index[top_indices].tolist()

    return pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': np.round(top_scores, 3)
    })

# ---------------- SESSION STATE ---------------- #
if "search_result" not in st.session_state:
    st.session_state.search_result = None

if "recommend_result" not in st.session_state:
    st.session_state.recommend_result = None

# ---------------- HEADER ---------------- #
st.markdown(
    "<h1 style='text-align:center; color:#1e40af; font-size:50px; font-weight:900;'>🏠 Smart Apartment Recommender</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#555; font-size:18px; margin-bottom:40px;'>Find nearby properties and get AI-powered recommendations</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# 🔷 CUSTOM GAP LAYOUT
# =========================================================
left_col, spacer, right_col = st.columns([1, 0.25, 1])

# =========================================================
# 📍 LEFT
# =========================================================
with left_col:
    st.markdown("### 📍 Search Properties by Location")

    st.markdown("<br>", unsafe_allow_html=True)

    selected_location = st.selectbox(
        "Location",
        sorted(location_df.columns.to_list()),
        key="location"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    radius = st.slider(
        "Radius (KM)",
        min_value=0.0,
        max_value=40.0,
        value=20.0,
        step=0.5,
        key="radius"
    )

    if st.button("🔍 Search", use_container_width=True, type="primary"):
        if selected_location not in location_df.columns:
            st.error("Location not found!")
        else:
            result_ser = location_df[
                location_df[selected_location] <= radius
            ][selected_location].sort_values()

            if result_ser.empty:
                st.session_state.search_result = pd.DataFrame()
            else:
                result_df = result_ser.reset_index()
                result_df.columns = ["Property", "Distance (KM)"]
                result_df["Distance (KM)"] = result_df["Distance (KM)"].round(2)

                st.session_state.search_result = result_df

    if st.session_state.search_result is not None:
        st.markdown("#### Nearby Properties")

        if st.session_state.search_result.empty:
            st.warning("No properties found in this radius")
        else:
            st.dataframe(st.session_state.search_result, use_container_width=True)

# =========================================================
# 🤖 RIGHT
# =========================================================
with right_col:
    st.markdown("### 🤖 Get Apartment Recommendations")

    st.markdown("<br>", unsafe_allow_html=True)

    selected_appartment = st.selectbox(
        "Apartment",
        sorted(location_df.index.to_list()),
        key="apartment"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    num_recommend = st.slider(
        "Number of Recommendations",
        min_value=1,
        max_value=10,
        value=5,
        key="num_rec"
    )

    if st.button("✨ Recommend", use_container_width=True, type="primary"):
        recommendation_df = recommend_properties_with_scores(
            selected_appartment,
            num_recommend
        )

        styled_df = recommendation_df.copy()
        styled_df.index = np.arange(1, len(styled_df) + 1)

        st.session_state.recommend_result = styled_df

    if st.session_state.recommend_result is not None:
        st.markdown("#### Top Recommendations")

        st.dataframe(st.session_state.recommend_result, use_container_width=True)