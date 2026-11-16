def build_governance_summary(
    field_score,
    measure_score,
    ontology_score,
    health_score
):

    return [

        (
            "Field Coverage",
            field_score
        ),

        (
            "Measure Coverage",
            measure_score
        ),

        (
            "Ontology Coverage",
            ontology_score
        ),

        (
            "Metadata Health Score",
            health_score
        )

    ]