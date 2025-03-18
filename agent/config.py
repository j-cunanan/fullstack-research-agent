from langchain_openai import AzureChatOpenAI, ChatOpenAI
import getpass
import os


if "AZURE_OPENAI_API_KEY" not in os.environ:
    os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass(
        "Enter your AzureOpenAI API key: "
    )
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://jayso-m86ldqty-eastus2.cognitiveservices.azure.com/"


# Description: Configuration file
class Config:
    def __init__(self):
        """
        Initializes the configuration for the agent
        """
        self.BASE_LLM = ChatOpenAI(model="gpt-4", temperature=0.2)
        self.FACTUAL_LLM = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
        # self.BASE_LLM = AzureChatOpenAI(
        #     azure_deployment="gpt-4o-mini",  # or your deployment
        #     api_version="2024-10-21",  # or your api version
        #     temperature=0,
        #     max_tokens=None,
        #     timeout=None,
        #     max_retries=2,
        #     # other params...
        # )
        # self.FACTUAL_LLM = AzureChatOpenAI(
        #     azure_deployment="gpt-4o-mini",  # or your deployment
        #     api_version="2024-10-21",  # or your api version
        #     temperature=0,
        #     max_tokens=None,
        #     timeout=None,
        #     max_retries=2,
        #     # other params...
        # )
        self.DEBUG = False
