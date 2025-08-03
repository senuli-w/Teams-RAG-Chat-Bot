import { ActivityTypes } from "@microsoft/agents-activity";
import {
  AgentApplication,
  AttachmentDownloader,
  MemoryStorage,
  TurnContext,
  TurnState,
} from "@microsoft/agents-hosting";
import { version } from "@microsoft/agents-hosting/package.json";
import axios from "axios";

// RAG Bot API Configuration
const RAG_BOT_API_URL = process.env.RAG_BOT_API_URL || "http://localhost:8000"; // Update with your actual API URL
const RAG_BOT_ENDPOINT = "/chat"; // Update with your actual endpoint

// Function to call RAG bot API
async function callRagBot(userMessage: string): Promise<string> {
  try {
    const response = await axios.post(`${RAG_BOT_API_URL}${RAG_BOT_ENDPOINT}`, {
      question: userMessage,
      // Add any other parameters your RAG bot API expects
      // session_id: "teams-bot-session", // if needed
      // max_tokens: 500, // if needed
    }, {
      headers: {
        'Content-Type': 'application/json',
        // Add any authentication headers if needed
        // 'Authorization': 'Bearer your-token-here',
      },
      timeout: 30000 // 30 second timeout
    });

    return response.data.answer || "I received your message but couldn't generate a response.";
  } catch (error) {
    console.error("Error calling RAG bot API:", error);
    if (axios.isAxiosError(error)) {
      if (error.response) {
        console.error("API responded with error:", error.response.status, error.response.data);
        return `Sorry, I encountered an error while processing your request. (Status: ${error.response.status})`;
      } else if (error.request) {
        console.error("No response received from API");
        return "Sorry, I couldn't connect to the knowledge base. Please try again later.";
      }
    }
    return "Sorry, I encountered an unexpected error while processing your request.";
  }
}

interface ConversationState {
  count: number;
}
type ApplicationTurnState = TurnState<ConversationState>;

const downloader = new AttachmentDownloader();

// Define storage and application
const storage = new MemoryStorage();
export const teamsBot = new AgentApplication<ApplicationTurnState>({
  storage,
  fileDownloaders: [downloader],
});

// Listen for user to say '/reset' and then delete conversation state
teamsBot.message("/reset", async (context: TurnContext, state: ApplicationTurnState) => {
  state.deleteConversationState();
  await context.sendActivity("Ok I've deleted the current conversation state.");
});

teamsBot.message("/count", async (context: TurnContext, state: ApplicationTurnState) => {
  const count = state.conversation.count ?? 0;
  await context.sendActivity(`The count is ${count}`);
});

teamsBot.message("/diag", async (context: TurnContext, state: ApplicationTurnState) => {
  await state.load(context, storage);
  await context.sendActivity(JSON.stringify(context.activity));
});

teamsBot.message("/state", async (context: TurnContext, state: ApplicationTurnState) => {
  await state.load(context, storage);
  await context.sendActivity(JSON.stringify(state));
});

teamsBot.message("/runtime", async (context: TurnContext, state: ApplicationTurnState) => {
  const runtime = {
    nodeversion: process.version,
    sdkversion: version,
  };
  await context.sendActivity(JSON.stringify(runtime));
});

teamsBot.message("/test-rag", async (context: TurnContext, state: ApplicationTurnState) => {
  const testResponse = await callRagBot("Hello, this is a test message.");
  await context.sendActivity(`RAG Bot Test Response: ${testResponse}`);
});

teamsBot.conversationUpdate(
  "membersAdded",
  async (context: TurnContext, state: ApplicationTurnState) => {
    await context.sendActivity(
      `Hi there! I'm a RAG bot running on Agents SDK version ${version}. Ask me anything and I'll search my knowledge base to help you!`
    );
  }
);

// Listen for ANY message to be received. MUST BE AFTER ANY OTHER MESSAGE HANDLERS
teamsBot.activity(
  ActivityTypes.Message,
  async (context: TurnContext, state: ApplicationTurnState) => {
    // Skip if message is empty or only whitespace
    const userMessage = context.activity.text?.trim();
    if (!userMessage) {
      await context.sendActivity("Please send a message for me to process.");
      return;
    }

    // Increment count state
    let count = state.conversation.count ?? 0;
    state.conversation.count = ++count;

    // Call RAG bot API
    const ragResponse = await callRagBot(userMessage);

    // Send the RAG bot response
    await context.sendActivity(`[${count}] ${ragResponse}`);
  }
);

teamsBot.activity(/^message/, async (context: TurnContext, state: ApplicationTurnState) => {
  await context.sendActivity(`Matched with regex: ${context.activity.type}`);
});

teamsBot.activity(
  async (context: TurnContext) => Promise.resolve(context.activity.type === "message"),
  async (context, state) => {
    await context.sendActivity(`Matched function: ${context.activity.type}`);
  }
);
