<!-- Math rendered using GitHub Markdown: use $...$ and $$...$$ -->


# Slides — Session 2 Linear Transformations

---  
## Slide: Transformations
Scaling, rotation, shear, reflection.


```
flowchart LR
v["v"]
R["Rotation Matrix"]
v --> R --> vR["R(v)"]

```

```

---  
## Slide: Determinant
- Area/volume scaling factor
- det=0: collapse
- det<0: orientation flip

---  
## Slide: Inverse
- Exists if det ≠ 0
- For orthogonal, inverse = transpose

---  
## Slide: Gram-Schmidt
Orthogonalization by projection subtraction.

---  
## Slide: Eigen decomposition
- Solve det(A-λI)=0
- Eigenbasis: diagonalize A
```
