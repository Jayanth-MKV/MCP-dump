from dotenv import load_dotenv
from fastmcp import Client
from google import genai
import asyncio
from fastmcp.client.transports import SSETransport

load_dotenv()

transport = SSETransport(url="http://127.0.0.1:8000/sse")
mcp_client = Client(transport)
gemini_client = genai.Client()


async def main():
    async with mcp_client:
        tools = await mcp_client.list_tools_mcp()
        print(f"Available tools: {tools}")

        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents="create a new file with 10 jokes",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[mcp_client.session],  # Pass the FastMCP client session
            ),
        )
        print(response.text)


if __name__ == "__main__":
    asyncio.run(main())
