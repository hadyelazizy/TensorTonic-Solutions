import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    arr=np.array(data,dtype=np.float64)

    l_percentile=np.percentile(arr,lo_q,axis=0) #(n,)
    h_percentile=np.percentile(arr,hi_q,axis=0) #(n,)

    l_percentile=l_percentile[np.newaxis,:]
    h_percentile=h_percentile[np.newaxis,:]

    clipped_values=np.clip(arr,l_percentile,h_percentile)

    return np.stack([clipped_values,arr<l_percentile.astype(np.float64),arr>h_percentile.astype(np.float64)])
    

    