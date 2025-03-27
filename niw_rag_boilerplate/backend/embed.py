# backend/embed.py
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import Document

def index_documents(documents):
    if isinstance(documents[0], Document):
        return VectorStoreIndex.from_documents(documents)

    chunker = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    nodes = chunker.get_nodes_from_documents(documents)
    return VectorStoreIndex.from_documents(nodes)