import numpy as np
from student_impl import pca

def test_shape():
    X=np.random.randn(50,3)
    Z=pca(X,2)
    assert Z.shape==(50,2)
