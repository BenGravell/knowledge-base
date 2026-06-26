<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CORL: A Continuous-state Offset-dynamics Reinforcement Learner

Topics include Reinforcement learning, Continuous state spaces, Offset dynamics, Sample complexity, Fitted value iteration, Robotic driving, Probably approximately correct learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces CORL for learning continuous-state MDPs whose dynamics switch among offset models, giving PAC-style sample-complexity bounds that include the cost of approximate planning. The paper is a bridge between theoretical RL and robotics because it learns a structured transition model, solves it with fitted value iteration, and demonstrates the representation on a robotic car over varying terrain.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Continuous state spaces and stochastic, switching dynamics characterize a number of rich, realworld domains, such as robot navigation across varying terrain. We describe a reinforcementlearning algorithm for learning in these domains and prove for certain environments the algorithm is probably approximately correct with a sample complexity that scales polynomially with the state-space dimension. Unfortunately, no optimal planning techniques exist in general for such problems; instead we use fitted value iteration to solve the learned MDP, and include the error due to approximate planning in our bounds. Finally, we report an experiment using a robotic car driving over varying terrain to demonstrate that these dynamics representations adequately capture real-world dynamics and that our algorithm can be used to efficiently solve such problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Reinforcement learning (RL) has had some impressive successes, such as model helicopter flying and expert software backgammon players. Two key challenges in reinforcement learning are scaling to large worlds, which often involves a form of generalization, and efficiently handling the exploration/exploitation tradeoff. Many real-life problems involve real-valued state variables: discretizing such environments causes an exponential growth in the number of states as the state dimensionality increases, and so solutions that directly reason with continuous-states are of important consideration.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we build on recent work on probably efficient reinforcement learning and focus on continuous-state, discrete-action environments. We consider the case when the dynamics can be described as Michael L. Littman † Nicholas Roy ∗ † Department of Computer Science Rutgers University Piscataway, NJ 08854 switching noisy offsets where the parameters of the dynamics depend on the state's 'type' t and the action taken a. More formally, where s is the current state, s ′ is the next state, ε at ∼ N (0, Σ at) is drawn from a zero-mean Gaussian with covariance Σ at and β at is the offset.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An example where we expect such dynamics to arise is during autonomous traversal of varying terrain. Here, types represent the ground surface, such as dirt or rocks. The dynamics of the car may be approximated by an offset from the prior state plus some noise, where the offset and noise depend on the surface underneath the car. These models could be useful approximations in a number of other problems, including transportation planning (learning the mean speed and variance of interstate highways and local streets for path planning to a goal location), and packet routing (learning that wireless and ethernet have different bandwidth/usage patterns and routing accordingly).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We present a new RL algorithm for learning in continuousstate, discrete-action Markov decision processes (MDPs) with switching noisy offset dynamics and show that this algorithm is probably approximately correct (PAC) in certain environments with a sample complexity that scales polynomially with the state space dimensionality. We perform planning using fitted value iteration (FVI) and incorporate the error due to approximate planning into our bounds.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Finally, we present experiments on a small robot task that involves navigation over varying terrains. These experiments demonstrate that our dynamics models can adequately capture real-life dynamics and our algorithm can quickly learn good policies in such environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "CONTINUOUS-STATE OFFSET-DYNAMICS REINFORCEMENT LEARNER", "weight": 1.0} -->

This section introduces terminology and then presents our algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "ALGORITHM", "weight": 1.0} -->

Our algorithm (c.f., Algorithm 1) is derived from the Rmax algorithm of Brafman and Tennenholtz. We first form a set of 〈 t, a 〉 tuples, one for each type-action pair. Note that each tuple corresponds to a particular pair of dynamics model parameters, 〈 β, Σ at 〉. A tuple is considered to be 'known' if the agent has been in type t and 1 For simplicity, the reward is assumed to be only a function of state in this paper, but the arguments can be easily extended to where the reward model is also a function of the action chosen.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Algorithm 1 CORL", "weight": 1.0} -->

