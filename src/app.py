import streamlit as st


st.set_page_config(
    page_title="Semantic Navigator",
    layout="wide"
)

st.title(
    "Semantic Navigator"
)

st.write(
    """
AI-powered semantic model
documentation and governance.
"""
)

uploaded_files = st.file_uploader(

    "Upload TMDL Files",

    type=["tmdl"],

    accept_multiple_files=True

)

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} files uploaded."
    )