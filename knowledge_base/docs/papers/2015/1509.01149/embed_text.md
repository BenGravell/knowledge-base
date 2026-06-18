## INTRODUCTION

The path integral optimal control framework provides a mathematically sound methodology for developing optimal control algorithms based on stochastic sampling of trajectories. The key idea in this framework is that the value function for the optimal control problem is transformed using the Feynman-Kac lemma into an expectation over all possible trajectories, which is known as a path integral. This transformation allows stochastic optimal control problems to be solved with a Monte-Carlo approximation using forward sampling of stochastic diffusion processes.

There have been a variety of algorithms developed in the path integral control setting. The most straight-forward application of path integral control is when the iterative feedback control law suggested in is implemented in its open loop formulation. This requires that sampling takes place only from the initial state of the optimal control problem. A more effective approach is to use the path integral control framework to find the parameters of a feedback control policy. This can be done by sampling in policy parameter space, these methods are known as Policy Improvement with Path Integrals. Another approach to finding the parameters of a policy is to attempt to directly sample from the optimal distribution defined by the value function. Other methods along similar threads of research include.

Another way that the path integral control framework can be applied is in a model predictive control setting. In this setting an open-loop control sequence is constantly optimized in the background while the machine is simultaneously executing the "best guess" that the controller has. An issue with this approach is that many trajectories must be sampled in real-time, which is difficult when the system has complex dynamics. One way around this problem is to drastically simplify the system under consideration by using a hierarchical scheme, and use path integral control to generate trajectories for a point mass which is then followed by a low level controller. Even though this approach may be successfull for certain applications, it is limited in the kinds of behaviors that it can generate since it does not consider the full non-linearity of dynamics. A more efficient approach is to take advantage of the parallel nature of sampling and use a graphics processing unit (GPU) to sample thousands of trajectories from the nonlinear dynamics.

A major issue in the path integral control framework is that the expectation is taken with respect to the uncontrolled dynamics of the system. This is problematic since the probability of sampling a low cost trajectory using the uncontrolled dynamics is typically very low. This problem becomes more drastic when the underlying dynamics are nonlinear and sampled trajectories can become trapped in undesirable parts of the state space. It has previously been demonstrated how to change the mean of the sampling distribution using Girsanov's theorem, this can then be used to develop an iterative algorithm. However, the variance of the sampling distribution has always remained unchanged. Although in some simple simulated scenarios changing the variance is not necessary, in many cases the natural variance of a system will be too low to produce useful deviations from the current trajectory. Previous methods have either dealt with this problem by artificially adding noise into the system and then optimizing the noisy system. Or they have simply ignored the problem entirely and sampled from whatever distribution worked best. Although these approaches can be successful, both are problematic in that the optimization either takes place with respect to the wrong system or the resulting algorithm ignores the theoretical basis of path integral control.

The approach we take here generalizes these approaches in that it enables for both the mean and variance of the sampling distribution to be changed by the control designer, without violating the underlying assumptions made in the path integral derivation. This enables the algorithm to converge fast enough that it can be applied in a model predictive control setting. After deriving the model predictive path integral control (MPPI) algorithm, we compare it with an existing model predictive control formulation based on differential dynamic programming (DDP). DDP is one of the most powerful techniques for trajectory optimization, it relies on a first or second order approximation of the dynamics and a quadratic approximation of the cost along a nominal trajectory, it then computes a second order approximation of the value function which it uses to generate the control.

## PATH INTEGRAL CONTROL

In this section we review the path integral optimal control framework. Let $\mathbf{x}_{t} \in {\mathbb{R}}^{N}$ denote the state of a dynamical system at time $t$, ${\mathbf{u}{(\mathbf{x}_{t},t)}} \in {\mathbb{R}}^{m}$ denotes a control input for the system, $\tau:{{\lbrack t_{0},T\rbrack}\rightarrow{\mathbb{R}}^{n}}$ represents a trajectory of the system, and ${d\mathbf{w}} \in {\mathbb{R}}^{p}$ is a brownian disturbance. In the path integral control framework we suppose that the dynamics take the form:

In other words, the dynamics are affine in control and subject to an affine brownian disturbance. We also assume that $\mathbf{G}$ and $\mathbf{B}$ are partitioned as:

Expectations taken with respect to are denoted as ${\mathbb{E}}_{\mathbb{Q}}\lbrack \cdot \rbrack$, we will also be interested in taking expectations with respect to the uncontrolled dynamics of the system (i.e with $\mathbf{u} \equiv 0$). These will be denoted ${\mathbb{E}}_{\mathbb{P}}\lbrack \cdot \rbrack$. We suppose that the cost function for the optimal control problem has a quadratic control cost and an arbitrary state-dependent cost. Let $\phi{(\mathbf{x}_{T})}$ denote a final the terminal cost, $q{(\mathbf{x}_{t},t)}$ a state dependent running cost, and define $\mathbf{R}{(\mathbf{x}_{t},t)}$ as a positive definite matrix. The value function $V{(\mathbf{x}_{t},t)}$ for this optimal control problem is then defined as:

The Stochastic Hamilton-Jacobi-Bellman equation for the type of system in and for the cost function in is given as:

where the optimal control is expressed as:

The solution to this backwards PDE yields the value function for the stochastic optimal control problem, which is then used to generate the optimal control. Unfortunately, classical methods for solving partial differential equations of this nature suffer from the curse of dimensionality and are intractable for systems with more than a few state variables.

The approach we take in the path integral control framework is to transform the backwards PDE into a path integral, which is an expectation over all possible trajectories of the system. This expectation can then be approximated by forward sampling of the stochastic dynamics. In order to effect this transformation we apply an exponential transformation of the value function

Here $\lambda$ is a positive constant. We also have to assume a relationship between the cost and noise in the system (as well as $\lambda$) through the equation:

The main restriction implied by this assumption is that $\mathbf{B}{(\mathbf{x}_{t},t)}$ has the same rank as $\mathbf{R}{(\mathbf{x}_{t},t)}$. This limits the noise in the system to only effect state variables that are directly actuated (i.e. the noise is control dependent). There are a wide variety of systems which naturally fall into this description, so the assumption is not too restrictive. However, there are interesting systems for which this description does not hold (i.e. if there are known strong disturbances on indirectly actuated state variables or if the dynamics are only partially known).

By making this assumption and performing the exponential transformation of the value function the stochastic HJB equation is transformed into the *linear* partial differential equation:

Here we've denoted the covariance matrix

as $\Sigma{(\mathbf{x}_{t},t)}$. This equation is known as the backward Chapman-Kolmogorov PDE. We can then apply the Feynman-Kac lemma, which relates backward PDEs of this type to path integrals through the equation:

Note that the expectation (which is the path integral) is taken with respect to $\mathbb{P}$ which is the uncontrolled dynamics of the system. By recognizing that the term $\Psi{(\mathbf{x}_{T})}$ is the transformed terminal cost: $e^{- {\frac{1}{\lambda}\phi{(\mathbf{x}_{T})}}}$ we can re-write this expression as:

where ${S{(\tau)}} = {{\phi{(\mathbf{x}_{T})}} + {\int_{t_{0}}^{T}{q{(\mathbf{x}_{t},t)}{dt}}}}$ is the cost-to-go of the state dependent cost of a trajectory. Lastly we have to compute the gradient of $\Psi$ with respect to the initial state $\mathbf{x}_{t_{0}}$. This can be done analytically and is a straightforward, albeit lengthy, computation so we omit it and refer the interested reader to. After taking the gradient we obtain:

Where the matrix ${\mathcal{G}}{(\mathbf{x}_{t},t)}$ is defined as:

