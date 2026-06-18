<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates

Topics include Trajectory optimization, iLQR, Differentiable programming, Nonlinear control, Tutorial.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents iLQR and its variants as differentiable programming algorithmic templates, enabling systematic derivation, implementation, and differentiation through iLQR solvers using automatic differentiation frameworks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Iterative optimization algorithms depend on access to information about the objective function. In a differentiable programming framework, this information, such as gradients, can be automatically derived from the computational graph. We explore how nonlinear control algorithms, often employing linear and/or quadratic approximations, can be effectively cast within this framework. Our approach illuminates shared components and differences between gradient descent, Gauss-Newton, Newton, and differential dynamic programming methods in the context of discrete time nonlinear control. Furthermore, we present line-search strategies and regularized variants of these algorithms, along with a comprehensive analysis of their computational complexities. We study the performance of the aforementioned algorithms on various nonlinear control benchmarks, including autonomous car racing simulations using a simplified car model. All implementations are publicly available in a package coded in a differentiable programming language.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider nonlinear control problems in discrete time with finite horizon, i.e., problems of the form

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problems of the form have been tackled in various ways, from direct approaches using nonlinear optimization to convex relaxations using semi-definite optimization. Numerous packages exist for such problems such as CasAdi, Pyomo, JumP, IPOPT, or SNOPT, Crocoddyl, acados. A popular approach of the former category proceeds by computing at each iteration the linear quadratic regulator associated with a linear quadratic approximation of the problem around the current candidate solutions (Jacobson and Mayne; Li and Todorov; Sideris and Bobrow; Tassa et al. ). The computed feedback policies are then applied either along the linearized dynamics or along the original dynamics to output a new candidate solution. Such canonical nonlinear control algorithms efficiently incorporate second-order information into the optimization procedure by exploiting the dynamical structure of the problem. This approach lends itself to an integration in a differentiable programming framework to extend this paradigm beyond first-order oracles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Differentiable programming consists of the implementation of functions in a programming language that enables access to derivatives of these functions by automatic differentiation (Baur and Strassen; Rumelhart et al.; LeCun; Schmidhuber; Gilbert; Werbos; Griewank and Walther; Baydin et al.; Bolte and Pauwels; Abadi et al.; Paszke et al. ). Automatic differentiation itself has roots in the control literature, and its use is pervasive in numerous domains, in particular deep learning (Zhang et al.; Goodfellow et al. ). Canonical nonlinear control algorithms incorporating second order information can also be integrated in reinforcement learning pipelines (Recht; Kakade et al. ), and may then benefit from a differentiable programming viewpoint to isolate their underlying principles. These algorithms have indeed generally be presented through linear algebraic manipulations instantiated separately for each algorithm, which hinder a global perspective (Murray and Yakowitz; Pantoja; Li and Todorov; Sideris and Bobrow; Tassa et al. ).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The motivation of this work is to cast all such algorithms in a common differentiable programming viewpoint to delineate the discrepancies between the different algorithms and identify the common subroutines. We review the implementation of (i) a Gauss-Newton method, a.k.a. Iterative Linear Quadratic Regulator (ILQR), (ii) a Newton method (Pantoja; Liao and Shoemaker; Dunn and Bertsekas ), (iii) a differential dynamic programming approach based on linear approximations of the dynamics and quadratic approximations of the costs, a.k.a. iterative Linear Quadratic Regulator (iLQR), (iv) a differential dynamic programming approach based on quadratic approximations of both dynamics and costs, usually simply called DDP, and consider regularized variants of the aforementioned algorithms with their corresponding line searches. In turn, the differentiable programming viewpoint informs efficient handling of memory by appropriate check-pointing. An extended related work discussion is in Appendix B.\

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outline. In Sec. we recall how linear quadratic control problems are solved by dynamic programming and used as a building block for nonlinear control algorithms. The implementation of classical optimization oracles such as a gradient step, a Gauss-Newton step, or a Newton step is presented in Sec.. Sec. details the rationale and implementation of differential dynamic programming approaches. Sec. presents the computational complexities of each oracle in terms of space and time complexities in a differentiable programming framework. All algorithms are tested on several synthetic problems in Sec.: swinging-up a fixed pendulum, and autonomous car racing with simple dynamics. Code is available at
