from app.services.llm_service import LLMService


llm = LLMService()

prompt = """
Explain in simple terms why eating fruits and vegetables
is important in a healthy diet.
"""

response = llm.generate(prompt)

print("\nLLM Response:\n")
print(response)