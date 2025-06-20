from pydantic import BaseModel

class LogInput(BaseModel):
    timestamp: str
    source: str
    event: str
    user: str

class ClassificationResult(BaseModel):
    category: str
    severity: str
    mitre_id: str
    confidence: int
    explanation: str
    remediation: str
