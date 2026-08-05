<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Optimal Control Approach to Particle Filtering

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel particle filtering framework for continuous-time dynamical systems with continuous-time measurements. Our approach is based on the duality between estimation and optimal control, which allows reformulating the estimation problem over a fixed time window into an optimal control problem. The resulting optimal control problem has a cost function that depends on the measurements and the closed-loop dynamics under optimal control coincides with the posterior distribution over the trajectories for the corresponding estimation problem. This type of stochastic optimal control problem can be solved using a remarkable technique known as path integral control. By recursively solving these optimal control problems using path integral control as new measurements become available we obtain an optimal control-based particle filtering algorithm. A distinguishing feature of the proposed method is that it uses the measurements over a finite-length time window instead of a single measurement for the estimation at each time step, resembling the batch methods of filtering, and improving fault tolerance. The efficacy of our algorithm is illustrated with several numerical examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In control engineering, filtering refers to estimating the true state of a dynamical system using the the raw sensor measurements. It is a critical component in feedback control and plays an indispensable role in almost all applications related to control. There are many theories and algorithms for filtering that have been developed. The celebrated Kalman filter is for linear dynamics driven by Gaussian noise. It is optimal in the sense of mean-square error. It also computes the exact posterior distribution of the state given the available measurements. For nonlinear systems, the filtering problem is much more challenging; the posterior distribution of the state rarely has a simple parametrization. To attain the posterior distribution, one needs to solve a stochastic partial differential equation known as the Kushner--Stratonovich equation. The methods relying on discretizing the state space and the Kushner--Stratonovich equation are computationally infeasible for high dimensional problems. There are some algorithms that approximate posterior distributions using Gaussian distributions, including the extended Kalman filter (EKF) and the unscented Kalman filter (UKF).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the performance of this type of methods deteriorates as the posterior distribution drifts away from the Gaussian family.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One approach that avoids brutal force discretization of the state space while still retaining the richness of the posterior distributions is representing the distributions with particles. This type of methods are known as the particle filtering. Over the last decades, many different versions of particle filtering algorithms have been proposed. In the standard setup of particle filtering, the posterior distribution at the current step is approximated by $K$ weighted particles. These particles are propagated forward following a proposal density and then combined with the next measurement to estimate the posterior distribution at the next time step. The implementation of particle filtering is extremely easy if the proposal density is simple, which makes particle filtering a popular method for nonlinear filtering. Theoretically, it can be shown that as the number of particles $K$ goes to infinity, the empirical distribution of the particles converges to the true posterior distribution at each time step in some suitable sense. In practice, however, due to the potentially large difference between prior dynamics and posterior dynamics, the weights of the particles become degenerate quickly. That is, the weights of most of the particles become negligible and the mass of the particles only concentrates on a few particles, rendering a small effective particle size.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A resampling step is commonly adopted to mitigate the effects of degenerate weights. However, both in theory and in practice, how to choose a proper proposal density is critical and most particle filtering algorithms still perform poorly in high-dimensional problems, largely due to particle degeneracy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we consider nonlinear filtering problems for continuous-time diffusion dynamics with continuous-time measurements. We present a new particle filtering method based on an elegant duality between estimation and optimal control. Building on this duality, we are able to obtain a superior proposal density by (approximately) solving an optimal control problem and thus establish a particle filtering algorithm with great performance. Moreover, this duality makes it natural to resample the particles from the past; this is different to most particles filtering algorithms only samples in the present. This extra flexibility of updating samples in the past provides us the opportunity to correct numerical errors or errors induced by outlier in the previous filtering steps and makes the algorithm more robust to mistakes and outlier measurements. Empirically, we also observe that extending the sampling to the past, with proper proposals, can significantly mitigate the particle degeneracy issue.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed algorithm is most related to those proposed in and. In a block sampling strategy is proposed to resample particles in the past as in our algorithm. However, they focus on an abstract framework for general discrete-time systems. How to leverage the structure of the underlying dynamics to construct a proper proposal distribution is not discussed explicitly. In, an optimal control approach to smoothing is proposed. However, they consider smoothing problem over a fixed-time window. Moreover, though the dynamics they use is continuous-time diffusion, their measurement model is discrete-time. The same setting with continuous-time diffusion and discrete-time measurement is used. In addition, even though some path integral idea is used, the algorithm in is grid-based, not particle based. There are also some other particle filtering algorithms such as feedback particle filtering and particle flow filter that aim to improve the performance by using a better proposal.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is structured as follows. In Section 2, we provide a brief introduction to particle filtering and stochastic optimal control. The remarkable duality between filtering and optimal control is presented in Section 3. We then use this optimal control formulation of filtering to derive our particle filtering algorithm in Section 4. The algorithm is illustrated in Section 5 with several numerical examples. This is followed by a concluding remark in Section 6.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Particle filtering", "weight": 1.0} -->

