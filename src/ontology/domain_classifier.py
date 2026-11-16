def classify_domain(name):

    name = name.lower()

    if "revenue" in name:
        return "Commercial Performance"

    if "margin" in name:
        return "Commercial Performance"

    if "sales" in name:
        return "Commercial Performance"

    if "customer" in name:
        return "Customer"

    if "cost" in name:
        return "Finance"

    if "profit" in name:
        return "Finance"

    return "General"