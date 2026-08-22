# Team Synergy Engine
# AI Talent Mapper - Vidhishastra Foundation

SYNERGY_MATRIX = {
    "EI2": {
        "EI2": 80,
        "9HY": 90,
        "80L": 75,
        "O21": 95,
        "23BR": 85,
        "D1": 80,
    },
    "9HY": {
        "EI2": 90,
        "9HY": 75,
        "80L": 90,
        "O21": 85,
        "23BR": 80,
        "D1": 95,
    },
    "80L": {
        "EI2": 75,
        "9HY": 90,
        "80L": 80,
        "O21": 90,
        "23BR": 95,
        "D1": 85,
    },
    "O21": {
        "EI2": 95,
        "9HY": 85,
        "80L": 90,
        "O21": 80,
        "23BR": 90,
        "D1": 85,
    },
    "23BR": {
        "EI2": 85,
        "9HY": 80,
        "80L": 95,
        "O21": 90,
        "23BR": 80,
        "D1": 85,
    },
    "D1": {
        "EI2": 80,
        "9HY": 95,
        "80L": 85,
        "O21": 85,
        "23BR": 85,
        "D1": 75,
    },
}


def calculate_team_synergy(code_a, code_b):
    """
    Calculate synergy score between two Talent Codes.
    Returns a score from 0 to 100.
    """

    code_a = str(code_a).upper()
    code_b = str(code_b).upper()

    if code_a not in SYNERGY_MATRIX:
        raise ValueError(f"Unknown Talent Code: {code_a}")

    if code_b not in SYNERGY_MATRIX[code_a]:
        raise ValueError(f"Unknown Talent Code: {code_b}")

    score = SYNERGY_MATRIX[code_a][code_b]

    if score >= 90:
        level = "Excellent"
    elif score >= 80:
        level = "Strong"
    elif score >= 70:
        level = "Good"
    else:
        level = "Needs Balance"

    return {
        "code_a": code_a,
        "code_b": code_b,
        "synergy_score": score,
        "synergy_level": level
    }
