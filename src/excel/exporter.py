from pathlib import Path

from openpyxl import Workbook


def create_data_dictionary(
    tables,
    lineage=None,
    impact=None
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
    # BUILD DEPENDENCY LOOKUP
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
            "Friendly Name",
            "Definition",
            "Purpose",
            "Dependencies"
        ]
    )

    for table in tables:

        for measure in table.measures:

            measure_sheet.append(
                [
                    measure.name,
                    measure.friendly_name,
                    measure.definition,
                    measure.purpose,
                    dependency_map.get(
                        measure.name,
                        ""
                    )
                ]
            )

    # =====================================
    # LINEAGE SHEET
    # =====================================

    if lineage:

        lineage_sheet = workbook.create_sheet(
            "Lineage"
        )

        lineage_sheet.append(
            [
                "Measure",
                "Dependencies"
            ]
        )

        for item in lineage:

            lineage_sheet.append(
                [
                    item["measure"],
                    ", ".join(
                        item["dependencies"]
                    )
                ]
            )

    # =====================================
    # IMPACT ANALYSIS SHEET
    # =====================================

    if impact:

        impact_sheet = workbook.create_sheet(
            "Impact Analysis"
        )

        impact_sheet.append(
            [
                "Field",
                "Used In"
            ]
        )

        for field, measures in impact.items():

            impact_sheet.append(
                [
                    field,
                    ", ".join(
                        measures
                    )
                ]
            )

    # =====================================
    # FORMAT COLUMNS
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

                    if value_length > max_length:
                        max_length = value_length

                except Exception:
                    pass

            adjusted_width = (
                max_length + 4
            )

            sheet.column_dimensions[
                column_letter
            ].width = adjusted_width

    # =====================================
    # SAVE FILE
    # =====================================

    output_file = Path(
        r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\outputs\DataDictionary.xlsx"
    )

    workbook.save(
        output_file
    )

    print(
        f"Workbook saved to: {output_file}"
    )