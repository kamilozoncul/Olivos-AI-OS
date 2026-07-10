from registry import AgentRegistry


class Orchestrator:

    def __init__(self):
        self.registry = AgentRegistry()

    def execute(self, workflow, task):

        results = []
        context = {}

        for agent_name in workflow:

            agent = self.registry.get(agent_name)

            if agent is None:
                continue

            result = agent.run(task, context)

            results.append(result)

            # ReportingAgent context'e eklenmesin
            if agent_name != "reporting":
                context[agent_name] = result

        return results