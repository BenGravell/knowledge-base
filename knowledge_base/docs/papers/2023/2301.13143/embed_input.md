<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RRT Guided Model Predictive Path Integral Method

Topics include Trajectory optimization, Model predictive path integral control, Rapidly-exploring random tree, Sampling-based planning, Model predictive control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Grows an RRT to produce a coarse initial plan, then uses that plan as the mean of the MPPI sampling distribution, combining the global exploration of RRT with the local refinement of MPPI.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work presents an optimal sampling-based method to solve the real-time motion planning problem in static and dynamic environments, exploiting the Rapid-exploring Random Trees (RRT) algorithm and the Model Predictive Path Integral (MPPI) algorithm. The RRT algorithm provides a nominal mean value of the random control distribution in the MPPI algorithm, resulting in satisfactory control performance in static and dynamic environments without a need for fine parameter tuning. We also discuss the importance of choosing the right mean of the MPPI algorithm, which balances exploration and optimality gap, given a fixed sample size. In particular, a sufficiently large mean is required to explore the state space enough, and a sufficiently small mean is required to guarantee that the samples reconstruct the optimal controls. The proposed methodology automates the procedure of choosing the right mean by incorporating the RRT algorithm. The simulations demonstrate that the proposed algorithm can solve the motion planning problem in real-time for static or dynamic environments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning problems have been widely discussed in recent years in the field of robotics, such as self-driving car navigation, automatic drone, and bipedal robots. The main goal of motion planning problems is to find a path for the agents to move from an initial position to a target position in fully-known environments while preventing collisions. However, it still remains challenging to solve the optimal motion planning problems efficiently in dynamic environments and implement the algorithms on the robotic systems in real-time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For motion planning problems, sampling-based methods have been proven to be effective for complex systems since the methods avoid calculating the derivatives of the dynamic equation and the cost function. In particular, the Probabilistic Roadmap (PRM) algorithm is the first sampling-based algorithm that solves the motion planning problem. The algorithm utilizes a local planner to connect the sampling configuration in free space. The Rapid-exploring Random Trees (RRT) algorithm, one of the most famous sampling-based algorithms, combines the exploration of the configuration space and the biased sampling around the goal configuration space. Most of the RRT algorithm variants can efficiently solve motion planning problems but can not find an optimal solution. The RRT\* algorithm has been developed in to find an optimal solution by using incremental rewirings of the graph to provide an asymptotically optimal solution to the motion planning problems. However, compared to the RRT algorithm, the RRT\* algorithm and its variants have a relatively longer execution time because the algorithm calculates the neighboring nodes and rewires the graph.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most RRT and RRT\* algorithms can not handle dynamic environments since it requires one to abandon the current result path, and the new path grows from scratch. Dynamic Rapidly-exploring Random Trees (DRRTs) algorithm was developed to address the problem by trimming the original results and exploring to get the target again. In, the authors provide a variant of replanning RRT algorithms combined with the Multipartite RRT (MP-RRT) algorithm. The MP-RRT algorithm biases the sampling distribution towards previous useful states and analytically computes which part of the previous RRT results can be re-utilized. Yet, both algorithms could not guarantee an optimal solution to the motion planning problem since the algorithms are based on non-optimal RRT algorithms. Thus, we provide a different approach to solving optimal real-time motion problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

