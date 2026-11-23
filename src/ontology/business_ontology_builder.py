from ontology.relationship_discovery import (
    classify_relationship
)


def build_business_ontology(
    relationships
):

    ontology = []

    for source, target in relationships:

        relationship = (
            classify_relationship(
                source,
                target
            )
        )

        ontology.append(

            (
                source,
                relationship,
                target
            )

        )

    return ontology