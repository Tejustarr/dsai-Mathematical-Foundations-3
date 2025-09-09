import numpy as np

def fit(X,y):
    return np.linalg.inv(X.T@X)@X.T@y
