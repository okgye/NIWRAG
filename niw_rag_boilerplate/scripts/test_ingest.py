# scripts/test_ingest.py
from backend.parse import parse_documents
from backend.embed import index_documents

docs = parse_documents(["data/accepted_niw_letters/sample_letter.pdf"])
index = index_documents(docs)

print("Indexed successfully!")