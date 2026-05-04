import numpy as np

def skewness_kurtosis(data):
    """
    Returns: dict with 'skewness', 'kurtosis', and interpretation strings.
    """
    arr=np.array(data,dtype=np.float64)

    n=len(arr)

    mean=np.mean(arr)

    std=np.std(arr,ddof=1)

    g1=(n/((n-1)*(n-2)))*np.sum(((arr-mean)/std)**3)
    g2 = ((n * (n+1)) / ((n-1) * (n-2) * (n-3))) * np.sum(((arr - mean) / std) ** 4) - (3 * (n-1)**2) / ((n-2) * (n-3))

    g1 = round(float(g1), 4)
    g2 = round(float(g2), 4)

    if g1 > 0.5:
        skew_interp = "right-skewed"
    elif g1<-0.5:
        skew_interp = "left-skewed"
    else:
        skew_interp = "approximately symmetric"
        
    if g2 > 1:
        kurt_interp = "leptokurtic"
    elif g2 < -1:
        kurt_interp = "platykurtic"
    else:
        kurt_interp = "mesokurtic"

    return {
        'skewness':g1,
        'kurtosis':g2,
        'skew_interpretation':skew_interp,
        'kurtosis_interpretation':kurt_interp
    }