Note that if $\mathbf{G}_{c}{(\mathbf{x}_{t},t)}$ is square (which is the case if the system is not over actuated) this reduces to $\mathbf{G}_{c}{(\mathbf{x}_{t},t)}^{- 1}$.

Equation is the path integral form of the optimal control. The fundamental difference between this form of the optimal control and classical optimal control theory is that instead of relying on a backwards in time process, this formula requires the evaluation of an expectation which can be approximated using forward sampling of stochastic differential equations.

### II-A Discrete Approximation

Equation provides an expression for the optimal control in terms of a path integral. However, these equations are for continuous time and in order to sample trajectories on a computer we need discrete time approximations.

We first discretize the dynamics of the system. We have that $\mathbf{x}_{t + 1} = {\mathbf{x}_{t} + {d\mathbf{x}_{t}}}$ where $d\mathbf{x}_{t}$ is defined as:

The term $\epsilon$ is a vector of standard normal Gaussian random variables. For the uncontrolled dynamics of the system we have:

Another way we can express $\mathbf{B}{(\mathbf{x}_{t},t)}d\mathbf{w}$ which will be useful is as:

Lastly we say: ${S{(\tau)}} \approx {{\phi{(\mathbf{x}_{T})}} + {\sum_{i = 0}^{N}{q{(\mathbf{x}_{t},t)}\Deltat}}}$ where $N = {{{({T - t})}/\Delta}t}$ Then by defining $\mathsf{p}$ as the probability induced by the discrete time uncontrolled dynamics we can approximate as:

Note that we have moved the $\Deltat$ term multiplying $\mathbf{u}$ over to the right-hand side of the equation and inserted it into the expectation.

## GENERALIZED IMPORTANCE SAMPLING

Equation provides an implementable method for approximating the optimal control via random sampling of trajectories. By drawing many samples from $\mathsf{p}$ the expectation can be evaluated using a Monte-Carlo approximation. In practice, this approach is unlikely to succeed. The problem is that $\mathsf{p}$ is typically an inefficient distribution to sample from (i.e the cost-to-go will be high for most trajectores sampled from $\mathsf{p}$). Intuitively sampling from the uncontrolled dynamics corresponds to turning a machine on and waiting for the natural noise in the system dynamics to produce interesting behavior.

In order to efficiently approximate the controls, we require the ability to sample from a distribution which is likely to produce low cost trajectories. In previous applications of path integral control the mean of the sampling distribution has been changed which allows for an iterative update law. However, the variance of the sampling distribution has always remained unchanged. In well engineered systems, where the natural variance of the system is very low, changing the mean is insufficient since the state space is never aggressively explored. In the following derivation we provide a method for changing both the initial control input and the variance of the sampling distribution.

### III-A Likelihood Ratio

We suppose that we have a sampling distribution with non-zero control input and a changed variance, which we denote as $\mathsf{q}$, and we would like to approximate using samples from $\mathsf{q}$ as opposed to $\mathsf{p}$. Now if we write the expectation term in integral form we get:

Where we are abusing notation and using $\tau$ to represent the discrete trajectory $(\mathbf{x}_{t_{0}},\mathbf{x}_{t_{1}},{\ldots\mathbf{x}_{t_{N}}})$. Next we multiply both integrals by $1 = \frac{\mathsf{q}{(\tau)}}{\mathsf{q}{(\tau)}}$ to get:

And we can then write this as an expectation with respect to $\mathsf{q}$:

We now have the expectation in terms of a sampling distribution $\mathsf{q}$ for which we can choose:

The initial control sequence from which to sample around.

The variance of the exploration noise which determines how aggressively the state space is explored.

However, we now have an extra term to compute $\frac{\mathsf{p}{(\tau)}}{\mathsf{q}{(\tau)}}$. This is known as the *likelihood ratio* (or Radon-Nikodym derivative) between the distributions $\mathsf{p}$ and $\mathsf{q}$. In order to derive an expression for this term we first have to derive equations for the probability density functions of $\mathsf{p}{(\tau)}$ and $\mathsf{q}{(\tau)}$ individually. We can do this by deriving the probability density function for the general discrete time diffusion processes $P{(\tau)}$, corresponding to the dynamics:

The goal is to find ${P{(\tau)}} = {P{(\mathbf{x}_{t_{0}},\mathbf{x}_{t_{1}},{\ldots\mathbf{x}_{t_{N}}})}}$. By conditioning and using the Markov property of the state space this probability becomes:

Now recall that a portion of the state space has deterministic dynamics and that we've partitioned the diffusion matrix as:

We can partition the state variables $\mathbf{x}$ into the deterministic and non-deterministic variables $\mathbf{x}_{t}^{(a)}$ and $\mathbf{x}_{t}^{(c)}$ respectively. The next step is to condition on $\mathbf{x}_{t + 1}^{(a)} = {F^{(a)}{(\mathbf{x}_{t},t)}} = {\mathbf{x}_{t}^{(a)} + {\left( {{\mathbf{f}^{(a)}{(\mathbf{x}_{t},t)}} + {\mathbf{G}^{(a)}{(\mathbf{x}_{t},t)}\mathbf{u}_{t}}} \right)dt}}$ since if this does not hold $P{(\tau)}$ is zero. We thus need to compute:

And from the dynamics equations we know that each of these one-step transitions is Gaussian with mean: ${\mathbf{f}^{(c)}{(\mathbf{x}_{t},t)}} + {\mathbf{G}^{(c)}{(\mathbf{x}_{t_{i}},t_{i})}\mathbf{u}{(\mathbf{x}_{t_{i}},t_{i})}}$ and variance:

We then define $\mathbf{z}_{i} = {\frac{d\mathbf{x}_{t_{i}}^{(c)}}{\Deltat} - {f^{(c)}{(\mathbf{x}_{t_{i}},t_{i})}}}$, and $\mu_{i} = {\mathbf{G}^{(c)}{(\mathbf{x}_{t_{i}},t_{i})}\mathbf{u}{(\mathbf{x}_{t_{i}},t_{i})}}$. Applying the definition of the Gaussian distribution with these terms yields:

And then using basic rules of exponents this probability becomes:

Where ${Z{(\tau)}} = {\prod_{i = 1}^{N}{{({2\pi})}^{n/2}{|\Sigma_{i}|}^{1/2}}}$. With this equation in hand we're now ready to compute the likelihood ratio between two diffusion processes.

### Theorem 1

Let $\mathsf{p}{(\tau)}$ be the probability density function for trajectories under the uncontrolled discrete time dynamics:

And let $\mathsf{q}{(\tau)}$ be the probability density function for trajectories under the controlled dynamics with an adjusted variance:

Where the adjusted variance has the form:

And define $\mathbf{z}_{i}$, $\mu_{i}$, and $\Sigma_{i}$ as before. Let $Q_{i}$ be defined as:

Then under the condition that each $A_{t_{i}}$ is invertible and each $\Gamma_{i}$ is invertible, the likelihood ratio for the two distributions is:

### Proof

In discrete time the probability of a trajectory is formulated according to the. We thus have $\mathsf{p}{(\tau)}$ equal to:

and $q{(\tau)}$ equal to:

Then dividing these two equations we have $\frac{\mathsf{p}(\tau)}{\mathsf{q}(\tau)}$ as:

Using basic rules of determinants it is easy to see that the term outside the exponent reduces to

So we need only show that $\zeta_{i}$ reduces to $Q_{i}$. Observe that at every timestep we have the difference between two quadratic functions of $\mathbf{z}_{i}$, so we can complete the square to combine this into a single quadratic function. If we recall the definition of $\Gamma_{i}$ from above, and define $\Lambda_{i} = {A_{t_{i}}^{T}\Sigma_{i}A_{t_{i}}}$ then completing the square yields:

Now we expand out the first quadratic term to get:

Notice that the two underlined terms are the same, except for the sign, so they cancel out and we're left with:

Now define ${\overset{\sim}{\mathbf{z}}}_{i} = {\mathbf{z}_{i} - \mu_{i}}$, and then re-write this equation in terms of $\overset{\sim}{\mathbf{z}_{i}}$:

which expands out to:

Which then simplifies to:

Now recall that $\Gamma_{i} = {({\Sigma_{i}^{- 1} - \Lambda_{i}^{- 1}})}^{- 1}$, so we can split the quadratic terms in $\Gamma_{i}^{- 1}$ into the $\Sigma_{i}^{- 1}$ and $\Lambda_{i}^{- 1}$ components. Doing this yields:

and by noting that the underlined terms cancel out we see that we're left with:

which is the same as:

And so $\zeta_{i} = Q_{i}$ which completes the proof. ∎

The key difference between this proof and earlier path integral works which use an application of Girsanov's theorem to sample from a non-zero control input is that this theorem allows for a change in the variance as well.

In the expression for the likelihood ratio derived here the last two terms (${2\mu_{i}^{T}\Sigma_{i}^{- 1}\left( {\mathbf{z}_{i} - \mu_{i}} \right)} + {\mu_{i}^{T}\Sigma_{i}^{- 1}\mu_{i}}$) are exactly the terms from Girsanov's theorem. The first term ($\left( {\mathbf{z}_{i} - \mu_{i}} \right)^{T}\Gamma_{i}^{- 1}\left( {\mathbf{z}_{i} - \mu_{i}} \right)$), which can be interpreted as penalizing over-aggressive exploration, is the only additional term.

### III-B Likelihood Ratio as Additional Running Cost

The form of the likelihood ratio just derived is easily incorporated into the path integral control framework by folding it into the cost-to-go as an extra running cost. Note that the likelihood ratio appears in both the numerator and denominator of. Therefore, any terms which do not depend on the state can be factored out of the expectation and canceled. This removes the numerically troublesome normalizing term $\prod_{j = 1}^{N}{|A_{t_{j}}|}$. So only the summation of $Q_{i}$ remains. Recall that $\Sigma = {\lambda\mathbf{G}{(\mathbf{x}_{t},t)}\mathbf{R}{(\mathbf{x}_{t},t)}^{- 1}\mathbf{G}{(\mathbf{x}_{t},t)}}$. This implies that:

Now define $\mathbf{H} = {\mathbf{G}{(\mathbf{x}_{t},t)}\mathbf{R}{(\mathbf{x}_{t},t)}^{- 1}\mathbf{G}{(\mathbf{x}_{t},t)}^{T}}$ and $\overset{\sim}{\Gamma} = {\frac{1}{\lambda}\Gamma}$. We then have:

Then by re-defining the running cost $q{(\mathbf{x}_{t},t)}$ as:

and ${\overset{\sim}{S}{(\tau)}} = {{\phi{(\mathbf{x}_{T})}} + {\sum_{j = 1}^{N}{\overset{\sim}{q}{(\mathbf{x},\mathbf{u},{d\mathbf{x}})}}}}$, we have:

Also note that $d\mathbf{x}_{t}$ is now equal to:

So we can re-write $\frac{d\mathbf{x}_{t}}{\Deltat} - {\mathbf{f}{(\mathbf{x}_{t},t)}}$ as:

And then since $\mathbf{G}{(\mathbf{x}_{t},t)}$ does not depend on the expectation we can pull it out and get the iterative update law:

### III-C Special Case

The update law is applicable for a very general class of systems. In this section we examine a special case which we use for all of our experiments. We consider dynamics of the form:

And for the sampling distribution we set $A$ equal to $\sqrt{\nu}I$. We also assume that $\mathbf{G}_{c}{(\mathbf{x}_{t},t)}$ is a square invertible matrix. This reduces ${\mathcal{H}}{(\mathbf{x}_{t},t)}$ to $\mathbf{G}_{c}{(\mathbf{x}_{t},t)}^{- 1}$. Next the dynamics can be re-written as:

