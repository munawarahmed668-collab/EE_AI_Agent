import os
import shutil

from ai.rag import index_pdf

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def upload_pdf(file):

    if file is None:
        return "No PDF selected."

    filename = os.path.basename(file)

    destination = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    shutil.copy(file, destination)

    index_pdf(destination)

    return f"✅ {filename} uploaded and indexed successfully!"