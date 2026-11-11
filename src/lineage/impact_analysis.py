def build_impact_analysis(lineage):

    impact = {}

    for item in lineage:

        measure = item["measure"]

        for dependency in item["dependencies"]:

            if dependency not in impact:

                impact[dependency] = []

            impact[dependency].append(
                measure
            )

    return impact