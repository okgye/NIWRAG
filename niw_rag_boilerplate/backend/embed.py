# backend/embed.py
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

def index_documents(documents):
    chunker = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    nodes = chunker.get_nodes_from_documents(documents)

    index = VectorStoreIndex.from_documents(nodes)
    return index