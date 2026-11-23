from pathlib import Path

from openpyxl import Workbook


def create_data_dictionary(
    tables,
    model_name,
    lineage=None,
    impact=None,
    ontology=None,
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
            "Business Domain",
            "Synonyms"
        ]
    )

    for table in tables:

        for column in table.columns:

            synonyms = ""

            if column.synonyms:
                synonyms = ", ".join(
                    column.synonyms
                )

            dictionary_sheet.append(
                [
                    table.name,
                    column.name,
                    column.data_type,
                    column.definition,
                    column.business_domain,
                    synonyms
                ]
            )

    # =====================================
    # DEPENDENCY LOOKUP
    # =====================================

    dependency_map = {}

    if lineage:

        for item in lineage:

            dependency_map[
                item["measure"]
            ] = ", ".join(
                item["dependencies"]
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

    expanded_dependencies = {}

    if lineage:

        from measures.measure_dependency_expander import (
            expand_measure_dependencies
        )

        expanded_dependencies = (
            expand_measure_dependencies(
                lineage
            )
        )

    from ai.measure_classifier import (
        classify_measure
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
                    measure.definition,
                    measure_type,
                    fields
                ]
            )


    # =====================================
    # ONTOLOGY
    # =====================================

    if ontology:

        ontology_sheet = workbook.create_sheet(
            "Ontology"
        )

        ontology_sheet.append(
            [
                "Domain",
                "Concept",
                "Source Type"
            ]
        )

        for node in ontology:

            ontology_sheet.append(
                [
                    node.domain,
                    node.concept,
                    node.source_type
                ]
            )

    # =====================================
    # GOVERNANCE
    # =====================================

    if governance_summary:

        governance_sheet = workbook.create_sheet(
            "Governance"
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
                column[0].column_letter
            )

            for cell in column:

                try:

                    length = len(
                        str(cell.value)
                    )

                    if length > max_length:

                        max_length = length

                except Exception:

                    pass

            sheet.column_dimensions[
                column_letter
            ].width = max_length + 4

    # =====================================
    # SAVE FILE
    # =====================================

    output_file = Path(
        rf"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\outputs\{model_name}_Documentation.xlsx"
    )

    workbook.save(
        output_file
    )

    print(
        f"Workbook saved to: {output_file}"
    )