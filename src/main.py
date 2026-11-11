import sys

sys.path.append(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src"
)

from parser.model_parser import parse_model_folder

tables = parse_model_folder(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\samples\simple_model\tables"
)

for table in tables:
    print(table)