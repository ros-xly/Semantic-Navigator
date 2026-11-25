from ontology.business_relationship import (
    BusinessRelationship
)

from ontology.entity_discovery import (
    discover_entity
)

from ontology.relationship_naming import (
    discover_relationship
)


def build_relationships(
    relationships
):

    output = []

    for source, target in relationships:

        source_table = (
            source.split(".")[0]
        )

        source_column = (
            source.split(".")[1]
        )

        target_table = (
            target.split(".")[0]
        )

        target_column = (
            target.split(".")[1]
        )

        source_entity = (
            discover_entity(
                source_table
            )
        )

        target_entity = (
            discover_entity(
                target_table
            )
        )

        relationship = (
            discover_relationship(
                source_entity,
                target_entity
            )
        )

        output.append(

            BusinessRelationship(

                source_entity=
                source_entity,

                source_table=
                source_table,

                source_column=
                source_column,

                relationship=
                relationship,

                target_entity=
                target_entity,

                target_table=
                target_table,

                target_column=
                target_column,

                description=
                (
                    f"{source_entity} "
                    f"{relationship} "
                    f"{target_entity}"
                )

            )

        )

    return output