from pathlib import Path

from agents.base_agent import BaseAgent
from knowledge.loader import KnowledgeLoader
from llm.factory import LLMFactory


class SEOAgent(BaseAgent):

    def __init__(self):
        super().__init__("SEOAgent")

        self.loader = KnowledgeLoader()
        self.llm = LLMFactory.create()

    def run(self, task, context):

        base = Path(__file__).resolve().parents[2]

        system_prompt = self.loader.load(
            base / "Agents" / "SEOAgent" / "SystemPrompt.md"
        )

        framework = self.loader.load(
            base / "Agents" / "SEOAgent" / "SEOFramework.md"
        )

        workflow = self.loader.load(
            base / "Agents" / "SEOAgent" / "Workflow.md"
        )

        full_prompt = f"""
{system_prompt}

{framework}

{workflow}
"""

        response = self.llm.generate(
            full_prompt,
            task
        )

        self.log("SEO knowledge loaded successfully.")

        return {
            "agent": self.name,
            "result": response
        }