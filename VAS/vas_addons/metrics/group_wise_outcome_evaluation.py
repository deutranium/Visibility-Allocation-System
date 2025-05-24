from VAS.metrics import Metric


class GroupWiseOutcomeEvaluation(Metric):
    """Evaluate outcome of a tool by groups

    Attributes:
        col_with_groups (str, required): Name of the column with groups
            operation_on_col (function, required): A function that returns a value for
                the column to be evaluated, when grouped by groups in
                col_with_groups
    """

    def __init__(self, col_with_groups, operation_on_col):
        super().__init__()
        self.col_with_groups = col_with_groups
        self.operation_on_col = operation_on_col

    def _evaluate(self, dataset, col_to_evaluate):  # type: ignore -- not the best practice, but it's fine
        """
        Evaluate `col_to_evaluate` by groups defined in `self.col_with_groups`

        Args:
        dataset (pandas.DataFrame, required): Final dataset after a pipeline
            has run
        col_to_evaluate (str, required): Name of the dataframe column to be
            evaluated
        """
        groups = list(dataset[self.col_with_groups].unique())
        res = {}

        for group in groups:
            group_rows = dataset[dataset[self.col_with_groups] == group]
            res[group] = self.operation_on_col(group_rows[col_to_evaluate])

        return res
