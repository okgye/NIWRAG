# scripts/test_ingest.py
from backend.parse import parse_documents
from backend.embed import index_documents
from backend.query import query_index
from app.generator import generate_letter

docs = parse_documents(["data/accepted_niw_letters/sample_letter.pdf"])
index = index_documents(docs)

user_profile = """
PhD in Electrical Engineering from Seoul National University.
Current research on lithium-ion battery safety systems.
Published 3 peer-reviewed papers.
Worked with LG Energy Solution on electrode coating systems.
"""

relevant_context = query_index(index, user_profile)

print("Top Relevant Snippets:\n")
print(relevant_context)

letter = generate_letter(user_profile, relevant_context)
print("\n📄 Drafted Letter:\n")
print(letter)