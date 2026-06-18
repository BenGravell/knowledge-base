## Introduction

Reinforcement learning (RL) is the subfield of machine learning that studies how to use past data to enhance the future manipulation of a dynamical system. A control engineer might be puzzled by such a definition and interject that this is precisely the scope of control theory. That the RL and control communities remain practically disjoint has led to the co-development of vastly different approaches to the same problems. However, it should be impossible for a control engineer not to be impressed by the recent successes of the RL community such as solving Go.

Indeed, given this dramatic recent progress in reinforcement learning, a tremendous opportunity lies in deploying its data-driven systems in more demanding interactive tasks including self-driving vehicles, distributed sensor networks, and agile robotic systems. For RL to expand into such technologies, however, the methods must be both safe and reliable---the failure of such systems has severe societal and economic consequences, including the loss of human life. How can we guarantee that our new data-driven automated systems are robust? These types of reliability concerns are at the core of control engineering, and reinforcement learning practitioners might be able to make their methods robust by applying appropriate control tools for engineering systems to match prescribed safety guarantees.

This survey aims to provide a language for the control and reinforcement learning communities to begin communicating, highlighting what each can learn from the other. Controls is the theory of designing complex actions from well-specified models, while reinforcement learning often makes intricate, model-free predictions from data alone. Yet both RL and control aim to design systems that use richly structured perception, perform planning and control that adequately adapt to environmental changes, and exploit safeguards when surprised by a new scenario. Understanding how to properly analyze, predict, and certify such systems requires insights from current machine learning practice and from the applied mathematics of optimization, statistics, and control theory. With a focus on problems in continuous control, I will try to disentangle the similarities and differences of methods of the complementary perspectives and present a set of challenging problems whose solution will require significant input from both sets of practitioners.

I focus first on casting RL problems in an optimization framework, establishing the sorts of methodological tools brought to bear in contemporary RL. I then lay out the main solution techniques of RL including the dichotomy between the model-free and model-based methodologies. Next, I try to put RL and control techniques on the same footing through a case study of the linear quadratic regulator (LQR) with unknown dynamics. This baseline will illuminate the various trade-offs associated with techniques from RL and control. In particular, we will see that the so-called "model-free" methods popular in deep reinforcement learning are considerably less effective in both theory and practice than simple model-based schemes when applied to LQR. Perhaps surprisingly, I also show cases where these observations continue to hold on more challenging nonlinear applications. I then argue that model-free and model-based perspectives can be unified, combining their relative merits. This leads to a concluding discussion of some of the challenges at the interface of control and learning that must be solved before we can build robust, safe learning systems that interact with an uncertain physical environment, which will surely require tools from *both* the machine learning and control communities.

## What is reinforcement learning?

Reinforcement learning is the study of how to use past data to enhance the future manipulation of a dynamical system. How does this differ from ordinary machine learning? The main view of this survey is of reinforcement learning as optimal control when the dynamics are unknown. Our goal will be to find a sequence of inputs that drives a dynamical system to maximize some objective beginning with minimal knowledge of how the system responds to inputs.

In the classic optimal control problem, we begin with a dynamical system governed by the difference equation $x_{t + 1} = {f_{t}{(x_{t},u_{t},e_{t})}}$ where $x_{t}$ is the *state* of the system, $u_{t}$ is the control action, and $e_{t}$ is a random disturbance. $f_{t}$ is the rule that maps the current state, control action, and disturbance at time $t$ to a new state. Assume that at every time, we receive some reward $R{(x_{t},u_{t})}$ for our current $x_{t}$ and $u_{t}$. The goal is to maximize this reward. In terms of mathematical optimization, we aim to solve the problem

That is, we aim to maximize the expected reward over $N$ time steps with respect to the control sequence $u_{t}$, subject to the dynamics specified by the state-transition rule $f_{t}$. The expected value is over the disturbance, and assumes that $u_{t}$ is to be chosen having seen only the states $x_{0}$ through $x_{t}$ and previous inputs $u_{0}$ through $u_{t - 1}$. $R_{t}$ is the reward gained at each time step and is determined by the state and control action. Note that $x_{t}$ is not really a decision variable in the optimization problem: it is determined entirely by the previous state, control action, and disturbance. I will refer to a *trajectory*, $\tau_{t}$, as a sequence of states and control actions generated by a dynamical system.

Since the dynamics are stochastic, the optimal control problem typically allows a controller to observe the state before deciding upon the next action. This allows a controller to continually mitigate uncertainty through *feedback*. Hence, rather than optimizing over deterministic sequences of controls $u_{t}$, we instead optimize over policies. A *control policy* (or simply "a policy") is a function, $\pi$, that takes a trajectory from a dynamical system and outputs a new control action. Note that $\pi$ gets access only to previous states and control actions.

To slightly lower the notational burden, I will hereon work with the *time-invariant* version of Problem (2.1), assuming that the dynamical update rule is constant over time and that the rewards for state-action pairs are also constant:

The policies $\pi_{t}$ are the decision variables of the problem.

Let us now directly bring machine learning into the picture. What happens when we don't know the state-transition rule $f$? There are a variety of commonly occurring scenarios when we might lack such knowledge. We may have unknown relationships between control forces and torques in a mechanical system. Or we could have a considerably more complicated system such as a massive data center with complex heat transfer interactions between the servers and the cooling systems. Can we still solve Problem (2.3) well without a precise model of the dynamics? Some lines of work even assume that we don't know the reward function $R$, but for the purpose of this survey, it makes no difference whether $R$ is known or unknown. The important point is that we can't solve this optimization problem using standard optimization methods unless we know the dynamics. We must learn something about the dynamical system and subsequently choose the best policy based on our knowledge.

The main paradigm in contemporary RL is to play the following game. We decide on a policy $\pi$ and horizon length L. Then we pass this policy either to a simulation engine or to a real physical system and are returned a trajectory $\tau_{L}$ and a sequence of rewards $\{{R{(x_{t},u_{t})}}\}$. We want to find a policy that maximizes the reward with the fewest total number of samples computed by the oracle, and we are allowed to do whatever we'd like with the previously observed trajectories and reward information when computing a new policy. If we were to run $m$ queries with horizon length $L$, we would pay a total cost of $mL$. However, we are free to vary our horizon length for each experiment. This is our *oracle model* and is called *episodic reinforcement learning* (See, for example Chapter 3 of Sutton and Barto, Chapter 2 of Puterman, or Dann and Brunskill ). We want the expected reward to be high for our derived policy, but we also need the number of oracle queries to be small.

