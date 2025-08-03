"""
RAG (Retrieval-Augmented Generation) Chatbot API

This FastAPI application provides a chatbot service that uses:
- Azure OpenAI for language generation
- Azure AI Search for document retrieval
- LangChain for orchestrating the RAG pipeline

The chatbot retrieves relevant documents from an Azure Search index
and uses them to provide contextual answers to user questions.
"""

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import logging

from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores import AzureSearch
from langchain.chains import RetrievalQA

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# FastAPI application instance
app = FastAPI(
    title="RAG Chatbot API",
    description="A RAG-based chatbot using Azure OpenAI and Azure AI Search",
    version="1.0.0"
)

# Pydantic models for request/response validation
class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    question: str
    
    class Config:
        schema_extra = {
            "example": {
                "question": "What is Azure AI Search?"
            }
        }

class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    answer: str
    
class ErrorResponse(BaseModel):
    """Response model for errors"""
    error: str
    answer: str

# Azure OpenAI Embeddings Configuration
# Used to convert text into vector embeddings for semantic search
embedding_function = AzureOpenAIEmbeddings(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT"],  # text-embedding model
    api_version=os.environ["AZURE_OPENAI_API_VERSION"]
)

# Azure AI Search Vector Store Configuration
# Connects to the pre-indexed documents in Azure Search
search = AzureSearch(
    azure_search_endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
    azure_search_key=os.environ["AZURE_SEARCH_KEY"],
    index_name=os.environ["AZURE_SEARCH_INDEX"],
    embedding_function=embedding_function
)

# Azure OpenAI Chat Model Configuration
# The language model that generates responses
llm = AzureChatOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT"],  # gpt-4o-mini or similar
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    temperature=0  # Lower temperature for more deterministic responses
)

# RAG Chain Configuration
# Combines retrieval (search) with generation (LLM)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=search.as_retriever(),
    return_source_documents=True
)

# API Endpoints

@app.get("/", tags=["General"])
async def root():
    """
    Root endpoint providing API information and available endpoints.
    """
    return {
        "message": "RAG Chatbot API is running!",
        "version": "1.0.0",
        "description": "A RAG-based chatbot using Azure OpenAI and Azure AI Search",
        "endpoints": {
            "chat": "POST /chat - Send a question to the chatbot",
            "docs": "GET /docs - Interactive API documentation",
            "health": "GET /health - Health check"
        }
    }

@app.get("/health", tags=["General"])
async def health():
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "healthy", 
        "message": "RAG Chatbot API is operational"
    }

@app.post("/chat", response_model=ChatResponse, tags=["Chatbot"])
async def chat(request: ChatRequest):
    """
    Main chat endpoint for the RAG chatbot.
    
    This endpoint:
    1. Takes a user question
    2. Searches for relevant documents in Azure AI Search
    3. Uses Azure OpenAI to generate a contextual response
    4. Returns the answer to the user
    
    Args:
        request (ChatRequest): Contains the user's question
        
    Returns:
        ChatResponse: Contains the chatbot's answer
        
    Raises:
        HTTPException: If there's an error processing the request
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        logger.info(f"Processing question: {request.question[:100]}...")
        
        # Invoke the RAG chain to get an answer
        result = rag_chain.invoke({"query": request.question})
        
        # Extract the answer from the result
        answer = result.get("result", "No answer found")
        
        logger.info("Question processed successfully")
        
        return ChatResponse(answer=answer)
        
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        
        # Return a user-friendly error message
        raise HTTPException(
            status_code=500, 
            detail="Sorry, I encountered an error processing your question. Please try again."
        )