import os

from ai.azure_client import (
    client
)


def generate_ontology_story(
    ontology
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
Describe the business
process architecture.
"""
                },

                {
                    "role": "user",

                    "content":

                    str(
                        ontology
                    )

                }

            ]

        )
    )

    return (
        response.choices[0]
        .message.content
    )