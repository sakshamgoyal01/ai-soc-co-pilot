# Fallback static map of keywords → MITRE tactics
MITRE_MAP = {
    "unauthorized api": "T1078",  # Valid Accounts
    "login failure": "T1110",     # Brute Force
    "dns tunneling": "T1071.004", # Application Layer Protocol: DNS
    "suspicious powershell": "T1059.001",  # Command and Scripting Interpreter: PowerShell
    "malicious macro": "T1203",   # Exploitation for Client Execution
    "command and control": "T1071", # Application Layer Protocol
    "data exfiltration": "T1041", # Exfiltration Over C2 Channel
    "persistence": "T1547",       # Boot or Logon Autostart Execution
    "privilege escalation": "T1068",  # Exploitation for Privilege Escalation
    "registry modification": "T1112", # Modify Registry
    "scheduled task": "T1053.005",    # Scheduled Task/Job: Scheduled Task
    "process injection": "T1055",     # Process Injection
    "remote desktop access": "T1021.001", # Remote Services: Remote Desktop Protocol
    "credential dumping": "T1003",    # OS Credential Dumping
    "windows admin shares": "T1077",  # Windows Admin Shares
    "bypass uac": "T1548.002",        # Abuse Elevation Control Mechanism: Bypass User Account Control
    "mimikatz": "S0002",              # Software: Mimikatz
    "malicious file download": "T1105", # Ingress Tool Transfer
    "suspicious network traffic": "T1071", # Application Layer Protocol
    "usb drop attack": "T1091",       # Replication Through Removable Media
    "system information discovery": "T1082", # System Information Discovery
    "unusual process tree": "T1059",  # Command and Scripting Interpreter
    "living off the land": "T1218",   # Signed Binary Proxy Execution
}

def keyword_to_mitre(log_event: str) -> str:
    for k, v in MITRE_MAP.items():
        if k in log_event.lower():
            return v
    return "T0000"
