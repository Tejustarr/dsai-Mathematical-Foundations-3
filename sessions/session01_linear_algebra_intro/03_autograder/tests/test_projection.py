import numpy as np
from numpy.testing import assert_allclose

from projection_impl import projection

def test_proj_basic():
    u = np.array([3.,4.])
    v = np.array([1.,0.])
    p = projection(u,v)
    assert_allclose(p, np.array([3.,0.]))

def test_proj_orthogonal():
    u = np.array([1.,2.])
    v = np.array([2.,-1.])
    p = projection(u,v)
    # p should be collinear with v
    ratio = p[0]/v[0] if v[0]!=0 else p[1]/v[1]
    assert_allclose(p, ratio * v)
