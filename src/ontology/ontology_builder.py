from measures.measure_dependency_expander import (
    expand_measure_dependencies
)

from ontology.concept_builder import (
    build_concept_tree
)


def build_ontology(
    tables,
    lineage
):

    expanded_dependencies = (
        expand_measure_dependencies(
            lineage
        )
    )

    ontology = (
        build_concept_tree(
            expanded_dependencies
        )
    )

    return ontology
