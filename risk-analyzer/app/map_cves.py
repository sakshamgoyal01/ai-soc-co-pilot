import json
from sbom_parser import extract_components
from trivy_parser import extract_cves
from trivy_parser import extract_cves_by_package
from scorer import calculate_risk_score

def enrich_components_with_cves(sbom_path, trivy_path):
    components = extract_components(sbom_path)
    cve_map = extract_cves_by_package(trivy_path)

    for comp in components:
        comp_name = comp["name"].lower()
        matched_cves = cve_map.get(comp_name, [])
        comp["cves"] = matched_cves
        comp["risk_score"] = calculate_risk_score(matched_cves)

    return components

# Example usage
sbom_file = "../sboms/sbom.json"
trivy_file = "../sboms/trivy.json"

enriched_report = enrich_components_with_cves(sbom_file, trivy_file)

# Print or save result
print(json.dumps(enriched_report, indent=2))