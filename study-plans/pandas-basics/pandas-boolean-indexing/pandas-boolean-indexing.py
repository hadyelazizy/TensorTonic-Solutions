import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """

    df=pd.DataFrame(data)

    filtered_data=df.loc[df[column]>threshold].to_dict('list')


    
    return {
        'filtered_data':filtered_data,
        'count':len(df.loc[df[column]>threshold])
    }