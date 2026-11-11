import sys

sys.path.append(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src"
)

from parser.model_parser import parse_model_folder
from reporting.console_report import print_model_summary

from lineage.lineage_builder import build_lineage
from lineage.impact_analysis import build_impact_analysis

from excel.exporter import create_data_dictionary


tables = parse_model_folder(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\samples\simple_model\tables"
)

from ai.enrichment import enrich_columns

tables = enrich_columns(tables)

print_model_summary(tables)

lineage = build_lineage(tables)

impact = build_impact_analysis(
    lineage
)

create_data_dictionary(
    tables,
    lineage,
    impact
)

print(
    "\nExcel Data Dictionary Generated"
)

print(
    tables[1].columns[1].definition
)