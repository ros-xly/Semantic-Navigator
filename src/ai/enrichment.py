from ai.mock_dictionary_ai import (
    generate_definition,
    generate_synonyms,
    generate_domain
)

def enrich_columns(tables):

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

            column.business_domain = (
                generate_domain(
                    column.name
                )
            )

    return tables

