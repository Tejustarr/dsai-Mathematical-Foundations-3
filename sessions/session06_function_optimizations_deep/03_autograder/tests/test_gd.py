import numpy as np
from student_impl import gradient_descent

def test_quadratic():
    f=lambda v:(v[0]-1)**2+(v[1]+2)**2
    g=lambda v: np.array([2*(v[0]-1),2*(v[1]+2)])
    traj=gradient_descent(f,g,np.array([0.,0.]),0.1,100)
    assert np.allclose(traj[-1],[1,-2],atol=1e-2)
