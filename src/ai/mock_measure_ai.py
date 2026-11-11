def generate_measure_definition(
    measure_name
):

    definitions = {

        "Revenue":
            "Total revenue generated from completed sales.",

        "Margin":
            "Revenue less associated costs.",

        "Customer Count":
            "Total number of customers."
    }

    return definitions.get(
        measure_name,
        f"Business definition for {measure_name}"
    )

def generate_measure_purpose(
    measure_name
):

    purposes = {

        "Revenue":
            "Tracks commercial performance.",

        "Margin":
            "Tracks profitability.",

        "Customer Count":
            "Tracks customer volume."
    }

    return purposes.get(
        measure_name,
        "Business KPI"
    )

def generate_friendly_name(
    measure_name
):

    names = {

        "Revenue":
            "Revenue",

        "Margin":
            "Profit Margin",

        "Customer Count":
            "Customer Count"
    }

    return names.get(
        measure_name,
        measure_name
    )

