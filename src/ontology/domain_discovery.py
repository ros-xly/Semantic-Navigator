import os

from ai.azure_client import (
    client
)


def discover_domain(
    entities
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
You are an enterprise architect.

Identify the business domain.

Examples:

Procurement
Finance
Operations
Workforce
Customer
Supply Chain
"""
                },

                {
                    "role": "user",

                    "content":

                    "\n".join(
                        entities
                    )

                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
    )