# backend/query.py
from llama_index.core.query_engine import RetrieverQueryEngine

def get_query_engine(index, top_k=5):
    return index.as_query_engine(similarity_top_k=top_k)

def query_index(index, user_profile):
    query_engine = get_query_engine(index)
    response = query_engine.query(user_profile)
    return response.response