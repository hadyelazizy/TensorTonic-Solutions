import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr=np.array(data,dtype=np.float64)
    
    mask_1=(arr>threshold).astype(np.float64)

    mask2=np.any(arr>threshold,axis=1)

    mask3=np.all(arr>threshold,axis=1)

    mask2=mask2[:,np.newaxis]
    mask3=mask3[:,np.newaxis]


    any_filtered = np.where(mask2,arr, 0.0)

    all_filtered = np.where(mask3,arr, 0.0)

    return np.stack([mask_1, any_filtered, all_filtered])
