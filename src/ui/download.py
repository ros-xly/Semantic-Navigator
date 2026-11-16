from pathlib import Path


def get_latest_excel():

    outputs = Path(
        "outputs"
    )

    files = list(
        outputs.glob("*.xlsx")
    )

    files.sort(
        reverse=True
    )

    return files[0]