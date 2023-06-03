import os

from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ChatVectorDBChain
from langchain.chat_models import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_DB_FULL_PATH = os.getenv("DB_DIR") + os.getenv("DB_NAME")
PDF_FULL_PATH = os.getenv("PDF_DIR") + os.getenv("PDF_NAME")

embeddings = OpenAIEmbeddings()

loader = PyPDFLoader(f"{PDF_FULL_PATH}.pdf")
pages = loader.load_and_split()
vectordb = Chroma.from_documents(pages, embedding=embeddings, persist_directory=VECTOR_DB_FULL_PATH)
vectordb.persist()

print(f"Succesfully indexed document {os.getenv('PDF_NAME')}.")