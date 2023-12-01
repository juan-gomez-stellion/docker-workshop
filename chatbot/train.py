from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import chromadb
from chromadb.config import Settings
import os

os.environ["OPENAI_API_KEY"] = "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"

loader = UnstructuredHTMLLoader("Diplomado en Fundamentos de computación en la Nube – ITM.html")
documents = loader.load()


text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
documents = text_splitter.split_documents(documents)

print(documents)

path = './db'
settings = Settings(
    persisy_directory=path,
    anonymized_telemetry=False
    )
    
client = chromadb.PersistentClient(settings=settings, path=path)

vectordb = Chroma.from_documents(
    documents=documents,
    embedding=OpenAIEmbeddings(),
    client=client)
    
