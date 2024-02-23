from langchain_community.document_loaders import PyPDFLoader
import os
import getpass
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import dotenv_values

file_path = '../data/RaptorContract.pdf'
env_vars = dotenv_values('.env')
openai_api_key = env_vars.get('OPENAI_API_KEY')
# print(openai_api_key)
from langchain.embeddings.openai import OpenAIEmbeddings
def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    print(pages[0])    

    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(openai_api_key=openai_api_key))
    print(faiss_index)
    # docs = faiss_index.similarity_search("Under what circumstances and to what extent the Sellers are responsible for a breach of representations and warranties?", k=2)
    # for doc in docs:
    #     print(str(doc.metadata["page"]) + ":", doc.page_content[:300])    
         

pdf_loader(file_path)