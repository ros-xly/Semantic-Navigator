import os

from pathlib import Path

from ai.azure_client import (
    client
)


def load_business_context():

    context_file = Path(
        r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src\ai\business_context.txt"
    )

    if not context_file.exists():

        return ""

    return context_file.read_text(
        encoding="utf-8"
    )


def generate_definition(
    field_name
):

    business_context = (
        load_business_context()
    )

    response = (
        client.chat.completions.create(

            model=os.getenv(
                "AZURE_OPENAI_MODEL"
            ),

            messages=[

                {
                    "role": "system",

                    "content":
                    f"""
You are creating an MMCG business glossary.

Business Context:

{business_context}

Rules:

- Use MMCG terminology
- Keep language business-friendly
- Be specific
- Do not repeat the field name
- Do not start with:
    This field
    The field
- Do not mention:
    table
    column
    dataset
    semantic model
- Maximum 30 words
- Use consistent terminology across all definitions
"""
                },

                {
                    "role": "user",

                    "content":
                    field_name
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
        .strip()
    )


def generate_synonyms(
    field_name
):

    business_context = (
        load_business_context()
    )

    response = (
        client.chat.completions.create(

            model=os.getenv(
                "AZURE_OPENAI_MODEL"
            ),

            messages=[

                {
                    "role": "system",

                    "content":
                    f"""
Business Context:

{business_context}

Return exactly three business synonyms.

Only comma separated values.
"""
                },

                {
                    "role": "user",

                    "content":
                    field_name
                }

            ]

        )
    )

    return (

        response.choices[0]
        .message.content
        .split(",")

    )