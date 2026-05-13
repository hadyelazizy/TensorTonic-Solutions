import numpy as np

def standard_errors(samples):
    """
    Returns: dict with 'standard_errors' (list of floats) and 'comparison'.
    """
    standard_errors=[]

    for s in samples:

        arr=np.array(s,dtype=float)

        se = float(np.std(arr, ddof=1) / len(arr)**0.5)

        standard_errors.append(round(se, 4))

    mean_standard_error=round(float(np.mean(standard_errors)),4)
    
    return {"standard_errors": standard_errors, "mean_se": mean_standard_error}


        