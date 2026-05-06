import numpy as np

def matrix_transpose(A):
    """
    Returns: ndarray, the transpose of A.
    """
    arr=np.array(A,dtype=np.float64)

    return arr.T