One alternative way to efficiently solve optimal motion planning problems with dynamic environments is to use the Model Predictive Integral Control (MPPI) algorithm. By sampling the forward trajectories of dynamic systems, the MPPI algorithm avoids calculating the derivatives of the dynamic functions or the cost functions. Since the forward trajectories can be sampled efficiently by Graphic Processing Units (GPUs), the algorithm can be applied to diverse robotic systems with finishing the calculation in a fixed time. The MPPI algorithm enables real-time implementation by adjusting the fixed computation time, whereas a longer computation time reduces the optimality gap. Since the algorithm solves the motion planning problem iteratively, the algorithm can handle dynamic environments directly. However, the performance of the algorithm is influenced by the hyper-parameters dramatically, especially the mean value of the control input sample distribution. Intuitively, a small mean value may result in conservative exploration, and a large mean value may result in risky behaviors. Especially in dynamic environments, to get better performance, a time-varying mean value is needed. Thus, in this work, we utilize the RRT algorithm to design a better sample mean to guide the MPPI algorithm in exploring the workspace and sampling the trajectories.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The idea of using the RRT and RRT\* algorithms to solve motion planning problems in dynamic environments is inspired. In this work, the authors propose the RRT^X^ algorithm, which combines the replanning ideas provided in the DRRT algorithm and RRT\* algorithm to continuously update the path during the exploration when the environment changes. However, the algorithms require large computation power and are hard to implement on the robots in real-time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The idea of using a nominal or baseline controller to improve the performance of the MPPI algorithm is inspired. In, the authors present a method using the entire planning tree from RRT\* algorithm to approximate the value functions in the MPPI algorithm. However, due to the learning procedure in the algorithm, the cost of finding an optimal solution to the motion planning problem is computationally expensive. In, the authors control the variance of the MPPI algorithm to handle the dynamic environments and provide a faster running time and better collision avoidance in a ground unicycle simulation. However, the algorithm requires the linearized dynamic model, which results in expensive computation for complex or high-dimension systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution. This work presents a real-time sampling-based algorithm to solve the motion planning problem. We use the RRT algorithm to provide a nominal mean value for the random control distribution of the MPPI algorithm. The proposed algorithm advances the RRT algorithm in terms of dynamic environment navigation and optimality, and with respect to the MPPI algorithm, it reduces the need to fine-tune the mean value. We provide simulation results and sample size analysis to discuss the importance of tuning the mean value in the original MPPI algorithm. In particular, the sampling-based algorithms need sufficiently large means to explore the state space and sufficiently small means to guarantee that the samples reconstruct the optimal control. Thus, our proposed method avoids fine-tuning the mean value by using the nominal path provided by the RRT algorithms. Our algorithm finds the optimal solutions by allowing the MPPI algorithm to explore freely, and it has a better performance in running time by using the RRT algorithm to provide a nominal path to guide the MPPI algorithm. If the MPPI algorithm reaches the area where the nominal path provided by the RRT algorithm has not been explored before, our algorithm uses a real-time Replanning RRT algorithm to provide new nominal paths.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we implement our algorithm on a unicycle robot and solve the motion planning problem in static and dynamic environments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. Section II formulates the optimal motion planning problems. Section III proposes the RRT-MPPI algorithm to solve the motion planning problems provided in Section II. We show the necessity of an automated design procedure for an RRT-based MPPI algorithm by demonstrating that a large mean is desired for exploration purposes in Section III-B and by showing that a small mean is desired to reduce the optimality gap in Section IV, given fixed sample size. Section V provides simulations for a ground robot navigating through static and dynamic environments. We also compare the running time of the original MPPI algorithm and our RRT-based MPPI algorithm.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given $\mathcal{X},\mathcal{X}_{obs},x_{g}$, and ${x_{t}{}} = x_{s}$, we aim to find the optimal control input $u^{\ast}$ that would lead to the shortest path to state $x_{g}$ in the static or dynamic environments (i.e., time-varying $\mathcal{X}_{obs}$). Specifically, we aim to minimize the cost functions $S{(x_{t},u_{t})}$, defined as: subject to $x_{j} \in \mathcal{X}_{f}$, where $q{(x_{j},u_{j})}$ is a running cost function, and $\phi{(x_{t + T})}$ is the terminal cost function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Approach", "weight": 1.0} -->

To this end, we propose the RRT-guided MPPI algorithm in Section III-C, which addresses Problem 1. By generating mean values using the RRT (presented in Section III-A), the MPPI algorithm (presented in Section III-B) does not need fine parameter tuning in dynamic environments. Furthermore, the MPPI algorithm provides real-time implementable optimal control inputs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Approach", "weight": 1.0} -->

Given: Initial vertices 𝒮 ← {ss} Given: Initial edges ε ← ⌀ Algorithm 1 RRT algorithm

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Rapidly-Exploring Random Trees Algorithm", "weight": 1.0} -->

We present the RRT algorithm in Algorithm 1. The algorithm uses function SampleState to uniformly sample a new state $s_{sample}$ in the configuration space $\mathcal{X}$. Then, the algorithm finds the nearest vertex $s_{near}$ with function NearestNeighbor and projects the sample state $s_{sample}$ to the ball with radius $\gamma$ with function Steer. If the new edge between the $s_{near}$ and $s$ is free from collision, the projected state $s$ will be added to the vertex set, and the new edge $(s,s_{nearest})$ will be added to the vertex set. If the new vertex $s$ is within a radius $\gamma$ of the goal state $s_{goal}$, then the RRT reaches the target and returns the path $p$. Otherwise, the algorithm adds the new vertex and advances the exploration.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Rapidly-Exploring Random Trees Algorithm", "weight": 1.0} -->

