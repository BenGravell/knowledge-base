<!-- arxiv-full-text:v1 {"arxiv_id": "2504.14099", "source": "arxiv-html"} -->

## Introduction

A convex optimization problem, parametrized by $\theta \in \Theta \subseteq \text{R}^{d}$, can be written as where $x \in \text{R}^{n}$ is the optimization variable, $f_{0}$ is the objective function to be minimized, which is convex in $x$, and $f_{1},\ldots,f_{m}$ are inequality constraint functions that are convex in $x$. The parameter $\theta$ specifies data that can change, but is constant and given (or chosen) when we solve an instance of the problem. We refer to the parametrized problem as a *problem family*; when we specify a fixed value of $\theta \in \Theta$, we refer to it as a *problem instance*. We let $x^{\star}$ denote an optimal point for problem, assuming it exists. To emphasize its dependence on $\theta$, we write it as $x^{\star}{(\theta)}$.

Convex optimization is used in many domains, including signal and image processing \[, \], machine learning \[ \], control systems \[RMD^+^17 \], quantitative finance \[, BJK^+^24, BBD^+^17 \], and operations research \[ \].

### Differentiating through convex optimization problems

In many applications we are interested in the sensitivity of the solution $x^{\star}$ with respect to the parameter $\theta$. We will assume there is a unique solution for parameters near $\theta$, and that the mapping from $\theta$ to $x^{\star}$ is differentiable with Jacobian ${\partial{x^{\star}/{\partial\theta}}} \in \text{R}^{n \times d}$, evaluated at $\theta$. We then have where $\Delta\theta$ is the change in $\theta$, and $\Delta x^{\star}$ is the resulting change in $x^{\star}$.

We make a few comments on our assumptions. First, the solution $x^{\star}$ need not be unique, and so does not define a function from $\theta$ to $x^{\star}$. Even when the solution is unique for each parameter value, the mapping from $\theta$ to $x^{\star}$ need not be differentiable. Following universal practice in machine learning, we simply ignore these issues. When $x^{\star}$ is not unique, or when the mapping is not differentiable, we simply use some reasonable value for the (nonexistent) derivative. It has been observed that simple gradient (or subgradient) based methods for optimizing parameters are tolerant of these approximations.

Approximating the change in solution with a change in parameters can be useful by itself in some applications. As an example, consider a machine learning problem where we fit the parameters of a model to data by minimizing the sum of a convex loss function over the given training data. Considering the training data as a parameter, and the solution as the estimated model parameters, the Jacobian above gives us the sensitivity of each model parameter with respect to the training data. In particular, these sensitivities are sometimes used to compute a risk estimate for the learned model parameters \[, \]. As another example, suppose we model some economic variables (e.g., consumption, demand for products, trades) as maximizing a concave utility function that depends on parameters. The Jacobian here directly gives us an approximation of the change in demand (say) when the utility parameters change.

### Autodifferentiation framework

The solution map derivative is much more useful when it is part of an autodifferentiation system such as JAX \[BFH^+^18\], PyTorch \[PGC^+^17\], or Tensorflow \[ABC^+^16\]. We consider a scalar function that is described by its compution graph, which can include standard operations and functions, as well the solution of one or more convex optimization problems. We can compute the gradient of this function automatically, and this can be used for applications such as tuning or optimizing the performance of a system. We give a few simple generic examples here.

In machine learning, we fit model parameters (also called weights or coefficents) using convex optimization, but we may have other hyper-parameters (e.g., that scale regularization terms) that we would like to tune to get good performance on an unseen, out-of-sample test data set. The scalar function that we differentiate is the loss function computed with test data, and we differentiate with respect to the hyper-parameters of the machine learning model. A similar situation occurs in finance, where the actual trades to execute are determined by solving a parameterized problem \[BBD^+^17\], which also contains a number of hyper-parameters that set limits on the portfolio or trading, or scale objective terms, and our goal is to obtain good performance on a simulation that uses historical data, i.e., a back-test. In this case, the scalar function that we optimize might be a metric like the realized portfolio return or the Sharpe ratio, and we differentiate with respect to the hyper-parameters of the portfolio construction model.

### Related work

### Differentiating through convex optimization problems

There are two main classes of methods to differentiate the mapping from problem parameters to the solution. First, autodifferentiation software like PyTorch \[PGC^+^17\] and Tensorflow \[ABC^+^16\], as commonly used in backpropagation for machine learning, would differentiate through all instructions of an iterative optimization algorithm. While these tools are commonly used in the deep learning domain, they neglect the structure and optimality conditions of, particularly, convex optimization problems.

Second, as less of a brute-force approach, one can directly differentiate through the optimality conditions of a convex optimization problem, also referred to as *argmin differentiation* \[ABB^+^19, \]. CVXPYlayers \[AAB^+^19\] is based on prior work on differentiating through a cone program, called diffcp \[ABB^+^19\], and provides interfaces to PyTorch and Tensorflow. OptNet addresses quadratic programs. Least squares auto-tuning is a specialized hyper-parameter tuning framework for least squares problems, i.e., a subclass of quadratic programs, with parametrized problem data. It admits flexible tuning objectives and tuning regularizers (called hyper-hyper-parameters), and computes their gradient with respect to the parameters of the least squares problem. PyEPO combines various autodifferentiation and argmin differentiation tools into one software suite.

### Tuning systems that involve convex optimization

