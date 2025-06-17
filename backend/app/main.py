import os
import shutil
from typing import List

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from app.services.document_processor import process_documents
from app.services.vector_store import create_vector_db
from app.services.qa_engine import get_answer

app = FastAPI()

UPLOAD_DIR = "backend/data"

@app.post("/upload/")
async def upload_docs(files: List[UploadFile] = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    saved_files = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved_files.append(file_path)

    processed = process_documents(saved_files)

    create_vector_db(processed)

    return {"documents": processed}


class QueryRequest(BaseModel):
    query: str

@app.post("/query/")
async def ask_question(req: QueryRequest):
    result = get_answer(req.query)
    return result
