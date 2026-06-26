## Introduction

Kalman smoothers are widely used to estimate the state of a linear dynamical system from noisy measurements. In the traditional formulation, the dynamics and output matrices are considered fixed attributes of the system; the covariance matrices of the process and sensor noise are tuned by the designer, within some limits, to obtain good performance in simulation or on the actual system. For example, it is common to use noise levels in the Kalman smoother well in excess of the actual noise, to obtain practical robustness \[3, §8\].

In this paper we take a machine learning approach to the problem of tuning a Kalman smoother. We start with the observation that (by our definition) only the output is observed. This implies that the only way we can verify that a Kalman smoother is working well is to compare the outputs we predict with those that actually occur, on new or unseen test data, i.e., data that was not used by the Kalman smoother. In machine learning terms, we would consider this output prediction error to be our error, with the goal of minimizing it. We consider the noise covariance matrices, as well as the system matrices, as *parameters* that can be varied to obtain different estimators, in this case, different Kalman smoothers. These are varied, within limits, to obtain good test performance; this final Kalman smoother can then be checked on entirely new data.

To do this we formulate the Kalman smoothing problem, with missing observations, as a simple least squares problem, with a coefficient matrix that depends on the parameters, i.e., the system and noise covariance matrices. We show how to efficiently compute the derivative of the test error with respect to the parameters, and use a simple proximal gradient method to update them to improve the test error. This method yields a Kalman smoother *auto-tuning* method. It uses one or more observed output sequences, and the usual prior knowledge in determining the starting system matrices as well as a description of the set over which we are allowed to vary them.

The same formulation works for tuning robust Kalman smoothers, where the process and sensor noises are assumed to have a non-Gaussian distribution, typically with fatter tails. In this case the least squares formulation of the Kalman smoother becomes a convex optimization problem, and the effect of the parameters is even less obvious, and therefore harder to tune manually. Our auto-tuning method extends immediately to such problems.

In summary, the contributions of this paper are: We describe a Kalman smoother auto-tuning method that requires only a dataset of measurements, which may have missing entries.

We describe an efficient method for computing the gradient of the prediction error with respect to the Kalman smoother parameters, that incurs little to no additional computational cost on top of already smoothing.

We provide an open-source implementation of the aforementioned ideas and illustrate the method via numerical examples that use real data.

## Related work

The Kalman filter was independently invented by Swerling and Kalman around 1960, and one of its original applications was for space aircraft tracking in the Apollo navigation system. The Kalman filter assumes *a priori* knowledge of the system matrices and noise statistics. Indeed, in his ground-breaking paper, Kalman remarked on the difficulty of identifying such parameters: > In real life, however, the situation is usually reversed. One is given the covariance matrix \[of the state\] and the problem is to get \[the dynamics\] and the statistical properties of \[the disturbance\]. This is a subtle and presently largely unsolved problem in experimentation and data reduction.

Despite its wide use and success, practitioners employing the Kalman smoother still have to resort to manually tuning its parameters. As a result, many have proposed methods for instead automatically tuning the parameters in Kalman smoothers. One of the first methods proposed was to jointly learn the parameters and state/output sequence using expectation-maximization. More recent approaches employ different optimization approaches, including the simplex algorithm, coordinate descent, genetic algorithms, nonlinear programming using finite differencing to estimate the gradient, Bayesian optimization, and reinforcement learning.

Our approach is inspired by previous research on automatically tuning hyper-parameters in least squares. Our paper departs from prior work on tuning Kalman filters in several ways. Since our Kalman smoother can deal with missing measurements, we can hold out measurements and use those to evaluate the smoother. Also, our method makes explicit use of the gradient of the loss with respect to the parameters, leading to a more efficient optimization algorithm.

## Kalman smoother

### System model

We consider a linear system with dynamics and output or sensor measurements Here $x_{t} \in \text{R}^{n}$ is the state, $w_{t} \in \text{R}^{n}$ is the process noise, $y_{t} \in \text{R}^{p}$ is the output or sensor measurement, and $v_{t} \in \text{R}^{p}$ is the sensor noise, at time $t$. The matrix $A \in \text{R}^{n \times n}$ is the state dynamics matrix and $C \in \text{R}^{p \times n}$ is the output matrix.

