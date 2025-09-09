<!-- Math rendered using GitHub Markdown: use $...$ and $$...$$ -->


# Lecture Notes — Session 1: Introduction to Linear Algebra

## 1. What is Linear Algebra?
Linear algebra studies vectors, vector spaces, linear maps (matrices), and systems of linear equations. It provides language and tools for representing, manipulating, and reasoning about linear relationships. In data science and ML, linear algebra underpins:
- Data representation (vectors, matrices)
- Transformations (feature engineering, convolutions)
- Learning algorithms (linear regression, PCA, SVD)
- Optimization (gradient computations live in vector spaces)

## 2. Vector — definition and notation
A **vector** is an ordered list of numbers. We denote vectors with boldface or an arrow: **v** or $\vec{v}$.
In coordinates: $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$.

### 2.1 Vector operations (component-wise)
- **Addition:** $\mathbf{u} + \mathbf{v} = [u_1+v_1, \dots, u_n+v_n]^T$.
- **Scalar multiplication:** $c\mathbf{v} = [cv_1, \dots, cv_n]^T$.
- **Linear combination:** $a\mathbf{u} + b\mathbf{v}$.

### 2.2 Inner product (dot product)
For $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$:
$$
\mathbf{u}\cdot\mathbf{v} = \sum_{i=1}^n u_i v_i = \mathbf{u}^T\mathbf{v}.
$$
**Properties:** bilinear, symmetric, positive-definite (if not zero vector).

### 2.3 Norms
The (Euclidean) norm:
$$
\|\mathbf{v}\|_2 = \sqrt{\mathbf{v}^T\mathbf{v}} = \sqrt{\sum_i v_i^2}.
$$
Other norms: $L_1$ (sum of absolute values), $L_\infty$ (max absolute).

### 2.4 Angle and orthogonality
Cosine angle:
$$
\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}.
$$
Orthogonal iff $\mathbf{u}\cdot\mathbf{v}=0$.

## 3. Vector spaces, span, and linear independence
A set $V$ is a **vector space** over $\mathbb{R}$ if closed under addition & scalar multiplication.

**Span:** Given vectors $v_1,\dots,v_k$, their span is
$\text{span}\{v_1,\dots,v_k\} = \{a_1 v_1 + \dots + a_k v_k : a_i\in\mathbb{R}\}$.

**Linear independence:** $v_1,\dots,v_k$ are independent if
$\sum_i a_i v_i = 0 \Rightarrow a_i = 0\ \forall i$.

**Basis:** A linearly independent set that spans a vector space. The number of basis vectors = **dimension**.

### Example
In $\mathbb{R}^2$, vectors $[1,0]^T$ and $[0,1]^T$ form the standard basis.

## 4. Change of basis (vectors)
If $B = \{b_1,\dots,b_n\}$ is a basis, every vector $x$ has coordinates $[x]_B$ such that:
$$
x = B [x]_B, \quad \text{where } B = [b_1\ b_2\ \dots\ b_n] \in \mathbb{R}^{n\times n}.
$$
If $P$ is the change-of-basis matrix from basis $B$ to standard basis, then $x = P[x]_B$. To convert coordinates between bases:
$$
[x]_{B'} = P_{B'}^{-1} P_B [x]_B.
$$

## 5. Matrices — introduction
A matrix $A\in\mathbb{R}^{m\times n}$ represents a linear map $A: \mathbb{R}^n\to\mathbb{R}^m$.
Action on vector: $y = A x$.

**Matrix operations**
- **Addition, scalar multiplication**
- **Matrix multiplication:** $(AB)_{ij} = \sum_k A_{ik}B_{kj}$
- **Transpose:** $A^T$
- **Identity:** $I_n$ such that $I_n x = x$
- **Inverse:** $A^{-1}$ s.t. $A^{-1}A = I$ (only for square invertible matrices)

## 6. Types of matrices (common)
- **Square matrix:** $n\times n$
- **Diagonal matrix:** non-zero only on diagonal
- **Symmetric:** $A^T = A$
- **Orthogonal:** $Q^T Q = I$ (columns orthonormal)
- **Triangular (upper/lower)**
- **Permutation matrix**
- **Sparse matrices** (many zeros)

## 7. Solving linear systems
System $A x = b$. Methods:
- Direct: Gaussian elimination, LU decomposition.
- For least squares (overdetermined): normal equations $A^T A x = A^T b$ or use QR/pseudoinverse.

## 8. Geometric intuition & applications
- Rotations, scalings, shears as matrices in $\mathbb{R}^2$ or $\mathbb{R}^3$.
- Data as vectors (features) and matrices (datasets, images).
- PCA, SVD, linear regression, kernels — all use linear algebra.

---

## Appendix: Quick reference of formulas

- Dot product: $\mathbf{u}\cdot\mathbf{v} = \mathbf{u}^T \mathbf{v}$
- Norm: $\|\mathbf{v}\|_2 = \sqrt{\mathbf{v}^T\mathbf{v}}$
- Projection of $x$ onto $u$: $\text{proj}_u(x) = \frac{u^T x}{u^T u} u$
- Projection onto subspace spanned by columns of $A$: $P = A(A^T A)^{-1} A^T$ (when columns independent)
- Least squares solution: $\hat x = (A^T A)^{-1} A^T b$ (normal equations)