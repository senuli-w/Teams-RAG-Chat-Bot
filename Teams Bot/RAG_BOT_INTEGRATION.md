# RAG Bot Integration

This Teams bot has been modified to integrate with a RAG (Retrieval Augmented Generation) bot API instead of simply echoing messages.

## Configuration

### Environment Variables

The following environment variable should be configured in your `.env` files:

- `RAG_BOT_API_URL`: The base URL of your RAG bot API (default: `http://localhost:8000`)

### API Endpoint

The bot expects your RAG API to have an endpoint that accepts POST requests with the following structure:

```json
{
  "message": "User's question or message"
}
```

And returns a response with one of these structures:

```json
{
  "response": "The RAG bot's response"
}
```

or

```json
{
  "message": "The RAG bot's response"
}
```

## Available Commands

- `/reset` - Clears conversation state
- `/count` - Shows current message count
- `/test-rag` - Tests the RAG bot API connection
- `/diag` - Shows diagnostic information
- `/state` - Shows current state
- `/runtime` - Shows runtime information

## How it Works

1. When a user sends a message, the bot intercepts it
2. The message is sent to your RAG bot API
3. The response from the RAG bot is sent back to the user
4. Message count is maintained for conversation tracking

## Error Handling

The bot includes comprehensive error handling for:
- API connection failures
- Timeout errors (30 seconds)
- Empty responses
- Network errors

## Customization

To customize the integration for your specific RAG bot API:

1. Update the `RAG_BOT_API_URL` environment variable
2. Modify the `RAG_BOT_ENDPOINT` constant in `teamsBot.ts` if needed
3. Adjust the request/response format in the `callRagBot` function
4. Add authentication headers if your API requires them

## Testing

1. Start your RAG bot API server
2. Run the Teams bot using `npm run dev:teamsfx:testtool`
3. Use the `/test-rag` command to verify the connection
4. Send regular messages to test the full integration
