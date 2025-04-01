import os
import httpx
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from tavily import AsyncTavilyClient
from typing import List, Optional, Dict, Sequence
from copilotkit.langchain import copilotkit_emit_state
from langchain_core.runnables import RunnableConfig

class CustomAsyncTavilyClient(AsyncTavilyClient):
        def __init__(self, api_key: Optional[str] = None, 
                    company_info_tags: Sequence[str] = ("news", "general", "finance")):
            if api_key is None:
                api_key = os.getenv("TAVILY_API_KEY")
                
            # Skip calling parent's __init__ and implement the same logic but with verify=False
            self._client_creator = lambda: httpx.AsyncClient(
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                base_url="https://api.tavily.com",
                timeout=180,
                verify=False
            )
            self._company_info_tags = company_info_tags
            
# tavily_client = AsyncTavilyClient()
tavily_client = CustomAsyncTavilyClient()


class TavilyExtractInput(BaseModel):
    urls: List[str] = Field(description="List of a single or several URLs for extracting raw content to gather additional information")
    state: Optional[Dict] = Field(description="State of the research")


@tool("tavily_extract", args_schema=TavilyExtractInput, return_direct=True)
async def tavily_extract(urls, state):
    """Perform full scrape to a provided list of urls."""

    try:
        response = await tavily_client.extract(urls=urls)
        results = response['results']
        # Match and add raw_content to urls in state
        tool_msg = "Extracted raw content to gather additional information from the following sources:\n"
        for itm in results:
            url = itm['url']
            raw_content = itm['raw_content']
            if url in state["sources"]:
                state["sources"][url]['raw_content'] = raw_content
            else:
                state["sources"][url] = {'raw_content': raw_content}
            tool_msg += f"{url}\n"

        config = RunnableConfig()
        state["logs"] = state.get("logs", [])
        state["logs"].append({
            "message": "🚀 Extracting additional content from valuable sources",
            "done": True
        })
        await copilotkit_emit_state(config, state)
        return state, tool_msg

    except Exception as e:
        print(f"Error occurred during extract: {str(e)}")
        return state, ""

