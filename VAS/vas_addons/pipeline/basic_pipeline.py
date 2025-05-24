from VAS.pipeline import Pipeline
import copy


# pipeline
class BasicPipeline(Pipeline):
    def __init__(self):
        super().__init__()
        self.tools_to_run = []
        self.metrics_to_evaluate = []

    def _add_tool(self, tool, config):
        tool = copy.deepcopy(tool)  # not sure if this works. intuition: user
        # can add the same instance of tool class multiple times, but
        # there should be a way to differentiate them
        self.tools_to_run.append({"tool": tool, "config": config})

        # here only for readability, it doesn't do anything
        self._add_connection()

    def _add_metric(self, metric, config):
        self.metrics_to_evaluate.append({"metric": metric, "config": config})

    def _add_connection(self):
        pass

    def _run(self, dataset):
        dataset = dataset.copy()
        self.res_cols = {}
        for elem in self.tools_to_run:
            tool, config = elem["tool"], elem["config"]
            config["kwargs"]["dataset"] = dataset
            res_col = tool.run(**config["kwargs"])
            dataset[config["col_name"]] = res_col
            self.res_cols[config["col_name"]] = res_col  # check for dupes?

        self.final_dataset = dataset
        return dataset

    def _evaluate_metrics(self):
        self.evals = {}
        for elem in self.metrics_to_evaluate:
            metric, config = elem["metric"], elem["config"]
            self.evals[metric] = {}
            for col_name in config["col_names"]:
                res = metric.evaluate(self.final_dataset, col_name)
                self.evals[metric][col_name] = res
