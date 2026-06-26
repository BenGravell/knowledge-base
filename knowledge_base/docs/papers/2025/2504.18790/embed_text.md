## Introduction

Mathematical derivatives are fundamental to much of science. At a high level, derivatives offer a local characterization of a function's steepest ascent or descent directions. In practice, this property is frequently employed in numerical optimization, where derivatives guide the iterative process of navigating downhill through the landscape of a function. For example, derivative-based optimization is widely used in robotics for tasks such as inverse kinematics, trajectory optimization, physics simulation, control, learning, and constrained planning.

Since derivative computation often takes place within a tight, low-level loop in the application stack, the speed of this process is critical to maintaining sufficient performance. For example, consider a legged robot using a derivative-based model predictive control (MPC) algorithm to maintain balance. If the robot is nudged, it must compute derivatives very rapidly to guide the optimization process and allow the real-time reactive actuations of its legs to stay upright.

As we will discuss in §II, there are several standard techniques to calculate the derivatives of a function. These techniques generally involve repeatedly evaluating the function with slightly modified arguments, observing the resulting perturbations in the function's input or output space, and constructing the derivative from these observations. However, since the number of function evaluations required typically scales with the number of inputs or outputs of the function, these approaches can quickly become prohibitively expensive when either, or especially both, of these dimensions increase.

Figure 1: In this work, we present an approach for efficiently computing a sequence of approximate derivatives by reusing information from recent calculations. Our approach first isolates an affine solution space where the true derivative must lie (purple line). Next, a closed-form optimization procedure locates the point in this space that is the closest orthogonal distance (red lines) to a “web” of affine spaces (dark blue lines) that intersects at the previous approximate derivative (orange dot). This optimal point will be the transpose of the approximate derivative matrix, D*⊤ (green dot).

In this work, we recognize that derivatives are often not computed in isolation; conversely, it is quite common to calculate a sequence of derivatives, each one building on the last. For example, in optimization, function inputs typically change only slightly between iterations as small steps are taken downhill, with each input incrementally leading to the next. The key insight of this work is that derivative computation can be accelerated by reusing information from previous, related calculations---a strategy known as coherence.

We present a first instantiation of this coherence-based strategy for derivative computation through a novel approach called the Web of Affine Spaces (WASP) Optimization. At its core, this approach frames derivative computation as a constrained least-squares minimization problem. Each iteration of the algorithm requires only one Jacobian-vector product (JVP) which creates an affine space within which the true derivative is guaranteed to lie. The optimization is then tasked with finding the transpose of an approximate derivative that lies on this affine space (specified by a hard constraint) while best aligning with previous, related computations (specified in the objective function). This process is illustrated in Figure 1.

We provide a closed-form solution to this minimization problem by directly solving its corresponding Karush-Kuhn-Tucker (KKT) system. Our algorithm that uses this minimization also incorporates an error detection and correction mechanism that automatically identifies when its outputs drift too far from the ground-truth derivatives, allocating additional iterations to realign its results as needed. This mechanism is guided by two user-adjustable parameters, affording a flexible balance between accuracy and computational performance tailored to specific applications.

The algorithm associated with our approach (§V) is straightforward to implement and can be easily interfaced with existing code. The algorithm does not require tape-based variable tracking or an external automatic differentiation library; it simply uses standard forward passes through a function. All ideas presented in this work can be implemented in less than 100 lines of code in any programming language that supports numerical computing.

We demonstrate the effectiveness of our approach through a series of numerical experiments, benchmarking it against alternative derivative computation methods. We show that our approach improves the performance of computing a sequence of derivatives on small to medium-sized functions, i.e., functions with approximately fewer than 500 combined inputs and outputs. Additionally, we demonstrate its practical applicability in a robotics optimization context, showcasing its use in a Jacobian-pseudoinverse-based root-finding procedure to determine the pose of a quadruped robot with specified foot and end-effector placements. We conclude with a discussion of the limitations and implications of our work.

## Background

In this section, we provide background for our approach, including notation, problem setup, standard approaches for derivative computation, and relevant prior work.

### II-A Notation

The main mathematical building blocks through this work are matrices and vectors. Matrices will be denoted with bold upper case letters, e.g., $\mathbf{A}$, and vectors will be denoted with bold lower case letters, e.g., $\mathbf{x}$. Indexing into matrices or vectors will use sub-brackets, e.g., $\mathbf{A}_{\lbrack 0,1\rbrack}$ or $\mathbf{x}_{\lbrack 2\rbrack}$. A full row or column of a matrix can be referenced using a colon, e.g., $\mathbf{A}_{\lbrack:,0\rbrack}$ is the first column and $\mathbf{A}_{\lbrack 0,:\rbrack}$ is the first row.

### II-B Problem Setup

In this work, we will refer to some function under consideration as $f$, which has $n$ inputs and $m$ outputs, i.e., $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$. We will also assume that the given function $f$ is computable and differentiable.

The mathematical object we are trying to compute is the derivative object of $f$ at a given input $\mathbf{x}_{k} \in {\mathbb{R}}^{n}$, denoted as $\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}$. This derivative will be an $m \times n$ matrix, i.e., $\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}} \in {\mathbb{R}}^{m \times n}$, with the following structure: This matrix is referred to as a Jacobian, or specifically as a gradient when $m = 1$. Throughout this work, however, we will consistently use the broader term, derivative.

### II-C Problem Statement

In this work, we are specifically looking to compute a sequence of approximate derivative matrices: Our goal is to compute these approximate derivatives as quickly and as accurately as possible. We assume that the derivative computation at an input $\mathbf{x}_{k}$ can utilize knowledge of all prior inputs and calculations (i.e., information available up to and including $k$), but it has no access to information about future inputs (i.e., data beyond $k$).

There is an implicit assumption in our problem that adjacent inputs, e.g., $\mathbf{x}_{k}$ and $\mathbf{x}_{k + 1}$, are relatively "close", as is often the case in iterative optimization. However, our approach does not impose any specific requirement for the closeness of neighboring inputs. Instead, it is informally assumed that the approach will perform more effectively when the inputs are closer to each other with efficiency or accuracy likely diminishing as the distance between inputs increases.

### II-D Standard Derivative Computation Algorithms

A common strategy for computing derivatives involves introducing small perturbations in the input or output space surrounding the derivative and incrementally constructing the derivative matrix by analyzing the local behavior exhibited by the derivative in response to these perturbations.

Specifically, perturbing the derivative in the input space looks like the following: The $\Delta\mathbf{x}$ object here is commonly called a tangent, and the resulting $\Delta\mathbf{f}$ is known as the Jacobian-vector product (JVP) or directional derivative. Conversely, perturbing the derivative in the output space looks like the following: The $\Delta\mathbf{f}^{\top}$ object here is commonly called an adjoint, and the result $\Delta\mathbf{x}^{\top}$ is known as the vector-Jacobian product (VJP).

