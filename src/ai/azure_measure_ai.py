import os

from ai.azure_client import (
    client
)


def generate_measure_definition(
    measure_name
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
You are creating a business glossary.

Provide a short business
definition.

Do not repeat the measure name.

Maximum 25 words.
"""
                },

                {
                    "role": "user",

                    "content":
                    measure_name
                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
        .strip()
    )


def generate_measure_purpose(
    measure_name
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
Describe the business purpose
of this KPI:

{measure_name}

One sentence only.
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


def generate_friendly_name(
    measure_name
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
Convert this measure
into a user-friendly
business name.

Measure:

{measure_name}

Return only the name.
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