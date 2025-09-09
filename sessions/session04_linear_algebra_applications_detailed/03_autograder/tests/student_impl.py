import numpy as np

def pca(X,k):
    Xc = X - X.mean(0)
    U,S,Vt = np.linalg.svd(Xc,full_matrices=False)
    return Xc@Vt[:k].T
