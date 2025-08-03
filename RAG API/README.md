# RAG Chatbot API

A **R**etrieval-**A**ugmented **G**eneration (RAG) chatbot built with FastAPI, Azure OpenAI, and Azure AI Search.

## 🏗️ Architecture

This application combines:
- **Azure OpenAI** for natural language generation
- **Azure AI Search** for document retrieval
- **LangChain** for orchestrating the RAG pipeline
- **FastAPI** for the REST API

## 📋 Prerequisites

- Python 3.11+
- Azure OpenAI service with deployments for:
  - Chat model (e.g., `gpt-4o-mini`)
  - Embeddings model (e.g., `text-embedding-3-small`)
- Azure AI Search service with indexed documents
- Required Azure credentials and endpoints

## ⚙️ Configuration

Create a `.env` file with your Azure credentials:

```env
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_KEY=your-search-key
AZURE_SEARCH_INDEX=your-index-name
AZURE_OPENAI_ENDPOINT=https://your-openai-service.openai.azure.com/
AZURE_OPENAI_API_KEY=your-openai-api-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server
```bash
# Option 1: Using the batch script (Windows)
start_server.bat

# Option 2: Using uvicorn directly
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Test the API
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Root Endpoint**: http://localhost:8000/

## 📡 API Endpoints

### POST `/chat`
Send a question to the chatbot and receive an AI-generated response.

**Request:**
```json
{
  "question": "What is Azure AI Search?"
}
```

**Response:**
```json
{
  "answer": "Azure AI Search is a cloud-based search service..."
}
```

### GET `/health`
Check if the API is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "message": "RAG Chatbot API is operational"
}
```

## 🧪 Testing

### Using the Interactive Documentation
1. Go to http://localhost:8000/docs
2. Click on the `/chat` endpoint
3. Click "Try it out"
4. Enter your question and click "Execute"

### Using curl
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"question": "Your question here"}'
```

### Using the Test Script
```bash
python test_client.py
```

## 🏢 Teams Integration Ready

This API is designed to be easily integrated with Microsoft Teams bots. The clean endpoints and error handling make it suitable for production use.

## 📁 Project Structure

```
rag-bot-backend/
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in git)
├── start_server.bat      # Server startup script
├── test_client.py        # API testing script
└── README.md            # This file
```

## 🔧 Key Features

- **Clean API Design**: RESTful endpoints with proper HTTP status codes
- **Error Handling**: Graceful error handling with user-friendly messages
- **Logging**: Structured logging for monitoring and debugging
- **Documentation**: Auto-generated interactive API documentation
- **Validation**: Request/response validation using Pydantic
- **Production Ready**: Suitable for deployment and Teams integration

## 🚨 Important Notes

- Ensure your Azure AI Search index contains the documents you want to query
- The embeddings model deployment must match the one used during document indexing
- Keep your `.env` file secure and never commit it to version control
