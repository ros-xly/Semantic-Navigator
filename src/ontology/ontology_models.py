from dataclasses import dataclass


@dataclass
class OntologyNode:

    domain: str

    concept: str

    source_type: str