The RRT algorithm focuses on fast iteration while not guaranteeing finding the optimal solution to the motion planning problem. RRT\* is the first variant of the RRT algorithm that could ensure asymptotic optimality. By allowing the new vertices to "rewire" graph edges within the local neighborhood, the algorithm guarantees asymptotic optimality with the cost of increasing running time. However, the computation time of the RRT\* algorithm also increases dramatically, and it is hard to implement the algorithm in real-time. In this work, instead of using the RRT\* algorithm, we utilize the MPPI algorithm to find the optimal solution to the motion planning problems.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Model Predictive Path Integral Control Algorithm", "weight": 1.0} -->

In this section, we introduce the MPPI algorithm to solve the motion planning problems. First, we need to sample $K$ trajectories with time horizon $T$ with random control input $u_{i,j} \sim {\mathcal{N}{(\mu,\Sigma)}}$, where $i = {1,\cdots,K}$ is the sample trajectory index. In each trajectory $\tau_{i}$, we denote $u_{i} = {\lbrack u_{i,t},\ldots,u_{i,{{t + T} - 1}}\rbrack}^{T}$ the actual control input sequence, and ${\lbrack x_{i,{t + 1}},\ldots,x_{i,{t + T}}\rbrack}^{T}$ the states of the current sample trajectory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Model Predictive Path Integral Control Algorithm", "weight": 1.0} -->

The evaluated cost for $i^{th}$ trajectory is given by where ${q{(x_{i,j},u_{i,j})}} = {{{({x_{g} - x_{i,j}})}^{T}{({x_{g} - x_{i,j}})}} + {\frac{1}{2}u_{i,j}^{T}Ru_{i,j}}}$, where $R$ is a positive definite control penalty matrix. We define the weight of $i^{th}$ trajectory $\omega_{i}$ as: where $\lambda$ is the parameter that decides how much we trust the better-performed trajectories. Then the MPPI algorithm updates the control input using the following equation for $j = {t,\cdots,{{t + T} - 1}}$, which approximates the optimal control inputs using sampled trajectories.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Model Predictive Path Integral Control Algorithm", "weight": 1.0} -->

In conclusion, the MPPI algorithm uses sample trajectories to find the optimal control input to solve the motion planning problem. Because the MPPI algorithm avoids calculating the derivatives of the nonlinear dynamic systems or the value functions, it can be implemented in real-time with the help of parallel computations on the GPUs, even for complex dynamic systems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Model Predictive Path Integral Control Algorithm", "weight": 1.0} -->

While the MPPI algorithm has clear merits mentioned in the previous paragraph, its performance is dramatically influenced by the mean of the control input distribution. In the unicycle simulations presented in figure 1, the MPPI algorithm may fail to solve the motion planning problems due to the bad choice of the mean value. In figure 1, the red path is the result when the mean value of the control input is $\mu = {\lbrack 1,0\rbrack}^{T}$, the yellow path is the result when the mean value is $\mu = {\lbrack 1,1\rbrack}^{T}$, and the green path is the result when the mean value is $\mu = {\lbrack 0,0\rbrack}^{T}$. We can find out easily that a smaller mean value hinders the exploration and cannot finish the path planning task in the provided horizon. A larger mean value may result in a safety violation. If the mean value is large, the MPPI algorithm is more aggressive and finishes the task faster. However, it also provides more risky control inputs and should require a larger sample size to get an optimal solution.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Model Predictive Path Integral Control Algorithm", "weight": 1.0} -->

We will show a required sample size analysis in Section IV.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Model Predictive Path Integral Control Algorithm", "weight": 1.0} -->

An example of MPPI trajectory in a dynamic environment is shown in Figure 2, where we increase the radius of circle obstacles by $2$ and $4$. The mean value for the MPPI is ${\lbrack 1,0\rbrack}^{T}$, which has a perfect performance in a static environment but fails the task, being stuck in between obstacles in dynamic environments, as the second figure shown in Figure 2. Thus, we can conclude that for a dynamic environment, the MPPI algorithm needs a time-varying mean value to obtain a fine performance. To automate the procedure of choosing dynamic mean values, we combine it with the RRT algorithm.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

We propose a new sampling-based method that utilizes the RRT algorithm to guide the MPPI algorithm to solve the optimal motion planning problem defined in Problem 1. Our algorithm performs well without tuning the mean value of the control distribution. Our algorithm also has a fast running speed, and thus it can be implemented in real-time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

