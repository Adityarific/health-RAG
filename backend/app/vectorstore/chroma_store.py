from langchain_chroma import Chroma


class ChromaStore:
    def __init__(self, embedding_model):
        self.vectorstore = Chroma(
            collection_name="nutrition_knowledge",
            embedding_function=embedding_model.model,
            persist_directory="chroma_db",
        )

    def add_documents(self, documents):
        self.vectorstore.add_documents(documents)

    def similarity_search(self, query: str, k: int = 3):
        return self.vectorstore.similarity_search(query, k=k)