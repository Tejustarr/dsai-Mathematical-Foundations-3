
# Lecture Notes — Session 3: Linear Algebra for Machine Learning

## 1. Linear Regression Overview
Goal: Given dataset {(x_i, y_i)}, find weights w to minimize sum of squared errors.

Formulate as:
- X ∈ R^{m×n}: design matrix (rows are samples)
- y ∈ R^m: target vector
- Problem: minimize ||Xw - y||_2^2

## 2. Normal Equations
Set gradient = 0:
2 X^T (Xw - y) = 0
→ X^T X w = X^T y
→ Solution: ŵ = (X^T X)^{-1} X^T y

## 3. Example
Data: x=[1,2,3], y=[2,2.5,3.5].
Design matrix: X = [[1,1],[1,2],[1,3]]
Solve for w (intercept, slope).

## 4. Image basics
- Digital image = matrix of pixel intensities.
- Grayscale: single matrix.
- RGB: three matrices stacked.

## 5. Image as linear algebra
- Vectorization: flatten image into long vector.
- Linear transformations = apply matrix to pixel vector.
- Filtering (convolution) = multiplication by Toeplitz-like matrix.

## 6. Example: Filters
- Blur: average neighbors
- Edge detection: Sobel or Laplacian kernels