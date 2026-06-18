<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Discovering Governing Equations from Data: Sparse Identification of Nonlinear Dynamical Systems

Topics include System identification, Sparse regression, SINDy, Nonlinear dynamics, Data-driven methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces SINDy, which applies sparse nonlinear least squares regression over a library of candidate nonlinear functions to identify parsimonious governing equations from trajectory data, recovering interpretable symbolic expressions for nonlinear dynamical systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extracting governing equations from data is a central challenge in many diverse areas of science and engineering. Data are abundant whereas models often remain elusive, as in climate science, neuroscience, ecology, finance, and epidemiology, to name only a few examples. In this work, we combine sparsity-promoting techniques and machine learning with nonlinear dynamical systems to discover governing equations from noisy measurement data. The only assumption about the structure of the model is that there are only a few important terms that govern the dynamics, so that the equations are sparse in the space of possible functions; this assumption holds for many physical systems in an appropriate basis. In particular, we use sparse regression to determine the fewest terms in the dynamic governing equations required to accurately represent the data. This results in parsimonious models that balance accuracy with model complexity to avoid overfitting. We demonstrate the algorithm on a wide range of problems, from simple canonical systems, including linear and nonlinear oscillators and the chaotic Lorenz system, to the fluid vortex shedding behind an obstacle. The fluid example illustrates the ability of this method to discover the underlying dynamics of a system that took experts in the community nearly 30 years to resolve.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also show that this method generalizes to parameterized systems and systems that are time-varying or have external forcing.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extracting physical laws from data is a central challenge in many diverse areas of science and engineering. There are many critical data-driven problems, such as understanding cognition from neural recordings, inferring patterns in climate, determining stability of financial markets, predicting and suppressing the spread of disease, and controlling turbulence for greener transportation and energy. With abundant data and elusive laws, it is likely that data-driven discovery of dynamics will continue to play an increasingly important role in these efforts.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in machine learning and data science have promised a renaissance in the analysis and understanding of complex data, extracting patterns in vast multimodal data that is beyond the ability of humans to grasp. However, despite the rapid development of tools to understand static data based on statistical relationships, there has been slow progress in distilling physical models of dynamic processes from big data. This has limited the ability of data science models to extrapolate the dynamics beyond the attractor where they were sampled and constructed.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An analogy may be drawn with the discoveries of Kepler and Newton. Kepler, equipped with the most extensive and accurate planetary data of the era, developed a *data-driven* model for the motion of the planets, resulting in his famous elliptic orbits. However, this was an *attractor* based view of the world, and it did not explain the fundamental dynamic relationships that give rise to planetary orbits, or provide a model for how these bodies react when perturbed. Newton, in contrast, discovered a dynamic relationship between momentum and energy that described the underlying processes responsible for these elliptic orbits. This dynamic model may be generalized to predict behavior in regimes where no data was collected. Newton's model has proven remarkably robust for engineering design, making it possible to land a spacecraft on the moon, which would not have been possible using Kepler's model alone.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A seminal breakthrough by Schmidt and Lipson has resulted in a new approach to determine the underlying structure of a nonlinear dynamical system from data. This method uses symbolic regression (i.e., genetic programming ) to find nonlinear differential equations, and it balances complexity of the model, measured in the number of terms, with model accuracy. The resulting model identification realizes a long-sought goal of the physics and engineering communities to discover dynamical systems from data. However, symbolic regression is expensive, does not scale well to large systems of interest, and may be prone to overfitting unless care is taken to explicitly balance model complexity with predictive power. In, the Pareto front is used to find parsimonious models in a large family of candidate models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we re-envision the dynamical system discovery problem from an entirely new perspective of sparse regression and compressed sensing. In particular, we leverage the fact that most physical systems have only a few relevant terms that define the dynamics, making the governing equations *sparse* in a high-dimensional nonlinear function space. Before the advent of compressive sampling, and related sparsity-promoting methods, determining the few non-zero terms in a nonlinear dynamical system would have involved a combinatorial brute-force search, meaning that the methods would not scale to larger problems with Moore's law. However, powerful new theory guarantees that the sparse solution may be determined with high-probability using convex methods that do scale favorably with problem size. The resulting nonlinear model identification inherently balances model complexity (i.e., sparsity of right hand side dynamics) with accuracy, and the underlying convex optimization algorithms ensure that the method will be applicable to large-scale problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The method described here shares some similarity to the recent dynamic mode decomposition (DMD), which is a linear dynamic regression. DMD is an example of an equation-free method, since it only relies on measurement data, but not on knowledge of the governing equations. Recent advances in the extended DMD have developed rigorous connections between DMD built on nonlinear observable functions and the Koopman operator theory for nonlinear dynamical systems. However, there is currently no theory for which nonlinear observable functions to use, so that assumptions must be made on the form of the dynamical system. In contrast, the method developed here results in a *sparse, nonlinear* regression that automatically determines the relevant terms in the dynamical system. The trend to exploit sparsity in dynamical systems is recent but growing. In this work, promoting sparsity in the dynamics results in parsimonious natural laws.\

