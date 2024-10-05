import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv

def add_custom_css():
    st.markdown("""
    <style>
    /* Main content styling */
    .main-content {
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Customizing text input */
    .stTextInput input {
        padding: 10px;
        font-size: 16px;
        border-radius: 8px;
        border: 1px solid #d3d3d3;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    /* Button Styling */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }

    .stButton > button:hover {
        background-color: #45a049;
    }

    /* Sidebar Styling */
    .sidebar .block-container {
        padding-top: 2rem;
    }
    
    .sidebar .stFileUploader {
        background-color: #ffffff;
        border: 1px solid #d3d3d3;
        border-radius: 8px;
        padding: 10px;
    }

    .sidebar .stButton > button {
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
    }

    .sidebar .stButton > button:hover {
        background-color: #0056b3;
    }

    </style>
    """, unsafe_allow_html=True)

def get_text(docs):
    text = ""
    for pdf in docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text
        
def main():
    st.set_page_config(page_title="SnapDoc", page_icon="📚", layout="wide")
    add_custom_css()
    st.title("📚 Chat with Multiple PDFs using SnapDoc")
    st.write("Ask questions about your documents and get insights with ease.")
    st.text_input("Type your question here:")
    st.markdown("</div>", unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your Documents")
        docs = st.file_uploader("Upload PDFs here:", type=["pdf"], accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                #getting raw content from the pdfs
                raw_content = get_text(docs)
                #get the text chunks

                #creating vector store7


if __name__ == '__main__':
    main()
