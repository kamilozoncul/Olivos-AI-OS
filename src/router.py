class Router:

    def route(self, task):

        task = task.lower()

        workflow = []

        if any(word in task for word in ["strateji", "strategy", "plan"]):
            workflow.append("ceo")

        if any(word in task for word in ["seo", "keyword"]):
            workflow.append("seo")

        if any(word in task for word in ["blog", "content", "içerik"]):
            workflow.append("content")

        if any(word in task for word in ["meta", "facebook", "instagram", "ads", "reklam"]):
            workflow.append("meta")

        if any(word in task for word in ["analiz", "analytics", "kpi", "rapor"]):
            workflow.append("analytics")

        if any(word in task for word in ["ideasoft", "ürün", "kategori", "mağaza"]):
            workflow.append("ideasoft")

        workflow.append("reporting")

        return workflow