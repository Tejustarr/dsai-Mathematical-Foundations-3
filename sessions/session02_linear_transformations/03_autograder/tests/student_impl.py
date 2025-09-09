import numpy as np
def is_orthogonal(Q,tol=1e-8):
    return np.allclose(Q.T@Q, np.eye(Q.shape[0]), atol=tol)
