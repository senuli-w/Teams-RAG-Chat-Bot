@echo off
echo Starting RAG Bot Backend...
echo ============================
cd /d "C:\Users\senul\Desktop\RAG BOT API\rag-chatbot-api"
echo Current directory: %CD%
echo Using Python: "C:\Users\senul\Desktop\RAG BOT API\rag-chatbot-api\venv\Scripts\python.exe"
echo.
echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
"C:\Users\senul\Desktop\RAG BOT API\rag-chatbot-api\venv\Scripts\python.exe" -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
pause
