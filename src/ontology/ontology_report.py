def print_ontology_summary(
    ontology
):

    print("\nONTOLOGY\n")

    if not ontology:

        print(
            "No ontology generated."
        )

        return

    for parent, child in ontology:

        print(
            f"{parent} -> {child}"
        )