We make the standard statistical assumptions that $w_{1},\ldots,w_{T - 1}$ are IID $\mathcal{N}{(0,W)}$ and $v_{1},\ldots,v_{T}$ are IID $\mathcal{N}{(0,V)}$, where the symmetric positive definite matrices $W$ and $V$ are the process and sensor noise covariance matrices, respectively.

### Missing measurements

We assume throughout that only the sequence $y_{t}$ is observed. Indeed, we will assume that not all of the measurements are available to us. To model this, we modify the output equation so that $y_{t} \in {({\text{R} \cup {\{?\}}})}^{p}$, where ? denotes a missing value. We have where $\mathcal{K} \subseteq {{\{ 1,\ldots,T\}} \times {\{ 1,\ldots,p\}}}$ is the set of (scalar) outputs that are available. For ${(t,i)} \notin \mathcal{K}$, we take ${(y_{t})}_{i} = ?$. We refer to entries of $y_{t}$ that are real as *known measurements* and the entries of $y_{t}$ that have the value ? as *missing measurements*.

### Smoothing

The goal in smoothing is to reconstruct or approximate the missing measurements given the known measurements. Since the outputs and states are jointly Gaussian, the maximum likelihood and conditional mean estimates of the missing output values are the same, and can be found as the solution of the constrained least squares problem with variables ${\hat{x}}_{1},\ldots,{\hat{x}}_{T}$ and ${\hat{y}}_{1},\ldots,{\hat{y}}_{T}$.

Also, the problem has a simple and widely used recursive solution for ${\hat{x}}_{t}$ when $\mathcal{K} = {{(1,\ldots,m)} \times {(1,\ldots,T)}}$, and also when $T\rightarrow\infty$. This recursive solution is often referred to as the Kalman filter.

### Solving the Kalman smoothing problem

There are many ways to solve the Kalman smoothing problem. One method is to eliminate the equality constraint \[§4.2.4\] and solve the resulting unconstrained least squares problem, which has a banded coefficient matrix. This method has time and space complexity of order $T{({n + p})}^{2}$. We give some details on another method that has roughly the same complexity, but is simpler since it does not require eliminating the equality constraints.

Let $N = {T{({n + p})}}$ and define the vector $z \in \text{R}^{N}$ as $z = {({\hat{x}}_{1},\ldots,{\hat{x}}_{T},{\hat{y}}_{1},\ldots,{\hat{y}}_{T})}$. Using the variable $z$, we can express the estimation problem compactly as the constrained least squares problem where $B \in \text{R}^{{|\mathcal{K}|} \times N}$ is a selector matrix and $c \in \text{R}^{|\mathcal{K}|}$ contains the corresponding entries of $y_{t}$. Concretely, if we assume that $\mathcal{K}$ is ordered, then if $\mathcal{K}_{j} = {(i,t)}$, the $j$th row of $B$ is $e_{{Tn} + {tp} + i}$ and the $j$th entry of $c$ is ${(y_{t})}_{i}$. The matrix $D \in \text{R}^{N - {n \times N}}$ is given by The matrices $D$ and $B$ are evidently very sparse, since each have a density of approximately $\frac{1}{N}$.

The optimality conditions for can be expressed as where $\eta \in \text{R}^{|\mathcal{K}|}$ is the dual variable for the equality constraint and $v = {Dz}$. The KKT matrix, denoted by is also very sparse, since $B$ and $D$ are sparse.

We assume for the remainder of the paper that $M$ is full rank (if it is not, we can add a small amount of regularization to make it invertible). Therefore we can solve the KKT system using any method for solving a sparse system of linear equations, e.g., a sparse LU factorization. Since the sparsity pattern is banded (when re-ordered the right way), the complexity of the sparse LU factorization will be linear in $T$. We have also observed this to be true in practice (see figure 1).

### Judging a Kalman smoother

Suppose we have gathered a sequence of outputs denoted ${y_{1},\ldots,y_{T}} \in {({\text{R} \cup {\{?\}}})}^{p}$. We can judge how well a Kalman smoother is working on this sequence of observations by obscuring a fraction of the known outputs and comparing the outputs predicted by the Kalman smoother to those that actually occurred.

