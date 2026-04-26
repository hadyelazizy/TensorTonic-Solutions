import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true=np.array(y_true,dtype=np.float64)
    y_pred=np.array(y_pred,dtype=np.float64)


    e=y_true-y_pred
    x=0.5*(e**2)
    y=delta*(np.abs(e)-(0.5*delta))
    
    loss=np.where(np.abs(e)<=delta,x,y)

    return np.mean(loss)