from pathlib import Path


def parse_relationships(
    model_folder
):

    relationships = []

    relationship_file = (
        Path(model_folder)
        .parent
        / "relationships.tmdl"
    )

    if not relationship_file.exists():

        return relationships

    with open(
        relationship_file,
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

    from_table = None

    to_table = None

    for line in lines:

        stripped = line.strip()

        if "fromTable:" in stripped:

            from_table = (
                stripped
                .replace(
                    "fromTable:",
                    ""
                )
                .strip()
            )

        if "toTable:" in stripped:

            to_table = (
                stripped
                .replace(
                    "toTable:",
                    ""
                )
                .strip()
            )

            relationships.append(

                (
                    from_table,
                    to_table
                )

            )

    return relationships