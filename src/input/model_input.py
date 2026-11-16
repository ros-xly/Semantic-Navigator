from pathlib import Path


def get_model_path():

    path = input(
        "\nEnter path to semantic model tables folder:\n"
    )

    return Path(
        path
    )