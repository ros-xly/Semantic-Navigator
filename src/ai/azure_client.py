import os

from dotenv import load_dotenv

from openai import AzureOpenAI


load_dotenv()


client = AzureOpenAI(

    api_key=os.getenv(
        "AZURE_OPENAI_KEY"
    ),

    api_version="2024-10-21",

    azure_endpoint=os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

)