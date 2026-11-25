import json
import os

from ai.azure_client import (
    client
)


def discover_processes(
    tables
):

    table_names = sorted(

        [
            table.name

            for table in tables

            if not (
                table.name.startswith(
                    "LocalDateTable"
                )
            )
        ]

    )

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

Analyse ALL table names together.

Do NOT classify tables individually.

Create business process groups.

Return ONLY JSON.

Example:

{
    "Supplier Management":
    [
        "Supplier",
        "SupplierContact"
    ],

    "Purchase Ordering":
    [
        "PurchaseOrder",
        "PurchaseOrderLine"
    ],

    "Invoice Processing":
    [
        "Invoice",
        "InvoiceLine"
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

    result = (
        response.choices[0]
        .message.content
    )

    result = (
        result
        .replace(
            "```json",
            ""
        )
        .replace(
            "```",
            ""
        )
        .strip()
    )

    try:

        return json.loads(
            result
        )

    except Exception:

        return {
            "Unknown":
            table_names
        }