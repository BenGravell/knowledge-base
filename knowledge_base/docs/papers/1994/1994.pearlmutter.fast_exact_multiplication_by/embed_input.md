<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Exact Multiplication by the Hessian

Topics include Automatic differentiation, Hessian-vector products, Second-order optimization, Neural networks, Backpropagation, R-operator.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the R-operator method for computing exact Hessian-vector products at roughly the cost of a gradient evaluation, without forming the full Hessian. This became a central automatic-differentiation primitive for second-order neural-network optimization, curvature estimation, and iterative methods that only need matrix-vector products.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Just storing the Hessian H (the matrix of second derivatives δ2E/δwiδwj of the error E with respect to each pair of weights) of a large neural network is difficult. Since a common use of a large matrix like H is to compute its product with various vectors, we derive a technique that directly calculates Hv, where v is an arbitrary vector. To calculate Hv, we first define a differential operator Rv{f(w)} = (δ/δr)f(w + rv)|r=0, note that Rv{▽w} = Hv and Rv{w} = v, and then apply Rv{·} to the equations used to compute ▽w. The result is an exact and numerically stable procedure for computing Hv, which takes about as much computation, and is about as local, as a gradient evaluation. We then apply the technique to a one pass gradient calculation algorithm (backpropagation), a relaxation gradient calculation algorithm (recurrent backpropagation), and two stochastic gradient calculation algorithms (Boltzmann machines and weight perturbation).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we show that this technique can be used at the heart of many iterative techniques for computing various properties of H, obviating any need to calculate the full Hessian.