This oracle model is considerably more complicated than those typically considered in oracle models for optimization. Each episode returns a complex feedback signal of states and rewards. What is the best way to tie this information together in order to improve performance? What is the best way to query and probe a system to achieve high quality control with as few interventions as possible? Here "best" is also not clearly defined. Do we decide an algorithm is best if it crosses some reward threshold in the fewest number of samples? Or is it best if it achieves the highest reward given a fixed budget of samples? Or maybe there's a middle ground? This oracle provides a rich and complex model for interacting with a system and brings with it considerably more complexity than in standard stochastic optimization settings. What's the most efficient way to use all of the collected data in order to improve future performance?

### Connections to supervised learning

The predominant paradigm of machine learning is *supervised learning* or *prediction*. In prediction, the goal is to predict the variable $y$ from a vector of *features* $x$ such that on new data you are predicting $y$ from $x$ with high accuracy. This form of machine learning includes classification and regression as special cases. Most of the time when the term machine learning is used colloquially, it refers to this sort of prediction. From this perspective, niche topics like semi-supervised learning and matrix completion are prediction tasks as well.

By contrast, there are *two* special variables in reinforcement learning, $u$ and $r$. The goal now is to analyze the features $x$ and then subsequently choose a policy that emits $u$ so that $r$ is large.^11^1To achieve notational consistency, I am throughout adopting the control-centric notation of denoting state-action pairs as $(x,u)$ rather than $(s,a)$ as is commonly used in reinforcement learning. There are an endless number of problems where this formulation is applied from online decision making in games to engagement maximization on internet platforms. A key distinguishing aspect of RL is the control action $u$. Unlike in prediction, the practitioner can vary $u$, which has implications both for learning (e.g., designing experiments to learn about a given system) and for control (e.g., choosing inputs to maximize reward).

Reinforcement learning is clearly more challenging than supervised learning, but, at the same time, it can be considerably more valuable. Reinforcement learning provides a useful framework to conceptualize interaction in machine learning, and promises to help mitigate changing distributions, gaming, adversarial behavior, and unexpected amplification. There is a precarious trade-off that must be carefully considered: reinforcement learning demands interventions with the promise that these actions will directly lead to valuable returns, but the resulting complicated feedback loops are hard to study in theory, and failures can have catastrophic consequences.

## Strategies for solving reinforcement learning problems

Let us now turn to a taxonomy of the varied algorithmic frameworks for reinforcement learning, focused on solving Problem (2.3) when the state-transition function is unknown. *Model-Based* Reinforcement learning fits a model to previously observed data and then uses this model in some fashion to approximate the solution to Problem (2.3). *Model-Free* Reinforcement learning eschews the need for a system's model, directly seeking a map from observations to actions.

The role of models in reinforcement learning remains hotly debated. Model-free methods, as discussed below, aim to solve optimal control problems only by probing the system and improving strategies based on past rewards and states. Many researchers argue for algorithms that can innately learn to control without access to the complex details required to simulate a dynamical system. They argue that it is often easier to find a policy for a task than it is to fit a general purpose model of the system dynamics (see for example, the discussion in Chapter 3 of Volume 2 of Bertsekas ). Model-free methods are primarily divided into two approaches: *Policy Search* and *Approximate Dynamic Programming*. Policy Search directly searches for policies by using data from previous episodes in order to improve the reward. Approximate Dynamic Programming uses Bellman's principle of optimality to approximate Problem (2.3) using previously observed data.

Throughout, my aim will be to highlight the main conceptual ideas of different approaches and to avoid embroiling myself in a thorough discussion of the myriad of technical details required to make all of the statements crisply precise. What is important is that all of the approaches surveyed reduce to some sort of function fitting from noisy observations of the dynamical system, though performance can be drastically different depending on how you fit this function. In model-based reinforcement learning, we fit a model of the state transitions to best match observed trajectories. In approximate dynamic programming, we estimate a function that best characterizes the "cost to go" for experimentally observed states. And in direct policy search, we attempt to find a policy that directly maximizes the optimal control problem using only input-output data. The main question is which of these approaches makes the best use of samples and how quickly do the derived policies converge to optimality.

### Model-based reinforcement learning

One of the simplest and perhaps most obvious strategies to solve the core RL Problem (2.3) is to estimate a predictive model for the dynamical process and then to use it in a dynamic programming solution to the prescribed control problem. The estimated model is called the *nominal model*, and I will refer to control design assuming the estimated model is true as *nominal control*. Nominal control, commonly verbosely referred to as "control under the principle of certainty equivalence," serves as a useful baseline algorithm.

Estimation of dynamical systems is called *system identification* in the control community. System Identification differs from conventional estimation because one needs to carefully choose the right inputs to excite various degrees of freedom and because dynamical outputs are correlated over time with the parameters we hope to estimate, the inputs we feed to the system, and the stochastic disturbances. Once data are collected, however, conventional machine learning tools can be used to find the system that best agrees with the data and can be applied to analyze the number of samples required to yield accurate models.

Suppose we want to build a predictor of $x_{t + 1}$ from the trajectory history. A simple, classic strategy is simply to inject a random probing sequence $u_{t}$ for control and then measure how the state responds. Up to stochastic noise, we should have that

where $\varphi$ is some model aiming to approximate the true dynamics. $\varphi$ might arise from a first-principles physical model or might be a non-parametric approximation by a neural network. The state-transition function can then be fit using supervised learning. For instance, a model can be fit by solving the least squares problem

Let $\hat{\varphi}$ denote the function fit to the collected data to model the dynamics. Let $\omega_{t}$ denote a random variable that we will use as a model for the noise process. With such a point estimate for the model, we might solve the optimal control problem

In this case, we are solving the wrong problem to get our control policies $\pi_{t}$. Not only is the model incorrect, but this formulation requires some plausible model of the noise process. But if $\hat{\varphi}$ and $f$ are close, this approach might work well in practice.

### Approximate Dynamic Programming

Approximate dynamic programming approaches the RL problem by directly approximating the optimal control cost and then solving this approximation with techniques from dynamic programming. The dynamic programming solution to Problem (2.3) is based on the *principle of optimality*: if you've found an optimal control policy for a time horizon of length $N$, $\pi_{1},\ldots,\pi_{N}$, and you want to know the optimal strategy starting at state $x$ at time $t$, then you just have to take the optimal policy starting at time $t$, $\pi_{t},\ldots,\pi_{N}$. Dynamic programming then lets us recursively find a control policy by starting at the final time and recursively solving for policies at earlier times.

Define the *Q-function* for (2.3) to be the mapping

