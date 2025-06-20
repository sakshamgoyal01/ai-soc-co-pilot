from pydantic import BaseModel
from typing import List

class CVE(BaseModel):
    id: str
    severity: str
    score: float

class ArtifactRisk(BaseModel):
    name: str
    component_type: str
    cves: List[CVE]
    risk_score: float