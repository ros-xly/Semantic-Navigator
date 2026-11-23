import os

from ai.azure_client import (
    client
)


def discover_processes(
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
Identify business processes.

Examples:

Purchase to Pay

Order to Cash

Recruit to Retire

Plan to Produce
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