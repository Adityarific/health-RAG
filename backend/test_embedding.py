from app.embeddings.embedding_model import EmbeddingModel


embedding_model = EmbeddingModel()

text = "A healthy diet should include a variety of nutritious foods."

vector = embedding_model.embed_query(text)

print(f"Embedding dimensions: {len(vector)}")
print(f"First 10 values: {vector[:10]}")