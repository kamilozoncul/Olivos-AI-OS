from agents.base_agent import BaseAgent


class ContentAgent(BaseAgent):

    def __init__(self):
        super().__init__("ContentAgent")

    def run(self, task):
        self.log(f"Creating content for: {task}")

        return {
            "agent": self.name,
            "result": "Content Generated"
        }