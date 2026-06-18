<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Parametric Convex Functions

Topics include Convex optimization, Optimization, Learning, Convex function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A parametrized convex function depends on a variable and a parameter, and is convex in the variable for any valid value of the parameter. Such functions can be used to specify parametrized convex optimization problems, i.e., a convex optimization family, in domain specific languages for convex optimization. In this paper we address the problem of fitting a parametrized convex function that is compatible with disciplined programming, to some given data. This allows us to fit a function arising in a convex optimization formulation directly to observed or simulated data. We demonstrate our open-source implementation on several examples, ranging from illustrative to practical.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Parametrized convex functions", "weight": 1.0} -->

A *parametrized convex function* (PCF) $f$ has the form

<!-- chunk {"id": "body-0004", "role": "body", "section": "Parametrized convex functions", "weight": 1.0} -->

where $\Theta \subseteq \text{R}^{p}$. To be a PCF, $f$ must be continuous in $\theta$, and for each $i = {1,\ldots,d}$, $f_{i}{(x,\theta)}$ is convex in $x$ for any $\theta \in \Theta$. We refer to the first argument $x$ of the PCF $f$ as the *variable*, and the second argument $\theta$ as the *parameter*. When $d = 1$, we refer to $f$ as a scalar PCF.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

The terms variable and parameter in a PCF are taken from disciplined convex programming (DCP), a method for expressing a PCF as an expression in a domain specific language (DSL) constructed from variables, constants, parameters, and a small library of functions called atoms. In DCP, the expression must be constructed in a specific way that corresponds to a composition rule that establishes convexity of the function with respect to the variable, for any valid parameter.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Disciplined convex programming", "weight": 1.0} -->

Functions expressed in DCP form can be used to form a parametrized convex optimization problem or convex optimization family. When the parameters are given specific numerical values, we obtain a problem instance, which can be solved by automatically transforming the problem instance to a canonical form, solving the canonical form, and then retrieving the solution of the original problem instance from the solution of the canonicalized problem instance. Examples of DSLs that leverage DCP for modeling convex optimization problems (and support parameters) include CVXPY (in Python), CVXR (in R), Convex.jl \[UMZ^+^14\] and JuMP (in Julia). Precursors that do not handle parameters include CVX and YALMIP \[L0̈4\] (in Matlab).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Examples", "weight": 1.0} -->

PCFs arise in many applications, including control, machine learning, resource allocation, and finance, to name just a few. We describe below a few typical ones, some specific and some more generic. In our examples we assume that $f$ is a scalar PCF.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Fuel use map", "weight": 1.0} -->

Here $f{(x,\theta)}$ gives the instantaneous fuel use rate. The variable $x$ might correspond to thrust or power output, variables that typically appear in an optimization problem; the parameter $\theta$ contains additional parameters that affect the fuel use, such as temperature. When modeling the total fuel use of a set of actuators on a moving vehicle, $x$ can represent the net force and torque on the vehicle, and $\theta$ can contain the vehicle orientation, which would affect which actuators are used to obtain the required force and torque.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Battery aging model", "weight": 1.0} -->

Here $f{(x,\theta)}$ gives the rate of aging of a battery, i.e., reduction of capacity due to use, relative to the initial battery capacity. The variable $x$ corresponds to the battery charge/discharge rate, which might appear in an optimization problem. The parameter $\theta$ contains other quantities that affect aging of the battery, such as its temperature.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Convex optimization control policy (COCP)", "weight": 1.0} -->

A control policy maps the context, i.e., what is known at a given time, such as the state of a dynamic system and other measurable quantities, into an action denoted $u \in \mathcal{U} \subseteq \text{R}^{r}$. In a convex optimization control policy (COCP) the action $u$ is found as the solution of a convex optimization problem that is parametrized by the context. As a concrete example, $f{(x,\theta)}$ gives the cost of the action $u$, combined with the long term cost of the next state, which depends on the action. The parameter $\theta$ contains the context observed when computing the control action \[RMD^+^17 \].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Resource allocation", "weight": 1.0} -->

Here $f{(x,\theta)}$ gives the cost (or negative utility) of providing resources specified by the vector $x \in \text{R}^{n}$ to $n$ agents. The parameter $\theta$ might contain information like time of the year, month, or day.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Financial portfolio construction", "weight": 1.0} -->

