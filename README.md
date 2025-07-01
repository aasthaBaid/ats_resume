# 🤖 ATS Resume Analyzer with Gemini + Streamlit

This is an AI-powered Resume Analyzer built with **Streamlit**, integrated with **Google's Gemini API**, designed to simulate an Applicant Tracking System (ATS). You upload your resume as a PDF, and the app intelligently parses, visualizes, and evaluates your resume content using Gemini's capabilities.

---

## ✨ Features

- 📄 **Upload and parse resumes (PDF)**
- 🧠 **Analyze your resume using Gemini 1.5 Pro or Flash**
- 🖼️ **Converts resume to image for vision-based models**
- 🤖 **Natural language analysis with prompts**
- 🧪 Built for experimentation and prototyping

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ats-resume-gemini.git
cd ats-resume-gemini
````

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Poppler (Required for PDF to Image conversion)

#### macOS (using Homebrew)

```bash
brew install poppler
```

#### Windows

Download from: [https://github.com/oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows)
Add the `bin/` folder to your system PATH.

---

## 🔑 Set up your Gemini API Key

Create a `.env` file in the root directory:

```env
GOOGLE_GEMINI_API=your_api_key_here
```

> Get your API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 🖥️ Run the App

```bash
streamlit run app.py
```

---

## ⚠️ Common Issues

* **`PDFInfoNotInstalledError`**
  → Install `poppler` and make sure it's in your system's PATH.

* **`404 Model Not Found`**
  → You're using a deprecated model. Use `"gemini-1.5-pro"` or `"gemini-1.5-flash"`.

* **`429 Resource Exhausted`**
  → You’ve hit your quota. Use `gemini-1.5-flash`, reduce prompt size, or enable billing.

---

## 🧠 Model Info

This app uses the following Gemini models:

* **`gemini-2.5-pro`** – High-quality, slower, more costly
* **`gemini-2.5-flash`** – Fast, cost-effective, perfect for quick feedback

You can switch models in the code depending on your needs or quota status.

---

## 📁 Folder Structure

```
ats-resume-gemini/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env                    # Gemini API key (not committed)
└── assets/                 # Any logos or UI files (optional)
```

---

## 🙋‍♀️ Why this project?

Hiring today is hard. Candidates are filtered out by bots before humans ever see them. This project helps you:

* Understand how ATS systems "read" your resume
* Get feedback powered by Google's cutting-edge AI
* Learn how your resume might perform before submitting it

---
