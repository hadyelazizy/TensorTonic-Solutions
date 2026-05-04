import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    arr = np.asarray(x, dtype=float)
    mean=np.mean(arr)
    median=np.median(arr)

    counts = Counter(arr)
    mode = float(max(counts, key=counts.get))
    return {
        'mean':mean,
        'median':median,
        'mode':mode
    }
    