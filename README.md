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
