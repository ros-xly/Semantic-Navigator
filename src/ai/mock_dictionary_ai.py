def generate_definition(column_name):

    definitions = {

        "SalesAmount":
            "Monetary value associated with completed sales transactions.",

        "CustomerID":
            "Unique identifier assigned to a customer.",

        "CustomerName":
            "Name used to identify a customer.",

        "Cost":
            "Value associated with providing goods or services."
    }

    return definitions.get(
        column_name,
        f"Business definition for {column_name}"
    )

def generate_synonyms(column_name):

    synonyms = {

        "SalesAmount":
            [
                "Revenue",
                "Sales Value",
                "Turnover"
            ]
    }

    return synonyms.get(
        column_name,
        []
    )

def generate_domain(column_name):

    domains = {

        "SalesAmount":
            "Commercial",

        "Cost":
            "Finance",

        "CustomerID":
            "Customer"
    }

    return domains.get(
        column_name,
        "General"
    )

