from dataclasses import dataclass


@dataclass
class ProcessMapping:

    domain: str

    capability: str

    process: str

    table: str