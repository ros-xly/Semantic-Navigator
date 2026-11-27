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
# ENTITY RELATIONSHIPS
# =====================================

from ontology.relationship_parser import (
    parse_relationships
)

from ontology.business_relationship_builder import (
    build_relationships
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

from governance.health_score import (
    calculate_health_score
)

from governance.governance_builder import (
    build_governance_summary
)

from governance.governance_report import (
    print_governance_report
)

# =====================================
# REPORTING
# =====================================

from reporting.process_report import (
    print_processing_report
)

# =====================================
# EXCEL
# =====================================

from excel.exporter import (
    create_data_dictionary
)

try:

    model_path = get_model_path()

    validate_model_path(
        model_path
    )

    model_name = get_model_name(
        model_path
    )

    # ---------------------
    # Parse Model
    # ---------------------

    tables = parse_model_folder(
        str(model_path)
    )

    # ---------------------
    # Enrichment
    # ---------------------

    tables = enrich_columns(
        tables
    )

    tables = enrich_measures(
        tables
    )

    # ---------------------
    # Measure Dependencies
    # ---------------------

    lineage = build_lineage(
        tables
    )

    # ---------------------
    # Relationships
    # ---------------------

    raw_relationships = (
        parse_relationships(
            model_path
        )
    )

    entity_relationships = (
        build_relationships(
            raw_relationships
        )
    )

    # ---------------------
    # Governance
    # ---------------------

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

    ontology_score = 100

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

    # ---------------------
    # Reporting
    # ---------------------

    print_processing_report(
        model_name,
        tables
    )

    print_governance_report(
        field_score,
        measure_score,
        ontology_score,
        health_score
    )

    # ---------------------
    # Export
    # ---------------------

    create_data_dictionary(
        tables=tables,
        model_name=model_name,
        relationships=entity_relationships,
        governance_summary=governance_summary
    )

    print(
        "\nDocumentation Complete"
    )

except Exception as error:

    handle_error(
        error
    )