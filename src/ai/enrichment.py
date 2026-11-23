from ai.azure_dictionary_ai import (

    generate_definition,

    generate_synonyms

)


def enrich_columns(
    tables
):

    for table in tables:

        for column in table.columns:

            column.definition = (
                generate_definition(
                    column.name
                )
            )

            column.synonyms = (
                generate_synonyms(
                    column.name
                )
            )

    return tables