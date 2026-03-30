# AI Phishing Detector — Documentation

## Project Overview
The AI Phishing Detector is a clever web application that uses artificial intelligence to protect you from malicious emails. It allows users to either manually paste suspicious text into a web interface for a quick check, or securely connect directly to a Gmail inbox to automatically scan unread messages. It instantly flags potential threats so you know what is legitimate and what might be a phishing attempt.

The AI Phishing Detector is a web-based application that uses Machine Learning to analyze emails and detect whether they are:

🚨 Phishing (malicious)
✅ Legitimate (safe)


How It Works (Simple Flow)
Email → Clean Text → Vectorizer → ML Model → Result
Step-by-step:
Fetch emails from Gmail (IMAP)
Clean the text (remove noise)
Convert text → numbers (Vectorizer)
ML model predicts phishing or not

## Folder Structure
- `app.py` - The main web server file
- `email_reader.py` - Handles secure connections to Gmail
- `predict.py` - Runs predictions from the terminal
- `train.py` - Teaches the machine learning model
- `utils.py` - Prepares and cleans email text
- `requirements.txt` - Lists required external tools
- `static/` - Files sent straight to the user's browser
  - `script.js` - Makes the website interactive
  - `style.css` - Makes the website look cool
- `templates/` - HTML structure files
  - `index.html` - The main application page
- `model.pkl` & `vectorizer.pkl` - Saved "brain" data from the trained AI
- `emails.csv` - The original data used to teach the algorithm (requires user generation)

## Technology Stack
- **Python**: The core programming language used to build the logic, connect backend systems, and power the machine learning model.
- **Flask**: A lightweight, beginner-friendly web framework used to run the application online and serve web pages to the browser.
- **Scikit-learn**: A popular machine learning library used to teach the application how to spot patterns in phishing emails.
- **Pandas**: Used as a fast, flexible tool for organizing and reading the email dataset during the AI training phase.
- **HTML, CSS, JavaScript**: The essential building blocks for the website interface, customized to provide an engaging, terminal-hacker aesthetic.


## File Explanations

### `app.py`
This is the beating heart of the web application. It sets up the server and creates the roads (or "routes") that your browser talks to. It handles bringing up the homepage, receiving manual text submissions, and kicking off inbox scans. 

### `email_reader.py`
This script is basically a high-speed courier. It securely logs into a specified Gmail inbox, searches for any unread messages, extracts the subject lines and text bodies, and passes them off to the rest of the application so the AI can investigate them.

### `predict.py`
A tiny, standalone script designed for quick command-line tests. You don't need to boot up the whole web server to use this—you simply type in the terminal, paste your text, and it'll spit out a "Phishing" or "Legitimate" answer instantly.

### `train.py`
This is the teacher for our artificial intelligence. Rather than guessing, the AI learns from examples. This script reads a spreadsheet of past emails (`emails.csv`), studies what a safe email looks like versus a dangerous one, and then saves all that hard-earned knowledge into the `.pkl` files for future rapid use.

### `utils.py`
Computers are very literal, so odd spacing, weird symbols, and web addresses can confuse the AI. This file acts like an editor, cleaning up incoming text into plain, lowercase, simple words so the machine learning model can focus completely on the message content.

### `static/script.js`
This powers the dynamic parts of the website that happen without reloading the page. For instance, when you click the remote scan button, this script reaches out to the server and creates a staggered, hacker-style text animation to display the results one by one.

### `static/style.css`
This handles the look and feel of the web page. It overrides default browser styles to give the app a high-contrast, "brutalist" terminal appearance featuring a dark background, bright neon text, and blinking status indicators.

### `templates/index.html`
This is the skeleton of the webpage the user interacts with. It lays out where the title goes, where the manual submission box belongs, and where the remote scanning results should be shown.

### `requirements.txt`
A very simple to-do list for Python. When a new developer wants to run this project, rather than finding and installing each dependency like Flask or Pandas manually, they simply tell Python to install everything on this list at once.

## How It All Works Together
When a user opens the app, `app.py` loads the structure from `templates/index.html` and styles it with the rules from `static/style.css`.
 
If the user wants to test an email themselves, they paste it into the manual analysis box. The text is sent back to `app.py`, which washes the text using `utils.py`, and asks the already-taught artificial intelligence (`model.pkl`) for a verdict. It then displays if it was "Legitimate" or "Phishing".

If the user clicks "Initiate Remote Scan," the JavaScript (`static/script.js`) reaches out to the server. The server asks `email_reader.py` to quietly log into Gmail, fetch all unread emails, and evaluate them through the AI. The results are passed back to the website and animated dynamically onto the screen.

more detail about the AI-Phishing-Detector

⚙️ Installation Guide
1️⃣ Install Python

Make sure Python is installed:

python --version
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt

📧 Setting Up Email Access (IMPORTANT)
Step 1: Enable Gmail App Password
Go to:
👉 Google Account → Security → App Passwords
Generate a password like:
abcd efgh ijkl mnop

Step 2: Create .env file
In your project root:
.env
Add:
EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password

🏋️‍♂️ Train the Model
Run:
python train.py
This will:
Read emails.csv
Train the model
Save:
model.pkl
vectorizer.pkl

🔍 Test Prediction (Optional)
python predict.py
Type an email message → get prediction.

🌐 Run the Web App
python app.py

Open browser:
http://127.0.0.1:5000

🖥️ Features
✉️ 1. Manual Email Check
Paste email text
Click Check Email
Get result instantly

📥 2. Scan Inbox
Click Scan Inbox
App connects to Gmail
Fetches emails
Displays predictions

Example Output
🚨 Phishing: "Your account has been suspended..."
✅ Legitimate: "Meeting scheduled for tomorrow..."

🧰 Technologies Used
Python 
Flask → Web framework
Scikit-learn → Machine learning
TF-IDF Vectorizer → Text processing
HTML/CSS/JS → Frontend
IMAP (imaplib) → Email fetching
