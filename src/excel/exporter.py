from openpyxl import Workbook


def create_data_dictionary(tables):

    workbook = Workbook()

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

    workbook.save(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\outputs\DataDictionary.xlsx"
)