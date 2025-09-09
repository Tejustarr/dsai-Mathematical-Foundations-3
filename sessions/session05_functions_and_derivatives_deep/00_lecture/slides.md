<!-- Math rendered using GitHub Markdown: use $...$ and $$...$$ -->


# Slides — Session 5 Functions & Derivatives

---  
## Slide: Function types
- explicit, implicit, parametric
- scalar vs vector-valued

---  
## Slide: Univariate rules (quick list)
- power, product, quotient, chain

---  
## Slide: Chain rule (visual)

```
flowchart LR
x["x"]
g["g(x)"]
f["f(g(x))"]
x --> g --> f
subgraph deriv
  dg["g'(x)"] --> mul["*"]
  df["f'(g(x))"] --> mul
  mul --> out["(f∘g)'"]
end

```

```

---  
## Slide: Jacobian & Hessian
- Jacobian = matrix of partials
- Hessian = second derivatives; curvature

---  
## Slide: Numerical differentiation
- forward, backward, central
- pick h carefully (roundoff vs truncation)

---  
## Slide: Applications in ML
- gradients for loss functions (MSE, logistic)
- Hessian in Newton's method
```
