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

---

## 🔧 Installation

Follow the steps below to install and run RAGIFY on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/anonhossain/RAGIFY.git
cd RAGIFY
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3.  Make .env file and add the Credentials 

```bash
PINECONE_API_KEY = "Your_API_Key"

GOOGLE_API_KEY = "Your_API_Key"
MODEL = "Preferred model,  here gemini-1.5-flash has been used"

INDEX_NAME = "Your_Index_Name"
PDF_FILE = "./document/"
PDF_PATH = "document/document.pdf"

DIMENSION = Select a dimentsion 768 Has been used here
METRIC = "Your_Matric" (Cosine has been used)
CLOUD = "cloud_name" (aws has been used)
REGION = "Select Region" (us-east-1 has been used)
EMBED_MODEL_NAME = "Select Embed Model" (llama-text-embed-v2 has been used)
```

---

##📡 API Output

Below are sample outputs returned by various API endpoints.
API List:
![APi List](https://github.com/anonhossain/RAGify/blob/main/screenshot/API%20List.PNG)


- `/upload_document` → `{"message": "Document uploaded successfully"}`
![Upload Document](https://github.com/anonhossain/RAGify/blob/main/screenshot/Submit%20pdf.PNG)

- `/embed_pdf` → `{"status": "Embedding completed"}`
![Embed PDF](https://github.com/anonhossain/RAGify/blob/main/screenshot/Embed%20pdf%20and%20upload%20to%20Pinecone.PNG)
![Update in Pinecone](https://github.com/anonhossain/RAGify/blob/main/screenshot/update%20in%20Pinecone.PNG)

- `/embed_website` → `{"status": "Website embedded successfully"}`
![Embed PDF](https://github.com/anonhossain/RAGify/blob/main/screenshot/web_embed.PNG)
![Embed in pinecone] (https://github.com/anonhossain/RAGify/blob/main/screenshot/update%20web%20pinecone.PNG)
- `/chat` → `{"response": "Here is the answer to your question..."}`
![[chat response](https://github.com/anonhossain/RAGify/blob/main/screenshot/chat.PNG)]



 
 
