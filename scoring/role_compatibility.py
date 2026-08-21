# Role Compatibility Index (RCI)
# AI Talent Mapper - Vidhishastra Foundation

ROLE_PROFILES = {
    "Software Developer": {
        "80L": 0.35,
        "9HY": 0.25,
        "D1": 0.20,
        "O21": 0.10,
        "EI2": 0.05,
        "23BR": 0.05,
    },

    "Project Manager": {
        "23BR": 0.30,
        "EI2": 0.25,
        "O21": 0.20,
        "D1": 0.10,
        "9HY": 0.10,
        "80L": 0.05,
    },

    "Entrepreneur": {
        "D1": 0.30,
        "9HY": 0.25,
        "23BR": 0.15,
        "EI2": 0.10,
        "O21": 0.10,
        "80L": 0.10,
    },
}


def calculate_role_compatibility(score_percentages):
    results = {}

    for role, weights in ROLE_PROFILES.items():
        compatibility = 0

        for code, weight in weights.items():
            compatibility += score_percentages.get(code, 0) * weight

        results[role] = round(compatibility, 2)

    ranked_roles = sorted(
        results.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return {
        "role_scores": results,
        "recommended_role": ranked_roles[0][0],
        "recommended_role_score": ranked_roles[0][1]
    }
