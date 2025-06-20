import json
from open_AI import query_openai
from mitre_map import keyword_to_mitre
from schemas import LogInput, ClassificationResult


async def classify_log(log: LogInput) -> ClassificationResult:
    result_raw = query_openai(log.event)

    try:
        result = json.loads(result_raw.split("```json")[-1].split("```")[0])
    except:
        # fallback parsing or log error
        result = {}

    return ClassificationResult(
        category=result.get("category", "Unknown"),
        severity=result.get("severity", "Medium"),
        mitre_id=result.get("mitre_id", keyword_to_mitre(log.event)),
        confidence=result.get("confidence", 50),
        explanation=result.get("explanation", "Not available"),
        remediation=result.get("remediation", "Monitor the user activity and rotate credentials")
    )