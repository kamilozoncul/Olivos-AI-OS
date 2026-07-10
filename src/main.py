from router import Router
from orchestrator import Orchestrator


def main():

    task = input("Görev: ")

    router = Router()

    workflow = router.route(task)

    print("\nWorkflow:", workflow)

    orchestrator = Orchestrator()

    results = orchestrator.execute(workflow, task)

    print("\nSonuçlar\n")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()