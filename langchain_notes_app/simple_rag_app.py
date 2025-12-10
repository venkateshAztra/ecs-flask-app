import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import tempfile
import os

st.set_page_config(page_title="🧠 Simple RAG Chatbot", layout="wide")
st.title("📄 Chat with Your PDF - Simple RAG")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        tmp_file_path = tmp_file.name
    
    st.success("✅ File uploaded successfully!")
    
    # Process the PDF
    with st.spinner("🔄 Processing PDF..."):
        try:
            # Load and split the document
            loader = PyPDFLoader(tmp_file_path)
            documents = loader.load()
            
            text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            docs = text_splitter.split_documents(documents)
            
            # Create embeddings and vector store
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            vectorstore = Chroma.from_documents(docs, embeddings)
            
            st.success(f"✅ Processed {len(docs)} document chunks!")
            
            # Query interface
            query = st.text_input("Ask a question about the PDF:")
            
            if query:
                with st.spinner("🔍 Searching for relevant information..."):
                    # Retrieve relevant documents
                    relevant_docs = vectorstore.similarity_search(query, k=3)
                    
                    # Display results
                    st.write("📎 **Relevant Information Found:**")
                    
                    for i, doc in enumerate(relevant_docs, 1):
                        with st.expander(f"📄 Relevant Chunk {i}"):
                            st.write(doc.page_content)
                            if hasattr(doc, 'metadata') and 'page' in doc.metadata:
                                st.caption(f"Page: {doc.metadata['page']}")
                    
                    # Simple answer generation (concatenate relevant chunks)
                    context = "\n\n".join([doc.page_content for doc in relevant_docs])
                    
                    st.write("🤖 **Simple Answer:**")
                    st.info(f"Based on the document, here are the most relevant sections related to '{query}':\n\n{context[:1000]}...")
                    
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
        
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)

else:
    st.info("👆 Please upload a PDF file to start chatting with it!")
    
    # Show example
    st.markdown("""
    ### How it works:
    1. **Upload** a PDF file
    2. **Wait** for processing (creates embeddings)
    3. **Ask** questions about the content
    4. **Get** relevant sections from the document
    
    This is a simple RAG (Retrieval Augmented Generation) system that:
    - Splits your PDF into chunks
    - Creates vector embeddings
    - Finds relevant sections based on your questions
    - Shows you the most relevant content
    """)