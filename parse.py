from dotenv import load_dotenv
load_dotenv()

from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader

parser = LlamaParse(
    result_type="markdown"
)

file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=['data/canada.pdf'], file_extractor=file_extractor).load_data()
print(documents)