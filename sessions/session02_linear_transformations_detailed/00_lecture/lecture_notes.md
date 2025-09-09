<!-- Math rendered using GitHub Markdown: use ![](https://render.githubusercontent.com/render/math?math=...) and 

![](https://render.githubusercontent.com/render/math?math=...)

 -->


# Lecture Notes — Session 2: Linear Transformations

## 1. Basic matrix transformations in R^2
- **Scaling:** ![](https://render.githubusercontent.com/render/math?math=S+%3D+%5Cbegin%7Bbmatrix%7Ds_x+%26+0+%5C%5C+0+%26+s_y%5Cend%7Bbmatrix%7D)
- **Rotation:** ![](https://render.githubusercontent.com/render/math?math=R%28%5Ctheta%29+%3D+%5Cbegin%7Bbmatrix%7D%5Ccos%5Ctheta+%26+-%5Csin%5Ctheta+%5C%5C+%5Csin%5Ctheta+%26+%5Ccos%5Ctheta%5Cend%7Bbmatrix%7D)
- **Reflection:** across x-axis ![](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Bbmatrix%7D1%260%5C%5C0%26-1%5Cend%7Bbmatrix%7D), y-axis ![](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Bbmatrix%7D-1%260%5C%5C0%261%5Cend%7Bbmatrix%7D)
- **Shear:** ![](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Bbmatrix%7D1+%26+k+%5C%5C+0+%26+1%5Cend%7Bbmatrix%7D)

All these are special cases of linear transformations ![](https://render.githubusercontent.com/render/math?math=T%28x%29+%3D+Ax).

## 2. Determinant
For a square matrix ![](https://render.githubusercontent.com/render/math?math=A), det(A) is:
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
Defined by: ![](https://render.githubusercontent.com/render/math?math=A%5E%7B-1%7D+A+%3D+I).

**Formula for 2x2:**
![](https://render.githubusercontent.com/render/math?math=A+%3D+%5Cbegin%7Bbmatrix%7Da%26b%5C%5Cc%26d%5Cend%7Bbmatrix%7D%2C%5C+A%5E%7B-1%7D+%3D+%5Cfrac%7B1%7D%7Bad-bc%7D%5Cbegin%7Bbmatrix%7Dd%26-b%5C%5C-c%26a%5Cend%7Bbmatrix%7D).

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