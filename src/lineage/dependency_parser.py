import re


def extract_dependencies(expression):

    matches = re.findall(
        r"\[([^\]]+)\]",
        expression
    )

    return matches