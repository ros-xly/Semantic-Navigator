from ontology.process_mapper import (
    discover_processes
)


def build_ontology(
    tables,
    lineage=None
):

    ontology = (
        discover_processes(
            tables
        )
    )

    return ontology