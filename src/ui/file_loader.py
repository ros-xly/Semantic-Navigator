from pathlib import Path


def save_uploaded_files(
    uploaded_files
):

    upload_folder = Path(
        "temp_upload"
    )

    upload_folder.mkdir(
        exist_ok=True
    )

    for file in uploaded_files:

        save_path = (
            upload_folder
            / file.name
        )

        with open(
            save_path,
            "wb"
        ) as output:

            output.write(
                file.getbuffer()
            )

    return upload_folder