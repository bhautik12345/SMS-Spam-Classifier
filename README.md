# 📩 SMS Spam Classifier 🦈

A simple and interactive web app built with **Streamlit** that classifies SMS messages as **Spam** or **Not Spam** using a trained machine learning model. It uses natural language processing techniques (TF-IDF vectorization) and a Naive Bayes classifier to make accurate predictions.

---

## 🚀 Features

- 🔍 Real-time SMS classification
- 🧠 Trained on a labeled spam dataset
- 🗂️ Uses `TfidfVectorizer` for text preprocessing
- ✅ Interactive and user-friendly web interface with Streamlit

---

## 🧪 Example Predictions

| Input Message                                  | Output        |
|-----------------------------------------------|---------------|
| "Congratulations! You've won a free iPhone!"  | 🚫 Spam       |
| "Hey, are we still on for dinner tonight?"    | ✅ Not Spam   |

---

🤖 Technologies Used
  - Python
  - Scikit-learn
  - Streamlit
  - Natural Language Processing (NLP)

## 🛠️ Installation

1. **Clone this repository**:
```bash
git clone https://github.com/bhautik12345/SMS-Spam-Classifier.git
cd sms-spam-classifier

2. **Install dependencies**:
```bash
pip install -r requirements.txt

3. **Run the app**:
```bash
streamlit run inference.py



