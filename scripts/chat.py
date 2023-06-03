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

embeddings = OpenAIEmbeddings()

vectordb = Chroma(persist_directory=VECTOR_DB_FULL_PATH, embedding_function=embeddings)

qa = ChatVectorDBChain.from_llm(ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo"), vectordb, return_source_documents=True)

chat_history = []
while True:
	query = input("Any question or do you want to STOP? ")
	if "STOP" in query or "stop" in query:
		break
	result = qa({"question": query, "chat_history": ""})
	aswer = result["answer"]
	chat_history.append((query, aswer))
	print("Answer:\n")
	print(aswer)