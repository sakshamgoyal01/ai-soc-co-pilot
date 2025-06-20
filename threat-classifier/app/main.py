from fastapi import FastAPI
from classify import classify_log
from schemas import LogInput, ClassificationResult

app = FastAPI()

@app.post("/classify", response_model=ClassificationResult)
async def classify_endpoint(log: LogInput):
    return await classify_log(log)