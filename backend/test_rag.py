from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retriever.nutrition_retriever import NutritionRetriever
from app.services.llm_service import LLMService
from app.services.rag_service import RAGService


embedding_model = EmbeddingModel()

store = ChromaStore(embedding_model)

retriever = NutritionRetriever(store.vectorstore)

llm_service = LLMService()

rag_service = RAGService(
    retriever=retriever,
    llm_service=llm_service,
)


report = """
Hemoglobin: 10 g/dL
Vitamin D: 18 ng/mL
Vitamin B12: 170 pg/mL
The person wants advice about improving their diet.
"""

result = rag_service.analyze(report)

print("\n========== NUTRITION ANALYSIS ==========\n")
print(result)