def build_entity_catalogue(
    tables
):

    entities = []

    for table in tables:

        entities.append(
            table.name
        )

    return entities