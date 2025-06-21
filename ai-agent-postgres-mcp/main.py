import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

# 1. Load environment variables (.env file should have your keys and MCP URL)
load_dotenv()

llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=0,
    streaming=True,
)

client = MultiServerMCPClient({
    "postgres": {
        "url": os.getenv("MCP_RENDER_URL"),  # e.g., "https://your-mcp-server.onrender.com/sse"
        "transport": "sse",
    }
})

checkpointer = InMemorySaver()

async def main():
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "user-convo-123"}}

    # First question
    print("\n--- Turn 1 ---")
    q1 = "How many customers are in the customers table?"
    async for event in agent.astream_events({"messages": [{"role": "user", "content": q1}]}, config=config, version="v1"):
        if event["event"] == "on_chat_model_stream" and event["data"]["chunk"]["content"]:
            print(event["data"]["chunk"]["content"], end="", flush=True)

    # Follow-up, demonstrating memory
    print("\n\n--- Turn 2 ---")
    q2 = "And how many orders are there?"
    async for event in agent.astream_events({"messages": [{"role": "user", "content": q2}]}, config=config, version="v1"):
        if event["event"] == "on_chat_model_stream" and event["data"]["chunk"]["content"]:
            print(event["data"]["chunk"]["content"], end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
