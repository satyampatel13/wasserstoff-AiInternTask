```markdown
## AI Internship Task - Wasserstoff Labs

This project is a document-based intelligent QA system built as part of the Wasserstoff AI Internship Task.

It allows users to upload multiple documents (PDFs, images, or text files), ask questions, and receive document-wise answers as well as a theme-based summary generated using an LLM.

---

### Features

-  Upload 75+ files (PDF, image, or text)
-  Extract content using OCR (Tesseract) and parsing
-  Store text as embeddings using ChromaDB
-  Use Groq's LLaMA 3 API to answer questions
-  Return both document-wise and theme-wise responses
-  Clean, simple Streamlit web interface
-  Fully deployed using Railway (backend) and Streamlit Cloud (frontend)

---

## 🔧 Tech Stack

| Component   | Technology             |
|-------------|-------------------------|
| 🧠 LLM       | Groq LLaMA 3            |
| 🔍 Vector DB | ChromaDB                |
| 📄 OCR       | Tesseract + PyMuPDF     |
| 🧩 Backend   | FastAPI (Python)        |
| 💻 Frontend  | Streamlit               |
| 🌐 Deploy    | Railway (backend), Streamlit Cloud (frontend)

---

### Folder Structure

```

chatbot\_theme\_identifier/
├── backend/         # FastAPI + LLM logic
│   ├── app/
│   └── requirements.txt
├── frontend/        # Streamlit app
│   ├── app.py
│   └── requirements.txt
├── render.yaml      # (For Render)
└── README.md

```

---

### Live Demo Links

-  **Frontend (Streamlit):** [Click to Open](https://wasserstoff-aiinterntask-sp.streamlit.app)
-  **Backend (FastAPI Swagger):** [Click to Open](https://wasserstoff-backend.up.railway.app/docs)

---

### How It Works

1. **Upload files** → They are read using OCR and parsed
2. **Stored in ChromaDB** → Text converted into vector embeddings
3. **Ask any question** → Relevant docs are found and passed to Groq's LLM
4. **Response shown**:
   - Document-wise answers
   - Summary with theme-based grouping

---

## Demo Flow (in simple English)

1. I open the web app (Streamlit)
2. I upload some documents (PDF, image, or text)
3. Then I ask a question, like:  
   _“What are the penalties mentioned in the SEBI Act?”_
4. The system searches all documents and sends relevant info to LLaMA 3
5. I get:
   - Individual document answers
   -  summary of the main themes

6. I also show the backend API using the `/docs` page

---

## About Me

> Name: **Satyam Patel**  
> Role: AI/ML Intern Applicant  
> Email: **[your-email@example.com]** (replace)  
> GitHub: [github.com/satyampatel13](https://github.com/satyampatel13)

---

## Notes

- No plagiarism: All code written from scratch
- Uses open-source tools and APIs
- Focused on performance + clean structure
- Fully working and deployed for real-world testing

---

## Thank You

Thank you Wasserstoff team for the opportunity. I’m excited to join, learn, and contribute to real-world AI solutions.

```
