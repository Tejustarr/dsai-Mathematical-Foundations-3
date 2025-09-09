import numpy as np

def central_difference(f, x, i, h=1e-6):
    x = np.array(x, dtype=float)
    e = np.zeros_like(x); e[i]=h
    return (f(*(x+e)) - f(*(x-e))) / (2*h)
