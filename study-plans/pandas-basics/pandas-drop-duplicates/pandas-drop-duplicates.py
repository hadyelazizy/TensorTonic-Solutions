import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df=pd.DataFrame(data)

    r0=len(df)

    df1=df.drop_duplicates()

    r1=len(df1)

    return [r0,r1,df1.to_dict('list')]

    