from scipy import stats

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, alpha):
    """
    Returns: [p_control, p_treatment, z_stat, p_value, reject] as a list.
    """
    pc=control_conversions/control_visitors
    pt=treatment_conversions/treatment_visitors

    p_hat=(control_conversions+treatment_conversions)/(control_visitors+treatment_visitors)


    se = (p_hat * (1 - p_hat) * (1/control_visitors + 1/treatment_visitors)) ** 0.5

    z=round((pt-pc)/se,4)
    p_val = round(2 * float(stats.norm.sf(abs(z))), 4)
    return [pc, pt, z, p_val, p_val < alpha]
    

    