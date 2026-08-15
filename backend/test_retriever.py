from app.loaders.pdf_loader import PDFLoader
from app.preprocessing.splitter import TextSplitter
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore
from app.retriever.nutrition_retriever import NutritionRetriever


pdf_path = "knowledge_base/nutrition/healthy_diet.pdf"

loader = PDFLoader()
documents = loader.load(pdf_path)

splitter = TextSplitter()
chunks = splitter.split(documents)

embedding_model = EmbeddingModel()

store = ChromaStore(embedding_model)
store.add_documents(chunks)

retriever = NutritionRetriever(store.vectorstore)

results = retriever.retrieve(
    "What foods should be included in a healthy diet?",
    k=1
)

print(f"Retrieved {len(results)} chunks.\n")

for i, result in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print(result.page_content[:500])
    print("Source:", result.metadata.get("source"))
    print("Page:", result.metadata.get("page"))
    print()