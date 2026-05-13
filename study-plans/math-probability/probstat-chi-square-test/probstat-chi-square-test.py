import numpy as np
from scipy import stats

def chi_square_test(observed, expected):
    """
    Returns: [chi2_stat, df, p_value, reject] as a list.
    """
    obs=np.array(observed,dtype=float)
    exp=np.array(expected,dtype=float)

    chi2=round(np.sum((obs-exp)**2/exp),4)

    df=len(obs)-1

    p_val = round(float(stats.chi2.sf(chi2, df)), 4)
    return [chi2, df, p_val, p_val < 0.05]    