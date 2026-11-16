import sys

sys.path.append(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src"
)

# =====================================
# PARSER
# =====================================

from parser.model_parser import (
    parse_model_folder
)

# =====================================
# REPORTING
# =====================================

from reporting.console_report import (
    print_model_summary
)

# =====================================
# AI ENRICHMENT
# =====================================

from ai.enrichment import (
    enrich_columns
)

from ai.measure_enrichment import (
    enrich_measures
)

# =====================================
# LINEAGE
# =====================================

from lineage.lineage_builder import (
    build_lineage
)

from lineage.impact_analysis import (
    build_impact_analysis
)

# =====================================
# ONTOLOGY
# =====================================

from ontology.ontology_builder import (
    build_ontology
)

from ontology.ontology_report import (
    print_ontology_summary
)

from ontology.ontology_scoring import (
    score_ontology
)

# =====================================
# GOVERNANCE
# =====================================

from governance.coverage_scoring import (
    score_field_coverage
)

from governance.measure_scoring import (
    score_measure_coverage
)

from governance.ontology_scoring import (
    score_ontology_coverage
)

from governance.health_score import (
    calculate_health_score
)

from governance.governance_report import (
    print_governance_report
)

from governance.governance_builder import (
    build_governance_summary
)

# =====================================
# EXCEL
# =====================================

from excel.exporter import (
    create_data_dictionary
)

# =====================================
# LOAD MODEL
# =====================================

tables = parse_model_folder(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\samples\simple_model\tables"
)

# =====================================
# ENRICH DATA
# =====================================

tables = enrich_columns(
    tables
)

tables = enrich_measures(
    tables
)

# =====================================
# BUILD LINEAGE
# =====================================

lineage = build_lineage(
    tables
)

impact = build_impact_analysis(
    lineage
)

# =====================================
# BUILD ONTOLOGY
# =====================================

ontology = build_ontology(
    tables
)

# =====================================
# GOVERNANCE SCORING
# =====================================

field_score = score_field_coverage(
    tables
)

measure_score = score_measure_coverage(
    tables
)

ontology_score = score_ontology_coverage(
    ontology
)

health_score = calculate_health_score(
    field_score,
    measure_score,
    ontology_score
)

governance_summary = (
    build_governance_summary(
        field_score,
        measure_score,
        ontology_score,
        health_score
    )
)

# =====================================
# CONSOLE OUTPUT
# =====================================

print_model_summary(
    tables
)

print_ontology_summary(
    ontology
)

score_ontology(
    ontology
)

print_governance_report(
    field_score,
    measure_score,
    ontology_score,
    health_score
)

# =====================================
# EXCEL OUTPUT
# =====================================

create_data_dictionary(
    tables,
    lineage,
    impact,
    ontology,
    governance_summary
)

print(
    "\nExcel Data Dictionary Generated"
)