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
# INPUT
# =====================================

from input.model_input import (
    get_model_path
)

from input.model_validation import (
    validate_model_path
)

from input.model_metadata import (
    get_model_name
)

from input.error_handler import (
    handle_error
)

# =====================================
# REPORTING
# =====================================

from reporting.process_report import (
    print_processing_report
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

# =====================================
# BUSINESS ONTOLOGY
# =====================================

from ontology.ontology_builder import (
    build_ontology
)

from ontology.unclassified import (
    find_unclassified
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
# MAIN
# =====================================

try:

    # -------------------------
    # MODEL INPUT
    # -------------------------

    model_path = get_model_path()

    validate_model_path(
        model_path
    )

    model_name = get_model_name(
        model_path
    )

    # -------------------------
    # MODEL PARSE
    # -------------------------

    tables = parse_model_folder(
        str(model_path)
    )

    # -------------------------
    # AI ENRICHMENT
    # -------------------------

    tables = enrich_columns(
        tables
    )

    tables = enrich_measures(
        tables
    )

    # -------------------------
    # LINEAGE
    # -------------------------

    lineage = build_lineage(
        tables
    )

    # -------------------------
    # BUSINESS ONTOLOGY
    # -------------------------

    ontology = build_ontology(
        tables,
        lineage
    )

    unclassified = (
        find_unclassified(
            tables,
            ontology
        )
    )

    # -------------------------
    # GOVERNANCE
    # -------------------------

    field_score = (
        score_field_coverage(
            tables
        )
    )

    measure_score = (
        score_measure_coverage(
            tables
        )
    )

    ontology_score = (
        score_ontology_coverage(
            ontology
        )
    )

    health_score = (
        calculate_health_score(
            field_score,
            measure_score,
            ontology_score
        )
    )

    governance_summary = (
        build_governance_summary(
            field_score,
            measure_score,
            ontology_score,
            health_score
        )
    )

    # -------------------------
    # CONSOLE REPORTING
    # -------------------------

    print_processing_report(
        model_name,
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

    # -------------------------
    # EXCEL EXPORT
    # -------------------------

    create_data_dictionary(
        tables,
        model_name,
        ontology,
        unclassified,
        governance_summary
    )

    print(
        "\nDocumentation Complete"
    )

except Exception as error:

    handle_error(
        error
    )