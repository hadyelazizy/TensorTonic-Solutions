import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a=np.array(a,dtype=np.float64)
    b=np.array(b,dtype=np.float64)

    a=np.clip(a,lo,hi)
    b=np.clip(b,lo,hi)

    a_num=a-lo
    b_num=b-lo

    den=hi-lo


    
    return np.abs(np.where(den!=0,(a_num/den),0)-np.where(den!=0,(b_num/den),0))

    

    
