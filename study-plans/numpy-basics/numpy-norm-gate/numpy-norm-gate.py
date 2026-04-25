import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    z=np.array(X,dtype=np.float64) @ np.array(W,dtype=np.float64)

    norm=np.linalg.norm(z,axis=1)

    return np.where(norm[:,np.newaxis]>=threshold,z,0.0)