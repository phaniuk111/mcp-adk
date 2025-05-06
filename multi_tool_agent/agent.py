import datetime
from zoneinfo import ZoneInfo
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.sessions import InMemorySessionService

async def create_agent():
  """Gets tools from MCP Server."""
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
          command='uv',
          args=[    
             "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/phaneendrakumar/mcp-adk/gcloud_mcp.py"  # This is the path to your gcloud_mcp.py file change it accordingly
          ],
      )
  )

  agent = LlmAgent(
    name="Devops_Specialist",
    model="gemini-2.0-flash",
    description=(
        "Agent is a devops specialist working in google cloud platform. "
    ),
    instruction=(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
       "You are a seasoned DevOps Engineer with deep expertise in Google Cloud Platform. You can:"
       	"1.	Execute arbitrary gcloud CLI commands to inspect and manage GCP resources."
        "2.	Perform web searches to research issues, find best practices, and surface up-to-date documentation or examples."
        "3.	Combine live shell output with online resources to diagnose problems, propose fixes, and automate operational tasks."
    ),
    tools=tools,

)
  return agent, exit_stack


root_agent = create_agent()




