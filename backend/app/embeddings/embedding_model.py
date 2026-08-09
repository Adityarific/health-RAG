from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def embed_documents(self, documents):
        return self.model.embed_documents(
            [document.page_content for document in documents]
        )

    def embed_query(self, query: str):
        return self.model.embed_query(query)