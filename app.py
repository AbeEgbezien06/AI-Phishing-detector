# app.py
from flask import Flask, render_template, request
import pickle
from utils import clean_text
from email_reader import fetch_emails
import imaplib

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_email(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return "Phishing" if pred[0] == 1 else "Legitimate"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        email_text = request.form["email"]
        result = predict_email(email_text)
    return render_template("index.html", result=result)

# app.py
from flask import Flask, render_template, request
import pickle
from utils import clean_text
from email_reader import fetch_emails

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_email(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return "Phishing" if pred[0] == 1 else "Legitimate"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        email_text = request.form["email"]
        result = predict_email(email_text)
    return render_template("index.html", result=result)

@app.route("/scan")
def scan():
    emails = fetch_emails()

    if emails == ["ERROR_CONNECTION_FAILED"]:
        return {"results": [["Connection to Gmail failed", "Error"]]}

    results = [(e, predict_email(e)) for e in emails]
    return {"results": results}

if __name__ == "__main__":
    app.run(debug=True)