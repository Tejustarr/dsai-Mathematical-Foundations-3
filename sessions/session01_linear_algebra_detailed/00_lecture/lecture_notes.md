<!-- Math rendered using GitHub Markdown: use ![](https://render.githubusercontent.com/render/math?math=...) and 

![](https://render.githubusercontent.com/render/math?math=...)

 -->


# Lecture Notes — Session 1: Introduction to Linear Algebra

## 1. What is Linear Algebra?
Linear algebra studies vectors, vector spaces, linear maps (matrices), and systems of linear equations. It provides language and tools for representing, manipulating, and reasoning about linear relationships. In data science and ML, linear algebra underpins:
- Data representation (vectors, matrices)
- Transformations (feature engineering, convolutions)
- Learning algorithms (linear regression, PCA, SVD)
- Optimization (gradient computations live in vector spaces)

## 2. Vector — definition and notation
A **vector** is an ordered list of numbers. We denote vectors with boldface or an arrow: **v** or ![](https://render.githubusercontent.com/render/math?math=%5Cvec%7Bv%7D).
In coordinates: ![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Bv%7D+%3D+%5Cbegin%7Bbmatrix%7D+v_1+%5C%5C+v_2+%5C%5C+%5Cvdots+%5C%5C+v_n+%5Cend%7Bbmatrix%7D+%5Cin+%5Cmathbb%7BR%7D%5En).

### 2.1 Vector operations (component-wise)
- **Addition:** ![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Bu%7D+%2B+%5Cmathbf%7Bv%7D+%3D+%5Bu_1%2Bv_1%2C+%5Cdots%2C+u_n%2Bv_n%5D%5ET).
- **Scalar multiplication:** ![](https://render.githubusercontent.com/render/math?math=c%5Cmathbf%7Bv%7D+%3D+%5Bcv_1%2C+%5Cdots%2C+cv_n%5D%5ET).
- **Linear combination:** ![](https://render.githubusercontent.com/render/math?math=a%5Cmathbf%7Bu%7D+%2B+b%5Cmathbf%7Bv%7D).

### 2.2 Inner product (dot product)
For ![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Bu%7D%2C%5Cmathbf%7Bv%7D%5Cin%5Cmathbb%7BR%7D%5En):


![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Bu%7D%5Ccdot%5Cmathbf%7Bv%7D+%3D+%5Csum_%7Bi%3D1%7D%5En+u_i+v_i+%3D+%5Cmathbf%7Bu%7D%5ET%5Cmathbf%7Bv%7D.)


**Properties:** bilinear, symmetric, positive-definite (if not zero vector).

### 2.3 Norms
The (Euclidean) norm:


![](https://render.githubusercontent.com/render/math?math=%5C%7C%5Cmathbf%7Bv%7D%5C%7C_2+%3D+%5Csqrt%7B%5Cmathbf%7Bv%7D%5ET%5Cmathbf%7Bv%7D%7D+%3D+%5Csqrt%7B%5Csum_i+v_i%5E2%7D.)


Other norms: ![](https://render.githubusercontent.com/render/math?math=L_1) (sum of absolute values), ![](https://render.githubusercontent.com/render/math?math=L_%5Cinfty) (max absolute).

### 2.4 Angle and orthogonality
Cosine angle:


![](https://render.githubusercontent.com/render/math?math=%5Ccos%5Ctheta+%3D+%5Cfrac%7B%5Cmathbf%7Bu%7D%5Ccdot%5Cmathbf%7Bv%7D%7D%7B%5C%7C%5Cmathbf%7Bu%7D%5C%7C%5C%7C%5Cmathbf%7Bv%7D%5C%7C%7D.)


Orthogonal iff ![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Bu%7D%5Ccdot%5Cmathbf%7Bv%7D%3D0).

## 3. Vector spaces, span, and linear independence
A set ![](https://render.githubusercontent.com/render/math?math=V) is a **vector space** over ![](https://render.githubusercontent.com/render/math?math=%5Cmathbb%7BR%7D) if closed under addition & scalar multiplication.

**Span:** Given vectors ![](https://render.githubusercontent.com/render/math?math=v_1%2C%5Cdots%2Cv_k), their span is
![](https://render.githubusercontent.com/render/math?math=%5Ctext%7Bspan%7D%5C%7Bv_1%2C%5Cdots%2Cv_k%5C%7D+%3D+%5C%7Ba_1+v_1+%2B+%5Cdots+%2B+a_k+v_k+%3A+a_i%5Cin%5Cmathbb%7BR%7D%5C%7D).

**Linear independence:** ![](https://render.githubusercontent.com/render/math?math=v_1%2C%5Cdots%2Cv_k) are independent if
![](https://render.githubusercontent.com/render/math?math=%5Csum_i+a_i+v_i+%3D+0+%5CRightarrow+a_i+%3D+0%5C+%5Cforall+i).

**Basis:** A linearly independent set that spans a vector space. The number of basis vectors = **dimension**.

### Example
In ![](https://render.githubusercontent.com/render/math?math=%5Cmathbb%7BR%7D%5E2), vectors ![](https://render.githubusercontent.com/render/math?math=%5B1%2C0%5D%5ET) and ![](https://render.githubusercontent.com/render/math?math=%5B0%2C1%5D%5ET) form the standard basis.

## 4. Change of basis (vectors)
If ![](https://render.githubusercontent.com/render/math?math=B+%3D+%5C%7Bb_1%2C%5Cdots%2Cb_n%5C%7D) is a basis, every vector ![](https://render.githubusercontent.com/render/math?math=x) has coordinates ![](https://render.githubusercontent.com/render/math?math=%5Bx%5D_B) such that:


![](https://render.githubusercontent.com/render/math?math=x+%3D+B+%5Bx%5D_B%2C+%5Cquad+%5Ctext%7Bwhere+%7D+B+%3D+%5Bb_1%5C+b_2%5C+%5Cdots%5C+b_n%5D+%5Cin+%5Cmathbb%7BR%7D%5E%7Bn%5Ctimes+n%7D.)


If ![](https://render.githubusercontent.com/render/math?math=P) is the change-of-basis matrix from basis ![](https://render.githubusercontent.com/render/math?math=B) to standard basis, then ![](https://render.githubusercontent.com/render/math?math=x+%3D+P%5Bx%5D_B). To convert coordinates between bases:


![](https://render.githubusercontent.com/render/math?math=%5Bx%5D_%7BB%27%7D+%3D+P_%7BB%27%7D%5E%7B-1%7D+P_B+%5Bx%5D_B.)



## 5. Matrices — introduction
A matrix ![](https://render.githubusercontent.com/render/math?math=A%5Cin%5Cmathbb%7BR%7D%5E%7Bm%5Ctimes+n%7D) represents a linear map ![](https://render.githubusercontent.com/render/math?math=A%3A+%5Cmathbb%7BR%7D%5En%5Cto%5Cmathbb%7BR%7D%5Em).
Action on vector: ![](https://render.githubusercontent.com/render/math?math=y+%3D+A+x).

**Matrix operations**
- **Addition, scalar multiplication**
- **Matrix multiplication:** ![](https://render.githubusercontent.com/render/math?math=%28AB%29_%7Bij%7D+%3D+%5Csum_k+A_%7Bik%7DB_%7Bkj%7D)
- **Transpose:** ![](https://render.githubusercontent.com/render/math?math=A%5ET)
- **Identity:** ![](https://render.githubusercontent.com/render/math?math=I_n) such that ![](https://render.githubusercontent.com/render/math?math=I_n+x+%3D+x)
- **Inverse:** ![](https://render.githubusercontent.com/render/math?math=A%5E%7B-1%7D) s.t. ![](https://render.githubusercontent.com/render/math?math=A%5E%7B-1%7DA+%3D+I) (only for square invertible matrices)

## 6. Types of matrices (common)
- **Square matrix:** ![](https://render.githubusercontent.com/render/math?math=n%5Ctimes+n)
- **Diagonal matrix:** non-zero only on diagonal
- **Symmetric:** ![](https://render.githubusercontent.com/render/math?math=A%5ET+%3D+A)
- **Orthogonal:** ![](https://render.githubusercontent.com/render/math?math=Q%5ET+Q+%3D+I) (columns orthonormal)
- **Triangular (upper/lower)**
- **Permutation matrix**
- **Sparse matrices** (many zeros)

## 7. Solving linear systems
System ![](https://render.githubusercontent.com/render/math?math=A+x+%3D+b). Methods:
- Direct: Gaussian elimination, LU decomposition.
- For least squares (overdetermined): normal equations ![](https://render.githubusercontent.com/render/math?math=A%5ET+A+x+%3D+A%5ET+b) or use QR/pseudoinverse.

## 8. Geometric intuition & applications
- Rotations, scalings, shears as matrices in ![](https://render.githubusercontent.com/render/math?math=%5Cmathbb%7BR%7D%5E2) or ![](https://render.githubusercontent.com/render/math?math=%5Cmathbb%7BR%7D%5E3).
- Data as vectors (features) and matrices (datasets, images).
- PCA, SVD, linear regression, kernels — all use linear algebra.

---

## Appendix: Quick reference of formulas

- Dot product: ![](https://render.githubusercontent.com/render/math?math=%5Cmathbf%7Bu%7D%5Ccdot%5Cmathbf%7Bv%7D+%3D+%5Cmathbf%7Bu%7D%5ET+%5Cmathbf%7Bv%7D)
- Norm: ![](https://render.githubusercontent.com/render/math?math=%5C%7C%5Cmathbf%7Bv%7D%5C%7C_2+%3D+%5Csqrt%7B%5Cmathbf%7Bv%7D%5ET%5Cmathbf%7Bv%7D%7D)
- Projection of ![](https://render.githubusercontent.com/render/math?math=x) onto ![](https://render.githubusercontent.com/render/math?math=u): ![](https://render.githubusercontent.com/render/math?math=%5Ctext%7Bproj%7D_u%28x%29+%3D+%5Cfrac%7Bu%5ET+x%7D%7Bu%5ET+u%7D+u)
- Projection onto subspace spanned by columns of ![](https://render.githubusercontent.com/render/math?math=A): ![](https://render.githubusercontent.com/render/math?math=P+%3D+A%28A%5ET+A%29%5E%7B-1%7D+A%5ET) (when columns independent)
- Least squares solution: ![](https://render.githubusercontent.com/render/math?math=%5Chat+x+%3D+%28A%5ET+A%29%5E%7B-1%7D+A%5ET+b) (normal equations)