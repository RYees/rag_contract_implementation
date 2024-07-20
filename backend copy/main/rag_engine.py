import pandas as pd
import os, sys
from ..utils import chroma
from ..utils.chunking import CrossEncoderReranker
from ..utils import reranking
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
            return jsonify(result), 200
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500
        
    def embed_and_store_to_chromadb_vectorestore(self, documents: list, query:str):  
        try: 
            token_split_texts = CrossEncoderReranker.chunking_strategy(documents)  
            embedding_function = chroma.embedding(token_split_texts)
            chroma_client = chromadb.Client()
            chroma_collection = chroma_client.create_collection("microsoft_annual_report_20", embedding_function=embedding_function)
            ids = [str(i) for i in range(len(token_split_texts))]
            chroma_collection.add(ids=ids, documents=token_split_texts)   
            llm_response = self.execute_question(chroma_collection, query)
            return jsonify(llm_response), 200
        except Exception as error:
                return jsonify({"error": "An error occurred"}), 500

    def execute_question(self, chroma_collection:chromadb.api.models.Collection.Collection, query:str):
        try:
            retrieved_documents = chroma_collection.query(query_texts=[query], n_results=500)
            top_docs = reranking.cross_encoder_reranker(query, retrieved_documents)
            output_answer = chroma.openai_model_answer(query=query, retrieved_documents=top_docs)
            return jsonify(output_answer), 200
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500

