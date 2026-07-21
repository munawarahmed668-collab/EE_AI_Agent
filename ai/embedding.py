from sentence_transformers import SentenceTransformer
from huggingface_hub import login
from config import EMBEDDING_MODEL
import os
from dotenv import load_dotenv

load_dotenv()

#login(token=os.getenv("HF_TOKEN"))

print("Loading embedding model...")

model = SentenceTransformer(EMBEDDING_MODEL)

print("Embedding model loaded!")


def create_embeddings(chunks):
    return model.encode(chunks, convert_to_numpy=True)


def embed_query(query):
    return model.encode(query, convert_to_numpy=True)