class Orchestrator:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, workflow, task):

        results = []

        for step in workflow:

            agent = self.registry.get(step)

            result = agent.run(task)

            results.append(result)

        return results