First, we use the RRT algorithm to provide an offline nominal path $p_{n}$, which provides a possible solution to solve the motion planning problem. Although the RRT algorithm has a relatively fast iteration speed, the algorithm is still hard to implement in real-time, which will also be shown later in the simulations. So we first run the RRT algorithm offline, not in real-time. Since the RRT algorithm only provides the state information instead of the control information, we then use Lyapunov controllers or PD controllers to obtain a nominal control input $u_{n}$ in real-time. However, since the RRT algorithm cannot guarantee the optimal solution, we use the MPPI algorithm with nominal control input $u_{n}$ as the mean of the random control distribution to explore an optimal control input $u^{\ast}$ at each time step.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

As the difference between the nominal control input $u_{n}$ and the optimal control input $u^{\ast}$ becomes increasingly large, the optimal control input may lead the agents to reach the area where the path $p_{n}$ of the RRT algorithm never reached before. In this case, the nominal path may have a negative influence on the MPPI algorithm. To address this issue, we use the replanning idea first presented in the DRRT algorithm, where the agents replan under the changing environment. However, unlike the DRRT algorithm, our algorithm replans when the nominal controllers $u_{n}$ are no longer helpful. In our implementation, we use a distance $R$ to justify if the replanning is needed. We use a NearestNeighbor function to calculate the distance between the current state $x$ and its closest point $x_{n}$ in the nominal path, and if the distance is larger than $R$, our algorithm replans.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

The detail of the Replanning RRT algorithm is presented in algorithm 2. Our replanning RRT algorithm has a different input compared to the previous RRT algorithm, where the vertices set $\mathcal{S}$ is given by the previous nominal path $p_{n}$, and vertices set $\mathcal{S}'$ contains the start state $s_{s}$. Next, we sample the state $s_{sample}$ and find the nearest neighbor $s_{near}'$ and project the states $s$ same way as the RRT algorithm in Algorithm 1. However, we will also find the closest state $s_{near}$ to the vertices set $\mathcal{S}'$. Then we check if the new edges $(s_{near}',s)$ are in the collision-free space $\mathcal{X}_{f}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

Finally, we repeat the previous procedure until the distance between new vertex $s$ and target state $s_{g}$ or closest state on the nominal path $s_{near}$ is smaller than the radius $\gamma$ and return the new path $p$. Since our replanning algorithm uses the MPPI algorithm to give a penalty to the obstacles at each time step, we do not need to trim the previous result. As a result, the proposed algorithm is significantly faster than the original RRT algorithm and can be implemented on the robots in real-time.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

