import numpy as np
from scipy import stats

def t_test_one_sample(data, mu_0, alpha):
    """
    Returns: dict with 't_stat', 'p_value', 'df' (floats), 'reject' (bool), 'ci_lower', 'ci_upper'.
    """

    arr=np.array(data,dtype=float)

    x_bar=np.mean(arr)

    s=np.std(arr,ddof=1)

    n=len(arr)

    degrees_of_freedom=n-1

    if s == 0:

        p_val=1

        if mu_0 == x_bar:
            t=0
        elif mu_0>x_bar:
            t=float('inf')
        else:
            t=float('-inf')

    else:
        t=round((x_bar-mu_0)/(s/n**0.5),4)
        p_val = round(2 * float(stats.t.sf(abs(t), degrees_of_freedom)), 4)

    return {"t_statistic": t, "degrees_of_freedom": degrees_of_freedom, "p_value": p_val, "reject_null": p_val < alpha}



    

    
    