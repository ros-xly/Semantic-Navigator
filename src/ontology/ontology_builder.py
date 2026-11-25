from ontology.process_mapper import (
    discover_processes
)

from ontology.process_parser import (
    parse_process_response
)


def build_ontology(
    tables,
    lineage=None
):

    response = (
        discover_processes(
            tables
        )
    )

    return (
        parse_process_response(
            response
        )
    )