<!-- chunk {"id": "body-0011", "role": "body", "section": "Symbolic regression and machine learning", "weight": 1.0} -->

Symbolic regression involves the determination of a function that relates input--output data, and it may be viewed as a form of machine learning. Typically, the function is determined using genetic programming, which is an evolutionary algorithm that builds and tests candidate functions out of simple building blocks. These functions are then modified according to a set of evolutionary rules and generations of functions are tested until a pre-determined accuracy is achieved.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Symbolic regression and machine learning", "weight": 1.0} -->

Recently, symbolic regression has been applied to data from *dynamical* systems, and ordinary differential equations were discovered from measurement data. Because it is possible to overfit with symbolic regression and genetic programming, a parsimony constraint must be imposed, and, they accept candidate equations that are at the Pareto front of complexity.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sparse representation and compressive sensing", "weight": 1.0} -->

In many regression problems, only a few terms in the regression are important, and a *sparse feature selection* mechanism is required.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sparse representation and compressive sensing", "weight": 1.0} -->

Performing a standard regression to solve for $\mathbf{ξ}$ will result in a solution with nonzero contributions in each element.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sparse representation and compressive sensing", "weight": 1.0} -->

The parameter $\lambda$ weights the sparsity constraint. This formulation is closely related to the compressive sensing framework, which allows for the sparse vector $\mathbf{ξ}$ to be determined from relatively few *incoherent* random measurements. The sparse solution $\mathbf{ξ}$ to Eq. 1 may also be used for sparse classification schemes, such as the sparse representation for classification (SRC). Importantly, the compressive sensing and sparse representation architectures are convex and scale well to large problems, as opposed to brute-force combinatorial alternatives.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

In this work, we are concerned with identifying the governing equations that underly a physical system based on data that may be realistically collected in simulations or experiments. Generically, we seek to represent the system as a nonlinear dynamical system

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

The vector ${\mathbf{x}{(t)}} = \begin{bmatrix}
\end{bmatrix}^{T} \in {\mathbb{R}}^{n}$ represents the state of the system at time $t$, and the nonlinear function $\mathbf{f}{({\mathbf{x}{(t)}})}$ represents the dynamic constraints that define the equations of motion of the system. In the following sections, we will generalize Eq. (3 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) to allow the dynamics $\mathbf{f}$ to vary in time, and also with respect to a set of bifurcation parameters ${\mathbf{μ}} \in {\mathbb{R}}^{q}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

The key observation in this paper is that for many systems of interest, the function $\mathbf{f}$ often consists of only a few terms, making it sparse in the space of possible functions. For example, the Lorenz system in Eq. (22c ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) has very few terms in the space of polynomial functions. Recent advances in compressive sensing and sparse regression make this viewpoint of sparsity favorable, since it is now possible to determine *which* right hand side terms are non-zero without performing a computationally intractable brute-force search.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

To determine the form of the function $\mathbf{f}$ from data, we collect a time-history of the state $\mathbf{x}{(t)}$ and its derivative $\overset{˙}{\mathbf{x}}{(t)}$ sampled at a number of instances in time $t_{1},t_{2},\cdots,t_{m}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

Next, we construct an augmented library $\mathbf{\Theta}{(\mathbf{X})}$ consisting of candidate nonlinear functions of the columns of $\mathbf{X}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