The goal of financial portfolio construction is to find a portfolio of financial assets that maximizes the expected return of the portfolio while limiting the investment risk. The function $f{(x,\theta)}$ might represent a combination of expected return and risk as a function of $x$, which describes the portfolio. The parameter $\theta$ provides information about market conditions, or current forecasts.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning a parametrized convex function", "weight": 1.0} -->

This paper concerns learning a PCF $f$ from data, i.e., fitting a PCF to data,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning a parametrized convex function", "weight": 1.0} -->

The PCF $f$ is specified by its architecture and a choice of *model weights*, which we denote $w \in \text{R}^{q}$. We require our approximation $f$ to be DCP expressible, which implies that it can be used to construct parametrized convex problems. This fitting method allows us to learn a DCP expression directly from observed (or generated) data.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Fitting method", "weight": 1.0} -->

We use a standard regularized loss method to choose a set of model weights. Let $\ell:{{\text{R}^{q} \times \text{R}^{n} \times \Theta \times \text{R}^{d}}\rightarrow\text{R}}$ denote a loss function, and $r:{\text{R}^{q}\rightarrow\text{R}}$ a regularizer function. The loss function is used to judge how well our approximation fits the data, and the regularization function is meant to penalize complexity. We choose $w$ to (approximately) minimize the regularized average loss,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Fitting method", "weight": 1.0} -->

where $\lambda \geq 0$ is a hyper-parameter that scales the regularization. In this context we refer to the data as training data, since it is used to train or learn the PCF.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Fitting method", "weight": 1.0} -->

As in all data fitting methods we judge a candidate PCF by its accuracy on unseen data. (The loss used to evaluate the model can differ from the loss $\ell$ used to train the model.) To find a PCF that performs well on unseen data we use the standard technique of cross-validation. We partition the original data into $K$ groups of approximately equal size, called folds, and for each fold we train the model weights on the data not including that fold, and evaluate the average loss on the data in that fold. We average the losses for the $K$ folds to obtain an overall fitting metric. We choose the architecture and the regularization hyper-parameter $\lambda$ so as to minimize the overall fitting metric. Once the architecture and hyper-parameter are chosen, we fit the PCF using all the data.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Special cases", "weight": 1.0} -->

The PCF learning problem, i.e., minimizing, reduces to well known problems in special cases. When $n = 0$, i.e., there is no variable, it reduces to the very general problem of fitting a continuous function from $\Theta$ into $\text{R}^{d}$. When $p = 0$ (or $\Theta$ is a singleton), there is (effectively) no parameter, and the problem reduces to fitting a convex function to some given data. Several architectures have been developed for this task, such as input-convex neural networks, which we build.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Non-parametric PCF fitting problems", "weight": 1.0} -->

We can solve several more general fitting problems exactly, with no constraint on the architecture (i.e., non-parametric) and no regularization. When $p = 0$ and the loss is convex in $y$, the problem of minimizing the average loss over all convex functions, which is an infinite-dimensional non-parametric fitting problem, can be solved exactly using convex optimization, as decribed in \[, §5.5.5\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Non-parametric PCF fitting problems", "weight": 1.0} -->

This can be extended to the more general case when $p > 0$ and $r = 0$. To do this we collect the data into groups associated with unique values of $\theta$, and for each one, we fit a convex function to these data as described above. We can then interpolate these functions for values of $\theta$ not appearing in the data. This solution globally minimizes the loss, but since it does not include any penalty on complexity of $f$, it is very likely to perform poorly on unseen data.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contribution", "weight": 1.0} -->

We provide a seamless path from data to a PCF that can be used for parametrized convex optimization. Our open-source implementation LPCF offers a simple user interface for fitting a PCF to variable-parameter-output triples and a variety of extensions for PCFs with special properties and uses. The resulting PCFs can be exported for immediate use in optimization frameworks like JAX \[BFH^+^18\] or CVXPY.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Outline", "weight": 1.0} -->

In § we propose an architecture, which is a generalization of input-convex neural networks that handles parameters, and describe our specific implementation. In § we describe a set of extensions that allow for modeling more specialized types of PCFs. In § we give some numerical results for both simple illustrative examples and some practical ones. In § we conclude the paper.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Architecture", "weight": 1.0} -->

Let $\phi:{\text{R}\rightarrow\text{R}}$ be a nondecreasing convex activation function, such as rectified linear unit (ReLU) with ${\phi{(a)}} = {\max{\{ a,0\}}}$ or softplus with ${\phi{(a)}} = {\log{({1 + e^{a}})}}$, that we will also refer to as *logistic* due to its use in formulating logistic regression problems. We have $L$ layers, with $z^{l} \in \text{R}^{n_{l}}$ the activation of layer $l$, $l = {1,\ldots,{L - 1}}$. We have

<!-- chunk {"id": "body-0024", "role": "body", "section": "Architecture", "weight": 1.0} -->

where $\phi$ is applied componentwise. Here $W^{l} \in \text{R}^{n_{l} \times n_{l - 1}}$ is the weight matrix associated with layer $l$, $V^{l} \in \text{R}^{n_{l} \times n}$ is the weight matrix that feeds the input $x$ into layer $l$, and $\omega_{l} \in \text{R}^{n_{l}}$ is the offset for layer $l$. We can take $W^{1} = 0$ without loss of generality since $z^{0} = x$. This is a standard residual network architecture, with feedforward from the input $x$ into each layer.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Architecture", "weight": 1.0} -->

We take the weight matrices $W^{l}$, $V^{l}$, and offsets $\omega^{l}$ to be a function of the parameter $\theta$,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Architecture", "weight": 1.0} -->

where $\psi:{\Theta\rightarrow\text{R}^{m}}$ describes a generic neural network architecture with output dimension

<!-- chunk {"id": "body-0027", "role": "body", "section": "Architecture", "weight": 1.0} -->

(We will impose one constraint on the function $\psi$, described below.) We denote the weight matrices and offsets as $W^{l}{(\theta)}$, $V^{l}{(\theta)}$ and $\omega^{l}{(\theta)}$ to emphasize their dependence on the parameter $\theta$. The model weights $w$ defining the loss in are the weights defining $\psi$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Architecture", "weight": 1.0} -->

The proposed architecture is given by and. It is specified by the layer dimensions $n_{1},\ldots,n_{L - 1}$ (the final layer width $n_{L}$ is fixed to $d$) and the architecture for $\psi$. This architecture determines a function $f:{{\text{R}^{n} \times \Theta}\rightarrow\text{R}^{d}}$, illustrated as a block diagram in figure. The model weights $w$ associated with $f$ are the model weights appearing in the righthand side of.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convexity", "weight": 1.0} -->

We impose one restriction on the weight matrices: $W^{l}{(\theta)}$ are elementwise nonnegative, for any $\theta \in \Theta$. This can be enforced by the architecture of $\psi$, for example by having the weight matrices $W^{l}{(\theta)}$ come directly from a nonnegative activation function such as ReLU or logistic, without any offset.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convexity", "weight": 1.0} -->

With this restriction, the function $f$ is a PCF. We argue using recursion that each element of $z^{l}$ is a convex function of $x$, for any fixed $\theta$. It is evidently true for $l = 1$. Assuming that each element of $z^{l - 1}$ is a convex function of $x$, we observe that each entry of

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convexity", "weight": 1.0} -->

is a convex function of $x$, since it is a nonnegative weighted sum of convex functions, plus an affine function of $x$. By the composition rule \[, §3.2.4\], each entry of $z^{l}$ is a convex function of $x$. This argument is exactly the one used in DCP. This means that, assuming the activation function is an atom, $f{(x,\theta)}$ is DCP.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convexity", "weight": 1.0} -->

As in an input convex neural network, our architecture (and the nonnegativity constraint on $W^{l}$), was chosen specifically so that it implements a PCF for any valid choice of the weights.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Loss and regularizer", "weight": 1.0} -->

The loss and regularizer used in the fitting process are arbitrary. Some conventional choices of loss include quadratic, $\ell_{1}$, or Huber. Conventional choices of regularizer include quadratic, $\ell_{1}$, or a combination (known as elastic net regularization). See, e.g., or \[, Chap. 6.3\].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation", "weight": 1.0} -->

Our open-source implementation `lpcf` is available at

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation", "weight": 1.0} -->

In `lpcf` the user can specify the architecture, activation function, and type of regularization. The generic `.fit(data)` method fits the PCF to data, using cross-validation to choose the regularization hyper-parameter, and reports the performance of the fit obtained, for separate test data. In `lpcf`, the R2-score is the standard validation metric used for cross-validation and testing. Utilities are provided for the user to evaluate the resulting PCF, score it on another data set, and to export the function to CVXPY, where it can be freely used anywhere a convex function can be.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Implementation", "weight": 1.0} -->

A simple script illustrating this functionality is shown in figure. In lines 5--6 we instantiate a `pcf` object and fit its weights to data. In line 11 we export to the DCP expression `f` via the `tocvxpy` method, which takes a CVXPY variable and a CVXPY parameter as arguments, which are defined in the two lines above. We illustrate the use of `f` in constructing a CVXPY problem in line 15. In this example we simply add the fitted PCF to the objective, but we note that it can be used anywhere in CVXPY that a convex function appear, e.g., in constraints.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation", "weight": 1.0} -->

1from lpcf.pcf import PCF
4# create default PCF object and fit to data Y, X, Theta
6pcf.fit(Y, X, Theta)
8# export to cvxpy expression
11f = pcf.tocvxpy(x, theta)
13# solve cvxpy problem involving f
14# g is another function, constraints a list of (in)equalities
15problem = cp.Problem(cp.Minimize(f + g), constraints)
Figure 2: Using LPCF with CVXPY. The initialization code for dimensions n, p, data Y, X, Theta, and CVXPY objects g and constraints is omitted for clarity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation", "weight": 1.0} -->

To fit the weights $w$ of the network $\psi$ we use `jax-sysid`, a Python package based on the auto-differentiation framework JAX, for system identification, neural network training, and nonlinear regression/classification. The package supports several types of regularization, simple bounds on $w$, parallel training from different initial values of $w$, and quasi-Newton methods for faster terminal convergence and better model quality than gradient descent.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Default choices", "weight": 1.0} -->

We make a number of default choices, all of which can be modified by the user. We take $L = 3$ layers in the input-convex network, with layer dimensions $n_{1} = \cdots = n_{L - 1} = {2{\lfloor{{({n + d})}/2}\rfloor}}$, and ReLU activation function. We take $\psi$ to be a fully connected neural network with feedforward terms from $\theta$ into each layer, very similar to the architecture of the input-convex network. The output activation $\phi_{W}$ only affects $W^{2},\ldots,W^{L}$. We use the ReLU function to make them elementwise nonnegative. The architecture is visualized in figure.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Default choices", "weight": 1.0} -->

By default there are $M = 3$ layers, of which the two inner ones are $\lfloor{{({p + m})}/2}\rfloor$ wide, with ReLU activation. By default, we use a quadratic loss (mean squared error) without regularization, i.e., $\lambda = 0$, and the cross-validation procedure is turned off. Otherwise, the default number of folds for cross-validation is 5. The default optimizer runs 200 iterations of Adam to obtain a good set of network weights, followed by 2000 iterations of L-BFGS-B (a variant of L-BFGS for bound-constrained optimization, to respect the nonnegativity constraints on $W^{l}$) to refine the model weights. We run the entire fitting method on multiple random initial sets of model weights, and take the best one as our final choice. We parallelize training with multi-core processing, with a default of 4 cores. By default, we set the number of initializations to 10 or the number of cores, whichever is greater. All of these settings can be customized by the user.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Extensions", "weight": 1.0} -->

We describe a few extensions of the basic model and methods.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Adding a quadratic term", "weight": 1.0} -->

We can add a (convex) quadratic function to our more general architecture,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Adding a quadratic term", "weight": 1.0} -->

This automatically guarantees positive semidefiniteness of $Q$, without any additional constraints on the parameter network $\psi$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Adding a quadratic term", "weight": 1.0} -->

A further variation is a low rank plus diagonal quadratic $Q = {{F^{T}F} + {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(d_{1}^{2},\ldots,d_{n}^{2})}}}$, where $F \in \text{R}^{m \times n}$ is a wide matrix with $m \ll n$ and $d \in \text{R}^{n}$ is a vector of diagonal entries before they are squared to make $Q$ positive semidefinite. Such a form can be used to capture the dominant directions of curvature when $n$ is large.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Monotonicity", "weight": 1.0} -->

In certain cases we may wish to impose that the PCF $f$ is monotonically nondecreasing or nonincreasing with respect to some or all the components of $x$ for any $\theta \in \Theta$, e.g., when modeling a concave and increasing utility function (that we wish to maximize).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Monotonicity", "weight": 1.0} -->

Monotonicity of $f$ can be imposed as follows. Assume that the activation function $\phi$ is nondecreasing (e.g., ReLU or softplus). Consider the architecture of the network $\psi$ described in figure. We achieve monotonicity by obtaining $V^{j}$, $j = {1,\ldots,L}$ similary to how we obtain $W^{j}$, as the output of the nonnegative activation $\phi_{W}$, $j = {2,\ldots,L}$ (enforcing convexity in that case).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Monotonicity", "weight": 1.0} -->

By cascading instead $V^{j}$ with a nonpositive activation function $\phi_{-}$, such as $\phi_{-} = {- \phi_{+}}$, $j = {1,\ldots,L}$, by repeating the above argument it is easy to see that the resulting PCF $f$ is convex and decreasing with respect to each component of $x$ for any $\theta \in \Theta$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Specifying a subgradient", "weight": 1.0} -->

We may wish to specify (or encourage) a PCF to be minimized at a particular point $g{(\theta)}$, where $g:{\Theta\rightarrow\text{R}^{n}}$ is given. When $f$ is differentiable this is equivalent to ${{\nabla_{x}f}{({g{(\theta)}},\theta)}} = 0$, or, more generally, that $0 \in {\partial_{x}{f{({g{(\theta)}},\theta)}}}$ (the subdifferential of $f$ with respect to $x$). This can be encouraged in the training process by adding a regularization term such as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Specifying a subgradient", "weight": 1.0} -->

to the loss, where $\rho_{\min}$ is a hyper-parameter that scales the regularization. This (sub)gradient can be computed by automatic differentiation of the PCF $f$ with respect to its first argument.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Specifying a subgradient", "weight": 1.0} -->

As a further generalization, we can require (or encourage) ${f{(x,\theta)}} - {q{(\theta)}^{T}x}$ to be minimized at $x = {g{(\theta)}}$. This is equivalent to ${{\nabla_{x}f}{({g{(\theta)}},\theta)}} = {q{(\theta)}}$, and a similar regularization term can be added to the training objective.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Fitting a parametrized convex set", "weight": 1.0} -->

The same framework can be used to fit a parametrized convex set $C:{\Theta\rightarrow 2^{\text{R}^{n}}}$, described as

<!-- chunk {"id": "body-0052", "role": "body", "section": "Fitting a parametrized convex set", "weight": 1.0} -->

We can judge the loss on test data using either the same logistic loss function or the actual error rate,

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments", "weight": 1.0} -->

We start with two illustrative examples on simple functions, and then give two real applications, battery aging and control. We conduct the experiments on an Apple M4 Max machine.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Piecewise affine function on R", "weight": 1.0} -->

We generate data from a piecewise affine (PWA) function of the form

<!-- chunk {"id": "body-0055", "role": "body", "section": "Piecewise affine function on R", "weight": 1.0} -->

where $x \in \text{R}$ and $\theta = {(s_{+},s_{-},m,v)} \in \text{R}^{4}$. Note that $f^{\text{true}}$ is convex (i.e., a PCF) when $s_{+} \geq {- s_{-}}$, but we also carry out experiments when this is not the case. We use a quadratic loss function.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We sample 2000 values of $\theta$ from a uniform distribution on ${\lbrack{- 1},1\rbrack}^{4}$. For each value of $\theta$, we take 50 equally spaced points $x$ on $\lbrack{- 1},1\rbrack$, which gives $N = {2000 \times 50} = 10^{5}$ data points. We divide these data into two sets: Those for which $f^{\text{true}}$ is convex, and those for which it is not. For those that are nonconvex, we find the best affine fit, which is the (non-parametric) closest convex approximation of the function.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We fit this data using the default values for the network architecture and learning parameters.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results", "weight": 1.0} -->

Table contains the root mean squared error (RMSE) values of the learned PCF $f$, for $10^{5}$ random test data points with the true function values on a scale from $- 3$ to $3$. The first three values are with respect to the true data-generating function $f^{\text{true}}$, for all test data and computed for the convex and nonconvex data separately. The last value is the RMSE for nonconvex data, computed with the best affine fit as the ground truth.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results", "weight": 1.0} -->

Nonconvex (relative to best affine fit)

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results", "weight": 1.0} -->

We observe that the overall RMSE is very small. When only considering the convex examples, the RMSE is more than an order of magnitude smaller. As expected, the RMSE is considerably larger when only taking the nonconvex examples. When computed with respect to the best affine fit $f^{\text{linear}}$, the RMSE for the nonconvex examples is also in the order of the RMSE for the convex data.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Quadratic function on $\\text{R}^{3}$", "weight": 1.0} -->

We generate data from a parametrized quadratic function

<!-- chunk {"id": "body-0062", "role": "body", "section": "Quadratic function on $\\text{R}^{3}$", "weight": 1.0} -->

where the variable is $x \in \text{R}^{n}$ and the parameter is $\theta \in \text{S}_{+}^{n}$ (the set of $n \times n$ positive semidefinite symmetric matrices). The true function $f^{\text{true}}$ is convex, i.e., a PCF.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We take $n = 3$ and generate $1000$ values of $\theta$ where each entry is taken from $\lbrack{- 1},1\rbrack$. For each value of $\theta$, we sample $100$ values of $x$ from a uniform distribution on the unit ball, which gives $N = 10^{5}$ data points.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We fit the PCF with the softplus activation function and otherwise default settings for the network architecture and learning algorithm.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Results", "weight": 1.0} -->

For $10^{5}$ random test data points, where the value of the true data generating function $f^{\text{true}}$ moves between $0$ and $2$, we attain a low RMSE value of about $0.02$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Battery aging", "weight": 1.0} -->

When repeatedly charging and discharging the battery of, e.g., a hybrid electric vehicle or an industrial energy storage system, the battery capacity degrades over time, a process called battery aging \[, SOS^+^11, \]. We denote by $y$ the aging rate and generate data from the battery aging model as introduced and used for optimal battery management,

<!-- chunk {"id": "body-0067", "role": "body", "section": "Battery aging", "weight": 1.0} -->

where $x = {(q,b)} \in \text{R}_{+}^{2}$ is the variable, consisting of the battery's charge $q$ and the absolute charge rate $b$. The parameter is $\theta = {(A,Q,T)} \in \text{R}_{+}^{3}$ and contains the accumulated charge throughput $A$, the battery capacity $Q$, and temperature $T$. The remaining symbols are constants. We use the values, the physical constants

<!-- chunk {"id": "body-0068", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We generate $1000$ values of $\theta$, with accumulated charge throughput $A \in {\lbrack 0,50\rbrack}$ and temperature $T \in {\lbrack 10,50\rbrack}$. We keep the battery capacity fixed at $Q = 1$, since it is the slowest changing parameter (especially for a new battery where $A$ moves fast) and one can re-fit the PCF as $Q$ changes over time. For each value of $\theta$, we sample $100$ values of $x$ with state of charge $q \in {\lbrack 0.2,0.8\rbrack}$ and charge rate $b \in {\lbrack 0,30\rbrack}$, which gives $N = 10^{5}$ data points.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We fit the PCF with the softplus activation function. The input-convex network is 5 wide, the network $\psi$ has a single hidden layer of width 10, and we train with 1000 and 4000 epochs with Adam and L-BFGS-B, respectively.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We compare our fit to the convex approximation used for short term battery management,

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

This is a PCF itself, and can be derived as the first-order Taylor expansion of $f^{\text{true}}$ around the point ${(q,b)} = {({Q/2},0)}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Results", "weight": 1.0} -->

For $10^{5}$ random test points with $f^{\text{true}}$ on a scale from $0$ to $0.06$, the RMSE is $0.001$. This is about 7 times better than using the short term approximation $f^{\text{short}}$, which gives an RMSE of $0.007$. Figure shows the true data-generating function $f^{\text{true}}$ and the learned PCF $f$, for three random values of $\theta$. We observe that the approximations are good in all cases.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

We consider a nonlinear dynamical system of the form

<!-- chunk {"id": "body-0074", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

where $z_{t} \in \text{R}^{n}$ is the state, $u_{t} \in \text{R}^{m}$ is the input, $\theta$ is a vector of parameters, $F:{{\text{R}^{n} \times \Theta}\rightarrow\text{R}^{n}}$ gives the dynamics, and $G:{{\text{R}^{n} \times \Theta}\rightarrow\text{R}^{n \times m}}$ gives the input-to-state matrix. Since $z_{t + 1}$ is an affine function of $u_{t}$, this is called input-affine form. We are given the inital state $z_{0}$, and seek inputs $u_{0},u_{1},\ldots$ that minimize the cost function

<!-- chunk {"id": "body-0075", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

where $H:{{\text{R}^{n} \times \text{R}^{m} \times \Theta}\rightarrow\text{R}_{+}}$ is a nonnegative stage cost, assumed convex with respect to $(z_{t},u_{t})$. This is a nonconvex optimal control problem, which is hard to solve globally. A local method can however be used to approximately solve this problem, typically out to some large terminal time $t = T$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

Approximate dynamic programming (ADP) is a heuristic for approximately solving the optimal control problem, choosing $u_{t}$ one step at a time by solving a convex problem. It has the form

<!-- chunk {"id": "body-0077", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

for $t = {0,1,\ldots}$, where we update $z_{t}$ using the dynamics. Here $\hat{V}:{{\text{R}^{n} \times \Theta}\rightarrow\text{R}}$ is a PCF, so the minimization over $u$ is a convex optimization problem.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

ADP is motivated by the Bellman or recursive form of the optimal input sequence $u_{t}$, given by with $\hat{V}$ replaced by the value or cost-to-go function

<!-- chunk {"id": "body-0079", "role": "body", "section": "Approximate dynamic programming", "weight": 1.0} -->

To find the convex approximate value function, we use a local method to approximately solve the problem (out to some large time period $t = T$) for multiple values of the initial state $z_{0}$. Each such optimization in fact gives us a set of (approximate) values of the value function, one obtained at each state on the trajectory, with value equal to the corresponding tail cost.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider the problem of swinging up a pendulum to the vertical position by controlling the applied torque. We start with a nonlinear model of the continuous time dynamics

<!-- chunk {"id": "body-0081", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

where $\delta$ is the angular position of the pendulum, $m \in {\lbrack 0.5,2\rbrack}$ is its mass, $l = 1$ its length, $b = 0.05$ is the damping coefficient, $g = 9.81$ is the gravitational acceleration, and $u$ is the applied torque, all in standard metric units. We obtain an input-affine discrete-time model as in by setting $z = {(\delta,\overset{˙}{\delta})}$ and using a first-order forward Euler integration (with sampling time $0.02$). The stage cost is

<!-- chunk {"id": "body-0082", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Our parameter is $\theta = m$, with $\Theta = {\lbrack 0.5,2\rbrack}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We generate $N = 1000$ data points by sampling uniformly $\delta_{k} \in {\lbrack{- {\pi/6}},{{7\pi}/6}\rbrack}$, ${\overset{˙}{\delta}}_{k} \in {\lbrack{- 1},1\rbrack}$, and $m_{k} \in {\lbrack 0.5,2\rbrack}$. For each combination, we (approximately) solve the optimal control problem out to $t = T = 150$, using the L-BFGS-B optimizer.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We fit the PCF with the softplus activation function, width 20 for the input-convex network, two hidden layers of width 10 for the network $\psi$, and default architecture otherwise. We use the elastic net regularization term ${r{(w)}} = {{10^{- 8}{\| w\|}_{2}^{2}} + {0.1{\| w\|}_{1}}}$ in and two of the extensions described in §: We add a quadratic term (see §3.1) and specify a subgradient (see §3.3). In particular, we know that $V{(z,\theta)}$ has a minimum at the equilibrium $z^{eq} = {(\pi,0)}$. We promote that the same holds for $f$, by using ${g{(\theta)}} = z^{eq}$ in the regularization term.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We train the PCF from 16 different initial values, running $1000$ Adam iterations followed by up to $5000$ function evaluations in L-BFGS-B.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have shown how to fit a PCF to data, in a simple yet customizable way, with our open-source Python tool LPCF. Our method allows (parametrized) convex optimization to be (in part) data driven: while the modeling stage may heavily rely on learning functions from data, the first-principles structure of convex optimization is retained when solving a given problem instance. Our experiments exhibit good modeling accuracy (also compared to alternative convex function approximations), and the use of learned PCFs in convex optimization problems.
