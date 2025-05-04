import pickle
import streamlit as st

# Page settings
st.set_page_config(page_title='📩 SMS Spam Classifier', page_icon="🦈", layout="centered")

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Title and description
st.markdown("## 🧠 SMS Spam Classifier")
st.markdown("Classify whether a message is **Spam** or **Not Spam** using a trained machine learning model.")

# User input
st.markdown("### 📥 Enter your SMS message below:")
user_input = st.text_input("", placeholder="Type an SMS message here...")

# Prediction
if user_input:
    with st.spinner("Analyzing message..."):
        text = vectorizer.transform([user_input])
        output = model.predict(text)

    if output == [0]:
        st.success("✅ This is **Not Spam**.")
    else:
        st.error("🚫 This is **Spam**.")
else:
    st.info("💡 Enter an SMS message to get a prediction.")