The Q-function determines the value of the optimal control problem that is attained when the first action is set to be $u$ and the initial condition is $x$. Note that it then trivially follows that the optimal value of Problem (2.3) is ${\max_{u}\mathcal{Q}}{(x_{0},u)}$, and the optimal policy is ${\pi{(x_{0})}} = {{\arg{\max_{u}\mathcal{Q}}}{(x_{0},u)}}$. If we had access to the Q-function, we'd have everything we'd need to know to take the first step in the optimal control problem. We can use dynamic programming to compute this Q-function and the Q-function associated with every subsequent action. That is, we define the terminal Q-function to be

and then define recursively

This is the dynamic programing algorithm in a nutshell: we can recursively define the Q-functions by passing backward in time, and then compute the optimal controls from any starting $x_{0}$ by applying the policy that maximizes the right hand side of (3.3) at each time step. (3.3) is known as Bellman's equation. Note that for all time, the optimal policy is $u_{k} = {{\arg{\max_{u}\mathcal{Q}_{k}}}{(x_{k},u)}}$ and *depends only on the current state.*

Approximate Dynamic Programming methods typically try to compute these action-value functions from data. They do so by assuming that the Q-function is stationary. (i.e., ${\mathcal{Q}_{k}{(x,u)}} = {\mathcal{Q}{(x,u)}}$ for all $k$ and some function $\mathcal{Q}$). Such stationarity indeed arises assuming the time horizon is infinite. Consider the limit:

And we define the Q-function $\mathcal{Q}{(x_{0},u_{0})}$ to be the average reward accrued running from state $x_{0}$ with initial action $u_{0}$. Unfortunately, Problem (3.4) is not directly amenable to dynamic programming without introducing further technicalities. For mathematical convenience and also to connect to common practice in RL, it's useful to instead consider the *discounted* reward problem

where $\gamma$ is a scalar in $$ called the *discount factor*. For $\gamma$ close to $1$, the discounted reward is approximately equal to the average reward. The discounted cost has particularly clean optimality conditions that make it amenable to estimation. If we define $\mathcal{Q}_{\gamma}{(x,u)}$ to be the Q-function obtained from solving Problem (3.5) with initial condition $x$, then we have a discounted version of dynamic programming, now with the same Q-functions on the left and right hand sides:

The optimal policy is now for *all times* to let

This is a remarkably simple formula which is part of what makes Q-learning methods so attractive.

We can try to solve for the Q-function using stochastic approximation. If we draw a sample trajectory using the policy given by (3.6), then we should have (approximately and in expectation)

Thus, beginning with some initial guess $\mathcal{Q}_{\gamma}^{({old})}$ for the Q-function, we can update

where $\eta$ is a *step-size* or *learning rate*. (3.7) forms the basis of *Q-learning* algorithms.

Surveying ADP using only Q-functions is somewhat unorthodox. Most introductions to ADP instead focus on *value* functions where

Methods for estimating value functions are also widely used in reinforcement learning and developed through the perspective of estimation and stochastic approximation. In particular, Temporal Difference algorithms are derived from the value-function-centric perspective.

Note that in all cases here, though we have switched away from models, there's no free lunch. We are still estimating functions here, and we need to assume that the functions have some reasonable structure or we can't learn them. Choosing a parameterization of the Q-function *is a modeling assumption.* The term "model-free" almost always means "no model of the state transition function" when casually claimed in reinforcement learning research. However, this does not mean that modeling is not heavily built into the assumptions of model-free RL algorithms. Moreover, for continuous control problems these methods appear to make an inefficient use of samples. Suppose the internal state of the system is of dimension $d$. When modeling the state-transition function, (3.1) provides $d$ equations per time step. By contrast, we are only using $1$ equation per time step in ADP. Such inefficiency is certainly seen in practice below. Also troubling is the fact that we had to introduce the discount factor in order to get a simple Bellman equation. One can avoid discount factors, but this requires considerably more sophisticated analysis. Large discount factors do in practice lead to brittle methods, and the discount becomes a hyperparameter that must be tuned to stabilize performance. We will determine below when and how these issues arise in practice in control.

### Direct Policy Search

The most ambitious form of control without models attempts to directly learn a policy function from episodic experiences without ever building a model or appealing to the Bellman equation. From the oracle perspective, these policy driven methods turn the problem of RL into derivative-free optimization.

### A generic algorithm for sampling to optimize

In turn, let's first begin with a review of a general paradigm for leveraging random sampling to solve optimization problems. Consider the general unconstrained optimization problem

Any optimization problem like this is equivalent to an optimization over probability distributions on $z$:

If $z_{\star}$ is the optimal solution, then we'll get the same value if we put a $\delta$-function around $z_{\star}$. Moreover, if $p$ is a probability distribution, it is clear that the *expected value of the reward function* can never be larger than the maximal reward achievable by a fixed $z$. So we can either optimize over $z$ or we can optimize over *distributions* over $z$.

Since optimizing over the space of all probability densities is intractable, we must restrict the class of densities over which we optimize. For example, we can consider a family parameterized by a parameter vector $\vartheta$: $p{(u;\vartheta)}$ and attempt to optimize

If this family of distributions contains all of the Delta functions, then the optimal value will coincide with the non-random optimization problem. But if the family does not contain the Delta functions, the resulting optimization problem only provides a lower bound on the optimal value no matter how good of a probability distribution we find.

That said, this reparameterization provides a powerful and general algorithmic framework for optimization. In particular, we can compute the derivative of ${J{(\vartheta)}}:={{\mathbb{E}}_{p{(z;\vartheta)}}{\lbrack{R{(z)}}\rbrack}}$ using the following calculation (called "the log-likelihood trick"):

This derivation reveals that the gradient of $J$ with respect to $\vartheta$ is the expected value of the function

Hence, if we sample $z$ from the distribution defined by $p{(z;\vartheta)}$, we can compute $G{(z,\vartheta)}$ and will have an unbiased estimate of the gradient of $J$. We can follow this direction and will be running stochastic gradient descent on $J$, defining Algorithm 1.

3: while ending condition not satisfied do

Algorithm 1 is typically called REINFORCE and its main appeal is that it is trivial to implement. If you can efficiently sample from $p{(z;\vartheta)}$, you can run this algorithm on essentially any problem. But such generality must and does come with a significant cost. The algorithm operates on stochastic gradients of the sampling distribution, but the function we cared about optimizing---$R$---is only accessed through function evaluations. Direct search methods that use the log-likelihood trick are necessarily derivative free optimization methods, and, in turn, are necessarily less effective than methods that compute actual gradients, especially when the function evaluations are noisy. Another significant concern is that the choice of distribution can lead to very high variance in the stochastic gradients. Such high variance in turn implies that many samples need to be drawn to find a stationary point.

