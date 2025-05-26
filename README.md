# 📚 RAGIFY: Retrieve-Augmented Generation System

RAGIFY is a smart, modular Retrieval-Augmented Generation (RAG) system that allows you to upload a **PDF** or provide a **website URL**, and then ask questions directly to the AI chatbot powered by Google's **Gemini model**.

---

## 🚀 Features

- 🔍 **Document Understanding** – Upload a PDF and extract relevant chunks for semantic search.
- 🌐 **Website Scraping** – Provide any website URL and RAGIFY will extract and embed the content.
- 🧠 **Conversational AI** – Ask questions based on the uploaded document or website using a Gemini-powered chatbot.
- ⚡ **FastAPI Backend** – Clean and powerful API endpoints ready to deploy.
- 💡 **Frontend UI** – Simple HTML/CSS/JavaScript interface for interaction.
- ✅ **Contextual Memory** – Uses vector similarity search to retrieve top relevant text chunks (`k=2` or configurable).

---

## 📬 API Endpoints

| Endpoint           | Method | Description                                      |
|--------------------|--------|--------------------------------------------------|
| `/hello`           | GET    | Simple test endpoint                             |
| `/upload_document` | POST   | Upload a PDF file                                |
| `/embed_pdf`       | POST   | Embed uploaded PDF content into vector DB        |
| `/embed_website`   | POST   | Submit a website URL for scraping and embedding  |
| `/chat`            | POST   | Ask questions after document/website embedding   |
