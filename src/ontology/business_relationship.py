from dataclasses import dataclass


@dataclass
class BusinessRelationship:

    source_entity: str

    source_table: str

    source_column: str

    relationship: str

    target_entity: str

    target_table: str

    target_column: str

    description: str