Each column of $\mathbf{\Theta}{(\mathbf{X})}$ represents a candidate function for the right hand side of Eq. (3 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). There is tremendous freedom of choice in constructing the entries in this matrix of nonlinearities. Since we believe that only a few of these nonlinearities are active in each row of $\mathbf{f}$, we may set up a sparse regression problem to determine the sparse vectors of coefficients $\mathbf{\Xi} = \begin{bmatrix}
{\mathbf{ξ}}_{1} & {\mathbf{ξ}}_{2} & \cdots & {\mathbf{ξ}}_{n}
\end{bmatrix}$ that determine which nonlinearities are active, as illustrated in Fig. 1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems").

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

Each column ${\mathbf{ξ}}_{k}$ of $\mathbf{\Xi}$ represents a sparse vector of coefficients determining which terms are active in the right hand side for one of the row equations ${\overset{˙}{\mathbf{x}}}_{k} = {\mathbf{f}_{k}{(\mathbf{x})}}$ in Eq. (3 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

Note that $\mathbf{\Theta}{(\mathbf{x}^{T})}$ is a vector of symbolic functions of elements of $\mathbf{x}$, as opposed to $\mathbf{\Theta}{(\mathbf{X})}$, which is a data matrix. This results in the overall model

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sparse identification of nonlinear dynamics (SINDy)", "weight": 1.0} -->

We may solve for $\mathbf{\Xi}$ in Eq. (7 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) using sparse regression.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

There are a number of algorithms to determine sparse solutions $\mathbf{\Xi}$ to the regression problem in Eq. (7 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). Each column of Eq. (7 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) requires a distinct optimization problem to find the sparse vector of coefficients ${\mathbf{ξ}}_{k}$ for the $k^{\text{th}}$ row equation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

For the examples in this paper, the matrix $\mathbf{\Theta}{(\mathbf{X})}$ has dimensions $m \times p$, where $p$ is the number of candidate nonlinear functions, and where $m \gg p$ since there are more time samples of data than there are candidate nonlinear functions. In most realistic cases, the data $\mathbf{X}$ and $\overset{˙}{\mathbf{X}}$ will be contaminated with noise so that Eq. (7 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) does not hold exactly. In the case that $\mathbf{X}$ is relatively clean but the derivatives $\overset{˙}{\mathbf{X}}$ are noisy, the equation becomes

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

where $\mathbf{Z}$ is a matrix of independent identically distributed Gaussian entries with zero mean, and $\eta$ is the noise magnitude. Thus we seek a sparse solution to an overdetermined system with noise.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

The LASSO from statistics works well with this type of data, providing a sparse regression. However, it may be computationally expensive for very large data sets.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

An alternative is to implement the sequential thresholded least-squares algorithm in Code (1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). In this algorithm, we start with a least-squares solution for $\mathbf{\Xi}$ and then threshold all coefficients that are smaller than some cutoff value $\lambda$. Once the indices of the remaining non-zero coefficients are identified, we obtain another least-squares solution for $\mathbf{\Xi}$ onto the remaining indices. These new coefficients are again thresholded using $\lambda$, and the procedure is continued until the non-zero coefficients converge. This algorithm is computationally efficient, and it rapidly converges to a sparse solution in a small number of iterations. The algorithm also benefits from simplicity, with a single parameter $\lambda$ required to determine the degree of sparsity in $\mathbf{\Xi}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

Depending on the noise, it may still be necessary to filter the data $\mathbf{X}$ and derivative $\overset{˙}{\mathbf{X}}$ before solving for $\mathbf{\Xi}$. In particular, if only the data $\mathbf{X}$ is available, and $\overset{˙}{\mathbf{X}}$ must be obtained by differentiation, then the resulting derivative matrix may have large noise magnitude. To counteract this, we use the total variation regularized derivative to de-noise the derivative. An alternative would be to filter the data $\mathbf{X}$ and $\overset{˙}{\mathbf{X}}$, for example using the optimal hard threshold for singular values described.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

It is important to note that previous algorithms to identify dynamics from data have been quite sensitive to noise. The algorithm in Code (1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) is remarkably robust to noise, and even when velocities must be approximated from noisy data, the algorithm works surprisingly well.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithm for sparse representation of dynamics with noise", "weight": 1.0} -->

%% compute Sparse regression: sequential least squares
Xi = Theta\dXdt; % initial guess: Least-squares
% lambda is our sparsification knob.
smallinds = (abs(Xi)&lt;lambda); % find small coefficients
Xi(smallinds)=0; % and threshold
for ind = 1:n % n is state dimension
biginds = ~smallinds(:,ind);
% Regress dynamics onto remaining terms to find sparse Xi
Xi(biginds,ind) = Theta(:,biginds)\dXdt(:,ind);
Code 1: Sparse representation algorithm in Matlab.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Cross-validation to determine parsimonious sparse solution on Pareto front", "weight": 1.0} -->

To determine the sparsification parameter $\lambda$ in the algorithm in Code (1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")), it is helpful to use the concept of cross-validation from machine learning. It is always possible to hold back some test data apart from the training data to test the validity of models away from training values. In addition, it is important to consider the balance of model complexity (given by the number of nonzero coefficients in $\mathbf{\Xi}$) with the model accuracy. There is an "elbow" in the curve of accuracy vs. complexity parameterized by $\lambda$, the so-called Pareto front. This value of $\lambda$ represents a good tradeoff between complexity and accuracy, and it is similar to the approach taken.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Extensions and Connections", "weight": 1.0} -->

There are a number of extensions to the basic theory above that generalize this approach to a broader set of problems. First, the method is generalized to a discrete-time formulation, establishing a connection with the dynamic mode decomposition (DMD). Next, high-dimensional systems obtained from discretized partial differential equations are considered, extending the method to incorporate dimensionality reduction techniques to handle big data. Finally, the sparse regression framework is modified to include bifurcation parameters, time-dependence, and external forcing.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discrete-time representation", "weight": 1.0} -->

There are a number of reasons to implement Eq. (11 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). First, many systems, such as the logistic map in Eq. are inherently discrete-time systems. In addition, it may be possible to recover specific integration schemes used to advance Eq. (3 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). The discrete-time formulation also foregoes the calculation of a derivative from noisy data.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discrete-time representation", "weight": 1.0} -->

The continuous-time sparse regression problem in Eq.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discrete-time representation", "weight": 1.0} -->

and the function $\mathbf{f}$ is the same as in Eq. (9 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discrete-time representation", "weight": 1.0} -->

In the discrete setting in Eq. (11 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")), and for linear dynamics, there is a striking resemblance to dynamic mode decomposition. In particular, if ${\mathbf{\Theta}{(\mathbf{x})}} = \mathbf{x}$, so that the dynamical system is linear, then Eq. (13 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) becomes

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discrete-time representation", "weight": 1.0} -->

This is equivalent to the DMD, which seeks a dynamic regression onto linear dynamics $\mathbf{\Xi}^{T}$. In particular, $\mathbf{\Xi}^{T}$ is $n \times n$ dimensional, which may be prohibitively large for a high-dimensional state $\mathbf{x}$. Thus, DMD identifies the dominant terms in the eigendecomposition of $\mathbf{\Xi}^{T}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "High-dimensional systems, partial differential equations, and dimensionality reduction", "weight": 1.0} -->

Often, the physical system of interest may be naturally represented by a partial differential equation (PDE) in a few spatial variables. If data is collected from a numerical discretization or from experimental measurements on a spatial grid, then the state dimension $n$ may be prohibitively large. For example, in fluid dynamics, even simple two-dimensional and three-dimensional flows may require tens of thousands up to billions of variables to represent the discretized system.

<!-- chunk {"id": "body-0041", "role": "body", "section": "High-dimensional systems, partial differential equations, and dimensionality reduction", "weight": 1.0} -->

The method described above is prohibitive for a large state dimension $n$, both because of the factorial growth of $\mathbf{\Theta}$ in $n$ and because each of the $n$ row equations in Eq. (8 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")) requires a separate optimization. Fortunately, many high-dimensional systems of interest evolve on a low-dimensional manifold or attractor that may be well-approximated using a dimensionally reduced low-rank basis $\mathbf{\Psi}$. For example, if data $\mathbf{X}$ is collected for a high-dimensional system as in Eq.

<!-- chunk {"id": "body-0042", "role": "body", "section": "High-dimensional systems, partial differential equations, and dimensionality reduction", "weight": 1.0} -->

where $\mathbf{a}$ is an $r$-dimensional vector of mode coefficients. We assume that this is a good approximation for a relatively low rank $r$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "High-dimensional systems, partial differential equations, and dimensionality reduction", "weight": 1.0} -->

There are many choices for a low-rank basis, including proper orthogonal decomposition (POD), based on the SVD.

<!-- chunk {"id": "body-0044", "role": "body", "section": "External forcing, bifurcation parameters, and normal forms", "weight": 1.0} -->

In practice, many real-world systems depend on parameters, and dramatic changes, or bifurcations, may occur when the parameter is varied. The algorithm above is readily extended to encompass these important parameterized systems, allowing for the discovery of normal forms associated with a bifurcation parameter $\mathbf{μ}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "External forcing, bifurcation parameters, and normal forms", "weight": 1.0} -->

It is then possible to identify the right hand side $\mathbf{f}{(\mathbf{x};{\mathbf{μ}})}$ as a sparse combination of functions of components in $\mathbf{x}$ as well as the bifurcation parameter $\mathbf{μ}$. This idea is illustrated on two examples, the one-dimensional logistic map and the two-dimensional Hopf normal form.

<!-- chunk {"id": "body-0046", "role": "body", "section": "External forcing, bifurcation parameters, and normal forms", "weight": 1.0} -->

This generalization makes it possible to analyze systems that are externally forced or controlled. For example, the climate is both parameterized and has external forcing, including carbon dioxide and solar radiation. The financial market presents another important example with forcing and active feedback control, in the form of regulations, taxes, and interest rates.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

We demonstrate the methods described in Sec. 3 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") on a number of canonical systems, ranging from simple linear and nonlinear damped oscillators, to noisy measurements of the fully chaotic Lorenz system, and to measurements of the unsteady fluid wake behind a circular cylinder, extending this method to nonlinear partial differential equations (PDEs) and high-dimensional data. Finally, we show that bifurcation parameters may be included in the sparse models, recovering the correct normal forms from noisy measurements of the logistic map and the Hopf normal form.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 1a: Two-dimensional damped oscillator (linear vs. nonlinear)", "weight": 1.0} -->

