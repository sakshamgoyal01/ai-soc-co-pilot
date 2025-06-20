import json

def extract_components(sbom_path):
    with open(sbom_path) as f:
        sbom = json.load(f)
    components = []

    for pkg in sbom.get("packages", []):
        components.append({
            "name": pkg["name"],
            "version": pkg.get("versionInfo", "unknown"),
            "type": "library"
        })
    return components

sbom_file_path = "../sboms/sbom.json"
# Use updated function with SPDX-based SBOM
extracted_spdx_components = extract_components(sbom_file_path)

# Output results
print(extracted_spdx_components)



