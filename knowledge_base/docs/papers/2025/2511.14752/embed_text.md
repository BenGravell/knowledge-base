## Introduction

Trajectory optimization methods are widely employed in modern guidance, navigation, and control (GNC) systems for their computational efficiency and convergence guarantees \[Malyuta_CSM, Bonalli_gusto\]. Though GNC problems are almost always nonconvex, convex optimization-based trajectory generation methods, such as sequential convex programming (SCP), have proven to be effective in solving several real-world problems, such as autonomous drone guidance, spacecraft rendezvous and docking, and planetary landing \[Malyuta_CSM, acikmese_lcvx\]. Convex optimization-based algorithms are typically guaranteed to converge to a stationary point, but since they are local methods, their solution is highly dependent on the initial guess \[Elango_ctcs, bryson2018applied\]. It follows that trajectory optimization algorithms generally produce suboptimal solutions in the neighborhood of their initial guess.

Sampling-based methods present an alternative to trajectory-optimization methods. Methods such as RRT \[lavalle1998_rrt\], A^∗^ \[hart1968_astar\], probabilistic roadmaps \[kavraki2002_probroadmaps\], among others, incrementally generate discrete points by sampling from a distribution to build a solution-space exploring tree \[lavalle2006planning\]. Violations of constraints are detected and used to guide sampling. The exploratory nature of sampling-based methods helps mitigate the challenge posed by local minima. However, these methods generally do not scale well with problem dimension. Moreover, they do not always consider optimality, and those that do require infinitely many samples to guarantee optimality \[orthey2023_sampling\].

Multi-start optimization has been used to promote exploration of a nonconvex landscape by solving multiple optimization problems with differing initializations \[Martí_Resende_Ribeiro_2013, resende2016_grasp\]. Diverse initial solutions are used to promote exploration of different regions of the search space. This method, while effective in combinatorial optimization applications, can lead to large computational overhead in trajectory optimization applications since each initialization explores the landscape in isolation, and information about basins of attraction is not shared, leading to independent redundant convergence to the same local minimum \[denobel_2024\].

Another technique for escaping local minima within trajectory optimization is to perturb the gradient with noise, helping the optimizer escape saddle points \[Kalakrishnan_Chitta_Theodorou_Pastor_Schaal_2011\]. However, the injected noise can produce trajectories that violate feasibility, making the method unsuitable for safety-critical applications \[Kalakrishnan_Chitta_Theodorou_Pastor_Schaal_2011\]. Moreover, this method is computationally intensive due to the large number of noisy trajectories simulated.

The augmented Lagrangian method is widely used for solving constrained optimization problems via a series of unconstrained problems. The alternating direction method of multipliers (ADMM) is a variant of the augmented Lagrangian scheme widely used for distributed and convex optimization, particularly due to its ability to handle problems with a separable structure efficiently \[MAL-016, Hosseini_Chapman_Mesbahi_2015, ryu2022_book\]. This ability to break down a complex problem is formalized by the concept of *operator splitting*, which is a mathematical framework for solving problems involving the sum of multiple terms by iteratively solving subproblems that handle each term independently.

ADMM has been used in the field of optimal control for exploiting structure in the context of model predictive control \[kang2015_mpc_admm, rey2017_mpcadmm, rey2020_mpcadmm\]. The problems solved by each agent are convex optimal control problems. In the context of nonconvex optimization, operator splitting was used to parallelize trajectory optimization for speed improvements in \[Wang2021_trajsplitting\]. In particular, ADMM was employed to temporally split a trajectory optimization problem so that agents could solve trajectory optimization problems with fewer discrete samples in parallel. A similar strategy was used to simultaneously compute optimal trajectories and time-varying linear feedback control policies in \[Vikas2017_Sequential_operator_splitting\].

Figure 1: Overview of standard SCP and OS-SCP. Initial state is represented by a black circle and goal state by black star. Two obstacles are shown in white.

This paper leverages operator splitting to promote exploration in SCP. This is achieved by constructing a population of agents with diverse initializations that each solve for locally optimal solutions and collectively form a consensus using the ADMM framework. This provides a structured framework for promoting exploration of a shared, nonconvex solution landscape. By initializing agents with diverse initial guesses, the agents are drawn to different regions of the solution space. Then, the agents are pulled towards a consensus, allowing the agents to escape stationary points where standard gradient-based methods would stagnate. We show that this process leads to increased exploration of the solution space over multi-start methods, enabling agents to converge to solutions about which no trajectories were initialized. We demonstrate empirically that the proposed exploration-focused operator splitting method escapes local stationary points in nonconvex trajectory optimization problems where gradient-based methods fail. An overview of the standard SCP approach and the proposed Operator-Splitting SCP (OS-SCP) approach is shown in Figure 1.

The remainder of this paper is structured as follows. Section II introduces concepts used in the exploratory OS-SCP algorithm. Section III introduces the proposed algorithm, and numerical results are presented in Section IV. Finally, concluding remarks are given in Section V.

Notation. The following notation is used throughout this work. We denote the set of functions that are $n -$times differentiable by $\mathcal{C}^{n}$. A vector of ones of length $n$ is denoted $\mathbf{1}_{n}$, and a vector of zeros of length $n$ is denoted $\mathbf{0}_{n}$. We use the shorthand $\lbrack K\rbrack$ to denote the set of integers $\{ 0,\ldots,K\}$. The sets of real numbers are denoted by $\mathbb{R}$ and positive reals by ${\mathbb{R}}_{+}$, and the sets of integers and positive integers are denoted $\mathbb{Z}$, and ${\mathbb{Z}}_{+}$, respectively. Given a continuous-time signal $x{(t)}$ sampled with period $\DeltaT$, we denote the value of the signal at time instant $k\DeltaT$, $k \in {\mathbb{Z}}_{+}$, by $x_{k} = {x{({k\DeltaT})}}$.

## Background

This section introduces key concepts used in the proposed operator splitting SCP framework introduced in the following section.

### II-A Consensus ADMM

Traditionally, consensus ADMM decomposes the objective function of an optimization problem across multiple subproblems with a consensus constraint enforced through dual variables and proximal penalties. Consider the optimization problem

where each $p_{i}:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}}$ is a convex term in the objective function, and $q:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}}$ encodes shared regularization or constraints. To apply consensus ADMM, the problem is reformulated using a splitting variable, resulting in

where $z_{i} \in {\mathbb{R}}^{n_{z}}$ for $i \in {\lbrack n_{a}\rbrack}$ is the state of agent $i$, and $\overline{z} \in {\mathbb{R}}^{n_{z}}$ is the global state. Now, each $p_{i}{(z_{i})}$ is a convex per-agent objective, and $q{(\overline{z})}$ represents shared regularization or constraints. The goal of consensus optimization is for each agent to eventually aggregate to a consensus such that all agents achieve the value of the global state, $z_{i} = \overline{z}$ for all $i \in {\lbrack n_{a}\rbrack}$. This is achieved through an iterative process, in which the individual agent updates are first solved in parallel over $i$, then a consensus update is performed, and finally a dual update is computed \[MAL-016\], expressed as

$z_{i}^{j + 1}$ ${= {{{\underset{z}{\arg\min}p_{i}}(z)} + {\frac{\rho}{2}\left\| {{z - {\overline{z}}^{j}} + \xi_{i}^{j}} \right\|_{2}^{2}}}},$ (3a)
${\overline{z}}^{j + 1}$ ${= {{{\underset{\overline{z}}{\arg\min}q}\left( \overline{z} \right)} + {\frac{\rho}{2}{\sum\limits_{i = 1}^{n_{a}}\left\| {{z_{i}^{j + 1} - \overline{z}} + \xi_{i}^{j}} \right\|_{2}^{2}}}}},$ (3b)

for $i \in {\lbrack n_{a}\rbrack}$. Here, the primal and dual variables are represented by $z_{i}$ and $\xi_{i} \in {\mathbb{R}}^{n_{z}}$, respectively, $j \in {\mathbb{Z}}_{+}$ is the iteration variable, and $\rho \in {\mathbb{R}}_{+}$ is the consensus penalty parameter.

### Proposition II.1

If each $p_{i}$ and $q$ are convex, closed, and proper, then the consensus residuals vanish, meaning that as $j\rightarrow\infty$, the primal residual

Moreover, the dual residuals vanish as $j\rightarrow\infty$ such that

### Proof

This result has been shown in \[MAL-016, Appx. A\]. ∎

Proposition II.1 implies that the shared consensus variable has stabilized. For nonconvex problems, ADMM is often observed to converge to a stationary point under certain assumptions, but global optimality is not guaranteed, see \[wang2019_nonconvexadmm\] for additional details.