The standard setting of particle filtering is over a discrete-time dynamic system | with observation model | Here $p_{X}{(\cdot)},p_{X}{(\cdot | \cdot)}$ and $p_{Y}{(\cdot | \cdot)}$ denote the prior distribution of the initial state, transition probability, and measurement probability respectively. Continuous-time systems can be converted into this form via a discretization over time.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Particle filtering", "weight": 1.0} -->

The main idea of particle filtering is to represent the posterior distributions $p{(\left. x_{t} \middle| y_{1:t} \right.)}$ by a collection of particles $\{ x_{t}^{1},x_{t}^{2},\ldots,x_{t}^{K}\}$ and the corresponding weights $\{ w_{t}^{1},w_{t}^{2},\ldots,w_{t}^{K}\}$ satisfying ${\sum_{i = 1}^{K}w_{t}^{i}} = 1$. More specifically, the posterior distribution is approximated by where $\delta_{x}$ is the Dirac delta distribution located at $x$. One of the most widely used particle filtering algorithm is the sequential important resampling (SIR) particle filter.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Particle filtering", "weight": 1.0} -->

It starts with $K$ independent samples ${\{ x_{0}^{i}\}}_{i = 1}^{K}$ from the prior distribution $p_{X}{(\cdot)}$. Since these samples are independently sampled, they are assigned equal weights, that is, $w_{0}^{1} = w_{0}^{2} = \cdots = w_{0}^{K} = {1/K}$. SIR uses the following updates to iteratively approximate $p{(\left. x_{t} \middle| y_{1:t} \right.)}$. A resampling step is implemented after several steps to avoid the weight degeneracy. The weight degeneracy is quantified by the effective ratio The value of $\gamma$ has maximum $1$, achieved when the weights are uniform. When the effective ratio is below a certain threshold $\gamma_{thres}$, a resampling step is carried out.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stochastic optimal control", "weight": 1.0} -->

Consider the stochastic dynamics described by the stochastic differential equation (SDE) where ${X_{t} \in {\mathbb{R}}^{n}},{u_{t} \in {\mathbb{R}}^{m}}$ denotes the state and control input respectively, and $W_{t} \in {\mathbb{R}}^{m}$ represents a standard Wiener process. The drift $b{(\cdot, \cdot)}$ and the input channel matrix $\sigma{(\cdot, \cdot)}$ are assumed to be Lipschitz continuous and bounded.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stochastic optimal control", "weight": 1.0} -->

In the finite horizon stochastic optimal control problem one seeks an optimal feedback control strategy that minimizes the cost function over a fixed time interval $\lbrack 0,T\rbrack$. Here, $w$ and $\Psi$ represent running cost and terminal cost respectively. This problem can be solved via dynamic programming, which boils down to solving the Hamilton-Jacobi-Bellman (HJB) equation where $\mathcal{L}_{t}^{\alpha}$ denotes the generator of the controlled process defined as for any sufficiently smooth $f{(\cdot)}$. The space-time function $V_{t}{(x)}$ is known as the cost-to-go function, capturing the minimum cost over the time window $\lbrack t,T\rbrack$ conditioned on $X_{t} = x$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stochastic optimal control", "weight": 1.0} -->

The optimal control strategy is of state feedback form $u_{t}^{\star} = {\alpha^{\star}{(t,X_{t})}}$ with The filtering algorithm developed in this work is closely related to the special case of stochastic control problems where the running cost is of the form Clearly, with this running cost, the minimization in can be solved in closed-form, yielding the optimal policy and the HJB equation simplifies to The running cost plays a crucial role in our framework. The quadratic cost in control in quantifies the difference of the controlled and the uncontrolled ($u_{t} \equiv 0$) process.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stochastic optimal control", "weight": 1.0} -->