Then we can interpret $\frac{1}{\sqrt{\rho}}\frac{\epsilon}{\sqrt{\Deltat}}$ as a random change in the control input, to emphasize this we will denote this term as ${\delta\mathbf{u}} = {\frac{1}{\sqrt{\rho}}\frac{\epsilon}{\sqrt{\Deltat}}}$. We then have ${\mathbf{B}{(\mathbf{x}_{t},t)}\frac{\epsilon}{\sqrt{\Deltat}}} = {\mathbf{G}{(\mathbf{x}_{t},t)}\delta\mathbf{u}}$. This yields the iterative update law as:

which can be approximated as:

Where $K$ is the number of random samples (termed rollouts) and $S{(\tau_{i,k})}$ is the cost-to-go of the $k_{th}$ rollout from time $t_{i}$ onward. This expression is simply a reward-weighted average of random variations in the control input. Next we investigate what the likelihood ratio addition to the running cost is. For these dynamics we have the following simplifications:

${\mathbf{z} - \mu} = {\mathbf{G}{(\mathbf{x}_{t},t)}\delta\mathbf{u}}$

${\overset{\sim}{\Gamma}}^{- 1} = {{({1 - \nu^{- 1}})}\mathbf{G}{(\mathbf{x}_{t},t)}^{- 1}\mathbf{R}{(\mathbf{x}_{t},t)}\mathbf{G}{(\mathbf{x}_{t},t)}}$

$\mathbf{H}^{- 1} = {\mathbf{G}{(\mathbf{x}_{t},t)}^{- 1}\mathbf{R}{(\mathbf{x}_{t},t)}\mathbf{G}{(\mathbf{x}_{t},t)}^{- 1}}$

Given these simplifications $\overset{\sim}{q}$ reduces to:

This means that the introduction of the likelihood ratio simply introduces the original control cost from the optimal control formulation into the sampling cost, which originally only included state-dependent terms.

## MODEL PREDICTIVE CONTROL ALGORITHM

We apply the iterative path integral control update law, with the generalized importance sampling term, in a model predictive control setting. In this setting optimization and execution occur simultaneously: the trajectory is optimized and then a single control is executed, then the trajectory is re-optimized using the un-executed portion of the previous trajectory to warm-start the optimization. This scheme has two key requirements:

Rapid convergence to a good control input.

The ability to sample a large number of trajectories in real-time.

The first requirement is essential because the algorithm does not have the luxury of waiting until the trajectory has converged before executing. The new importance sampling term enables tuning of the exploration variance which allows for rapid convergence, this is demonstrated in Fig. 1.

The second requirement, sampling a large number of trajectories in real-time, is satisfied by implementing the random sampling of trajectories on a GPU. The algorithm is given in Algorithm 1, in the parallel GPU implementation the sampling for loop (for k to K-1) is run completely in parallel.

Given: K: Number of samples;
(u0,u1,… uN − 1): Initial control sequence;
Δ t, xt0, f, G, B, ν: System/sampling dynamics;
uinit: Value to initialize new controls to;
while task not completed do

${\overset{\sim}{S}{(\tau_{{i + 1},k})}} = {{\overset{\sim}{S}{(\tau_{i,k})}} + \overset{\sim}{q}}$;

$\mathbf{u}_{i}\leftarrow{\mathbf{u}_{i} + \left\lbrack {\sum_{k = 1}^{K}\left( \frac{\left. \exp\left( - \frac{1}{\lambda}{\overset{\sim}{S}}_{(}\tau_{i,k}) \right. \right)\delta\mathbf{u}_{i,k}}{\left. \sum_{k = 1}^{K}\exp\left( - \frac{1}{\lambda}{\overset{\sim}{S}}_{(}\tau_{i,k}) \right. \right)} \right)} \right\rbrack}$;

