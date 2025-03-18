# open-research-ANA 🔍

This demo showcases ANA (Agent Native Application), a research canvas app that combines Human-in-the-Loop capabilities with [Tavily's](https://tavily.com/) real-time search and [CopilotKit's](https://copilotkit.ai) agentic interface. 

Powered by [LangGraph](https://www.langchain.com/langgraph), it simplifies complex research tasks, making them more interactive and efficient.

<p align="left">
   <a href="https://docs.copilotkit.ai/coagents" rel="dofollow">
      <strong>Explore the CopilotKit docs »</strong>
   </a>
</p>

![tavily-demo](https://github.com/user-attachments/assets/70c7db1b-de5b-4fb2-b447-09a3a1b78d73)

## Quick Start 🚀

### 1. Prerequisites
This projects uses the following tools:

- [pnpm](https://pnpm.io/installation)
- [UV](https://docs.astral.sh/uv/)
- [Langgraph CLI](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)

### 2. API Keys Needed
Running locally, you'll need the following API keys:

- [OpenAI](https://platform.openai.com/api-keys)
- [Tavily](https://tavily.com/#pricing)
- [LangSmith](https://docs.smith.langchain.com/administration/how_to_guides/organization_management/create_account_api_key)
- [CopilotKit](https://cloud.copilotkit.ai) (optional)

### 3. Start the Agent
There are two main components to this project: the agent and the frontend. First, we'll start the agent.

```bash
cd agent

# Create and populate .env
cat << EOF > .env
OPENAI_API_KEY=your_key
TAVILY_API_KEY=your_key
LANGSMITH_API_KEY=your_key
EOF

## Start the agent
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --host localhost --port 8000
```

### 4. Start the Frontend
Next, we'll start the frontend.

```bash
cd frontend
pnpm install

# Create and populate .env
cat << EOF > .env
OPENAI_API_KEY=your_openai_key
LANGSMITH_API_KEY=your_langsmith_key
LOCAL_DEPLOYMENT_URL=http://localhost:8000
EOF

# Start the app
pnpm run dev
```

## Documentation 📚
- [CopilotKit Docs](https://docs.copilotkit.ai/coagents)
- [LangGraph Platform Docs](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/)
