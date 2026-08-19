import json
from pathlib import Path


def load_json(file_path):
    """Load and return data from a JSON file."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, file_path):
    """Save data to a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def normalize_answer(answer):
    """Convert an answer into a consistent format."""
    if answer is None:
        return ""

    if isinstance(answer, str):
        return answer.strip().lower()

    return answer


def calculate_percentage(score, maximum_score):
    """Calculate percentage safely."""
    if maximum_score <= 0:
        return 0

    return round((score / maximum_score) * 100, 2)
