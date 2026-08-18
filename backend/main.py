from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retriever.nutrition_retriever import NutritionRetriever
from app.services.llm_service import LLMService
from app.services.rag_service import RAGService


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


embedding_model = EmbeddingModel()

vectorstore = ChromaStore(embedding_model)

retriever = NutritionRetriever(vectorstore.vectorstore)

llm_service = LLMService()

rag_service = RAGService(
    retriever=retriever,
    llm_service=llm_service,
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Nutrition Report AI Backend!"
    }


@app.post("/analyze")
def analyze_report(request: ReportRequest):
    analysis = rag_service.analyze(request.report)

    return {
        "message": "Report analyzed successfully!",
        "analysis": analysis,
    }