In general, there are two standard ways of computing JVPs: forward-mode automatic differentiation; and finite-differencing. Forward-mode automatic differentiation propagates tangent information alongside standard numerical computations. This technique commonly involves overloading floating-point operations to include additional tangent data. A JVP via first-order finite-differencing derives from the standard limit-based definition of a derivative: If $\epsilon$ is small, this approximation is close to the true JVP. Note that this JVP requires two forward passes through $f$, and additional JVPs at the same input $\mathbf{x}_{k}$ would only require one additional forward pass through $f$ each.

Conversely, there is generally only one way of computing a VJP: reverse-mode automatic differentiation, often called backpropagation in a machine-learning context. This process involves building a computation graph (or Wengert List ) on a forward pass, then doing a reverse pass over this computation graph to backward propagate adjoint information. In general, VJP-based differentiation is more challenging to implement and manage compared to its JVP-based counterpart. This approach typically requires an external library to track variables and operations, enabling the construction of a computation graph. As a result, all downstream computations within a function must adhere to the same code structure or use the same library.

Note that the concepts of JVPs and VJPs now give a clear strategy for isolating the whole derivative matrix. For instance, using "one-hot" vectors for tangents or adjoints, i.e., vectors where only the $i$-th element is $1$ and all others are $0$, can effectively capture the $i$-th column or $i$-th row of the derivative matrix, respectively. Thus, the derivative matrix can be fully recovered using $n$ JVPs or $m$ VJPs.

In practice, a JVP-based approach is typically used if $n < m$ and a VJP-based approach is typically used if $m < n$. However, as either $m$ or $n$ increase -- or, especially if both increase -- these approaches can quickly become inefficient.

### II-E Other Related Works

Our work builds on previous methods aimed at accelerating derivative computations through approximations. For first-order derivatives, our approach is closest to Simultaneous Perturbation Stochastic Approximation (SPSA). SPSA, primarily used in optimization, estimates gradients using only two function evaluations by perturbing the function along one sampled direction. This idea has inspired more recent work that approximates a gradient via a bundle of stochastic samples at a point.

Our approach also approximates derivatives by perturbing inputs in random directions and observing the output changes. Like SPSA (and related methods), it aims to achieve an approximate derivative with a small number forward passes through the function. However, we treat the random directions as a matrix in a least squares optimization, aligning the result with prior observations. Also, unlike previous methods that primarily focus on gradients, our approach handles derivative objects of any shape, including full Jacobian matrices.

Interestingly, while coherence-based strategies have not been widely explored for first-order derivatives, they are frequently used in second-order derivative computations of scalar functions within optimization algorithms. For example, quasi-Newton methods like Davidon--Fletcher--Powell (DFP), Symmetric Rank 1 (SR1), and Broyden--Fletcher--Goldfarb--Shanno (BFGS) use the secant equation to iteratively build approximations of the Hessian matrix over a sequence of related inputs. However, these algorithms cannot compute gradients directly, as they rely on them as inputs. Through this lens, our current approach can be viewed as quite related to quasi-Newton methods for Hessian approximation, but specifically for first-order derivatives.

## Technical Overview

In this section, we overview the central concepts and intuitions of our idea.

### III-A Differentiation as Linear System

As covered in §II, each pass through the function in JVP-based differentiation generates one JVP: ${\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}\Delta\mathbf{x}} = {\Delta\mathbf{f}}$. We can bundle several tangents together in a matrix in order to get a matrix of JVPs: Note that the $i$-th tangent vector and JVP are denoted as $\Delta\mathbf{x}_{i}$ and $\Delta\mathbf{f}_{i}$, respectively. We use this same notation throughout the paper. From Equation 6, we see that JVP-based differentiation can also be interpreted as setting $\Delta\mathbf{X}$ to be the identity matrix and "solving" a linear system: This concept is mathematically straight forward, but it is important to note that generating $\Delta\mathbf{F}$ can be computationally expensive as it requires $n$ forward passes through $f$. Our idea builds on this linear system idea, with $\Delta\mathbf{X}$ no longer only being an identity matrix.

### III-B Differentiation as Least Squares Optimization

In the section above, we assessed the linear system ${\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}\Delta\mathbf{X}} = {\Delta\mathbf{F}}$. If we take the transpose of both sides, we get the following: This equation now nicely matches a standard "${Ax} = b$" linear system, with "$x$" being an unknown matrix variable, in our case. We cast this linear system as a least squares optimization: Here, $\mathbf{D}^{\top}$ is the decision variable acting as the derivative matrix, and $F$ denotes the Frobenius norm over matrices. This formulation offers a clear analytical framework for considering general solutions, even when $\Delta\mathbf{X}$ is not a square or identity matrix. The closed-form solution for this optimization problem is the following: where the $\dagger$ symbol denotes the Moore-Penrose Pseudoinverse. If $\Delta\mathbf{X}$ is full rank, $r \geq n$ (i.e., $\Delta\mathbf{X}^{\top}$ is square or tall), and $\Delta\mathbf{F}$ is a matrix of JVPs corresponding to the tangents in $\Delta\mathbf{X}$, this solution exactly matches the true derivative matrix. However, this solution has not yet improved efficiency since we would still have to compute $\Delta\mathbf{F}$, which was the most expensive step from before.

A key insight in this work is that $\Delta\mathbf{F}$ in the minimization above can be replaced with an approximation, $\hat{\Delta ⁢\mathbf{F}}$: Rather than fully recomputing $\Delta\mathbf{F}$ for each new input, we incrementally update $\hat{\Delta ⁢\mathbf{F}}$ across a sequence of inputs. Since $\hat{\Delta ⁢\mathbf{F}}$ is an approximation, the entire minimization process now becomes an approximation as well. Through the remainder of this work, we argue that, given an additional constraint on Equation 10 and a particular strategy for updating $\hat{\Delta ⁢\mathbf{F}}$, this approach is more efficient than standard approaches for computing a sequence of derivative matrices while maintaining accuracy sufficient for practical use.

## Technical Details

In this section, we detail the Web of Affine of Spaces (WASP) Optimization approach for computing a sequence of approximate derivatives matrices.

### IV-A Affine Solution Space

As discussed above, the bottleneck of Equation 8 is the calculation of $\Delta\mathbf{F}$, the matrix bundle consisting of $r$ JVPs, where $r \geq n$. Rather than relying solely on $r$ JVPs, we first think about how much information about the derivative solution can be inferred from only one JVP.

