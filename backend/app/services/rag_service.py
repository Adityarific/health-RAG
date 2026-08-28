from app.prompts.nutrition_prompt import build_nutrition_prompt


class RAGService:
    def __init__(self, retriever, llm_service):
        self.retriever = retriever
        self.llm_service = llm_service

    def analyze(self, report: str) -> str:
        documents = self.retriever.retrieve(report, k=3)

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = build_nutrition_prompt(
            report=report,
            context=context,
        )

        return self.llm_service.generate(prompt)