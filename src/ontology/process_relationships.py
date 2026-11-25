import os

from ai.azure_client import (
    client
)


def discover_process_flow(
    processes
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

Identify relationships
between business processes.

Return JSON list.

Example:

[
    {
        "source":
            "Supplier Management",

        "relationship":
            "Supplies",

        "target":
            "Purchase Ordering"
    }
]
"""
                },

                {
                    "role": "user",

                    "content":
                    str(
                        processes
                    )
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
    )