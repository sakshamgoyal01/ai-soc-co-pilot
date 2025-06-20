from fastapi import FastAPI
from router import process_threat
from router import router
from schemas import ThreatResponse
app = FastAPI(
    title="Cybersecurity Threat Analyzer",
    version="1.0.0"
)
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Cybersecurity Threat Analyzer API is running"}


