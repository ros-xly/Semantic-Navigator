def score_ontology(
    ontology
):

    total_concepts = len(
        ontology
    )

    general_concepts = 0

    domains = set()

    for node in ontology:

        domains.add(
            node.domain
        )

        if node.domain == "General":

            general_concepts += 1

    coverage = round(
        (
            (
                total_concepts
                - general_concepts
            )
            /
            total_concepts
        )
        * 100,
        2
    )

    print("\nONTOLOGY SCORE\n")

    print(
        f"Domains Identified: {len(domains)}"
    )

    print(
        f"Concepts Identified: {total_concepts}"
    )

    print(
        f"General Concepts: {general_concepts}"
    )

    print(
        f"Coverage: {coverage}%"
    )