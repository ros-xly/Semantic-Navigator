def classify_measure(
    expression
):

    expression = (
        expression.lower()
    )

    if (
        "distinctcount"
        in expression
    ):

        return "Count"

    if (
        "count("
        in expression
    ):

        return "Count"

    if (
        "sumx("
        in expression
    ):

        return "Sum"

    if (
        "sum("
        in expression
    ):

        return "Sum"

    if (
        "averagex("
        in expression
    ):

        return "Average"

    if (
        "average("
        in expression
    ):

        return "Average"

    if (
        "divide("
        in expression
    ):

        return "Percentage"

    if (
        "%"
        in expression
    ):

        return "Percentage"

    if (
        "/"
        in expression
    ):

        return "Ratio"

    return "KPI"