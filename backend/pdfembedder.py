# backend/pdf2vector.py

import os
import PyPDF2
from dotenv import load_dotenv
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec
import pinecone

# Load environment variables
load_dotenv()

# Environment variables
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
INDEX_NAME = os.getenv('INDEX_NAME')
PDF_PATH = os.getenv("PDF_PATH")
DIMENSION = os.getenv("DIMENSION")
METRIC = os.getenv("METRIC")
CLOUD = os.getenv("CLOUD")
REGION = os.getenv("REGION")
EMBED_MODEL = os.getenv("EMBED_MODEL")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if it doesn't exist
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=DIMENSION,
        metric=METRIC,
        spec=ServerlessSpec(
            cloud=CLOUD,
            region=REGION,
            embed={
                "model": EMBED_MODEL,
                "field_map": {
                    "text": "text"
                }
            }
        )
    )

index = pc.Index(INDEX_NAME)

def embed_pdf():
    try:
        # Step 1: Extract text from the PDF
        with open(PDF_PATH, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                #print(f"Page {i + 1} extracted text: {page_text}")
                if page_text:
                    full_text += page_text

        print(f"Total characters extracted: {len(full_text)}")

        # Step 2: Create Document and split it
        documents = [Document(page_content=full_text)]
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=10)
        texts = text_splitter.split_documents(documents)

        print(f"Total chunks created: {len(texts)}")
        for i, doc in enumerate(texts):
            print(f"Chunk {i + 1} length: {len(doc.page_content)} characters")

        # Step 3: Prepare data for Pinecone
        data = [
            {"id": f"vec{i+1}", "text": doc.page_content}
            for i, doc in enumerate(texts)
        ]

        # Step 4: Upsert into Pinecone
        index.upsert_records(
            namespace="notes-namespace",
            records=data
        )

        return {
            "message": "PDF is ready to use.",
            "chunks": len(data)
        }

    except Exception as e:
        return {"error": str(e)}
