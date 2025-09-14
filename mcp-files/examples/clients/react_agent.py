import asyncio
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

mcp_client = MultiServerMCPClient({"file_server": {"url": "http://127.0.0.1:8000/sse", "transport": "sse"}})

# 4. Main Agent Function
async def run_agent():
    print("Connection successful. Loading tools...")

    tools = await mcp_client.get_tools()
    print(f"Available tools: {tools}")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    agent_executor = create_react_agent(llm, tools, debug=True)
    print("\nMCP client ready. Type 'quit' to exit.")

    while True:
        query = input("\nAsk me anything: ")
        if query.lower() == "quit":
            break

        response = await agent_executor.ainvoke({"messages": [("user", query)]})
        final_message = response["messages"][-1].content
        print(f"\nAssistant: {final_message}")


if __name__ == "__main__":
    asyncio.run(run_agent())
