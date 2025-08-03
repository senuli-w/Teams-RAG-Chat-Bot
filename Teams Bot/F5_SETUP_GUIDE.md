# Quick F5 Setup Guide

## ✅ What F5 Will Do Automatically

When you press F5 in VS Code with the Microsoft 365 Agents Toolkit, it runs this sequence:

1. **Check Prerequisites** - Validates Node.js, M365 account, available ports
2. **Start Local Tunnel** - Creates a public URL pointing to your local bot
3. **Provision Resources** - Creates Azure resources if they don't exist
4. **Deploy App** - Builds and registers your bot with Teams
5. **Start Application** - Runs your bot locally with debugging
6. **Launch Teams** - Opens Teams in browser/desktop with your bot

## 🔧 First Time Setup (One-time only)

### Step 1: Install Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Microsoft 365 Agents Toolkit"
4. Install and reload VS Code

### Step 2: Sign In
1. Click the Microsoft 365 Agents Toolkit icon in the sidebar
2. Sign in with your Microsoft 365 account
3. Choose your Azure subscription when prompted

### Step 3: Configure Environment
1. Open `env/.env.dev` 
2. Update `AZURE_SUBSCRIPTION_ID` with your subscription ID
3. Update `AZURE_RESOURCE_GROUP_NAME` (or create new one)
4. Set `RESOURCE_SUFFIX` to something unique (e.g., your initials + random numbers)

### Step 4: Press F5! 🚀
1. Open the Teams Bot folder in VS Code
2. Press F5
3. Choose "Debug in Microsoft 365 Agents Playground" for first test
4. Wait for provisioning (first time takes 2-5 minutes)
5. Teams will open automatically when ready

## 🔍 Troubleshooting F5

### "Prerequisites check failed"
- **Node.js not found**: Install Node.js 18, 20, or 22
- **M365 account not signed in**: Sign in through the extension
- **Port occupied**: Close apps using ports 3978 or 9239

### "Provision failed"
- **Azure subscription**: Make sure you have permissions
- **Resource name conflicts**: Change `RESOURCE_SUFFIX` to something unique
- **Resource group**: Create a new resource group if having issues

### "Deploy failed"
- **Build errors**: Run `npm run build` to check for TypeScript errors
- **Permission issues**: Check Azure resource group permissions

### "Teams won't open"
- **Firewall**: Allow VS Code and Node.js through Windows firewall
- **Browser**: Try different debug configurations (Edge/Chrome/Desktop)

## 🎯 Quick Test

To verify everything works:
1. Press F5
2. Choose "Debug in Microsoft 365 Agents Playground"
3. Type a message in the playground chat
4. Your bot should respond

## 🔄 Daily Workflow

After first-time setup, your daily workflow is simply:
1. Open VS Code
2. Press F5
3. Start debugging!

The toolkit remembers your settings and provisions, so subsequent F5 presses are much faster (10-30 seconds).
