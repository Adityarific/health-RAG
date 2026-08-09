from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReportRequest(BaseModel):
    report: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Nutrition Report AI Backend!"
    }

@app.post("/analyze")
def analyze_report(request: ReportRequest):
    return {
        "message": "Report received successfully!",
        "report": request.report
    }
