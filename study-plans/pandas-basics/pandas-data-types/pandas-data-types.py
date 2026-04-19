import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df=pd.DataFrame(data)

    dtypes={str(c):str(t) for c,t in df.dtypes.items()}


    type_counts={}

    for c,t in df.dtypes.items():

        t=str(t)

        if t in type_counts:

            type_counts[t]+=1
        else:
            type_counts[t]=1
    
    num_columns=int(df.shape[1])

    dict={
        "dtypes":dtypes,
        "type_counts":type_counts,
        "num_columns":num_columns
    }
    return dict