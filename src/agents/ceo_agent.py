from agents.base_agent import BaseAgent


class CEOAgent(BaseAgent):

    def __init__(self):
        super().__init__("CEOAgent")

    def run(self, task):
        self.log(f"Planning strategy: {task}")

        return {
            "agent": self.name,
            "result": "Strategy Created"
        }