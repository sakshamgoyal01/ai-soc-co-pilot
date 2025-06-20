SEVERITY_WEIGHT = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 5
}


def calculate_risk_score(cves):
    """
    Calculates a weighted risk score based on severity and CVSS score.

    Args:
        cves (list): List of CVE dictionaries with 'severity' and 'score' keys.

    Returns:
        float: Average weighted risk score.
    """
    if not cves:
        return 0.0

    weighted_scores = []

    for cve in cves:
        severity = cve.get("severity", "LOW").upper()
        score = cve.get("score", 0)

        # Validate and apply defaults if malformed
        if severity not in SEVERITY_WEIGHT:
            severity = "LOW"
        try:
            numeric_score = float(score)
        except (ValueError, TypeError):
            numeric_score = 0.0

        weight = SEVERITY_WEIGHT[severity]
        weighted_scores.append(weight * numeric_score)

    average_score = round(sum(weighted_scores) / len(weighted_scores), 2)
    return average_score

sample_cves = [
    {"id": "CVE-2024-12345", "severity": "HIGH", "score": 7.5},
    {"id": "GHSA-xy12", "severity": "MEDIUM", "score": 6.0},
    {"id": "CVE-2024-99999", "severity": "CRITICAL", "score": 9.8}
]

risk = calculate_risk_score(sample_cves)
print("Risk Score:", risk)