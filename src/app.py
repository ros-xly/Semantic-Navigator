import streamlit as st

from ui.file_loader import (
    save_uploaded_files
)

from ui.download import (
    get_latest_excel
)

from parser.model_parser import (
    parse_model_folder
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

from governance.governance_builder import (
    build_governance_summary
)

from excel.exporter import (
    create_data_dictionary
)

st.set_page_config(
    page_title="Semantic Navigator",
    layout="wide"
)

st.title(
    "Semantic Navigator"
)

st.write(
    """
AI-powered semantic model documentation,
ontology generation and governance
assessment.
"""
)

uploaded_files = st.file_uploader(

    "Upload TMDL Files",

    type=["tmdl"],

    accept_multiple_files=True

)

if uploaded_files:

    with st.spinner(
        "Processing semantic model..."
    ):

        folder = save_uploaded_files(
            uploaded_files
        )

        model_name = "Uploaded_Model"

        # --------------------
        # Parse
        # --------------------

        tables = parse_model_folder(
            str(folder)
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
        # Lineage
        # --------------------

        lineage = build_lineage(
            tables
        )

        impact = build_impact_analysis(
            lineage
        )

        # --------------------
        # Ontology
        # --------------------

        ontology = build_ontology(
            tables
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
        # Excel
        # --------------------

        create_data_dictionary(
            tables,
            model_name,
            lineage,
            impact,
            ontology,
            governance_summary
        )

    st.success(
        "Documentation generated."
    )

    # --------------------
    # Dashboard
    # --------------------

    table_count = len(
        tables
    )

    column_count = sum(
        len(table.columns)
        for table in tables
    )

    measure_count = sum(
        len(table.measures)
        for table in tables
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Tables",
        table_count
    )

    col2.metric(
        "Columns",
        column_count
    )

    col3.metric(
        "Measures",
        measure_count
    )

    # --------------------
    # Download
    # --------------------

    excel_file = get_latest_excel()

    with open(
        excel_file,
        "rb"
    ) as file:

        st.download_button(
            label="Download Documentation",
            data=file,
            file_name=excel_file.name,
            mime=(
                "application/vnd."
                "openxmlformats-"
                "officedocument."
                "spreadsheetml.sheet"
            )
        )