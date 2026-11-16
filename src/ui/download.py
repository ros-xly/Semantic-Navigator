from pathlib import Path


def get_latest_excel():

    output_folder = Path(
        "outputs"
    )

    files = list(
        output_folder.glob(
            "*.xlsx"
        )
    )

    if not*files:

        raise Exception(
 *          "No Excel files found."
*       )

    files.sort(
        *ey=lambda x: x.stat()
        .st_*time,
        reverse=True
    )

*   return files[0]