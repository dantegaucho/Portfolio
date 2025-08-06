import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Daniel Mutiso | Data Science Portfolio", layout="wide")

# --- Sidebar ---
st.sidebar.image("image\profile_photo.jpg", width=120)  # profile image
st.sidebar.title("Daniel Mutiso")
st.sidebar.markdown("A fresh graduate Data Scientist| Python | SQL | Machine Learning | Data Visualization | Data Analysis")
st.sidebar.markdown("[GitHub](https://github.com/dantegaucho)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/dmutiso/)")
st.sidebar.markdown("[Resume](https://drive.google.com/drive/folders/1GKQli3l445pGSjeTwFbF8Yceocf-AWIJ)")

# --- Main Section ---
st.title("👋 Hi, I'm Daniel Mutiso")
st.markdown("""
I'm a transitioning data scientist with a background in logistics and sales.
I enjoy building data-driven tools to solve real-world problems.
""")

# --- Projects Section ---
st.header("📊 Projects")

with st.expander("📈 Stocks Forecasting Time Series"):
    st.markdown("""
    - Built and deployed a stock price prediction model using ARIMA/SARIMA.
    - Visualized trends using matplotlib & seaborn.
    - [GitHub Repo](https://github.com/Sylvia-W-Mwangi/Stocks_forecasting_time_series)
    """)

with st.expander("📉 Customer Churn Prediction"):
    st.markdown("""
    - Used classification models to predict churn: Logistic Regression, Random Forest.
    - Emphasized data preprocessing and EDA.
    - [GitHub Repo](https://github.com/dantegaucho/Customer-churn)
    """)

with st.expander("🎬 Movie Recommendation System"):
    st.markdown("""
    - Created a content and collaborative filtering system using cosine similarity.
    - Evaluated recommendations using relevance metrics.
    - [GitHub Repo](https://github.com/dantegaucho/Movie-recommendation-system)
    """)

# --- Resume Section ---
st.header("📄 Resume")
st.markdown("You can [download my resume here](https://drive.google.com/drive/folders/1GKQli3l445pGSjeTwFbF8Yceocf-AWIJ).")  # Replace # with actual link to PDF resume

# --- Contact ---
st.header("📬 Contact Me")
st.markdown("""
- Email: danmutiso17@gmail.com  
- GitHub: [dantegaucho](https://github.com/dantegaucho)  
- LinkedIn: [Here](https://www.linkedin.com/in/dmutiso/)
""")
# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Daniel Mutiso | Powered by Streamlit")
