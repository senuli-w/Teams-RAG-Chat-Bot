# Teams RAG Chat Bot

A Microsoft Teams chatbot that answers questions using Retrieval-Augmented Generation (RAG) powered by Azure AI services. Upload documents, ask questions, and get intelligent answers directly in Teams!

## 🚀 What This Project Does

This bot lets you:
- **Upload documents** (PDFs) and automatically extract and index content
- **Ask questions** about your documents in Microsoft Teams
- **Get intelligent answers** powered by Azure OpenAI and Azure AI Search
- **Chat naturally** with context-aware responses

Perfect for teams that need to quickly search through documentation, manuals, or knowledge bases.

## 🏗️ Architecture (Simple Overview)

```
📄 PDF Document
    ↓
📊 Data Ingestion (Python)
    ↓ Extract & chunk text
🔍 Azure AI Search (Vector Database)
    ↓ Store embeddings
🤖 RAG API (Python/FastAPI)
    ↓ Search + Generate
💬 Teams Bot (TypeScript)
    ↓ User interface
👥 Microsoft Teams
```

**Flow:**
1. **Data Ingestion**: PDF → Extract text → Create embeddings → Store in Azure AI Search
2. **User asks question** in Teams
3. **Teams Bot** sends question to RAG API
4. **RAG API** searches relevant documents + generates answer using Azure OpenAI
5. **Bot responds** with intelligent answer in Teams

## 🛠️ Tech Stack

- **Azure AI Search**: Document storage and vector search
- **Azure OpenAI**: Text embeddings and GPT for answer generation  
- **Python**: Data processing and RAG API (FastAPI)
- **TypeScript/Node.js**: Teams bot implementation
- **Microsoft 365 Agents Toolkit**: Teams integration
- **Unstructured.io**: PDF text extraction

## ⚡ Quick Start

### Prerequisites
- Node.js (18, 20, or 22)
- Python 3.8+
- [Microsoft 365 Agents Toolkit](https://aka.ms/teams-toolkit) VS Code Extension
- Azure subscription with AI services

### 🎯 Easiest Way: Press F5!

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd Teams-RAG-Chat-Bot
   ```

2. **Install VS Code extension**
   - Install "Microsoft 365 Agents Toolkit" in VS Code
   - Sign in with your Microsoft 365 account

3. **Configure Azure credentials**
   - Copy `.env.example` to `.env` in both `Data Ingestion` and `RAG API` folders
   - Fill in your Azure AI Search and OpenAI credentials

4. **Run the Teams Bot**
   - Open `Teams Bot` folder in VS Code
   - **Press F5** 🚀
   - Choose "Debug in Microsoft 365 Agents Playground"

The F5 workflow automatically handles Azure provisioning, tunneling, and Teams integration!

### 📋 Manual Setup (Alternative)

<details>
<summary>Click to expand manual setup steps</summary>

1. **Set up Data Ingestion**
   ```bash
   cd "Data Ingestion"
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your Azure credentials
   ```

2. **Process and ingest your data**
   ```bash
   python 1_process_data.py    # Extract text from PDF
   python 2_ingest_data.py     # Upload to Azure AI Search
   ```

3. **Set up RAG API**
   ```bash
   cd "../RAG API"
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your Azure credentials
   python app.py              # Start API server
   ```

4. **Set up Teams Bot**
   ```bash
   cd "../Teams Bot"
   npm install
   # Configure env/.env.dev with your settings
   npm run dev                # Start bot
   ```

</details>

## 📁 Project Structure

```
Teams-RAG-Chat-Bot/
├── 📂 Data Ingestion/          # PDF processing and data upload
│   ├── 1_process_data.py       # Extract text from PDF
│   ├── 2_ingest_data.py        # Upload to Azure AI Search
│   ├── data.json               # Processed document chunks
│   ├── support-ticket-system.pdf  # Sample document
│   └── .env.example            # Azure credentials template
│
├── 📂 RAG API/                 # FastAPI server for Q&A
│   ├── app.py                  # Main API server
│   ├── test_client.py          # API testing script
│   └── .env.example            # Azure credentials template
│
├── 📂 Teams Bot/               # Microsoft Teams integration
│   ├── index.ts                # Bot entry point
│   ├── teamsBot.ts             # Bot logic
│   ├── package.json            # Node.js dependencies
│   └── env/                    # Environment configuration
│       └── .env.dev            # Teams app settings
│
└── 📄 README.md                # This file
```

## 🔧 Configuration

### Required Azure Services
1. **Azure AI Search** - For document storage and vector search
2. **Azure OpenAI** - For embeddings and GPT models
3. **Microsoft 365** - For Teams integration

### Environment Variables
Each component needs these credentials in their `.env` files:

```bash
# Azure AI Search
AZURE_AI_SEARCH_ENDPOINT=https://your-search.search.windows.net
AZURE_AI_SEARCH_API_KEY=your-api-key
AZURE_AI_SEARCH_INDEX_NAME=your-index-name

# Azure OpenAI  
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=text-embedding-3-small
```

## 🎮 How to Use

1. **Start the system** using F5 in VS Code (recommended) or manual setup
2. **Open Microsoft Teams** (web or desktop)
3. **Find your bot** in the Apps section
4. **Start chatting!** Ask questions about the uploaded documents

Example questions:
- "What is the support ticket system?"
- "How do I create a new ticket?"
- "What are the priority levels?"

## 🚨 Troubleshooting

**Bot not responding?**
- Check if RAG API is running (`python app.py`)
- Verify Azure credentials in `.env` files
- Check Azure AI Search has indexed data

**F5 not working?**
- Install Microsoft 365 Agents Toolkit extension
- Sign in to Microsoft 365 account
- Check `Teams Bot/F5_SETUP_GUIDE.md` for detailed steps

**Data ingestion failed?**
- Verify Azure AI Search credentials
- Check if PDF file exists in Data Ingestion folder
- Run `python 1_process_data.py` first, then `python 2_ingest_data.py`

## 📚 Additional Resources

- [Teams Bot Setup Guide](Teams%20Bot/SETUP.md) - Detailed setup instructions
- [F5 Quick Start](Teams%20Bot/F5_SETUP_GUIDE.md) - VS Code F5 workflow
- [Microsoft 365 Agents Toolkit](https://aka.ms/teams-toolkit) - Official documentation

---

## 📋 Original Project Requirements

This project was created as an exercise for hands-on experience with retrieval-augmented generation (RAG) and Microsoft Teams integration, focusing on practical application of Azure and AI technologies.

### Exercise Objective
Develop a functional Q&A chatbot integrated with Microsoft Teams, utilizing RAG to answer questions based on a custom dataset.

### Technologies Used

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