Suppose we have one fixed tangent of random values, ${\Delta\mathbf{x}} \in {\mathbb{R}}^{n}$ with a corresponding JVP, ${\Delta\mathbf{f}} \in {\mathbb{R}}^{m}$. We can plug these vectors into Equation 8, with ${\Delta\mathbf{X}^{\top}} \equiv {\Delta\mathbf{x}^{\top}} \in {\mathbb{R}}^{1 \times n}$ and ${\Delta\mathbf{F}^{\top}} \equiv {\Delta\mathbf{f}^{\top}} \in {\mathbb{R}}^{1 \times m}$. If $n > 1$, we have $\Delta\mathbf{X}^{\top}$ as a "wide matrix" that elicits an under-determined least squares system with infinitely many solutions. The space of all solutions is parameterized as follows: where $\mathbf{Z}_{\Delta\mathbf{x}^{\top}} \in {\mathbb{R}}^{n \times {({n - 1})}}$ is the null space matrix of $\Delta\mathbf{x}^{\top}$ (i.e., ${\Delta\mathbf{x}^{\top}\mathbf{Z}_{\Delta\mathbf{x}^{\top}}} = \mathbf{0}$), and $\mathbf{Y}$ is any matrix in ${\mathbb{R}}^{{({n - 1})} \times m}$. Equation 11 defines an ${({n - 1})} \times m$-dimensional affine space encompassing all possible solutions, where $\mathbf{Z}_{\Delta\mathbf{x}^{\top}}\mathbf{Y}$ represents the associated vector space, and ${({\Delta\mathbf{x}^{\top}})}^{\dagger}\Delta\mathbf{f}^{\top}$ (the minimum-norm solution) serves as the offset from the origin. Even with just one JVP, we have captured a space where the true derivative must lie for some setting of $\mathbf{Y}$. Our idea, covered below, constrains the solution to lie within the space defined in Equation 11, while also maintaining alignment with recent computations.

### IV-B Web of Affine Spaces

In the previous section, we isolated a space where the true derivative must lie given only a single JVP. We now assess what happens if we consider more JVPs.

Consider $r$ JVPs, $\Delta\mathbf{f}_{i}$, with corresponding tangents $\Delta\mathbf{x}_{i}$, where $i \in {1,\ldots,r}$. Each JVP defines its own affine solution space, within which the true derivative must reside: ${{({\Delta\mathbf{x}_{i}^{\top}})}^{\dagger}\Delta\mathbf{f}_{i}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{i}^{\top}}\mathbf{Y}}$. Knowing that the true derivative must lie within all of these affine spaces, we can deduce that it must be located at the intersection of these spaces. Indeed, when $r \geq n$, the intersection of all these spaces results in a single, unique matrix: the exact derivative. Essentially, this is precisely what the solution in Equation 9 achieves.

We now return to the idea presented in Equation 10. What if some JVPs are approximate, $\hat{\Delta ⁢\mathbf{f}}$, rather than ground-truth, $\Delta\mathbf{f}$? The idea here is that, if we have one ground-truth JVP, $\Delta\mathbf{f}_{i}$, along with at least $n - 1$ other approximate JVPs, ${\hat{\Delta ⁢\mathbf{f}}}_{j}$, we can still force the solution to lie on ${{({\Delta\mathbf{x}_{i}^{\top}})}^{\dagger}\Delta\mathbf{f}_{i}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{i}^{\top}}\mathbf{Y}}$ in a manner that gets as close as possible to the affine spaces corresponding to the other approximate JVPs, ${{({\Delta\mathbf{x}_{j}^{\top}})}^{\dagger}{\hat{\Delta ⁢\mathbf{f}}}_{j}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{j}^{\top}}\mathbf{Y}}$. We refer to these approximate JVP affine spaces as the web of affine spaces.

### IV-C Web of Affine Spaces Optimization

In this section, we overview the mathematical side of the Web of Affine Spaces (WASP) Optimization. We specify the algorithmic details that instantiate this math in practice in §V.

Suppose $\Delta\mathbf{X}$ is a full rank $n \times r$ matrix where $r \geq n$. We consider the columns of $\Delta\mathbf{X}$ to be $r$ separate tangent vectors where the $i$-th column is denoted as $\Delta\mathbf{x}_{i}$. Assume we have a current input, $\mathbf{x}_{k}$, a selected tangent vector, $\Delta\mathbf{x}_{i}$, and a JVP corresponding to $\mathbf{x}_{k}$ in the $\Delta\mathbf{x}_{i}$ direction, $\Delta\mathbf{f}_{i}$ (likely computed using Equation 4). Also, assume we have a web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$.

We cast the optimization described above as a modified version of Equation 10 with an added constraint: This constrained optimization best matches the intersection of the web of affine spaces, specified in the objective function, while also restricting the solution to lie on the affine solution space, specified in the constraint.

The solution to Equation 12 is the following: This solution is derived using a Karush-Kuhn-Tucker (KKT) system, as seen in detail in §IV-D. Here, $\mathbf{D}^{\ast \top} \in {\mathbb{R}}^{n \times m}$ is the transpose of the approximate derivative matrix and $\mathbf{\Lambda}^{\ast \top} \in {\mathbb{R}}^{1 \times m}$ is a vector of Lagrange multipliers. We can rewrite the solution in Equation 13 by taking the block matrix inverse of the left matrix: Here, $s_{i}$ is the Schur Complement of the block matrix $\mathbf{A} = {2\Delta\mathbf{X}\Delta\mathbf{X}^{\top}}$.

Because we do not use the Lagrange multipliers in this work, we can use Equation 14 to more directly solve for $\mathbf{D}^{\ast \top}$: Here, $\mathbf{I}_{n \times n}$ is an $n \times n$ identity matrix, and $\mathbf{A}$ and $s$ can be found in Equation 14. For interested readers, we discuss the geometric significance of Equation 15 in the Appendix §X-A.

Again, this section has only covered the mathematical procedure behind the Web of Affine Spaces Optimization. In §V, we overview our algorithm that utilizes this optimization, including how to initialize and update $\hat{\Delta ⁢\mathbf{F}}$, how to preprocess and cache parts of Equation 15 to accelerate the optimization at runtime, how to determine if $\mathbf{D}^{\ast \top}$ is an acceptable approximation, and how to achieve a more accurate result if the expected error is too high.

### IV-D Derivation of Web of Affine Spaces Solution

In this section, we derive the solution specified in Equation 13. First, note that another way of writing the objective function ${\|{{\Delta\mathbf{X}^{\top}\mathbf{D}^{\top}} - {\hat{\Delta ⁢\mathbf{F}}}^{\top}}\|}_{F}^{2}$ is the following: where $tr$ is the matrix trace. We now multiply the terms within the trace function: Writing the whole optimization out in this form: we form the Lagrangian of the optimization: where $\mathbf{\Lambda} \in {\mathbb{R}}^{m \times 1}$ are the Lagrange multipliers.

