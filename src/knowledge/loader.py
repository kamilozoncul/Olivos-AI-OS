from pathlib import Path


class KnowledgeLoader:

    def load(self, filepath):

        path = Path(filepath)

        if not path.exists():
            return ""

        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )