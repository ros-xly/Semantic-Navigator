from pathlib import Path

from openpyxl import Workbook


def create_data_dictionary(
    tables,
    lineage=None,
    impact=None
):

    workbook = Workbook()

    # -------------------------
    # Data Dictionary
    # -------------------------

    sheet = workbook.active

    sheet.title = "Data Dictionary"

    sheet.append(
        [
            "Table",
            "Field",
            "Data Type"
        ]
    )

    for table in tables:

        for column in table.columns:

            sheet.append(
                [
                    table.name,
                    column.name,
                    column.data_type
                ]
            )

    # -------------------------
    # Lineage Sheet
    # -------------------------

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
                    ", ".join(item["dependencies"])
                ]
            )

    # -------------------------
    # Impact Sheet
    # -------------------------

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
                    ", ".join(measures)
                ]
            )

    # -------------------------
    # Save
    # -------------------------

    output_file = Path(
        r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\outputs\DataDictionary.xlsx"
    )

    workbook.save(output_file)

    print(
        f"Workbook saved to: {output_file}"
    )