<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fitting a Kalman Smoother to Data

Topics include Kalman filtering, Datasets.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers the problem of fitting the parameters of a Kalman smoother to data. We formulate the Kalman smoothing problem with missing measurements as a constrained least squares problem and provide an efficient method to solve it based on sparse linear algebra. We then introduce the Kalman smoother tuning problem, which seeks to find parameters that achieve low prediction error on held out measurements. We derive a Kalman smoother auto-tuning algorithm, which is based on the proximal gradient method, that finds good, if not the best, parameters for a given dataset. Central to our method is the computation of the gradient of the prediction error with respect to the parameters of the Kalman smoother; we describe how to compute this at little to no additional cost. We demonstrate the method on population migration within the United States as well as data collected from an IMU+GPS system while driving. The paper is accompanied by an open-source implementation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kalman smoothers are widely used to estimate the state of a linear dynamical system from noisy measurements. In the traditional formulation, the dynamics and output matrices are considered fixed attributes of the system; the covariance matrices of the process and sensor noise are tuned by the designer, within some limits, to obtain good performance in simulation or on the actual system. For example, it is common to use noise levels in the Kalman smoother well in excess of the actual noise, to obtain practical robustness \[3, §8\].

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we take a machine learning approach to the problem of tuning a Kalman smoother. We start with the observation that (by our definition) only the output is observed. This implies that the only way we can verify that a Kalman smoother is working well is to compare the outputs we predict with those that actually occur, on new or unseen test data, i.e., data that was not used by the Kalman smoother. In machine learning terms, we would consider this output prediction error to be our error, with the goal of minimizing it. We consider the noise covariance matrices, as well as the system matrices, as *parameters* that can be varied to obtain different estimators, in this case, different Kalman smoothers. These are varied, within limits, to obtain good test performance; this final Kalman smoother can then be checked on entirely new data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To do this we formulate the Kalman smoothing problem, with missing observations, as a simple least squares problem, with a coefficient matrix that depends on the parameters, i.e., the system and noise covariance matrices. We show how to efficiently compute the derivative of the test error with respect to the parameters, and use a simple proximal gradient method to update them to improve the test error. This method yields a Kalman smoother *auto-tuning* method. It uses one or more observed output sequences, and the usual prior knowledge in determining the starting system matrices as well as a description of the set over which we are allowed to vary them.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The same formulation works for tuning robust Kalman smoothers, where the process and sensor noises are assumed to have a non-Gaussian distribution, typically with fatter tails. In this case the least squares formulation of the Kalman smoother becomes a convex optimization problem, and the effect of the parameters is even less obvious, and therefore harder to tune manually. Our auto-tuning method extends immediately to such problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We describe a Kalman smoother auto-tuning method that requires only a dataset of measurements, which may have missing entries.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We describe an efficient method for computing the gradient of the prediction error with respect to the Kalman smoother parameters, that incurs little to no additional computational cost on top of already smoothing.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide an open-source implementation of the aforementioned ideas and illustrate the method via numerical examples that use real data.

<!-- chunk {"id": "body-0010", "role": "body", "section": "System model", "weight": 1.0} -->

We consider a linear system with dynamics

<!-- chunk {"id": "body-0011", "role": "body", "section": "System model", "weight": 1.0} -->

We make the standard statistical assumptions that $w_{1},\ldots,w_{T - 1}$ are IID $\mathcal{N}{(0,W)}$ and $v_{1},\ldots,v_{T}$ are IID $\mathcal{N}{(0,V)}$, where the symmetric positive definite matrices $W$ and $V$ are the process and sensor noise covariance matrices, respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Missing measurements", "weight": 1.0} -->

We assume throughout that only the sequence $y_{t}$ is observed. Indeed, we will assume that not all of the measurements are available to us. To model this, we modify the output equation so that $y_{t} \in {({\text{R} \cup {\{?\}}})}^{p}$, where ? denotes a missing value. We have

