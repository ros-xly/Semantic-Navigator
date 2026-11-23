def build_concept_tree(
    expanded_dependencies
):

    concepts = []

    for measure, fields in (
        expanded_dependencies.items()
    ):

        for field in fields:

            concepts.append(

                (
                    measure,
                    field
                )

            )

    return concepts