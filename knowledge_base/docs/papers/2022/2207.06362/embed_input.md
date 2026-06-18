Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates

Topics include Trajectory optimization, iLQR, Differentiable programming, Nonlinear control, Tutorial.

Presents iLQR and its variants as differentiable programming algorithmic templates, enabling systematic derivation, implementation, and differentiation through iLQR solvers using automatic differentiation frameworks.

Iterative optimization algorithms depend on access to information about the objective function. In a differentiable programming framework, this information, such as gradients, can be automatically derived from the computational graph. We explore how nonlinear control algorithms, often employing linear and/or quadratic approximations, can be effectively cast within this framework. Our approach illuminates shared components and differences between gradient descent, Gauss-Newton, Newton, and differential dynamic programming methods in the context of discrete time nonlinear control. Furthermore, we present line-search strategies and regularized variants of these algorithms, along with a comprehensive analysis of their computational complexities. We study the performance of the aforementioned algorithms on various nonlinear control benchmarks, including autonomous car racing simulations using a simplified car model. All implementations are publicly available in a package coded in a differentiable programming language.

## Introduction

We consider nonlinear control problems in discrete time with finite horizon, i.e., problems of the form

Problems of the form have been tackled in various ways, from direct approaches using nonlinear optimization to convex relaxations using semi-definite optimization. Numerous packages exist for such problems such as CasAdi, Pyomo, JumP, IPOPT, or SNOPT, Crocoddyl, acados. A popular approach of the former category proceeds by computing at each iteration the linear quadratic regulator associated with a linear quadratic approximation of the problem around the current candidate solutions (Jacobson and Mayne; Li and Todorov; Sideris and Bobrow; Tassa et al. ).

Differentiable programming consists of the implementation of functions in a programming language that enables access to derivatives of these functions by automatic differentiation (Baur and Strassen; Rumelhart et al.; LeCun; Schmidhuber; Gilbert; Werbos; Griewank and Walther; Baydin et al.; Bolte and Pauwels; Abadi et al.; Paszke et al. ). Automatic differentiation itself has roots in the control literature, and its use is pervasive in numerous domains, in particular deep learning (Zhang et al.; Goodfellow et al. ).

The motivation of this work is to cast all such algorithms in a common differentiable programming viewpoint to delineate the discrepancies between the different algorithms and identify the common subroutines. We review the implementation of (i) a Gauss-Newton method, a.k.a. Iterative Linear Quadratic Regulator (ILQR), (ii) a Newton method (Pantoja; Liao and Shoemaker; Dunn and Bertsekas ), (iii) a differential dynamic programming approach based on linear approximations of the dynamics and quadratic approximations of the costs, a.k.a.

Outline. In Sec. we recall how linear quadratic control problems are solved by dynamic programming and used as a building block for nonlinear control algorithms. The implementation of classical optimization oracles such as a gradient step, a Gauss-Newton step, or a Newton step is presented in Sec.. Sec. details the rationale and implementation of differential dynamic programming approaches. Sec. presents the computational complexities of each oracle in terms of space and time complexities in a differentiable programming framework.
