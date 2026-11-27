from pathlib import Path

from datetime import datetime

from openpyxl import Workbook


def create_data_dictionary(
    tables,
    model_name,
    relationships=None,
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
    # ENTITY RELATIONSHIPS
    # =====================================

    if relationships:

        sheet = workbook.create_sheet(
            "Entity Relationships"
        )

        sheet.append(
            [
                "Source Entity",
                "Source Table",
                "Source Field",
                "Relationship",
                "Target Entity",
                "Target Table",
                "Target Field"
            ]
        )

        for relationship in relationships:

            sheet.append(
                [
                    relationship.source_entity,
                    relationship.source_table,
                    relationship.source_column,
                    relationship.relationship,
                    relationship.target_entity,
                    relationship.target_table,
                    relationship.target_column
                ]
            )

    # =====================================
    # RELATIONSHIP METADATA
    # =====================================

    if relationships:

        sheet = workbook.create_sheet(
            "Relationship Metadata"
        )

        sheet.append(
            [
                "Source Table",
                "Source Column",
                "Target Table",
                "Target Column",
                "Description"
            ]
        )

        for relationship in relationships:

            sheet.append(
                [
                    relationship.source_table,
                    relationship.source_column,
                    relationship.target_table,
                    relationship.target_column,
                    relationship.description
                ]
            )

    # =====================================
    # GOVERNANCE
    # =====================================

    if governance_summary:

        sheet = workbook.create_sheet(
            "Governance"
        )

        sheet.append(
            [
                "Metric",
                "Score"
            ]
        )

        for metric, score in governance_summary:

            sheet.append(
                [
                    metric,
                    score
                ]
            )

    # =====================================
    # FORMAT
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

                    if cell.value:

                        max_length = max(
                            max_length,
                            len(
                                str(
                                    cell.value
                                )
                            )
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
        f"\nWorkbook saved to:\n{output_file}"
    )