In this example, we consider the two-dimensional damped harmonic oscillator with either linear or cubic dynamics, as in Eq. (20 ‣ 4.1 Example 1: Simple illustrative systems ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). The dynamic data and the sparse identified model are shown in Fig. 2 ‣ 4.1 Example 1: Simple illustrative systems ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"). The correct form of the nonlinearity is obtained in each case; the augmented nonlinear library $\mathbf{\Theta}{(\mathbf{x})}$ includes polynomials in $\mathbf{x}$ up to fifth order. The sparse identified model and algorithm parameters are shown in the Appendix in Tables 1 and 2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 1b: Three-dimensional linear system", "weight": 1.0} -->

A linear system with three variables and the sparse approximation are shown in Fig. 3. In this case, the dynamics are given by

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 1b: Three-dimensional linear system", "weight": 1.0} -->

The sparse identification algorithm correctly identifies the system in the space of polynomials up to second or third order, and the sparse model is given in Table 3. Interestingly, including polynomial terms of higher order (e.g. orders 4 or 5) introduces a degeneracy in the sparse identification algorithm, because linear combinations of powers of $e^{\lambdat}$ may approximate other exponential rates. This unexpected degeneracy motivates a hierarchical approach to identification, where subsequently higher order terms are included until the algorithm either converges or diverges.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

