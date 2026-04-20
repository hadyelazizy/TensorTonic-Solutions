import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df=pd.DataFrame(data)

    df1=df.set_index(index_col)

    df1_cols=df1.columns.tolist()

    df2=df1.reset_index()

    df2_cols=df2.columns.tolist()

    return [df1_cols,df2_cols]

    