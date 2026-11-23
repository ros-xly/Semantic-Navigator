import os

from ai.azure_client import (
    client
)


def generate_definition(
    field_name
):

    response = (
        client.chat.completions.create(

            model=os.getenv(
                "AZURE_OPENAI_MODEL"
            ),

            messages=[

                {
                    "role": "system",

                    "content":
                    """
You are creating a business glossary.

Provide a plain-English business definition.

Rules:

- Do not repeat the field name
- Do not start with:
  'This field'
  'The field'
- Do not mention:
  columns
  tables
  datasets
  semantic models
- Maximum 30 words
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

    response = (
        client.chat.completions.create(

            model=os.getenv(
                "AZURE_OPENAI_MODEL"
            ),

            messages=[

                {
                    "role": "user",

                    "content":
                    f"""
Provide three business synonyms.

Return only comma-separated values.

Field:

{field_name}
"""
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
        .split(",")
    )