That said, the ease of implementation should not be readily discounted. Direct search methods are trivial to implement, and oftentimes reasonable results can be achieved with considerably less effort than custom solvers tailored to the structure of the optimization problem. There are two primary ways that this sort of stochastic search arises in reinforcement learning: Policy Gradient and Pure Random Search.

### Policy Gradient

As seen from Bellman's equation, the optimal policy for Problem (2.3) is always deterministic. Nonetheless, the main idea behind policy gradient is to use *probabilistic policies*. Probabilistic policies are optimal for other optimization-based control problems such as control of partially observed Markov decision processes or in zero-sum games. Hence, exploring their value for the RL problems studied in this survey does not appear too outlandish at first glance.

We fix our attention on *parametric, randomized policies* such that $u_{t}$ is sampled from a distribution $p{(\left. u \middle| {\tau_{t};\vartheta} \right.)}$ that is a function only of the currently observed trajectory and a parameter vector $\vartheta$. A probabilistic policy induces a probability distribution over trajectories:

Moreover, we can overload notation and define the reward of a trajectory to be

Then our optimization problem for reinforcement learning tidily takes the form of Problem (3.9). Policy gradient thus proceeds by sampling a trajectory using the probabilistic policy with parameters $\vartheta_{k}$, and then updating using REINFORCE.

Using the log-likelihood trick and (3.11), it is straightforward to verify that the gradient of $J$ with respect to $\vartheta$ *is not an explicit function of the underlying dynamics*. However, at this point this should not be surprising. By shifting to distributions over policies, we push the burden of optimization onto the sampling procedure.

### Pure Random Search

An older and more widely applied method to solve Problem (3.8) is to directly perturb the current decision variable $z$ by random noise and then update the model based on the received reward at this perturbed value. That is, we apply Algorithm 1 with sampling distribution ${p{(z;\vartheta)}} = {p_{0}{({z - \vartheta})}}$ for some distribution $p_{0}$. The simplest examples for $p_{0}$ would be the uniform distribution on a sphere or a normal distribution. Perhaps less surprisingly here, REINFORCE can again be run without any knowledge of the underlying dynamics. Note that in this case, the REINFORCE algorithm has a simple interpretation in terms of gradient approximation. Indeed, REINFORCE is equivalent to approximate gradient ascent of $R$

with the gradient approximation

This update says to compute a finite difference approximation to the gradient along the direction $\epsilon$ and move along the gradient. One can reduce the variance of such a finite-difference estimate by sampling along multiple random directions and averaging:

This is akin to approximating the gradient in the random subspace spanned by the $\epsilon_{i}$

This particular algorithm and its generalizations go by many different names. Probably the earliest proposal for this method was made by Rastrigin. In an unexpected historical surprise, Rastrigin initially developed this method to solve reinforcement learning problems! His main motivating example was an inverted pendulum. A rigorous analysis using contemporary techniques was provided by Nesterov and Spokoiny. Random search was also discovered by the evolutionary algorithms community, where it is called a $(\mu,\lambda)$-Evolution Strategy. Random search has also been studied in the context of stochastic approximation and bandits. Algorithms that are invented independently by four different communities probably have something good going for them.

The random search method is considerably simpler than the policy gradient algorithm but it uses much less structure from the problem as well. Since RL problems tend to be nonconvex, it is not clear which of these approaches is best unless we focus on specific instances. In light of this, in the next section we turn to a set of instances where we may be able to glean more insights about the relative merits of all of the approaches to RL covered in this section.

### Deep reinforcement learning

Note that in this section I have spent no time discussing *deep* reinforcement learning. That is because there is nothing conceptually different other than the use of neural networks for function approximation. That is, if one wants to take any of the described methods and make them deep, they simply need to add a neural net. In model-based RL, $\varphi$ is parameterized as a neural net, in ADP, the Q-functions or Value Functions are assumed to be well-approximated by neural nets, and in policy search, the policies are set to be neural nets. The algorithmic concepts themselves don't change. However, convergence analysis certainly will change, and algorithms like Q-learning might not even converge. The classic text Neuro-dynamic Programming by Bertsekas and Tsitisklis discusses the adaptations needed to admit function approximation. By eliminating the complicating variable of function approximation, we can get better insights into the relative merits of these methods, especially when focusing on a simple set of instances of optimal control, namely, the Linear Quadratic Regulator.

## Simplifying theme: The Linear Quadratic Regulator

With this varied list of approaches to reinforcement learning, it is difficult from afar to judge which method fares better on which problems. It is likely best to start simple and small and find the simplest non-trivial problem that can assist in distinguishing the various approaches to control. Though simple models are not the end of the story in analysis, it tends to be the case that if a complicated method fails to perform on a simple problem, then this indicates a flaw in the method.

I'd argue that in controls, the simplest non-trivial class of instances of optimal control is those with convex quadratic rewards and linear dynamics. That is, the problem of the Linear Quadratic Regulator (LQR):

Here, $Q$, $R$, and $S$ are positive semidefinite matrices. Do note that we have switched to minimization from maximization, as is conventional in optimal control. The state transitions are governed by a linear update rule with $A$ and $B$ appropriately sized matrices.

A few words are in order to defend this baseline as instructive for general problems in continuous control and RL. Though linear dynamics are somewhat restrictive, many systems are linear over the range we'd like them to operate. Indeed, enormous engineering effort goes into designing systems so that their responses are as close to linear as possible. From an optimization perspective, linear dynamics are the only class where we are guaranteed that our constraint set is convex, which is another appealing feature for analysis.

What about cost functions? Whereas dynamics are typically handed to the engineer, cost functions are completely at their discretion. Designing and refining cost functions are part of optimal control design, and different characteristics can be extracted by iteratively refining cost functions to meet specifications. This is no different in machine learning where, for example, combinatorial losses in classification are replaced with smooth losses like logistic or squared loss. Designing cost functions is a major challenge and tends to be an art form in engineering. But since we're designing our cost functions, we should focus our attention on costs that are easier to solve. Quadratic cost is particularly attractive not only because it is convex, but also for how it interacts with noise. The cost of the stochastic problem is equal to that of the noiseless problem plus a constant that is independent of the choice of $u_{t}$. The noise will degrade the achievable cost, but it will not affect how control actions are chosen.

Note that when the parameters of the dynamical system are known, the standard LQR problem admits an elegant dynamic programming solution. The control action is a *linear function* of the state

