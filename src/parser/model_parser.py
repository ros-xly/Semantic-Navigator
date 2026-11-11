from pathlib import Path

from parser.tmdl_parser import parse_tmdl_file


def parse_model_folder(folder_path: str):

    tables = []

    for file in Path(folder_path).glob("*.tmdl"):

        table = parse_tmdl_file(str(file))

        tables.append(table)

    return tables