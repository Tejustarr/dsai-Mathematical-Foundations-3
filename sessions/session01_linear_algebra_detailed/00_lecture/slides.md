<!-- Math rendered using GitHub Markdown: use ![](https://render.githubusercontent.com/render/math?math=...) and 

![](https://render.githubusercontent.com/render/math?math=...)

 -->


# Slides — Session 1 (Markdown slide-style)

---  
## Slide: What is Linear Algebra?
- Language for vectors, matrices, linear maps
- Relevance to data science & ML

---  
## Slide: Vector basics
- Definitions & operations
- Dot product, norm, orthogonality

---  
## Slide: Vector space & basis
- Span, linear independence, basis, dimension

---  
## Slide: Change of basis (diagram)

```
flowchart LR
$$
subgraph StandardBasis
  e1["e1"] --> v["v (coords)"]
  e2["e2"] --> v
end
subgraph NewBasis
  b1["b1"] --> vB["v_B (coords)"]
  b2["b2"] --> vB
end
vB --> P["P (change-of-basis)"]
P --> v
$$

```




![](https://render.githubusercontent.com/render/math?math=---++%0A%23%23+Slide%3A+Matrix+types+%26+examples%0A-+Identity%2C+diagonal%2C+symmetric%2C+orthogonal%0A-+Example%3A+rotation+matrix+in+2D)


R(\theta)=\begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}


![](https://render.githubusercontent.com/render/math?math=---++%0A%23%23+Slide%3A+Projection+%26+least+squares+%28formula%29%0A-+Projection+matrix+%24P+%3D+A%28A%5ET+A%29%5E%7B-1%7D+A%5ET%24%0A-+Least+squares+solution+%24%5Chat+x+%3D+%28A%5ET+A%29%5E%7B-1%7D+A%5ET+b%24%0A%0A---++%0A%23%23+Slide%3A+Applications%0A-+PCA%2C+linear+regression%2C+image+transforms%2C+embeddings%0A%0A---++%0A%23%23+Slide%3A+References+%26+next+session%0A-+Strang+ch.1%E2%80%932%2C+numpy+docs)



