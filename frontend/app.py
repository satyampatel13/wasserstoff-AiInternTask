import streamlit as st
import requests
import os

API_URL = "http://localhost:8000"
UPLOAD_URL = f"{API_URL}/upload/"
QUERY_URL = f"{API_URL}/query/"

# Streamlit page setup
st.set_page_config(page_title="Wasserstoff Theme Chatbot", layout="centered")
st.title("Document Theme Identifier")

# Initialize session state
if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

# Upload documents section
st.header("Upload Files")
uploaded_files = st.file_uploader(
    "Select PDFs, images or text files",
    type=["pdf", "png", "jpg", "jpeg", "txt"],
    accept_multiple_files=True
)

if uploaded_files and st.button("Upload"):
    files = [("files", (file.name, file, file.type)) for file in uploaded_files]
    with st.spinner("Processing..."):
        res = requests.post(UPLOAD_URL, files=files)
        if res.status_code == 200:
            st.success("Files uploaded successfully")
            st.session_state.uploaded = True
        else:
            st.error("Upload failed Try again.")

# Ask question
if st.session_state.uploaded:
    st.header("Ask a Question")
    query = st.text_input("Enter your question:")

    if query and st.button("Get Answer"):
        with st.spinner("Generating response..."):
            res = requests.post(QUERY_URL, json={"query": query})
            if res.status_code == 200:
                data = res.json()
                st.subheader("Document Answers")
                st.markdown("---")
                for line in data["answer"].split("\n"):
                    if line.startswith("DOC"):
                        st.markdown(f"-{line.strip()}")
                
                st.markdown("---")
                st.subheader("Key Themes")
                theme_lines = [l for l in data["answer"].split("\n") if "Theme" in l or l.startswith("  DOC")]
                for line in theme_lines:
                    if "Theme" in line:
                        st.markdown(f"{line.strip()}")
                    else:
                        st.markdown(f"{line.strip()}")
            else:
                st.error("Something went wrong. Try again.")
