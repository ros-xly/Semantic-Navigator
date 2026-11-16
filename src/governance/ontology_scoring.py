def score_ontology_coverage(
    ontology
):

    total = len(
        ontology
    )

    classified = 0

    for node in ontology:

        if node.domain != "General":

            classified += 1

    if total == 0:

        return 0

    return round(
        (
            classified
            / total
        ) * 100,
        2
    )