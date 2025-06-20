import json

def extract_cves(trivy_report_path):
    with open(trivy_report_path) as f:
        report = json.load(f)
    vulns = []
    for target in report.get("Results", []):
        for vuln in target.get("Vulnerabilities", []):
            vulns.append({
                "id": vuln["VulnerabilityID"],
                "severity": vuln["Severity"],
                "score": vuln.get("CVSS", {}).get("nvd", {}).get("V3Score", 5.0)
            })
    return vulns

def extract_cves_by_package(trivy_path):
    with open(trivy_path) as f:
        report = json.load(f)
    cve_map = {}
    for target in report.get("Results", []):
        for vuln in target.get("Vulnerabilities", []):
            pkg = vuln.get("PkgName")
            if not pkg:
                continue
            entry = {
                "id": vuln["VulnerabilityID"],
                "severity": vuln["Severity"],
                "score": vuln.get("CVSS", {}).get("nvd", {}).get("V3Score", 5.0)
            }
            cve_map.setdefault(pkg.lower(), []).append(entry)
    return cve_map

trivy_file_path = "../sboms/trivy.json"
extracted_vulns = extract_cves(trivy_file_path)

# Print output
for v in extracted_vulns:
    print(f"CVE ID: {v['id']}, Severity: {v['severity']}, CVSS Score: {v['score']}")
