def print_ontology_summary(
    ontology
):

    print(
        "\nBUSINESS ONTOLOGY\n"
    )

    for process, tables in (

        ontology.items()

    ):

        print(
            f"\n{process}"
        )

        for table in tables:

            print(
                f"  - {table}"
            )