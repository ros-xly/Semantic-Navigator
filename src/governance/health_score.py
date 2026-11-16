def calculate_health_score(
    field_score,
    measure_score,
    ontology_score
):

    return round(
        (
            field_score
            + measure_score
            + ontology_score
        )
        / 3,
        2
    )