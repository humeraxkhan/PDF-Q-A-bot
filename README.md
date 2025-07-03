# PDF-Q-A-bot
# 🤖 Chat with Your PDF

An intelligent Streamlit web app that allows you to upload any PDF and ask natural language questions about its content. Powered by **LangChain**, **FAISS**, and **LLMs** (like OpenAI GPT-3.5), this tool provides contextual answers by combining semantic search with real-time language generation.

---

## 🚀 Features

- 📄 Upload and parse any PDF (supports large files up to 200MB)
- 🔍 Chunked semantic search using Sentence-BERT
- 🧠 Contextual question answering via LLM (OpenAI GPT-3.5 or other)
- 🗣️ Natural, chat-like interaction
- 💾 Efficient vector search with FAISS
- 🌐 Streamlit web interface – no code needed

---

## 🖼️ Demo

![demo-gif](https://user-images.githubusercontent.com/demo-placeholder.gif)  
_Try asking: “What is the cancellation policy mentioned in the document?”_

---

## 📁 Project Structure

```bash
📂 project-root/
│
├── app.py               # Streamlit UI
├── chatbot.py           # LangChain logic and model setup
├── requirements.txt     # All required Python packages
└── README.md            # This file
