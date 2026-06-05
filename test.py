import json
from typing import List

# Unstructured for documents parsing
from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title

# Langchain components
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

print("Successfully imported all libraries.")
load_dotenv()

from transformers import DetrImageProcessor
print("DETR OK inside notebook")