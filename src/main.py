import sys

sys.path.append(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src"
)

from parser.model_parser import (
    parse_model_folder
)

from reporting.console_report import (
    print_model_summary
)

from ai.enrichment import (
    enrich_columns
)

from ai.measure_enrichment import (
    enrich_measures
)

from lineage.lineage_builder import (
    build_lineage
)

from lineage.impact_analysis import (
    build_impact_analysis
)

from ontology.ontology_builder import (
    build_ontology
)

from ontology.ontology_report import (
    print_ontology_summary
)

from ontology.ontology_scoring import (
    score_ontology
)

from excel.exporter import (
    create_data_dictionary
)

# ------------------------
# Parse Model
# ------------------------

tables = parse_model_folder(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\samples\simple_model\tables"
)

# ------------------------
# Enrichment
# ------------------------

tables = enrich_columns(
    tables
)

tables = enrich_measures(
    tables
)

# ------------------------
# Lineage
# ------------------------

lineage = build_lineage(
    tables
)

impact = build_impact_analysis(
    lineage
)

# ------------------------
# Ontology
# ------------------------

ontology = build_ontology(
    tables
)

# ------------------------
# Console Output
# ------------------------

print_model_summary(
    tables
)

print_ontology_summary(
    ontology
)

score_ontology(
    ontology
)

# ------------------------
# Excel
# ------------------------

create_data_dictionary(
    tables,
    lineage,
    impact,
    ontology
)

print(
    "\nExcel Data Dictionary Generated"
)