from abc import ABC, abstractmethod
import pandas as pd


class Tool(ABC):
    """Abstract class to define a tool."""

    def __init__(self):
        super().__init__()
        self.metrics = []
        pass

    def run(self, **kwargs):
        res = self._run(**kwargs)

        assert (
            type(res) == pd.Series
        ), "`_run()` of a subclass of VAS.tools.Tool should return an object \
            of type pandas.Series"
        # checks
        return self._run(**kwargs)

    @abstractmethod
    def _run(self, **kwargs):
        """
        Abstract method defining how the tool runs. This would almost always
        include a dataset, but we do not mention it in the method signature to
        keep the scope open for tools that don't necessarily operate on a
        dataset.
        """
        pass


class Filter(Tool, ABC):
    """Abstract class to define a filter tool"""

    def __init__(self, func):
        super().__init__()
        self.func = func

    def filter(self, dataset, **kwargs):
        """
        Calls `_filter()`

        Args:
            dataset (pandas.DataFrame, required): The dataset to operate on."""
        return self._filter(dataset, **kwargs)

    @abstractmethod
    def _filter(self, dataset, **kwargs):
        """
        Implement the filtering mechanism on the input dataset.

        Args:
            dataset (pandas.DataFrame, required): The dataset to operate on.
        """
        pass

    def _run(self, **kwargs):
        return self.filter(**kwargs)


class Search(Tool):
    """Abstract class to define a search tool"""

    def __init__(self):
        super().__init__()

    def search(self, dataset, **kwargs):
        """
        Calls `_search()`

        Args:
            dataset (pandas.DataFrame, required): The dataset to operate on."""
        return self.search(dataset, **kwargs)

    @abstractmethod
    def _search(self, dataset, **kwargs):
        """
        Implement the search mechanism on the input dataset.

        Args:
            dataset (pandas.DataFrame, required): The dataset to operate on.
        """
        pass

    def _run(self, **kwargs):
        return self.search(**kwargs)


class Sort(Tool):
    """Abstract class to define a sort tool"""

    def __init__(self):
        super().__init__()

    def sort(self, dataset, **kwargs):
        """
        Calls `_sort()`

        Args:
            dataset (pandas.DataFrame, required): The dataset to operate on."""
        return self._sort(dataset, **kwargs)

    @abstractmethod
    def _sort(self, dataset, **kwargs):
        """
        Implement the sort mechanism on the input dataset.

        Args:
            dataset (pandas.DataFrame, required): The dataset to operate on.
        """
        pass

    def _run(self, **kwargs):
        return self.sort(**kwargs)
