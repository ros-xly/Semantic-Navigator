from pathlib import Path

from openpyxl import Workbook


def create_data_dictionary(
    tables,
    model_name,
    ontology=None,
    unclassified=None,
    governance_summary=None
):

    workbook = Workbook()

    # =====================================
    # DATA DICTIONARY
    # =====================================

    dictionary_sheet = workbook.active

    dictionary_sheet.title = "Data Dictionary"

    dictionary_sheet.append(
        [
            "Table",
            "Field",
            "Data Type",
            "Definition",
            "Synonyms"
        ]
    )

    for table in tables:

        for column in table.columns:

            synonyms = ""

            if hasattr(
                column,
                "synonyms"
            ) and column.synonyms:

                synonyms = ", ".join(
                    column.synonyms
                )

            dictionary_sheet.append(
                [
                    table.name,
                    column.name,
                    column.data_type,
                    getattr(
                        column,
                        "definition",
                        ""
                    ),
                    synonyms
                ]
            )

    # =====================================
    # MEASURES
    # =====================================

    measure_sheet = workbook.create_sheet(
        "Measures"
    )

    measure_sheet.append(
        [
            "Measure",
            "Definition",
            "Type",
            "Fields"
        ]
    )

    from lineage.lineage_builder import (
        build_lineage
    )

    from measures.measure_dependency_expander import (
        expand_measure_dependencies
    )

    from ai.measure_classifier import (
        classify_measure
    )

    lineage = build_lineage(
        tables
    )

    expanded_dependencies = (
        expand_measure_dependencies(
            lineage
        )
    )

    for table in tables:

        for measure in table.measures:

            measure_type = (
                classify_measure(
                    measure.expression
                )
            )

            fields = ", ".join(
                expanded_dependencies.get(
                    measure.name,
                    []
                )
            )

            measure_sheet.append(
                [
                    measure.name,
                    getattr(
                        measure,
                        "definition",
                        ""
                    ),
                    measure_type,
                    fields
                ]
            )

    # =====================================
    # BUSINESS ONTOLOGY
    # =====================================

        if ontology:

            ontology_sheet = workbook.create_sheet(
                "Business Ontology"
            )

            ontology_sheet.append(
                [
                    "Domain",
                    "Capability",
                    "Process",
                    "Table"
                ]
            )

            for item in ontology:

                ontology_sheet.append(
                    [
                        item.domain,
                        item.capability,
                        item.process,
                        item.table
                    ]
                )

            if unclassified:

                sheet = workbook.create_sheet(
                    "Unclassified"
                )

                sheet.append(
                    [
                        "Table"
                    ]
                )

                for table_name in unclassified:

                    sheet.append(
                        [
                            table_name
                        ]
                    )
    # =====================================
    # UNCLASSIFIED
    # =====================================

    if unclassified:

        unclassified_sheet = (
            workbook.create_sheet(
                "Unclassified"
            )
        )

        unclassified_sheet.append(
            [
                "Table"
            ]
        )

        for table_name in unclassified:

            unclassified_sheet.append(
                [
                    table_name
                ]
            )

    # =====================================
    # GOVERNANCE
    # =====================================

    if governance_summary:

        governance_sheet = (
            workbook.create_sheet(
                "Governance"
            )
        )

        governance_sheet.append(
            [
                "Metric",
                "Score"
            ]
        )

        for metric, score in governance_summary:

            governance_sheet.append(
                [
                    metric,
                    score
                ]
            )

    # =====================================
    # AUTO SIZE COLUMNS
    # =====================================

    for sheet in workbook.worksheets:

        for column in sheet.columns:

            max_length = 0

            column_letter = (
                column[0]
                .column_letter
            )

            for cell in column:

                try:

                    value_length = len(
                        str(cell.value)
                    )

                    if (
                        value_length
                        > max_length
                    ):

                        max_length = (
                            value_length
                        )

                except Exception:

                    pass

            sheet.column_dimensions[
                column_letter
            ].width = (
                max_length + 4
            )

    # =====================================
    # SAVE
    # =====================================

    from datetime import datetime

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = Path(
        rf"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\outputs\{model_name}_Documentation_{timestamp}.xlsx"
    )

    workbook.save(
        output_file
    )

    print(
        f"Workbook saved to: {output_file}"
    )