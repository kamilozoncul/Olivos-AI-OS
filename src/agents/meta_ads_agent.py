from agents.base_agent import BaseAgent


class MetaAdsAgent(BaseAgent):

    def __init__(self):
        super().__init__("MetaAdsAgent")

    def run(self, task):
        self.log(f"Preparing Meta Ads campaign: {task}")

        return {
            "agent": self.name,
            "result": "Meta Campaign Ready"
        }