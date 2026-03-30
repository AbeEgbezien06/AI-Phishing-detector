# utils.py
import re

def clean_text(text):
    """Clean email text for ML model"""
    text = str(text).lower()
    text = re.sub(r"http\S+", "URL", text)  # replace links
    text = re.sub(r"[^a-zA-Z]", " ", text)  # remove special characters
    text = re.sub(r"\s+", " ", text)  # remove extra spaces
    return text.strip()