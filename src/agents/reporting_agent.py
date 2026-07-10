from agents.base_agent import BaseAgent


class ReportingAgent(BaseAgent):

    def __init__(self):
        super().__init__("ReportingAgent")

    def run(self, results):
        self.log("Preparing final report...")

        return {
            "agent": self.name,
            "summary": results
        }