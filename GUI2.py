import streamlit as st
import joblib

# Page config
st.set_page_config(page_title="News Category Prediction", page_icon="📰")

# Title & description
st.title("📰 News Category Prediction")
st.write("Paste a news article below and click **Predict Category** to see the result.")

# Load model
model = joblib.load("hello.joblib")

# Input text
input_text = st.text_area(
    "Enter news text",
    placeholder="Type or paste the news content here...",
    height=200,
    max_chars=2000
)

# Predict button
if st.button("🔍 Predict Category"):
    if input_text.strip() == "":
        st.warning("Please enter some news text before predicting.")
    else:
        prediction = model.predict([input_text])
        st.success(f"📌 Predicted Category: **{prediction[0]}**")
