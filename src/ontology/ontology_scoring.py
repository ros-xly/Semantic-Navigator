def score_ontology(
    ontology
):

    total_concepts = len(
        ontology
    )

    if total_concepts == 0:

        print("\nONTOLOGY SCORE\n")

        print(
            "No ontology concepts found."
        )

        return

    print("\nONTOLOGY SCORE\n")

    print(
        f"Concepts Identified: {total_concepts}"
    )