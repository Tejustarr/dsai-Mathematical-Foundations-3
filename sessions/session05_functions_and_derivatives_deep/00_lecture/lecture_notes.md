
# Lecture Notes — Session 5: Functions & Derivatives (Deep)

## 1. What is a function?
A **function** $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^m$ maps each input $x\in\mathcal{D}$ to a unique output $y=f(x)\in\mathbb{R}^m$.
- Domain $\mathcal{D}$, codomain $\mathbb{R}^m$, image/range $f(\mathcal{D})$.
- Representation: explicit $y=f(x)$, implicit $g(x,y)=0$, parametric $\mathbf{r}(t)$.

### 1.1 Examples
- Linear: $f(x)=ax+b$ (single variable), $f(x)=A x + b$ (multivariate)
- Non-linear: $f(x)=\sin x$, $f(x)=x^3$, $f(x)=\exp(x)$
- Piecewise, absolute value, ReLU, saturation functions in ML

## 2. Single-variable differentiation
For $f:\mathbb{R}\to\mathbb{R}$,
$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$
**Rules**:
- Constant rule: $\frac{d}{dx} c = 0$
- Power rule: $\frac{d}{dx} x^n = n x^{n-1}$
- Sum rule: $(f+g)'=f'+g'$
- Product rule: $(fg)'=f'g+fg'$
- Quotient rule: $\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}$
- Chain rule: $(f\circ g)'(x) = f'(g(x)) g'(x)$

**Higher derivatives:** $f''(x), f^{(k)}(x)$.

**Taylor series (local approximation):**
$$
f(x+h) = \sum_{k=0}^n \frac{f^{(k)}(x)}{k!} h^k + R_n(h)
$$
Where $R_n$ is the remainder.

## 3. Multivariable differentiation
Let $f:\mathbb{R}^n\to\mathbb{R}$. The partial derivative wrt $x_i$ is:
$$
\frac{\partial f}{\partial x_i}(x) = \lim_{h\to0} \frac{f(x_1,\dots,x_i+h,\dots,x_n)-f(x)}{h}
$$
**Gradient**: $\nabla f(x) = \begin{bmatrix}\partial f/\partial x_1 \\ \vdots \\ \partial f/\partial x_n\end{bmatrix}$, points in direction of steepest ascent.

**Directional derivative** in direction $u$:
$$
D_u f(x) = \nabla f(x)\cdot u
$$
if f is differentiable.

**Total derivative / Differentiability:** f is differentiable at x if there exists linear map (Jacobian) J such that:
$$
f(x+h) = f(x) + J(x) h + o(\|h\|)
$$

## 4. Vector-valued functions & Jacobian
For $F:\mathbb{R}^n\to\mathbb{R}^m$, the **Jacobian** is $m\times n$ matrix:
$$
J_{ij} = \frac{\partial F_i}{\partial x_j}
$$
Jacobian generalizes gradient and linear approximation: $F(x+h)\approx F(x)+J(x)h$.

## 5. Hessian & second derivatives
For scalar $f:\mathbb{R}^n\to\mathbb{R}$, Hessian $H$ is $n\times n$ symmetric matrix of second partials:
$$
H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}
$$
Quadratic form $h^T H h$ indicates curvature. If $H$ positive definite at a critical point, it's a local minimum.

## 6. Rules for multivariable derivatives
- Linear functions: gradient is constant (∇(Ax+b)=A^T)
- Chain rule (vector form): if $F: \mathbb{R}^n\to\mathbb{R}^m$ and $G:\mathbb{R}^m\to\mathbb{R}^p$, then $D(G\circ F)(x)=D G(F(x)) \cdot D F(x)$ (matrix product).

## 7. Implicit differentiation
Given $g(x,y)=0$ and y = y(x), then
$$
\frac{dy}{dx} = -\frac{\partial g/\partial x}{\partial g/\partial y}
$$
assuming denominator ≠ 0.

## 8. Numerical differentiation & gradient checking
Finite differences:
- Forward: $f'(x)\approx (f(x+h)-f(x))/h$
- Backward: $(f(x)-f(x-h))/h$
- Central: $(f(x+h)-f(x-h))/(2h)$ — O(h^2) accuracy.

**Gradient checking:** compare analytic gradient with numerical central difference to validate implementations.

## 9. Integration (brief)
Indefinite integral $F(x)=\int f(x) dx$; definite integral $\int_a^b f(x) dx$.
Fundamental theorem: if F'=f then $\int_a^b f(x)dx = F(b)-F(a)$.
Multivariate integrals: double integrals, change of variables (Jacobian determinant).

---

## Appendix: Common derivative formulas (cheat sheet)
- $\frac{d}{dx} \sin x = \cos x$
- $\frac{d}{dx} \cos x = -\sin x$
- $\frac{d}{dx} e^x = e^x$
- $\frac{d}{dx} \ln x = 1/x$
- $\nabla (x^T A x) = (A + A^T) x$  (useful for quadratic forms)