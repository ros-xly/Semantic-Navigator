def print_model_summary(tables):

    print("\nSEMANTIC MODEL SUMMARY\n")

    for table in tables:

        print(f"Table: {table.name}")

        print("Columns:")

        for column in table.columns:

            print(
                f"  - {column.name} ({column.data_type})"
            )

        print("Measures:")

        for measure in table.measures:

            print(
                f"  - {measure.name}"
            )

        print()