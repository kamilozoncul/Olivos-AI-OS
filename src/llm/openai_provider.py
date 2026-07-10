import os

from dotenv import load_dotenv
from openai import OpenAI

from llm.provider import LLMProvider

load_dotenv()


class OpenAIProvider(LLMProvider):

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY bulunamadı. .env dosyasını kontrol edin."
            )

        self.client = OpenAI(api_key=api_key)

    def generate(self, system_prompt, user_prompt):

        response = self.client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response.choices[0].message.content