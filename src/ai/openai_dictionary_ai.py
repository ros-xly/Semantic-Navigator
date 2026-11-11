import os

from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def test_connection():

    response = client.responses.create(
        model="gpt-5",
        input="Explain SalesAmount in one sentence."
    )

    return response.output_text