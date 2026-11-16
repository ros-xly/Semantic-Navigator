def print_ontology_summary(
    ontology
):

    print("\nONTOLOGY\n")

    domains = {}

    for node in ontology:

        if node.domain not in domains:

            domains[node.domain] = []

        domains[node.domain].append(
            node.concept
        )

    for domain, concepts in domains.items():

        print(f"{domain}")

        for concept in concepts:

            print(
                f"   - {concept}"
            )

        print()