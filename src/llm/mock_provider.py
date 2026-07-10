from llm.provider import LLMProvider


class MockProvider(LLMProvider):

    def generate(self, system_prompt, user_prompt):

        return f"""

=== MOCK AI RESPONSE ===

SYSTEM

{system_prompt[:150]}...

-----------------------

USER

{user_prompt}

========================

"""