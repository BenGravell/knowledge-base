Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization

Topics include Convex optimization, Nonconvex optimization, Stochastic optimization, Neural networks, Classification, Optimization, ZO-SVRG, ZO, Variance reduction, Black box.

As application demands for zeroth-order (gradient-free) optimization accelerate, the need for variance reduced and faster converging approaches is also intensifying. This paper addresses these challenges by presenting: a) a comprehensive theoretical analysis of variance reduced zeroth-order (ZO) optimization, b) a novel variance reduced ZO algorithm, called ZO-SVRG, and c) an experimental evaluation of our approach in the context of two compelling applications, black-box chemical material classification and generation of adversarial examples from black-box deep neural network models. Our theoretical analysis uncovers an essential difficulty in the analysis of ZO-SVRG: the unbiased assumption on gradient estimates no longer holds. We prove that compared to its first-order counterpart, ZO-SVRG with a two-point random gradient estimator could suffer an additional error of order O(1/b), where b is the mini-batch size. To mitigate this error, we propose two accelerated versions of ZO-SVRG utilizing variance reduced gradient estimators, which achieve the best rate known for ZO stochastic optimization (in terms of iterations)....

## Introduction

Zeroth-order (gradient-free) optimization is increasingly embraced for solving machine learning problems where explicit expressions of the gradients are difficult or infeasible to obtain. Recent examples have shown zeroth-order (ZO) based generation of prediction-evasive, black-box adversarial attacks on deep neural networks (DNNs) as effective as state-of-the-art white-box attacks, despite leveraging only the inputs and outputs of the targeted DNN. Additional classes of applications include network control and management with time-varying constraints and limited computation capacity, and parameter inference of black-box systems....

Although many ZO algorithms have recently been developed and analyzed, they often suffer from the high variances of ZO gradient estimates, and in turn, hampered convergence rates. In addition, these algorithms are mainly designed for convex settings, which limits their applicability in a wide range of (non-convex) machine learning problems.

## Conclusion

In this paper, we studied ZO-SVRG, a new ZO nonconvex optimization method. We presented new convergence results beyond the existing work on ZO nonconvex optimization. We show that ZO-SVRG improves the convergence rate of ZO-SGD from $O{({1/\sqrt{T}})}$ to $O{({1/T})}$ but suffers a new correction term of order $O{({1/b})}$. The is the side effect of combining a two-point random gradient estimators with SVRG. We then propose two accelerated variants of ZO-SVRG based on improved gradient estimators of reduced variances. We show an illuminating trade-off between the iteration and the function query complexity....

where $\delta_{n} = 1$ if the mini-batch contains i.i.d. samples from $\lbrack n\rbrack$ with replacement, and $\delta_{n} = {I{({b < n})}}$ if samples are randomly selected without replacement. Here $I{({b < n})}$ is $1$ if $b < n$, and $0$ if $b = n$.

In addition to RandGradEst and Avg-RandGradEst, the work considered a coordinate-wise gradient estimator. Here every partial derivative is estimated via the two-point querying scheme under fixed direction vectors,

Proposition 2 shows that compared to CoordGradEst, RandGradEst and Avg-RandGradEst involve an additional error term within a factor $O{(d)}$ and $O{({{({q + d})}/q})}$ of ${\|{{\nabla f}{(\mathbf{x})}}\|}_{2}^{2}$, respectively....
