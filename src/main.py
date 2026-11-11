import sys

sys.path.append(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src"
)

from parser.model_parser import parse_model_folder

tables = parse_model_folder(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\samples\simple_model\tables"
)
from reporting.console_report import print_model_summary

print_model_summary(tables)

from excel.exporter import create_data_dictionary

create_data_dictionary(tables)

print(
    "\nExcel Data Dictionary Generated"
)