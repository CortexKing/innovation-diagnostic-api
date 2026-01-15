def interpreter_score_global(score):
    if score >= 80:
        return "Très forte maturité d’innovation. L’enjeu principal est désormais le passage à l’échelle."
    elif score >= 60:
        return "Bon socle d’innovation. Des axes d’amélioration ciblés peuvent générer une forte accélération."
    elif score >= 40:
        return "Capacité d’innovation moyenne. Une structuration des démarches est prioritaire."
    else:
        return "Risque élevé sur l’innovation. Une remise à plat stratégique est recommandée."


def interpreter_dimensions(scores_dimensions):
    interpretations = {}

    for dimension, score in scores_dimensions.items():
        if score >= 70:
            interpretations[dimension] = "Point fort structuré et maîtrisé."
        elif score >= 50:
            interpretations[dimension] = "Niveau correct mais perfectible."
        else:
            interpretations[dimension] = "Point de fragilité nécessitant une action prioritaire."

    return interpretations
