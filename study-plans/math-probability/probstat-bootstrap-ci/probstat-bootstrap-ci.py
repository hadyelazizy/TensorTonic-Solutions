import numpy as np

def bootstrap_ci(data, n_bootstraps, confidence, seed):
    """
    Returns: [mean, ci_lower, ci_upper] as a list.
    """
    rng = np.random.RandomState(seed)
    arr = np.array(data, dtype=float)
    boot_means = []
    for _ in range(n_bootstraps):
        sample = rng.choice(arr, size=len(arr), replace=True)
        boot_means.append(float(np.mean(sample)))
    boot_means = sorted(boot_means)
    alpha = 1 - confidence
    lower_idx = int(np.floor(alpha / 2 * n_bootstraps))
    upper_idx = int(np.floor((1 - alpha / 2) * n_bootstraps)) - 1
    return [round(float(np.mean(boot_means)), 4),
            round(boot_means[lower_idx], 4),
            round(boot_means[upper_idx], 4)]