for some matrix $K_{t}$ that can be computed via a simple linear algebraic recursion with only knowledge of $(A,B,Q,R)$.

In the limit as the time horizon tends to infinity, the optimal control *policy* is *static*, *linear* *state feedback*:

where $K$ is a fixed matrix defined by

and $M$ is a solution to the *Discrete Algebraic Riccati Equation*

That is, for LQR on an infinite time horizon, ${\pi_{t}{(x_{t})}} = {- {Kx_{t}}}$. Here, $M$ is the unique solution of the Riccati equation where all of the eigenvalues of $A - {BK}$ have magnitude less than $1$. Finding this specific solution is relatively easy using standard linear algebraic techniques.

There are a variety of ways to derive these formulae. In particular, one can use dynamic programming as in Section 3.2. In this case, one can check that the Q-function on a finite time horizon satisfies a recursion

for some positive definite matrix $M_{k + 1}$. The limit of these matrices are the solution of (4.2)

Though LQR cannot capture every interesting optimal control problem, it has many of the salient features of the generic optimal control problem. Dynamic programming recursion lets us compute the control actions efficiently and, for long time horizons, a static policy is nearly optimal.

Now the main question to consider in the context of RL: What happens when we don't know $A$ and $B$? What's the right way to interact with the dynamical system in order to quickly and efficiently get it under control? Let us now dive into the different styles of reinforcement learning and connect them to ideas in controls, using LQR as a guiding baseline.

### The sample complexity of model-based RL for LQR

For LQR, maximum likelihood estimation of a nominal model is a least squares problem:

How well do these model estimates work for the LQR problem? Suppose we treat the estimates as true and use them to compute a state feedback control from a Riccati equation. While we might expect this to work well in practice, how can we verify the performance? As a simple case, suppose that the true dynamics are slightly unstable so that $A$ has at least one eigenvalue of magnitude larger than $1$. It is fully possible for the least squares estimates of such a mode is less than one, and, consequently, the optimal control strategy using the estimate will fail to account for the poorly estimated unstable eigenvalue. How can we include the knowledge that our model is just an estimate and not accurate with a small sample count? One possible solution is to use tools from robust control to mitigate this uncertainty.

### Coarse-ID Control: a new paradigm for learning to control

My collaborators and I have been considering an approach to merge robust control and high-dimensional statistics dubbed "Coarse-ID Control." The general framework consists of the following three steps:

Use supervised learning to learn a coarse model of the dynamical system to be controlled. I will refer to the system estimate as the *nominal system*.

Using either prior knowledge or statistical tools like the bootstrap, build probabilistic guarantees about the distance between the nominal system and the true, unknown dynamics.

Solve a *robust optimization* problem that optimizes control of the nominal system while penalizing signals with respect to the estimated uncertainty, ensuring stable, robust execution.

As long as the true system behavior lies in the estimated uncertainty set, we'll be guaranteed to find a performant controller. The key here is that we are using machine learning to identify not only the plant to be controlled, *but the uncertainty as well*. Indeed, the main advances in the past two decades of estimation theory consist of providing reasonable estimates of such uncertainty sets with guaranteed bounds on their errors as a function of the number of observed samples. Taking these new tools and merging them with old and new ideas from robust control allow us to bound the end-to-end performance of a controller in terms of the number of observations.

The coarse-ID procedure is well illustrated through the case study of LQR. We can guarantee the accuracy of the least squares estimates for $A$ and $B$ using novel probabilistic analysis. With the estimate of model error in hand, one can pose a robust variant of the standard LQR optimal control problem that computes a robustly stabilizing controller seeking to minimize the worst-case performance of the system given the (high-probability) norm bounds on our modeling errors.

To design a good control policy, we here turn to state-of-the-art tools from robust control. We leverage the recently developed System Level Synthesis (SLS) framework to solve this robust optimization problem. SLS lifts the system description into a higher dimensional space that enables efficient search for controllers. The proposed approach provides non-asymptotic bounds that guarantee finite performance on the infinite time horizon, and quantitatively bound the gap between the computed solution and the true optimal controller.

Suppose in LQR that we have a state dimension $d$ and control dimension $p$. Denote the minimum cost achievable by the optimal controller as $J_{\star}$. Our analysis guarantees that after a observing a trajectory of length $T$, we can design a controller that will have infinite-time-horizon cost $\hat{J}$ with

Here, the notation $\overset{\sim}{O}{( \cdot )}$ suppresses logarithmic factors and instance-dependent constants. In particular, we can guarantee that we stabilize the system after seeing only a finite amount of data.

Where Coarse-ID control differs from nominal control is that it explicitly accounts for the uncertainty in the least squares estimate. By appending this uncertainty to the original LQR optimization problem, we can circumvent the need to study perturbations of Riccati equations. Moreover, since the approach is optimization based, it can be readily applied to other optimal control problems beyond the LQR baseline.

### The sample complexity of model-free RL for LQR

Since we know that the Q-function for LQR is quadratic, we can try to estimate it by dynamic programming. Such a method was probably first proposed by Bradtke, Barto, and Ydstie. More recently, Tu showed that the *Least-squares Temporal Differencing* algorithm, also due to Bradtke and Barto, could estimate the value function of LQR to low error with $\overset{\sim}{O}\left( \sqrt{\frac{d^{2}}{T}} \right)$ samples. This estimator can then be combined with a method to improve the estimated policy over time.

Note that the bound on the efficiency of the estimator here is worse than the error obtained for estimating the model of the dynamical system. While comparing worst-case upper bounds is certainly not valid, it is suggestive that, as mentioned above, temporal differencing methods use only one defining equation per time step whereas model estimation uses $d$ equations per time step. So while the conventional wisdom suggests that estimating Q-functions for specific tasks should be simpler than estimating models, the current methods appear to be less efficient with aggregated data than system identification methods.

With regard to direct search methods, we can already see variance issues enter the picture even for small LQR instances. Consider the most trivial example of LQR:

Let $p{(u;\vartheta)}$ be a multivariate Gaussian with mean $\vartheta$ and variance $\sigma^{2}I$. Then

Obviously, the best thing to do would be to set $\vartheta = 0$. Note that the expected reward is off by $\sigma^{2}d$ at this point, but at least this would be finding a good guess for $u$. Also, as a function of $\vartheta$, the cost is *strongly convex*, and the most important thing to know is the expected norm of the gradient as this will control the number of iterations. Now, after sampling $u$ from a Gaussian with mean $\vartheta_{0}$ and variance $\sigma^{2}I$ and using formula (3.10), the first gradient will be

