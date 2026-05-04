import numpy as np

def pearson_correlation(X):
    """
    Returns: ndarray, the Pearson correlation matrix.
    """
    X = np.asarray(X, dtype=float)
    return np.corrcoef(X,rowvar=False)
