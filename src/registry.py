from agents.seo_agent import SEOAgent
from agents.content_agent import ContentAgent
from agents.analytics_agent import AnalyticsAgent
from agents.reporting_agent import ReportingAgent
from agents.ceo_agent import CEOAgent
from agents.meta_ads_agent import MetaAdsAgent
from agents.ideasoft_agent import IdeaSoftAgent


class AgentRegistry:

    def __init__(self):
        self.agents = {
            "ceo": CEOAgent(),
            "seo": SEOAgent(),
            "content": ContentAgent(),
            "meta": MetaAdsAgent(),
            "analytics": AnalyticsAgent(),
            "ideasoft": IdeaSoftAgent(),
            "reporting": ReportingAgent(),
        }

    def get(self, name):
        return self.agents.get(name)