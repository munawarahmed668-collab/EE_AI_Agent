from utils.pdf_reader import read_pdf
from utils.chunker import split_text
from ai.embedding import create_embeddings, embed_query

import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="ee_books"
)


def index_pdf(pdf_path):

    text = read_pdf(pdf_path)

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print("PDF indexed successfully!")


def search_pdf(question, top_k=3):

    query_embedding = embed_query(question)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return "\n\n".join(results["documents"][0])