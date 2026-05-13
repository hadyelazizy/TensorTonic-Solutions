import numpy as np
from scipy import stats

def anova_f_test(groups):
    """
    Returns: [f_stat, df_between, df_within, p_value, reject] as a list.
    """
    all_data=[x for g in groups for x in g]

    
    
    k=len(groups)

    n=len(all_data)

    grande_mean=np.mean(all_data)

    df_between=k-1
    df_within=n-k

    ssb=0

    means=[float(np.mean(g)) for g in groups]

    
    
    for i in range(k):

        ssb+=((means[i]-grande_mean)**2)*len(groups[i])
        
    
    ssw=sum(sum((g-np.mean(g))**2) for g in groups)
        
    f=round((ssb/df_between)/(ssw/df_within),4)
    p = round(float(stats.f.sf(f, df_between, df_within)), 4)
    
    return [f, df_between, df_within, p, p < 0.05]

    