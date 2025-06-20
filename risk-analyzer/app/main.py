from fastapi import FastAPI, UploadFile
from sbom_parser import extract_components
from trivy_parser import extract_cves_by_package
from map_cves import enrich_components_with_cves
from trivy_parser import extract_cves
from scorer import calculate_risk_score
from schemas import ArtifactRisk

app = FastAPI()


@app.post("/analyze", response_model=list[ArtifactRisk])
async def analyze_sbom(sbom: UploadFile, trivy: UploadFile):
    sbom_path = f"/tmp/{sbom.filename}"
    trivy_path = f"/tmp/{trivy.filename}"

    with open(sbom_path, "wb") as f: f.write(await sbom.read())
    with open(trivy_path, "wb") as f: f.write(await trivy.read())

    components = extract_components(sbom_path)
    cves = extract_cves(trivy_path)
    cve_map = extract_cves_by_package(trivy_path)

    artifact_risks = []
    for comp in components:
        comp_name = comp["name"].lower()
        matched_cves = cve_map.get(comp_name, [])
        comp["cves"] = matched_cves
        comp["risk_score"] = calculate_risk_score(matched_cves)
        artifact_risks.append(ArtifactRisk(
            name=comp["name"],
            component_type=comp["type"],
            cves=comp["cves"],
            risk_score=comp["risk_score"]
        ))

    return artifact_risks