where $\omega$ is a normally distributed random vector with mean zero and covariance $\sigma^{2}I$. The expected norm of this stochastic gradient is on the order of

which indicates a significant scaling with dimension.

Several works have analyzed the complexity of this method, and the upper and lower bounds strongly depend on the dimension of the search space. The upper bounds also typically depend on the largest magnitude reward $B$. If the function values are noisy, even for convex functions, the convergence rate is $O{({({{d^{2}B^{2}}/T})}^{- {1/3}})}$, and this assumes you get the algorithm parameters exactly right. For strongly convex functions, this can be reduced to $O{({({{d^{2}B^{2}}/T})}^{- {1/2}})}$ function evaluations, but this result is also rather fragile to the choice of parameters. Finally, note that just adding an constant offset to the reward dramatically slows down the algorithm. If you start with a reward function whose values are in $\lbrack 0,1\rbrack$ and subtract one million from each reward, this will increase the running time of the algorithm by a factor of a million, even though the ordering of the rewards amongst parameter values remains the same.

## Numerical comparisons

The preceding analyses of the RL paradigms when applied to LQR are striking. A model-based approach combining supervised learning and robust control achieves nearly optimal performance given its sampling budget. Approximate dynamic programming appears to fare worse in terms of worst-case performance. And direct policy search seems to be of too high variance to work in practice. In this section, we implement these various methods and test them on some simple LQR instances to see how these theoretical predictions reflect practice.

### Double Integrator

As a simple test case, consider the classic problem of a discrete-time double integrator with the dynamical model

Such a system could model, say, the position (first state) and velocity (second state) of a unit mass object under force $u$.

As an instance of LQR, we can try to steer this system to reach point $0$ from initial condition ${x0} = {\lbrack{- 1},0\rbrack}$ without expending much force:

for some scalar $r_{0}$. Note that even in this simple instance there is an element of design: Changing the value of $r_{0}$ will change the character of the control law balancing expending energy versus speed or reaching the desired destination.

To compare the different approaches, I ran experiments on this instance with a small amount of noise ($e_{t}$ zero mean with covariance $10^{- 4}I$), and training episode length $L = 10$. The goal was to design a controller that works on an arbitrarily long time horizon using the fewest number of simulations of length $L$.

With one simulation (10 samples) using a white noise input with unit variance, the nominal estimate is correct to 3 digits of precision. And, not surprisingly, this returns a nearly optimal control policy. Right out of the box, this nominal control strategy works well on this simple example. Note that using a least squares estimator makes the nominal controller's life hard here because all prior information about sparsity on the state transition matrices is discarded. In a more realistic situation, the only parameter that would need to be estimated would be the $$ entry in $B$ which governs how much force is put out by the actuator and how much mass the system has.

Now, let's compare with approximate dynamic programming and policy search methods. For policy search, let us restrict to policies that use a static, linear gain as would be optimal on an infinite time horizon. Note that a static linear policy works almost as well as a time-varying policy for this simple LQR problem with two state dimensions. Moreover, there are only *two decision variables* for this simple problem. For Policy Gradient, I used the Adam algorithm to shape the iterates. I also subtracted the mean reward of previous iterates, a popular *baseline subtraction heuristic* to reduce variance (Dayan attributes this heuristic to Sutton and Williams ). I was unable to get policy gradient to converge without these additional algorithmic ornamentations. I also compared against a simple ADP method based called Least Squares Policy Iteration proposed by Lagoudakis and Parr. I ran each of these methods using 10 different random seeds. Figure 1 plots the median performance of the various methods with error bars encompassing the maximum and minimum over all trials. Both nominal control and LSPI are able to find high quality controllers with only ten observations. Direct policy methods, on the other hand, require many times as many samples. Policy gradient, in particular requires thousands of times as many samples as simple nominal control.

Figure 1: Cost for the double integrator model for various RL algorithms. The solid plots denote the median performance. Shaded regions capture the maximum and minimum performance. Nominal control and LSPI are indistinguishable from the optimal controller in this experiment and hence are omitted.

### Unstable Laplacian dynamics

As an illustrative example of the power of LQR as a baseline, let's now move to a considerably harder instance of LQR and show how it highlights issues of robustness and safety. Consider an idealized instance of "data center cooling," a popularized application of reinforcement learning.

Define the model to have three heat sources coupled to their own cooling devices. Each component of the state $x$ is the internal temperature of one each heat source, and the sources heat up under a constant load. They also shed heat to their neighbors. This can be approximately modeled by a linear dynamical system with state-transition matrices

Note that the open loop system here is *unstable*: With any nonzero initial condition, the state vector will blow up because the limit of $A^{k}$ is infinite. Moreover, if a method estimates one of the diagonal entries of $A$ to be less than $1$, we might guess that this mode is actually stable and put less effort into cooling that source. So it is imperative to obtain a high quality estimate of the system's true behavior for near optimal control. Or rather, we must be able to ascertain whether or not our current policy is safe or the consequences can be disastrous.

Let's try to solve the LQR problem with the settings $Q = I$ and $R = {1000I}$. This models a high relative cost for power consumption and hence may encourage small control inputs on modes that are estimated as stable. What happens for our RL methods on this instance?

Figure 2 compares nominal control to two versions of the robust LQR problem described in section 4.1. To solve the robust LQR problem, we end up solving a small semidefinite programming problem as described by Dean et al. These semidefinite programs are solved on my laptop in well under a second. The blue line denotes performance when we tell the robust optimization solver what the actual distance is from the nominal model to the true model. The green curve depicts what happens when we estimate this difference between the models using a bootstrap simulation. Note that estimating the error from data only yields slightly worse LQR performance than exactly knowing the true model error.

Figure 2: (left) Cost for the Laplacian model for varied models. The blue curve shows the performance of robust LQR when provided with the true distance between the estimate and model. The green curve displays the performance when the uncertainty is learned from data. (right) the fraction of the time that the synthesized control strategy returns a stabilizing controller.

Note also that the nominal controller does tend to frequently find controllers that fail to stabilize the true system. A necessary and sufficient condition for stabilization is for the matrix $A + {BK}$ to have all of its eigenvalues to be less than 1. We can plot how frequently the various search methods find stabilizing control policies when looking at a finite horizon in Figure 1 (right). The robust optimization really helps here to provide controllers that are guaranteed to find a stabilizing solution. On the other hand, in industrial practice nominal control does seem to work quite well. A great open problem is to find reasonable assumptions under which the nominal controller is stabilizing.

