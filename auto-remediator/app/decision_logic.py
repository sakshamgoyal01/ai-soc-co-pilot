import os
from openai import OpenAI

# Set up Groq client
client = OpenAI(
    api_key="57668865",  # Replace with your actual Groq API key
    base_url="https://api.groq.com/openai/v1"
)

def decide_action(threat: dict) -> str:
    """
    Given a threat dictionary with keys: mitre_id, severity, component, explanation,
    return a single recommended remediation action.
    """
    prompt = f"""
Given this threat:
- MITRE ID: {threat['mitre_id']}
- Severity: {threat['severity']}
- Component: {threat['component']}
- Explanation: {threat['explanation']}

Decide ONE remediation action from this list:
- isolate_pod
- restart_service
- revoke_access
- rotate_secret
- escalate_to_human

Respond with just the action.
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a cybersecurity assistant. Always respond with exactly one action from the list."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=10
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    sample_threat = {
        "mitre_id": "T1078",
        "severity": "High",
        "component": "Authentication Service",
        "explanation": "Detected use of compromised credentials to access protected resource"
    }

    action = decide_action(sample_threat)
    print("🔧 Recommended Action:", action)
