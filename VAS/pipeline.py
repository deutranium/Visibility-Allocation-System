from abc import ABC, abstractmethod
from typing import override


class Pipeline(ABC):
    """
    Abstract class to define a VAS pipeline

    The attribute `has_ran` tracks if `run()` has been called at least once
    """

    def __init__(self):
        self.has_ran = False
        pass

    def add_tool(self, tool, *args):
        """
        Add a tool (node) to the pipeline (graph).

        This method runs `_add_tool()` - where the tool addition logic is
        implemented.

        Args:
        tool (VAS.tools.Tool): Tool to be added
        *args: Parameters for the tool
        """

        return self._add_tool(tool, *args)

    def add_connection(self, from_tool, to_tool):
        """Add a connection between tools (edge between nodes) of the pipeline
        (graph).

        This method runs `_add_connection()` - where the connection addition
        logic is implemented.

        Args:
        from_tool (VAS.tools.Tool): The tool that runs before the `to_tool`
        to_tool (VAS.tools.Tool): The tool that runs after the `from_tool`
        """

        return self._add_connection(from_tool, to_tool)

    def add_metric(self, metric, *args):
        """Add a metric to the pipeline. *args shold contain information about
        the tools the said metric will evaluate.

        Calls `_add_metric()`

        Args:
        metric (VAS.metrics.Metric): Metric attached to the pipeline
        *args: Parameters for metric, should contain information about what to
          evaluate. Check VAS.vas_addons.basic_pipeline.BasicPipeline for example.
        """
        return self._add_metric(metric, *args)

    def run(self, dataset):
        """Runs the whole pipeline.

        Calls `_run()`

        dataset (pandas.DataFrame): The dataset to run the pipeline with."""
        self.has_ran = True
        return self._run(dataset)

    def evaluate_metrics(self):
        """
        Evaluate all the metrics added using `add_metric()`.

        Calls `_evaluate_metrics()`
        """

        # checking if the pipeline has indeed ran
        assert self.has_ran
        return self._evaluate_metrics()

    @abstractmethod
    def _add_tool(self, tool, **args):
        pass

    @abstractmethod
    def _add_connection(self, from_tool, to_tool):
        pass

    @abstractmethod
    def _add_metric(self, metric, *args):
        pass

    @abstractmethod
    def _run(self, dataset):
        pass

    @abstractmethod
    def _evaluate_metrics(self):
        pass
