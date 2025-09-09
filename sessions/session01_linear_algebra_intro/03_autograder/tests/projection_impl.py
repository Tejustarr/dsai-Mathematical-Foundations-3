import numpy as np

def projection(u, v):
    v = v.astype(float)
    return (v.dot(u) / v.dot(v)) * v
