import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """

    left_df=pd.DataFrame(left)
    right_df=pd.DataFrame(right)

    return pd.merge(left_df,right_df,on=on,how=how).to_dict('list')
