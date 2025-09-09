import numpy as np
from numpy.testing import assert_allclose
from student_impl import is_orthogonal

def test_identity():
    I=np.eye(3)
    assert is_orthogonal(I)

def test_rotation():
    Q=np.array([[0,-1],[1,0]])
    assert is_orthogonal(Q)
