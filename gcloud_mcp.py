"""
MCP server exposing Google‑Cloud Recommender data.

Run with:
    python gcp_recommender_server.py          (stdio transport – Claude Desktop, Cursor, etc.)
or:
    python gcp_recommender_server.py --http   (HTTP transport for browsers / reverse proxies)
"""

from __future__ import annotations

import asyncio
import json
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP          
from utils import GcloudTool

# Initialise both the MCP server  the underlying GCP client
mcp = FastMCP("gcp-recommender")                
          
tool = GcloudTool.initialize(debug=True)



# Each @mcp.tool decorated async‑def automatically becomes an MCP tool definition
@mcp.tool()
async def run_gcloud_command(input_cmd: str) -> str:
    """
    Execute any 'gcloud …' command and return only its stdout.
    Args:
        input_cmd: A string beginning with 'gcloud' (e.g.
                   "gcloud projects list --format=json")

    Returns:
        The command’s stdout (empty string on failure). 
    """
    success, stdout, stderr = await tool.run(input_cmd)
    return stdout