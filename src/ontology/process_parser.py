import json

from ontology.business_architecture import (
    ProcessMapping
)


def parse_process_response(
    response
):

    processes = []

    data = json.loads(
        response
    )

    for item in data:

        processes.append(

            ProcessMapping(

                domain=item[
                    "domain"
                ],

                capability=item[
                    "capability"
                ],

                process=item[
                    "process"
                ],

                table=item[
                    "table"
                ]

            )

        )

    return processes