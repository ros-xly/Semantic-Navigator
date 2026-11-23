def classify_measure(
    expression
):

    expression = expression.lower()

    if "count" in expression:

        return "Count"

    if "sum" in expression:

        return "Sum"

    if "%" in expression:

        return "Percentage"

    if "/" in expression:

        return "Ratio"

    return "KPI"