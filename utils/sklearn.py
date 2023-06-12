# make up a dataset
from sklearn.datasets import make_moons, make_blobs
#impor random 

def get_moons(seed):
    #random.seed(seed)
    X, y = make_moons(n_samples=100, noise=0.1)

    return X, y

