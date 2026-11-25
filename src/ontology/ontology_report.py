def print_ontology_summary(
    ontology
):

    print(
        "\nBUSINESS ARCHITECTURE\n"
    )

    for item in ontology:

        print(

            f"{item.domain} | "
            f"{item.capability} | "
            f"{item.process} | "
            f"{item.table}"

        )