# train.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from utils import clean_text

# Load dataset
data = pd.read_csv("emails.csv")  # Make sure you create this CSV

# Clean text
data['clean_text'] = data['text'].apply(clean_text)

# Features
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(data['clean_text'])
y = data['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model & vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved!")