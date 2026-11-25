def find_unclassified(
    tables,
    ontology
):

    classified = set()

    for process, process_tables in (

        ontology.items()

    ):

        for table in process_tables:

            classified.add(
                table
            )

    unclassified = []

    for table in tables:

        if (
            table.name
            not in classified
        ):

            unclassified.append(
                table.name
            )

    return sorted(
        list(
            set(
                unclassified
            )
        )
    )