from pathlib import Path

from src.parser.models import Column, Measure, Table

def parse_tmdl_file(file_path: str) -> Table:
    
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    table_name = ""
    columns = []
    measures = []

    current_column = None

    for line in lines:

        stripped = line.strip()

        if stripped.startswith("table "):
            table_name = stripped.replace("table ", "").strip()

        elif stripped.startswith("column "):
            column_name = stripped.replace("column ", "").strip()

            current_column = Column(
                name=column_name,
                data_type=""
            )

            columns.append(current_column)

        elif stripped.startswith("dataType:"):

            if current_column:
                current_column.data_type = (
                    stripped.replace("dataType:", "").strip()
                )

        elif stripped.startswith("measure "):

            measure_name = (
                stripped.replace("measure ", "")
                .split("=")[0]
                .strip()
            )

            measures.append(
                Measure(
                    name=measure_name,
                    expression=""
                )
            )

    return Table(
        name=table_name,
        columns=columns,
        measures=measures
    )