Here, we consider the nonlinear Lorenz system to explore the identification of chaotic dynamics evolving on an attractor, shown in Fig.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

Although these equations give rise to rich and chaotic dynamics that evolve on an attractor, there are only a few terms in the right-hand side of the equations. Figure 1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") shows a schematic of how data is collected for this example, and how sparse dynamics are identified in a space of possible right-hand side functions using convex $\ell_{1}$-minimzation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

For this example, data is collected for the Lorenz system, and stacked into two large data matrices $\mathbf{X}$ and $\overset{˙}{\mathbf{X}}$, where each row of $\mathbf{X}$ is a snapshot of the state $\mathbf{x}$ in time, and each row of $\overset{˙}{\mathbf{X}}$ is a snapshot of the time derivative of the state $\overset{˙}{\mathbf{x}}$ in time.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

Each column of $\mathbf{\Theta}{(\mathbf{X})}$ represents a candidate function for the right hand side of Eq. (3 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")), and a sparse regression determines which terms are active in the dynamics, as in Fig. 1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), and Eq. (7 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

Zero-mean Gaussian measurement noise with variance $\eta$ is added to the derivative calculation to investigate the effect of noisy derivatives. The short-time ($t = 0$ to $t = 20$) and long-time ($t = 0$ to $t = 250$) system reconstruction is shown in Fig. 4 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") for two different noise values, $\eta = 0.01$ and $\eta = 10$. The trajectories are also shown in dynamo view in Fig. 5 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), and the $\ell_{2}$ error vs. time for increasing noise $\eta$ is shown in Fig. 6 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"). Although the $\ell_{2}$ error increases for large noise values $\eta$, the form of the equations, and hence the attractor dynamics, are accurately captured.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