The first step in judging a Kalman smoother is to mask some fraction (e.g., 20%) of the non-missing entries in the observations, denoted by the set $\mathcal{M}_{i} \subseteq {{(1,\ldots,T)} \times {(1,\ldots,m)}}$, resulting in a *masked trajectory* ${\overset{\sim}{y}}_{1},\ldots,{\overset{\sim}{y}}_{T}$. That is, we let ${({\overset{\sim}{y}}_{t})}_{i} = ?$ for ${(i,t)} \in \mathcal{M}$ and ${({\overset{\sim}{y}}_{t})}_{i} = {(y_{t})}_{i}$ for ${(i,t)} \notin \mathcal{M}$.

We then solve the smoothing problem with $y_{t} = {\overset{\sim}{y}}_{t}$ and known set $\mathcal{K} \smallsetminus \mathcal{M}$, resulting in a predicted output trajectory ${\hat{y}}_{1},\ldots,{\hat{y}}_{T}$.

In order to judge the Kalman smoother, we calculate the squared difference between the predicted output trajectory and the actual trajectory in the entries that we masked, which is given by We refer to this quantity as the *prediction error*; the goal in the sequel will be to adjust the parameters to minimize this error. We note that the entries in the output should been suitably scaled or normalized such that is a good measure of prediction error for the given application.

## Kalman smoother auto-tuning

In this section we describe how to automatically tune the parameters in a Kalman smoother (that is, the dynamic matrices and covariance matrices) to minimize the prediction error on the held-out measurements. Once the parameters have been tuned, the Kalman smoother can be tested on another (unseen) output sequence.

Algorithm 4.1 Kalman smoother auto-tuning. given initial hyper-parameter vector θ1 ∈ Θ, initial step size t1, number of iterations niter, 1. Filter the output sequence. Let ŷ1, …, ŷT be the solution to. 2. Compute the gradient of the prediction error. gk = ∇θL (θ). 3. Compute the gradient step. θk + 1/2 = θk − tk gk. 4. Compute the proximal operator. θtent = proxtk r (θk + 1/2).

Increase step size and accept update. tk + 1 = (1.5) tk; θk + 1 = θtent.

Stopping criterion. quit if ∥(θk − θk + 1)/tk + (gk + 1 − gk)∥2 ≤ ϵ. 6. else Decrease step size and reject update. tk + 1 = (0.5) tk; θk + 1 = θk.

### Kalman smoother parameters

A Kalman smoother has four parameters, which we denote by Evidently, this parametrization of the Kalman smoother is not unique. For example, if $T \in \text{R}^{n \times n}$ is invertible, then ${\overset{\sim}{x}}_{t} = {Tx_{t}}$, $\overset{\sim}{A} = {TAT^{- 1}}$, $\overset{\sim}{W} = {T^{- 1}WT^{- T}}$, $\overset{\sim}{C} = {CT^{- 1}}$, and $\overset{\sim}{V} = V$ gives another representation of. As another example, scaling $W$ and $V$ by $\alpha > 0$ gives an equivalent representation of.

### Auto-tuning problem

The prediction error $L$ in is a function of the parameters, and from here onwards we denote that function by $L{(\theta)}$. To tune the Kalman smoother, we propose solving the optimization problem with variable $\theta$ (the parameters of the Kalman smoother), where $r:{\Theta\rightarrow\text{R}}$ is a regularization function. Here $\Theta$ denotes the set of allowable parameters and can, for example, include constraints on what parameters we are allowed to change. (The function $r$ evaluates to $+ \infty$ for $\theta \notin \Theta$, thus constraining $\theta$ to be in $\Theta$.)

The objective function $F:{\Theta\rightarrow\text{R}}$ is composed of two parts: the prediction error and the regularization function. The first term here encourages the Kalman filter to have the same outputs as those observed, and the second term encourages the parameters to be simpler or closer to an initial guess.

### Regularization functions

There are many possibilities for the regularization function $r$; here we describe a few. Suppose we have some initial guess for $A$, denoted $A_{nom}$. We could then penalize deviations of $A$ from $A_{nom}$ by letting, e.g., As another example, suppose we suspected that $C$ was low rank; then we could use where ${\| C\|}_{\ast}$ is the nuclear norm of $C$, i.e., the sum of the singular values of $C$. This regularizer encourages $C$ to be low rank. Of course, any combination of these regularization functions is possible.

