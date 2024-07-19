import pandas as pd
from langchain.text_splitter import CharacterTextSplitter
import os, sys
import utils.chroma as chom
import chromadb

def upload_pdf(file_path):
    # file_path = '../data/RaptorContract.pdf'
    pdftexts = chom.pdf_reader(file_path)
    pdftexts[0]

def chunking_strategy(pdf_doc):
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator = "\n\n",
        chunk_size = 100,
        chunk_overlap = 100,
        is_separator_regex = False,
        model_name='text-embedding-3-small', #used to calculate tokens
        encoding_name='text-embedding-3-small'
    )
    character_split_texts = text_splitter.split_text('\n\n'.join(pdf_doc))
    token_split_texts = chom.sentence_transfomer_textsplitter(character_split_texts)
    # print(f"\nTotal chunks: {len(character_split_texts)}")  
    return token_split_texts

def embed_and_store_to_chromadb_vectorestore(token_split_texts):    
    embedding_function = chom.embedding(token_split_texts)
    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.create_collection("microsoft_annual_report_20", embedding_function=embedding_function)

    ids = [str(i) for i in range(len(token_split_texts))]

    chroma_collection.add(ids=ids, documents=token_split_texts)
    chroma_collection.count()
    return chroma_collection

def vectordb_answer_question(chroma_collection, query):
    results = chroma_collection.query(query_texts=[query], n_results=500)
    retrieved_documents = results['documents'][0]
    return retrieved_documents