More specifically, denote $\mathcal{P}_{u}$ the measure over the path space $\Omega = {C{({\lbrack 0,T\rbrack};{\mathbb{R}}^{n})}}$ induced by the dynamics, and $\mathcal{P}_{0}$ the measure associated with the uncontrolled process, then by the celebrated Girsanov theorem, It follows that the Kullback-Leibler divergence between $\mathcal{P}_{u}$ and $\mathcal{P}_{0}$ is where the expectation is with respect to the controlled process. Thus, the optimal control problem with running cost can be equivalently written as Note that the optimization variable becomes $\mathcal{P}_{u}$ instead of the control policy; the two are equivalent as the control policy fully determines the measure $\mathcal{P}_{u}$ and vice versa.

<!-- chunk {"id": "body-0017", "role": "body", "section": "A linear approach to stochastic optimal control", "weight": 1.0} -->

When the cost is of the form, it turns out that the above nonlinear optimal control problem can be solved in a linear manner. One way to see it is through the logarithmic transformation of the HJB equation. More specifically, let then a straightforward calculation points to The associated optimal control strategy reads Note that unlike the HJB which is nonlinear, is a linear partial differential equation (PDE); it is the Backward Kolmogorov equation associated with the (uncontrolled $u_{t} \equiv 0$) process and killing rate $g$. This transformation is remarkable; linear PDE is often much easier to solve than nonlinear PDE. In fact, this special PDE can be solved through Monte Carlo sampling as discussed below. This idea is the foundation of the path integral control.

<!-- chunk {"id": "body-0018", "role": "body", "section": "A linear approach to stochastic optimal control", "weight": 1.0} -->

To distinguish the processes associated with different control policies, we denote by $X^{u}$ the diffusion process with feedback control $u$ and ${\mathbb{E}}_{X^{u}}$ the corresponding expectation. By the celebrated Feynman-Kac formula, we have | Moreover, the optimal control at $(t,x)$ is | We remark that the expectation is with respect to the uncontrolled process $X^{0}$. This is counter-intuitive; it says that one can recover the optimal control $u^{\star}$ by taking expectation with respect to the process with zero control. In practice, one can simulate many trajectories from $X^{0}$ with $X_{t}^{0} = x$ and approximate $\varphi$ and $u^{\star}$ by taking average over these trajectories. This is exactly the path integral control.

<!-- chunk {"id": "body-0019", "role": "body", "section": "A linear approach to stochastic optimal control", "weight": 1.0} -->

One potential issue of is that the variance of the Monte Carlo approximation could be high and thus a large number of samples is needed to achieve a reasonable accuracy. This drawback can be mitigated by importance sampling as follows.

<!-- chunk {"id": "body-0020", "role": "body", "section": "A linear approach to stochastic optimal control", "weight": 1.0} -->

The estimated optimal control then becomes where $\Deltat$ is the stepsize and $\DeltaW_{t,i}$ is one discretized step of $W_{t,i}$. The variance of estimation is governed by the optimality of the policy $u{(t,x)}$. When $u$ is close to the optimal policy $u^{\star}$, the sample variance is small. In fact, when $u$ coincides with the optimal control $u^{\star}$, the sample variance is $0$, meaning one can estimate with one trajectory.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Smoothing as stochastic control", "weight": 1.0} -->

Consider a diffusion process with measurement noise where the measurement $Y_{t} \in {\mathbb{R}}^{p}$ is corrupted by white noise $dB_{t}$ weighted by $\sigma_{B} > 0$ and the initial state $X_{0}$ follows some prior distribution $\nu_{0}$. The smoothing problem is a particular type of Bayesian inference problem that aims at estimating the distribution of $X_{t}$ for $0 \leq t \leq T$ given the full history of measurement $\{{{Y_{t},\, 0} \leq t \leq T}\}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Smoothing as stochastic control", "weight": 1.0} -->