A first-order necessary condition for an optimal solution is that the Karush-Kuhn-Tucker (KKT) conditions are satisfied. Specifically, for an equality constrained problem, this means that the partial derivatives of the Lagrangian with respect to both the decision variables and the Lagrange multipliers (associated with the equality constraints) are zero: We start with the first requirement: We now set the term equal to zero: For the second requirement from the Lagrangian, $\frac{\partial\mathcal{L}}{\partial\mathbf{\Lambda}^{\top}} = 0$, we have the following: Putting the previous components together into a KKT system, we have the following matrix equation: Using the matrix inverse, our final solution is the following: matching the solution seen in Equation 13. $\square$

## Algorithmic Details

In this section, we present algorithms that transform the mathematical framework from the previous section into a practical, implementable form. Pseudocode for our approach is found in Algorithms 1--4. $\hat{\Delta ⁢\mathbf{F}}\leftarrow\mathbf{0}_{m \times n}$ // m × n matrix of zeros 1 ΔX ← get_tangent_matrix(n) 𝒞1 ← // will store cached matrices 𝒞2 ← // will store cached matrices $\mathcal{C}_{1}\overset{+}{\leftarrow}{\mathbf{A}^{- 1}\left({\mathbf{I}_{n \times n} - {s_{i}^{- 1}\Delta\mathbf{x}_{i}\Delta\mathbf{x}_{i}^{\top}\mathbf{A}^{- 1}}} \right)2\Delta\mathbf{X}}$ // cached matrix $\mathcal{C}_{2}\overset{+}{\leftarrow}{s_{i}^{- 1}\mathbf{A}^{- 1}\Delta\mathbf{x}_{i}}$ // cached matrix cache ← ⌀ // A cache object that will store preprocessed items cache.i ← 0 // assuming matrices are using 0-indexing 11${cache}.{\hat{\Delta ⁢\mathbf{F}}\leftarrow\hat{\Delta ⁢\mathbf{F}}}$ Algorithm 1 get_cache(n, m) 2T ← randomly sampled n × n matrix U, Σ, V⊤ ← svd(T) // singular value decomposition on matrix ΔX ← UV⊤ // guaranteed to be an orthonormal matrix Algorithm 2 get_tangent_matrix(n) Δxi ← cache.ΔX[:,i] // i-th column of tangent bundle matrix ${\Delta\mathbf{f}_{i}}\leftarrow\frac{{f\left({\mathbf{x}_{k} + {\epsilon\Delta\mathbf{x}_{i}}} \right)} - f_{\mathbf{x}_{k}}}{\epsilon}$ // get ground truth JVP in current direction; ϵ should be a small value, e.g., ϵ = 0.00001 ${{\hat{\Delta ⁢\mathbf{f}}}_{i}\leftarrow{cache}}.{\hat{\Delta ⁢\mathbf{F}}}_{\lbrack:,i\rbrack}$ // current approximation for JVP in Δxi direction ${cache}.{{\hat{\Delta ⁢\mathbf{F}}}_{\lbrack:,i\rbrack}\leftarrow{\Delta\mathbf{f}_{i}}}$ // set i-th column to be ground truth JVP 11 ${\hat{\Delta ⁢\mathbf{F}}\leftarrow{cache}}.\hat{\Delta ⁢\mathbf{F}}$ $\mathbf{D}^{\ast \top}\leftarrow{{\mathbf{C}_{1}{\hat{\Delta ⁢\mathbf{F}}}^{\top}} + {\mathbf{C}_{2}\Delta\mathbf{f}_{i}^{\top}}}$ // solution from eq. 15 13 ${cache}.{\hat{\Delta ⁢\mathbf{F}}\leftarrow{\mathbf{D}^{\ast}\Delta\mathbf{X}}}$ 15 if $(\hat{\Delta ⁢\mathbf{f}_{i}},{\Delta\mathbf{f}_{i}})$ then Algorithm 3 wasp(f, xk, n, cache, dθ, dℓ) 2if ${|{\frac{\mathbf{a} \cdot \mathbf{b}}{\left\| \mathbf{a} \right\|\left\| \mathbf{b} \right\|} - 1}|} > d_{\theta}$ then 4if ${\min{({|{\frac{\left\| \mathbf{a} \right\|}{\left\| \mathbf{b} \right\|} - 1}|},{|{\frac{\left\| \mathbf{b} \right\|}{\left\| \mathbf{a} \right\|} - 1}|})}} > d_{\ell}$ then Algorithm 4 close_enough(a, b, dθ, dℓ)

### V-A Approximate Differentiation as Iterative Process

Our algorithm for computing approximate derivatives for a sequence of inputs ($\mathbf{x}_{k}$, $\mathbf{x}_{k + 1}$,...) is structured as an iterative process. This process centers around three matrices introduced in previous sections: $\mathbf{D}^{\ast}$, the current approximate derivative matrix; $\hat{\Delta ⁢\mathbf{F}}$, the current matrix of approximate JVPs; and $\Delta\mathbf{X}$, the matrix of tangents.

Given an input in the sequence, $\mathbf{x}_{k}$, our algorithm aims to compute an approximate derivative at that input, $\left. \hat{\frac{\partial f}{\partial\mathbf{x}}} \right|_{\mathbf{x}_{k}}$. The process begins by using the $\Delta\mathbf{X}$ matrix and current $\hat{\Delta ⁢\mathbf{F}}$ matrix to compute an updated version of $\mathbf{D}^{\ast}$. Subsequently, the new $\mathbf{D}^{\ast}$ matrix is used to update $\hat{\Delta ⁢\mathbf{F}}$. These two steps are repeated iteratively for the current input $\mathbf{x}_{k}$ until there is evidence that the current $\mathbf{D}^{\ast}$ matrix is close enough to the ground truth derivative matrix, $\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}$.

This procedure is applied to all inputs in the sequence, interleaving updates to the $\mathbf{D}^{\ast}$ and $\hat{\Delta ⁢\mathbf{F}}$ matrices on-the-fly. Detailed steps are presented in the sections below.

### V-B Algorithm Explanation

Our approach begins at Algorithm 1, which outputs a cache object. This cache object holds key data that will be utilized during runtime, such as the tangent matrix, $\Delta\mathbf{X}$ (initialized in Algorithm 2) and the web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$. Algorithm 1 serves as a one-time preprocessing step, with no part of this subroutine being re-executed at runtime.

The runtime component of our algorithm is detailed in Algorithm 3. This subroutine takes as input the function to be differentiated, $f$, the current input at which the derivative will be approximated, $\mathbf{x}_{k}$, the number of function inputs, $n$, a cache object generated by Algorithm 1, and two distance threshold values, $d_{\theta}$ and $d_{\ell}$. This algorithm consists of five main steps:

### V-B1 Ground-truth JVP computation (Alg. 3, lines 4--5)

