<!-- Math rendered using GitHub Markdown: use $...$ and $$...$$ -->


# Lecture Notes — Session 4: Applications of Linear Algebra

## 1. Covariance Matrix
Given data X ∈ R^{m×n}, with m samples, n features.
- Center data: X_c = X - mean(X, axis=0)
- Covariance: Σ = (1/(m-1)) X_c^T X_c

Properties:
- Σ is symmetric, positive semidefinite
- Diagonal entries = variances of features
- Off-diagonal = covariances

## 2. PCA
Goal: reduce dimensionality while preserving variance.
Steps:
1. Center data.
2. Compute covariance Σ.
3. Eigen-decomposition Σ = VΛV^T.
4. Choose top k eigenvectors (principal components).
5. Project data: Z = X_c V_k.

Variance explained ratio = λ_k / sum λ_i.

## 3. Singular Value Decomposition
For any m×n matrix X:
X = U Σ V^T
- U ∈ R^{m×m}, V ∈ R^{n×n} orthogonal
- Σ diagonal with singular values (nonnegative)

Connections:
- Eigen-decomposition of X^T X: V eigenvectors, singular values = sqrt(eigenvalues)
- PCA can be implemented via SVD

## 4. Image Compression
- Represent image as matrix (grayscale) or 3 matrices (RGB).
- Apply SVD: A ≈ U_k Σ_k V_k^T with k < rank.
- Store only top k singular values/vectors.
- Compression ratio ~ (k(m+n))/(mn).
- Reconstruction error relates to discarded singular values.

Applications: storage reduction, noise reduction, latent semantic analysis.