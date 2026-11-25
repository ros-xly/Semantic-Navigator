def score_ontology_coverage(
    ontology
):

    if not ontology:

        return 0

    classified_tables = 0

    for process, tables in (
        ontology.items()
    ):

        classified_tables += len(
            tables
        )

    return classified_tables