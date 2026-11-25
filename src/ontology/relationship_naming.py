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
                    "role": "user",

                    "content":
                    f"""
Source:

{source_entity}

Target:

{target_entity}

Provide business
relationship.

Examples:

Receives

Generates

Charged To

Creates

Is Matched To

Return only phrase.
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