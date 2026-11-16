def print_processing_report(
    model_name,
    tables
):

    table_count = len(
        tables
    )

    column_count = sum(
        len(table.columns)
        for table in tables
    )

    measure_count = sum(
        len(table.measures)
        for table in tables
    )

    print("\nPROCESSING SUMMARY\n")

    print(
        f"Model: {model_name}"
    )

    print(
        f"Tables: {table_count}"
    )

    print(
        f"Columns: {column_count}"
    )

    print(
        f"Measures: {measure_count}"
    )