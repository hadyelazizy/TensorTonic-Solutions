import numpy as np
from scipy import stats

def clt_confidence_interval(data, confidence):
    """
    Returns: [mean, std_error, ci_lower, ci_upper] as a list.
    """
    arr=np.array(data,dtype=np.float64)
    n= len(arr)

    mean=round(np.mean(arr),4)
    std_error=round(np.std(arr,ddof=1)/n**0.5,4)
    z = round(float(stats.norm.ppf((1 + confidence) / 2)), 4)

    ci_lower = round(mean-z*std_error,4)
    ci_upper = round(mean+z*std_error,4)

    return [mean, std_error, ci_lower, ci_upper]