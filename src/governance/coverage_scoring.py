def score_field_coverage(
    tables
):

    total_fields = 0
    documented_fields = 0

    for table in tables:

        for column in table.columns:

            total_fields += 1

            if column.definition:

                documented_fields += 1

    if total_fields == 0:

        return 0

    return round(
        (
            documented_fields
            / total_fields
        ) * 100,
        2
    )
