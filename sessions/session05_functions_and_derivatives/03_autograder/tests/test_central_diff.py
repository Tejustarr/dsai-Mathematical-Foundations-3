import numpy as np
from student_impl import central_difference

def test_simple():
    f = lambda a,b: a**2 * np.sin(b)
    val = central_difference(f, [0.7,0.3], 0)
    # expected approx derivative w.r.t a
    expected = 2*0.7*np.sin(0.3)
    assert abs(val - expected) < 1e-5
