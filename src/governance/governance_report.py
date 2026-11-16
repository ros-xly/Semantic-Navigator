def print_governance_report(
    field_score,
    measure_score,
    ontology_score,
    health_score
):

    print("\nGOVERNANCE REPORT\n")

    print(
        f"Field Coverage: {field_score}%"
    )

    print(
        f"Measure Coverage: {measure_score}%"
    )

    print(
        f"Ontology Coverage: {ontology_score}%"
    )

    print(
        f"Metadata Health Score: {health_score}%"
    )