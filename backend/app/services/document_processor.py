import os
import uuid
import re
from typing import List
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path

# Set tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"[ERROR] Failed to extract PDF text: {e}")
    return clean_text(text)

def extract_text_via_ocr(pdf_path: str) -> str:
    text = ""
    try:
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            text += pytesseract.image_to_string(image)
    except Exception as e:
        print(f"[ERROR] OCR extract failed: {e}")
    return clean_text(text)

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def process_documents(files: List[str]) -> List[dict]:
    results = []
    for file in files:
        file_type = os.path.splitext(file)[1].lower()
        content = ""

        if file_type in ['.pdf']:
            content = extract_text_from_pdf(file)
            if len(content.strip()) < 100:
                print("[INFO] Using OCR due to low text")
                content = extract_text_via_ocr(file)
        elif file_type in ['.png', '.jpg', '.jpeg']:
            content = pytesseract.image_to_string(file)
        elif file_type in ['.txt']:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

        results.append({
            "id": str(uuid.uuid4()),
            "filename": os.path.basename(file),
            "content": clean_text(content)
        })
    return results
