import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    df=pd.DataFrame(data)

    agg_df=df.groupby(group_col)[value_col]

    return {f:agg_df.agg(f).to_dict() for f in funcs}