Update the current state after receiving feedback;
check for task completion;

Algorithm 1 Model Predictive Path Integral Control

## EXPERIMENTS

We tested the model predictive path integral control algorithm (MPPI) on three simulated platforms A cart-pole, A miniature race car, and A quadrotor attempting to navigate an obstacle filled environment. For the race car and quadrotor we used a model predictive control version of the differential dynamic programming (DDP) algorithm as a baseline comparision. In all of these experiments the controller operates at 50 Hz, this means that the open loop control sequence is re-optimized every 20 milliseconds.

Figure 1: Average running cost for the cart-pole swing-up task as a function of the exploration variance ν and the number of rollouts. Using only the natural system variance the MPC algorithm does not converge in this scenario.

### V-A Cart-Pole

For the cart-pole swing-up task we used the state cost: ${q{(\mathbf{x})}} = {p^{2} + {500{({1 + {\cos{(\theta)}}})}^{2}} + {\overset{˙}{\theta}}^{2} + {\overset{˙}{p}}^{2}}$, where $p$ is the position of cart, $\overset{˙}{p}$ is the velocity and $\theta,\overset{˙}{\theta}$ are the angle and angular velocity of the pole. The control input is desired velocity, which maps to velocity through the equation: $\overset{¨}{p} = {10{({u - \overset{˙}{p}})}}$. The disturbance parameter $\frac{1}{\sqrt{\rho}}$ was set equal $.01$ and the control cost was $\mathbf{R} = 1$. We ran the MPPI controller for 10 seconds with a 1 second optimization horizon. The controller has to swing-up the pole and keep it balanced for the rest of the 10 second horizon. The exploration variance parameter, $\nu$, was varied between $1$ and $1500$. The MPPI controller is able to swing-up the pole faster with increasing exploration variance. Fig. 1 illustrates the performance of the MPPI controller as the exploration variance and the number of rollouts are changed. Using only the natural variance of the system for exploration is insufficient in this task, in that case (not shown in the figure) the controller is never able to swing-up the pole which results in a cost around 2000.

### V-B Race Car

In the race car task the goal was to minimize the objective function: ${q{(\mathbf{x})}} = {{100d^{2}} + {({v_{x} - 7.0})}^{2}}$. Where $d$ is defined as: $d = {|{{\left( \frac{x}{13} \right)^{2} + \left( \frac{y}{6} \right)^{2}} - 1}|}$, and $v_{x}$ is the forward (in body frame) velocity of the car. This cost ensures that the car to stays on an elliptical track while maintaining a forward speed of 7 meters/sec. We use a non-linear dynamics model which takes into account the (highly non-linear) interactions between tires and the ground. The exploration variance was set to a constant $\nu$ times the natural variance of the system.

Figure 2: Performance comparison in terms of average cost between MPPI and MPC-DDP as the exploration variance ν changes from 50 to 300 and the number of rollouts changes from 10 to 1000. Only with a very large increase in the exploration variance is MPPI able to outperform MPC-DDP. Note that the cost is capped at 25.0

The MPPI controller is able to enter turns at close to the desired speed of 7 m/s and then slide through the turn. The DDP solution does not attempt to slide and significantly reduces its forward velocity before entering the turn, this results in a higher average cost compared to the MPPI controller. Fig. 2 shows the cost comparison between MPPI and MPC-DDP, and Figures 3 and 4 show samples of the trajectories taken by the two algorithms as well as the velocity profiles.

Figure 3: Comparison of DDP (left) and MPPI (right) performing a cornering maneuver along an ellipsoid track. MPPI is able to make a much tigther turn while carrying more speed in and out of the corner than DDP. The direction of travel is counterclockwise.

Figure 4: Comparison of DDP (left) and MPPI (right) performing a cornering maneuver along an ellipsoid track. MPPI is able to make a much tigther turn while carrying more speed in and out of the corner than DDP.

### V-C Quadrotor

