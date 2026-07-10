from pathlib import Path

from agents.base_agent import BaseAgent
from knowledge.loader import KnowledgeLoader
from llm.factory import LLMFactory


class ContentAgent(BaseAgent):

    def __init__(self):
        super().__init__("ContentAgent")

        self.loader = KnowledgeLoader()
        self.llm = LLMFactory.create()

    def run(self, task, context):

        base = Path(__file__).resolve().parents[2]

        system_prompt = self.loader.load(
            base / "Agents" / "ContentAgent" / "SystemPrompt.md"
        )

        framework = self.loader.load(
            base / "Agents" / "ContentAgent" / "ContentFramework.md"
        )

        workflow = self.loader.load(
            base / "Agents" / "ContentAgent" / "Workflow.md"
        )

        seo_result = context.get("seo")

        previous_output = ""

        if seo_result:
            previous_output = seo_result["result"]

        full_prompt = f"""
PREVIOUS AGENT OUTPUT

{previous_output}

--------------------

SYSTEM

{system_prompt}

FRAMEWORK

{framework}

WORKFLOW

{workflow}
"""

        response = self.llm.generate(
            full_prompt,
            task
        )

        self.log("Content knowledge loaded successfully.")

        return {
            "agent": self.name,
            "result": response
        }