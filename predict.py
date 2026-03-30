# predict.py
import pickle
from utils import clean_text

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_email(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return "Phishing" if pred[0] == 1 else "Legitimate"

if __name__ == "__main__":
    email = input("Paste email text to check: ")
    print("Prediction:", predict_email(email))