A ground truth JVP, $\Delta\mathbf{f}_{i}$, is computed in the direction $\Delta\mathbf{x}_{i}$ at the given input $\mathbf{x}_{k}$ using Equation 4.

Figure 2: (a) The web of affine spaces, encoded as the columns of the $\hat{\Delta ⁢\mathbf{F}}$ matrix, start an iteration as intersecting at the previously computed derivative solution, D*⊤. (b) When a ground truth directional derivative is computed (Δf1 in this case), the affine space associated with its tangent direction (Δx1 in this case) is shifted away from the other affine spaces. This affine space, illustrated as a purple line, is guaranteed to contain the transpose of the ground truth derivative at the current input. (c) The constrained optimization step locates the point on the solution space that is closest (in terms of Euclidean distance) to the web of other affine spaces. (d) This point is the transpose of the approximate derivative at the current input, and the web of affine spaces (via the $\hat{\Delta ⁢\mathbf{F}}$ matrix) is updated such that they now intersect at this new point. The space is now ready for either another iteration of the algorithm on the same input, if needed, or the next input in the sequence, xk + 1.

### V-B2 Error detection and correction (Alg. 3, lines 6--9 & 17--18)

Error detection involves comparing the current approximation of the $i$-th JVP, ${\hat{\Delta ⁢\mathbf{f}}}_{i}$, with the just computed ground-truth JVP, $\Delta\mathbf{f}_{i}$. These vectors are compared using Algorithm 4. Specifically, this subroutine checks whether the angle and norm between the two vectors are below specified threshold values, $d_{\theta}$ and $d_{\ell}$, respectively. If this subroutine returns True, it indicates that $\hat{\Delta ⁢\mathbf{f}_{i}}$ aligns closely in direction and magnitude with $\Delta\mathbf{f}_{i}$, suggesting that the approximate derivative used to compute ${\hat{\Delta ⁢\mathbf{f}}}_{i}$ is likely a good approximation of the ground-truth derivative. Conversely, if this subroutine returns False, the current approximate derivative must not match the true derivative, and another iteration of the algorithm is taken on the same input $\mathbf{x}_{k}$. This loop continues until the approximate JVP is deemed close enough to the ground truth JVP (lines 17--18).

### V-B3 Ground-truth JVP update (Alg. 3, line 10)

Prior to line 10 in Algorithm 3, the $\hat{\Delta ⁢\mathbf{F}}$ matrix satifies the equation ${\mathbf{D}^{\ast}\Delta\mathbf{X}} = \hat{\Delta ⁢\mathbf{F}}$, where $\mathbf{D}^{\ast}$ here is the most recently computed approximate derivative. In other words, recalling §IV-B, the affine spaces ${{({\Delta\mathbf{x}_{j}^{\top}})}^{\dagger}{\hat{\Delta ⁢\mathbf{f}_{j}}}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{j}^{\top}}\mathbf{Y}}$ for all $j \in {\{ 1,\ldots,n\}}$ (where $\mathbf{Z}_{\Delta\mathbf{x}_{j}^{\top}}$ is the null-space matrix of the $1 \times n$ matrix $\Delta\mathbf{x}_{j}^{\top}$) only intersect at a single point: the transpose of the previously computed solution $\mathbf{D}^{\ast \top}$, illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")a.

After the current approximation of the $i$-th JVP, ${\hat{\Delta ⁢\mathbf{f}}}_{i}$, is compared with the just computed ground-truth JVP, $\Delta\mathbf{f}_{i}$, the ground truth can now replace the approximation in the web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$. This effectively shifts the affine space associated with the $i$-th JVP, leaving the other $n - 1$ affine spaces still intersecting at the previous solution $\mathbf{D}^{\ast \top}$. This shift is illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")b.

### V-B4 Optimization (Alg. 3, lines 10--14)

Line 14 reflects the mathematical procedure specified in Equation 15. This process locates the point on the affine space ${{({\Delta\mathbf{x}_{i}^{\top}})}^{\dagger}\Delta\mathbf{f}_{i}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{i}^{\top}}\mathbf{Y}}$ that is closest (in terms of Euclidean distance) to the other $n - 1$ affine spaces that are still intersecting at the previous solution, illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")c. Cached matrices $\mathbf{C}_{1}$ and $\mathbf{C}_{2}$ are used to speed up this result without needing to compute matrix inverses at runtime. The output from this step is a new matrix $\mathbf{D}^{\ast \top}$.

### V-B5 Web of affine spaces matrix update (Alg. 3 line 15)

The web of affine spaces matrix is updated such that ${\mathbf{D}^{\ast}\Delta\mathbf{X}} = \hat{\Delta ⁢\mathbf{F}}$. After this update, the affine spaces within $\hat{\Delta ⁢\mathbf{F}}$ will all intersect again at the just computed $\mathbf{D}^{\ast \top}$, illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")d. The matrix is now ready for either another iteration of the algorithm on the same input, if needed, or the next input in the sequence, $\mathbf{x}_{k + 1}$.

### V-C Initializing and Updating Matrices

Two key components of our approach are the tangent matrix, $\Delta\mathbf{X}$, and the web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$. The tangent matrix is initialized in Algorithm 2, where it is specifically constructed as a random orthonormal matrix, meaning its columns have unit length and are mutually orthogonal. For interested readers, we provide full analysis and rationale for this structure in the Appendix §X-B. To generate a random orthonormal matrix, we apply singular value decomposition (SVD) to a uniformly sampled random $n \times n$ matrix.

The web of affine spaces matrix is initialized as a zero matrix in algorithm 1. This matrix will dynamically update through the error detection and correction mechanism as needed. For instance, on the first call to Algorithm 3, the close_enough function will almost surely return $False$ for several iterations, allowing the matrix to progressively improve in accuracy over these updates.

### V-D Run-time Analysis

In this section, we analyze the run-time of our approach compared to alternatives. We will use the notation $\text{rt}{(.)}$ to denote the run-time of a subroutine. Approximate runtimes for several algorithms can be seen in Table I.

For WASP, $\mathbf{P}\mathbf{Q}$ and $\mathbf{R}\mathbf{S}$ are the matrix multiplications in Equation 15 (after preprocessing) and $q$ is the number of iterations needed to achieve sufficient accuracy. In many cases, $q = 1$, though note that even in the worst case, it is guaranteed that $q \leq n$ because when $k = n$, all columns in $\hat{\Delta ⁢\mathbf{F}}$ will be ground-truth JVPs.

Comparing to other approaches, we see that WASP shifts the computational burden of scaling $m$ and $n$ to matrix multiplications rather than repeated forward or reverse calls to $f$. This adjustment is expected to yield run-time improvements when ${\text{rt}{(f)}} > {{\text{rt}{({\mathbf{P}\mathbf{Q}})}} + {\text{rt}{({\mathbf{R}\mathbf{S}})}}}$, particularly when a low value of $q$ is achievable due to a sequence of closely related inputs. rt(f) + q [rt(f) + rt(⏟PRn ×n⏟QRn ×m) +rt(⏟RRn ×1⏟SR1 ×m)] rt(build_computation_graph(f)) +m ⋅rt(reverse(f)) TABLE I: Approximate run-times for derivative computation approaches

