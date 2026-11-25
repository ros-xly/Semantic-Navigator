def find_unclassified(
    tables,
    ontology
):

    classified = set()

    for item in ontology:

        classified.add(
            item.table
        )

    return [

        table.name

        for table in tables

        if table.name
        not in classified

    ]