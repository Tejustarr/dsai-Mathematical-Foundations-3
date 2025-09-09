import numpy as np
from student_impl import fit

def test_regression():
    X=np.array([[1,1],[1,2],[1,3]])
    y=np.array([2,2.5,3.5])
    w=fit(X,y)
    assert np.allclose(w,[1.5,0.5])
