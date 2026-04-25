import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    arr=np.array(x,dtype=np.float64)

    return 1/(np.exp(-arr)+1)