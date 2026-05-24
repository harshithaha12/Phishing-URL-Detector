SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "bank",
    "paypal",
    "free",
    "bonus",
    "signin",
    "account",
    "crypto"
]


def extract_features(url):

    features = {}

    features["URL Length"] = len(url)

    features["HTTPS"] = (
        "Enabled"
        if "https://" in url
        else "Disabled"
    )

    suspicious_count = 0

    for word in SUSPICIOUS_WORDS:

        if word in url.lower():

            suspicious_count += 1

    features["Suspicious Keywords"] = suspicious_count

    return features


def analyze_url(url):

    features = extract_features(url)

    score = 0

    if features["URL Length"] > 70:
        score += 2

    if features["HTTPS"] == "Disabled":
        score += 2

    score += features["Suspicious Keywords"]

    if score >= 6:

        result = "HIGH RISK"

        color = "#ff3b30"

    elif score >= 3:

        result = "SUSPICIOUS"

        color = "#ff9500"

    else:

        result = "SAFE"

        color = "#34c759"

    return (
        result,
        color,
        score,
        features
    )