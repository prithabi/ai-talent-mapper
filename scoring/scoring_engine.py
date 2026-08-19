"""
AI Talent Mapper
Scoring Engine

Converts candidate answers into Intelligence Code scores.
"""

from models.talent_codes import TALENT_CODES


def calculate_scores(answers):
    """
    Calculate Intelligence Code scores.

    answers format:
    {
        "Q1": "E12",
        "Q2": "23BR",
        "Q3": "021"
    }
    """

    scores = {
        code: 0
        for code in TALENT_CODES
    }

    for question_id, selected_code in answers.items():

        if selected_code in scores:
            scores[selected_code] += 1

    return scores


def rank_codes(scores):
    """
    Rank Intelligence Codes from highest to lowest score.
    """

    ranked = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return ranked


def get_primary_code(scores):
    """
    Return the highest scoring Intelligence Code.
    """

    ranked = rank_codes(scores)

    if not ranked:
        return None

    return ranked[0][0]


def get_secondary_codes(scores, limit=2):
    """
    Return the next highest scoring Intelligence Codes.
    """

    ranked = rank_codes(scores)

    return [
        code
        for code, score in ranked[1:limit + 1]
        if score > 0
    ]


def generate_talent_profile(answers):
    """
    Generate complete candidate talent profile.
    """

    scores = calculate_scores(answers)

    primary_code = get_primary_code(scores)

    secondary_codes = get_secondary_codes(scores)

    return {
        "scores": scores,
        "primary_code": primary_code,
        "secondary_codes": secondary_codes,
        "primary_profile": (
            TALENT_CODES.get(primary_code)
            if primary_code
            else None
        )
    }


if __name__ == "__main__":

    # Example candidate answers
    sample_answers = {
        "Q1": "E12",
        "Q2": "E12",
        "Q3": "23BR",
        "Q4": "021",
        "Q5": "E12",
        "Q6": "9HY",
        "Q7": "E12",
        "Q8": "23BR",
        "Q9": "80L",
        "Q10": "E12"
    }

    profile = generate_talent_profile(sample_answers)

    print("AI TALENT MAPPER")
    print("----------------")
    print("Primary Code:", profile["primary_code"])
    print("Secondary Codes:", profile["secondary_codes"])
    print("Scores:", profile["scores"])
