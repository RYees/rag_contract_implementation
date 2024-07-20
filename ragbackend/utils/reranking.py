from sentence_transformers import CrossEncoder
import numpy as np
from flask import request, jsonify

class CrossEncoderReranker:
    def cross_encoder_reranker(query:str, retrieved_documents:list):
        try:
            cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
            query_text = query
            pairs = [[query_text, doc] for doc in retrieved_documents]
            scores = cross_encoder.predict(pairs)
            for score in scores:
                f"{score:.2f}"
            ordered_indices = np.argsort(scores)[::-1]
            for i in ordered_indices:
                f"{i+1}. {retrieved_documents[i]}"
            top_scored_docs = [retrieved_documents[i] for i in ordered_indices[:15]]
            return top_scored_docs, 200
        except Exception as error:
            # print(error)
            return jsonify({"error": "An error occurred"}), 500