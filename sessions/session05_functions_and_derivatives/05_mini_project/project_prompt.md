# Mini-Project: Derivatives in Practice — Logistic Regression from First Principles

**Objective**: Derive gradients and Hessians for logistic loss; implement optimization methods and compare.

Parts:
1. Math derivation:
   - Logistic model: p_i = σ(w^T x_i), σ(z)=1/(1+e^{-z})
   - Negative log-likelihood L(w)= - sum_i [ y_i log p_i + (1-y_i) log(1-p_i) ]
   - Derive gradient ∇L(w) and Hessian H(w) analytically.
2. Implementation:
   - Implement functions to compute loss, gradient (analytic), Hessian (analytic).
   - Implement Gradient Descent (GD) with line search and Newton's method.
   - Use synthetic dataset provided in `04_datasets/logistic_data.csv`.
3. Experiments:
   - Compare convergence (iterations to threshold), runtime, and final accuracy.
   - Plot learning curves and parameter trajectories.
4. Deliverables:
   - `project_notebook.ipynb` (runnable) with math, code, plots.
   - Short report (2 pages) describing derivation and experiments.