Differentiating through a convex problem is useful in a broad array of applications sometimes called predict-then-optimize. In these applications we make some forecast or prediction (using convex optimization or other machine learning models), and then take some action (using convex optimization), and we are interested in the gradient of parameters appearing both in the predictor and the action policy \[, \]. In some cases, the prediction and optimization steps are fused into one black-box model that maps features to actions, called *learning to optimize from features* \[KDVC^+^24\], which avoids differentiating through an optimization problem. This approximation is not necessary when it is possible to differentiate through the optimization problem in an easy and fast way, which motivates this work.

We also mention that when the dimension of $\theta$ is small enough, the parameters can be optimized using zero-order or derivative-free methods, which do not require the gradient of the overall metric with respect to the parameters \[, AAB^+^19\]. Examples include Optuna \[ASY^+^19\], HOLA \[MBK^+^22\], for tuning parameters with respect to some overall metric, and Hyperband \[LJD^+^18\], which dynamically allocates resources for efficient hyper-parameter search in machine learning. Even when a tuning problem can be reasonably carried out using derivative-free methods, the ability to evaluate the gradient can give faster convergence with fewer evaluations.

### Domain-specific languages for convex optimization

Argmin differentiation tools like CVXPYlayers admit convex optimization problems that are specified in a domain-specific language (DSL). Such systems allow the user to specify the functions $f_{i}$ and $A$ and $b$, in a simple format that closely follows the mathematical description of the problem. Examples include YALMIP \[L0̈4\] and CVX (in Matlab), CVXPY (in Python), which CVXPYlayers is based , Convex.jl \[UMZ^+^14\] and JuMP (in Julia), and CVXR (in R). We focus on CVXPY, which also supports the declaration of parameters, enabling it to specify problem families, not just problem instances.

DSLs parse the problem description and translate (canonicalize) it to an equivalent problem that is suitable for a solver that handles some generic class of problems, such as linear programs (LPs), quadratic programs (QPs), second-order cone programs (SOCPs), semidefinite programs (SDPs), and others such as exponential cone programs. Our work focuses on LPs and QPs. After the canonicalized problem is solved, a solution of the original problem is retrieved from a solution of the canonicalized problem.

It is useful to think of the whole process as a function that maps $\theta$, the parameter that specifies the problem instance, into $x^{\star}$, an optimal value of the variable. With a DSL, this process consists of three steps. First the original problem description is canonicalized to a problem in some standard (canonical) form; then the canonicalized problem is solved using a solver; and finally, a solution of the original problem is retrieved from a solution of the canonicalized problem. When differentiating through the problem, the sequence of canonicalization, canonical solving, and retrieval is reversed. Reverse retrieval is followed by canonical differentiating and reverse canonicalization.

Most DSLs are organized as *parser-solvers*, which carry out the canonicalization each time the problem is solved (with different parameter values). This simple setting is illustrated in figure 1(a).

(a) Parser-solver calculating solution x⋆ for problem instance with parameter θ.

(b) Source code generation for problem family, followed by compilation to custom solver and custom gradient computation (new, signified with blue color). The compiled solver computes a solution x⋆ to the problem instance with parameter θ. The compiled differentiator computes the gradient Δθ given Δx.

Figure 1: Comparison of convex optimization problem parsing and solving/differentiating approaches.

### Code generation for convex optimization

We are interested in applications where we solve many instances of the problem, possibly in an embedded application with hard real-time constraints, or a non-embedded application with limited compute. For such applications, a *code generator* makes more sense.

A code generator takes as input a description of a problem family, and generates specialized source code for that specific family. That source code is then compiled, and we have an efficient solver for the specific family. In this work, we add a program that efficiently computes the gradient of the parameter-solution mapping. The overall workflow is illustrated in figure 1(b). The compiled solver and differentiator have a number of advantages over parser-solvers. First, by caching canonicalization and exploiting the problem structure, the compiled solver and the compiled differentiator are faster. Second, the compiled solver and in some applications also the compiled differentiator can be deployed in embedded systems, fulfilling rules for safety-critical code.

### Contribution

In this paper, we extend the code generator CVXPYgen \[SBD^+^22\] to produce source code for differentiating the parameter-solution mapping of convex optimization problems that can be reduced to QPs. We allow for the use of any canonical solver that is supported by CVXPYgen, including conic solvers. We combine existing theory on differentiating through the optimality conditions of a QP with low-rank updates to the factorization of quasidefinite systems \[, \] to enable very fast repeated differentiation. Along with the generated C code, we compile two Python interfaces, one for use with CVXPY and one for use with CVXPYlayers. To the best of our knowledge, CVXPYgen is the first code generator for convex optimization that supports differentiation.

We give three examples, tuning the hyper-parameters and feature engineering parameters of a machine learning model, tuning the controller weights of an approximate dynamic programming controller, and adjusting the parameters in a financial trading engine. CVXPYgen accelerates these applications by around an order of magnitude.

### Outline

The remainder of this paper is structured as follows. In §2 we describe, at a high level, how CVXPYgen generates code to differentiate through convex optimization problems. In §3 we describe the generic system tuning framework that runs the CVXPYgen solvers and differentiators, and in §4, we illustrate how we use it for three realistic examples that compare the performance of CVXPYgen to CVXPYlayers. We conclude the paper in §5.

## Differentiating with CVXPYgen

CVXPYgen is an open-source code generator, based on the Python-embedded domain-specific language CVXPY. While CVXPY treats all typical conic programs and CVXPYgen generates code to solve LPs, QPs, and SOCPs, we focus on differentiating through problems that can be reduced to a QP, i.e., LPs and QPs.

### Disciplined parametrized programming

The CVXPY language uses disciplined convex programming (DCP) to allow for modeling instructions that are very close to the mathematical problem description and to verify convexity in a systematic way. Disciplined parametrized programming (DPP) is an extension to the DCP rules for modeling convex optimization problems. While a DCP problem is readily canonicalized, a DPP problem is readily canonicalized with *affine* mappings from the user-defined parameters to the canonical parameters. Similarly, the mapping from a canonical solution back to a solution to the user-defined problem is affine for DPP problems \[AAB^+^19\]. DPP imposes mild restrictions on how parameters enter the problem expressions. In short, if all parameters enter the problem expressions in an affine way, the problem is DPP. We model all example problems in §4 DPP and illustrate standard modifications to make DCP problems DPP. Details on the DCP and DPP rules can be found at

### Differentiating through parametrized problems

Differentiating through a DPP problem consists of three steps: affine parameter canonicalization, canonical solving, and affine solution retrieval, where $\theta$ is the user-defined parameter, $C$ and $R$ are sparse matrices, and $\mathcal{S}{(\cdot)}$ is the canoncial solver. We mark the canonical parameter and solution with a tilde.

In this work, we want to propagate a gradient in terms of the current solution, called $\Delta x$, to a gradient in the parameters $\Delta\theta$. This mapping is symmetric to the solution mapping \[AAB^+^19\], i.e., and we can simply re-use the descriptions of $R$ and $C$ that CVXPYgen has already extracted for solving the problem. The following section explains how we (re)compute the canonical derivative ${({\mathsf{D}^{T}\mathcal{S}})}{({\Delta\overset{\sim}{x}};{\overset{\sim}{x}}^{\star},\overset{\sim}{\theta})}$ efficiently.

### Differentiating through canonical solver

We focus on differentiating through LPs and QPs, i.e., problems that can be reduced to the QP standard form as used by the OSQP solver \[SBG^+^20\]. The variable is $\overset{\sim}{x} \in \text{R}^{\overset{\sim}{n}}$ and all other symbols are parameters. The objective is parametrized with $P \in \text{S}_{+}^{\overset{\sim}{n}}$, where $\text{S}_{+}^{\overset{\sim}{n}}$ is the set of symmetric positive semidefinite matrices, and $q \in \text{R}^{\overset{\sim}{n}}$. The constraints are parametrized with $A \in \text{R}^{m \times \overset{\sim}{n}}$, $l \in {\text{R}^{m} \cup {\{{- \infty}\}}}$, and $u \in {\text{R}^{m} \cup {\{\infty\}}}$. If an entry of $l$ or $u$ is $- \infty$ or $\infty$, respectively, it means there is no constraint. A pair of equal entries $l_{i} = u_{i}$ represents an equality constraint.

We closely follow the approach that is used in OptNet. We denote by $A_{\mathcal{C}}$ the row slice of $A$ that contains all rows $A_{i}$ for which the lower or upper constraint is active at optimality, i.e., it holds that ${A_{i}\overset{\sim}{x}} = l_{i}$ or ${A_{i}\overset{\sim}{x}} = u_{i}$ (or both, in the case of an equality constraint). We omit the superscript $\star$ for brevity. We set $b_{\mathcal{C}}$ to contain the entries of $l$ or $u$ at the active constraints indices, i.e., ${A_{\mathcal{C}}\overset{\sim}{x}} = b_{\mathcal{C}}$. Then, the solution is characterized by the KKT system where ${\overset{\sim}{y}}_{\mathcal{C}}$ is the slice of the dual variable corresponding to the active constraints. Note that we use the sign of $\overset{\sim}{y}$ to determine constraint activity. (The first block row of system corresponds to stationarity of the Lagrangian, and the second block row corresponds to primal feasibility.)

We take the differential of and re-group the terms as where the righthand side is evaluated using algorithm 1. To avoid singularity of the linear system, we regularize the matrix diagonal with a small $\epsilon > 0$, solve the regularized system and add $N^{\text{refine}}$ steps of iterative refinement \[, \] to correct for the effect of $\epsilon$ on the solution.

1:Initialize P, A𝒞, $\Delta\overset{\sim}{x}$ 2:$K_{\mathcal{C}} = \begin{bmatrix} \end{bmatrix}$, $K_{\mathcal{C}}^{\epsilon} = {K_{\mathcal{C}} + \begin{bmatrix} \end{bmatrix}}$, $r = \begin{bmatrix} {\Delta\overset{\sim}{x}} \\Algorithm 1 Regularized system solve The regularization strength $\epsilon = 10^{- 6}$ and $N^{\text{refine}} = 3$ iterations of iterative refinement work well in most practical cases.

Ultimately, the gradients in the QP parameters are We copy the rows of $\Delta A_{\mathcal{C}}$ and $\Delta b_{\mathcal{C}}$ into the corresponding rows of $\Delta A$ and $\Delta b$, respectively, and set all other entries of $\Delta A$ and $\Delta b$ to zero.

### Low-rank updates to factorization of linear system

For the quasidefinite matrix $K_{\mathcal{C}}^{\epsilon}$ used in algorithm 1, there always exists an LDL-factorization, If the entries of $P$ or $A$ change, we perform a full re-factorization. Otherwise, we use the fact that the factors $L_{\mathcal{C}}$ and $D_{\mathcal{C}}$ change with the set of active constraints, denoted by $\mathcal{C}$. For the constraints that switch from inactive to active or vice-versa, we perform a sequence of rank-1 updates to $L_{\mathcal{C}}$ and $D_{\mathcal{C}}$.

We re-write the LDL-factorization as where lowercase symbols marked with a bar denote row/column combinations that are added or deleted. Uppercase symbols marked with a bar are sub-matrices that will be altered due to the addition or deletion.

For a constraint that switches from inactive to active, we add the respective row/column combination to $K_{\mathcal{C}}^{\epsilon}$ and run algorithm 2.

1:Solve the lower triangular system ${L_{11}D_{11}{\overline{l}}_{12}} = {\overline{k}}_{12}$ for ${\overline{l}}_{12}$ 2:${\overline{d}}_{22} = {{\overline{k}}_{22} - {{\overline{l}}_{12}^{T}D_{11}{\overline{l}}_{12}}}$ 5:Perform the rank-1 downdate ${{\overline{L}}_{33}{\overline{D}}_{33}{\overline{L}}_{33}^{T}} = {{L_{33}D_{33}L_{33}^{T}} - {ww^{T}}}$ according to algorithm 5 Algorithm 2 Row/column addition (variant of algorithm 1) If a constraint switches from active to inactive, we run algorithm 3 for row/column deletion.

5:Perform the rank-1 update ${{\overline{L}}_{33}{\overline{D}}_{33}{\overline{L}}_{33}^{T}} = {{L_{33}D_{33}L_{33}^{T}} + {ww^{T}}}$ according to algorithm 5 Algorithm 3 Row/column deletion (variant of algorithm 2) All steps of the row/column addition and deletion algorithms operate on the sparse matrices $K_{\mathcal{C}}^{\epsilon}$ and $L_{\mathcal{C}}$ stored in compressed sparse column format. The diagonal matrix $D_{\mathcal{C}}$ is stored as an array of diagonal entries. Note that ${({- {\overline{d}}_{22}})}^{1/2}$ is always real because we run algorithms 2 and 3 only for row/column combinations that are in the lower and right parts of $K_{\mathcal{C}}^{\epsilon}$ (where $A_{\mathcal{C}}$ changes), for which the diagonal entries of $D_{\mathcal{C}}$ are all negative by quasidefiniteness of $K_{\mathcal{C}}^{\epsilon}$.

It is important to note that all steps, including step 5 in both algorithms, are of at most quadratic complexity, whereas a full re-factorization would be of cubic complexity. When only a few constraints switch their activity, this procedure is considerably faster than full re-factorizations. This is demonstrated in §4 for three practical cases. In the worst case where all constraints switch to active or inactive between two consecutive solves, the complexity returns to cubic.

Open source code and full documentation for CVXPYgen and its differentiation feature is available at

## System tuning framework

We present a generic tuning method for systems of the form where $p \in \text{R}$ is a performance objective, $\Gamma$ evaluates the system, which includes many solves of the convex optimization problem, possibly sequentially, and $\omega \in \Omega \subseteq \text{R}^{p}$ is a *design*, where $\Omega$ is the design space, i.e., the set of admissible designs. Then, we describe in detail what $\Gamma$ and $\omega$ are, for two important classes of system tuning.

### A generic tuning method

We compute the gradient ${\nabla\Gamma}{(\omega)}$ using the chain rule and our ability to differentiate through DPP problems. We use ${\nabla\Gamma}{(\omega)}$ in a simple projected gradient method \[, \] to optimize the design $\omega$.

We use Euclidean projections onto the design space $\Omega$, denoted by $\Pi{( \cdot )}$, and a simple line search to guarantee that the algorithm is a descent method. If the performance is improved with the current step size, we use it for the current iteration and increase it by a constant factor $\beta > 1$ for the next iteration. Otherwise, we repeatedly shrink the step size by a constant factor $\eta > 1$ until the performance is improved. The simple generic design method we use is given in algorithm 4.

5: ωk + 1 = ω̂, αk + 1 = βαk ⊳ accept update and increase step size 7: αk ← αk/η, go to step 3 ⊳ shrink step size and re-evaluate 10:until ∥ωk − Π(ωk − αk∇Γ(ωk))∥2 ≤ ϵrel∥ωk∥2 + ϵabs Algorithm 4 Projected gradient descent Note that algorithm 4 assumes that $\Gamma{(\omega)}$ is to be minimized. If $\Gamma{(\omega)}$ is to be maximized, replace it with $- {\Gamma{(\omega)}}$.

### Initialization

We initialize $\omega^{0}$ to a value that is typical for the respective application and $\alpha^{0}$ with the clipped Polyak step size where $\hat{p}$ is an estimate for the optimal value of the performance objective. We clip the step size at 1 to avoid too large initial steps due to local concavity. The algorithm is not particularly dependent on the line search parameters $\beta$ and $\eta$. Reasonable choices are, e.g., $\beta = 1.2$ and $\eta = 1.5$.

### Stopping criterion

We stop the algorithm as soon as the termination criterion with ${\epsilon^{\text{rel}},\epsilon^{\text{abs}}} > 0$ is met. This is also referred to as the *projected gradient* being small. When $\Gamma$ is convex, this corresponds to the first-order optimality condition, i.e., the gradient ${\nabla\Gamma}{(\omega^{k})}$ lying in (or close to) the normal cone to $\Omega$ at $\omega^{k}$. Depending on the application, the stopping tolerances $\epsilon^{\text{rel}}$ and $\epsilon^{\text{abs}}$ might range between $10^{- 2}$ and $10^{- 6}$.

### Tuning hyper-parameters of machine learning models

We call the data points used for *training* a machine learning model ${{(z_{1},y_{1})},\ldots,{(z_{N},y_{N})}} \in \mathcal{D}$, where each data point consists of features $z_{i}$ and output $y_{i}$. For the design $\omega$ of the machine learning model, we consider any hyper-parameters, including pre-processing parameters that determine how the data ${(z_{1},y_{1})},\ldots,{(z_{N},y_{N})}$ is modified before fitting the model.

For any choice of $\omega$, we find the model weights $\beta \in \text{R}^{n}$ as where $\ell:{{\mathcal{D} \times \text{R}^{n} \times \Omega}\rightarrow\text{R}}$ is the training loss function and $r:{{\text{R}^{n} \times \Omega}\rightarrow\text{R}}$ is the regularizer. While the entries of $\beta$ are oftentimes referred to as *model parameters* in the machine learning literature, we call them *weights* to make clear that they enter the above optimization problem as variables (and not as parameters of the optimization problem). Both $\ell$ and $r$ are parametrized by the design $\omega$. In the case of $\ell$, the design $\omega$ might enter in terms of pre-processing parameters like thresholds for processing outliers. In the case of $r$, the design $\omega$ might enter as the scaling of the regularization term. In the remainder of this work, we consider $\ell$ and $r$ that are convex and quadratic, admitting the differentiation method described in §2.

We choose $\omega$ to minimize the validation loss where $\ell^{\text{val}}:{{\mathcal{D} \times \text{R}^{n} \times \Omega}\rightarrow\text{R}}$ is the validation loss function, with validation data $(z_{i}^{\text{val}},y_{i}^{\text{val}})$ that is different from and ideally uncorrelated with the training data. Here, $\ell^{\text{val}}$ need not be convex (or quadratic), since we use the projected gradient method described in §3.1. Note that the design $\omega$ enters $\ell^{\text{val}}$ both directly (for example as pre-processing parameters) and through the optimal model parameters $\beta^{\star}{(\omega)}$.

If $\ell^{\text{val}}$ is the squared error (between data and model output), then the alternative performance objective is more meaningful, as it resembles the root mean square error (RMSE).

### Cross validation

For better generalization of the optimized $\omega$ to unseen data, we can employ cross validation (CV) \[, \]. We split the set of data points into $J$ partitions or *folds* (typically equally sized) and train the model $J$ times. Every time, we take $J - 1$ folds as training data and $1$ fold as validation data. We compute the performance $p_{j}$ as described above, where the subscript $j$ denotes that the validation data $(z_{i}^{\text{val}},y_{i}^{\text{val}})$ is that of the $j$th fold. Then, we average these over all folds as This is usually referred to as the cross validation loss. Similarly, if $\ell^{\text{val}}$ is the squared error, we compute the cross-validated RMSE ${\overline{p}}^{\text{CV}}$ by averaging all ${\overline{p}}_{j}$.

### Tuning the weights of convex optimization control policies

We consider a convex optimization control policy (COCP) that determines a control input $u \in \mathcal{U} \subseteq \text{R}^{m}$ that is applied to a dynamical system with state $x \in \mathcal{X} \subseteq \text{R}^{n}$, by solving the convex optimization problem Here, $\phi:{{\mathcal{X} \times \Omega}\rightarrow\mathcal{U}}$ is a family of control policies, parametrized by $\omega$, and $x$ is the current measurement (or estimate) of the state of the dynamical system. The loss function $\ell:{{\mathcal{X} \times \mathcal{U} \times \Omega}\rightarrow\text{R}}$ is parametrized by the design $\omega$, which might involve controller weights, for example.

We choose $\omega$ to minimize the closed-loop loss where the loss function $\ell^{\text{cl}}:{{\mathcal{X} \times \Omega}\rightarrow\text{R}}$ involves a simulation or real experiment starting from the initial state $x_{0}$ and using the control policy $u = {\phi{(x;\omega)}}$.

## Numerical experiments

In this section we present three numerical examples, comparing the solve and differentiation speed of CVXPYgen with CVXPYlayers, for system tuning with the framework presented in §3.1. In all three cases we take OSQP as the canonical solver for CVXPYgen and Clarabel as the canonical solver for CVXPYlayers (since it only supports conic solvers). The code that was used for the experiments is available at

### Elastic net regression with winsorized features

We consider a linear regression model with elastic net regularization, which is a sum of ridge (sum squares) and lasso (sum absolute) regularization, each of which has a scaling parameter. In addition, we clip or *winsorize* each feature at some specified level to mitigate the problem of feature outliers. The clipping levels for each feature are also parameters.

We consider $m$ data points with one observation and $n$ features each. We start with a set of observations $y_{i} \in \text{R}$ and raw features $z_{i} \in \text{R}^{n}$, where $z_{i,j}$ is the $j$th feature for the $i$th observation, subject to outliers. We obtain the winsorized features $x_{i} \in \text{R}^{n}$ by clipping the $n$ components at winsorization levels $w \in \text{R}_{+ +}^{n}$ (part of the design) as The training loss function and regularizer as in §3.2 are where $\lambda \geq 0$ and $\gamma \geq 0$ are the the ridge and lasso regularization factors, respectively. Since the model performance depends mainly on the orders of magnitude of $\lambda$ and $\gamma$, we write them as $\lambda = 10^{\mu}$ and $\gamma = 10^{\nu}$.

Together with the winsorization levels $w$, the design vector becomes $\omega = {(w,\mu,\nu)} \in {\text{R}_{+ +}^{n} \times \text{R}^{2}}$. We allow to clip $z_{i}$ between 1 and 3 standard deviations and search the elastic net weights across 7 orders of magnitude. We assume that the entries of $z_{i}$ are approximately centered and scaled, i.e., have zero mean and standard deviation 1. The design space becomes The validation loss function $\ell^{\text{val}}$ is identical to the training loss function $\ell$ and the performance objective is the cross-validated RMSE ${\overline{p}}^{\text{CV}}$ from §3.2.

### Code generation

Figure 2 shows how to generate code for this problem.

2from cvxpygen import cpg 5beta = cp.Variable(n, name=’beta’) 6X = cp.Parameter((m-m//J, n), name=’X’) 7l = cp.Parameter(nonneg=True, name=’l’) 8g = cp.Parameter(nonneg=True, name=’g’) 9prob = cp.Problem(cp.Minimize(cp.sum_squares(X @ beta - y) + l * cp.sum_squares(beta) + g * cp.norm(beta, 1))) 12cpg.generate_code(prob, gradient=True) 14# use CVXPYlayers interface 15from cvxpylayers.torch import Cvxpylayer 16from cpg_code.cpg_solver import forward, backward 17layer = Cvxpylayer(prob, parameters=[X,l,g], variables=[beta], custom_method=(forward, backward)) 18p = Gamma(w, mu, nu) # involves beta_solution = layer(...) 20print(w.grad, mu.grad, nu.grad) Figure 2: Code generation and CVXPYlayers interface for elastic net example. The integers m, n, and J, the constant y, the function Gamma, and the torch tensors w, mu, and nu are pre-defined.

The problem is modeled with CVXPY in lines 5--9. Code is generated with CVXPYgen in line 12, where we use the `gradient=True` option to generate code for computing gradients through the problem. After importing the CVXPYlayers interface in line 16, it is passed to the `Cvxpylayer` constructor in line 17 through the `custom_method` keyword. The performance objective is computed in line 18 and differentiated in line 19.

### Data generation

We take $m = 100$ data points, $n = 20$ features, and $J = 10$ CV folds. For every fold, we reserve ${m/J} = 10$ data points for validation and use the other $90$ data points for training. We generate the features ${\overline{z}}_{i}$ without outliers by sampling from the Gaussian $\mathcal{N}{}$. Then, we sample $\overline{\beta} \sim {\mathcal{N}{(0,I)}}$ and set noisy labels $y_{i} = {{{\overline{z}}_{i}^{T}\overline{\beta}} + \xi_{i}}$ with $\xi_{i} \sim {\mathcal{N}{(0,0.01)}}$. Afterwards, we simulate feature outliers due to, e.g., data capturing errors. For every feature, we randomly select ${m/10} = 10$ indices and increase the magnitude of the respective entries of ${\overline{z}}_{i}$ to a value $\sim {\mathcal{U}{\lbrack 2,4\rbrack}}$, i.e., between 2 and 4 standard deviations, and save them in $z_{i}$. We estimate the optimal cross-validated RMSE as $\hat{p} = 0.1$ corresponding to the standard deviation of the noise $\xi$ (if it was known). This is a very optimistic estimate, since it implies that the data is outlier-free after winsorization. The tuning parameters are initialized to $\omega^{0} = {(w,\mu,\nu)}^{0} = {({3 \cdot \mathbf{1}},0,0)}$. We set the termination tolerances to $\epsilon^{\text{rel}} = \epsilon^{\text{abs}} = 10^{- 3}$.

### Results

The projected gradient method terminates after $11$ steps with a reduction of the cross-validated RMSE from $2.85$ to $2.12$, as shown in figure 3.

Figure 3: CV loss over tuning iterations.

Figure 4 shows the tuned winsorization thresholds $w$ and we obtain $\lambda \approx 0.68$ and $\gamma \approx 0.80$.

Figure 4: Thresholds before (magenta) and after tuning (blue). The dashed black lines show the range of possible winsorization thresholds.

### Timing

Table 1 shows that the speed-up factor for the gradient computations is about 5. The speed-up for the full tuning loop is reduced due to Python overhead.

Solve and Gradient Table 1: Computation times with CVXPY and CVXPYgen for the elastic net example.

### Approximate dynamic programming controller

We investigate controller design with an ADP controller \[, \] where the state and input cost parameters are subject to tuning.

We are given the discrete-time dynamical system with state $x_{t} \in \text{R}^{n}$, input $u \in \text{R}^{m}$ limited as ${\| u\|}_{\infty} \leq 1$, and state disturbance $w_{t}$, where $w_{t}$ are unknown, but assumed IID $\mathcal{N}{(0,W)}$, with $W$ known. The matrices $A \in \text{R}^{n \times n}$ and $B \in \text{R}^{n \times m}$ are the given state transition and input matrices, respectively.

We seek a state feedback controller $u_{t} = {\phi{(x_{t})}}$ that guides the state $x_{t}$ to zero while respecting the constraint ${\| u\|}_{\infty} \leq 1$. We judge a controller $\phi$ by the metric where $Q \in \text{S}_{+}^{n}$ and $R \in \text{S}_{+ +}^{m}$ are given. We assume that the matrix $A$ contains no unstable eigenvalues with magnitude beyond $1$, such that $J$ is guaranteed to exist. Corresponding to §3.3, we will take our performance metric as where $T$ is large and fixed, and $w_{t}$ are sampled from $\mathcal{N}{(0,W)}$. Note that all $x_{1},\ldots,x_{T - 1}$ and $u_{0},\ldots,u_{T - 1}$ are fully determined by the initial state $x_{0}$, the controller $\phi{(x;\omega)}$, and the system dynamics.

When the input constraint is absent, we can find the optimal controller (i.e., the one that minimizes $J$) using dynamic programming, by minimizing a convex quadratic function, where the matrix $P^{\text{lqr}} \in \text{S}_{+ +}^{n}$ is the solution of the algebraic Riccati equation (ARE) for discrete time systems. The minimizer is readily obtained analytically, with $u$ a linear function of the state $x_{t}$. See, e.g., \[\].

We will use an approximate dynamic programming (ADP) controller The controller is designed by $\omega = Z$ with $\Omega = \text{S}_{+}^{n}$. The state $x_{t}$ is another parameter and the matrices $A$, $B$, $P^{\text{lqr}}$, and $R$ are constants.

The quadratic form in the objective makes the above formulation non-DPP. We render the problem DPP as where the DPP parameter $\theta$ consists of $g = {L^{T}Ax_{t}}$ and $H = {L^{T}B}$. Here, $L = {\operatorname{\mathbf{C}\mathbf{h}\mathbf{o}\mathbf{l}}{({P^{\text{lqr}} + Z})}}$, where $\operatorname{\mathbf{C}\mathbf{h}\mathbf{o}\mathbf{l}}{(\cdot)}$ returns the lower Cholesky factor of its argument. In other words, ${LL^{T}} = {P^{\text{lqr}} + Z}$ and $L$ is lower triangular. (When running our projected gradient descent algorithm, we modify $L$ instead of $Z$ and recover $Z = {{LL^{T}} - P^{\text{lqr}}}$ at the end of the tuning).

### Data generation

We choose $n = 6$ states and $m = 3$ inputs. We consider an open-loop system $A = {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}a}$ with stable and unstable modes sampled from $\lbrack 0.99,1.00\rbrack$. The entries of the input matrix $B$ are sampled from $\lbrack{- 0.01},0.01\rbrack$. We initialize the state at the origin and simulate for $T = 1000$ steps with noise covariance $W = {0.1^{2}I}$. The *true* state and input cost matrices are $Q = R = I$, respectively, which we use to compute $P^{\text{lqr}}$ as the solution to the ARE. We initialize $\omega^{0} = Z^{0} = 0$ and estimate the optimal control performance $\hat{p}$ by running the simulation with the input constraint of the controller removed. We use $\epsilon^{\text{rel}} = \epsilon^{\text{abs}} = 0.005$.

### Results

The projected gradient descent algorithm terminates after 16 gradient steps with a reduction of the control objective from $8.23$ to $6.32$, as shown in figure 5.

Figure 5: Control performance over tuning iterations.

### Timing

The gradient computations are sped up compared to CVXPY by a factor of about 40. Including Python overhead, the whole tuning loop is still sped up by a factor of about 6, as shown in table 2.

Solve and gradient Table 2: Computation times with CVXPY and CVXPYgen for the ADP controller tuning example.

### Portfolio optimization

We consider a variant of the classical Markowitz portfolio optimization model with holding cost for short positions, transaction cost, and a leverage limit \[BJK^+^24, \], embedded in a multi-period trading system \[BBD^+^17\].

We want to find a fully invested portfolio of holdings in $N$ assets. The holdings are represented relative to the total portfolio value, in terms of weights $w \in \text{R}^{N}$ with ${\mathbf{1}^{T}w} = 1$. The expected portfolio return is $\mu^{T}w$, with esimated returns $\mu \in \text{R}^{N}$. The variance or risk of the portfolio return is $w^{T}\Sigma w$, with estimated asset return covariance $\Sigma \in \text{S}_{+ +}^{N}$. We assume that $\mu$ and $\Sigma$ are pre-computed, which we will detail later. We approximate the cost of holding short positions as $\kappa^{\text{hold}}\mathbf{1}^{T}w_{-}$, where $\kappa^{\text{hold}}$ describes the (equal) cost of holding a short position in any asset. Subscript "$-$" denotes the negative part, i.e., $w_{-} = {\max{\{{- w},0\}}}$. We approximate the transaction cost as $\kappa^{\text{tc}}{\|{w - w^{\text{pre}}}\|}_{1}$, where $\kappa^{\text{tc}}$ describes the cost of trading any asset and $w^{\text{pre}}$ is the pre-trade portfolio. We solve where ${w,{\Delta w}} \in \text{R}^{N}$ are the variables. We introduced the variable $\Delta w$, also referred to as the *trade vector*, to prevent products of parameters and render the problem DPP. Problem can also be seen as a convex optimization control policy as described in §3.3, where the expected returns $\mu$ (updated once per trading period) and the previous portfolio $w^{\text{pre}}$ are the state $x$ and the trade $\Delta w$ is the input $u$. Our design consists of the leverage limit $L$ and the aversion factors ${\gamma^{\text{risk}},\gamma^{\text{hold}},\gamma^{\text{tc}}} > 0$ for risk, holding cost, and short-selling cost, respectively. Since the model performance depends primarily on the orders of magnitude of these factors, we write them as and tune $\omega = {(L,\nu^{\text{risk}},\nu^{\text{hold}},\nu^{\text{tc}})}$, restricted to the design space We keep the risk $\Sigma$ and costs $\kappa^{\text{hold}}$ and $\kappa^{\text{tc}}$ constant.

We evaluate the performance of the model via a back-test over $h$ trading periods. After solving problem at a given period, we trade to $w^{\star}$, pay short-selling cost $\kappa^{\text{hold}}\mathbf{1}^{T}w_{-}^{\star}$ and transaction cost $\kappa^{\text{tc}}{\|{w^{\star} - w^{\text{pre}}}\|}_{1}$, experience the returns $r_{t}$, and re-invest the full portfolio value. Hence, the total portfolio value evolves as The pre-trade portfolio for the following trading period is re-balanced as and the portfolio realized return at period $t$ is We consider the average return and portfolio risk, respectively, and annualize them as where $h^{\text{ann}}$ is the number of trading periods per year. We take their ratio as performance metric, the so-called *Sharpe ratio (SR)*,

### Data generation

We consider three adjacent intervals of trading periods. First, we use a *burn-in* interval to compute the estimate for the expected returns at later time periods and to compute the constant risk estimate. Second we take a *tune* interval to perform parameter optimization. Third, we use a *test* interval to evaluate the final parameter choice out-of-sample. We denote the lengths of the three intervals by $h^{\text{burnin}}$, $h^{\text{tune}}$, and $h^{\text{test}}$, respectively.

We compute the expected return $\mu_{t}$ for the holdings at time $t$ as the back-looking moving average of historical returns $r_{t}$ with window size $h^{\text{burnin}}$. To compute the constant risk estimate, we first compute the empirical covariance $\hat{\Sigma}$ of returns over the burn-in interval. Then, we fit the standard factor model to $\hat{\Sigma}$, where $F \in \text{R}^{N \times K}$ is the factor loading matrix and the diagonal matrix $D \in \text{S}_{+ +}^{N}$ stores the variance of the idiosyncratic returns.

We consider $N = 25$ stock assets, chosen randomly from the S&P 500, where historical return data is available from 2016--2019. While this clearly imposes survivership bias, the point of this experiment is not to find realistic portfolios but rather to assess the numerical performance of CVXPYgen. We choose $K = 5$ factors, $h^{\text{burnin}} = 260$, $h^{\text{tune}} = 520$, $h^{\text{test}} = 260$, and we take the number of trading periods per year as $h^{\text{ann}} = 260$, i.e., we trade once a day. In other words, we use data from the year 2016 as burn-in interval for estimating $\mu_{t}$ and to estimate $\Sigma$. We tune the model with data from the years 2017 and 2018 and test it with data from the year 2019. We fix $\kappa^{\text{hold}} = \kappa^{\text{tc}} = 0.001$. We estimate the optimal Sharpe ratio to be roughly $\hat{p} = 1$. We initialize the design vector as $\omega^{0} = {(L,\nu^{\text{risk}},\nu^{\text{hold}},\nu^{\text{tc}})}^{0} = {}$. We set the termination tolerances to $\epsilon^{\text{rel}} = \epsilon^{\text{abs}} = 0.03$.

### Results

The projected gradient descent algorithm terminates after 7 iterations and improves the Sharpe ratio by a bit more than $0.1$, from $0.69$ to $0.80$, where it is saturating, as shown in figure 6.

Figure 6: Sharpe ratio over tuning iterations.

The values of the tuning parameters are changed to $\gamma^{\text{risk}} \approx 10$, $\gamma^{\text{hold}} \approx 1$, $\gamma^{\text{tc}} \approx 1.2$, and $L \approx 1$. Figure 7 contains the portfolio value over the trading periods used for tuning and out-of-sample, before and after tuning, respectively.

Figure 7: Portfolio value evolution before (dashed line) and after tuning (solid line). Blue and pink color represent the tuning and testing intervals, respectively.

Table 3 contains the respective Sharpe ratios. While the tuning interval appears to be a difficult time period with large drawdown in the middle and the end of the interval, the Sharpe ratio is improved out-of-sample from an already high level.

Table 3: Sharpe ratios.

### Timing

Table 4 shows the solve and differentiation times. The gradient computations are sped up by a factor of about 10. Including Python overhead, the overall tuning loop is sped up by a factor of about 3.

Solve and gradient Table 4: Computation times with CVXPY and CVXPYgen for the portfolio optimization example.

## Conclusions

We have added new functionality to the code generator CVXPYgen for differentiating through parametrized convex optimization problems. Users can model their problem in CVXPY with instructions close to the math, and create an efficient implementation of the gradient computation in C, by simply setting an additional keyword argument of the CVXPYgen code generation method. Our numerical experiments show that the gradient computations are sped up by around one order of magnitude for typical use cases.
