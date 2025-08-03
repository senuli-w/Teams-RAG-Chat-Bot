# Teams RAG Chat Bot

## 1.0 Introduction

This folder contains the implementation for the Teams RAG Chat Bot, an exercise project designed to provide hands-on experience with retrieval-augmented generation (RAG) and Microsoft Teams integration. The project aligns with the Charlie onboarding ramp-up plan and focuses on practical application of key Azure and AI technologies.

## 2.0 Exercise Overview

The objective is to develop a functional Q&A chatbot integrated with Microsoft Teams, utilizing RAG to answer questions based on a custom dataset. The primary technologies and frameworks used include:

- **Azure AI Search**: For document retrieval and indexing.
- **Azure OpenAI**: For generating answers using GPT models and embeddings.
- **LangChain**: For orchestrating the RAG workflow.
- **Azure Bot Service**: For integrating the bot with Teams as the client interface.
- **Unstructured.io (or similar)**: For data extraction and preprocessing.

### Key Implementation Steps

#### Data Ingestion and Indexing
- Select a small dataset (single PDF or simple website).
- Use Unstructured.io or similar tools to extract and preprocess data.
- Create an Azure AI Search instance and define an index with an appropriate schema.
- Set up Azure OpenAI with deployed embedding and GPT models.
- Ingest processed data into the AI Search index.

#### Orchestrator Implementation
- Build a chat API and implement a RAG flow using LangChain (TypeScript/Python).
- Connect the orchestrator to the AI Search index and OpenAI models.

#### Teams Bot Implementation
- Start with a Teams bot template in VSCode.
- Integrate the orchestrator chat API.
- Use default UI cards for displaying questions and answers.

#### Environment Setup
- Use the `charlie-dev_sandbox` Azure resource group (Dev subscription).
- Opt for free or lowest-cost tiers (e.g., Linux-based app services).
- Use resource naming conventions to differentiate individual environments.
- Create a single Azure AI Search account with multiple indexes per project.

### Out of Scope
- Deployment automation (manual provisioning is acceptable).
- Navigation to answer references.
- Chat history support.
- Custom Teams bot prompts/commands.

### Additional Steps (Not Implemented)
- Explore improvements in data extraction & ingestion processes.
- Research the latest in RAG and potential workflow enhancements.

## 3.0 Outcome

Expected deliverables:

- Functional RAG chatbot integrated with Microsoft Teams (demo-ready).
- Simple representation of the ingestion flow and data mapping.
- Architecture and workflow diagrams.

## 4.0 Evaluation Criteria

- The project should be operational and demonstrable.
- The developer should understand the end-to-end flow from data ingestion to RAG-based response generation.
- Creativity and any additional enhancements are encouraged.

---

**Note:** The resources and implementation should prioritize cost efficiency and simplicity. For questions or further guidance, refer to the Charlie onboarding documentation or reach out to the project mentor.