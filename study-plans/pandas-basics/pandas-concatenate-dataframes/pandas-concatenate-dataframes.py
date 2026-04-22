import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    dataframes=[pd.DataFrame(df) for df in dfs]

    result=pd.concat(dataframes,ignore_index=True)

    return [list(result.shape),result.to_dict('list')]

    