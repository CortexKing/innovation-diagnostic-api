def interpret_dimension(score: float):
    if score < 4:
        return "fragile"
    elif score < 7:
        return "en_construction"
    else:
        return "solide"


def detect_profiles(scores):
    profiles = []

    if scores.get("technology", 0) > 7 and scores.get("market", 0) < 4:
        profiles.append("Risque de techno-push")

    if scores.get("market", 0) > 7 and scores.get("business_model", 0) < 4:
        profiles.append("Risque de monétisation")

    if all(v >= 6 for v in scores.values()):
        profiles.append("Projet globalement mature")

    if scores.get("funding", 0) < 4:
        profiles.append("Préparation au financement insuffisante")

    return profiles
