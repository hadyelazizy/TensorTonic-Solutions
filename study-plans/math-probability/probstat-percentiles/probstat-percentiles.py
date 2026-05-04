import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    x = np.asarray(x, dtype=float)

    return np.percentile(x,q)

