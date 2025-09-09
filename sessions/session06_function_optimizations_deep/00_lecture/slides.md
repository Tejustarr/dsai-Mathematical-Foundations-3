<!-- Math rendered using GitHub Markdown: use ![](https://render.githubusercontent.com/render/math?math=...) and 

![](https://render.githubusercontent.com/render/math?math=...)

 -->


# Slides — Session 6 Function Optimizations

---  
## Slide: Maxima & Minima
- ∇f=0 critical points
- Hessian test: positive definite = min, negative = max, indefinite = saddle

---  
## Slide: Convex functions
- definition
- all local minima are global
- examples: quadratic, norm

---  
## Slide: Gradient Descent
x_{k+1} = x_k - α ∇f(x_k)
- step size α matters
- too small = slow, too large = divergence

---  
## Slide: SGD
- use random subset
- cheaper per update
- noisy trajectory, but scalable