### II-B Sequential Convex Programming

Consider the discrete-time dynamics

where $x_{k} \in {\mathbb{R}}^{n_{x}}$ is the state, $u_{k} \in {\mathbb{R}}^{n_{u}}$ is the control input, and $f_{k}:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{u}}}\rightarrow{\mathbb{R}}^{n_{x}}}$ are the discrete-time system dynamics between times $t_{k}$ and $t_{k} + {k\Deltat}$. We introduce the variable

where $z_{k} \in {\mathbb{R}}^{n_{z}} = {\mathbb{R}}^{n_{x} + n_{u}}$. Note that for ease of notation, we let $u_{K} = \mathbf{0}_{n_{u}}$. Moreover, we let $z = z_{0:K}$, where $z \in {\mathbb{R}}^{n_{z} \times K}$. The optimal control problem is

${{g{(z_{k})}} \leq 0},$ ${k \in {\lbrack K\rbrack}},$ (8c)
${z_{k} \in \mathcal{Z}_{k}^{c}},$ ${k \in {\lbrack K\rbrack}},$ (8e)

where $J_{k}:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}}$ is the running cost function, $J_{K}:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}}$ is the terminal cost function, $e^{x} \in {\mathbb{R}}^{n_{z}}$ is a row matrix that extracts $x$ from $z$, i.e. $e^{x} = \begin{bmatrix}
\mathbf{1}_{n_{x}}^{\top} & \mathbf{0}_{n_{u}}^{\top}
\end{bmatrix}$, $\mathcal{Z}_{k}^{c} \subseteq {\mathbb{R}}^{n_{z}}$ is the set of convex state and control constraints at time step $k$, $g:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}^{n_{g}}}$ are nonconvex inequality constraints, and $h:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}^{n_{h}}}$ are nonconvex equality constraints. We assume that ${J,f_{k},g,h} \in \mathcal{C}^{1}$ are closed, and nonconvex, and that $\mathcal{Z}_{k}^{c}$ for $k \in {\lbrack K\rbrack}$ is closed and convex. We note that this problem can be the discretized form of a continuous-time optimal control problem and can include path constraints, see \[Elango_ctcs\] for details.

We apply the prox-linear method \[drusvyatskiy_proxlin, szmuk_ptr, reynolds_ptr\] to solve. For a general function $\Xi:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}^{n_{\Xi}}}$, we denote the linearized function

where $\overline{z}$ is the state about which the function is linearized. We can formulate as an unconstrained minimization problem by penalizing the nonconvex constraints \[nocedalwright_2006\]. The convex constraints are enforced through an indicator function. At the ${({j + 1})}^{th}$ iteration, the nonconvex cost and constraints are linearized about the solution to the $j^{th}$ subproblem. We define the linear function

where ${w^{1},w^{2},w^{3}} \in {\mathbb{R}}_{+}$ are user-selected weights, and $\mathcal{Z}^{c} = {\bigcup_{k \in {\lbrack K\rbrack}}\mathcal{Z}_{k}^{c}}$. Note that if the running cost and terminal cost functions are convex, they need not be linearized, and ${\overset{\sim}{J}}_{K}{(z_{K}^{j},z_{K})}$ and ${\overset{\sim}{J}}_{k}{(z_{K}^{j},z_{K})}$ in are replaced by $J_{K}{(z_{K})}$ and $J_{k}{(z_{K})}$, respectively. Since the linearizations of the cost and constraints are only accurate in the neighborhood of the trajectory about which they are performed, deviation from that trajectory is penalized with a trust region, resulting in the function

where $w^{p} \in {\mathbb{R}}_{+}$ is a user-selected proximal weight. The SCP framework solves by successively solving the *convex subproblem*

Between SCP iterations, the trajectory about which the problem is linearized is updated with the solution of the previous iterate. This process is repeated until a convergence criterion is satisfied. Algorithm 1 outlines a multi-start version of the standard SCP algorithm, in which $n_{a}$ initial trajectories are used to initialize the algorithm.

while j ≤ jmax, ∥Θ (zij − 1,zij)∥ &gt; ϵc do
zij + 1 ← arg min zΓ (zij,z)
Algorithm 1 Multi-Start Standard SCP

## Exploratory SCP Algorithm

