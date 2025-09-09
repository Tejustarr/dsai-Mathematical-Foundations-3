
# Lecture Notes — Session 2: Linear Transformations

## 1. Basic matrix transformations in R^2
- **Scaling:** $S = \begin{bmatrix}s_x & 0 \\ 0 & s_y\end{bmatrix}$
- **Rotation:** $R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix}$
- **Reflection:** across x-axis $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$, y-axis $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$
- **Shear:** $\begin{bmatrix}1 & k \\ 0 & 1\end{bmatrix}$

All these are special cases of linear transformations $T(x) = Ax$.

## 2. Determinant
For a square matrix $A$, det(A) is:
- Signed volume scaling factor of the linear map
- det=0 => not invertible
- det<0 => orientation reversed

**Properties:**
- det(AB) = det(A)det(B)
- det(A^T)=det(A)
- det(cA)=c^n det(A) for n×n
- det(I)=1
- det of triangular = product of diagonal entries

## 3. Inverse
A^-1 exists iff det(A)≠0.
Defined by: $A^{-1} A = I$.

**Formula for 2x2:**
$A = \begin{bmatrix}a&b\\c&d\end{bmatrix},\ A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$.

## 4. Special matrices
- Diagonal: easy det (product of diag), inverse is reciprocal diag entries
- Triangular: det = product of diagonal entries
- Orthogonal: Q^T Q = I, det=±1, inverse = transpose

## 5. Gram-Schmidt Process
Given independent set {v1,...,vk}, construct orthonormal basis:
u1 = v1/||v1||
u2 = (v2 - proj_u1(v2))/||...||
General: subtract projections onto earlier u's, normalize.

Result: orthonormal basis spanning same subspace.
Matrix form: A=QR decomposition.

## 6. Eigenvalues and Eigenvectors
Definition: For square A, nonzero v is eigenvector with eigenvalue λ if Av=λv.

Solve det(A-λI)=0 for λ (characteristic polynomial).
Then solve (A-λI)v=0 for eigenvectors.

## 7. Eigenbasis and diagonalization
If A has n independent eigenvectors (n×n matrix), can form V=[v1...vn], diagonalize:
A = V Λ V^-1, where Λ=diag(λ1,...,λn).

Geometric meaning: transformation scales eigenvectors by λi.

Applications: differential equations, PCA, spectral clustering.