import json
import os

from ai.azure_client import (
    client
)


def discover_process_groups(
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
You are a procurement architect.

Group these tables
into business processes.

Return JSON.

Example:

{
    "Supplier Management":
    [
        "Supplier"
    ],

    "Purchase Ordering":
    [
        "PurchaseOrder",
        "PurchaseOrderLine"
    ]
}
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

    return json.loads(

        response.choices[0]
        .message.content

    )