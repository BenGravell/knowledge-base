## Introduction

### Convex optimization models

We consider the problem of learning to predict outputs $y \in \mathcal{Y}$ from inputs $x \in \mathcal{X}$, given a set of input-output pairs $(x^{i},y^{i})$, $i = {1,\ldots,N}$, with ${(x^{i},y^{i})} \in {\mathcal{X} \times \mathcal{Y}}$. We assume that $\mathcal{Y} \subseteq \text{R}^{m}$ is a convex set, but make no assumptions on $\mathcal{X}$. In this paper, we specifically consider models $\phi:{\mathcal{X}\rightarrow\mathcal{Y}}$ that predict the output $y$ by solving a convex optimization problem that depends on the input $x$. We call such models *convex optimization models*. While convex optimization has historically played a large role in *fitting* machine learning models, we emphasize that in this paper, we solve convex optimization problems to perform *inference*.

A convex optimization model has the form

where the objective function $E:{{\mathcal{X} \times \mathcal{Y}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ is convex in its second argument, and $\theta$ is a parameter belonging to a set of allowable parameters $\Theta$. The objective function $E$ is the model's *energy function*, and the quantity $E{(x,y;\theta)}$ is the energy of $y$ given $x$; the energy $E{(x,y;\theta)}$ can depend arbitrarily on $x$ and $\theta$, as long as it is convex in $y$. Infinite values of $E$ encode additional constraints on the prediction, since ${E{(x,y;\theta)}} = {+ \infty}$ implies ${\phi{(x;\theta)}} \neq y$. Evaluating a convex optimization model at $x$ corresponds to finding an output $y \in \mathcal{Y}$ of minimum energy. The function $\phi$ is in general set-valued, since the convex optimization problem in may have zero, one, or many solutions. Throughout this paper, we only consider the case where the argmin exists and is unique.

Convex optimization models are particularly well-suited for problems in which the outputs $y \in \mathcal{Y}$ are known to have structure. For example, if the outputs are probability mass functions, we can take $\mathcal{Y}$ to be the probability simplex; if they are sorted vectors, we can take $\mathcal{Y}$ to be the monotone cone; or if they are covariance matrices, we can take $\mathcal{Y}$ to be the set of symmetric positive semidefinite matrices. In all cases, convex optimization models provide an efficient way of searching over a structured set to produce predictions satisfying known priors.

Because convex optimization models can depend arbitrarily on $x$ and $\theta$, they are quite general. We will see that they include familiar models for regression and classification, such as linear and logistic regression, as specific instances. In the basic examples of linear and logistic regression, the corresponding convex optimization models have analytical solutions. But in most cases, convex optimization models must be evaluated by a numerical algorithm.

Learning a parametric model requires tuning the parameters to make good predictions on $\mathcal{D}$ and ultimately on held-out input-output pairs. In this paper, we present a gradient method for learning the parameters in a convex optimization model; this learning problem is in general non-convex, since the solution map of a convex optimization model is a complicated function. Our method uses the fact that the solution map is often differentiable, and its derivative can be computed efficiently, without differentiating through each step of the numerical solver.

### Outline

Our learning method is presented in §2 for the general case. In the following three sections, we describe general classes of convex optimization models with particular forms or interpretations. In §3, we interpret convex optimization models as solving a maximum a posteriori (MAP) inference task, and we give examples of these MAP models in regression, classification, and graphical models. In §4, we show how convex optimization models can be used to model utility-maximizing processes. In §5, we give examples of modeling agents using the framework of stochastic control. In §6, we present numerical experiments of learning convex optimization models for several prediction tasks.

### Related work

### Structured prediction

Structured prediction refers to supervised learning problems where the output has known structure. A common approach to structured prediction is energy-based models, which associate a scalar energy to each output, and select a value of the output that minimizes the energy, subject to constraints on the output. Most energy-based learning methods are learned by reducing the energy for input-output pairs in the training set and increasing it for other pairs. More recently, the authors of proposed a method for end-to-end learning of energy networks by unrolled optimization. Indeed, a convex optimization model can be viewed as a form of energy-based learning where the energy function is convex in the output. For example, input-convex neural networks (ICNNs) can be viewed as a convex optimization model where the energy function is an ICNN. We also note that several authors have proposed using structured prediction methods as the final layer of a deep neural network; of particular note is, in which the authors used a second-order cone program (SOCP) as their final layer.

### Inverse optimization

Inverse optimization refers to the problem of recovering the structure or parameters of an optimization problem, given solutions to it. In general, inverse optimization is very difficult. One special case where it is tractable is when the optimization problem is a linear program and the loss function is convex in the parameters, and another is when the optimization problem is convex and the parameters enter in a certain way. This paper can be viewed as a heuristic method for inverse optimization for general convex optimization problems.

### Differentiable optimization

There has been significant recent interest in differentiating the solution maps of optimization problems; these differentiable solution maps are sometimes called *optimization layers*. The paper showed how quadratic programs can be embedded as optimization layers in machine learning pipelines, by implicitly differentiating the KKT conditions (as in the early works ). Recently, showed how to efficiently differentiate through convex cone programs by applying the implicit function theorem to a residual map introduced in, and showed how to differentiate through convex optimization problems by an automatable reduction to convex cone programs; our method for learning convex optimization models builds on this recent work. Optimization layers have been used in many applications, including control, game-playing, computer graphics, combinatorial tasks, automatic repair of optimization problems, and data fitting more generally. Differentiable optimization for nonconvex problems is often performed numerically by differentiating each individual step of a numerical solver, although sometimes it is done implicitly; see, e.g.,.

### Bilevel optimization

The task of minimizing the training error of a convex optimization model can be interpreted as a *bilevel* optimization problem, i.e., an optimization problem in which some of the variables are constrained to be optimal for another optimization problem. In our case, the optimization problem is to minimize the model's training error, subject to the constraint that the predicted output is the solution to a convex optimization problem.

## Learning convex optimization models

In this section we describe a general method for learning the parameter $\theta$ in a convex optimization model, given a data set consisting of input-output pairs ${{(x^{1},y^{1})},\ldots,{(x^{N},y^{N})}} \in {\mathcal{X} \times \mathcal{Y}}$. We let ${\hat{y}}^{i} = {\phi{(x^{i};\theta)}}$ denote the prediction of $y^{i}$ based on $x^{i}$, for $i = {1,\ldots,N}$. These predictions depend on $\theta$, but we suppress this dependency to lighten the notation.

### Learning problem

The fidelity of a convex optimization model's predictions is measured by a loss function $L:{{\mathcal{Y} \times \mathcal{Y}}\rightarrow\text{R}}$. The value $L{({\hat{y}}^{i},y^{i})}$ is the loss for the $i$th data point; the lower the loss, the better the prediction. Through ${\hat{y}}^{i}$, this depends on the parameter $\theta$.

Our ultimate goal is to construct a model that generalizes, i.e., makes accurate predictions for input-output pairs not present in $\mathcal{D}$. To this end, we first partition the data pair indices into two sets, a training set $\mathcal{T} \subset {\{ 1,\ldots,N\}}$ and a validation set $\mathcal{V} = {{\{ 1,\ldots,N\}} \smallsetminus \mathcal{T}}$. We define the average training loss as

We fit the model by choosing $\theta$ to minimize the average training loss plus a regularizer $R:{\Theta\rightarrow{\text{R} \cup {\{\infty\}}}}$, i.e., solving the optimization problem

with variable $\theta$. The regularizer measures how compatible $\theta$ is with prior knowledge, and we assume that ${R{(\theta)}} = \infty$ for $\theta \notin \Theta$, i.e., the regularizer encodes the constraint $\theta \in \Theta$. We describe below a gradient-based method to (approximately) solve the problem.

We can check how well a convex optimization model generalizes by computing its average loss on the validation set,

In some cases, the model or learning procedure depends on parameters other than $\theta$, called hyper-parameters. It is common to learn multiple models over a grid of hyper-parameter values and use the model with the lowest validation loss.

### A gradient-based learning method

In general, $\mathcal{L}$ is not convex, so we must resort to an approximate or heuristic method for learning the parameters. One could consider zeroth-order methods, e.g., evolutionary strategies, Bayesian optimization, or random search. Instead, we use a first-order method, taking advantage of the fact that the convex optimization model is often differentiable in the parameter $\theta$.

### Differentiation

The output of a non-pathological convex optimization model is an implicit function of the input $x$ and the parameter $\theta$. When some regularity conditions are satisfied, this implicit function is differentiable, and its derivative with respect to $\theta$ can often be computed in less time than is needed to compute the solution. One generic way of differentiating through convex optimization problems involves a reduction to an equivalent convex cone program, and implicit differentiation of a residual map of the cone program; this is the method we use in this paper. For readers interested in more details on the derivative computation, we suggest. In our experience, it is unnecessary to check regularity conditions, since we and others have empirically observed that the derivative computation in usually provides useful first-order information in the rare cases when the solution map is not differentiable at the current iterate. In this sense, convex optimization models are similar to other kinds of machine learning models, such as neural networks, which can be trained using gradient descent despite only being differentiable almost everywhere.

### Learning method

We propose a proximal stochastic gradient method. The method is iterative, starting with an initial parameter $\theta^{1}$. The first step in iteration $k$ is to choose a batch of (training) data denoted $\mathcal{B}^{k} \subset \mathcal{T}$. There are many ways to do this, e.g., by cycling through the training set or by selecting indices in $\mathcal{T}$ at random. The next step is to compute the gradient of the loss averaged over the batch,

This step requires applying the chain rule for differentiation to $|\mathcal{B}^{k}|$ compositions of the convex optimization model (discussed above) and the loss function. The final step is to update $\theta$ by first taking a step in the negative gradient direction, and then applying the proximal operator of $R$,

where $t^{k} > 0$ is a step size. We assume that the proximal operator of $R$ is single-valued and easy to evaluate. When $R{(\theta)}$ is the $\{ 0,\infty\}$ indicator function of $\Theta$, this method reduces to the standard projected stochastic gradient method,

where $\Pi_{\Theta}$ is the Euclidean projection operator onto $\Theta$. There are many ways to select the step sizes $t^{k}$; see, e.g.,.

## MAP models

Let the inputs $x \in \mathcal{X}$ and outputs $y \in \mathcal{Y}$ be random vectors, and suppose that the conditional distribution of $y$ given $x$ has a log-concave density $p$, parametrized by $\theta$. The energy function

yields a *maximum a posteriori* (MAP) model: $\hat{y} = {\phi{(x;\theta)}}$ is the MAP estimate of the random vector $y$, given $x$ \[24, §1.2.5\]. Conversely, any convex optimization model can be interpreted as a MAP model, by identifying the density of $y$ given $x$ with an exponential transformation of the negative energy

is the normalizing constant or partition function. Crucially, evaluating a MAP model does not require computing $Z{(x;\theta)}$ since it does not depend on $y$; i.e., MAP models can be used even when the partition function is computationally intractable, as is often the case \[38, §18\].

### Regression

Several basic regression models can be described as MAP models, with

where $x \in \mathcal{X} = \text{R}^{n}$, $y \in \mathcal{Y} = \text{R}^{m}$, $\theta \in \text{R}^{n \times m}$ is the parameter and $f:{\text{R}^{m}\rightarrow\text{R}}$ is a convex penalty function. (The expression $\theta^{T}x$ can be replaced with a more complex function, such as a neural network, since convex optimization models can depend arbitrarily on $x$ and $\theta$; we focus on the linear case for simplicity.) If the penalty $f$ is minimized at 0, then the MAP model is the linear predictor ${\phi{(x;\theta)}} = {\theta^{T}x}$. In this case, fitting the MAP model with a mean-squared loss ${L{(\hat{y},y)}} = {\|{\hat{y} - y}\|}_{2}^{2}$ is equivalent to fitting a linear regression model; fitting it with an $\ell_{1}$ loss is equivalent to $\ell_{1}$ regression; and fitting it with the Huber loss \[26, §6.1\] yields robust Huber regression.

These very basic examples can be made more interesting by constraining the outputs $y$ to lie in a convex subset $C$ of $\mathcal{Y}$, using a density of the form

Because the output is constrained, different choices of the penalty function $f$ yield different MAP models. When the penalty function $f$ is the squared Euclidean norm, ${f{(u)}} = {\| u\|}_{2}^{2}$, the MAP estimate $\hat{y} = {\phi{(x;\theta)}}$ is the Euclidean projection of $\theta^{T}x$ onto $C$. Other penalty functions, like the $\ell_{1}$ norm ${f{(u)}} = {\| u\|}_{1}$ or the Huber function \[26, §6.1\] yield interesting non-trivial regression models. We present some examples of the constraint set $C$ below.

### Nonnegative regression

Taking $C = \text{R}_{+}^{m}$ (the set of nonnegative $m$-vectors) yields a MAP model for nonnegative regression, i.e., the MAP estimates in this model are guaranteed to be nonnegative.

### Monotonic output regression

When $C$ is the monotone cone, i.e., the set of ordered vectors

the MAP estimates in the regression model are guaranteed to be sorted in ascending order. When $f$ is the Euclidean norm, the MAP estimate is the projection of $\theta^{T}x$ onto the monotone cone, and evaluating it requires solving a convex quadratic program (QP); in this special case, once $\theta^{T}x$ has been computed (which takes $O{({mn})}$ time), evaluating the convex optimization model is equivalent to monotonic or isotonic regression, which takes $O{(m)}$ time, meaning it has the same complexity as the standard linear regression model.

We note the distinction between traditional isotonic regression and a convex optimization model with monotone constraint. In isotonic regression, we seek a single vector with nondecreasing components. In a convex optimization model with a monotone constraint, we seek a model that maps $x \in \mathcal{X}$ to a prediction $\hat{y}$ that always has nondecreasing components.

### Classification

In (probabilistic) classification tasks, the outputs are vectors in the probability simplex, i.e.,

The output $y$ can be interpreted as a probability distribution over $\{ 1,\ldots,m\}$ associated with an input $x \in \mathcal{X} = \text{R}^{n}$. The MAP estimate $\hat{y} = {\phi{(x;\theta)}}$ is therefore the most likely distribution associated with $x$, under a particular density $p{({y \mid {x;\theta}})}$. This includes as a special case the familiar setting in which each output is a label, e.g., a number in $\{ 1,\ldots,m\}$, since the label $k$ can be represented by a vector $y$ such that $y_{k} = 1$ and $y_{i} = 0$ for $i \neq k$.

As a simple first example, consider the MAP model with density

where $\theta \in \text{R}^{n \times m}$ and ${H{(y)}} = {- {\sum_{i = 1}^{m}{y_{i}{\log y_{i}}}}}$ is the entropy function. The resulting convex optimization model is just the softmax of $\theta^{T}x$, i.e., ${\phi{(x;\theta)}} = {{{\exp{({\theta^{T}x})}}/\mathbf{1}^{T}}{\exp{({\theta^{T}x})}}}$, where the exponentiation and the division are meant elementwise. (This fact is readily verified via the KKT conditions of the convex optimization model \[6, §2.4.4\]).

Since the outputs are probability distributions, a natural loss function is the KL-divergence from the true output $y$ to the prediction $\hat{y} = {\phi{(x;\theta)}}$, i.e.,

Discarding the constant terms $y_{i}{\log y_{i}}$, which do not affect learning, recovers the commonly used cross-entropy loss \[40, §2.6\]. Using this loss function with the softmax model recovers multinomial logistic regression \[40, §4.4\]. This model can be made more interesting by simple extensions.

### Constrained logistic regression

We can readily add constraints on the distribution $\hat{y}$. As a simple example, a box-constrained logistic regression model has the form

where $C$ is a convex subset of $\Delta^{m - 1}$. There are many interesting constraints we can impose on the distribution $y$. As a simple example, the constraint set

where ${\alpha,\beta} \in \text{R}^{m}$ are vectors and the the inequalities are meant elementwise can be used to require that $\hat{y}$ have heavy tails, by making the leading and trailing components of $\alpha$ large, or thin tails, by making the leading and trailing components of $\beta$ small. Another simple example is to specify the expected value of an arbitrary function on $\{ 1,\ldots,m\}$ under $\hat{y}$, which is a simple linear equality constraint on $\hat{y}$. More generally, any affine equality constraints and convex inequality constraints on $\hat{y}$ may be imposed; these include constraints on the quantiles of the random variable associated with $y$, lower bounds on its variance, and inequality constraints on conditional probability distributions.

### Piecewise-constant logistic regression

A piecewise-constant logistic regression model has the form

where the parameter is $\theta$ and $\lambda > 0$ is a (hyper-)parameter. To the standard energy we add a total variation term that encourages $y$ to have few "jumps", i.e., few indices $i$ such that $y_{i} \neq y_{i + 1}$, $i = {1,\ldots,{m - 1}}$ \[43, §7.4\]. The larger the hyper-parameter $\lambda$ is, the fewer jumps it will have (typically).

### Graphical models

A Markov random field (MRF) is an undirected graphical model that describes the joint distribution of a set of random variables, which are represented by the nodes in the graph. An MRF associates parametrized potential functions to cliques of nodes, and the joint distribution it describes is proportional to the product of these potential functions. MRFs are commonly used for structured prediction, but learning their parameters is in general difficult \[24, §8.3\]. When the potential functions are log-concave, however, we can fit the parameters using the methods described in this paper.

Suppose we are given an MRF describing the joint distribution of the random vectors $x$ and $y$. Let $z = {(x,y)} \in \text{R}^{n + m}$, and let $c_{1}$, $c_{2}$,..., $c_{p}$ denote the indices of the graph cliques; we write $z_{c_{k}}$ to denote the components of $z$ in clique $c_{k}$. For example, if $c_{k} = {}$, then $z_{c_{k}} = {(z_{1},z_{4},z_{5})}$. Suppose the MRF has a Boltzmann distribution, meaning

Here, $\exp{({- {E_{k}{(z_{c_{k}})}}})}$ are the potential functions, and $E_{k}$ is a local energy function, parametrized by $\theta$, for the clique $k$. As long as the functions $E_{1},\ldots,E_{p}$ are convex, the corresponding MAP model

is a convex optimization model. In this case, given a dataset of input-output pairs $(x,y)$, we can fit the parameter $\theta$ without evaluating or differentiating through the partition function.

### Quadratic MRFs

Consider an MRF in which the variables $x$ and $y$ lie in convex sets (such as slabs, or all of $\text{R}^{n}$ or $\text{R}^{m}$). Suppose the MRF has $\binom{n + m}{2} + n + m$ pairwise cliques of the form $\{ z_{i},z_{j}\}$ ($1 \leq i \leq j \leq {n + m}$), and a Boltzmann distribution with local energy functions

where $\theta \in \Theta = \text{S}_{+}^{n + m}$ is the parameter ($\text{S}_{+}^{n + m}$ is the set of positive semidefinite matrices). The MAP inference task for this MRF is a convex optimization model, of the form

MRFs with a similar clique structure have been proposed for various signal and image denoising tasks. We give a numerical example of fitting a quadratic MAP model of an MRF in §6.

We emphasize that the dependence on $x$ can be arbitrary; e.g., if the energy function were

where $f$ were a neural network, the MAP model would remain convex.

## Utility maximization models

We now consider the case where the output $y$ is interpreted as a decision, and the input $x$ is a context or feature vector that affects the decision. We assume that the decision $y$ is chosen to maximize some given parametrized utility function

where $U{(x,y;\theta)}$ is the utility of choosing a decision $y$ given the context $x$ and the parameters $\theta$, and is concave in $y$. Infinite values of $U$ are used to constrain the decision $y$. (In most cases the utility function $U$ is monotone increasing in $y$, but we do not need this property.) The energy function in a utility maximization model is simply the negative utility,

The resulting convex optimization model $\phi{(x;\theta)}$ gives a maximum utility decision in the context $x$. The same losses used for regression (see §3.1) and classification (see §3.2) can be used for utility maximization. The context $x$ might include, for example, a total budget on the decision $y$, prices that affect the decision, or availabilities that affect the decision.

### Resource allocation

A standard example of utility maximization is resource allocation. In the simplest case, this involves allocating a single, finite resource across $m$ agents or tasks. The decision $y \in \text{R}_{+}^{m}$ gives the allocation across those tasks, where $y_{i}$ is the resource allocated to task $i$; because the resource is finite, the allocation must satisfy ${\mathbf{1}^{T}y} \leq B$, where $B \in \text{R}_{+}$ is a nonnegative budget. The context $x$ contains the budget $B$, and possibly other important parameters such as limits on allocations to the tasks. When the input $x$ is just the budget, the utility has the form

where $U{(y;\theta)}$ is some parametrized concave utility function, describing the utility of an allocation. In this simple case, $\phi{(x;\theta)}$ gives the maximum utility allocation that satisfies the budget constraint.

The input $x$ is not limited to just the budget; it can also contain additional context that affects or constrain the decision. One important case is when the resource to be allocated is dollars, and $x$ contains the prices of the resource for each of the agents, denoted $p \in \text{R}_{+ +}^{m}$. When there are prices, an allocation of $y_{i}$ dollars provides $y_{i}/p_{i}$ units of some good to agent $i$. The utility in this case has form

where the division is meant elementwise, and $U{(z;\theta)}$ gives the utility of the agents receiving $z_{i}$ units of the resource, $i = {1,\ldots,m}$. The resulting convex optimization model $\phi{(x;\theta)}$ gives the maximum utility allocation that satisfies the budget constraints, given the current prices.

We can just as well model the allocation of multiple resources, each with its own budget, across agents or tasks; e.g., we might model the allocation of computational resources, such as CPU cores, memory, and disk space, to a pool of tasks. If there are $k$ resources and $m^{\prime}$ agents, then the output would be the $k$ allocation vectors for each resource, stacked together to form a vector $y \in \text{R}_{+}^{m}$, where $m = {km^{\prime}}$.

### Utility functions

A simple family of utility functions are the separable functions

where $U_{i}{(y_{i};\theta)}$ is the utility of allocating $y_{i}$ of the resource to the $i$th agent or task. In this case the entries of the decision $y$ are coupled by budget constraints. A simple example for separable utility is exponential utility ${U_{i}{(y_{i};\theta)}} = {- {{\exp{({\theta_{i}y_{i}})}}/\theta_{i}}}$.

However, $U$ need not be separable. A common example is when $y$ represents an allocation of a budget in a portfolio of stocks; the Markowitz utility or risk-adjusted return is

where $\mu \in \text{R}^{m}$ is the expected return of each investment, $\Sigma \in \text{S}_{+ +}^{m}$ is the covariance of the returns, and $\gamma > 0$ is the risk aversion parameter. We can take $\theta = {(\mu,\Sigma,\gamma)}$, in which case we are observing portfolios and attempting to infer the mean covariance, and risk aversion parameter that best model the observed portfolio allocations.

## Stochastic control agent models

In this section, we consider a setting in which $x \in \mathcal{X} = \text{R}^{n}$ is the context or state of a dynamical system, and $y \in \mathcal{Y} = \text{R}^{m}$ represents the action taken by the agent in that state. Our goal is to model the agent's actions as coming from a policy, i.e., a mapping from state to action. In this section, we describe generic ways to model an agent's policy with a convex optimization model. The convex optimization models we present are all instances of convex optimization policies commonly used for stochastic control. When learning these models, one can use the same losses proposed for regression (see §3.1).

### Stochastic control

To motivate the models presented in this section, we describe here a general stochastic control problem. Let $x_{t}$ and $y_{t}$ denote the state and action at time $t$. Suppose the state evolves according to the dynamics

where $w_{t} \in \mathcal{W}$ is a random variable, and the function $f:{{\text{R}^{n} \times \text{R}^{m} \times \mathcal{W}}\rightarrow\text{R}^{n}}$ gives the (stochastic) dynamics of the dynamical system. Suppose also that the agent selects actions according to

where $\phi:{\text{R}^{n}\rightarrow\text{R}^{m}}$ is the policy, and that the agent's goal is to minimize a discounted sum of stage costs $g:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ over time,

where $\gamma \in {(0,1\rbrack}$ is a discount factor, subject to the dynamics and the policy. It is well known (see, e.g., ) that an optimal policy is given by

where $V:{\text{R}^{n}\rightarrow\text{R}}$ is the cost-to-go function, which satisfies Bellman's equation

In general, given a dataset describing an agent's actions, we have no reason to believe that the agent chooses actions by solving a stochastic control problem. Nonetheless, choosing a model that corresponds to a policy for stochastic control can work well in practice. As we will see, our models involve learning the parameters in three functions that can be interpreted as dynamics, stage costs, and an approximate value function.

### Approximate dynamic programming (ADP)

One possible model of agent behavior is the ADP model \[22, §6\], which has the form

where $x_{+} \in \text{R}^{n}$ and $y \in \text{R}^{m}$ are the variables. The function $f:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow\text{R}^{n}}$, which must be affine in its second argument, can be interpreted as the dynamics; the function $g:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ is the stage cost (which is convex in its second argument); and the convex function $\hat{V}$ can be interpreted as an approximation of the cost-to-go or value function. All three of these functions are parametrized by the vector $\theta$. The value $\hat{y} = {\phi{(x;\theta)}}$ is the optimal value of the variable $y$, i.e., the ADP model chooses the action that minimizes the current stage cost plus an estimate of the cost-to-go of the next state.

One reasonable parametrized stage cost $g$ is the weighted sum of a number of convex functions ${h_{1},\ldots,h_{p}}:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$,

In this case we would have $\Theta = \text{R}_{+}^{p}$. For example, if the dynamical system were a car, the state was the physical state of the car, and the action was the steering wheel angle and the acceleration, there would be many reasonable costs: e.g., tracking, fuel use, and comfort. Such a stage cost could be used to trade off these costs, or to derive them from data.

Similarly, the cost-to-go function might be a weighted sum of functions ${{\hat{V}}_{1},\ldots,{\hat{V}}_{p}}:{\text{R}^{n}\rightarrow{\text{R} \cup {\{\infty\}}}}$,

yields a quadratic cost-to-go function.

### Model predictive control (MPC)

An MPC policy is an instance of the ADP policy \[22, §6.4.3\],

with variables $x_{0},\ldots,x_{T}$ and $y_{0},\ldots,y_{T - 1}$, where $T$ is the time horizon. Here $f_{t}:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow\text{R}^{n}}$ is the (affine) dynamics function at time $t$, and $g_{t}:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ is the stage cost function at time $t$, which is convex in $y_{t}$; both functions are parametrized by $\theta$. (The expression

can be interpreted as the approximate value function of an ADP policy.) The objective is the sum of the stage costs $g_{t}$ through time, and the constraints enforce the dynamics and the initial state. The MPC model chooses the action as the first action in a planned sequence of future actions $y_{0},\ldots,y_{T - 1}$, i.e., $\hat{y} = {\phi{(x;\theta)}}$ is the optimal value for the variable $y_{0}$.

## Numerical experiments

In this section we present four numerical experiments that mirror the examples from sections §3,§4, and §5. The code for all of these examples can be found online at

### Monotonic output regression

We consider the monotonic output regression model (see §3.1). We take $n = 20$ and $m = 10$. We generate a true parameter $\theta^{true} \in \text{R}^{n \times m}$ with entries sampled independently from a standard normal distribution, and sample 100 training data pairs and 50 validation data pairs according to

We compare the convex optimization model to linear regression, using the standard sum of squares loss and no regularizer. The results for both of these methods are displayed in figure 1. On the left, we show the validation loss versus training iteration. The final validation loss for linear regression is 3.375, for the convex optimization model is 0.562, and for the true model is 0.264. We also calculated the validation loss of a convex optimization model with the linear regression parameters; this resulted in a validation loss of 1.511. While better than 3.375, this shows that here our learning method is superior to learning the parameters using linear regression and then projecting the outputs onto the monotone cone. On the right, we show both model's predictions for a validation input.

Figure 1: Monotonic output regression: linear regression (LR), convex optimization model (COM), true model (true). Left: validation loss. Right: predictions for a held-out input.

### Signal denoising

Here, we fit the parameters in a quadratic MRF (see §3.3) for a signal denoising problem. We consider a denoising problem in which each input $x \in \text{R}^{n}$ is a noise-corrupted observation of an output $y \in \text{R}^{m}$, where $n = m$. The goal is to reconstruct the original signal $y$, given the noise-corrupted observation. We model the conditional density of $y$ given $x$ as

where $\theta = {({{M \in \text{R}^{n \times n}},{\lambda \in \text{R}_{+ +}}})}$ is the parameter and $D$ is the first-order difference matrix. The MAP estimate of $y$ given $x$ is ${\phi{(x;\theta)}} = {\operatorname{argmax}_{y}{{\log p}{({y \mid {x;\theta}})}}}$, and the corresponding convex optimization model has the energy function

The first term says that $x$ should be close to $y$, as measured by the squared quadratic $M$-norm, while the second term says that the entries of $y$ should vary smoothly. When $M = I$, this model is equivalent to least-squares denoising with Laplacian regularization. We note that this convex optimization model has the analytical solution

Figure 2: Signal denoising. Predictions for a held-out input; least squares (LS), convex optimization model (COM), and true output (true).

We use $n = 100$, $m = 100$, and $N = 500$ training pairs. Each output $y$ is generated by sampling a different scale factor $a$ from a uniform distribution over the interval $\lbrack 1,3\rbrack$, and then evaluating the cosine function at $100$ linearly spaced points in the interval $\lbrack 0,{2\pia}\rbrack$. The outputs are corrupted by Gaussian noise to produce the inputs. We generate a covariance matrix $\Sigma$ according to

and then generate the components of each input $x$

We generate $100$ validation points in the same way. As a baseline, we use least-squares denoising with Laplacian regularization, sweeping $\lambda$ to find the value which minimizes the error on the training set. The least-squares reconstruction achieves a validation loss of 0.090; after learning, the convex optimization model achieves a validation loss of 0.014. Figure 2 compares a prediction of the convex optimization model with least squares and the true output, for a held-out input-output pair.

### Resource allocation

We consider an instance of the resource allocation problem with prices, as described in §4, and use the separable exponential utility function. The input $x$ consists of the budget $B \in \text{R}_{+}$ and the prices $p \in \text{R}_{+}^{m}$, and the output $y \in \text{R}_{+}^{m}$ is the resource allocation. Our convex optimization model has the form

Here the feasible parameter set is $\Theta = \text{R}_{+}^{m}$. We take $m = 10$, and sample 100 training and 50 validation inputs and the true parameter according to

where $U{\lbrack a,b\rbrack}$ denotes the uniform distribution over the interval $\lbrack a,b\rbrack$. The outputs were generated according to

where $\odot$ denotes elementwise multiplication. In other words, we evaluate the true convex optimization model, multiply each output by a random number between $0.5$ and $1.5$, and re-scale the allocation so it sums to the budget $B$. We compare the convex optimization to logistic regression using the prices as features and the (normalized) allocation as the output. In figure 3 we show results for these two methods. On the left, we show the validation loss versus iteration for the convex optimization model, with horizontal lines for the validation loss of the logistic regression baseline and the true model. On the right, we show the learned and true utility function parameters, and observe that the learned parameters are quite close to the true parameters.

Figure 3: Resource allocation. Left: validation loss versus iteration for logistic regression and our convex optimization model. Right: learned and true parameters.

### Constrained MPC

Figure 4: Constrained MPC. Left: validation loss for a neural network (NN), convex optimization model (COM), and true model (true). Right: learned and true parameters.

We fit a convex optimization model for an instance of the MPC problem described in §5, with $n = 10$ states, $m = 4$ controls with $\mathcal{Y} = {\{{y \in \text{R}^{m}}\mid{{\| y\|}_{\infty} \leq 0.5}\}}$, and a horizon of $T = 5$. Our convex optimization model has the form

where the variables are the states ${x_{0},\ldots,x_{T}} \in \text{R}^{n}$ and the controls ${y_{0},\ldots,y_{T - 1}} \in \text{R}^{m}$, the square ${(x_{t})}^{2}$ is meant elementwise, and $\phi{(x;\theta)}$ is the optimal value of $y_{0}$. The parameter $\theta \in \text{R}_{+}^{n}$ parametrizes the stage cost, and the dynamics matrices $A$ and $B$ are known numerical constants.

We generate a true weight $\theta^{true} \in \text{R}_{+}^{n}$ with entries set to the absolute value of samples from a standard normal distribution. The dataset is generated by rolling out an MPC policy $\phi^{true}$ of the form, with parameter $\theta^{true}$. The policy is simulated from an initial state $x_{0} \sim {\mathcal{N}{(0,I)}}$. The outputs are noise-corrupted controls, generated according to

for $i = {1,\ldots,1000}$. We generate $1000$ validation points in the same way.

We use the mean-squared loss for the loss function $L$, and train for 20 iterations. As a baseline, we compare against a two-layer feedforward ReLU network with hidden layer dimension $n$, and with output clamped to have absolute value no greater than $0.5$. The results are displayed in figure 4. The ReLU network achieves a validation loss of 0.071. The trained convex optimization model achieves a validation loss of 0.066, which is close to the validation loss of the underlying model. Additionally, the convex optimization model nearly recovers the true weights.
