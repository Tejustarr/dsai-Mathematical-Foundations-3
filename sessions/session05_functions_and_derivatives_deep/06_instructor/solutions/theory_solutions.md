# Solutions — Theory Problems (sketches)

1. Product rule proof: Start from limit definition f'g = lim (f(x+h)g(x+h)-f(x)g(x))/h ; add and subtract f(x+h)g(x) etc.
2. For f(x,y)=x^2 y + e^{xy}:
   grad = [2x y + y e^{xy}, x^2 + x e^{xy}]  (verify)
   Hessian = [[2y + y^2 e^{xy}, 2x + e^{xy} + xy e^{xy}], [... symmetric ...]]
3. Jacobi's formula: d/dt det(A(t)) = det(A) trace(A^{-1} A').
4. Directional derivative identity follows from definition of directional derivative and linear approximation.
5. Error orders: central diff uses symmetric cancellation giving O(h^2).