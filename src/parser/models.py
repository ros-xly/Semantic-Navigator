from dataclasses import dataclass
from typing import List


@dataclass
class Column:
    name: str
    data_type: str


@dataclass
class Measure:
    name: str
    expression: str


@dataclass
class Table:
    name: str
    columns: List[Column]
    measures: List[Measure]