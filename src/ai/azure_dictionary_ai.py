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
                    (
                        "You are a data governance specialist."
                    )
                },

                {
                    "role": "user",

                    "content":
                    (
                        f"""
Provide a concise business definition
for the following field.

Field:

{field_name}

Return only the definition.
"""
                    )
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
        .strip()
    )