import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()
llama_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

def parse_documents(file_paths):
    parser = LlamaParse(api_key=llama_api_key)
    documents = parser.load_data(file_paths)
    return documents