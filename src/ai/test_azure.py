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


response = client.chat.completions.create(

    model=os.getenv(
        "AZURE_OPENAI_MODEL"
    ),

    messages=[

        {
            "role": "user",

            "content":
            (
                "Provide a business definition "
                "for SalesAmount."
            )
        }

    ]

)

print(

    response.choices[0]
    .message.content

)