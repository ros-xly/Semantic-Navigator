from dataclasses import dataclass
from typing import List


@dataclass
class Column:

    name: str

    data_type: str

    definition: str = ""

    synonyms: list = None

    alternative_names: list = None

    business_domain: str = ""


@dataclass
class Measure:

    name: str

    expression: str

    definition: str = ""

    purpose: str = ""

    friendly_name: str = ""


@dataclass
class Table:
    name: str
    columns: List[Column]
    measures: List[Measure]