- 1: Input: N A, N dim, N T, R, Σ max, Σ min, γ, ϵ, and δ. - 2: Set all type-action tuples 〈 t, a 〉 to be unknown and initialize the dynamics models (see text) to create an empirical known-state MDP model ˆ M K. - 3: Select a fixed set of evenly spaced points for fitted value iteration. - 6: Solve MDP ˆ M K using fitted value iteration and denote its optimal value function by Q t. - 7: Select action a = argmax a Q t (s, a). - 8: Transition to the next state s ′. - 9: Increment the appropriate n at count (where t is the type of state s) given the observed transition tuple 〈 s, a, s ′ 〉. - 10: If n at exceeds N at where N at is specified according to the analysis, then mark 〈 a, t 〉 as 'known' and estimate the dynamics model parameters for this tuple.

<!-- chunk {"id": "body-0012", "role": "body", "section": "end loop", "weight": 1.0} -->

taken action a a number N at times. At each timestep, we construct a new MDP ˆ M K as follows. If the number of times a tuple has been experienced, n, is greater than or equal to N, then we estimate the parameters for this dynamics model using maximum-likelihood estimation: where the sum ranges over all state action pairs experienced for which the type of s i was t and the action taken was a.

<!-- chunk {"id": "body-0013", "role": "body", "section": "end loop", "weight": 1.0} -->

Otherwise, we set the dynamics model for all states and action associated with this type-action tuple to be a transition with probability 1 back to the same state. We also modify the reward function for all states associated with an unknown type-action tuple 〈 t u, a u 〉 so that all state-action values Q ( s t u, a u ) have a reward of V max (the maximum value possible, 1 / (1 -γ ) ). We then seek to solve ˆ M K. This MDP includes switching dynamics with continuous states, and we are aware of no exact optimal planners for such MDPs 2. Instead, we will use fitted value iteration to approximately solve the MDP.

<!-- chunk {"id": "body-0014", "role": "body", "section": "end loop", "weight": 1.0} -->

In FVI, the value function is represented explicitly at only a fixed set of states that are (for example) uniformly spaced in a grid over the state space. Planning requires performing Bellman backups for each grid point µ f. Since we are only performing backups of the value function at a set of grid points µ f, we need a function approximator to estimate the value of other points that are not in this fixed set. We can use Gaussian kernel functions to interpolate the value at the grid points to other points. The value of a state s is 2 In contrast, optimal control is possible for linear Gaussian (non-switching) dynamics continuous-state systems with linear quadratic reward functions. where w f is a scalar and N (s; µ f, Σ f) represents a Gaussian with mean at grid point µ f and variance Σ f evaluated at state s. The grid-point locations, variances and weights (µ f, Σ f, w f) are defined so for all states s of interest.

<!-- chunk {"id": "body-0015", "role": "body", "section": "end loop", "weight": 1.0} -->

We would like this expression to exactly equal 1 for all states of interest as that guarantees the function approximator is an averager and therefore discounted infinite horizon fitted value iteration is guaranteed to converge. In practice, if Gaussians are placed at uniform intervals over the state space of interest, then this expression can be extremely close to 1. Indeed, as long as the sum in Equation 6 sums to less than or equal to 1 for all states, then the approximator operator is guaranteed to be a non-expansion in the max norm and therefore discounted infinite horizon fitted value iteration is still guaranteed to converge.

<!-- chunk {"id": "body-0016", "role": "body", "section": "end loop", "weight": 1.0} -->

Substituting this representation of the value function in place of V (s ′) and using the dynamics model in the Bellman backup equation, we can perform the integration over future reward in closed form to get For a given basis set of fixed states µ f, the majority of the right side can be computed once and used repeatedly during value iteration; essentially, the continuous-state MDP is converted to a new discrete-state MDP where the states are the fixed points.

<!-- chunk {"id": "body-0017", "role": "body", "section": "end loop", "weight": 1.0} -->

