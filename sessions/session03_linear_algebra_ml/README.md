# Session 3 — Linear Algebra for Machine Learning

**Session learning outcomes**:
- Formulate linear regression as a linear-algebra problem
- Derive normal equations and relate to least squares
- Understand image as matrices, basic filtering (convolution) as linear ops

## Notebooks (with short descriptions)
- `01_linear_regression_math.ipynb` — Derive closed-form OLS, normal equations, pseudoinverse.
- `02_regularization_ridge_lasso.ipynb` — Tikhonov regularization, bias-variance intuition (math-first).
- `03_image_as_matrix_and_filters.ipynb` — Image representations, convolution as Toeplitz matrix, simple filters.

## Exercises
- `regression_problems.md` — Derive OLS for small datasets, compute pseudoinverse, compare with sklearn.
- `image_lab.ipynb` — Apply smoothing and edge detection using matrix operations; implement convolution by matrix multiplication.

## Mini-project
- `regression_from_scratch.ipynb` — Train linear regression on a toy dataset using normal equations and gradient descent; include diagnostics (residuals, R^2).

## Suggested reading
- Hastie, Tibshirani ch.3 (regression basics)
