from decision_logic import decide_action
from actions import k8s, ansible_runner
from fastapi import APIRouter
from schemas import ThreatInput, ThreatResponse


router = APIRouter()

@router.post("/remediate", response_model=ThreatResponse)
def suggest_remediation(threat: ThreatInput):
    action = decide_action(threat.dict())
    return ThreatResponse(
        threat_id=threat.threat_id,
        mitre_id=threat.mitre_id,
        severity=threat.severity,
        component=threat.component,
        explanation=threat.explanation,
        suggested_action=action
    )
async def remediate(threat: ThreatResponse):
    return await process_threat(threat)

async def process_threat(threat: ThreatResponse):
    action = threat.suggested_action or decide_action(threat)

    if action == "isolate_pod":
        k8s.isolate_pod(threat.component)
    elif action == "restart_service":
        k8s.restart_service(threat.component)
    elif action == "revoke_access":
        ansible_runner.run_playbook("playbooks/revoke.yml", {"user": threat.component})
    elif action == "rotate_secret":
        ansible_runner.run_playbook("playbooks/rotate_secret.yml", {"secret": threat.component})

    return {"action_taken": action}
