def validate_model_path(
    model_path
):

    tmdl_files = list(
        model_path.glob(
            "*.tmdl"
        )
    )

    if len(
        tmdl_files
    ) == 0:

        raise Exception(
            "No TMDL files found."
        )

    return True