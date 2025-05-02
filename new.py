import streamlit as st
import fitz  # PyMuPDF
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ====== CONFIGURATION ======
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama3-70b-8192"
MAX_CHARS = 10000
# ===========================

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ask_groq(question, context):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Answer questions based on the provided document."},
        {"role": "user", "content": f"Document:\n{context}\n\nQuestion: {question}"}
    ]
    data = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# ========= Streamlit UI ==========
st.set_page_config(page_title="Chat with PDF (Groq)", layout="centered")
st.title("📄 Chat with PDF using Groq API")

uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF text extracted successfully.")

    question = st.text_input("💬 Ask a question about the PDF:")
    
    if question:
        with st.spinner("Thinking..."):
            truncated_text = pdf_text[:MAX_CHARS]
            answer = ask_groq(question, truncated_text)
        st.markdown("### 🤖 Answer:")
        st.write(answer)
else:
    st.info("Please upload a PDF to begin.")
