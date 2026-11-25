from src.parser.models import (
    Column,
    Measure,
    Table
)


def parse_tmdl_file(
    file_path: str
) -> Table:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

    table_name = ""

    columns = []

    measures = []

    current_column = None

    index = 0

    while index < len(lines):

        stripped = lines[
            index
        ].strip()

        # =====================
        # TABLE
        # =====================

        if stripped.startswith(
            "table "
        ):

            table_name = (
                stripped
                .replace(
                    "table ",
                    ""
                )
                .strip()
            )

        # =====================
        # COLUMN
        # =====================

        elif stripped.startswith(
            "column "
        ):

            column_name = (
                stripped
                .replace(
                    "column ",
                    ""
                )
                .strip()
            )

            current_column = Column(

                name=column_name,

                data_type=""

            )

            columns.append(
                current_column
            )

        elif stripped.startswith(
            "dataType:"
        ):

            if current_column:

                current_column.data_type = (

                    stripped.replace(
                        "dataType:",
                        ""
                    ).strip()

                )

        # =====================
        # MEASURE
        # =====================

        elif stripped.startswith(
            "measure "
        ):

            measure_name = (

                stripped.replace(
                    "measure ",
                    ""
                )
                .split("=")[0]
                .strip()

            )

            expression_lines = []

            next_index = (
                index + 1
            )

            while (

                next_index < len(lines)

                and not lines[
                    next_index
                ].strip().startswith(
                    "measure "
                )

                and not lines[
                    next_index
                ].strip().startswith(
                    "column "
                )

            ):

                expression_lines.append(

                    lines[
                        next_index
                    ].rstrip()

                )

                next_index += 1

            expression = "\n".join(
                expression_lines
            )

            measures.append(

                Measure(

                    name=measure_name,

                    expression=expression

                )

            )

        index += 1

    return Table(

        name=table_name,

        columns=columns,

        measures=measures

    )