Because the system has a positive Lyapunov exponent, small differences in model coefficients or initial conditions grow exponentially, until saturation, even though the attractor may remain unchanged.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

In the Lorenz example, the ability to capture dynamics on the attractor is more important than the ability to predict an individual trajectory, since chaos will quickly cause any small variations in initial conditions or model coefficients to diverge exponentially. As shown in Fig. 1 ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), our sparse model identification algorithm accurately reproduces the attractor dynamics from chaotic trajectory measurements. The algorithm not only identifies the correct linear and quadratic terms in the dynamics, but it accurately determines the coefficients to within $.03\%$ of the true values. When the derivative measurements are contaminated with noise, the correct dynamics are identified, and the attractor is well-preserved for surprisingly large noise values. When the noise is too large, the structure identification fails before the coefficients become too inaccurate.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Example 2: Lorenz system (Nonlinear ODE)", "weight": 1.0} -->

For this example, we use the standard parameters ${\sigma = 10},{{\beta = {8/3}},{\rho = 28}}$, with an initial condition $\begin{bmatrix}
\end{bmatrix}^{T} = \begin{bmatrix}
\end{bmatrix}^{T}$. Data is collected from $t = 0$ to $t = 100$ with a time-step of ${\Deltat} = 0.001$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Example 3: Fluid wake behind a cylinder (Nonlinear PDE)", "weight": 1.0} -->

The Lorenz system is a low-dimensional model of more realistic high-dimensional partial differential equation (PDE) models for fluid convection in the atmosphere. Many systems of interest are governed by PDEs, such as weather and climate, epidemiology, and the power grid, to name a few. Each of these examples are characterized by big data, consisting of large spatially resolved measurements consisting of millions or billions of states and spanning orders of magnitude of scale in both space and time. However, many high-dimensional, real-world systems evolve on a low-dimensional attractor, making the effective dimension much smaller.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Example 3: Fluid wake behind a cylinder (Nonlinear PDE)", "weight": 1.0} -->

Here we generalize the sparse identification of nonlinear dynamics method to an example in fluid dynamics that typifies many of the challenges outlined above. Data is collected for the fluid flow past a cylinder at Reynolds number 100 using direct numerical simulations of the two-dimensional Navier-Stokes equations. Then, the nonlinear dynamic relationship between the dominant coherent structures is identified from these flow field measurements with no knowledge of the governing equations.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Example 3: Fluid wake behind a cylinder (Nonlinear PDE)", "weight": 1.0} -->

The low-Reynolds number flow past a cylinder is a particularly interesting example because of its rich history in fluid mechanics and dynamical systems. It has long been theorized that turbulence may be the result of a sequence of Hopf bifurcations that occur as the Reynolds number of the flow increases. The Reynolds number is a rough measure of the ratio of inertial and viscous forces, and an increasing Reynolds number may correspond, for example, to increasing flow velocity, giving rise to more rich and intricate structures in the fluid.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Example 3: Fluid wake behind a cylinder (Nonlinear PDE)", "weight": 1.0} -->

After 15 years, the first Hopf bifurcation was discovered in a fluid system, in the transition from a steady laminar wake to laminar periodic vortex shedding at Reynolds number $47$. This discovery led to a long-standing debate about how a Hopf bifurcation, with cubic nonlinearity, can be exhibited in a Navier-Stokes fluid with quadratic nonlinearities. After 15 more years, this was finally resolved using a separation of time-scales argument and a mean-field model, shown in Eq. (24 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")). It was shown that coupling between oscillatory modes and the base flow gives rise to a slow manifold (see Fig. 7 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), left), which results in algebraic terms that approximate cubic nonlinearities on slow timescales.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Example 3: Fluid wake behind a cylinder (Nonlinear PDE)", "weight": 1.0} -->

This example provides a compelling test-case for the proposed algorithm, since the underlying form of the dynamics took nearly three decades to uncover. Indeed, the sparse dynamics algorithm correctly identifies the on-attractor and off-attractor dynamics using quadratic nonlinearities and preserves the correct slow-manifold dynamics. It is interesting to note that when the off-attractor trajectories are not included in the system identification, the algorithm incorrectly identifies the dynamics using cubic nonlinearities, and fails to correctly identify the dynamics associated with the shift mode, which connects the mean flow to the unstable steady state.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Direct numerical simulation", "weight": 1.0} -->

The direct numerical simulation involves a fast multi-domain immersed boundary projection method. Four grids are used, each with a resolution of $450 \times 200$, with the finest grid having dimensions of $9 \times 4$ cylinder diameters and the largest grid having dimensions of $72 \times 32$ diameters. The finest grid has 90,000 points, and each subsequent coarser grid has 67,500 distinct points. Thus, if the state includes the vorticity at each grid point, then the state dimension is 292,500. The vorticity field on the finest grid is shown in Fig. 7 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"). The code is non-dimensionalized so that the cylinder diameter and free-stream velocity are both equal to one: $D = 1$ and $U_{\infty} = 1$, respectively. The simulation time-step is ${\Deltat} = 0.02$ non dimensional time units.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Mean field model", "weight": 1.0} -->

To develop a mean-field model for the cylinder wake, first we must reduce the dimension of the system. The proper orthogonal decomposition (POD), provides a low-rank basis that is optimal in the $L^{2}$ sense, resulting in a hierarchy of orthonormal modes that are ordered by mode energy. The first two most energetic POD modes capture a significant portion of the energy; the steady-state vortex shedding is a limit cycle in these coordinates. An additional mode, called the shift mode, is included to capture the transient dynamics connecting the unstable steady state with the mean of the limit cycle (i.e., the direction connecting point 'C' to point 'B' in Fig. 7 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Mean field model", "weight": 1.0} -->

If $\lambda$ is large, so that the $z$-dynamics are fast, then the mean flow rapidly corrects to be on the (slow) manifold $z = {x^{2} + y^{2}}$ given by the amplitude of vortex shedding. When substituting this algebraic relationship into Eqs. 24a ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") and 24b ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), we recover the Hopf normal form on the slow manifold.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Mean field model", "weight": 1.0} -->

Remarkably, similar dynamics are discovered by the sparse dynamics algorithm, purely from data collected from simulations. The identified model coefficients, shown in Table 5, only include quadratic nonlinearities, consistent with the Navier-Stokes equations. Moreover, the transient behavior, shown in Figs. 9 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") and 10 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), is captured qualitatively for solutions that do not start on the slow manifold. When the off-attractor dynamics in Fig. 9 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") are not included in the training data, the model incorrectly identifies a simple Hopf normal form in $x$ and $y$ with cubic nonlinearities.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Mean field model", "weight": 1.0} -->

The data from Fig. 10 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems") was not included in the training data, and although qualitatively similar, the identified model does not exactly reproduce the transients. Since this initial condition had twice the fluctuation energy in the $x$ and $y$ directions, the slow manifold approximation may not be valid here. Relaxing the sparsity condition, it is possible to obtain models that agree almost perfectly with the data in Figs. 8 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems")-10 ‣ 4 Results ‣ Discovering governing equations from data: Sparse identification of nonlinear dynamical systems"), although the model includes higher order nonlinearities.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Example 4: Bifurcations and Normal Forms", "weight": 1.0} -->

It is then possible to identify the right hand side $\mathbf{f}{(\mathbf{x};\mu)}$ as a sparse combination of functions of components in $\mathbf{x}$ as well as the bifurcation parameter $\mu$. This idea is illustrated on two examples, the one-dimensional logistic map and the two-dimensional Hopf normal form.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Logistic map", "weight": 1.0} -->

The logistic map is a classical model that exhibits a cascade of bifurcations, leading to chaotic trajectories. The dynamics with stochastic forcing $\eta_{k}$ and parameter $\mu$ are given by

<!-- chunk {"id": "body-0071", "role": "body", "section": "Logistic map", "weight": 1.0} -->

Sampling the stochastic system at ten parameter values of $\mu$, the algorithm correctly identifies the underlying parameterized dynamics, shown in Fig. 11 and Table 6.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Hopf normal form", "weight": 1.0} -->

The final example illustrating the ability of the sparse dynamics method to identify parameterized normal forms is the Hopf normal form. Noisy data is collected from the Hopf system

<!-- chunk {"id": "body-0073", "role": "body", "section": "Hopf normal form", "weight": 1.0} -->

for various values of the parameter $\mu$. Data is collected on the blue and red trajectories in Fig. 12, and noise is added to simulate sensor noise. The total variation derivative is used to de-noise the derivative for use in the algorithm.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Hopf normal form", "weight": 1.0} -->

The sparse model identification algorithm correctly identifies the Hopf normal form, with model parameters given in Table 7. The noise-free model reconstruction is shown in Fig. 13. Note that with noise in the training data, although the model terms are correctly identified, the actual values of the cubic terms are off by almost $8\%$. Collecting more training data or reducing the noise magnitude both improve the model agreement.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion", "weight": 1.5} -->

In summary, we have demonstrated a powerful new technique to identify nonlinear dynamical systems from data without assumptions on the form of the governing equations. This builds on prior work in symbolic regression but with innovations related to sparse regression, which allow our algorithms to scale to high-dimensional systems. We demonstrate this new method on a number of example systems exhibiting chaos, high-dimensional data with low-rank coherence, and parameterized dynamics. As shown in the Lorenz example, the ability to predict a specific trajectory may be less important than the ability to capture the attractor dynamics. The example from fluid dynamics highlights the remarkable ability of this method to extract dynamics in a fluid system that took three decades for experts in the community to explain. There are numerous fields where this method may be applied, where there is ample data and the absence of governing equations, including neuroscience, climate science, epidemiology, and financial markets. Fields that already use genetic programming, such as machine learning control for turbulent fluid systems, may also benefit. Finally, normal forms may be discovered by including parameters in the optimization, as shown on two examples.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion", "weight": 1.5} -->

The identification of *sparse* governing equations and parameterizations marks a significant step toward the long-held goal of intelligent, unassisted identification of dynamical systems.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discussion", "weight": 1.5} -->

A number of open problems remain surrounding the dynamical systems aspects of this procedure. For example, many systems possess dynamical symmetries and conserved quantities that may alter the form of the identified dynamics. For example, the degenerate identification of a linear system in a space of high-order polynomial nonlinearities suggest a connection with near-identity transformations and dynamic similarity. We believe that this may be a fruitful line of research. Finally, it will be important to identify which approximating function space to use based on the data available. For example, it may be possible to improve the function space to make the dynamics more sparse through subsequent coordinate transformations.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Discussion", "weight": 1.5} -->

Data science is not a panacea for all problems in science and engineering, but used in the right way, it provides a principled approach to maximally leverage the data that we have and inform what new data to collect. Big data is happening all across the sciences, where the data is inherently *dynamic*, and where traditional approaches are prone to overfitting. Data discovery algorithms that produce *parsimonious* models are both rare and desirable. Data-science will only become more critical to efforts in science in engineering, where data is abundant, but physical laws remain elusive. These efforts include understanding the neural basis of cognition, extracting and predicting coherent changes in the climate, stabilizing financial markets, managing the spread of disease, and controlling turbulence,
