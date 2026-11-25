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

relationships = (
    parse_relationships(
        model_path
    )
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

from ontology.relationship_parser import (
    parse_relationships
)

from ontology.business_relationship_builder import (
    build_relationships
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

from ontology.ontology_flow import (
    build_process_flow
)

from ontology.unclassified import (
    find_unclassified
)

from ontology.ontology_report import (
    print_ontology_summary
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
# EXPORT
# =====================================

from excel.exporter import (
    create_data_dictionary
)

# =====================================
# MAIN
# =====================================

try:

    model_path = get_model_path()

    validate_model_path(
        model_path
    )

    model_name = get_model_name(
        model_path
    )

    # --------------------
    # Parse Model
    # --------------------

    tables = parse_model_folder(
        str(model_path)
    )

    # --------------------
    # AI Enrichment
    # --------------------

    tables = enrich_columns(
        tables
    )

    tables = enrich_measures(
        tables
    )

    # --------------------
    # Dependencies
    # --------------------

    lineage = build_lineage(
        tables
    )

    # --------------------
    # Business Ontology
    # --------------------

    ontology = build_ontology(
        tables,
        lineage
    )

    process_flow = (
        build_process_flow(
            ontology
        )
    )

    unclassified = (
        find_unclassified(
            tables,
            ontology
        )
    )

    entity_relationships = (
        build_relationships(
            relationships
        )
    )

    # --------------------
    # Governance
    # --------------------

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

    # --------------------
    # Console Output
    # --------------------

    print_processing_report(
        model_name,
        tables
    )

    print_ontology_summary(
        ontology
    )

    print_governance_report(
        field_score,
        measure_score,
        ontology_score,
        health_score
    )

    # --------------------
    # Export Workbook
    # --------------------

    create_data_dictionary(
        tables,
        model_name,
        ontology,
        process_flow,
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