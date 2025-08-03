# Teams Bot Setup Guide

This guide will help you set up and run the Teams Bot project after cloning from GitHub.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (versions 18, 20, or 22)
- [Microsoft 365 Agents Toolkit Visual Studio Code Extension](https://aka.ms/teams-toolkit) version 5.0.0 or higher
- [Git](https://git-scm.com/)
- A Microsoft 365 developer account

## Setup Instructions

### 1. Clone and Install Dependencies

```bash
# Clone the repository
git clone <your-repo-url>
cd Teams-RAG-Chat-Bot/Teams\ Bot

# Install dependencies
npm install
```

### 2. Install Required VS Code Extension

1. Open VS Code
2. Install the "Microsoft 365 Agents Toolkit" extension
3. Sign in to your Microsoft 365 account through the extension

### 3. Configure Environment Variables

The project uses environment files in the `env/` folder. You'll need to configure these based on your deployment:

#### For Development (`env/.env.dev`):
- Update `AZURE_SUBSCRIPTION_ID`
- Update `AZURE_RESOURCE_GROUP_NAME`
- Update `RESOURCE_SUFFIX` (must be globally unique)
- Configure `RAG_BOT_API_URL` (should point to your RAG API endpoint)

#### Create User-Specific Environment Files:
These files are not in the repo for security and need to be created locally:

**`env/.env.dev.user`**:
```bash
# Add any sensitive or user-specific environment variables here
# This file is ignored by git

# Example (fill with your actual values):
# SECRET_CLIENT_SECRET=your-secret-here
```

**`env/.env.local.user`**:
```bash
# Local development overrides
# This file is ignored by git
```

### 4. 🎯 Using F5 (Recommended Method)

**This is the easiest way to run the project!**

1. Open the `Teams Bot` folder in VS Code
2. Make sure the Microsoft 365 Agents Toolkit extension is installed
3. Sign in to your Microsoft 365 account
4. **Press F5** 

The F5 workflow will automatically:
- ✅ Check prerequisites (Node.js, M365 account, ports)
- ✅ Start local tunnel (creates public URL)
- ✅ Provision Azure resources (if needed)
- ✅ Deploy the app to Teams
- ✅ Start your bot locally
- ✅ Launch Teams in browser

**First time setup**: When you press F5 for the first time, you'll be prompted to:
- Sign in to Microsoft 365
- Choose your Azure subscription
- Provision Azure resources

### 5. Alternative: Manual Setup

If you prefer manual control or F5 doesn't work:

```bash
# Build the project
npm run build

# For development with hot reload
npm run dev

# For production
npm start
```

### 6. Debug Configurations Available

Press **Ctrl+Shift+P** and search for "Debug: Select and Start Debugging" to see options:
- **Debug in Microsoft 365 Agents Playground** - Test in simulator
- **Debug in Teams (Edge)** - Run in Teams web app (Edge)
- **Debug in Teams (Chrome)** - Run in Teams web app (Chrome)
- **Debug in Teams (Desktop)** - Run in Teams desktop app

## Project Structure

```
Teams Bot/
├── appPackage/          # Teams app manifest and icons
├── env/                 # Environment configuration files
├── infra/              # Azure infrastructure templates
├── img/                # Documentation images
├── index.ts            # Main application entry point
├── teamsBot.ts         # Bot logic implementation
├── package.json        # Node.js dependencies and scripts
└── tsconfig.json       # TypeScript configuration
```

## Common Issues and Solutions

### Issue: "Module not found" errors
**Solution**: Run `npm install` to ensure all dependencies are installed.

### Issue: Authentication errors
**Solution**: Make sure you're signed in to the correct Microsoft 365 account in VS Code.

### Issue: Azure resource conflicts
**Solution**: Update the `RESOURCE_SUFFIX` in `env/.env.dev` to a unique value.

### Issue: RAG API connection fails
**Solution**: Ensure the `RAG_BOT_API_URL` in `env/.env.dev` points to a running RAG API instance.

## Integration with RAG API

This bot integrates with the RAG API located in the `../RAG API/` folder. Make sure:

1. The RAG API is running and accessible
2. The `RAG_BOT_API_URL` environment variable points to the correct endpoint
3. Both the bot and API are using compatible authentication methods

## Development Workflow

1. Make your changes to the TypeScript files
2. Test locally using `npm run dev`
3. Build using `npm run build`
4. Deploy using the Microsoft 365 Agents Toolkit
5. Test in Teams

## Additional Resources

- [Microsoft 365 Agents Toolkit Documentation](https://aka.ms/teams-toolkit)
- [Teams Bot Framework Documentation](https://docs.microsoft.com/en-us/azure/bot-service/)
- [Azure Bot Service Documentation](https://docs.microsoft.com/en-us/azure/bot-service/)
