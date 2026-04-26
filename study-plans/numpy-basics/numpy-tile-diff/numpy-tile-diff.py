import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""

    pad = lambda x: np.pad(x,((0,1),(0,0)),mode='constant',constant_values=0)
    arr=np.array(data,dtype=np.float64)

    tile_arr=np.tile(arr,(reps,1))

    dif_arr=np.diff(tile_arr,axis=0)

    padded=pad(dif_arr)

    return np.stack([
        tile_arr,
        padded
    ])
    