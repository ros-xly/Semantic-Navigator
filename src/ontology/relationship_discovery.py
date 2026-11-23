import os

from ai.azure_client import (
    client
)


def classify_relationship(
    source,
    target
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
                    (
                        f"""
Entity A:

{source}

Entity B:

{target}

Provide a short business
relationship label.

Examples:

Receives

Raises

Generates

Invoices

Charged To

Matched To

Return only label.
"""
                    )
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
        .strip()
    )