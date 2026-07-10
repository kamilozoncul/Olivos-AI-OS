from agents.base_agent import BaseAgent


class IdeaSoftAgent(BaseAgent):

    def __init__(self):
        super().__init__("IdeaSoftAgent")

    def run(self, task):
        self.log(f"Processing IdeaSoft task: {task}")

        return {
            "agent": self.name,
            "result": "IdeaSoft Task Completed"
        }