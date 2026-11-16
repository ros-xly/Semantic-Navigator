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
assessment for Power BI semantic models.
"""
)

uploaded_files = st.file_uploader(

    "Upload TMDL Files",

    type=["tmdl"],

    accept_multiple_files=True

)

if uploaded_files:

    folder = save_uploaded_files(
        uploaded_files
    )

    tables = parse_model_folder(
        str(folder)
    )

    st.success(
        "Semantic model parsed successfully."
    )

    # -----------------------
    # Dashboard Metrics
    # -----------------------

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

    # -----------------------
    # Download Excel
    # -----------------------

    try:

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
                    "application/"
                    "vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                )
            )

    except Exception:

        st.warning(
            "No documentation workbook found."
        )