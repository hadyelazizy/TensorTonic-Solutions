import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    arr=np.array(data,dtype=np.float64)

    arr_copy=arr[row_idx].copy()

    clipped_arr=np.clip(arr_copy,lo,hi)

    return np.stack([arr_copy,clipped_arr])