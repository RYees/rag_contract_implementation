import pandas as pd
import os, sys
from ragbackend.utils import chroma
from ragbackend.utils.chunking import ChunkingApproaches
from ragbackend.utils.reranking import CrossEncoderReranker
import chromadb
from flask import request, jsonify
from ragbackend.main.base import (
    BaseResource
)

class TestResource(BaseResource):
    def post(self):
        return "hey"
    
class TestViewResource(BaseResource):
    def get(self):
        return "selam, it is working"

class RagEngineResource(BaseResource):
    def post(self):
        try:
            value = request.get_json()
            file_path = value.get('file_path')
            question = value.get('question')
            documents = chroma.pdf_reader(file_path)
            result = self.embed_and_store_to_chromadb_vectorestore(documents, question)
            return {"response": result}, 200
        except Exception as error:
            # print(error)
            return jsonify({"error": "An error occurred"}), 500
        
    def embed_and_store_to_chromadb_vectorestore(self, documents: list, query:str):  
        try: 
            token_split_texts = ChunkingApproaches.chunking_strategy(documents)  
            embedding_function = chroma.embedding()
            chroma_client = chromadb.Client()
            chroma_collection = chroma_client.create_collection("r0t0t_20", embedding_function=embedding_function)
            ids = [str(i) for i in range(len(token_split_texts))]
            chroma_collection.add(ids=ids, documents=token_split_texts)   
            chroma_collection.count()
            retrieved_documents = chroma_collection.query(query_texts=[query], n_results=chroma_collection.count())
            retrieved_documents = retrieved_documents['documents'][0]
            top_docs = CrossEncoderReranker.cross_encoder_reranker(query, retrieved_documents)        
            output_answer = chroma.openai_model_answer(query=query, retrieved_documents=top_docs)
            return output_answer , 200
        except Exception as error:
            # print(error)
            return jsonify({"error": "An error occurred"}), 500


