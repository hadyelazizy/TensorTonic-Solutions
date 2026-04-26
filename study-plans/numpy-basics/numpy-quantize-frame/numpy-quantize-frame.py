import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    arr=np.array(data,dtype=np.float64)

    pad=lambda x: np.pad(x,pad_width,mode='constant',constant_values=0.0)

    rounded = pad(np.round(arr, decimals))
    floored = pad(np.floor(arr))
    ceiled  = pad(np.ceil(arr))
    return np.stack([rounded, floored, ceiled])   



    

    

    