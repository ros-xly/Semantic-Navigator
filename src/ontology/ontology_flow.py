import json

from ontology.process_relationships import (
    discover_process_flow
)


def build_process_flow(
    ontology
):

    response = (
        discover_process_flow(
            ontology
        )
    )

    return json.loads(
        response
    )