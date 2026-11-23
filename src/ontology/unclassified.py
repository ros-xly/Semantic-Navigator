def find_unclassified(
    tables,
    ontology
):

    linked = set()

    for source, _, target in ontology:

        linked.add(
            source
        )

        linked.add(
            target
        )

    unclassified = []

    for table in tables:

        if table.name not in linked:

            unclassified.append(
                table.name
            )

    return unclassified