### Allowable sets

There are also many possibilities for $\Theta$, the allowable set of parameters. One option is to only allow certain entries of $A$ to vary by letting the set of allowable $A$ matrices be for some set $\Omega$. If we wanted to keep $A$ fixed, we could let $\Theta = {\{ A_{nom}\}}$. Another sensible option is to let $A$ vary within a box by letting the set of allowable $A$ matrices be for some nominal guess $A_{nom}$ and hyper-parameter $\rho > 0$.

### Solution method

The auto-tuning problem is in general nonconvex, even if $\Theta$ and $r$ are convex, so it is very difficult to solve exactly. Therefore, we must resort to a local or heuristic optimization method to (approximately) solve it. There are many methods that we could use to (approximately) solve the auto-tuning problem (see, e.g., ). In this paper we employ one of the simplest, the proximal gradient method, since $F$ is differentiable in $\theta$ (see below).

The proximal gradient method is described by the iteration where $k$ is the iteration number, $t^{k} > 0$ is a step size, and the proximal operator of $tr{(\cdot)}$ is defined as When $\Theta$ is a convex set and $r$ is convex, evaluating the proximal operator of $r$ requires solving a (small) convex optimization problem. Also, the proximal operator often has a (simple) closed-form expression. We note that $r$ need not be differentiable.

We employ the proximal gradient method with the adaptive step size scheme and stopping condition described . The full algorithm for Kalman smoother auto-tuning is summarized in Algorithm 4.

### Computing the gradient

Evidently, the proximal gradient method requires computing the gradient of the prediction error with respect to the parameters, denoted ${\nabla_{\theta}L}{(\theta)}$. The sensitivity analysis of Kalman smoothing has previously been considered in the forward direction, i.e., how changes in the parameters affect the output \[3, §7\]. Justification for our derivation can be found in \[12, §3.5\].

To do this, we first form the gradient of $L$ with respect to ${\hat{y}}_{1},\ldots,{\hat{y}}_{T}$, given by Next we form the gradient of $L$ with respect to the solution to, which is given by Next we solve the linear system which only requires a backsolve if we have already factorized $M$. Since the KKT system $M$ is invertible, the prediction error is indeed differentiable.

The next step is to form the gradient of $L$ with respect to the coefficient matrix $D$, which is given by Since $\theta$ only affects $D$ at certain entries, we only need to compute $G$ at those entries. That is, we compute $G$ at the entries which we can efficiently do since The final step is to form the gradients with respect to the parameters, which are given by The complexity of computing the gradient is roughly the same complexity as solving the original problem, since it requires the solution of another linear system. However, the time required to compute the gradient is often lower since we cache the factorization of $M$.

## Experiments

In this section, we describe our implementation of Kalman smoother auto-tuning, as well as the results of some numerical experiments that illustrate the method. All experiments were performed on a single core of an unloaded Intel i7-8770K CPU.

### Reference implementation

We have implemented the Kalman smoother auto-tuning method described in this paper as an open-source Python package, available at Our CPU-based implementation has methods for performing Kalman smoothing with missing measurements and for tuning the matrices in the Kalman smoother (Algorithm 4). Our only dependencies are `scipy`, which we use for sparse linear algebra, and `numpy`, which we use for dense linear algebra.

### Performance

We ran our Kalman smoothing function on random problems with $n = p = 10$. Fig. 1 shows the execution time, averaged over ten runs, of solving the smoothing problem (denoted as *forward* in the figure), as well as computing the derivative with respect to the the parameters (denoted as *backward* in the figure). As expected, the time required to compute the solution and its derivative is roughly linear in the length of the sequence $T$. Empirically, we found that the time required to compute the derivative is roughly half of the time required to compute the solution. We remark that our method is very efficient and effortlessly scales to extremely large problem sizes.

Figure 1: Method timings for a random problem with n = p = 10.

### Human migration example

Suppose we have $n$ states, where the $i$th state has a population $x_{i}$. At some cadence, say yearly, a fraction of people in each state decide to move to another state. We take noisy measurements of the population in some of the states and wish to infer the population in every state, including those we have not even measured.

### Dynamics

The vector $x_{t} \in \text{R}^{n}$ denotes the population in each state at year $t$. The dynamics are described by where $A \in \text{R}_{+}^{n \times n}$. Here $A_{ij}$ denotes the fraction of the population in state $j$ that move to state $i$ each year.

