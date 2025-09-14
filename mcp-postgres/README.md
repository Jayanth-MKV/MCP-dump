# ai-agent-postgres-mcp

This project demonstrates how to use the Model Context Protocol (MCP) to connect an AI agent to a Postgres database for advanced database analysis, health checks, and intelligent query capabilities. It includes both a Jupyter notebook and a Python script for interacting with a Postgres database using LangChain, LangGraph, and the MCP protocol.

## Features

- **Database Health Analysis:** Check index health, connection utilization, buffer cache, vacuum health, sequence limits, replication lag, and more.
- **Index Tuning:** Explore and recommend optimal indexes for your workload using advanced algorithms.
- **Query Plan Analysis:** Review and simulate EXPLAIN plans, including hypothetical indexes.
- **Schema Intelligence:** Context-aware SQL generation based on schema understanding.
- **Safe SQL Execution:** Configurable access control, including read-only mode and safe SQL parsing.
- **Agent Memory:** Demonstrates conversational memory across multiple queries.

## Structure

- [`ai_agent_postgres_mcp.ipynb`](ai_agent_postgres_mcp.ipynb): Interactive notebook for step-by-step exploration.
- [`main.py`](main.py): Script for running the agent in a standard Python environment.

## Requirements

- Python 3.8+
- Access to a running MCP server with a Postgres backend (see [MCP documentation](https://github.com/langchain-ai/langchain-mcp-adapters) for setup)
- A Postgres database (sample data: Northwind)
- API keys for Azure OpenAI (or compatible OpenAI endpoint)

### Python Dependencies

Install all dependencies with:

```sh
pip install -r requirements.txt
```

Or, for Colab/Notebook, see the `%pip install ...` lines in the notebook.

#### Main dependencies

- `langchain-mcp-adapters`
- `langgraph`
- `langchain_openai`
- `psycopg2-binary`
- `sqlalchemy`
- `pandas`
- `python-dotenv` (for `.env` support in `main.py`)

## Setup

1. **Clone the repository** and navigate to this directory.

2. **Prepare your environment variables**  
   Create a `.env` file in this directory with the following content:

   ```
   AZURE_OPENAI_API_KEY=your-azure-openai-key
   AZURE_OPENAI_ENDPOINT=https://your-azure-endpoint.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4.1
   MCP_RENDER_URL=https://your-mcp-server.onrender.com/sse
   ```

   Adjust the values as needed for your environment.

3. **(Optional) Load Sample Data**  
   The notebook includes commented code to load the Northwind sample database into your Postgres instance.

## Usage

### 1. Jupyter Notebook

Open [`ai_agent_postgres_mcp.ipynb`](ai_agent_postgres_mcp.ipynb) in Jupyter or Google Colab and follow the cells step by step:

- Install dependencies
- Connect to your Postgres database and verify data
- Configure the MCP client
- List available tools
- Set up the LLM (Azure OpenAI)
- Run agent queries and see conversational memory in action

### 2. Python Script

Edit your `.env` file as described above, then run:

```sh
python main.py
```

This will:

- Connect to your MCP server and Postgres database
- Ask "How many customers are in the customers table?"
- Follow up with "And how many orders are there?" (demonstrating memory)

## Example Output

```
--- Turn 1 ---
There are 91 customers in the customers table.

--- Turn 2 ---
There are 830 orders in the orders table.
```

## Customization

- Change the questions in `main.py` or the notebook to explore other database insights.
- Use the tools listed by `client.get_tools()` to see all available MCP capabilities.

## References

- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Northwind Postgres Sample](https://github.com/pthom/northwind_psql)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

## License

This project is for educational and experimental purposes. See the root [README.md](../README.md) for more details.