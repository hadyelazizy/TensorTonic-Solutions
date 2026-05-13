import numpy as np

def mle_normal(data):
    """
    Returns: dict with 'mu_hat' and 'sigma_hat' as floats (MLE estimates).
    """
    arr=np.array(data,dtype=np.float64)

    mu_hat=round(np.mean(arr),4)
    sigma_hat=round(np.std(arr,ddof=0),4)
    return {"mu_mle": mu_hat, "sigma_mle": sigma_hat}


    