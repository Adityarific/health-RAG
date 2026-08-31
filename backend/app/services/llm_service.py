import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is not set in the .env file")


class LLMService:
    def __init__(self):
        self.client = InferenceClient(
            api_key=HF_TOKEN
        )

        self.model = "google/gemma-4-31B-it:novita"

    def generate(self, prompt: str) -> str:
        response = self.client.chat_completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=700,
            temperature=0.3,
        )

        return response.choices[0].message.content