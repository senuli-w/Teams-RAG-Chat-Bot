"""
Test client for the RAG Chatbot API

This script tests all endpoints of the RAG Chatbot API to ensure
everything is working correctly before deployment or integration.
"""

import requests
import json
import sys

def test_api():
    """Test all API endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 RAG Chatbot API Test Suite")
    print("=" * 60)
    
    # Test 1: Health Check
    print("1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            print(f"✅ Health check passed: {response.json()['status']}")
        else:
            print(f"❌ Health check failed: Status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check failed: {e}")
        print("   Make sure the server is running on http://localhost:8000")
        return False
    
    print("\n" + "-" * 40)
    
    # Test 2: Root Endpoint
    print("2. Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint working: {data['message']}")
        else:
            print(f"❌ Root endpoint failed: Status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Root endpoint failed: {e}")
    
    print("\n" + "-" * 40)
    
    # Test 3: Chat Endpoint
    print("3. Testing chat endpoint...")
    test_questions = [
        "Hello, what can you help me with?",
        "What information do you have access to?",
        "Can you provide a summary of your capabilities?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n   Test {i}: '{question[:50]}...'")
        try:
            chat_data = {"question": question}
            response = requests.post(
                f"{base_url}/chat",
                headers={"Content-Type": "application/json"},
                json=chat_data,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data['answer'][:100] + "..." if len(data['answer']) > 100 else data['answer']
                print(f"   ✅ Response: {answer}")
            else:
                print(f"   ❌ Failed: Status {response.status_code}")
                print(f"   Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 API Test Suite Complete!")
    print("\nManual testing options:")
    print(f"• Root: {base_url}/")
    print(f"• Health: {base_url}/health")
    print(f"• Interactive Docs: {base_url}/docs")
    print(f"• Chat: POST {base_url}/chat")
    
    return True

if __name__ == "__main__":
    try:
        test_api()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
