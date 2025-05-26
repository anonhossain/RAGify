import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain # Assuming vectordb is defined in webembedder.py

# Load environment variables
load_dotenv()

# Get the Google API Key and Model from .env
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
MODEL = os.getenv('MODEL')

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
llm = genai.GenerativeModel(model_name=MODEL)

# Function to handle general conversation or Q/A
def get_chat_response(prompt: str) -> str:
    """
    Generates a response from the Gemini model based on the user's prompt.

    Args:
        prompt (str): The user input or question.

    Returns:
        str: The AI-generated response.
    """
    try:
        response = llm.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"