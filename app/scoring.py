RAW_MAX = 4
NORMALIZED_MAX = 10


def normalize(value: int) -> float:
    return round((value / RAW_MAX) * NORMALIZED_MAX, 2)


def compute_dimension_score(answers, question_ids):
    scores = [normalize(answers[q]) for q in question_ids if q in answers]
    return round(sum(scores) / len(scores), 2) if scores else 0.0


def compute_global_score(dimension_scores):
    return round(
        sum(dimension_scores.values()) / len(dimension_scores), 2
    ) if dimension_scores else 0.0
