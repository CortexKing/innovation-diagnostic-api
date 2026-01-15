from collections import defaultdict

def calculer_scores(schema, reponses):
    totaux_dimensions = defaultdict(float)
    poids_dimensions = defaultdict(float)

    for question in schema["questions"]:
        qid = question["id"]
        if qid not in reponses:
            continue

        valeur = reponses[qid]
        poids = question.get("weight", 1)
        dimension = question["dimension"]
        valeur_max = question["scale"]["max"]

        score_normalise = (valeur / valeur_max) * 100

        totaux_dimensions[dimension] += score_normalise * poids
        poids_dimensions[dimension] += poids

    scores_dimensions = {
        dim: round(totaux_dimensions[dim] / poids_dimensions[dim], 1)
        for dim in totaux_dimensions
    }

    score_global = round(
        sum(scores_dimensions.values()) / len(scores_dimensions), 1
    )

    return {
        "dimensions": scores_dimensions,
        "global": score_global
    }