At each timestep, the agent chooses the action that maximizes the estimate of its current value according to Q t: a = argmax a Q t ( s, a ). The complete algorithm is shown in Algorithm 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

In Section 4, we will analyze our algorithm in a family of MDPs with switching noisy offsets, and examine how many samples N at are necessary in order to produce a good policy. In particular, we prove it is probably approximately correct with a sample complexity ( N at ) that scales polynomially with the number of dimensions in the state space.

<!-- chunk {"id": "body-0019", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

When analyzing the performance of an RL algorithm A, there are many potential criteria to use. In our work, we will focus predominantly on sample complexity with a brief mention of computational complexity. Computational complexity refers to the number of operations executed by the algorithm for each step taken by the agent in the environment. We will follow Kakade and use sample complexity as shorthand for the sample complexity of learning. It is the number of timesteps at which the algorithm, when viewed as a non-stationary policy π, is not ϵ -optimal at the current state; that is, Q ∗ ( s, a ) -Q π ( s, a ) > ϵ where Q ∗ is the optimal state-action value function and Q π is the state-action value function of the non-stationary policy π. Following Strehl et al., we are interested in showing, for a given ϵ and δ, that with probability at least 1 -δ the sample complexity of the algorithm is less than or equal to a polynomial function of MDP parameters. Note that we only consider the number of samples to ensure the algorithm will learn and execute a near-optimal policy with high probability.

<!-- chunk {"id": "body-0020", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

As the agent acts in the world, it may be unlucky and experience a series of state transitions that poorly reflect the true dynamics, due to noise.

<!-- chunk {"id": "body-0021", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

We will follow the lead of a recent and related continuousstate reinforcement-learning algorithm by Strehl and Littman, and use the framework of Strehl et al.. Strehl et al. defined an algorithm to be greedy if it chooses its action to be the one that maximizes the value of the current state s (a = argmax a ∈ A Q (s, a)). Their paper's main result goes as follows: let A (ϵ, δ) denote a greedy learning algorithm. Maintain a list K of 'known' state-action pairs. At each new timestep, this list stays the same unless during that timestep a new stateaction pair becomes known. MDP M K is the known stateaction MDP (where the construction is essentially the same as described earlier, except that the reward and transition functions are the same as the original MDP for known state-action pairs) and π is the greedy policy with respect to the current value function, Q t.

<!-- chunk {"id": "body-0022", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

Assume that ϵ and δ are given and the following 3 conditions hold for all states, actions and timesteps: 3. The total number of times the agent visits a stateaction tuple that is not in K is bounded by ζ (ϵ, δ) (the learning complexity).

<!-- chunk {"id": "body-0023", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

Then, Strehl et al. show on any MDP M, A ( ϵ, δ ) will follow a 4 ϵ -optimal policy from its initial state on all but N total timesteps with probability at least 1 -2 δ, where N total is a polynomial in the problem's parameters ( ζ ( ϵ, δ ), 1 ϵ, 1 δ, 1 1 -γ ).

<!-- chunk {"id": "body-0024", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

The majority of our analysis will focus on showing that our algorithm fulfills these three criteria. In our approach, we will define the known state-action pairs to be all those state-actions for which the type-action pair 〈 t ( s ), a 〉 is known.

<!-- chunk {"id": "body-0025", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

Before we commence, we first briefly give some intuition for the above three criteria and describe how we will proceed in proving our algorithm satisfies them. Together, the first and second criteria can be interpreted as saying that the algorithm should produce accurate value estimates of the all state-action pairs in the known MDP, and that it should be optimistic about the values of all state-action pairs. The first criterion is more challenging to demonstrate. To show our estimates of known state-action pairs are close to their real values, we must consider two potential sources of error that could prevent it. The first is that the model dynamics are only estimated from the samples experienced, and so the dynamics model estimates may deviate from the true dynamics. In Proposition 4.1 and Lemmas 4.2, 4.3, and 4.4, we bound the number of samples necessary to ensure the dynamics model parameter estimates are close to the true dynamics. The second source of error comes from solving the MDP. We cannot currently perform exact optimal planning for these continuous-state noisy offset MDPs, and therefore we use approximate planning. In Section 4.2, we bound the error it introduces.

<!-- chunk {"id": "body-0026", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

We then combine these results in Lemma 4.5 to bound the error between our estimate of the value of the known-state MDP and the true optimal values. Theorem 4.6 uses this result to prove the algorithm is probably approximately correct with a sample complexity that scales polynomially in the problem parameters, including the state-space dimension.

<!-- chunk {"id": "body-0027", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

Note that our use of an approximate planner is a departure from most related work on PAC RL. Existing work typically assumes the existence of a planning oracle for choosing actions given the estimated model.

<!-- chunk {"id": "body-0028", "role": "body", "section": "LEARNING COMPLEXITY", "weight": 1.0} -->

To ensure fitted value iteration produces highly accurate results, our algorithm's worst-case computational complexity is exponential in the number of state dimensions. While this fact prevents it from being theoretically computationally efficient, our experimental results demonstrate our algorithm performs well compared to related approaches in a real-life robot problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

This section provides a formal analysis of Algorithm 1. For simplicity, it assumes a diagonal covariance matrix for the noise model: Σ = diag( σ 2 1, σ 2 2, · · ·, σ 2 N dim ). We believe it is possible to extend the analysis to the general covariance matrices, and leave it for future work. We also assume that the absolute values of the components in β at and Σ at are upper bounded by some known constants, B β and B σ, respectively. This assumption is often true in practice. We denote by | D | the determinant of matrix D. Due to space limitations some details will be omited in our analy- sis: please see Brunskill et al. for full proofs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "MODEL ACCURACY", "weight": 1.0} -->

We first establish the distance between two dynamics models with different parameters. It will be important for analyzing the potential difference in expected received reward between a MDP with the true dynamics model and an estimated (from the data) dynamics model. Following Abbeel and Ng, we use the variational distance Proposition 4.1 Assume that both Σ 1 and Σ 2 are diagonal matrices and let σ min be the minimum standard deviation along any of the dimensions. Also, assume without loss of generality that | Σ 1 | ≤ | Σ 2 |. Then, where σ 2 ki is the i -th diagonal component of Σ k.

<!-- chunk {"id": "body-0031", "role": "body", "section": "PLANNING ERROR", "weight": 1.0} -->

We next bound the error between the value function found by solving our particular continuous-state Markov decision process using fitted value iteration compared to the optimal value function V ∗. Recall that by performing FVI, we are essentially mapping the original MDP to a new finite-state MDP where the states are the chosen fixed points.

<!-- chunk {"id": "body-0032", "role": "body", "section": "PLANNING ERROR", "weight": 1.0} -->

Under a set of four assumptions, Chow and Tsitsiklis proved that the optimal value function V ε of a discrete-state MDP formed by discretizing a continuousstate MDP into O(ε)-length (per dimension) 4 grid cells is an ε -close approximation of the optimal continuous-state MDP value function V ∗: The first two assumptions used to prove the above result are that the reward function and probability distribution are Lipschitz-continuous. In our work, the reward function is assumed to be given so this condition is a prior condition on the problem specification. Our probability distributions are Gaussian distributions that are Lipschitzcontinuous so the second condition holds. The third key assumption is that the dynamics probabilities represent a true probablity measure that sums to 1 (∫ ′ s p (s ′ | s, a) = 1), though the authors show that this assumption can be relaxed to ∫ ′ s p (s ′ | s, a) ≤ 1 and the main results still hold. In our work, our dynamics models are defined to be true probability models.

<!-- chunk {"id": "body-0033", "role": "body", "section": "PLANNING ERROR", "weight": 1.0} -->

Chow and Tsitsiklis's final assumption is that there is a bounded difference between any two controls: in our case we consider only finite controls, so this property holds directly.

<!-- chunk {"id": "body-0034", "role": "body", "section": "PLANNING ERROR", "weight": 1.0} -->

In summary, assuming the reward model fulfills the first assumption, our framework satisfies all four assumptions made by Chow and Tsitsiklis. Therefore, by selecting fixed grid points at a regular spacing of O( ϵ FVI ) in each dimension (letting ε = ϵ FVI ), we can ensure that || ˜ V FVI -V ∗ || ∞ is at most ϵ FVI where ˜ V FVI is the FVI optimal value function.

<!-- chunk {"id": "body-0035", "role": "body", "section": "PLANNING ERROR", "weight": 1.0} -->

4 More specifically, the grid spacing h g must satisfy h g ≤ (1 -γ ) 2 ε K 1 +2 KK 2 and h g ≤ 1 2 K where K is the larger of the Lipschitz constants arising from the assumptions discussed in the text, and K 1 and K 2 are constants discussed in Chow and Tsitsiklis. For small ε any h g satisfying the first condition will automatically satisfy the second condition.

<!-- chunk {"id": "body-0036", "role": "body", "section": "APPROXIMATE REINFORCEMENT LEARNING", "weight": 1.0} -->

The next lemma relates the accuracy in the dynamics model parameters, and the error induced by approximate planning, to the value function of two MDPs. The proof strongly parallels a similar Simulation Lemma in recent work by Strehl and Littman.

<!-- chunk {"id": "body-0037", "role": "body", "section": "APPROXIMATE REINFORCEMENT LEARNING", "weight": 1.0} -->

Lemma 4.5 Let M 1 = 〈 S, A, p 1 ( s ′ | s, a ), R, γ 〉 and M 2 = 〈 S, A, p 2 ( s ′ | s, a ), R, γ 〉 be two MDPs 5 with dynamics as characterized in Equation 1 and non-negative rewards bounded above by 1. Assume || β 1 -β 2 || 2 √ 2 πσ min ≤ F 1 and | 1 -| Σ 1 | 0. 5 | Σ 2 | 0.

<!-- chunk {"id": "body-0038", "role": "body", "section": "APPROXIMATE REINFORCEMENT LEARNING", "weight": 1.0} -->

5 | ≤ F 2. Also assume that the difference between the value function ˜ V obtained by fitted value iteration (FVI) compared to the optimal value function V ∗, || ˜ V -V ∗ || ∞ is at most F 3. Let π be a policy that can be applied to both M 1 and M 2. Then, for any 0 < ϵ ≤ V max and stationary policy π, if F 1 = O ( (1 -γ ) 2 ϵ γ ) F 2 = O ( ϵ (1 -γ ) 2 γ ), and F 3 = O ( ϵ (1 -γ ) γ ), then for all states s and actions a, | Q π 1 ( s, a ) -˜ Q π 2 ( s, a ) | ≤ ϵ, where ˜ Q π 2 denotes the stateaction value obtained by performing FVI on MDP M 2 and Q π 1 denotes the true state-action value for MDP M 1 for policy π.

<!-- chunk {"id": "body-0039", "role": "body", "section": "APPROXIMATE REINFORCEMENT LEARNING", "weight": 1.0} -->

Proof: (Sketch) We analyze the norm between Q π 1 ( s, a ) and ˜ Q π 2 ( s, a ) by re-expressing each in terms of its respective Bellman operator. The main idea is to break the norm up into a difference between the values due to the different dynamics ( p 1 ( s ′ | s, a ) and p 2 ( s ′ | s, a ) ) and a difference due to using fitted value iteration to approximately solve for the values versus an exact solution. We use the triangle inequality to separate these terms and then bound each term separately, using the results from the prior sections.

<!-- chunk {"id": "body-0040", "role": "body", "section": "APPROXIMATELY OPTIMAL REINFORCEMENT LEARNING", "weight": 1.0} -->

Theorem 4.6 For any given δ and ϵ in a continuous-state noisy offset dynamics MDP with N T types where the variance along each dimension of all the dynamics models is bounded by [ σ 2 min, B 2 σ ] and the offset parameter is bounded by | β i | < B β on all but N total timesteps, our algorithm will follow a 4 ϵ -optimal policy from its current state with probability at least 1 -2 δ, where N total is polynomial in the problem parameters ( N dim, | A |, N T, 1 ϵ, 1 δ, 1 1 -γ, 1 σ min, B β, B σ ).

<!-- chunk {"id": "body-0041", "role": "body", "section": "APPROXIMATELY OPTIMAL REINFORCEMENT LEARNING", "weight": 1.0} -->

Proof: We demonstrate that our algorithm fulfills the three criteria outlined earlier. We omit details due to space considerations, but it can be shown using the results of the prior sections that after N at = O ( N 3 dim B 4 γ 2 σ 4 min (1 -γ ) 4 ϵ 2 ) samples, with probability 1 -δ, the errors ‖ β 1 -β 2 ‖ 2, and for each state dimension i, | σ 2 i -˜ σ 2 i | will be O ((1 -γ ) 2 ϵ ). We also chose the spacing of our fixed grid points such that ϵ FVI γ 1 -γ ≤ ϵ 2. Then, the Simulation Lemma (4.5) guarantees that the approximate value of our known state MDP solved using FVI is ϵ -close to the optimal value of the known state MDP with the true dynamics parameters || ˜ V π ˜ K -V π K || ∞ ≤ ϵ. All unknown type-action pairs that have not yet been experienced N M times are considered to be unknown and their value is set to V max. So, Conditions and hold. The third condition limits the number of times the algorithm may experience an unknown type-action tuple.

<!-- chunk {"id": "body-0042", "role": "body", "section": "APPROXIMATELY OPTIMAL REINFORCEMENT LEARNING", "weight": 1.0} -->

Since there are a finite number of types and actions, this quantity is bounded above by N at N T | A |, which is a polynomial in the problem parameters ( N dim, | A |, N T, 1 ϵ, 1 δ, 1 1 -γ, 1 σ min, B β, B σ ). Therefore, our algorithm fulfills the three criteria laid out and the result follows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "APPROXIMATELY OPTIMAL REINFORCEMENT LEARNING", "weight": 1.0} -->

5 For simplicity we present the results here without reference to types. In practice, each dynamics parameter would be subscripted by its associated MDP, type, and action.

<!-- chunk {"id": "body-0044", "role": "body", "section": "EXPERIMENT", "weight": 1.0} -->

To examine the performance of our algorithm, we performed experiments in a real-life robotic environment involving a navigation task where a robotic car must traverse multiple surface types to reach a goal location. Our experiments seek to demonstrate both that our dynamics models provide a sufficiently good representation of realworld dynamics to allow our algorithm to learn good policies, and that our algorithm is computationally tenable. We demonstrate the second quality by comparing to Leffler et al. 's RAM-Rmax algorithm, a provably efficient RL algorithm for learning in discrete-state worlds with types. The authors demonstrated that, by explicitly representing the types, they could get a significant learning speedup compared to Rmax, which learns a separate dynamics model for each state. The RAM-Rmax algorithm represents the dynamics model using a list of possible next outcomes for a given type. Our approach instead assumes a fixed parametric distribution that automatically constrains the size of the representation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

For our experiment, we ran a LEGO R © Mindstorms NXT robot on a multi-surface environment. A tracking pattern was placed on the top of the robot and an overhead camera was used to determine the robot's current position and orientation. The domain, shown in Figure 2, consisted of two types: rocks embedded in wax and a carpeted area. The goal was for the agent to begin in the start location (indicated in the figure by an arrow) and end in the goal without going outside the environmental boundaries. The rewards were -1 for going out of bounds, +1 for reaching the goal, and -0. 01 for taking an action. Reaching the goal and go- ing out of bounds ended the episode and resulted in the agent getting moved back to the start location.

<!-- chunk {"id": "body-0046", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

One difficulty of this environment is the difference in dynamics models. Due to the close proximity of the goal to the boundary, the agent needs an accurate dynamics model to reliably reach the goal. To make this task even more difficult, the actions were limited to going forward, turning left, and turning right. Without the ability to move backwards, the robot needed to approach the goal accurately to avoid falling out of bounds. A robot with an inaccurate transition model would be likely to judge this task as impossible.

<!-- chunk {"id": "body-0047", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

For the experiments, we compared our algorithm ('CORL') and the RAM-Rmax algorithm ('RAM'). The fixed points for the fitted value iteration portion of our algorithm were set to the discretized points of the RAM-Rmax algorithm. Both algorithms used an EDISON image segmentation system to uniquely identify the current surface type. The reward function was provided to both algorithms.

<!-- chunk {"id": "body-0048", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

The state space is three dimensional: x, y, and orientation. Our algorithm implementation for this domain used a full covariance matrix to model the dynamic's variance model. For the RAM-Rmax agent, the world was discretized to a forty-by-thirty-by-ten state space. In our algorithm, we used a function approximator of a weighted sum of Gaussians, as described in Section 2.2. We used the same number of Gaussians to represent the value function as the size of the state space used in the discretized algorithm, and placed these fixed Gaussians at the same locations. The variance over the x and y variables was independent of each other and of orientation, and was set to be 16. To average orientation vectors correctly (so that -180 ◦ degrees and 180 ◦ do not average to 0 ) we converted orientations θ to a Cartesian coordinate representa- tion x θ = cos( θ ), y θ = sin( θ ). The variance over these two was set to be 9 for each variable (with zero covariance).

<!-- chunk {"id": "body-0049", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

For our algorithm and the RAM-Rmax algorithm, the value of N at was set to four and five, respectively, which was determined after informal experimentation. The discount factor was set to 1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "RESULTS", "weight": 1.0} -->

Examining the learned dynamics model parameters revealed that the dynamics model variances learned for the rocks were larger than the learned variance for carpet for certain actions. Naturally, an important question is whether modeling the differences in the dynamics models is necessary in order to achieve good performance: in other words, could the robot perform as well by modeling the terrain as a single type? Prior work by RAM-Rmax on a similar task compared using two types to one, and found that two types did result in a better learned policy. This finding suggests that using multiple types to represent this environment provides measurable benefits.

<!-- chunk {"id": "body-0051", "role": "body", "section": "RESULTS", "weight": 1.0} -->

In addition, by using a fixed parametric representation, the computational time per episode of our algorithm is roughly constant. In the implementation of RAM-Rmax, the computational time grew with the number of episodes due to its dynamics model representation: however, this difficulty could be ameliorated by maintaining a finite list of potential dynamics transitions. Nonetheless, these results suggest that our algorithm is computationally competitive with existing approaches to handle domains with typed dynamics.

<!-- chunk {"id": "body-0052", "role": "body", "section": "RESULTS", "weight": 1.0} -->

In summary, the results on this task are encouraging since they indicate our algorithm can quickly and efficiently learn a good policy in a real-world environment with switching noisy offset dynamics.

<!-- chunk {"id": "body-0053", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have presented a new reinforcement-learning algorithm for handling continuous-state typed worlds where the dynamics can be modeled as a noisy offset. In this work, we have assumed that the state types are fully observable. This assumption is likely to be realistic for certain domains, such as when types correspond to the slope of an outdoor environment in which contour maps are available. In other cases, it might be useful to model the type as a hidden variable, and receive estimates of it through the agent's sensors. Such a scenario is beyond the scope of this paper but would be interesting future work.

<!-- chunk {"id": "body-0054", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In conclusion, we proved that when the noise covariance matrix is diagonal, the algorithm is probably approximately correct with a sample complexity that scales polynomially with the MDP parameters, including the state-space dimension. We also demonstrated that in some scenarios these dynamics representations can provide a sufficiently good approximation of real-world dynamics to enable a good policy to be learned by demonstrating the success of our algorithm in a small robotic experiment.
