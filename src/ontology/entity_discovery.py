import os

from ai.azure_client import (
    client
)


def discover_entity(
    table_name
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
Convert this table
into a business entity.

Table:

{table_name}

Return only entity name.
"""
                }

            ]

        )
    )

    return (

        response.choices[0]
        .message.content
        .strip()

    )