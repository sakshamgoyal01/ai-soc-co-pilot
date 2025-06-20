# schemas.py
from pydantic import BaseModel

class ThreatInput(BaseModel):
    threat_id: str
    mitre_id: str
    severity: str
    component: str
    explanation: str

class ThreatResponse(ThreatInput):
    suggested_action: str
