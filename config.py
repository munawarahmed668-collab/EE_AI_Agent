import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Models
CHAT_MODEL = "gemini-flash-latest"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Folders
UPLOAD_FOLDER = "uploads"
CHROMA_FOLDER = "chroma_db"
DATA_FOLDER = "data"

# App
APP_TITLE = "⚡ Electrical Engineering AI Assistant"