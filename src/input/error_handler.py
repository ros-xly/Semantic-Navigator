import traceback


def handle_error(
    error
):

    print(
        "\nPROCESSING FAILED\n"
    )

    print(
        str(error)
    )

    print(
        "\nFULL TRACEBACK\n"
    )

    traceback.print_exc()