It was discovered in that the smoothing problem can be reformulated as a stochastic optimal control problem whose cost function depends on the measurements. To see this, denote the measure over the path space $\Omega$ induced by the process (21a) by $\mathcal{P}$. This serves as the prior measure for this Bayesian inference problem. Denote the posterior distribution over $\Omega$ by $\mathcal{Q}^{Y}$. By Kallianpur-Striebel formula, The right hand side of is the likelihood of the measurement. The variational form of the smoothing problem seeks a distribution $\overset{\sim}{\mathcal{P}}$ on the path space that minimizes Let $\overset{\sim}{\mathcal{P}}$ be parametrized by the diffusion process ${\overset{\sim}{X}}_{t}$ with dynamics Note that is slightly different from since in the control problem $\mathcal{P}_{u}$ and $\mathcal{P}_{0}$ share the same initial distribution while and (21a) don't.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Smoothing as stochastic control", "weight": 1.0} -->

Plugging and into yields an optimal control-like formulation for the smoothing problem. Apart from an extra term ${KL}{({\pi_{0} \parallel \nu_{0}})}$ related to the initial distributions, coincides with the optimal control problem -- if we take

<!-- chunk {"id": "body-0024", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

Building on the control formulation of smoothing and the linear approach to optimal control presented in Section 2.3, we propose a new particle filtering algorithm under the name "path integral particle filtering (PIPF)."

<!-- chunk {"id": "body-0025", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

We begin with the smoothing problem to estimate the posterior distribution $\mathcal{Q}^{Y}$ for the system over the time-window $\lbrack 0,T\rbrack$. As discussed in Section 3, this smoothing problem amounts to an optimal control problem where $g$ and $\Psi$ are given. The only difference to a standard optimal control problem is that the initial distribution $\pi_{0}$, apart from the control $u$, is also an optimization variable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

Clearly, this small difference doesn't change the optimal control strategy, which remains to be ${u^{\star}{(t,x)}} = {\sigma{(t,x)}'{{\nabla\log}\varphi}{(t,x)}}$ with $\varphi$ as. Indeed, the optimal control strategy to an optimal control problem is invariant with respect to the initial condition. Plugging this optimal control into we arrive at the optimization over $\pi_{0}$, which reads Apparently, its optimal solution is Note that $\pi_{0}^{\star}$ is exactly the posterior distribution of $X_{0}$ given the full observation $\{{{Y_{t},\, 0} \leq t \leq T}\}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

Thus, to sample from the posterior distribution $\mathcal{Q}^{Y}$, one can sample $K$ trajectories ${\{ X_{t}^{k}\}}_{k = 1}^{K}$ of the diffusion process under optimal control strategy $u^{\star}$ with initial distribution $\pi_{0}^{\star}$. The empirical distribution formed by these $K$ trajectories on the path space $\Omega$ is an estimation of the posterior distribution $\mathcal{Q}^{Y}$. Moreover, is an estimation of the posterior distribution of $X_{t}$ given the full observation $\{{{Y_{t},\, 0} \leq t \leq T}\}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

The above sampling strategy requires the exact posterior distribution $\pi_{0}^{\star}$ of $X_{0}$ and the exact optimal control strategy $u^{\star}$. This can be made possible using path integral control but is still computational demanding. Our strategy to sample from $\mathcal{Q}^{Y}$ is to sample trajectories with a suboptimal initial distribution $\pi_{0}$ and a suboptimal control strategy $u$, and then weight the trajectories through important sampling. More precisely, let $\overset{\sim}{\mathcal{P}}$ be the measure over the path space $\Omega$ associated with initial distribution $\pi_{0}$ and a suboptimal control strategy $u$, and ${\{ X_{t}^{k}\}}_{k = 1}^{K}$ be $K$ trajectories independently sampled from $\overset{\sim}{\mathcal{P}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

By Girsanov theorem, in view of, where $S^{u}$ is defined in with $g,\Psi$ as. Denote the value of $S^{u}{}$ along the trajectory $X_{t}^{k}$ by $S_{k}^{u}{}$ and define the weights It follows that $\mathcal{Q}^{Y}$ can be approximated by the empirical distribution formed by the trajectories ${\{ X_{t}^{k}\}}_{k = 1}^{K}$ and weights ${\{ w^{k}\}}_{k = 1}^{K}$, that is, are the normalized weights. Similarly, the posterior distribution of $X_{t}$ is approximated by The effectiveness of the above approximation depends on the variance of the weights ${\{ w^{k}\}}_{k = 1}^{K}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

This variance reduces to zero when $\pi_{0}$ and $u$ are optimal, that is, ${\pi_{0} = \pi_{0}^{\star}},{u = u^{\star}}$. In general, computing the exact optimal solution is too expensive and one has to use a suboptimal solution that is easier to compute. There are many methods that can generate suboptimal controller, including differential dynamic programming (DDP) and iterative linear quadratic regulator (iLQR). One can also start from the original smoothing problem for and adopt suboptimal smoothing methods such as extended Rauch-Rung-Striebel (ERTS). These suboptimal smoothing methods induce suboptimal $\pi_{0}$ and $u$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Path integral particle smoothing", "weight": 1.0} -->

To summarize, our path integral particle smoothing method consists of a proposal initial distribution $\pi_{0}$ and a proposal feedback $u$. They should be designed such that the distribution on path space induced by $\pi_{0}$ and $u$ is an approximation of the posterior distribution $\mathcal{Q}^{Y}$. A better proposal implies a better estimation with lower variance. Once the proposal is chosen, we can sample trajectories from the controlled diffusion process under the proposal control strategy $u$ with the proposal initial distribution $\pi_{0}$. The posterior distribution $\mathcal{Q}^{Y}$ is then approximated.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

We next move to the filtering problem. We are interested in the filtering problem of estimating the posterior distribution of $X_{t}$ conditioning on the past observation $\{{{Y_{\tau},0} \leq \tau \leq t}\}$. More precisely, denote by $\mathcal{Y}_{t} = \sigma{(Y_{\tau}:0 \leq \tau \leq t)}$ the sigma-field generated by the observation up to time $t$, then the objective of filtering is to estimation $\mathcal{P}{(X_{t} \in \cdot \mid \mathcal{Y}_{t})}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

The path integral particle smoothing algorithm proposed in Section 4.1 is suitable for smoothing problem over a fixed time window $\lbrack 0,T\rbrack$. To use this method for filtering problem where new measurements keep coming, one naive strategy is to carryout smoothing task over the time window $\lbrack 0,t\rbrack$. However, this requires recursively implementing the smoothing algorithm over a larger and larger time window. As $t$ increases, the computational complexity of the smoothing problem grows and will eventually become computationally infeasible.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

We propose to use a sliding window implementation of the smoothing algorithm for filtering. More specifically, consider the smoothing problem over the time window $\lbrack{t - H},t\rbrack$ of size $H > 0$. It is equivalent to the optimal control problem The prior distribution $\nu_{t - H}$ for this smoothing problem is the posterior distribution $\mathcal{P}{(X_{t - H} \in \cdot \mid \mathcal{Y}_{t - H})}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

Since $\nu_{t - H}$ already accounts for all the observations $\{{{Y_{\tau},0} \leq \tau \leq {t - H}}\}$, the solution to the smoothing problem in fact induces the exact posterior distribution over the trajectories $\{{{X_{\tau},{t - H}} \leq \tau \leq t}\}$, conditioned on the full history of observation $\{{{Y_{\tau},0} \leq \tau \leq t}\}$. Thus, by running the smoothing algorithm presented in Section 4.1 over a fixed-size time window $\lbrack{t - H},t\rbrack$, we can obtain the posterior distribution of $\mathcal{P}{({X_{t} \mid \mathcal{Y}_{t}})}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

To implement path integral particle smoothing algorithm over the time window $\lbrack{t - H},t\rbrack$, one needs to evaluate ${{d\nu_{t - H}}/d}\pi_{t - H}$ as. However, in the proposed path integral particle filtering method, the distribution $\nu_{t - H}$ doesn't have a closed-form and is represented by a collection of weighted particles as Thus, a natural way to sample trajectories over time interval $\lbrack{t - H},t\rbrack$ is to initialize them with ${\{ X_{t - H}^{k}\}}_{k = 1}^{K}$ and then follow the closed-loop dynamics under some suboptimal control policy $u$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

With this strategy, the proposal initial distribution $\pi_{t - H}$ satisfies Let ${\{ X_{\tau}^{k}\}}_{k = 1}^{K}$ be the $K$ generated trajectories and $S_{k}^{u}{({t - H},t)}$ be the value of of the trajectory $X_{\tau}^{k}$ over the time interval $\lbrack{t - H},t\rbrack$, then the posterior distribution over the trajectory space conditioning on the past observation $\{{{Y_{\tau},0} \leq \tau \leq t}\}$ is approximated by with ${\{{\hat{w}}^{k}\}}_{k = 1}^{K}$ being the normalized version of the weights To see the intuition of, assume that $\nu_{t - H}$ is obtained using the path integral particle smoothing algorithm over the time interval with proposal initial distribution $\nu_{0}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Path integral particle filtering", "weight": 1.0} -->

Following the arguments in Section 4.1 we know where $S_{k}^{u}{(0,{t - H})}$ is evaluated over some sampled trajectory over the time interval $\lbrack 0,{t - H}\rbrack$. Combining it with we conclude that where $S_{k}^{u}{(0,t)}$ is evaluated over the concatenated trajectory of ${X_{\tau}^{k},0} \leq \tau \leq {t - H}$ and ${X_{\tau}^{k},{t - H}} \leq \tau \leq t$. Instead of resampling the whole trajectory starting from the very beginning, in the sliding window filtering, all the past weights are recorded in the particle representation of $\nu_{t - H}$ and are combined with the measurement over $\lbrack{t - H},t\rbrack$ to estimate the posterior distribution.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

In this section we provide implementation details of the path integral particle filtering algorithm. Let $0 = t_{0} < t_{1} < t_{2} < \cdots$ be a sequence of time discretization points. It can be a constant stepsize discretization, i.e., ${t_{j + 1} - t_{j}} = {\Deltat}$, or any other more flexible discretization scheme. Set the sliding window size after time-discretization in the path integral particle filtering algorithm to be $H$ with a slightly abuse of notation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

The proposed particle filtering algorithm can be divided into two stages. For ${t_{j},j} \leq H$, the total number of time steps is less than the window size and thus we use path integral particle smoothing over the time interval $\lbrack 0,t_{j}\rbrack$ to estimate the posterior distribution $\mathcal{P}{(\left. X_{t_{j}} \middle| \mathcal{Y}_{t_{j}} \right.)}$. When $j > H$, we adopt the path integral particle filtering over the time interval $\lbrack t_{j - H},t_{j}\rbrack$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

In the sliding window stage over $\lbrack t_{j - H},t_{j}\rbrack$, the choice of particle representation for the prior distribution $\nu_{t_{j - H}}$ ($\mathcal{P}{(\left. X_{t_{j - H}} \middle| \mathcal{Y}_{t_{j - H}} \right.)}$) is crucial. We use the trajectories generated in the previous step over time interval $\lbrack t_{j - H - 1},t_{j - 1}\rbrack$ and weight them properly to obtain an estimation of $\nu_{t_{j - H}}$. The locations of the particles generated in this way account for the measurement up to time $t_{j - 1}$ and are thus match better with the posterior distribution $\mathcal{P}{(\left.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

X_{t_{j - H}} \middle| \mathcal{Y}_{t_{j}} \right.)}$, which is the ideal proposal initial distribution. More explicitly, the prior distribution $\nu_{t_{j - H}}$ is updated recursively as follows. Let the particle representation of the prior distribution $\nu_{t_{j - H - 1}}$ at the previous step be and $S_{k}^{u}$ be the values of evaluated over the sampled trajectories over time window $\lbrack t_{j - H - 1},t_{j - 1}\rbrack$, then In the above, to simplify the notation, the normalization for the weight is not displayed explicitly.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

The effective size of the samples decreases much slower than the standard SIR filter. Yet, a resampling step is needed after a long time horizon. For resampling, we start with the samples. We resample them based on the weights obtaining new samples ${\hat{X}}_{t_{j - H}}^{k}$. These samples follow approximately the distribution $\mathcal{P}{(\left. X_{t_{j - H}} \middle| \mathcal{Y}_{t_{j - 1}} \right.)}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

With these new samples, the prior distribution $\nu_{t_{j - H}}$ is approximated by Once a particle representation of $\nu_{t_{j - H}} = {\sum_{k = 1}^{K}{w_{p}^{k}X_{t_{j - H}}^{k}}}$ is arrived, one can start from it and apply path integral particle smoothing over the time window $\lbrack t_{j - H},t_{j}\rbrack$. This leads to the particle filtering result Figure 1: Pipeline diagram of PIPF.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

The overall structure of the proposed algorithm is illustrated in the Figure 1. The full path integral particle filtering algorithm is presented in Algorithm 1 and a subroutine of it over a given time window is provided in Algorithm 2. The prior distribution at each step is represented by weighted particles $\{ X_{p}^{k},w_{p}^{k}\}$. The filtering results $\mathcal{P}{(\left. X_{t_{j}} \middle| \mathcal{Y}_{t_{j}} \right.)}$ at the current step is represented by weighted particles $\{ X^{k},{\hat{w}}^{k}\}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

Input: L: Total Number of time steps {Xpk}: Samples from prior distribution ν0 {wpk}: Weight of samples, all ones H: Length of sliding windows j-th time interval ← [min (0, tj − H), tj] {Xk}, {ŵk}, {Xpk}, {wpk}← Algorithm 2 for j-th time interval Algorithm 1 Path Integral Particle Filtering (PIPF) Input: b, σ, σB: System model γt h r e s: threshold for resampling {Xpk}, {wpk}: Samples and weight from the previous step Output: {Xk}, {ŵk}: Filtering results {Xpk}, {wpk}: Samples and weight for the current step Sampling k-th trajectory Xτk initialized by Xpk.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

Evaluate the value of Sku over the trajectory Xτk Filtering samples: Xk = Xtjk Filtering weight: ŵk ∝ wpk exp [−Sku (ti, tj)] Prior sample: Xpk = Xti + 1k Prior weight: wpk ∝ wpk exp [−Sku (ti, ti + 1)] Effective ratio: ${\gamma = \frac{1}{K{\sum_{k = 1}^{K}{({\hat{w}}^{k})}^{2}}}}.$ {Xpk} ∼ multinomial ({Xpk}, {wpk} exp [−Sku (ti, tj)]) {wpk} ∝ exp [Sku (ti + 1, tj)] Algorithm 2 One Step of PIPF The performance of the PIPF algorithm depends on the length $H$ of the sliding window and the choice of proposal suboptimal control $u$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm and Implementation", "weight": 1.0} -->

When $H = 1$ and $u \equiv 0$, our algorithm reduces to the standard SIR algorithm as explained further in the following remark.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Without any control, i.e. $u = 0$, the algorithm resembles the SIR particle filter. Indeed, when $u = 0$, the location of the particles $X_{t}^{k}$ is only governed by the open-loop dynamics (21a) similar to the SIR particle filter. And the weights of the particles $w_{t}^{k} \propto {\exp{\lbrack{- {S_{k}^{0}{(0,t)}}}\rbrack}}$ where This is precisely the log-likelihood of the observation signal over the time interval $\lbrack 0,t\rbrack$. With a time discretization of the integral $0 = t_{0} < t_{1} < \ldots < t_{J} = t$, the weights can be expressed as multiplication of the likelihoods $\prod_{j = 1}^{J}{p{(\left.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Y_{t_{j}} \middle| X_{t_{j}}^{k} \right.)}}$, which is similar to how SIR particle filter updates the weights.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In this section we present several numerical examples to demonstrate the efficacy of the proposed path integral particle filtering algorithm. In the first example, we test the proposed algorithm in linear filtering problems. In the second example, we consider a nonlinear filtering problem where the optimal filtering can be obtained in closed form and show that PIPF is able to approximate this optimal filtering well.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Linear Filtering exmaples", "weight": 1.0} -->

We first consider the following one-dimensional state space model where $\kappa > 0$. The model corresponds to an Ornstein-Uhlenbeck process, whose measurements are corrupted with Gaussian noise. The posterior distribution is Gaussian, that is, ${p{(\left. X_{t} \middle| \mathcal{Y}_{t} \right.)}} = {N{(\left. X_{t} \middle| {m_{t},P_{t}} \right.)}}$ with Three filtering algorithms are compared for this problem: (i) the sequential importance resampling (SIR) particle filter; (ii) the path integral particle filter with zero controller (PIPF-zero) $u \equiv 0$; (iii) the path integral particle filter with linear quadratic regulator controller (PIPF-LQR). LQR is designed based on the cost function given. The simulations are executed for $L = 600$ times-steps with step-size ${\Deltat} = 0.01$. Both employ a sliding window size $H = 20$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Linear Filtering exmaples", "weight": 1.0} -->

All three algorithms use $K = 500$ particles.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Linear Filtering exmaples", "weight": 1.0} -->

It is well known that degenerated particles will lead a low effective ratio and resampling procedure can help ease the notorious degeneracy problem. We benchmark performance in term of the mean squared errors (m.s.e) between closed-form mean (covariance) and estimated mean (covariance) with resampling and without resampling. The results are depicted in Figure 2 and Figure 3 respectively. Another quantity to measure the quality of the particles is the effective ratio $\gamma$. This is depicted in Figure 4 in the absence of resampling. In the experiments, each algorithm is repeated for 50 trials with different random seeds. The solid curves represent the mean of 50 trials and the shaded regions represent the corresponding $1 \times$ standard deviation. From these results we can clearly see the advantage of the path integral particle filtering. Compared with SIR, the introduction of the sliding window in PIPF-zero, which only requires negligible memory footprint, can help reduce the bias of the estimation. The significant improvement of PIPF-LQR owes to the high effective ratio and high-quality particles controlled by the optimal control policy.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Linear Filtering exmaples", "weight": 1.0} -->

To study the effects of problem dimension on the filtering performance, we consider the multi-dimensional state space model where ${A \in {\mathbb{R}}^{n \times n}},{C \in {\mathbb{R}}^{p \times n}}$ represent the dynamics matrix and output matrix respectively. In our experiments, $A,C$ are randomly generated for each dimension size $n$ and are then fixed. In Figure 6 we display the performance of PIPF-LQR and SIR for different $n$ in terms of m.s.e (of means) and effective ratio without resampling. Clearly, PIPF-LQR scales better than SIR as $n$ increases.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Nonlinear Filtering exmaple", "weight": 1.0} -->

We next evaluate our PIPF algorithm on the Benes filter problem where $x_{0}$ is a given constant, and the constants ${\mu,\sigma_{W},h_{1},h_{2}} \in {\mathbb{R}}$ are parameters. Regardless being a nonlinear filtering problem, its posterior distribution has an analytical expression In the experiments, we use the model parameters ${{\mu = 1},{{h_{1} = 1},{{h_{2} = 0},{{\sigma_{W} = 1},{x_{0} = {- 5.0}}}}}}.$ The simulation is carried out for $L = 6000$ time steps with step-size ${\Deltat} = 0.001$. We compare the performance of our PIPF algorithm and SIR. Since the dynamics is nonlinear, we use a suboptimal control policy, iterative linear quadratic regulator (iLQR) for PIPF.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Nonlinear Filtering exmaple", "weight": 1.0} -->

iLQR approximates the nonlinear dynamics by linearizing it around a nominal trajectory and the cost by a quadratic function, yielding a LQR problem. The iLQR algorithm then solves the resulting LQR problem. The nominal trajectory is calculated by minimizing control cost Equation locally under noise-free version of the dynamics. In PIPF-iLQR, the linearization for iLQR is done at the beginning of each sliding window.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Nonlinear Filtering exmaple", "weight": 1.0} -->

The results are displayed in Figure 7-8. The sliding window size for PIPF-iLQR and PIPF-zero are set to be $H = 10$. In particular, Figure 7 displays the estimated posterior distributions of the state at several time points. These distributions are approximated using KDE density estimator with bandwidth $0.2$. In Figure 8, we show the m.s.e of the means with resampling and the effective ratio without resampling. From the experiments we see that even though the optimality of controller is not promised, PIPF-iLQR still outperforms other algorithms.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, buliding on the duality between optimal estimation and optimal control theory, we developed a novel particle filtering algorithm. This algorithm has several distinguish features compared with standard particle filtering algorithms, including high effective ratio and the ability to update samples in the past so as to improve robustness. Our algorithm can also be combined with most existing filtering algorithms such as EKF and UKF to improve their performance. In the future, we plan to extend our algorithm to tackle filtering for diffusion processes with jumps.
