import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
INDEX_NAME = os.getenv('INDEX_NAME')

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if it doesn't exist
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1',
            embed={
                "model": "llama-text-embed-v2",
                "field_map": {
                    "text": "text"
                }
            }
        )
    )

index = pc.Index(INDEX_NAME)

def scrape_and_embed_website(url: str):
    try:
        # Step 1: Scrape the webpage
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        
        print(f"Total characters scraped: {len(text)}")

        # Step 2: Create Document and split it
        documents = [Document(page_content=text)]
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=10)
        chunks = text_splitter.split_documents(documents)

        print(f"Total chunks created: {len(chunks)}")

        # Step 3: Prepare for Pinecone
        records = [{"id": f"vec{i+1}", "text": doc.page_content} for i, doc in enumerate(chunks)]

        # Step 4: Upsert to Pinecone
        index.upsert_records(
            namespace="web-namespace",
            records=records
        )

        return {
            "message": "Website content embedded successfully.",
            "chunks": len(records)
        }

    except Exception as e:
        return {"error": str(e)}