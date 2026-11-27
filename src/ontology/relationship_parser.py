from pathlib import Path


def parse_relationships(
    model_path
):

    relationships = []

    relationship_file = (
        Path(
            model_path
        ).parent
        / "relationships.tmdl"
    )

    if not relationship_file.exists():

        return relationships

    with open(
        relationship_file,
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

    source = None

    target = None

    for line in lines:

        stripped = line.strip()

        if stripped.startswith(
            "fromColumn:"
        ):

            source = (
                stripped.replace(
                    "fromColumn:",
                    ""
                )
                .strip()
            )

        elif stripped.startswith(
            "toColumn:"
        ):

            target = (
                stripped.replace(
                    "toColumn:",
                    ""
                )
                .strip()
            )

            relationships.append(
                (
                    source,
                    target
                )
            )

    return relationships
