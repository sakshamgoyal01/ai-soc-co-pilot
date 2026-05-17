import os
import openai
from openai import OpenAI
# Set your Groq API key

client = OpenAI(
    api_key="g798657897656",  # Replace with your actual Groq API key
    base_url="https://api.groq.com/openai/v1"
)

def query_openai(log_event: str) -> str:
    prompt = f"""
You are a cybersecurity threat analyst.
Analyze this log: "{log_event}"
Respond only in compact JSON format with:
- category (e.g., Recon, Initial Access)
- severity (Low/Medium/High/Critical)
- mitre_id (like T1078)
- confidence (0–100)
- remediation
- explanation
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # or llama3-70b-8192
        messages=[
            {"role": "system", "content": "You are a helpful cybersecurity assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    log = "Suspicious PowerShell execution from user ADMIN"
    result = query_openai(log)
    print("🔍 Analysis:\n", result)
