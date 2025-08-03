# Teams Integration Guide

## Pre-requisites for Teams Integration

Before integrating with Microsoft Teams, ensure:

1. **API is Running**: Your RAG chatbot API is running and accessible
2. **Testing Complete**: All endpoints tested and working correctly
3. **Production Ready**: Code is clean and production-ready

## Teams Bot Integration Options

### Option 1: Azure Bot Service
- Create an Azure Bot Service resource
- Configure the messaging endpoint to point to your API
- Set up Teams channel

### Option 2: Teams App with Bot Framework
- Use Microsoft Bot Framework SDK
- Create a Teams app manifest
- Deploy via Teams Developer Portal

## API Endpoints for Teams

Your cleaned API provides these endpoints for Teams integration:

- **POST /chat** - Main chatbot endpoint
- **GET /health** - Health check for monitoring
- **GET /** - API information

## Next Steps

1. Deploy your API to a cloud service (Azure App Service, AWS, etc.)
2. Obtain a public HTTPS URL for your API
3. Follow Microsoft Teams bot development documentation
4. Configure webhooks to point to your `/chat` endpoint

## Security Considerations for Production

- Add authentication/authorization
- Implement rate limiting
- Add request validation
- Set up monitoring and logging
- Use HTTPS only
- Secure environment variables
