import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df=pd.DataFrame(data)

    if operation =='rank':

        df[f"{column}_transformed"]=df[column].rank()

    elif operation =="cumsum":
        df[f"{column}_transformed"]=df[column].cumsum()

    elif operation =="normalize":
        col_min = df[column].min()
        col_max = df[column].max()
        df[f"{column}_transformed"]=df[column].apply(
            lambda x: round((x - col_min) / (col_max - col_min), 4)
        )

    else:
        df[f"{column}_transformed"]=df[column].apply(lambda x:(x*2))

    return df.to_dict('list')
        


        

