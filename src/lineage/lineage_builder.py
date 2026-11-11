from lineage.dependency_parser import (
    extract_dependencies
)


def build_lineage(tables):

    lineage = []

    for table in tables:

        for measure in table.measures:

            dependencies = extract_dependencies(
                measure.expression
            )

            lineage.append(
                {
                    "measure": measure.name,
                    "dependencies": dependencies
                }
            )

    return lineage