Algorithm 2 Replanning RRT algorithm With the new nominal path $\mathcal{S}'$, we then use the Lyapunov controllers or the PD controllers to get the new nominal control input $u_{n}'$. We can obtain a sampled trajectory $\tau_{i} = {\lbrack x_{i,t},\ldots,x_{i,{{t + T} - 1}}\rbrack}^{T}$ with the new distribution $\mathcal{N}{(u_{n}',\Sigma)}$, where $T$ is the time horizon of the MPPI algorithm and $\Sigma$ is the fixed variance. Then we calculate the cost of the $i^{th}$ sampled trajectory by using the quadratic cost function $S{(\cdot)}$ and using the following equation, we calculate the weight of each trajectory: Note that we need to find the minimum value of all trajectories to prevent the numerical instability of the algorithms.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

Finally, we use the normalized trajectory weights to calculate the control update law: for $j = {t,\cdots,{{t + T} - 1}}$, The proposed RRT-guided MPPI algorithm is summarized in Algorithm 3.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Replanning RRT Guided MPPI Algorithm", "weight": 1.0} -->

Given: Number of sample trajectories K and timesteps T; Given: Initial variance Σ0; Given: Cost function parameters ϕ, q, R, λ; while task is not completed do Use RRT algorithm to get initial path pn Find the nearest state s ∈ pn to the current state x; Use Replanning RRT algorithm to get new pn Find new nearest state s ∈ pn Get nominal control mean value un = L (s, x) Generate control variations ui, j ∼ 𝒩 (un, Σ0); Simulate discrete dynamic to obtain xi, j; Calculate cost function S(τi)+ = q(xi, j, ui, j); Calculate the terminal cost S(τi)+ = ϕ(xi, t + T) Get sample weights ωi; Update control input using ωi, j and ui, j; Algorithm 3 RRT-MPPI algorithm

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sample Size Analysis", "weight": 1.0} -->

In this section, we show that if the mean value of the MPPI increases, the required sample size also increases. On the other hand, a sufficiently large sample size is required to explore the free space, as shown in Section III-B. As a result, we emphasize the necessity of an automated design procedure for a time-varying mean value by the RRT algorithm.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sample Size Analysis", "weight": 1.0} -->

In the MPPI algorithm, the sample size significantly influences the performance and running time. We provide the analysis of the required sample size of the MPPI algorithm based on the error between optimal control input provided by the Hamilton-Jacobi-Bellman (HJB) equation and its sampling-based approximation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sample Size Analysis", "weight": 1.0} -->

The MPPI algorithm solves an optimal control problem with a quadratic control cost and a state-dependent cost. The corresponding value function $V{(x_{t})}$ is then defined as: where $q'$ is the continuous-time version of the cost-to-go in and $\Deltat$ is the sampling time. With the boundary condition ${V{(x_{T})}} = {\phi{(x_{T})}}$, the solution to the stochastic HJB equation for the system defined in and the value function defined in is given as follows: However, the Partial Differential Equations (PDEs) are hard to solve for the curse of dimensionality. Thus, the algorithm uses exponential transformation of the value function ${V{(x_{t})}} = {- {\lambda{\log{({\Phi{(x_{t})}})}}}}$ to make the HJB linear in $\Phi$. The linearity allows us to solve the problem with forward-sampling.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sample Size Analysis", "weight": 1.0} -->

The iterative control update law can be calculated as a ratio of the expectations (the detailed derivations, see): where ${S{(\tau)}} = {{\phi{(x_{T})}} + {\int_{t_{0}}^{T\Deltat}{q'{(x_{t},t)}{dt}}}}$, and $\tau$ is a random trajectory process. The continuous-time trajectories are sampled as a *discretized* system according to where $\delta_{t}$ is the time-varying vector of standard normal Gaussian random variables, and $\Deltat$ denotes the time step of the time-discretization, and we use Euler--Maruyama method.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sample Size Analysis", "weight": 1.0} -->

Then the discrete-time control update law to approximate the optimal control becomes where $\deltau_{i,j}$ can be considered as a random control input, and ${S{(\tau)}} = {{\phi{(x_{i,{t + T}})}} + {\sum_{j = t}^{{t + T} - 1}{q{(x_{i,j},{\deltau_{i,j}})}}}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sample Size Analysis", "weight": 1.0} -->

In conclusion, the MPPI algorithm uses Monte Carlo (MC) methods to approximate the optimal control solution with the sampling-based control input. Our previous works on the sampling complexity of the MPPI method use Hoeffding's inequality and Chebyshev's inequality to provide the required sample size given error bounds and risk probability. Compared to the previous work, we focus on the influence of the mean of the sampling control distribution instead of the variance and prove that a larger mean of the random control distribution requires a larger sample size. Note that, while we only discuss the case of one-dimensional control input ${\deltau_{j}} \sim {\mathcal{N}{(\mu,\Sigma)}}$ for notational simplicity, the result can be extended to high-dimensional control input straightforwardly.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We suppose that the running cost function $q{(x_{i,t},u_{i,t})}$ and terminal cost function $\phi{(x_{i,{t + T}})}$ are quadratic functions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assume that the error bound $\epsilon_{1}$ of Chebyshev's inequality is smaller than the expectation of $\omega$

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Unicycle Dynamics", "weight": 1.0} -->

We implement our algorithm on a two-dimensional unicycle dynamic system: where $x,y$ are the coordinates, $\theta$ is the heading angle, and $\phi$ is the steering angle. $v$ is the linear velocity control input, and $\omega$ is the angular velocity control input. $L = 0.5$ is the length of the wheelbase. $\delta = {\lbrack\delta^{v},\delta^{\omega}\rbrack} \sim {\mathcal{N}{(\overline{0},I)}}$ is the random control input perturbation. The time step for the discrete-time simulation is ${\Deltat} = {0.05s}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Simulation Setups", "weight": 1.0} -->

The maximum sample size in the RRT algorithm is set to $20000$, and the projection radius is set to $\gamma = 0.5$. We set the sample size for the MPPI algorithm to be $K = 10000$, the time horizon to be 20, and $\lambda = 1.0$. The cost function is defined as: where $x$ represents the current states, and $x_{g}$ represents the goal state. $\mathcal{X}_{obs}$ is the obstacle set over ${\mathbb{R}}^{2}$, and $\mathbb{1}$ is the indicator function. We test our algorithm in two different environments, a static environment, and a dynamic environment. In both simulations, the start states are $x_{s} = {\lbrack 2,3,0,0\rbrack}^{T}$, and the goal states are $x_{g} = {\lbrack 49,24,0,0\rbrack}^{T}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Simulation Setups", "weight": 1.0} -->

We use a Lyapunov controller to design the velocity control input and a Proportional controller to design the angular velocity control input: where $e_{d},e_{\theta}$ are the error between the desired target state and current states.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Results", "weight": 1.0} -->

We first test our algorithm in a fully known static environment with the replanning conditions $R = 6$. Figure 3(a) shows the result of a unicycle robot navigating through the obstacles. The black rectangles represent the boundary of the environments, the grey circles and rectangles denote the obstacles, the blue square denotes the start state $x_{s}$, and the blue cross denotes the goal state $x_{g}$. The blue line in the figures is the result of the replanning RRT path, and the orange line in the figures is the resulting control output from the RRT-MPPI algorithm. Next, we implement our algorithm in dynamic environments where the radius of the circle obstacles increases by $2$ and $4$. We plot the environment changes by plotting the circles with dot lines as their boundaries. Figure 3(b) and Figure 3(c) show that our algorithm can handle dynamic environments. Note that in dynamic environments, the nominal path provided by the RRT path may violate safety. But, since the MPPI algorithm can explore freely, our algorithm is still able to find the solution to the optimal motion planning problems.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Results", "weight": 1.0} -->

Besides, we want to implement the algorithm in real-time, so the RRT algorithm we adopt here is relatively inaccurate and can only guide the MPPI algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Results", "weight": 1.0} -->

We repeat the previous experiments for 10 times and change the value of the replanning condition from $R = 2$ to $R = 8$. In Figure 4, we plot the average time, the maximum and minimum running time of our algorithm, and the original MPPI algorithm with mean ${\lbrack 1,0\rbrack}^{T}$ in static and dynamic environments. The time of the offline RRT algorithm is in purple color. Note that even the offline RRT algorithm takes around 0.2 seconds, but it is still not fast enough to be implemented in real-time. The online RRT-MPPI algorithm for the static environment is in blue color, and the dynamic environment is in yellow color. We also compare the computation time with the MPPI algorithm with a fixed mean value ${\lbrack\mu_{v},\mu_{\omega}\rbrack}^{T} = {\lbrack 1,0\rbrack}^{T}$, which is the grey color in the Figures. As the radius decreases, the RRT-MPPI algorithm can provide a more accurate nominal controller.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Results", "weight": 1.0} -->

But the times of the replanning procedure increase as well, and as a result, the total time to complete the task becomes longer. We can see that when the radius $R = 6$, the algorithm takes the least time to finish the motion planning task. All experiments are done on a Macbook Air laptop with an M1 chip in real-time.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Results", "weight": 1.0} -->

To calculate the required sample size, we set the desired bound ${\epsilon_{1} = 0.02},{\epsilon_{2} = 0.1}$, and set the allowable risk of failure ${\rho_{1} = 0.05},{\rho_{2} = 0.1}$. We calculate the numbers of samples $K_{1}$ and $K_{2}$ based on the equations and at time ${{T \ast \Delta}t} = {{50 \ast 0.05}s} = {2.5s}$. Table I shows that the required sample size of our algorithm is smaller than the original MPPI algorithm with a fixed mean value of 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Results", "weight": 1.0} -->

MPPI with fixed mean 1 Table I: Required Sample Size for RRT-MPPI and MPPI algorithm.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents a real-time RRT-MPPI algorithm to solve the motion planning problem in different environments. The proposed algorithm advances the RRT algorithm in terms of dynamic environment navigation and optimality and reduces the need to fine-tune the mean value of the MPPI algorithm. In particular, we use the RRT algorithm to provide the suitable nominal control mean value for the random distribution in the MPPI algorithm, which helps us to avoid fine-tuning the mean value and balance the optimality and exploration. Finally, in the simulations, we use a unicycle robot to implement the algorithm in real-time in static and dynamic environments. We compare the running time and required sample size of our RRT-MPPI algorithm with the fixed value MPPI algorithm in the experiments, showing that our algorithm is faster and requires a smaller sample size.
