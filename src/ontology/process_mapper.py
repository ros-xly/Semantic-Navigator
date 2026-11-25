import os
import json

from ai.azure_client import (
    client
)


def discover_processes(
    tables
):

    table_names = [

        table.name

        for table in tables

    ]

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

Review the table names.

Identify:

Domain

Capability

Process

Table

Return JSON array.

Example:

[
    {
        "domain":
            "Procurement",

        "capability":
            "Purchase To Pay",

        "process":
            "Invoice Processing",

        "table":
            "Invoice"
    }
]
"""
                },

                {
                    "role": "user",

                    "content":

                    "\n".join(
                        table_names
                    )

                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
    )