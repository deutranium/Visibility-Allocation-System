from VAS.tools import Sort


class SortByKey(Sort):
    """Sort a dataframe's column by the length of data in each cell

    Args: None
    Returns: None
    """

    def __init__(self):
        super().__init__()

    def key_function(self, s):
        """
        Key function to map the data point `s` to its length

        Args:
            s (object, required): A sequence or a collection on which len()
                can operate
        """
        return len(s)

    def _sort(self, dataset, col_to_sort_by, **kwargs):
        """
        Produces ranks using pandas.DataFrame.rank(). The _sort() method supports
            custom **kwargs for pandas.DataFrame.rank()

        Args:
            dataset (pandas.DataFrame, required): dataset to run the operation on
            col_to_sort_by (str, required): Name of the column to sort
            **kwargs (**dict): custom keyword arguments for pandas.DataFrame.rank()

        Returns:
            a pandas.Series object with ranks for every row of col_to_sort_by
        """
        data = dataset[col_to_sort_by]
        res_col = data.rank(**kwargs)

        return res_col