The solution found using standard SCP is a stationary point of in the neighborhood of the initial trajectory, $z^{0}$ \[Elango_ctcs, drusvyatskiy_proxlin\]. SCP solutions are therefore very sensitive to their initialization. In this section, we propose a method for exploring the nonconvex solution space of a problem using a modified SCP algorithm, referred to as OS-SCP.

### III-A Operator-Splitting SCP (OS-SCP)

The trust region term in promotes validity of the linearized model by penalizing deviation from the trajectory about which the problem was linearized. However, this impedes exploration of the nonconvex solution space and can prevent the algorithm from exiting a local minimum and finding a lower-cost solution. We therefore modify the conventional penalized linearization .

### III-A1 Primal update

We use $n_{a}$ virtual agents to explore the solution space of an optimal control problem through iterative solves of. The OS-SCP algorithm begins by solving (3a) with ${p_{i}{(z_{i})}} = {\Theta{(z_{i}^{j},z_{i})}}$ for each agent, which is analogous to a standard SCP iteration, given , with a modified penalty term. The subproblem can be expressed as

where $z_{i}$ is the trajectory of the $i^{th}$ agent, $z_{i}^{j}$ is the solution to the $j^{th}$ convex subproblem for the $i^{th}$ agent, and $\rho$ is the consensus penalty parameter. We define the penalized linearized cost as the objective in (12 ‣ III Exploratory SCP Algorithm ‣ A Sequential Operator-Splitting Framework for Exploration of Nonconvex Trajectory Optimization Solution Spaces")) so that

The modified penalty term penalizes deviation of the state of each agent from the consensus state, $\overline{z}$. This promotes the formation of a consensus among the agents.

### III-A2 Consensus update

We begin by defining the convexified constraint set

where $\mathcal{Z} \subseteq {\mathbb{R}}^{n_{z} \times K}$, and $\mathcal{Z}^{n} \subseteq {\mathbb{R}}^{n_{z} \times K}$ is the set of convexified nonconvex constraints, linearized about the mean trajectory, ${\hat{z}}^{j} = {\frac{1}{n_{a}}{\sum_{i = 1}^{n_{a}}{(z_{i}^{j})}}}$. The set of convexified nonconvex constraints is

We wish to obtain a consensus trajectory that is feasible with respect to the primal problem. We therefore define $q{(\overline{z})}$ in (3b) as the indicator function of the convex set $\mathcal{Z}$, resulting in

Equation (16 ‣ III Exploratory SCP Algorithm ‣ A Sequential Operator-Splitting Framework for Exploration of Nonconvex Trajectory Optimization Solution Spaces")) is solved by projecting the mean of the agent's trajectories onto the convexified constraint set, resulting in

where $\Pi_{\mathcal{Z}}{( \cdot )}$ denotes the Euclidean projection operator,

and $\xi_{i}^{j}$ is the dual variable for agent $i$ at the $j^{th}$ OS-SCP iteration.

### III-A3 Dual update

Finally, (3c) is solved to update the dual variables.

The algorithm is outlined in Algorithm 2 ‣ III Exploratory SCP Algorithm ‣ A Sequential Operator-Splitting Framework for Exploration of Nonconvex Trajectory Optimization Solution Spaces"). The agents begin with different initializations. The iterations outlined above are performed until the primal and dual variables converge below a specified tolerance.

while $\left( {{\left\| \delta_{r}^{j} \right\| &gt; \epsilon_{r}},{{\delta_{s}^{j} &gt; \epsilon_{s}},{{j \leq j^{\max}},{\left\| {\Theta{({\overline{z}}^{j - 1},{\overline{z}}^{j})}} \right\| &gt; \epsilon_{c}}}}} \right)$ do
$z_{i}^{j + 1}\leftarrow{{{\arg\min}_{z}\Gamma^{c}}{(z_{i}^{j},{\overline{z}}_{i}^{j},\xi_{i}^{j},z)}}$
${\overline{z}}^{j + 1}\leftarrow{\frac{\rho}{2}\Pi_{\mathcal{Z}}\left( {\frac{1}{n_{a}}{\sum_{i = 1}^{n_{a}}\left( {z_{i}^{j + 1} + \xi_{i}^{j}} \right)}} \right)}$
$\xi_{i}^{j + 1}\leftarrow{\xi_{i}^{j} + \left( {z_{i}^{j + 1} - {\overset{\sim}{z}}^{j + 1}} \right)}$
Algorithm 2 Operator-Splitting SCP

While we describe the method using consensus across all solution variables for ease of notation, the algorithm does not rely on this assumption. Consensus can be restricted to a subset of the state variables, which may be preferable when only certain portions of the state space pose challenges with local minima and consensus elsewhere is unnecessary.

## Numerical Results

We now demonstrate the performance of the exploration-focused operator-splitting SCP method against standard SCP in two illustrative examples: a simple obstacle avoidance example, and an obstacle avoidance example over a landscape with a non-uniform cost field.

### IV-A Unicycle Trajectory Optimization

Consider the discrete-time kinematic model for a unicycle with constant velocity

where the state is $x_{k} = {\lbrack r_{k}^{x}\quad r_{k}^{y}\quad\theta_{k}\rbrack}^{\top} \in {\mathbb{R}}^{3}$ and control $u_{k} \in {\mathbb{R}}$ is the yaw rate. The speed is defined as a constant $v > 0$, and the dynamics are discretized with the uniform time step $\Deltat$. We aim to find an optimal trajectory and nominal control to bring the vehicle from an initial state to a desired terminal state, while avoiding obstacles. The problem setup is shown in Figure 2.

Figure 2: Problem setup for simple obstacle avoidance example.

Let $x_{g}$ be the desired terminal state. We express the problem in the form of, where the convex terminal and running cost functions are

with $Q_{g} \succeq 0$. The nonconvex inequality constraints are

where $R_{\iota} \in {\mathbb{R}}_{+}$ is the radius of obstacle $\iota$ and $c_{\iota} \in {\mathbb{R}}^{2}$ is the center of obstacle $\iota$.

Following the prox-linear methodology, at iteration $j$, we formulate the nonconvex optimization problem as a convex unconstrained minimization problem by penalizing the constraints, and linearizing the cost and constraints about the solution to the ${({j - 1})}^{th}$ subproblem. We formulate the penalized cost as in with linearized cost . Note that since the terminal and running costs are convex, they need not be convexified, and ${\overset{\sim}{J}}_{K}{(z_{K}^{j},z_{K})}$ and ${\overset{\sim}{J}}_{k}{(z_{k}^{j},z_{k})}$ in are replaced by $J_{K}{(z_{K})}$ and $J_{k}{(z_{k})}$, respectively.

### IV-A1 SCP solution

We first solve this problem with the standard SCP method according to Algorithm 1 with three initial guesses. The first guess is an arc veering toward the left of the vehicle, the second is a straight line from initial state to the goal, and third is an arc veering toward the right of the vehicle. The initial guesses and the converged trajectories are shown in Figure 3, and the corresponding final costs and total iterations for each solve are shown in Table I. From Figure 3, it is evident that the SCP solution for each initialization converges to a solution in the neighborhood of the corresponding initial guess. This demonstrates the algorithm's difficulty in escaping the stationary point near its initialization. Additionally, Table I shows that only the solution with a straight initial guess converges to a minimum cost solution. This dependence on a good initial guess is a known limitation of SCP. In this visually intuitive example, a straight line guess might be an obvious choice. However, generating good (and especially dynamically feasible) initial guesses is generally not trivial. From this example, the need for an exploration focused, SCP-based algorithm is clearly evident.

Figure 3: Initial and converged trajectories computed using standard SCP algorithm.

TABLE I: SCP Results

### IV-A2 OS-SCP solution

We now solve the problem using the proposed OS-SCP method, summarized in Algorithm 2 ‣ III Exploratory SCP Algorithm ‣ A Sequential Operator-Splitting Framework for Exploration of Nonconvex Trajectory Optimization Solution Spaces"). At each iteration, each agent solves a convex subproblem. A consensus update is then performed, and finally a dual update is performed. This process repeats until the primal and dual residuals fall below specified tolerances $\epsilon_{r} \in {\mathbb{R}}_{+}$ and $\epsilon_{s} \in {\mathbb{R}}_{+}$, respectively. The same three initial guesses as before are used to initialize the three agents, where agent 1 is assigned the "upper" guess, agent 2 the "straight" guess, and agent 3 the "lower" guess. The converged solution is shown in Figure 4, and the evolution of the primal and dual residuals are shown in Figure 5. The residuals converge to zero over iterations, and OS-SCP successfully forms a consensus between all three agents. The consensus converges to the same trajectory as the lowest cost solution of the standard SCP example, demonstrating the ability for the OS-SCP method to pull agents out of the local minima near to their initialization. We compare the performance of both methods in Table II, where OS-SCP finds an equal cost trajectory in fewer iterations than standard SCP. Since at each iteration of OS-SCP, three convex subproblems are solved (one per agent), and three standard SCP problems are solved (one per initial guess), the run times of the methods are approximately equal.

Figure 4: Initial and converged trajectories computed using OS-SCP algorithm.

Figure 5: Primal and dual residuals over iterations for OS-SCP.

TABLE II: Numerical Comparison - Unicycle Trajectory

### IV-B Unicycle Trajectory Optimization with Gaussian Terrain Fields

The second problem extends the first example. Consider the same kinematic model and problem setup. However, we add spacial preference biases via a Gaussian terrain field. The cost map created by the terrain field is expressed as

where $\mu_{\ell} \in {\mathbb{R}}^{2}$ is the position of the center of the $\ell$-th Gaussian field, and $\Sigma_{\ell} \succeq 0$ controls the shape of the field and its amplitude. At the $j^{th}$ iteration, the cost map in is linearized about the solution to the ${({j - 1})}^{th}$ subproblem, $z^{j}$, and added to the linearized cost function . Then, SCP solves the same unconstrained convex subproblem as , but with updated $\Gamma{(z^{j},z)}$ to include the Gaussian terrain field cost.

The new problem setup is shown in Figure 6, where Gaussian cost fields are added between the upper and lower corridors of the obstacles. The terrain incentivizes traveling through the lower corridor by giving it negative cost, and penalizes the upper corridor with a higher cost terrain.

Figure 6: Problem setup for trajectory optimization problem with Gaussian terrain field.

### IV-B1 SCP Solution

As with the previous example, we first solve the problem with the standard SCP method outlined in Algorithm 1. We initialize three independent standard SCP solves with the same three initial guesses as from the first example. Figure 7 shows that each initialization results in a converged trajectory in the neighborhood of the initial guess. Notably, the "straight" guess gets trapped in a local minimum in the upper corridor. In order for this method to find a minimum cost solution, we need to add a new initial guess close to the global optimum which passes directly through the lower corridor. This solution is depicted in Figure 8. The only initialization to converge to the lowest cost trajectory is the one whose initial guess passes through the optimal region. This further demonstrates the sensitivity of the standard SCP algorithm to the initial guess. Again, for this visually intuitive example choosing an initial guess near the global optimum is possible. However, for systems in higher dimensions with more complex solution spaces, an initial guess close to the global optimum is generally difficult to generate.

### IV-B2 OS-SCP Solution

We then solve the problem with OS-SCP, where we use 3 agents with the same initial guesses as in the original example: "straight", "lower", and "upper". The agents explore the solution space before forming a consensus through the lower corridor, successfully finding the lowest cost solution, as shown in Figure 9, without the need for an initial guess that passes through the lower corridor. Table III compares the OS-SCP method against the lowest cost solution from standard SCP. The OS-SCP consensus converges to the same trajectory as the lowest cost solution from the standard SCP solves in near the same number of iterations, but does not have the same need for an initial guess near the global optimum. This example demonstrates the exploratory nature of the OS-SCP method and its lack of dependency on an accurate initial guess. Compared to the standard SCP approach, OS-SCP also provides the benefit of removing the human-in-the-loop requirement of selecting the best trajectory from a set of converged trajectories in the case of multiple unique trajectories with equivalent costs.

Figure 7: Initial and converged trajectories with Gaussian terrain field cost computed using standard SCP algorithm.

Figure 8: Initial and converged trajectories with Gaussian terrain field cost computed using standard SCP algorithm, including additional “lower corridor” guess.

Figure 9: Initial and converged trajectories with Gaussian terrain field cost computed using OS-SCP algorithm.

Standard SCP (3 guesses)

Standard SCP (4 guesses)

TABLE III: Numerical Results - Unicycle Trajectory with Gaussian Terrain Field

## Conclusion

This paper introduces the OS-SCP framework that promotes exploration in nonconvex trajectory optimization problems while preserving the feasibility and structure of standard SCP. Rather than solving a single locally convexified subproblem from one initialization, OS-SCP instantiates multiple agents with diverse initial guesses and couples them through a consensus ADMM update. This mechanism allows the population of agents to search not only the local minima about each initial guess, but also between local minima in the cost landscape. Results show that this can lead to OS-SCP finding lower-cost solutions than the standard SCP algorithm initialized with the same set of initial guesses.