The quadrotor task was to fly through a field filled with cylindrical obstacles as fast as possible. We used the quadrotor dynamics model from. This is a non-linear model which includes position, velocity, euler angles, angular acceleration, and the rotor dynamics. We randomly generated three forests, one where obstacles are on average 3 meters apart, the second one 4 meters apart, and the third 5 meters apart. We then separately created cost functions for both MPPI and DDP which guide the quadrotor through the forest as quickly as possible.

Figure 5: Left: sample DDP trajectory through 4m obstacle field, Right: Sample MPPI trajectory through the same field. Since the MPPI controller can directly reason about the shape of the obstacles it is able to safely pass through the field taking a much more direct route.

The cost function for MPPI was of the form: ${q{(\mathbf{x})}} = {{2.5{({p_{x} - p_{x}^{des}})}^{2}} + {2.5{({p_{y} - p_{y}^{des}})}^{2}} + {150{({p_{z} - p_{z}^{des}})}^{2}} + {50\psi^{2}} + {\| v\|}^{2} + {350{\exp{({- \frac{d}{12}})}}} + {1000C}}$ where $(p_{x},p_{y},p_{z})$ denotes the position of the vehicle. $\psi$ denotes the yaw angle in radians, v is velocity, and $d$ is the distance to the closest obstacle. $C$ is a variable which indicates whether the vehicle has crashed into the ground or an obstacle. Additionally if $C = 1$ (which indicates a crash), the rollout stops simulating the dynamics and the vehicle remains where it is for the rest of the time horizon. We found that the crash indicator term is not useful for the MPC-DDP based controller, this is not surprising since the discontinuity it creates is difficult to approximate with a quadratic function. The term in the cost for avoiding obstacles in the MPC-DDP controller consists purely of a large exponential term: $2000{\sum_{i = 1}^{N}{\exp{({- {\frac{1}{2}d_{i}^{2}}})}}}$, note that this sum is over all the obstacles in the proximity of the vehicle whereas the MPPI controller only has to consider the closest obstacle.

Figure 6: Time to navigate forest. Comparison between MMPI and DDP.

Since the MPPI controller can explicitly reason about crashing (as opposed to just staying away from obstacles), it is able to travel both faster and closer to obstacles than the MPC-DDP controller. Fig. 7 shows the difference in time between the two algorithms and Fig. 6 the trajectories taken by MPC-DDP and one of the MPPI runs on the forest with obstacles placed on average 4 meters away.

Figure 7: Simulated forest environment used in the quadrotor navigation task.

## CONCLUSION

In this paper we have developed a model predictive path integral control algorithm which is able to outperform a state-of-the-art DDP method on two difficult control tasks. The algorithm is based on stochastic sampling of system trajectories and requires no derivatives of either the dynamics or costs of the system. This enables the algorithm to naturally take into account non-linear dynamics, such as a non-linear tire model. It is also able to handle cost functions which are intuitively appealing, such as an impulse cost for hitting an obstacle, but are difficult for traditional approaches that rely on a smooth gradient signal to perform optimization. The two keys to achieving this level of performance with a sampling based method are:

The derivation of the generalized likelihood ratio between discrete time diffusion processes.

The use of a GPU to sample thousands of trajectories in real-time.

The derivation of the likelihood ratio enables the designer of the algorithm to tune the exploration variance in the path integral control framework, whereas previous methods have only allowed for the mean of the distribution to be changed. Tuning the exploration variance is critical in achieving a high level of performance since the natural variance of the system is typically too low to achieve good performance.

The experiments considered in this work only consider changing the variance by a constant multiple times the natural variance of the system. In this special case the introduction of the likelihood ratio corresponds to adding in a control cost when evaluating the cost-to-go of a trajectory. A direction for future research is to investigate how to automatically adjust the variance online. Doing so could enable the algorithm to switch from aggressively exploring the state space when performing aggressive maneuvers to exploring more conservatively for performing very precise maneuvers.
