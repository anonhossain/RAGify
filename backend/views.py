# Initialize router
from fastapi import APIRouter, UploadFile, File, Form
from webembedder import scrape_and_embed_website
from chat_engine import get_chat_response
from pdfembedder import embed_pdf
from file_uploader import save_document

api = APIRouter()

@api.get("/hello_anon")
def hello():
    return {"message": "Hello, Anon!"}

@api.post("/upload_document")
async def upload_files(pdf_file: UploadFile = File(...)):
    return await save_document(pdf_file)

@api.post("/embed_pdf")
async def run_embedding():
    return embed_pdf()

@api.post("/embed_website")
async def embed_website(url: str = Form(...)):
    return scrape_and_embed_website(url)

@api.post("/chat")
async def chat_with_ai(prompt: str):
    return {"response": get_chat_response(prompt)}