## Evaluation 1: Comparison on Benchmark Function

In Evaluation 1, we compare our approach to several other derivative computation approaches on a benchmark function.

### VI-A Procedure

Evaluation 1 follows a three step procedure: The benchmark function shown in Algorithm 5 in initialized with given parameters $n$, $m$, and $o$. This function will remain fixed and deterministic through the remaining steps; a random walk trajectory is generated following the process seen in Algorithm 6 with a given number of waypoints ($w$), dimensionality ($n$), and step length ($\lambda$); For all conditions, derivatives of the benchmark function are computed in order on the $w$ inputs in the random walk trajectory. This trajectory is kept fixed for all conditions. Metrics are recorded for all conditions.

The benchmark function used in this experiment is a randomly generated composition of sine and cosine functions. This function, detailed in Algorithm 5, was designed to be highly parameterizable, allowing for any number of inputs ($n$), outputs ($m$), and operations per output ($o$). Sine and cosine were selected for their smooth derivatives and composability, given their infinite domain and bounded range. Moreover, numerous subroutines in robotics and related fields involve many compositions of sine and cosine functions, making this function a reasonable analogue of these processes.

Evaluation 1 is divided into several sub-experiments, detailed below. Each sub-experiment varies which parameters of the procedure are allowed to change or remain fixed, aiming to assess different facets of the differentiation process.

3 r ← random list of o + 1 integers between 1 and n 4 s ← random list of o integers, either 1 or 2 8 tmp = sin (cos (tmp) + x[r[j + 1]]) 10 tmp = cos (sin (tmp) + x[r[j + 1]]) ${out}\overset{+}{\leftarrow}{tmp}$ // append to output 2x ← random sample from ℝn v ← random sample from ℝn // random direction $\mathbf{v}\leftarrow\frac{\mathbf{v}}{\left\| \mathbf{v} \right\|}$ // normalize the direction x ← x + λv // take a λ-length step in x direction ${out}\overset{+}{\leftarrow}\mathbf{x}$ // add state to output list Algorithm 6 get_random_walk(w, n, λ)

### VI-B Conditions

Evaluation 1 compares five conditions: Reverse-mode automatic differentiation with PyTorch backend (abbreviated as RAD-PyTorch) Finite-differencing with NumPy backend (abbreviated as FD) Simultaneous Perturbation Stochastic Approximation with NumPy backend (abbreviated as SPSA) Web of Affine Spaces Optimization with orthonormal $\Delta\mathbf{X}$ matrix and NumPy backend (abbreviated as WASP-O).

Web of Affine Spaces Optimization with random, non-orthonormal $\Delta\mathbf{X}$ matrix and NumPy backend (abbreviated as WASP-NO).

All conditions in this section are implemented in Python and executed on a Desktop computer with an Intel i9 4.4GHz processor and 32 GB of RAM. To ensure a fair comparison, the underlying benchmark function code remained consistent across all conditions, with backend switching managed via Tensorly^11^1 The conditions in this section were required to remain fully compatible with the given benchmark function implemented in Tensorly, without any modifications, optimizations, or code adjustments specific to individual conditions.

We note that JAX, a widely-used automatic differentiation library, is not included in this section. Although JAX is theoretically compatible with Tensorly, we found that extensive code modifications were required to enable optimal performance through just-in-time (JIT) compilation. Preliminary tests showed that JAX, when not JIT-compiled, exhibited run-times that were unreasonably slow and did not reflect its full potential. Therefore, we chose not to report non-JIT-compiled JAX results in this section.

For readers interested in further insights, supplementary results are provided in the Appendix (§X-C). These results relax the Tensorly-based uniformity constraints, allowing modifications, optimizations, and compilations to strive for maximum possible performance. Conditions in this supplemental section include JAX implementations compiled for both CPU and GPU, as well as Rust-based implementations.

### VI-C Metrics

We record and report on three metrics in Evaluation 1: Average runtime (in seconds) of derivative computation through the sequence of $w$ inputs.

Average number of calls to the benchmark function for a derivative computation through the sequence of $w$ inputs. Note that this value will be constant for all conditions aside from WASP.

Average accuracy of the derivative through the sequence of $w$ inputs. We measure accuracy as the sum of angular error (Algorithm 7) and norm error (Algorithm 8). The components of this error measure to what extent the rows of the returned derivative are facing the correct direction and have the correct magnitude, respectively. If this value is zero, the returned derivative exactly matches the ground-truth derivative. $\mathbf{r}\leftarrow\frac{\mathbf{D}_{\lbrack i,:\rbrack}}{\left\| \mathbf{D}_{\lbrack i,:\rbrack} \right\|}$ // normalized i-th row of ground-truth derivative $\hat{\mathbf{r}}\leftarrow\frac{\hat{\mathbf{D}_{\lbrack:,i\rbrack}}}{\left\| \hat{\mathbf{D}_{\lbrack i,:\rbrack}} \right\|}$ // normalized i-th row of approximate derivative $\theta\leftarrow{\arccos\left({\mathbf{r} \cdot \hat{\mathbf{r}}} \right)}$ // angle between vectors Algorithm 7 angular_error($\mathbf{D},\hat{\mathbf{D}}$) $a_{1}\leftarrow\frac{\left\| \mathbf{D}_{\lbrack i,:\rbrack} \right\|}{\left\| \hat{\mathbf{D}_{\lbrack i,:\rbrack}} \right\|}$ // norm ratio between the i-th rows of the ground truth and approximate derivative $a_{2}\leftarrow\frac{\left\| \hat{\mathbf{D}_{\lbrack i,:\rbrack}} \right\|}{\left\| \mathbf{D}_{\lbrack i,:\rbrack} \right\|}$ // norm ratio between the i-th rows of the ground truth and approximate derivative (other possible ordering) b2 ← |1 − a2| // distance from 1 (other possible ordering) 7 avg ← avg + min (b1, b2) Algorithm 8 norm_error($\mathbf{D},\hat{\mathbf{D}}$)

### VI-D Sub-experiment 1: Gradient Calculations

In sub-experiment 1, we run the procedure outlined in §VI-A with parameters, $m = 1$, $o = 1000$, $w = 100$, $\lambda = 0.05$, $d_{\theta} = 0.1$, $d_{\ell} = 0.1$, and $n = {\{ 1,50,100,150,\ldots,1000\}}$. Our goal in sub-experiment 1 is to observe how the different conditions scale as the number of function inputs $n$ grows while $m$ remains fixed at $1$. In other words, the benchmark function here is a scalar function and its derivative is a $1 \times n$ row-vector gradient.

Results for sub-experiment 1 can be seen in Figure 3 (top row). We observe that both WASP conditions outperform all other methods in runtime, except for SPSA, up to approximately $600$ inputs. Beyond this point, RAD-PyTorch. Additionally, the WASP conditions require orders of magnitude fewer function calls compared to FD, reflecting the goal of WASP to reuse recent information to avoid redundant calculation at the current input. While SPSA achieves the fastest runtime in sub-experiment 1, it incurs significant error. In contrast, the WASP conditions demonstrate much higher accuracy. Notably, the WASP condition utilizing the orthonormal tangent matrix structure maintains very low error, even for functions with up to 1000 inputs.

Figure 3: Results for Evaluation 1, Sub-Experiment 1 (top) Sub-Experiment 2 (middle) and Sub-Experiment 3 (bottom)

### VI-E Sub-experiment 2: Square Jacobian Calculations

In sub-experiment 2, we run the procedure outlined in §VI-A with parameters ${(n,m)} = {(x,x)}$ where $x \in {\{ 1,10,20,30,40,50\}}$, $o = 1000$, $w = 100$, $\lambda = 0.05$, $d_{\theta} = 0.1$, and $d_{\ell} = 0.1$. Our goal in sub-experiment 2 is to observe how the different conditions scale as the number of function inputs and number of function outputs both grow. Thus, the benchmark function here is a vector function with the same number of inputs and outputs, and its derivative is an $n \times n$ square Jacobian.

Results for sub-experiment 2 can be seen in Figure 3 (middle row). The WASP conditions demonstrate greater efficiency compared to RAD-PyTorch and FD, achieving a runtime comparable to SPSA. This efficiency advantage is likely primarily due to the lower number of function calls, as seen in the middle graph. Notably, WASP exhibits much lower error than SPSA, particularly in the variant incorporating the orthonormal matrix structure. This demonstrates that WASP more accurately approximates ground-truth Jacobian matrices.

### VI-F Sub-experiment 3: Varying step size

In sub-experiment 3, we run the procedure outlined in §VI-A with parameters, $n = 10$, $m = 10$, $o = 1000$, $w = 100$, $d_{\theta} = 0.1$, $d_{\ell} = 0.1$, and $\lambda = {\{ 0.001,0.01,0.1,1,10\}}$. Our goal in sub-experiment 3 is to observe how the different conditions scale as the step-length in the random walk trajectory grows.

Results for sub-experiment 3 can be seen in Figure 3 (bottom row). As expected, the performance of the WASP conditions generally declines as the step length increases. However, interestingly for a step length of $\lambda = 10$, the results show that the error approaches nearly zero, seemingly outperforming the trials with $\lambda = 1$ in terms of accuracy. This improved accuracy, however, comes at the cost of significantly more function calls, resulting in a much higher average runtime. Essentially, a step length of $\lambda = 10$ in this case was so large that the error detection and correction mechanism consistently triggered additional iterations until reaching the upper limit ($n$). As a result, the WASP conditions effectively defaulted to a standard finite-differencing strategy, hence why the WASP conditions are equivalent to the FD condition in terms of runtime and number of function calls in this scenario.

## Evaluation 2: Error Propagation Analysis

In §V-B, we described the error detection and correction mechanism in our algorithm, which is designed to prevent error accumulation over a sequence of approximate derivative computations. In Evaluation 2, we analyze how errors propagate through our algorithm under different parameter settings, thereby evaluating the effectiveness of our proposed mechanism over long derivative sequences.

Figure 4: Results for Evaluation 2. These results show the norm error (first row), angular error (second row), the number of function calls (third row), and runtime (fourth row) per derivative computation over a sequence of 50,000 derivatives (x-axis).

### VII-A Procedure

Evaluation 2 follows the same procedure as Evaluation 1, described in §VI-A. We use parameters $n = 50$, $m = 1$, $o = 1000$, $w = {50,000}$, $\lambda = 0.05$, where $n$ is the number of inputs to the benchmark function, $m$ is the number of outputs from the benchmark function, $o$ is the number of operations per output in the benchmark function, $w$ is the number of waypoints in the random walk trajectory, and $\lambda$ is the step length along the random walk trajectory.

### VII-B Conditions

The primary values we are varying and assessing in Evaluation 2 are the error threshold parameters, $d_{\theta}$ and $d_{\ell}$, outlined in §V-B. Specifically, we use parameter settings ${(d_{\theta},d_{\ell})} = {(x,x)}$ where $x \in {\{ 0.001,0.01,0.1,0.25,0.5,0.75,1.0\}}$. These settings allow us to evaluate error behavior across different error thresholds (the $d_{\theta}$ and $d_{\ell}$ parameters) over a long input sequence (as specified by the $w$ parameter above).

The WASP method in this evaluation uses a fixed orthonormal $\Delta\mathbf{X}$ matrix shared across all $d_{\theta}$ and $d_{\ell}$ configurations. We also compare the WASP variants against standard Finite Differencing using a NumPy backend.

All conditions in Evaluation 2 are implemented in Python using Tensorly for backend switching and executed on a Desktop computer with an Intel i7 5.4GHz processor and 32 GB of RAM.

### VII-C Metrics

We record and report on four metrics in Evaluation 2: Runtime (in seconds) per each derivative computation through the sequence of $w$ inputs.

Number of calls to the benchmark function for each derivative computation through the sequence of $w$ inputs.

The angular error of each derivative through the sequence of $w$ inputs (Algorithm 7).

The norm error of each derivative through the sequence of $w$ inputs (Algorithm 8).

### VII-D Results

Results for Eavluation 2 are shown in Figure 4. At a high level, we observe that WASP does not accumulate significant error over long sequences, even when high error thresholds are used. For instance, even at the $50,000$-th input, the errors remain low. In general, there are subtle ebbs and flows in error, naturally requiring more or fewer function calls throughout the sequence. At certain points, such as between the $13,000$-th and $15,000$-th inputs, WASP exhibits a transient increase in error under high thresholds, suggesting that this portion of the input sequence is less compatible with the WASP heuristic. However, even in these cases, the error remains within reasonable and usable bounds (e.g., less than $0.4$ radians from the ground truth gradient), and the algorithm successfully self-corrects after these brief periods of elevated error without diverging. As expected, using lower error thresholds consistently results in low error, but at the cost of additional function calls and runtime. In the limit as $d_{\theta}$ and $d_{\ell}$ approach $0$, both the accuracy and runtime performance converge to that of full finite differencing.

## Evaluation 3: Application in Robot Optimization

In Evaluation 3, we compare our approach to several other derivative computation approaches in a robotics-based root-finding procedure.

