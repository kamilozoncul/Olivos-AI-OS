from agents.base_agent import BaseAgent


class SEOAgent(BaseAgent):

    def __init__(self):
        super().__init__("SEOAgent")

    def run(self, task):
        self.log(f"Analyzing SEO task: {task}")

        return {
            "agent": self.name,
            "result": "SEO Analysis Completed"
        }