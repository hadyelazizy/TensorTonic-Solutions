from scipy import stats

def sampling_distribution(mu, sigma, n, threshold):
    """
    Returns: dict with 'mean', 'std_error', 'tail_probability' as floats.
    """
    mean_sample=round(mu,4)

    std_error=round(sigma/n**0.5,4)

    prob_below = round(float(stats.norm.cdf(threshold, mu, sigma / n**0.5)), 4)
    
    return {"sampling_mean": mean_sample, "sampling_std": std_error, "prob_below_threshold": prob_below}

