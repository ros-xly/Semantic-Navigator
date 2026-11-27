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
                    "role": "system",

                    "content":
                    """
Convert table names
into business entities.

Examples:

P2P_Purchase_Orders
    -> Purchase Order

P2P_Invoice_Details
    -> Invoice

Master_CostCentre
    -> Cost Centre

Return only entity name.
"""
                },

                {
                    "role": "user",

                    "content":
                    table_name
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
        .strip()
    )