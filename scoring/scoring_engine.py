"""
AI Talent Mapper
Scoring Engine

Vidhishastra Foundation

Scoring model:
Candidate gives a rating from 1 to 5 for each assessment question.
Each question is mapped to one Talent Code.

Scores are normalized because different Talent Codes may have
different numbers of questions.
"""

import json
from pathlib import Path

from models.talent_codes import TALENT_CODES


BASE_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_FILE = BASE_DIR / "data" / "questions.json"


def load_assessment():
    """
    Load assessment questions from data/questions.json.
    """
    with QUESTIONS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_question_id(question_id):
    """
    Accept IDs such as:
    1
    "1"
    "Q1"
    "q1"

    and return integer 1.
    """
    if isinstance(question_id, int):
        return question_id

    value = str(question_id).strip().upper()

    if value.startswith("Q"):
        value = value[1:]

    return int(value)


def validate_rating(value):
    """
    Validate candidate rating.

    Allowed values:
    1, 2, 3, 4, 5
    """
    try:
        rating = int(value)
    except (TypeError, ValueError):
        raise ValueError(
            f"Invalid answer '{value}'. Rating must be between 1 and 5."
        )

    if rating < 1 or rating > 5:
        raise ValueError(
            f"Invalid rating {rating}. Rating must be between 1 and 5."
        )

    return rating


def calculate_scores(answers):
    """
    Calculate raw and normalized Talent Code scores.

    Example answers:

    {
        "1": 5,
        "2": 4,
        "3": 3,
        "4": 5
    }

    Q-prefixed IDs are also accepted:

    {
        "Q1": 5,
        "Q2": 4
    }
    """

    assessment = load_assessment()
    questions = assessment["questions"]

    question_map = {
        question["id"]: question
        for question in questions
    }

    raw_scores = {
        code: 0
        for code in TALENT_CODES
    }

    answered_questions = {
        code: 0
        for code in TALENT_CODES
    }

    possible_questions = {
        code: 0
        for code in TALENT_CODES
    }

    # Count total available questions for each code
    for question in questions:
        code = question["code"]

        if code in possible_questions:
            possible_questions[code] += 1

    # Score candidate answers
    for question_id, value in answers.items():

        normalized_id = normalize_question_id(question_id)

        question = question_map.get(normalized_id)

        if not question:
            raise ValueError(
                f"Question ID {question_id} does not exist."
            )

        rating = validate_rating(value)

        code = question["code"]

        # Support reverse-scored questions in future
        if question.get("reverse", False):
            rating = 6 - rating

        if code in raw_scores:
            raw_scores[code] += rating
            answered_questions[code] += 1

    percentages = {}

    for code in TALENT_CODES:

        answered = answered_questions[code]

        if answered == 0:
            percentages[code] = 0.0
            continue

        maximum_score = answered * 5

        percentages[code] = round(
            (raw_scores[code] / maximum_score) * 100,
            2
        )

    return {
        "raw_scores": raw_scores,
        "percentages": percentages,
        "answered_questions": answered_questions,
        "possible_questions": possible_questions
    }


def rank_codes(percentages):
    """
    Rank Talent Codes from highest to lowest percentage.
    """

    return sorted(
        percentages.items(),
        key=lambda item: (-item[1], item[0])
    )


def get_primary_codes(percentages):
    """
    Return all codes tied for the highest score.
    """

    ranked = rank_codes(percentages)

    if not ranked:
        return []

    highest_score = ranked[0][1]

    if highest_score <= 0:
        return []

    return [
        code
        for code, score in ranked
        if score == highest_score
    ]


def get_primary_code(percentages):
    """
    Return one primary Talent Code.

    If there is a tie, the first code in deterministic ranking
    is returned while tied codes are also provided separately
    in the final profile.
    """

    primary_codes = get_primary_codes(percentages)

    if not primary_codes:
        return None

    return primary_codes[0]


def get_secondary_codes(percentages, primary_code, limit=2):
    """
    Return the next strongest Talent Codes.
    """

    ranked = rank_codes(percentages)

    secondary = []

    for code, score in ranked:

        if code == primary_code:
            continue

        if score <= 0:
            continue

        secondary.append(code)

        if len(secondary) >= limit:
            break

    return secondary


def generate_talent_profile(answers):
    """
    Generate complete AI Talent Mapper profile.
    """

    scoring = calculate_scores(answers)

    percentages = scoring["percentages"]

    primary_code = get_primary_code(percentages)

    tied_primary_codes = get_primary_codes(percentages)

    secondary_codes = get_secondary_codes(
        percentages,
        primary_code
    )

    primary_profile = (
        TALENT_CODES.get(primary_code)
        if primary_code
        else None
    )

    secondary_profiles = [
        {
            "code": code,
            "score_percentage": percentages[code],
            "profile": TALENT_CODES.get(code)
        }
        for code in secondary_codes
    ]

    return {
        "assessment": "AI Talent Mapper",
        "version": "0.2.0",

        "primary_code": primary_code,

        "primary_score_percentage": (
            percentages.get(primary_code, 0)
            if primary_code
            else 0
        ),

        "tied_primary_codes": tied_primary_codes,

        "secondary_codes": secondary_codes,

        "raw_scores": scoring["raw_scores"],

        "score_percentages": percentages,

        "answered_questions": scoring["answered_questions"],

        "primary_profile": primary_profile,

        "secondary_profiles": secondary_profiles,

        "note": (
            "This result is a talent and behavioral pattern "
            "assessment prototype. It is not a clinical or "
            "psychological diagnosis."
        )
    }


if __name__ == "__main__":

    sample_answers = {
        "1": 5,
        "2": 4,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 3,
        "7": 4,
        "8": 4,
        "9": 5,
        "10": 4,
        "11": 5,
        "12": 4,
        "13": 5,
        "14": 5,
        "15": 4,
        "16": 3,
        "17": 4,
        "18": 3,
        "19": 5,
        "20": 4,
        "21": 5
    }

    profile = generate_talent_profile(sample_answers)

    print("AI TALENT MAPPER")
    print("-------------------------")
    print("Primary Code:", profile["primary_code"])
    print(
        "Primary Score:",
        profile["primary_score_percentage"],
        "%"
    )
    print(
        "Secondary Codes:",
        profile["secondary_codes"]
    )
    print(
        "All Scores:",
        profile["score_percentages"]
    )
