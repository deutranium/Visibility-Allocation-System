from abc import ABC, abstractmethod

# individual fairness
# accuracy


class Metric(ABC):
    """Abstract class to create metrics."""

    def __init__(self):
        pass

    def evaluate(self, dataset, *args):
        """Calls _evaluate()

        Args:
        dataset (pandas.DataFrame): final dataset after a pipeline has run"""
        return self._evaluate(dataset, *args)

    @abstractmethod
    def _evaluate(self, dataset, *args):
        """The logic to evaluate a metric goes here

        Args:
        dataset (pandas.DataFrame): final dataset after a pipeline has run"""
        pass
