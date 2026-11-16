def score_measure_coverage(
    tables
):

    total_measures = 0
    documented_measures = 0

    for table in tables:

        for measure in table.measures:

            total_measures += 1

            if measure.definition:

                documented_measures += 1

    if total_measures == 0:

        return 0

    return round(
        (
            documented_measures
            / total_measures
        ) * 100,
        2
    )