def expand_measure_dependencies(
    lineage
):

    lookup = {}

    for item in lineage:

        lookup[
            item["measure"]
        ] = item["dependencies"]

    expanded = {}

    for measure, dependencies in lookup.items():

        fields = []

        for dependency in dependencies:

            if dependency in lookup:

                child_fields = ", ".join(
                    lookup[dependency]
                )

                fields.append(
                    f"{dependency} ({child_fields})"
                )

            else:

                fields.append(
                    dependency
                )

        expanded[
            measure
        ] = fields

    return expanded