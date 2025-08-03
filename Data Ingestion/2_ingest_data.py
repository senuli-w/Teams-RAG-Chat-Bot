import json
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Load environment variables from .env file
load_dotenv()

# Azure AI Search settings
search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
search_key = os.getenv("AZURE_AI_SEARCH_API_KEY")
search_index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")

# Azure OpenAI settings
openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_key = os.getenv("AZURE_OPENAI_API_KEY")
embedding_deployment_name = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")

# Source data file
DATA_FILE_PATH = "data.json"

# Initialize SDK clients
search_client = SearchClient(endpoint=search_endpoint, index_name=search_index_name, credential=AzureKeyCredential(search_key))
openai_client = AzureOpenAI(azure_endpoint=openai_endpoint, api_key=openai_key, api_version="2024-02-01")

# Load the data from the JSON file
with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
    documents_to_upload = json.load(f)

# Generate embeddings and add to documents
print(f"Generating embeddings for {len(documents_to_upload)} documents...")
for doc in documents_to_upload:
    text_to_embed = doc["content"]
    embedding = openai_client.embeddings.create(input=text_to_embed, model=embedding_deployment_name)
    doc["content_vector"] = embedding.data[0].embedding

print("Embeddings generated.")

# Upload the documents to Azure AI Search
print("Uploading documents...")
result = search_client.upload_documents(documents=documents_to_upload)

print(f"Upload complete. {len(result)} documents uploaded successfully.")