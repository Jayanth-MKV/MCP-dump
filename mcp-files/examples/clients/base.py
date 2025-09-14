import asyncio
from fastmcp import Client

from fastmcp.client.transports import SSETransport

# transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
transport = SSETransport(url="http://127.0.0.1:8000/sse")


async def main():
    # Connect to your STDIO server by specifying the Python file path
    # async with Client("../server/mcp_server.py") as client:
    async with Client(transport) as client:
        # Check connection
        await client.ping()
        print("Connected to server!")

        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")

        # Call the greet tool
        result = await client.call_tool("create_file", {"filename": "example.txt", "content": "This is an example file created by the MCP client."})
        print(f"Tool result: {result.content[0].text}")


# Run the client
if __name__ == "__main__":
    asyncio.run(main())
