import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    df=pd.DataFrame(data)

    pv_table=pd.pivot_table(
        df,
        values=values,
        columns=columns,
        index=index,
        aggfunc=aggfunc,
        fill_value=0
    )

    return pv_table.to_dict()