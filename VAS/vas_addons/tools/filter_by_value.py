from VAS.tools import Filter


class FilterByValue(Filter):
    """Filter out values based on a custom function `func`.

    Attributes:
        func (function): A function that takes one data point (i.e. one cell of
          a dataframe) and returns a boolean value indicating if the value
          should be filtered out (returns False), or if it should stay in the
          dataset (returns True)

    Returns: None
    """

    def __init__(self, func):
        super().__init__(func)

    def _filter(self, dataset, col_to_filter_by):
        """
        Produces a mask with boolean values indicating if the respective
        datapoint should be filtered (boolean value False) out or if it
        stays (boolean value True)

        Args:
            dataset (pandas.DataFrame, required): dataset to run the operation on
            col_to_filter_by (str, required): Name of the column to filter

        Returns:
            a pandas.Series object with a boolean mask
        """

        res_col = dataset[col_to_filter_by].apply(lambda x: self.func(x))
        return res_col
