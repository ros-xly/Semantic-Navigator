import os

from ai.azure_client import (
    client
)


def discover_relationship(
    source_entity,
    target_entity
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
Provide a business relationship.

Examples:

Receives

Creates

Generates

Is Matched To

Charged To

Belongs To

Return only the phrase.
"""
                },

                {
                    "role": "user",

                    "content":
                    f"""
Source Entity:

{source_entity}

Target Entity:

{target_entity}
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