import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df=pd.DataFrame(data)

    rows,cols=df.shape

    columns=df.columns.tolist()

    dtypes={col:type for col,type in df.dtypes.items()}

    total_values=df.size

    return {
        "rows":rows,
        "cols":cols,
        "columns":columns,
        "dtypes":dtypes,
        "total_values":total_values
    }