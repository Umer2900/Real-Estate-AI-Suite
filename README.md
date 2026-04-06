# 🏠 Real Estate AI Suite

**End-to-End Machine Learning Project for Property Price Prediction, Analytics & Apartment Recommendation**

<!-- [**Live Demo**]((https://skillfit-ai.streamlit.app/) ) -->

Real Estate AI Suite is a **Streamlit-based intelligent web application** that helps users analyze real estate data, predict property prices, and discover similar apartments using machine learning.

It combines **data science + visualization + recommendation systems** into a single interactive platform.

---

## 🎥 Demo

![Demo](assets/demo.gif)

---

## 📌 Table of Contents

- [❓ Why This Project Exists]((#exists))
- [Features](#features)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)

---

## ❓ Why This Project Exists

Real estate decisions are often based on incomplete or confusing data.

- Buyers struggle to estimate **fair property prices**
- Investors lack **clear market insights**
- Finding **similar properties manually is time-consuming**

### ✅ Solution

This project provides:
- 📊 Data-driven insights  
- 🤖 ML-based price prediction  
- 🏠 Smart apartment recommendations  

All in one place.

---

## 🚀 Features

### 💰 Price Prediction
- Predict property prices using ML pipeline
- Based on:
  - Location (sector)
  - Area (built-up area)
  - Bedrooms, bathrooms, amenities
- Outputs **price range (low–high)** instead of single value

---

### 📊 Analytics Dashboard
- Interactive visualizations:
  - 🗺️ Geospatial price map
  - 📈 Area vs Price scatter plots
  - 📉 Price distribution analysis
  - 📦 BHK price range (boxplot)
  - ☁️ Feature-based WordCloud
- Linked filters for sector & property type

---

### 🤖 Apartment Recommendation System
- Suggests similar properties using:
  - Location distance
  - Feature similarity
  - Content based cosine similarity matrices
- Adjustable number of recommendations
- Clean tabular output

---

### 🎯 Smart UI/UX
- Multi-page Streamlit app
- Persistent results using session state
- Responsive column-based layout
- Interactive filters & dynamic updates

---

## 🧭 Usage

### 1. Price Predictor
- Enter property details  
- Click **Predict Price**  
- Get estimated price range  

### 2. Analysis Dashboard
- Select sector & property type  
- Explore trends and patterns  
- Understand market behavior visually  

### 3. Recommendation System
- Search properties by location & radius  
- Get nearby properties  
- Select an apartment → Get similar recommendations  

---

## ⚙️ Technologies Used

| Layer            | Technology                     |
|------------------|--------------------------------|
| Frontend         | Streamlit                      |
| Backend          | Python                         |
| Data Processing  | Pandas, NumPy                  |
| Visualization    | Matplotlib, Seaborn, Plotly    |
| Machine Learning | Scikit-learn                   |
| NLP/Features     | WordCloud                      |
| Recommendation   | Cosine Similarity              |

---

## 📂 Project Structure

REAL ESTATE PROJECT/

├── 1. Data Gathering  
├── 2. Data Cleaning  
├── 3. Feature Engineering  
├── 4. EDA  
├── 5. Handling Outliers & Missing Values  
├── 6. Feature Selection  
├── 7. Model Selection  
│
├── 8. Real Estate App  
│    ├── datasets  
│    │   ├── cosine_sim1.pkl  
│    │   ├── cosine_sim2.pkl  
│    │   ├── cosine_sim3.pkl  
│    │   ├── data_viz1.csv  
│    │   ├── feature_text.pkl  
│    │   └── location_distance.pkl  
│    │  
│    ├── models  
│    │   ├── df.pkl  
│    │   └── pipeline.pkl 
│    │
│    ├── pages  
│    │   ├── 1_Price Predictor.py  
│    │   ├── 2_Analysis App.py  
│    │   └── 3_Recommend Appartments.py  
│    │   
│    └── app.py  
│
├── assets 
├── README.md  
├── requirements.txt  
├── .gitignore  

---

## ⚡ Setup Instructions

### 🔧 Prerequisites
- Python 3.8+
- pip
- Streamlit

### 📥 1. Clone Repository
```bash
git clone https://github.com/your-username/real-estate-ai.git
cd real-estate-ai
```

### 📦 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ 3. Run the App
```bash
streamlit run app.py
```

App will open at:
http://localhost:8501

---

## ❤️ Acknowledgement

Built as an **end-to-end Data Science project** combining:
- Machine Learning  
- Data Analysis  
- Interactive Web Apps  

---

## 📬 Contact

**Mohammad Umer Jan**  
B.Tech CSE | Data Science Enthusiast  