Figure 3: (left) Cost for the Laplacian model for varied models over 5000 iterations. (right) The fraction of the time that the synthesized control strategy returns a stabilizing controller.

Figure 3 additionally compares the performance to model-free methods on this instance. Here we again see that they are indeed far off from their model-based counterparts. The $x$ axis has increased by a factor of 10, and yet even the approximate dynamic programming approach does not find a decent solution. Surprisingly, LSPI, which worked very well on the double integrator, now performs worse than random search. This is likely because the LSPI subroutine requires a stabilizing controller for all iterations and also requires careful tuning of the discount factor. Not only are model-free methods sample hungry, but they fail to be safe. And safety is much more critical than sample complexity.

## Beyond the Linear Quadratic Regulator

Studying simple baselines such as LQR often provides insights into how to approach more challenging problems. In this section, we explore some directions inspired by our analysis of LQR.

### Derivative Free Methods for Optimal Control

Random search works well on simple linear problems and appears better than more complex methods like policy gradient. Does simple random search work less well on more difficult problems?

The answer, it turns out, is yes. The deep RL community has recently been using a suite of benchmarks to compare methods, maintained by OpenAI^22^2[https://gym.openai.com/envs/#mujoco](https://gym.openai.com/envs/#mujoco) and based on the MuJoCo simulator. Here, the optimal control problem is to get the simulation of a legged robot to walk as far and quickly as possible in one direction. Some of the tasks are very simple, but some are quite difficult like the complicated humanoid models with 22 degrees of freedom. The dynamics of legged robots are well specified by Lagrange's equations, but planning locomotion from these models is challenging because it is not clear how to best design the objective function and because the model is piecewise linear. The model changes whenever part of the robot comes into contact with a solid object, and hence a normal force is introduced that was not previously acting upon the robot. Hence, getting robots to work without having to deal with complicated nonconvex nonlinear models seems like a solid and interesting challenge for the RL paradigm. Moreover, seminal work by Tedrake, Zhang, and Seung demonstrated that direct policy search could rapidly find feedback control policies for certain constrained legged robot designs.

Levine and Koltun were among the first to use MuJoCo as a testbed for learning-based control, and were able to achieve walking in complex simulators without special-purpose techniques. Since then, these techniques have become standard continuous control benchmarks for reinforcement learning (see, for example ). Recently, Salimans and his collaborators at OpenAI showed that random search worked quite well on these benchmarks. In particular, they fit neural network controllers using random search with a few algorithmic enhancements. Random Search had indeed enjoyed significant success in some corners of the robotics community, and others had noted that in their applications, random search outperformed policy gradient. In another piece of great work, Rajeswaran *et al* showed that Natural Policy Gradient could learn *linear* policies that could complete these benchmarks. That is, they showed that static linear state feedback, like the kind we use in LQR, was also sufficient to control these complex robotic simulators. This of course left an open question: Can simple random search find linear controllers for these MuJoCo tasks?

Guy, Mania, and I tested this out, coding up a rather simple version of random search with a couple of small algorithmic enhancements. Many RL papers were using statistics of the states and whitening the states before passing them into the neural net mapping from state to action. We found that when random search performed the same whitening with linear controls, this algorithm was able to get state-of-the-art results on all of the MuJoCo benchmark tasks.

There are a few of important takeaways from this study. On the one hand, the results suggest that these MuJoCo demos are easy, or at least considerably easier than they were believed to be. Benchmarking is difficult, and having only a few simulation benchmarks encourages overfitting to these benchmarks. Indeed, it does seem like these benchmarks are more about taking advantage of simulation approximations in MuJoCo than they are about learning reasonable policies for walking. In terms of benchmarking, this is what makes LQR so attractive: LQR with unknown dynamics is a reasonable task to master as it is easy to specify new instances, and it is relatively easy to understand the limits of achievable performance.

Second, note that since our random search method is fast, we can evaluate its performance on many random seeds. All model-free methods exhibit alarmingly high variance on these benchmarks. For instance, on the humanoid task, the the model is slow to train almost a quarter of the time even when supplied with what we thought were good parameters (see Figure 4 (middle)). And, for those random seeds, we found the method returned rather peculiar gaits. Henderson *et al* and Islam *et al* observed this phenomenon with deep reinforcement learning methods, but our results on linear controllers suggest that such high variability will be a symptom of all model-free methods. Though direct policy search methods are easy to code up, their reliability on any reasonable control task remains in question.

Figure 4: (left) Sample frame of the MuJoCo humanoid. (middle) Variance of learning performance on 100 runs of random search on the humanoid model. Note that though high rewards are often achieved, it is more common to observe poor control performance from a random initialization. (right) Using MPC and a poor model, complex actions with humanoid simulations can be executed, such as climbing into a vehicle (image from supplementary video of Erez et al. ).

### Receding Horizon Control

Approximate dynamic programming is closely related to canonical receding horizon control (RHC) (also known as Model Predictive Control (MPC)). In RHC an agent makes a plan based on a simulation from the present until a short time into the future. The agent then executes one step of this plan, and then, based on what it observes after taking this action, returns to short-time simulation to plan the next action. This feedback loop allows the agent to link the actual impact of its choice of action with what was simulated, and hence can correct for model mismatch, noise realizations, and other unexpected errors.

To relate RHC to ADP, note that the discounted problem

is equivalent to Problem (3.5). Here we have just unrolled the cost beyond one step. Though this is trivial, it is again incredibly powerful: the longer we make the time horizon, the less we need to worry about the Q-function being accurate. Of course, now we need to worry about the accuracy of the state-transition map, $f$. But, especially in problems with continuous variables, it is not at all obvious which accuracy is more important in terms of finding algorithms with fast learning rates and short computation times. There is a trade-off between learning models and learning value functions, and this is a trade-off that needs to be better understood.

Though RHC methods appear fragile to model mismatch, the repeated feedback inside RHC can correct for many modeling errors. As an example, it is worth revisiting the robotic locomotion tasks inside the MuJoCo framework. These tasks were actually designed to test the power of a nonlinear RHC algorithm developed by Tassa, Erez, and Todorov. The receding horizon controller works to keep the robot upright even when the model is poorly specified. Moreover, the RHC approach to humanoid control solved for the controller in 7x real time in 2012. In 2013, the same research group published a cruder version of their controller that they used during the DARPA Robotics Challenge. All these behaviors are generated by RHC in real-time. Though the resulting walking is not of the same quality as what can be obtained from computationally intensive long-horizon trajectory optimization, it does look considerably better than the sort of gaits typically obtained by popular RL methods.

Is there a middle ground between expensive offline trajectory optimization and real time RHC? I think the answer is yes in the same way that there is a middle ground between learning dynamical models and learning Q-functions. The performance of a RHC system can be improved by better modeling of the Q-function that defines the terminal cost: The better a model you make of the Q-function, the shorter a time horizon you need for simulation, and the closer you get to real-time operation. Of course, if you had a perfect model of the Q-function, you could just solve the Bellman equation and you would have the optimal control policy. But by having an approximation to the Q-function, high performance can still be extracted in real time.

So what if we *learn* to iteratively improve the Q-function while running RHC? This idea has been explored in a project by Rosolia, Carvalho, and Borrelli. In their "Learning MPC" approach, the terminal cost is learned by a method akin to nearest neighbors. The terminal cost of a state is the value obtained last time that state was tried. If a state has not yet been visited, the cost is infinite. This formulation constrains the terminal condition to be in a state observed before. It enables the control system to explore new ways to decrease cost as long as it maintains the ability to reach a state that has already been demonstrated to be safe. This "nearest-neighbors" approach works surprisingly well in practice: in RC car demonstrations, the learned controller works better than a human operator after only a few laps around a fixed track.

Another reason to like this blended RHC approach to learning to control is that one can hard code in constraints on controls and states and easily incorporate models of disturbance directly into the optimization problem. Some of the most challenging problems in control are how to execute safely while continuing to learn more about a system's capability, and an RHC approach provides a direct route toward balancing safety and performance. Indeed, an interesting direction of future work would be merging the robust learning of Coarse-ID Control with receding horizon control.

## Challenges at the control-learning interface

We have set out to bridge the gap between the learning-centric views of RL and the model-centric views of control. Perhaps surprisingly, we found that for continuous control problems, machine learning seems best suited for model fitting rather than for direct control. Moreover, perhaps less surprisingly, we could seamlessly merge learned models and control action by accounting for the uncertainty in our model fits. Moreover, we showed how value functions and models could be learned in chorus and could provide impressive results on real embodied agents. These distinctions and connections are merely the beginning of what the control and machine learning communities can learn from each other. Let me close by discussing three particularly exciting and important research challenges that may be best solved with input from both perspectives.

### Merging perception and control

One of the grand aspirations of reinforcement learning is end-to-end control, mapping directly from sensors like pixels to actions. Computer vision has made major advances by adopting an "all-conv-net" end-to-end approach, and many, including industrial research at NVIDIA, suggest the same can be done for complex control tasks.

In general, this problem gets into very old intractability issues of nonlinear output feedback in control and partially observed Markov decision processes in reinforcement learning. Nonetheless, some early results in RL have shown promise in training optimal controllers directly from pixels. Of course, these results have even worse sample complexity than the same methods trained from states, but they are making progress.

In my opinion, the most promising approaches in this space follow the ideas of Guided Policy Search, which bootstraps standard state feedback to provide training data for a map from sensors directly to optimal action. That is, a mapping from sensor to action can be learned iteratively by first finding the optimal action and then finding a map to that control setting. A coupling along these lines where reliance on a precise state estimator is reduced over time could potentially provide a reasonably efficient method for learning to control from sensors.

However, these problems remain daunting. Moving from fully observed scenarios to partially observed scenarios makes the control problem exponentially more difficult. How to use diverse sensor measurements in a safe and reliable manner remains an active and increasingly important research challenge.

### Rethinking adaptive control

This survey has focused on "episodic" reinforcement learning and has steered clear of a much harder problem: adaptive control. In the adaptive setting, we want to learn the policy online. We only get *one* trajectory. The goal is, after a few steps, to have a model whose reward from here to eternity will be large. This is *very* different, and *much harder* that what people are doing in RL. In episodic RL, you get endless access to a simulator. In adaptive control, you get one go.

Even for LQR, the best approach to adaptive control is not settled. Pioneering work in the eighties used stochastic gradient-like techniques to find adaptive controls, but the guarantees for these schemes are all asymptotic. More recently, there has been a groundswell of activity in trying to understand this problem from the perspective of *online learning*. Beginning with work by Abbasi-Yadkori and Szepesvari, a variety of approaches have been devised to provide efficient schemes that yield near optimal control cost. Abbasi-Yadkori and Szepesvari's approach achieves an optimal reward building on techniques that give optimal algorithms for the multiarmed bandit. But their method requires solving a hard nonconvex optimization problem as a subroutine. Follow-up work has proposed methods using Thompson sampling, approximate dynamic programming, and even coarse-ID control, though no method has been found that is efficiently implementable and achieves optimal cost. Again, this emphasizes that even the simple LQR problem is not at all simple. New techniques must be developed to fully understand this baseline problem, but it is clear that insights from both machine learning and control will be necessary to develop efficient adaptive control that can cope with an ever-evolving world.

### Humans in the loop

One final important problem, which might be the most daunting of all, is how machines should learn when humans are in the loop. What can humans who are interacting with the robots do and how can we model human actions? Though economists may have a different opinion, humans are challenging to model.

One popular approach to modeling human-robot interaction is game theoretic. Humans can be modeled as solving their own optimal control problem, and then the human's actions enter as a disturbance in the optimal control problem. In this way, modeling humans is similar to modeling uncertain dynamic environments. But thinking of the humans as optimizers means that their behavior is constrained. If we know the cost, then we get a complex game theoretic version of receding horizon control. But as is usually the case, humans are bad at specifying their objectives, and hence what they are optimizing must be learned. This becomes a problem of *inverse optimal control* or *inverse reinforcement learning*, where we have to estimate the reward functions of the human and understand the loss accrued for crudely modeling these rewards.

### Towards Actionable Intelligence

As I've expressed before, I think that all of the daunting problems in machine learning are now RL problems. Whether they be autonomous transportation system or seemingly mundane social network engagement systems, actively interacting with reality has high stakes. Indeed, *as soon as a machine learning system is unleashed in feedback with humans, that system is a reinforcement learning system.* The broad engineering community must take responsibility for the now ubiquitous machine learning systems and understand what happens when we set them loose on the world.

Solving these problems is going to need advances in both machine learning and control. Perhaps this intersection needs a new name so that researchers can stop arguing about territory. I personally am fond of *actionable intelligence* as it sums up not only robotics but smarter, safer analytics. But I don't really care what we call it: There is a large community spanning multiple disciplines that is invested in making progress on these problems. Hopefully this tour has set the stage for a lot of great research at the intersection of machine learning and control, and I'm excited to see what progress the communities can make working together.
