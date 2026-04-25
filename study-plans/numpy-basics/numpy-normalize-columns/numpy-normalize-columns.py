import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    arr=np.array(data,dtype=np.float64)

    mean=np.mean(arr,axis=0)
    std=np.std(arr,axis=0)

    return (arr-mean)/std