
# Slides — Session 3 Linear Algebra for ML

---  
## Slide: Linear Regression
- Model: y ≈ Xw
- Loss: ||Xw - y||^2
- Solution: ŵ = (X^T X)^{-1} X^T y

---  
## Slide: Normal Equations (derivation)
Gradient of L(w) = 0
→ X^T X w = X^T y

---  
## Slide: Example
Data: x=[1,2,3], y=[2,2.5,3.5]
X = [[1,1],[1,2],[1,3]]

---  
## Slide: Image as Matrix
- Each pixel = intensity
- Grayscale = single 2D array
- RGB = 3 channels

---  
## Slide: Filtering
- Kernel convolution = linear operation
- Blur, sharpen, edge detection