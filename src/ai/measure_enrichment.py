from ai.mock_measure_ai import (
    generate_measure_definition,
    generate_measure_purpose,
    generate_friendly_name
)

def enrich_measures(
    tables
):

    for table in tables:

        for measure in table.measures:

            measure.definition = (
                generate_measure_definition(
                    measure.name
                )
            )

            measure.purpose = (
                generate_measure_purpose(
                    measure.name
                )
            )

            measure.friendly_name = (
                generate_friendly_name(
                    measure.name
                )
            )

    return tables

