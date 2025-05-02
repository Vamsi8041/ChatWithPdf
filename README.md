# 📄 Chat with PDF using Groq API

This is a Streamlit web application that allows you to upload any PDF document and ask questions about its content using [Groq's LLaMA models](https://groq.com). It extracts the text from your uploaded PDF, sends it along with your query to the Groq API, and returns intelligent, context-aware answers.

---

## ✨ Features

- 🔍 **PDF Text Extraction**: Uses `PyMuPDF` (`fitz`) to parse and extract content from multi-page PDFs.
- 🤖 **AI-Powered Q&A**: Leverages Groq's lightning-fast inference for LLaMA3-based large language models.
- 💬 **Interactive Chat**: Type in any question related to your PDF and get meaningful responses.
- 🔐 **Secure API Handling**: API keys are loaded from a `.env` file (not hardcoded).
- ⚡ **Built with Streamlit**: Clean, responsive UI that runs in a browser.

---

## 🚀 How to Run Locally

Follow these steps to run the app on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatwithpdf.git
cd chatwithpdf


2. Create a .env File
This file will securely store your Groq API key.

GROQ_API_KEY=your-api-key-here
⚠️ Never share this file or commit it to GitHub!

3. Install Dependencies
Make sure you’re using Python 3.8 or higher, then run:

pip install -r requirements.txt
4. Launch the App

streamlit run app.py
Open the local URL shown in your terminal to access the app in your browser.

🛠 Technologies Used
Python 3.8+

Streamlit – Frontend UI

PyMuPDF (fitz) – PDF text extraction

Groq API – LLaMA-based large language model interface

dotenv – For environment variable management

📁 Project Structure

chatwithpdf/
├── app.py              # Main Streamlit app
├── .env                # Environment file with your API key (DO NOT COMMIT)
├── .gitignore          # To exclude sensitive or unnecessary files
├── requirements.txt    # Dependencies
└── README.md           # You're reading it!
🔒 Security Note
✅ Never commit your .env file to GitHub.

✅ Use .gitignore to exclude .env and other sensitive files.

✅ Always rotate your API keys if you suspect they’ve been exposed.

🌐 Optional: Deploy on Streamlit Cloud
You can deploy this project for free using Streamlit Community Cloud.

Push your project to GitHub (excluding .env)

Go to streamlit.io/cloud and connect your repo
