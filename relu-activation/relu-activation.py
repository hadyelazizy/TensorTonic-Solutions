import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    arr=np.array(x,dtype=np.float64)

    return np.where(arr>=0,arr,0)