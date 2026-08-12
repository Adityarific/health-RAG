from app.loaders.pdf_loader import PDFLoader
from app.preprocessing.splitter import TextSplitter
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.chroma_store import ChromaStore


# pdf_path = "knowledge_base/nutrition/healthy_diet.pdf"

# loader = PDFLoader()
# documents = loader.load(pdf_path)

# splitter = TextSplitter()
# chunks = splitter.split(documents)

embedding_model = EmbeddingModel()

store = ChromaStore(embedding_model)
# store.add_documents(chunks)

# print(f"Added {len(chunks)} chunks to ChromaDB.")

results = store.similarity_search(
    "What is a diet for adult?",
    k=1
)

print("\nRetrieved chunks:\n")

for i, result in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print(result.page_content[:500])
    print("Metadata:", result.metadata)
    print()