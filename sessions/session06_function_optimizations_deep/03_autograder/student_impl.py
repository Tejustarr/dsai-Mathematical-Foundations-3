import numpy as np

def gradient_descent(f,grad,x0,alpha,iters):
    x=x0.copy(); hist=[x]
    for _ in range(iters):
        x=x-alpha*grad(x)
        hist.append(x.copy())
    return hist
