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
    # LINEAGE
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
    # IMPACT ANALYSIS
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
                    ", ".join(measures)
                ]
            )

    # =====================================
    # SAVE FILE
    # =====================================

    output_file = Path(
        r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\outputs\DataDictionary.xlsx"
    )

    workbook.save(output_file)

    print(
        f"Workbook saved to: {output_file}"
    )