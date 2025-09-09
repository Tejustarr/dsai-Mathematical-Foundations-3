
# Lecture Notes — Session 6: Function Optimizations

## 1. Optimization basics
Optimization = find x* that minimizes f(x) over domain.

Critical points: ∇f(x)=0. Classify using Hessian:
- Positive definite ⇒ local min
- Negative definite ⇒ local max
- Indefinite ⇒ saddle point

Global vs local optima.

Convex functions: any local min = global min. Conditions: f(θx+(1-θ)y) ≤ θf(x)+(1-θ)f(y).

## 2. First-order methods
Rely on gradient info.

- Gradient descent: x_{k+1} = x_k - α ∇f(x_k)
- Convergence depends on step size α, Lipschitz continuity.

## 3. Gradient Descent
For quadratic f(x)=1/2 x^T Q x - b^T x,
update: x_{k+1}=x_k - α(Qx_k-b).
Convergence if 0<α<2/λ_max(Q).

Variants: batch GD (all data), mini-batch GD, momentum, adaptive methods.

## 4. Stochastic Gradient Descent (SGD)
Use gradient on random sample (or minibatch).
Update: w_{k+1} = w_k - α ∇ℓ_i(w_k).
Stochastic noise helps escape saddles.
Convergence slower but scalable to big data.

Learning rate schedules: constant, decreasing, adaptive.

## 5. Applications
- Linear regression optimization
- Logistic regression
- Neural network training