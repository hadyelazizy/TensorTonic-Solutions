import numpy as np
from scipy import stats

def correlation_analysis(x, y):
    """
    Returns: dict with 'r', 't_stat', 'p_value' (floats), 'reject' (bool).
    """
    x=np.array(x,dtype=float)
    y=np.array(y,dtype=float)

    r=float(np.corrcoef(x,y,rowvar=False)[0, 1])

    r=round(r,4)

    n=len(x)

    r_squared=round(r*r,4)

    t_stat = round(r * ((n - 2)**0.5) / ((1 - r**2)**0.5), 4)

    t_stat=round(t_stat,4)
    p_val = round(2 * float(stats.t.sf(abs(t_stat), n - 2)), 4)
    return {"r": r, "r_squared": r_squared, "t_stat": t_stat, "p_value": p_val, "significant": p_val < 0.05}

