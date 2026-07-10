from llm.config import LLM_PROVIDER

from llm.mock_provider import MockProvider
from llm.openai_provider import OpenAIProvider


class LLMFactory:

    @staticmethod
    def create():

        provider = LLM_PROVIDER.lower()

        if provider == "mock":
            return MockProvider()

        if provider == "openai":
            return OpenAIProvider()

        raise ValueError(
            f"Unknown LLM provider: {LLM_PROVIDER}"
        )