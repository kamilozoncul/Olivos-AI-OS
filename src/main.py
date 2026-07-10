from registry import AgentRegistry
from router import Router
from orchestrator import Orchestrator


def main():

    task = input("Görev: ")

    router = Router()

    workflow = router.route(task)

    print("\nWorkflow:", workflow)

    registry = AgentRegistry()

    orchestrator = Orchestrator(registry)

    results = orchestrator.execute(workflow, task)

    print("\nSonuçlar\n")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()