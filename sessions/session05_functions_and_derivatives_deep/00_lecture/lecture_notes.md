<!-- Math rendered using GitHub Markdown: use ![](https://render.githubusercontent.com/render/math?math=...) and 

![](https://render.githubusercontent.com/render/math?math=...)

 -->


# Lecture Notes — Session 5: Functions & Derivatives (Deep)

## 1. What is a function?
A **function** ![](https://render.githubusercontent.com/render/math?math=f%3A+%5Cmathcal%7BD%7D+%5Csubseteq+%5Cmathbb%7BR%7D%5En+%5Cto+%5Cmathbb%7BR%7D%5Em) maps each input ![](https://render.githubusercontent.com/render/math?math=x%5Cin%5Cmathcal%7BD%7D) to a unique output ![](https://render.githubusercontent.com/render/math?math=y%3Df%28x%29%5Cin%5Cmathbb%7BR%7D%5Em).
- Domain ![](https://render.githubusercontent.com/render/math?math=%5Cmathcal%7BD%7D), codomain ![](https://render.githubusercontent.com/render/math?math=%5Cmathbb%7BR%7D%5Em), image/range ![](https://render.githubusercontent.com/render/math?math=f%28%5Cmathcal%7BD%7D%29).
- Representation: explicit ![](https://render.githubusercontent.com/render/math?math=y%3Df%28x%29), implicit ![](https://render.githubusercontent.com/render/math?math=g%28x%2Cy%29%3D0), parametric ![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Br%7D%28t%29).

### 1.1 Examples
- Linear: ![](https://render.githubusercontent.com/render/math?math=f%28x%29%3Dax%2Bb) (single variable), ![](https://render.githubusercontent.com/render/math?math=f%28x%29%3DA+x+%2B+b) (multivariate)
- Non-linear: ![](https://render.githubusercontent.com/render/math?math=f%28x%29%3D%5Csin+x), ![](https://render.githubusercontent.com/render/math?math=f%28x%29%3Dx%5E3), ![](https://render.githubusercontent.com/render/math?math=f%28x%29%3D%5Cexp%28x%29)
- Piecewise, absolute value, ReLU, saturation functions in ML

## 2. Single-variable differentiation
For ![](https://render.githubusercontent.com/render/math?math=f%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D),


![](https://render.githubusercontent.com/render/math?math=f%27%28x%29%3D%5Clim_%7Bh%5Cto+0%7D%5Cfrac%7Bf%28x%2Bh%29-f%28x%29%7D%7Bh%7D)


**Rules**:
- Constant rule: ![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdx%7D+c+%3D+0)
- Power rule: ![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdx%7D+x%5En+%3D+n+x%5E%7Bn-1%7D)
- Sum rule: ![](https://render.githubusercontent.com/render/math?math=%28f%2Bg%29%27%3Df%27%2Bg%27)
- Product rule: ![](https://render.githubusercontent.com/render/math?math=%28fg%29%27%3Df%27g%2Bfg%27)
- Quotient rule: ![](https://render.githubusercontent.com/render/math?math=%5Cleft%28%5Cfrac%7Bf%7D%7Bg%7D%5Cright%29%27%3D%5Cfrac%7Bf%27g-fg%27%7D%7Bg%5E2%7D)
- Chain rule: ![](https://render.githubusercontent.com/render/math?math=%28f%5Ccirc+g%29%27%28x%29+%3D+f%27%28g%28x%29%29+g%27%28x%29)

**Higher derivatives:** ![](https://render.githubusercontent.com/render/math?math=f%27%27%28x%29%2C+f%5E%7B%28k%29%7D%28x%29).

**Taylor series (local approximation):**


![](https://render.githubusercontent.com/render/math?math=f%28x%2Bh%29+%3D+%5Csum_%7Bk%3D0%7D%5En+%5Cfrac%7Bf%5E%7B%28k%29%7D%28x%29%7D%7Bk%21%7D+h%5Ek+%2B+R_n%28h%29)


Where ![](https://render.githubusercontent.com/render/math?math=R_n) is the remainder.

## 3. Multivariable differentiation
Let ![](https://render.githubusercontent.com/render/math?math=f%3A%5Cmathbb%7BR%7D%5En%5Cto%5Cmathbb%7BR%7D). The partial derivative wrt ![](https://render.githubusercontent.com/render/math?math=x_i) is:


![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%5Cpartial+f%7D%7B%5Cpartial+x_i%7D%28x%29+%3D+%5Clim_%7Bh%5Cto0%7D+%5Cfrac%7Bf%28x_1%2C%5Cdots%2Cx_i%2Bh%2C%5Cdots%2Cx_n%29-f%28x%29%7D%7Bh%7D)


**Gradient**: ![](https://render.githubusercontent.com/render/math?math=%5Cnabla+f%28x%29+%3D+%5Cbegin%7Bbmatrix%7D%5Cpartial+f%2F%5Cpartial+x_1+%5C%5C+%5Cvdots+%5C%5C+%5Cpartial+f%2F%5Cpartial+x_n%5Cend%7Bbmatrix%7D), points in direction of steepest ascent.

**Directional derivative** in direction ![](https://render.githubusercontent.com/render/math?math=u):


![](https://render.githubusercontent.com/render/math?math=D_u+f%28x%29+%3D+%5Cnabla+f%28x%29%5Ccdot+u)


if f is differentiable.

**Total derivative / Differentiability:** f is differentiable at x if there exists linear map (Jacobian) J such that:


![](https://render.githubusercontent.com/render/math?math=f%28x%2Bh%29+%3D+f%28x%29+%2B+J%28x%29+h+%2B+o%28%5C%7Ch%5C%7C%29)



## 4. Vector-valued functions & Jacobian
For ![](https://render.githubusercontent.com/render/math?math=F%3A%5Cmathbb%7BR%7D%5En%5Cto%5Cmathbb%7BR%7D%5Em), the **Jacobian** is ![](https://render.githubusercontent.com/render/math?math=m%5Ctimes+n) matrix:


![](https://render.githubusercontent.com/render/math?math=J_%7Bij%7D+%3D+%5Cfrac%7B%5Cpartial+F_i%7D%7B%5Cpartial+x_j%7D)


Jacobian generalizes gradient and linear approximation: ![](https://render.githubusercontent.com/render/math?math=F%28x%2Bh%29%5Capprox+F%28x%29%2BJ%28x%29h).

## 5. Hessian & second derivatives
For scalar ![](https://render.githubusercontent.com/render/math?math=f%3A%5Cmathbb%7BR%7D%5En%5Cto%5Cmathbb%7BR%7D), Hessian ![](https://render.githubusercontent.com/render/math?math=H) is ![](https://render.githubusercontent.com/render/math?math=n%5Ctimes+n) symmetric matrix of second partials:


![](https://render.githubusercontent.com/render/math?math=H_%7Bij%7D+%3D+%5Cfrac%7B%5Cpartial%5E2+f%7D%7B%5Cpartial+x_i+%5Cpartial+x_j%7D)


Quadratic form ![](https://render.githubusercontent.com/render/math?math=h%5ET+H+h) indicates curvature. If ![](https://render.githubusercontent.com/render/math?math=H) positive definite at a critical point, it's a local minimum.

## 6. Rules for multivariable derivatives
- Linear functions: gradient is constant (∇(Ax+b)=A^T)
- Chain rule (vector form): if ![](https://render.githubusercontent.com/render/math?math=F%3A+%5Cmathbb%7BR%7D%5En%5Cto%5Cmathbb%7BR%7D%5Em) and ![](https://render.githubusercontent.com/render/math?math=G%3A%5Cmathbb%7BR%7D%5Em%5Cto%5Cmathbb%7BR%7D%5Ep), then ![](https://render.githubusercontent.com/render/math?math=D%28G%5Ccirc+F%29%28x%29%3DD+G%28F%28x%29%29+%5Ccdot+D+F%28x%29) (matrix product).

## 7. Implicit differentiation
Given ![](https://render.githubusercontent.com/render/math?math=g%28x%2Cy%29%3D0) and y = y(x), then


![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bdy%7D%7Bdx%7D+%3D+-%5Cfrac%7B%5Cpartial+g%2F%5Cpartial+x%7D%7B%5Cpartial+g%2F%5Cpartial+y%7D)


assuming denominator ≠ 0.

## 8. Numerical differentiation & gradient checking
Finite differences:
- Forward: ![](https://render.githubusercontent.com/render/math?math=f%27%28x%29%5Capprox+%28f%28x%2Bh%29-f%28x%29%29%2Fh)
- Backward: ![](https://render.githubusercontent.com/render/math?math=%28f%28x%29-f%28x-h%29%29%2Fh)
- Central: ![](https://render.githubusercontent.com/render/math?math=%28f%28x%2Bh%29-f%28x-h%29%29%2F%282h%29) — O(h^2) accuracy.

**Gradient checking:** compare analytic gradient with numerical central difference to validate implementations.

## 9. Integration (brief)
Indefinite integral ![](https://render.githubusercontent.com/render/math?math=F%28x%29%3D%5Cint+f%28x%29+dx); definite integral ![](https://render.githubusercontent.com/render/math?math=%5Cint_a%5Eb+f%28x%29+dx).
Fundamental theorem: if F'=f then ![](https://render.githubusercontent.com/render/math?math=%5Cint_a%5Eb+f%28x%29dx+%3D+F%28b%29-F%28a%29).
Multivariate integrals: double integrals, change of variables (Jacobian determinant).

---

## Appendix: Common derivative formulas (cheat sheet)
- ![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdx%7D+%5Csin+x+%3D+%5Ccos+x)
- ![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdx%7D+%5Ccos+x+%3D+-%5Csin+x)
- ![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdx%7D+e%5Ex+%3D+e%5Ex)
- ![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdx%7D+%5Cln+x+%3D+1%2Fx)
- ![](https://render.githubusercontent.com/render/math?math=%5Cnabla+%28x%5ET+A+x%29+%3D+%28A+%2B+A%5ET%29+x)  (useful for quadratic forms)