<!-- chunk {"id": "body-0013", "role": "body", "section": "Missing measurements", "weight": 1.0} -->

where $\mathcal{K} \subseteq {{\{ 1,\ldots,T\}} \times {\{ 1,\ldots,p\}}}$ is the set of (scalar) outputs that are available. For ${(t,i)} \notin \mathcal{K}$, we take ${(y_{t})}_{i} = ?$. We refer to entries of $y_{t}$ that are real as *known measurements* and the entries of $y_{t}$ that have the value ? as *missing measurements*.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Smoothing", "weight": 1.0} -->

The goal in smoothing is to reconstruct or approximate the missing measurements given the known measurements. Since the outputs and states are jointly Gaussian, the maximum likelihood and conditional mean estimates of the missing output values are the same, and can be found as the solution of the constrained least squares problem

<!-- chunk {"id": "body-0015", "role": "body", "section": "Smoothing", "weight": 1.0} -->

Also, the problem has a simple and widely used recursive solution for ${\hat{x}}_{t}$ when $\mathcal{K} = {{(1,\ldots,m)} \times {(1,\ldots,T)}}$, and also when $T\rightarrow\infty$. This recursive solution is often referred to as the Kalman filter.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Solving the Kalman smoothing problem", "weight": 1.0} -->

There are many ways to solve the Kalman smoothing problem. One method is to eliminate the equality constraint \[§4.2.4\] and solve the resulting unconstrained least squares problem, which has a banded coefficient matrix. This method has time and space complexity of order $T{({n + p})}^{2}$. We give some details on another method that has roughly the same complexity, but is simpler since it does not require eliminating the equality constraints.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Solving the Kalman smoothing problem", "weight": 1.0} -->

The matrices $D$ and $B$ are evidently very sparse, since each have a density of approximately $\frac{1}{N}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Solving the Kalman smoothing problem", "weight": 1.0} -->

The optimality conditions for can be expressed as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Solving the Kalman smoothing problem", "weight": 1.0} -->

where $\eta \in \text{R}^{|\mathcal{K}|}$ is the dual variable for the equality constraint and $v = {Dz}$. The KKT matrix, denoted by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Solving the Kalman smoothing problem", "weight": 1.0} -->

is also very sparse, since $B$ and $D$ are sparse.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Solving the Kalman smoothing problem", "weight": 1.0} -->

We assume for the remainder of the paper that $M$ is full rank (if it is not, we can add a small amount of regularization to make it invertible). Therefore we can solve the KKT system using any method for solving a sparse system of linear equations, e.g., a sparse LU factorization. Since the sparsity pattern is banded (when re-ordered the right way), the complexity of the sparse LU factorization will be linear in $T$. We have also observed this to be true in practice (see figure 1).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Judging a Kalman smoother", "weight": 1.0} -->

Suppose we have gathered a sequence of outputs denoted ${y_{1},\ldots,y_{T}} \in {({\text{R} \cup {\{?\}}})}^{p}$. We can judge how well a Kalman smoother is working on this sequence of observations by obscuring a fraction of the known outputs and comparing the outputs predicted by the Kalman smoother to those that actually occurred.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Judging a Kalman smoother", "weight": 1.0} -->

In order to judge the Kalman smoother, we calculate the squared difference between the predicted output trajectory and the actual trajectory in the entries that we masked, which is given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Judging a Kalman smoother", "weight": 1.0} -->

We refer to this quantity as the *prediction error*; the goal in the sequel will be to adjust the parameters to minimize this error. We note that the entries in the output should been suitably scaled or normalized such that is a good measure of prediction error for the given application.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

In this section we describe how to automatically tune the parameters in a Kalman smoother (that is, the dynamic matrices and covariance matrices) to minimize the prediction error on the held-out measurements. Once the parameters have been tuned, the Kalman smoother can be tested on another (unseen) output sequence.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

given initial hyper-parameter vector θ1 ∈ Θ, initial step size t1, number of iterations niter,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

1. Filter the output sequence. Let ŷ1, …, ŷT be the solution to.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

2. Compute the gradient of the prediction error. gk = ∇θL (θ).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

4. Compute the proximal operator. θtent = proxtk r (θk + 1/2).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

Increase step size and accept update. tk + 1 = (1.5) tk; θk + 1 = θtent.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Kalman smoother auto-tuning", "weight": 1.0} -->

6. else Decrease step size and reject update. tk + 1 = (0.5) tk; θk + 1 = θk.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Kalman smoother parameters", "weight": 1.0} -->

A Kalman smoother has four parameters, which we denote by

<!-- chunk {"id": "body-0033", "role": "body", "section": "Auto-tuning problem", "weight": 1.0} -->

The prediction error $L$ in is a function of the parameters, and from here onwards we denote that function by $L{(\theta)}$. To tune the Kalman smoother, we propose solving the optimization problem

<!-- chunk {"id": "body-0034", "role": "body", "section": "Auto-tuning problem", "weight": 1.0} -->

with variable $\theta$ (the parameters of the Kalman smoother), where $r:{\Theta\rightarrow\text{R}}$ is a regularization function. Here $\Theta$ denotes the set of allowable parameters and can, for example, include constraints on what parameters we are allowed to change. (The function $r$ evaluates to $+ \infty$ for $\theta \notin \Theta$, thus constraining $\theta$ to be in $\Theta$.)

<!-- chunk {"id": "body-0035", "role": "body", "section": "Auto-tuning problem", "weight": 1.0} -->

The objective function $F:{\Theta\rightarrow\text{R}}$ is composed of two parts: the prediction error and the regularization function. The first term here encourages the Kalman filter to have the same outputs as those observed, and the second term encourages the parameters to be simpler or closer to an initial guess.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Regularization functions", "weight": 1.0} -->

There are many possibilities for the regularization function $r$; here we describe a few. Suppose we have some initial guess for $A$, denoted $A_{nom}$. We could then penalize deviations of $A$ from $A_{nom}$ by letting, e.g.,

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regularization functions", "weight": 1.0} -->

As another example, suppose we suspected that $C$ was low rank; then we could use

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regularization functions", "weight": 1.0} -->

where ${\| C\|}_{\ast}$ is the nuclear norm of $C$, i.e., the sum of the singular values of $C$. This regularizer encourages $C$ to be low rank. Of course, any combination of these regularization functions is possible.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Allowable sets", "weight": 1.0} -->

There are also many possibilities for $\Theta$, the allowable set of parameters. One option is to only allow certain entries of $A$ to vary by letting the set of allowable $A$ matrices be

<!-- chunk {"id": "body-0040", "role": "body", "section": "Allowable sets", "weight": 1.0} -->

for some set $\Omega$. If we wanted to keep $A$ fixed, we could let $\Theta = {\{ A_{nom}\}}$. Another sensible option is to let $A$ vary within a box by letting the set of allowable $A$ matrices be

<!-- chunk {"id": "body-0041", "role": "body", "section": "Allowable sets", "weight": 1.0} -->

for some nominal guess $A_{nom}$ and hyper-parameter $\rho > 0$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Solution method", "weight": 1.0} -->

The auto-tuning problem is in general nonconvex, even if $\Theta$ and $r$ are convex, so it is very difficult to solve exactly. Therefore, we must resort to a local or heuristic optimization method to (approximately) solve it. There are many methods that we could use to (approximately) solve the auto-tuning problem (see, e.g., ). In this paper we employ one of the simplest, the proximal gradient method, since $F$ is differentiable in $\theta$ (see below).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Solution method", "weight": 1.0} -->

The proximal gradient method is described by the iteration

<!-- chunk {"id": "body-0044", "role": "body", "section": "Solution method", "weight": 1.0} -->

where $k$ is the iteration number, $t^{k} > 0$ is a step size, and the proximal operator of $tr{( \cdot )}$ is defined as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Solution method", "weight": 1.0} -->

When $\Theta$ is a convex set and $r$ is convex, evaluating the proximal operator of $r$ requires solving a (small) convex optimization problem. Also, the proximal operator often has a (simple) closed-form expression. We note that $r$ need not be differentiable.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Solution method", "weight": 1.0} -->

We employ the proximal gradient method with the adaptive step size scheme and stopping condition described. The full algorithm for Kalman smoother auto-tuning is summarized in Algorithm 4.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

Evidently, the proximal gradient method requires computing the gradient of the prediction error with respect to the parameters, denoted ${\nabla_{\theta}L}{(\theta)}$. The sensitivity analysis of Kalman smoothing has previously been considered in the forward direction, i.e., how changes in the parameters affect the output \[3, §7\]. Justification for our derivation can be found in \[12, §3.5\].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

To do this, we first form the gradient of $L$ with respect to ${\hat{y}}_{1},\ldots,{\hat{y}}_{T}$, given by

<!-- chunk {"id": "body-0049", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

Next we form the gradient of $L$ with respect to the solution to, which is given by

<!-- chunk {"id": "body-0050", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

Next we solve the linear system

<!-- chunk {"id": "body-0051", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

which only requires a backsolve if we have already factorized $M$. Since the KKT system $M$ is invertible, the prediction error is indeed differentiable.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

The next step is to form the gradient of $L$ with respect to the coefficient matrix $D$, which is given by

<!-- chunk {"id": "body-0053", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

Since $\theta$ only affects $D$ at certain entries, we only need to compute $G$ at those entries. That is, we compute $G$ at the entries

<!-- chunk {"id": "body-0054", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

The final step is to form the gradients with respect to the parameters, which are given by

<!-- chunk {"id": "body-0055", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

The complexity of computing the gradient is roughly the same complexity as solving the original problem, since it requires the solution of another linear system. However, the time required to compute the gradient is often lower since we cache the factorization of $M$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we describe our implementation of Kalman smoother auto-tuning, as well as the results of some numerical experiments that illustrate the method. All experiments were performed on a single core of an unloaded Intel i7-8770K CPU.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Reference implementation", "weight": 1.0} -->

We have implemented the Kalman smoother auto-tuning method described in this paper as an open-source Python package, available at

<!-- chunk {"id": "body-0058", "role": "body", "section": "Reference implementation", "weight": 1.0} -->

Our CPU-based implementation has methods for performing Kalman smoothing with missing measurements and for tuning the matrices in the Kalman smoother (Algorithm 4). Our only dependencies are `scipy`, which we use for sparse linear algebra, and `numpy`, which we use for dense linear algebra.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Performance", "weight": 1.0} -->

We ran our Kalman smoothing function on random problems with $n = p = 10$. Fig. 1 shows the execution time, averaged over ten runs, of solving the smoothing problem (denoted as *forward* in the figure), as well as computing the derivative with respect to the the parameters (denoted as *backward* in the figure). As expected, the time required to compute the solution and its derivative is roughly linear in the length of the sequence $T$. Empirically, we found that the time required to compute the derivative is roughly half of the time required to compute the solution. We remark that our method is very efficient and effortlessly scales to extremely large problem sizes.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Human migration example", "weight": 1.0} -->

Suppose we have $n$ states, where the $i$th state has a population $x_{i}$. At some cadence, say yearly, a fraction of people in each state decide to move to another state. We take noisy measurements of the population in some of the states and wish to infer the population in every state, including those we have not even measured.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Dynamics", "weight": 1.0} -->

The vector $x_{t} \in \text{R}^{n}$ denotes the population in each state at year $t$. The dynamics are described by

<!-- chunk {"id": "body-0062", "role": "body", "section": "Dynamics", "weight": 1.0} -->

where $A \in \text{R}_{+}^{n \times n}$. Here $A_{ij}$ denotes the fraction of the population in state $j$ that move to state $i$ each year.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Outputs", "weight": 1.0} -->

Each year, we take noisy measurements of the populations in some of the states. The outputs are described by

<!-- chunk {"id": "body-0064", "role": "body", "section": "United States population data", "weight": 1.0} -->

We gathered yearly population data (in millions of people) for the $n = 48$ states in the continental U.S from the U.S. Census Bureau. The data includes all years from 1900 to 2018.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experiment details", "weight": 1.0} -->

Our goal is to learn the dynamics matrix, dynamics covariance, and output covariance via Kalman smoother auto-tuning. To this end, we use the regularization function ${r{(\theta)}} = 0$ and allowable set

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experiment details", "weight": 1.0} -->

For each year, we pick 30 out of the 48 states at random to be measured. In each year, of those measured, we pick 12 at random to be missing and 5 at random to be part of the test set. We ran the method for 50 iterations with $t_{0} = {1\text{×}10^{- 4}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results", "weight": 1.0} -->

The prediction error decreased from 0.0097 to 0.0058. The test error decreased from 0.0041 to 0.0030. The algorithm took 31 seconds to run. Besides the purely numerical results, there are interesting interpretations of the resulting parameters. For example, we can interpret the off-diagonal entries in the $A$ matrix as the fraction of the population in one state that migrates to another state over the course of one calendar year. The biggest such entries are displayed in Tab. 1.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Vehicle smoothing example", "weight": 1.0} -->

In vehicle smoothing, we have noisy measurements of the position, velocity, and acceleration of a vehicle over time, and wish to infer the true position, velocity, and acceleration at each time step.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Dynamics", "weight": 1.0} -->

(This system is often referred to as a double integrator, since the derivative of $p_{t}$ is $v_{t}$ and the derivative of $v_{t}$ is $a_{t}$.)

<!-- chunk {"id": "body-0070", "role": "body", "section": "Data", "weight": 1.0} -->

We used the Sensor Play data recorder iOS application to record the acceleration, attitude, latitude, longitude, heading, speed, and altitude of an iPhone mounted on a passenger vehicle. We converted the latitude and longitude into local North-East-Up coordinates, used the heading to convert the speed into a velocity in local coordinates, and used the attitude to orient the acceleration to local coordinates. We recorded data for a total of 330 seconds with a sampling frequency of $100\ {Hz}$, resulting in $T = 33000$ measurements.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experiment details", "weight": 1.0} -->

Our goal is to learn the state and observation covariance matrices, via Kalman smoother auto-tuning. To this end, we penalize the off-diagonal entries of

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experiment details", "weight": 1.0} -->

where $\alpha$ is a hyper-parameter (we use $\alpha = {1\text{×}10^{- 4}}$) and

<!-- chunk {"id": "body-0073", "role": "body", "section": "Experiment details", "weight": 1.0} -->

We initialize the covariances as $W_{0}^{- {1/2}} = I$, $V_{0}^{- {1/2}} = {{(0.01)}I}$, and initialize $A_{0}$ and $C_{0}$ as given in Sec. 5.2 and Sec. 5.2 respectively. We consider all measurement indices where the GPS or velocity change as known (since GPS is only useful when it changes) and all acceleration indices as known. We use 20% of the known position measurements as the missing measurements and another 20% as the test measurements. We ran the method for 25 iterations with $t_{0} = {1\text{×}10^{- 2}}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Results", "weight": 1.0} -->

The prediction error decreased from 13.23 to 2.97. The test error decreased from 16.57 to 1.37. The algorithm took 135 seconds to run. The diagonals of the final state and output covariance matrices were

<!-- chunk {"id": "body-0075", "role": "body", "section": "Results", "weight": 1.0} -->

(Note that these matrices can be scaled and the smoothing result is the same, so only relative magnitude matters.) We observe that there is more state noise in north and east dimensions than up, which makes sense. Also, there is less state noise in velocity than in position. We also observe that there is much higher measurement noise for $z$ direction in GPS, which is true with GPS. In Fig. 2 we show the position estimates before and after tuning. Visually, we see significant improvement from tuning.
