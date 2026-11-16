from ontology.ontology_models import (
    OntologyNode
)

from ontology.domain_classifier import (
    classify_domain
)

def generate_nodes(
    tables
):
    nodes = []
    for table in tables:

        for column in table.columns:

            node = OntologyNode(

                domain=
                classify_domain(
                    column.name
                ),

                concept=
                column.name,

                source_type="Column"
            )

            nodes.append(node)

        for measure in table.measures:

        node = OntologyNode(

            domain=
            classify_domain(
                measure.name
            ),

            concept=
            measure.name,

            source_type="Measure"
        )

        nodes.append(node)

    return nodes