### Outputs

Each year, we take noisy measurements of the populations in some of the states. The outputs are described by We use the set of known measurements $\mathcal{K}$ to denote the measurements we actually have access to.

### United States population data

We gathered yearly population data (in millions of people) for the $n = 48$ states in the continental U.S from the U.S. Census Bureau. The data includes all years from 1900 to 2018.

### Experiment details

Our goal is to learn the dynamics matrix, dynamics covariance, and output covariance via Kalman smoother auto-tuning. To this end, we use the regularization function ${r{(\theta)}} = 0$ and allowable set We initialize the parameters as For each year, we pick 30 out of the 48 states at random to be measured. In each year, of those measured, we pick 12 at random to be missing and 5 at random to be part of the test set. We ran the method for 50 iterations with $t_{0} = {1\text{×}10^{- 4}}$.

### Results

The prediction error decreased from 0.0097 to 0.0058. The test error decreased from 0.0041 to 0.0030. The algorithm took 31 seconds to run. Besides the purely numerical results, there are interesting interpretations of the resulting parameters. For example, we can interpret the off-diagonal entries in the $A$ matrix as the fraction of the population in one state that migrates to another state over the course of one calendar year. The biggest such entries are displayed in Tab. 1.

Table 1: Entries in the learned A matrix.

### Vehicle smoothing example

In vehicle smoothing, we have noisy measurements of the position, velocity, and acceleration of a vehicle over time, and wish to infer the true position, velocity, and acceleration at each time step.

### Dynamics

The state $x_{t} = {(p_{t},v_{t},a_{t})}$ is composed of the position $p_{t} \in \text{R}^{3}$, the velocity $v_{t} \in \text{R}^{3}$, and the acceleration $a_{t} \in \text{R}^{3}$. The dynamics are described by (This system is often referred to as a double integrator, since the derivative of $p_{t}$ is $v_{t}$ and the derivative of $v_{t}$ is $a_{t}$.)

### Outputs

Any output vector and linear output matrix is possible. In this specific example we use $y_{t} = {({\hat{p}}_{t},{\hat{a}}_{t},{({\hat{v}}_{t})}_{1},{({\hat{v}}_{t})}_{2})}$, so $p = 8$. The output is described by

### Data

We used the Sensor Play data recorder iOS application to record the acceleration, attitude, latitude, longitude, heading, speed, and altitude of an iPhone mounted on a passenger vehicle. We converted the latitude and longitude into local North-East-Up coordinates, used the heading to convert the speed into a velocity in local coordinates, and used the attitude to orient the acceleration to local coordinates. We recorded data for a total of 330 seconds with a sampling frequency of $100\ {Hz}$, resulting in $T = 33000$ measurements.

### Experiment details

Our goal is to learn the state and observation covariance matrices, via Kalman smoother auto-tuning. To this end, we penalize the off-diagonal entries of where $\alpha$ is a hyper-parameter (we use $\alpha = {1\text{×}10^{- 4}}$) and We initialize the covariances as $W_{0}^{- {1/2}} = I$, $V_{0}^{- {1/2}} = {{(0.01)}I}$, and initialize $A_{0}$ and $C_{0}$ as given in Sec. 5.2 and Sec. 5.2 respectively. We consider all measurement indices where the GPS or velocity change as known (since GPS is only useful when it changes) and all acceleration indices as known. We use 20% of the known position measurements as the missing measurements and another 20% as the test measurements. We ran the method for 25 iterations with $t_{0} = {1\text{×}10^{- 2}}$.

Figure 2: Smoothed position estimates before and after tuning.

### Results

The prediction error decreased from 13.23 to 2.97. The test error decreased from 16.57 to 1.37. The algorithm took 135 seconds to run. The diagonals of the final state and output covariance matrices were (Note that these matrices can be scaled and the smoothing result is the same, so only relative magnitude matters.) We observe that there is more state noise in north and east dimensions than up, which makes sense. Also, there is less state noise in velocity than in position. We also observe that there is much higher measurement noise for $z$ direction in GPS, which is true with GPS. In Fig. 2 we show the position estimates before and after tuning. Visually, we see significant improvement from tuning.
