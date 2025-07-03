from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Load and process PDF
def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(pages)
    return docs

# Create vectorstore
def create_vectorstore(docs):
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding)
    return vectorstore

# QA Chain
def create_qa_chain(vectorstore):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain
