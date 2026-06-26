<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Computing derivatives is a crucial subroutine in computer science and related fields as it provides a local characterization of a function's steepest directions of ascent or descent. In this work, we recognize that derivatives are often not computed in isolation; conversely, it is quite common to compute a \textit{sequence} of derivatives, each one somewhat related to the last. Thus, we propose accelerating derivative computation by reusing information from previous, related calculations-a general strategy known as \textit{coherence}. We introduce the first instantiation of this strategy through a novel approach called the Web of Affine Spaces (WASP) Optimization. This approach provides an accurate approximation of a function's derivative object (i.e. gradient, Jacobian matrix, etc.) at the current input within a sequence. Each derivative within the sequence only requires a small number of forward passes through the function (typically two), regardless of the number of function inputs and outputs. We demonstrate the efficacy of our approach through several numerical experiments, comparing it with alternative derivative computation methods on benchmark functions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that our method significantly improves the performance of derivative computation on small to medium-sized functions, i.e., functions with approximately fewer than 500 combined inputs and outputs. Furthermore, we show that this method can be effectively applied in a robotics optimization context. We conclude with a discussion of the limitations and implications of our work. Open-source code, visual explanations, and videos are located at the paper website: \href{

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mathematical derivatives are fundamental to much of science. At a high level, derivatives offer a local characterization of a function's steepest ascent or descent directions. In practice, this property is frequently employed in numerical optimization, where derivatives guide the iterative process of navigating downhill through the landscape of a function. For example, derivative-based optimization is widely used in robotics for tasks such as inverse kinematics, trajectory optimization, physics simulation, control, learning, and constrained planning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since derivative computation often takes place within a tight, low-level loop in the application stack, the speed of this process is critical to maintaining sufficient performance. For example, consider a legged robot using a derivative-based model predictive control (MPC) algorithm to maintain balance. If the robot is nudged, it must compute derivatives very rapidly to guide the optimization process and allow the real-time reactive actuations of its legs to stay upright.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As we will discuss in §II, there are several standard techniques to calculate the derivatives of a function. These techniques generally involve repeatedly evaluating the function with slightly modified arguments, observing the resulting perturbations in the function's input or output space, and constructing the derivative from these observations. However, since the number of function evaluations required typically scales with the number of inputs or outputs of the function, these approaches can quickly become prohibitively expensive when either, or especially both, of these dimensions increase.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we recognize that derivatives are often not computed in isolation; conversely, it is quite common to calculate a sequence of derivatives, each one building on the last. For example, in optimization, function inputs typically change only slightly between iterations as small steps are taken downhill, with each input incrementally leading to the next. The key insight of this work is that derivative computation can be accelerated by reusing information from previous, related calculations---a strategy known as coherence.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a first instantiation of this coherence-based strategy for derivative computation through a novel approach called the Web of Affine Spaces (WASP) Optimization. At its core, this approach frames derivative computation as a constrained least-squares minimization problem. Each iteration of the algorithm requires only one Jacobian-vector product (JVP) which creates an affine space within which the true derivative is guaranteed to lie. The optimization is then tasked with finding the transpose of an approximate derivative that lies on this affine space (specified by a hard constraint) while best aligning with previous, related computations (specified in the objective function). This process is illustrated in Figure 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a closed-form solution to this minimization problem by directly solving its corresponding Karush-Kuhn-Tucker (KKT) system. Our algorithm that uses this minimization also incorporates an error detection and correction mechanism that automatically identifies when its outputs drift too far from the ground-truth derivatives, allocating additional iterations to realign its results as needed. This mechanism is guided by two user-adjustable parameters, affording a flexible balance between accuracy and computational performance tailored to specific applications.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The algorithm associated with our approach (§V) is straightforward to implement and can be easily interfaced with existing code. The algorithm does not require tape-based variable tracking or an external automatic differentiation library; it simply uses standard forward passes through a function. All ideas presented in this work can be implemented in less than 100 lines of code in any programming language that supports numerical computing.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of our approach through a series of numerical experiments, benchmarking it against alternative derivative computation methods. We show that our approach improves the performance of computing a sequence of derivatives on small to medium-sized functions, i.e., functions with approximately fewer than 500 combined inputs and outputs. Additionally, we demonstrate its practical applicability in a robotics optimization context, showcasing its use in a Jacobian-pseudoinverse-based root-finding procedure to determine the pose of a quadruped robot with specified foot and end-effector placements. We conclude with a discussion of the limitations and implications of our work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Notation", "weight": 1.0} -->

The main mathematical building blocks through this work are matrices and vectors. Matrices will be denoted with bold upper case letters, e.g., $\mathbf{A}$, and vectors will be denoted with bold lower case letters, e.g., $\mathbf{x}$. Indexing into matrices or vectors will use sub-brackets, e.g., $\mathbf{A}_{\lbrack 0,1\rbrack}$ or $\mathbf{x}_{\lbrack 2\rbrack}$. A full row or column of a matrix can be referenced using a colon, e.g., $\mathbf{A}_{\lbrack:,0\rbrack}$ is the first column and $\mathbf{A}_{\lbrack 0,:\rbrack}$ is the first row.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Problem Setup", "weight": 1.0} -->

In this work, we will refer to some function under consideration as $f$, which has $n$ inputs and $m$ outputs, i.e., $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$. We will also assume that the given function $f$ is computable and differentiable.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Problem Setup", "weight": 1.0} -->

The mathematical object we are trying to compute is the derivative object of $f$ at a given input $\mathbf{x}_{k} \in {\mathbb{R}}^{n}$, denoted as $\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}$. This derivative will be an $m \times n$ matrix, i.e., $\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}} \in {\mathbb{R}}^{m \times n}$, with the following structure: This matrix is referred to as a Jacobian, or specifically as a gradient when $m = 1$. Throughout this work, however, we will consistently use the broader term, derivative.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Problem Statement", "weight": 1.0} -->

In this work, we are specifically looking to compute a sequence of approximate derivative matrices: Our goal is to compute these approximate derivatives as quickly and as accurately as possible. We assume that the derivative computation at an input $\mathbf{x}_{k}$ can utilize knowledge of all prior inputs and calculations (i.e., information available up to and including $k$), but it has no access to information about future inputs (i.e., data beyond $k$).

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Problem Statement", "weight": 1.0} -->

There is an implicit assumption in our problem that adjacent inputs, e.g., $\mathbf{x}_{k}$ and $\mathbf{x}_{k + 1}$, are relatively "close", as is often the case in iterative optimization. However, our approach does not impose any specific requirement for the closeness of neighboring inputs. Instead, it is informally assumed that the approach will perform more effectively when the inputs are closer to each other with efficiency or accuracy likely diminishing as the distance between inputs increases.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-D Standard Derivative Computation Algorithms", "weight": 1.0} -->

A common strategy for computing derivatives involves introducing small perturbations in the input or output space surrounding the derivative and incrementally constructing the derivative matrix by analyzing the local behavior exhibited by the derivative in response to these perturbations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-D Standard Derivative Computation Algorithms", "weight": 1.0} -->

Specifically, perturbing the derivative in the input space looks like the following: The $\Delta\mathbf{x}$ object here is commonly called a tangent, and the resulting $\Delta\mathbf{f}$ is known as the Jacobian-vector product (JVP) or directional derivative. Conversely, perturbing the derivative in the output space looks like the following: The $\Delta\mathbf{f}^{\top}$ object here is commonly called an adjoint, and the result $\Delta\mathbf{x}^{\top}$ is known as the vector-Jacobian product (VJP).

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-D Standard Derivative Computation Algorithms", "weight": 1.0} -->

In general, there are two standard ways of computing JVPs: forward-mode automatic differentiation; and finite-differencing. Forward-mode automatic differentiation propagates tangent information alongside standard numerical computations. This technique commonly involves overloading floating-point operations to include additional tangent data. A JVP via first-order finite-differencing derives from the standard limit-based definition of a derivative: If $\epsilon$ is small, this approximation is close to the true JVP. Note that this JVP requires two forward passes through $f$, and additional JVPs at the same input $\mathbf{x}_{k}$ would only require one additional forward pass through $f$ each.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-D Standard Derivative Computation Algorithms", "weight": 1.0} -->

Conversely, there is generally only one way of computing a VJP: reverse-mode automatic differentiation, often called backpropagation in a machine-learning context. This process involves building a computation graph (or Wengert List ) on a forward pass, then doing a reverse pass over this computation graph to backward propagate adjoint information. In general, VJP-based differentiation is more challenging to implement and manage compared to its JVP-based counterpart. This approach typically requires an external library to track variables and operations, enabling the construction of a computation graph. As a result, all downstream computations within a function must adhere to the same code structure or use the same library.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-D Standard Derivative Computation Algorithms", "weight": 1.0} -->

Note that the concepts of JVPs and VJPs now give a clear strategy for isolating the whole derivative matrix. For instance, using "one-hot" vectors for tangents or adjoints, i.e., vectors where only the $i$-th element is $1$ and all others are $0$, can effectively capture the $i$-th column or $i$-th row of the derivative matrix, respectively. Thus, the derivative matrix can be fully recovered using $n$ JVPs or $m$ VJPs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-D Standard Derivative Computation Algorithms", "weight": 1.0} -->

In practice, a JVP-based approach is typically used if $n < m$ and a VJP-based approach is typically used if $m < n$. However, as either $m$ or $n$ increase -- or, especially if both increase -- these approaches can quickly become inefficient.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-E Other Related Works", "weight": 1.0} -->

Our work builds on previous methods aimed at accelerating derivative computations through approximations. For first-order derivatives, our approach is closest to Simultaneous Perturbation Stochastic Approximation (SPSA). SPSA, primarily used in optimization, estimates gradients using only two function evaluations by perturbing the function along one sampled direction. This idea has inspired more recent work that approximates a gradient via a bundle of stochastic samples at a point.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-E Other Related Works", "weight": 1.0} -->

Our approach also approximates derivatives by perturbing inputs in random directions and observing the output changes. Like SPSA (and related methods), it aims to achieve an approximate derivative with a small number forward passes through the function. However, we treat the random directions as a matrix in a least squares optimization, aligning the result with prior observations. Also, unlike previous methods that primarily focus on gradients, our approach handles derivative objects of any shape, including full Jacobian matrices.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-E Other Related Works", "weight": 1.0} -->

Interestingly, while coherence-based strategies have not been widely explored for first-order derivatives, they are frequently used in second-order derivative computations of scalar functions within optimization algorithms. For example, quasi-Newton methods like Davidon--Fletcher--Powell (DFP), Symmetric Rank 1 (SR1), and Broyden--Fletcher--Goldfarb--Shanno (BFGS) use the secant equation to iteratively build approximations of the Hessian matrix over a sequence of related inputs. However, these algorithms cannot compute gradients directly, as they rely on them as inputs. Through this lens, our current approach can be viewed as quite related to quasi-Newton methods for Hessian approximation, but specifically for first-order derivatives.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Technical Overview", "weight": 1.0} -->

In this section, we overview the central concepts and intuitions of our idea.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Differentiation as Linear System", "weight": 1.0} -->

As covered in §II, each pass through the function in JVP-based differentiation generates one JVP: ${\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}\Delta\mathbf{x}} = {\Delta\mathbf{f}}$. We can bundle several tangents together in a matrix in order to get a matrix of JVPs: Note that the $i$-th tangent vector and JVP are denoted as $\Delta\mathbf{x}_{i}$ and $\Delta\mathbf{f}_{i}$, respectively. We use this same notation throughout the paper. From Equation 6, we see that JVP-based differentiation can also be interpreted as setting $\Delta\mathbf{X}$ to be the identity matrix and "solving" a linear system: This concept is mathematically straight forward, but it is important to note that generating $\Delta\mathbf{F}$ can be computationally expensive as it requires $n$ forward passes through $f$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Differentiation as Linear System", "weight": 1.0} -->

Our idea builds on this linear system idea, with $\Delta\mathbf{X}$ no longer only being an identity matrix.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Differentiation as Least Squares Optimization", "weight": 1.0} -->

In the section above, we assessed the linear system ${\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}_{k}}\Delta\mathbf{X}} = {\Delta\mathbf{F}}$. If we take the transpose of both sides, we get the following: This equation now nicely matches a standard "${Ax} = b$" linear system, with "$x$" being an unknown matrix variable, in our case. We cast this linear system as a least squares optimization: Here, $\mathbf{D}^{\top}$ is the decision variable acting as the derivative matrix, and $F$ denotes the Frobenius norm over matrices. This formulation offers a clear analytical framework for considering general solutions, even when $\Delta\mathbf{X}$ is not a square or identity matrix. The closed-form solution for this optimization problem is the following: where the $\dagger$ symbol denotes the Moore-Penrose Pseudoinverse.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Differentiation as Least Squares Optimization", "weight": 1.0} -->

If $\Delta\mathbf{X}$ is full rank, $r \geq n$ (i.e., $\Delta\mathbf{X}^{\top}$ is square or tall), and $\Delta\mathbf{F}$ is a matrix of JVPs corresponding to the tangents in $\Delta\mathbf{X}$, this solution exactly matches the true derivative matrix. However, this solution has not yet improved efficiency since we would still have to compute $\Delta\mathbf{F}$, which was the most expensive step from before.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Differentiation as Least Squares Optimization", "weight": 1.0} -->

A key insight in this work is that $\Delta\mathbf{F}$ in the minimization above can be replaced with an approximation, $\hat{\Delta ⁢\mathbf{F}}$: Rather than fully recomputing $\Delta\mathbf{F}$ for each new input, we incrementally update $\hat{\Delta ⁢\mathbf{F}}$ across a sequence of inputs. Since $\hat{\Delta ⁢\mathbf{F}}$ is an approximation, the entire minimization process now becomes an approximation as well. Through the remainder of this work, we argue that, given an additional constraint on Equation 10 and a particular strategy for updating $\hat{\Delta ⁢\mathbf{F}}$, this approach is more efficient than standard approaches for computing a sequence of derivative matrices while maintaining accuracy sufficient for practical use.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Technical Details", "weight": 1.0} -->

In this section, we detail the Web of Affine of Spaces (WASP) Optimization approach for computing a sequence of approximate derivatives matrices.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Affine Solution Space", "weight": 1.0} -->

As discussed above, the bottleneck of Equation 8 is the calculation of $\Delta\mathbf{F}$, the matrix bundle consisting of $r$ JVPs, where $r \geq n$. Rather than relying solely on $r$ JVPs, we first think about how much information about the derivative solution can be inferred from only one JVP.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Affine Solution Space", "weight": 1.0} -->

Equation 11 defines an ${({n - 1})} \times m$-dimensional affine space encompassing all possible solutions, where $\mathbf{Z}_{\Delta\mathbf{x}^{\top}}\mathbf{Y}$ represents the associated vector space, and ${({\Delta\mathbf{x}^{\top}})}^{\dagger}\Delta\mathbf{f}^{\top}$ (the minimum-norm solution) serves as the offset from the origin. Even with just one JVP, we have captured a space where the true derivative must lie for some setting of $\mathbf{Y}$. Our idea, covered below, constrains the solution to lie within the space defined in Equation 11, while also maintaining alignment with recent computations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Web of Affine Spaces", "weight": 1.0} -->

In the previous section, we isolated a space where the true derivative must lie given only a single JVP. We now assess what happens if we consider more JVPs.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Web of Affine Spaces", "weight": 1.0} -->

Consider $r$ JVPs, $\Delta\mathbf{f}_{i}$, with corresponding tangents $\Delta\mathbf{x}_{i}$, where $i \in {1,\ldots,r}$. Each JVP defines its own affine solution space, within which the true derivative must reside: ${{({\Delta\mathbf{x}_{i}^{\top}})}^{\dagger}\Delta\mathbf{f}_{i}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{i}^{\top}}\mathbf{Y}}$. Knowing that the true derivative must lie within all of these affine spaces, we can deduce that it must be located at the intersection of these spaces. Indeed, when $r \geq n$, the intersection of all these spaces results in a single, unique matrix: the exact derivative. Essentially, this is precisely what the solution in Equation 9 achieves.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Web of Affine Spaces", "weight": 1.0} -->

We now return to the idea presented in Equation 10. What if some JVPs are approximate, $\hat{\Delta ⁢\mathbf{f}}$, rather than ground-truth, $\Delta\mathbf{f}$?

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Web of Affine Spaces", "weight": 1.0} -->

{\mathbf{Z}_{\Delta\mathbf{x}_{j}^{\top}}\mathbf{Y}}$. We refer to these approximate JVP affine spaces as the web of affine spaces.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C Web of Affine Spaces Optimization", "weight": 1.0} -->

In this section, we overview the mathematical side of the Web of Affine Spaces (WASP) Optimization. We specify the algorithmic details that instantiate this math in practice in §V.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Web of Affine Spaces Optimization", "weight": 1.0} -->

Suppose $\Delta\mathbf{X}$ is a full rank $n \times r$ matrix where $r \geq n$. We consider the columns of $\Delta\mathbf{X}$ to be $r$ separate tangent vectors where the $i$-th column is denoted as $\Delta\mathbf{x}_{i}$. Assume we have a current input, $\mathbf{x}_{k}$, a selected tangent vector, $\Delta\mathbf{x}_{i}$, and a JVP corresponding to $\mathbf{x}_{k}$ in the $\Delta\mathbf{x}_{i}$ direction, $\Delta\mathbf{f}_{i}$ (likely computed using Equation 4). Also, assume we have a web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Web of Affine Spaces Optimization", "weight": 1.0} -->

We cast the optimization described above as a modified version of Equation 10 with an added constraint: This constrained optimization best matches the intersection of the web of affine spaces, specified in the objective function, while also restricting the solution to lie on the affine solution space, specified in the constraint.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Web of Affine Spaces Optimization", "weight": 1.0} -->

The solution to Equation 12 is the following: This solution is derived using a Karush-Kuhn-Tucker (KKT) system, as seen in detail in §IV-D. Here, $\mathbf{D}^{\ast \top} \in {\mathbb{R}}^{n \times m}$ is the transpose of the approximate derivative matrix and $\mathbf{\Lambda}^{\ast \top} \in {\mathbb{R}}^{1 \times m}$ is a vector of Lagrange multipliers. We can rewrite the solution in Equation 13 by taking the block matrix inverse of the left matrix: Here, $s_{i}$ is the Schur Complement of the block matrix $\mathbf{A} = {2\Delta\mathbf{X}\Delta\mathbf{X}^{\top}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Web of Affine Spaces Optimization", "weight": 1.0} -->

Because we do not use the Lagrange multipliers in this work, we can use Equation 14 to more directly solve for $\mathbf{D}^{\ast \top}$: Here, $\mathbf{I}_{n \times n}$ is an $n \times n$ identity matrix, and $\mathbf{A}$ and $s$ can be found in Equation 14. For interested readers, we discuss the geometric significance of Equation 15 in the Appendix §X-A.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Web of Affine Spaces Optimization", "weight": 1.0} -->

Again, this section has only covered the mathematical procedure behind the Web of Affine Spaces Optimization. In §V, we overview our algorithm that utilizes this optimization, including how to initialize and update $\hat{\Delta ⁢\mathbf{F}}$, how to preprocess and cache parts of Equation 15 to accelerate the optimization at runtime, how to determine if $\mathbf{D}^{\ast \top}$ is an acceptable approximation, and how to achieve a more accurate result if the expected error is too high.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Derivation of Web of Affine Spaces Solution", "weight": 1.0} -->

In this section, we derive the solution specified in Equation 13. First, note that another way of writing the objective function ${\|{{\Delta\mathbf{X}^{\top}\mathbf{D}^{\top}} - {\hat{\Delta ⁢\mathbf{F}}}^{\top}}\|}_{F}^{2}$ is the following: where $tr$ is the matrix trace. We now multiply the terms within the trace function: Writing the whole optimization out in this form: we form the Lagrangian of the optimization: where $\mathbf{\Lambda} \in {\mathbb{R}}^{m \times 1}$ are the Lagrange multipliers.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Derivation of Web of Affine Spaces Solution", "weight": 1.0} -->

A first-order necessary condition for an optimal solution is that the Karush-Kuhn-Tucker (KKT) conditions are satisfied. Specifically, for an equality constrained problem, this means that the partial derivatives of the Lagrangian with respect to both the decision variables and the Lagrange multipliers (associated with the equality constraints) are zero: We start with the first requirement: We now set the term equal to zero: For the second requirement from the Lagrangian, $\frac{\partial\mathcal{L}}{\partial\mathbf{\Lambda}^{\top}} = 0$, we have the following: Putting the previous components together into a KKT system, we have the following matrix equation: Using the matrix inverse, our final solution is the following: matching the solution seen in Equation 13. $\square$

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Approximate Differentiation as Iterative Process", "weight": 1.0} -->

Our algorithm for computing approximate derivatives for a sequence of inputs ($\mathbf{x}_{k}$, $\mathbf{x}_{k + 1}$,...) is structured as an iterative process. This process centers around three matrices introduced in previous sections: $\mathbf{D}^{\ast}$, the current approximate derivative matrix; $\hat{\Delta ⁢\mathbf{F}}$, the current matrix of approximate JVPs; and $\Delta\mathbf{X}$, the matrix of tangents.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Approximate Differentiation as Iterative Process", "weight": 1.0} -->

Given an input in the sequence, $\mathbf{x}_{k}$, our algorithm aims to compute an approximate derivative at that input, $\left. \hat{\frac{\partial f}{\partial\mathbf{x}}} \right|_{\mathbf{x}_{k}}$. The process begins by using the $\Delta\mathbf{X}$ matrix and current $\hat{\Delta ⁢\mathbf{F}}$ matrix to compute an updated version of $\mathbf{D}^{\ast}$. Subsequently, the new $\mathbf{D}^{\ast}$ matrix is used to update $\hat{\Delta ⁢\mathbf{F}}$. These two steps are repeated iteratively for the current input $\mathbf{x}_{k}$ until there is evidence that the current $\mathbf{D}^{\ast}$ matrix is close enough to the ground truth derivative matrix, $\left.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Approximate Differentiation as Iterative Process", "weight": 1.0} -->

This procedure is applied to all inputs in the sequence, interleaving updates to the $\mathbf{D}^{\ast}$ and $\hat{\Delta ⁢\mathbf{F}}$ matrices on-the-fly. Detailed steps are presented in the sections below.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Algorithm Explanation", "weight": 1.0} -->

Our approach begins at Algorithm 1, which outputs a cache object. This cache object holds key data that will be utilized during runtime, such as the tangent matrix, $\Delta\mathbf{X}$ (initialized in Algorithm 2) and the web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$. Algorithm 1 serves as a one-time preprocessing step, with no part of this subroutine being re-executed at runtime.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Algorithm Explanation", "weight": 1.0} -->

The runtime component of our algorithm is detailed in Algorithm 3. This subroutine takes as input the function to be differentiated, $f$, the current input at which the derivative will be approximated, $\mathbf{x}_{k}$, the number of function inputs, $n$, a cache object generated by Algorithm 1, and two distance threshold values, $d_{\theta}$ and $d_{\ell}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B1 Ground-truth JVP computation (Alg. 3, lines 4--5)", "weight": 1.0} -->

A ground truth JVP, $\Delta\mathbf{f}_{i}$, is computed in the direction $\Delta\mathbf{x}_{i}$ at the given input $\mathbf{x}_{k}$ using Equation 4.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B2 Error detection and correction (Alg. 3, lines 6--9 & 17--18)", "weight": 1.0} -->

Error detection involves comparing the current approximation of the $i$-th JVP, ${\hat{\Delta ⁢\mathbf{f}}}_{i}$, with the just computed ground-truth JVP, $\Delta\mathbf{f}_{i}$. These vectors are compared using Algorithm 4. Specifically, this subroutine checks whether the angle and norm between the two vectors are below specified threshold values, $d_{\theta}$ and $d_{\ell}$, respectively. If this subroutine returns True, it indicates that $\hat{\Delta ⁢\mathbf{f}_{i}}$ aligns closely in direction and magnitude with $\Delta\mathbf{f}_{i}$, suggesting that the approximate derivative used to compute ${\hat{\Delta ⁢\mathbf{f}}}_{i}$ is likely a good approximation of the ground-truth derivative. Conversely, if this subroutine returns False, the current approximate derivative must not match the true derivative, and another iteration of the algorithm is taken on the same input $\mathbf{x}_{k}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B2 Error detection and correction (Alg. 3, lines 6--9 & 17--18)", "weight": 1.0} -->

This loop continues until the approximate JVP is deemed close enough to the ground truth JVP (lines 17--18).

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B3 Ground-truth JVP update (Alg. 3, line 10)", "weight": 1.0} -->

Prior to line 10 in Algorithm 3, the $\hat{\Delta ⁢\mathbf{F}}$ matrix satifies the equation ${\mathbf{D}^{\ast}\Delta\mathbf{X}} = \hat{\Delta ⁢\mathbf{F}}$, where $\mathbf{D}^{\ast}$ here is the most recently computed approximate derivative.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B3 Ground-truth JVP update (Alg. 3, line 10)", "weight": 1.0} -->

In other words, recalling §IV-B, the affine spaces ${{({\Delta\mathbf{x}_{j}^{\top}})}^{\dagger}{\hat{\Delta ⁢\mathbf{f}_{j}}}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{j}^{\top}}\mathbf{Y}}$ for all $j \in {\{ 1,\ldots,n\}}$ (where $\mathbf{Z}_{\Delta\mathbf{x}_{j}^{\top}}$ is the null-space matrix of the $1 \times n$ matrix $\Delta\mathbf{x}_{j}^{\top}$) only intersect at a single point: the transpose of the previously computed solution $\mathbf{D}^{\ast \top}$, illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B3 Ground-truth JVP update (Alg. 3, line 10)", "weight": 1.0} -->

After the current approximation of the $i$-th JVP, ${\hat{\Delta ⁢\mathbf{f}}}_{i}$, is compared with the just computed ground-truth JVP, $\Delta\mathbf{f}_{i}$, the ground truth can now replace the approximation in the web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$. This effectively shifts the affine space associated with the $i$-th JVP, leaving the other $n - 1$ affine spaces still intersecting at the previous solution $\mathbf{D}^{\ast \top}$. This shift is illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")b.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-B4 Optimization (Alg. 3, lines 10--14)", "weight": 1.0} -->

Line 14 reflects the mathematical procedure specified in Equation 15. This process locates the point on the affine space ${{({\Delta\mathbf{x}_{i}^{\top}})}^{\dagger}\Delta\mathbf{f}_{i}^{\top}} + {\mathbf{Z}_{\Delta\mathbf{x}_{i}^{\top}}\mathbf{Y}}$ that is closest (in terms of Euclidean distance) to the other $n - 1$ affine spaces that are still intersecting at the previous solution, illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")c. Cached matrices $\mathbf{C}_{1}$ and $\mathbf{C}_{2}$ are used to speed up this result without needing to compute matrix inverses at runtime. The output from this step is a new matrix $\mathbf{D}^{\ast \top}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-B5 Web of affine spaces matrix update (Alg. 3 line 15)", "weight": 1.0} -->

The web of affine spaces matrix is updated such that ${\mathbf{D}^{\ast}\Delta\mathbf{X}} = \hat{\Delta ⁢\mathbf{F}}$. After this update, the affine spaces within $\hat{\Delta ⁢\mathbf{F}}$ will all intersect again at the just computed $\mathbf{D}^{\ast \top}$, illustrated in Figure 2 ‣ V-B Algorithm Explanation ‣ V Algorithmic Details ‣ Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization")d. The matrix is now ready for either another iteration of the algorithm on the same input, if needed, or the next input in the sequence, $\mathbf{x}_{k + 1}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-C Initializing and Updating Matrices", "weight": 1.0} -->

Two key components of our approach are the tangent matrix, $\Delta\mathbf{X}$, and the web of affine spaces matrix, $\hat{\Delta ⁢\mathbf{F}}$. The tangent matrix is initialized in Algorithm 2, where it is specifically constructed as a random orthonormal matrix, meaning its columns have unit length and are mutually orthogonal. For interested readers, we provide full analysis and rationale for this structure in the Appendix §X-B. To generate a random orthonormal matrix, we apply singular value decomposition (SVD) to a uniformly sampled random $n \times n$ matrix.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-C Initializing and Updating Matrices", "weight": 1.0} -->

The web of affine spaces matrix is initialized as a zero matrix in algorithm 1. This matrix will dynamically update through the error detection and correction mechanism as needed. For instance, on the first call to Algorithm 3, the close_enough function will almost surely return $False$ for several iterations, allowing the matrix to progressively improve in accuracy over these updates.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Run-time Analysis", "weight": 1.0} -->

In this section, we analyze the run-time of our approach compared to alternatives. We will use the notation $\text{rt}{(.)}$ to denote the run-time of a subroutine. Approximate runtimes for several algorithms can be seen in Table I.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D Run-time Analysis", "weight": 1.0} -->

For WASP, $\mathbf{P}\mathbf{Q}$ and $\mathbf{R}\mathbf{S}$ are the matrix multiplications in Equation 15 (after preprocessing) and $q$ is the number of iterations needed to achieve sufficient accuracy. In many cases, $q = 1$, though note that even in the worst case, it is guaranteed that $q \leq n$ because when $k = n$, all columns in $\hat{\Delta ⁢\mathbf{F}}$ will be ground-truth JVPs.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-D Run-time Analysis", "weight": 1.0} -->

Comparing to other approaches, we see that WASP shifts the computational burden of scaling $m$ and $n$ to matrix multiplications rather than repeated forward or reverse calls to $f$. This adjustment is expected to yield run-time improvements when ${\text{rt}{(f)}} > {{\text{rt}{({\mathbf{P}\mathbf{Q}})}} + {\text{rt}{({\mathbf{R}\mathbf{S}})}}}$, particularly when a low value of $q$ is achievable due to a sequence of closely related inputs. rt(f) + q [rt(f) + rt(⏟PRn ×n⏟QRn ×m) +rt(⏟RRn ×1⏟SR1 ×m)] rt(build_computation_graph(f)) +m ⋅rt(reverse(f)) TABLE I: Approximate run-times for derivative computation approaches

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluation 1: Comparison on Benchmark Function", "weight": 1.0} -->

In Evaluation 1, we compare our approach to several other derivative computation approaches on a benchmark function.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-A Procedure", "weight": 1.0} -->

Evaluation 1 follows a three step procedure: The benchmark function shown in Algorithm 5 in initialized with given parameters $n$, $m$, and $o$. This function will remain fixed and deterministic through the remaining steps; a random walk trajectory is generated following the process seen in Algorithm 6 with a given number of waypoints ($w$), dimensionality ($n$), and step length ($\lambda$); For all conditions, derivatives of the benchmark function are computed in order on the $w$ inputs in the random walk trajectory. This trajectory is kept fixed for all conditions. Metrics are recorded for all conditions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-A Procedure", "weight": 1.0} -->

The benchmark function used in this experiment is a randomly generated composition of sine and cosine functions. This function, detailed in Algorithm 5, was designed to be highly parameterizable, allowing for any number of inputs ($n$), outputs ($m$), and operations per output ($o$). Sine and cosine were selected for their smooth derivatives and composability, given their infinite domain and bounded range. Moreover, numerous subroutines in robotics and related fields involve many compositions of sine and cosine functions, making this function a reasonable analogue of these processes.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-A Procedure", "weight": 1.0} -->

Evaluation 1 is divided into several sub-experiments, detailed below. Each sub-experiment varies which parameters of the procedure are allowed to change or remain fixed, aiming to assess different facets of the differentiation process.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-A Procedure", "weight": 1.0} -->

3 r ← random list of o + 1 integers between 1 and n 4 s ← random list of o integers, either 1 or 2 8 tmp = sin (cos (tmp) + x[r[j + 1]]) 10 tmp = cos (sin (tmp) + x[r[j + 1]]) ${out}\overset{+}{\leftarrow}{tmp}$ // append to output 2x ← random sample from ℝn v ← random sample from ℝn // random direction $\mathbf{v}\leftarrow\frac{\mathbf{v}}{\left\| \mathbf{v} \right\|}$ // normalize the direction x ← x + λv // take a λ-length step in x direction ${out}\overset{+}{\leftarrow}\mathbf{x}$ // add state to output list Algorithm 6 get_random_walk(w, n, λ)

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-B Conditions", "weight": 1.0} -->

Evaluation 1 compares five conditions: Reverse-mode automatic differentiation with PyTorch backend (abbreviated as RAD-PyTorch) Finite-differencing with NumPy backend (abbreviated as FD) Simultaneous Perturbation Stochastic Approximation with NumPy backend (abbreviated as SPSA) Web of Affine Spaces Optimization with orthonormal $\Delta\mathbf{X}$ matrix and NumPy backend (abbreviated as WASP-O).

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-B Conditions", "weight": 1.0} -->

Web of Affine Spaces Optimization with random, non-orthonormal $\Delta\mathbf{X}$ matrix and NumPy backend (abbreviated as WASP-NO).

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-B Conditions", "weight": 1.0} -->

All conditions in this section are implemented in Python and executed on a Desktop computer with an Intel i9 4.4GHz processor and 32 GB of RAM. To ensure a fair comparison, the underlying benchmark function code remained consistent across all conditions, with backend switching managed via Tensorly^11^1 The conditions in this section were required to remain fully compatible with the given benchmark function implemented in Tensorly, without any modifications, optimizations, or code adjustments specific to individual conditions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-B Conditions", "weight": 1.0} -->

We note that JAX, a widely-used automatic differentiation library, is not included in this section. Although JAX is theoretically compatible with Tensorly, we found that extensive code modifications were required to enable optimal performance through just-in-time (JIT) compilation. Preliminary tests showed that JAX, when not JIT-compiled, exhibited run-times that were unreasonably slow and did not reflect its full potential. Therefore, we chose not to report non-JIT-compiled JAX results in this section.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-B Conditions", "weight": 1.0} -->

For readers interested in further insights, supplementary results are provided in the Appendix (§X-C). These results relax the Tensorly-based uniformity constraints, allowing modifications, optimizations, and compilations to strive for maximum possible performance. Conditions in this supplemental section include JAX implementations compiled for both CPU and GPU, as well as Rust-based implementations.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VI-C Metrics", "weight": 1.0} -->

We record and report on three metrics in Evaluation 1: Average runtime (in seconds) of derivative computation through the sequence of $w$ inputs.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-C Metrics", "weight": 1.0} -->

Average number of calls to the benchmark function for a derivative computation through the sequence of $w$ inputs. Note that this value will be constant for all conditions aside from WASP.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-C Metrics", "weight": 1.0} -->

Average accuracy of the derivative through the sequence of $w$ inputs. We measure accuracy as the sum of angular error (Algorithm 7) and norm error (Algorithm 8). The components of this error measure to what extent the rows of the returned derivative are facing the correct direction and have the correct magnitude, respectively. If this value is zero, the returned derivative exactly matches the ground-truth derivative.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-C Metrics", "weight": 1.0} -->

$a_{1}\leftarrow\frac{\left\| \mathbf{D}_{\lbrack i,:\rbrack} \right\|}{\left\| \hat{\mathbf{D}_{\lbrack i,:\rbrack}} \right\|}$ // norm ratio between the i-th rows of the ground truth and approximate derivative $a_{2}\leftarrow\frac{\left\| \hat{\mathbf{D}_{\lbrack i,:\rbrack}} \right\|}{\left\| \mathbf{D}_{\lbrack i,:\rbrack} \right\|}$ // norm ratio between the i-th rows of the ground truth and approximate derivative (other possible ordering) b2 ← |1 − a2| // distance from 1 (other possible ordering) 7 avg ← avg + min (b1, b2) Algorithm 8 norm_error($\mathbf{D},\hat{\mathbf{D}}$)

<!-- chunk {"id": "body-0079", "role": "body", "section": "VI-D Sub-experiment 1: Gradient Calculations", "weight": 1.0} -->

In sub-experiment 1, we run the procedure outlined in §VI-A with parameters, $m = 1$, $o = 1000$, $w = 100$, $\lambda = 0.05$, $d_{\theta} = 0.1$, $d_{\ell} = 0.1$, and $n = {\{ 1,50,100,150,\ldots,1000\}}$. Our goal in sub-experiment 1 is to observe how the different conditions scale as the number of function inputs $n$ grows while $m$ remains fixed at $1$. In other words, the benchmark function here is a scalar function and its derivative is a $1 \times n$ row-vector gradient.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-D Sub-experiment 1: Gradient Calculations", "weight": 1.0} -->

Results for sub-experiment 1 can be seen in Figure 3 (top row). We observe that both WASP conditions outperform all other methods in runtime, except for SPSA, up to approximately $600$ inputs. Beyond this point, RAD-PyTorch. Additionally, the WASP conditions require orders of magnitude fewer function calls compared to FD, reflecting the goal of WASP to reuse recent information to avoid redundant calculation at the current input. While SPSA achieves the fastest runtime in sub-experiment 1, it incurs significant error. In contrast, the WASP conditions demonstrate much higher accuracy. Notably, the WASP condition utilizing the orthonormal tangent matrix structure maintains very low error, even for functions with up to 1000 inputs.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-E Sub-experiment 2: Square Jacobian Calculations", "weight": 1.0} -->

In sub-experiment 2, we run the procedure outlined in §VI-A with parameters ${(n,m)} = {(x,x)}$ where $x \in {\{ 1,10,20,30,40,50\}}$, $o = 1000$, $w = 100$, $\lambda = 0.05$, $d_{\theta} = 0.1$, and $d_{\ell} = 0.1$. Our goal in sub-experiment 2 is to observe how the different conditions scale as the number of function inputs and number of function outputs both grow. Thus, the benchmark function here is a vector function with the same number of inputs and outputs, and its derivative is an $n \times n$ square Jacobian.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-E Sub-experiment 2: Square Jacobian Calculations", "weight": 1.0} -->

Results for sub-experiment 2 can be seen in Figure 3 (middle row). The WASP conditions demonstrate greater efficiency compared to RAD-PyTorch and FD, achieving a runtime comparable to SPSA. This efficiency advantage is likely primarily due to the lower number of function calls, as seen in the middle graph. Notably, WASP exhibits much lower error than SPSA, particularly in the variant incorporating the orthonormal matrix structure. This demonstrates that WASP more accurately approximates ground-truth Jacobian matrices.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-F Sub-experiment 3: Varying step size", "weight": 1.0} -->

In sub-experiment 3, we run the procedure outlined in §VI-A with parameters, $n = 10$, $m = 10$, $o = 1000$, $w = 100$, $d_{\theta} = 0.1$, $d_{\ell} = 0.1$, and $\lambda = {\{ 0.001,0.01,0.1,1,10\}}$. Our goal in sub-experiment 3 is to observe how the different conditions scale as the step-length in the random walk trajectory grows.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-F Sub-experiment 3: Varying step size", "weight": 1.0} -->

Results for sub-experiment 3 can be seen in Figure 3 (bottom row). As expected, the performance of the WASP conditions generally declines as the step length increases. However, interestingly for a step length of $\lambda = 10$, the results show that the error approaches nearly zero, seemingly outperforming the trials with $\lambda = 1$ in terms of accuracy. This improved accuracy, however, comes at the cost of significantly more function calls, resulting in a much higher average runtime. Essentially, a step length of $\lambda = 10$ in this case was so large that the error detection and correction mechanism consistently triggered additional iterations until reaching the upper limit ($n$). As a result, the WASP conditions effectively defaulted to a standard finite-differencing strategy, hence why the WASP conditions are equivalent to the FD condition in terms of runtime and number of function calls in this scenario.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Evaluation 2: Error Propagation Analysis", "weight": 1.0} -->

In §V-B, we described the error detection and correction mechanism in our algorithm, which is designed to prevent error accumulation over a sequence of approximate derivative computations. In Evaluation 2, we analyze how errors propagate through our algorithm under different parameter settings, thereby evaluating the effectiveness of our proposed mechanism over long derivative sequences.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VII-A Procedure", "weight": 1.0} -->

Evaluation 2 follows the same procedure as Evaluation 1, described in §VI-A. We use parameters $n = 50$, $m = 1$, $o = 1000$, $w = {50,000}$, $\lambda = 0.05$, where $n$ is the number of inputs to the benchmark function, $m$ is the number of outputs from the benchmark function, $o$ is the number of operations per output in the benchmark function, $w$ is the number of waypoints in the random walk trajectory, and $\lambda$ is the step length along the random walk trajectory.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VII-B Conditions", "weight": 1.0} -->

The primary values we are varying and assessing in Evaluation 2 are the error threshold parameters, $d_{\theta}$ and $d_{\ell}$, outlined in §V-B. Specifically, we use parameter settings ${(d_{\theta},d_{\ell})} = {(x,x)}$ where $x \in {\{ 0.001,0.01,0.1,0.25,0.5,0.75,1.0\}}$. These settings allow us to evaluate error behavior across different error thresholds (the $d_{\theta}$ and $d_{\ell}$ parameters) over a long input sequence (as specified by the $w$ parameter above).

<!-- chunk {"id": "body-0088", "role": "body", "section": "VII-B Conditions", "weight": 1.0} -->

The WASP method in this evaluation uses a fixed orthonormal $\Delta\mathbf{X}$ matrix shared across all $d_{\theta}$ and $d_{\ell}$ configurations. We also compare the WASP variants against standard Finite Differencing using a NumPy backend.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VII-B Conditions", "weight": 1.0} -->

All conditions in Evaluation 2 are implemented in Python using Tensorly for backend switching and executed on a Desktop computer with an Intel i7 5.4GHz processor and 32 GB of RAM.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VII-C Metrics", "weight": 1.0} -->

We record and report on four metrics in Evaluation 2: Runtime (in seconds) per each derivative computation through the sequence of $w$ inputs.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VII-C Metrics", "weight": 1.0} -->

Number of calls to the benchmark function for each derivative computation through the sequence of $w$ inputs.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VII-C Metrics", "weight": 1.0} -->

The angular error of each derivative through the sequence of $w$ inputs (Algorithm 7).

<!-- chunk {"id": "body-0093", "role": "body", "section": "VII-C Metrics", "weight": 1.0} -->

The norm error of each derivative through the sequence of $w$ inputs (Algorithm 8).

<!-- chunk {"id": "body-0094", "role": "body", "section": "VII-D Results", "weight": 1.0} -->

Results for Eavluation 2 are shown in Figure 4. At a high level, we observe that WASP does not accumulate significant error over long sequences, even when high error thresholds are used. For instance, even at the $50,000$-th input, the errors remain low. In general, there are subtle ebbs and flows in error, naturally requiring more or fewer function calls throughout the sequence. At certain points, such as between the $13,000$-th and $15,000$-th inputs, WASP exhibits a transient increase in error under high thresholds, suggesting that this portion of the input sequence is less compatible with the WASP heuristic. However, even in these cases, the error remains within reasonable and usable bounds (e.g., less than $0.4$ radians from the ground truth gradient), and the algorithm successfully self-corrects after these brief periods of elevated error without diverging. As expected, using lower error thresholds consistently results in low error, but at the cost of additional function calls and runtime.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VII-D Results", "weight": 1.0} -->

In the limit as $d_{\theta}$ and $d_{\ell}$ approach $0$, both the accuracy and runtime performance converge to that of full finite differencing.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Evaluation 3: Application in Robot Optimization", "weight": 1.0} -->

In Evaluation 3, we compare our approach to several other derivative computation approaches in a robotics-based root-finding procedure.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VIII-A Procedure", "weight": 1.0} -->

Evaluation 3 follows a three step procedure: A robot state is sampled for a simulated Unitree B1 quadruped robot^22^2 with a Z1 manipulator^33^3 mounted on its back (shown in Figure 5). This robot has 24 degrees of freedom (including a floating base to account for mobility). This sampled state, $\mathbf{x}_{0} \in {\mathbb{R}}^{24}$, will be an initial condition for an optimization process; A Jacobian pseudo-inverse method (Algorithm 9) is used to find a root for a constraint function (Algorithm 10). The constraint function has five outputs: four for specifying foot placements and one for specifying the end-effector pose for the manipulator mounted on the back. Thus, the Jacobian of this constraint function is a $5 \times 24$ matrix; Step 1--2 are run 50 times per condition. Metrics are recorded for all conditions. x ← x0 // set state to be given initial condition y ← f(x) // initialize residuals.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VIII-A Procedure", "weight": 1.0} -->

The goal is for this vector to be all zeros (at a root) 4for i ∈ 0..max iterations do ${\Delta\mathbf{x}}\leftarrow{\left. \frac{\partial f}{\partial\mathbf{x}} \right|_{\mathbf{x}}^{\dagger}\mathbf{y}}$ // Compute direction using Jacobian matrix pseudoinverse x ← x − ϵΔx // take a step in the Δx direction. We use a value of ϵ = 0.01 return x // If the residual is small, the optimization has converged and the result should be returned. In practice, we use a value of γ = 0.01 Algorithm 9 root_finding(f, x0) l ← fk(x) // forward kinematics on given robot state. Returns an ordered list of SE poses for all robot links.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VIII-A Procedure", "weight": 1.0} -->

${ee_ pose_ goal}\leftarrow{\text{se3_matrix}\left(\begin{bmatrix} \end{bmatrix}^{\top},\begin{bmatrix} \end{bmatrix}^{\top} \right)}$ // the SE end-effector pose goal for the back-mounted robot arm. The arguments here are translation then Euler angle parameters, thus the pose goal has no added rotation. $\left. t_{1}\leftarrow \middle| \middle| l\lbrack 10\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for front left foot placement $\left. t_{2}\leftarrow \middle| \middle| l\lbrack 17\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for front right foot placement $\left.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VIII-A Procedure", "weight": 1.0} -->

t_{3}\leftarrow \middle| \middle| l\lbrack 24\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for back left foot placement $\left. t_{4}\leftarrow \middle| \middle| l\lbrack 31\rbrack.translation - \begin{bmatrix} \end{bmatrix}^{\top} \middle| \right|_{2}$ // error signal for back right foot placement t5 ← ∥ln(l−1 ⋅ ee_pose_goal)∥2 // the ln here is the logarithm map for the SE Lie group; it maps to the 𝔰𝔢 Lie algebra. return $\begin{bmatrix} \end{bmatrix}^{\top}$ // return a 5-vector of all the terms squared Algorithm 10 robot_constraint_function(x)

<!-- chunk {"id": "body-0101", "role": "body", "section": "VIII-B Conditions", "weight": 1.0} -->

The conditions in Evaluation 3 are the same as those listed in §VI-B. All conditions are implemented in Python and executed on a Desktop computer with an Intel i7 5.4GHz processor and 32 GB of RAM. Only the CPU was used for these experiments and Tensorly was again used for all backend-switching to maintain uniformity.

<!-- chunk {"id": "body-0102", "role": "body", "section": "VIII-C Metrics", "weight": 1.0} -->

We record and report on two metrics in Evaluation 3: Average runtime (in seconds) to converge on a robot configuration sufficiently close to the constraint surface.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VIII-C Metrics", "weight": 1.0} -->

Average number of optimization steps needed to converge on a robot configuration sufficiently close to the constraint surface.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VIII-D Results", "weight": 1.0} -->

Results for Evaluation 3 can be seen in Table II. The results show that the WASP conditions achieve significantly faster convergence compared to alternative approaches. Additionally, the orthonormal structure of the tangent matrix further enhances convergence efficiency. In contrast, the SPSA condition failed to converge, highlighting that certain derivative approximation methods may lack the accuracy required for some optimization procedures.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VIII-D Results", "weight": 1.0} -->

Average runtime (seconds) TABLE II: Evaluation 3 results. The ∗ symbol means that the condition never converged in the maximum number of iterations. Range values denote standard deviation.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we introduced a coherence-based approach for efficiently calculating a sequence of derivatives. Our approach leverages a novel process, the Web of Affine Spaces (WASP) Optimization, to identify a point guaranteed to reside on an affine space containing the ground-truth derivative that also aligns well with prior related calculations. Through extensive evaluations, we demonstrate that our approach outperforms widely used techniques such as automatic differentiation and finite differencing in terms of efficiency, while delivering greater accuracy compared to other derivative approximation methods. In this section, we discuss the limitations and broader implications of our approach.

<!-- chunk {"id": "body-0107", "role": "body", "section": "IX-A Limitations", "weight": 1.0} -->

We note several limitations of our work that suggest future avenues of research and extensions. First, the derivatives produced by our approach are approximations. Although our method can, in theory, achieve high accuracy comparable to standard finite differencing, attaining such precision would necessitate additional iterations, likely compromising its efficiency. For applications demanding exact derivatives in all cases, alternative techniques may be more appropriate.

<!-- chunk {"id": "body-0108", "role": "body", "section": "IX-A Limitations", "weight": 1.0} -->

Next, this paper focuses on presenting the math, algorithms, and initial proofs of concept for the WASP derivative approach. While we believe this technique has potential for impact across robotics and other fields, exploring its full range of applications and establishing best practices across many different problems is beyond the scope of this paper.

<!-- chunk {"id": "body-0109", "role": "body", "section": "IX-A Limitations", "weight": 1.0} -->

Furthermore, as demonstrated in Evaluation 1, the effectiveness of our approach diminishes significantly as the gap between inputs increases. We aim to refine or reformulate aspects of our approach going forward to reduce its strong sensitivity to step size.

<!-- chunk {"id": "body-0110", "role": "body", "section": "IX-A Limitations", "weight": 1.0} -->

Additionally, while our error detection and correction technique performs well in practice, it does not guarantee the accuracy of the approximations relative to ground-truth derivatives. Currently, the approach relies on JVPs (directional derivatives) as a proxy for true derivatives. While this provides a necessary condition for correctness, it is not a sufficient condition. In other words, the true derivative will always yield matching directional derivatives, but matching directional derivatives do not necessarily guarantee the underlying derivatives are correct. Ideally, the error detection and correction mechanism, along with its associated parameters, would relate directly to the true derivatives. However, addressing this issue is inherently challenging and perhaps infeasible. To illustrate, such a solution seems to elicit a circular reasoning problem: if one could sufficiently estimate the ground-truth derivative well enough to bound the approximation, that same information could be used to directly select a closer approximation to the true derivative in the first place. This issue remains an open question that requires further investigation.

<!-- chunk {"id": "body-0111", "role": "body", "section": "IX-A Limitations", "weight": 1.0} -->

Lastly, while the current approach performs well for small to medium-sized problems, it does not scale effectively to large-scale functions. For example, applying this method to neural network training with millions or billions of parameters would be infeasible due to the prohibitive size of the matrices required for the optimization process. In future work, we plan to explore scalable adaptations of this approach that better manage storage and computational demands.

<!-- chunk {"id": "body-0112", "role": "body", "section": "IX-B Implications", "weight": 1.0} -->

Due to the ubiquity of derivative computation in robotics and beyond, we believe our work has the potential for broad impact and applicability. For example, it could prove to be valuable in areas such as model predictive control, physics simulation, trajectory optimization, inverse kinematics, and more. Our goal is to enable the community to leverage these derivatives to streamline computationally expensive subroutines, achieving performance gains with minimal code modifications. By doing so, we aim to unlock new levels of interactivity and adaptability for robots, empowering them to operate seamlessly and responsively in real-time environments.