Figure 5: Evaluation 3 involves assessing performance in a robotic root-finding procedure, where the goal is to determine a robot pose that positions its feet and end-effector at predefined locations or orientations.

### VIII-A Procedure

Evaluation 3 follows a three step procedure: A robot state is sampled for a simulated Unitree B1 quadruped robot^22^2 with a Z1 manipulator^33^3 mounted on its back (shown in Figure 5). This robot has 24 degrees of freedom (including a floating base to account for mobility). This sampled state, $\mathbf{x}_{0} \in {\mathbb{R}}^{24}$, will be an initial condition for an optimization process; A Jacobian pseudo-inverse method (Algorithm 9) is used to find a root for a constraint function (Algorithm 10). The constraint function has five outputs: four for specifying foot placements and one for specifying the end-effector pose for the manipulator mounted on the back. Thus, the Jacobian of this constraint function is a $5 \times 24$ matrix; Step 1--2 are run 50 times per condition. Metrics are recorded for all conditions. x ← x0 // set state to be given initial condition y ← f(x) // initialize residuals. The goal is for this vector to be all zeros (at a root) 4for i ∈ 0..max iterations do ${\Delta\mathbf{x}}\leftarrow{\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}}^{\dagger}\mathbf{y}}$ // Compute direction using Jacobian matrix pseudoinverse x ← x − ϵΔx // take a step in the Δx direction. We use a value of ϵ = 0.01 return x // If the residual is small, the optimization has converged and the result should be returned. In practice, we use a value of γ = 0.01 Algorithm 9 root_finding(f, x0) l ← fk(x) // forward kinematics on given robot state. Returns an ordered list of SE poses for all robot links. ${ee\_ pose\_ goal}\leftarrow{\text{se3\_matrix}\left(\begin{bmatrix} \end{bmatrix}^{\top},\begin{bmatrix} \end{bmatrix}^{\top} \right)}$ // the SE end-effector pose goal for the back-mounted robot arm. The arguments here are translation then Euler angle parameters, thus the pose goal has no added rotation. $\left. t_{1}\leftarrow \middle| \middle| l\lbrack 10\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for front left foot placement $\left. t_{2}\leftarrow \middle| \middle| l\lbrack 17\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for front right foot placement $\left. t_{3}\leftarrow \middle| \middle| l\lbrack 24\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for back left foot placement $\left. t_{4}\leftarrow \middle| \middle| l\lbrack 31\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for back right foot placement t5 ← ∥ln(l−1 ⋅ ee_pose_goal)∥2 // the ln here is the logarithm map for the SE Lie group; it maps to the 𝔰𝔢 Lie algebra. return $\begin{bmatrix} \end{bmatrix}^{\top}$ // return a 5-vector of all the terms squared Algorithm 10 robot_constraint_function(x)

### VIII-B Conditions

The conditions in Evaluation 3 are the same as those listed in §VI-B. All conditions are implemented in Python and executed on a Desktop computer with an Intel i7 5.4GHz processor and 32 GB of RAM. Only the CPU was used for these experiments and Tensorly was again used for all backend-switching to maintain uniformity.

### VIII-C Metrics

We record and report on two metrics in Evaluation 3: Average runtime (in seconds) to converge on a robot configuration sufficiently close to the constraint surface.

Average number of optimization steps needed to converge on a robot configuration sufficiently close to the constraint surface.

### VIII-D Results

Results for Evaluation 3 can be seen in Table II. The results show that the WASP conditions achieve significantly faster convergence compared to alternative approaches. Additionally, the orthonormal structure of the tangent matrix further enhances convergence efficiency. In contrast, the SPSA condition failed to converge, highlighting that certain derivative approximation methods may lack the accuracy required for some optimization procedures.

Average runtime (seconds) TABLE II: Evaluation 3 results. The ∗ symbol means that the condition never converged in the maximum number of iterations. Range values denote standard deviation.

## Discussion

In this work, we introduced a coherence-based approach for efficiently calculating a sequence of derivatives. Our approach leverages a novel process, the Web of Affine Spaces (WASP) Optimization, to identify a point guaranteed to reside on an affine space containing the ground-truth derivative that also aligns well with prior related calculations. Through extensive evaluations, we demonstrate that our approach outperforms widely used techniques such as automatic differentiation and finite differencing in terms of efficiency, while delivering greater accuracy compared to other derivative approximation methods. In this section, we discuss the limitations and broader implications of our approach.

### IX-A Limitations

We note several limitations of our work that suggest future avenues of research and extensions. First, the derivatives produced by our approach are approximations. Although our method can, in theory, achieve high accuracy comparable to standard finite differencing, attaining such precision would necessitate additional iterations, likely compromising its efficiency. For applications demanding exact derivatives in all cases, alternative techniques may be more appropriate.

Next, this paper focuses on presenting the math, algorithms, and initial proofs of concept for the WASP derivative approach. While we believe this technique has potential for impact across robotics and other fields, exploring its full range of applications and establishing best practices across many different problems is beyond the scope of this paper.

Furthermore, as demonstrated in Evaluation 1, the effectiveness of our approach diminishes significantly as the gap between inputs increases. We aim to refine or reformulate aspects of our approach going forward to reduce its strong sensitivity to step size.

Additionally, while our error detection and correction technique performs well in practice, it does not guarantee the accuracy of the approximations relative to ground-truth derivatives. Currently, the approach relies on JVPs (directional derivatives) as a proxy for true derivatives. While this provides a necessary condition for correctness, it is not a sufficient condition. In other words, the true derivative will always yield matching directional derivatives, but matching directional derivatives do not necessarily guarantee the underlying derivatives are correct. Ideally, the error detection and correction mechanism, along with its associated parameters, would relate directly to the true derivatives. However, addressing this issue is inherently challenging and perhaps infeasible. To illustrate, such a solution seems to elicit a circular reasoning problem: if one could sufficiently estimate the ground-truth derivative well enough to bound the approximation, that same information could be used to directly select a closer approximation to the true derivative in the first place. This issue remains an open question that requires further investigation.

Lastly, while the current approach performs well for small to medium-sized problems, it does not scale effectively to large-scale functions. For example, applying this method to neural network training with millions or billions of parameters would be infeasible due to the prohibitive size of the matrices required for the optimization process. In future work, we plan to explore scalable adaptations of this approach that better manage storage and computational demands.

### IX-B Implications

Due to the ubiquity of derivative computation in robotics and beyond, we believe our work has the potential for broad impact and applicability. For example, it could prove to be valuable in areas such as model predictive control, physics simulation, trajectory optimization, inverse kinematics, and more. Our goal is to enable the community to leverage these derivatives to streamline computationally expensive subroutines, achieving performance gains with minimal code modifications. By doing so, we aim to unlock new levels of interactivity and adaptability for robots, empowering them to operate seamlessly and responsively in real-time environments.
