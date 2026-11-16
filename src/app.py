import streamlit as st

from ui.file_loader import (
    save_uploaded_files
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
        "Semantic model parsed."
    )

    st.write(
        f"Tables Found: {len(tables)}"
    )