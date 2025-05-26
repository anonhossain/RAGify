import shutil
from dotenv import load_dotenv
import os

from fastapi import UploadFile

load_dotenv()

# Access variables from the .env file
PDF_FILE = os.getenv('PDF_FILE')
# Make sure folders exist
os.makedirs(PDF_FILE, exist_ok=True)

async def save_document(pdf_file: UploadFile):
    # Save PDF
    pdf_path = os.path.join(PDF_FILE, "document.pdf")
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    return {"message": "Files uploaded successfully"}