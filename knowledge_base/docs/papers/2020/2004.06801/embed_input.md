<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scalable Autonomous Vehicle Safety Validation through Dynamic Programming and Scene Decomposition

Topics include Autonomous driving, Vehicles, Safety, Scalability, Dynamic programming.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An open question in autonomous driving is how best to use simulation to validate the safety of autonomous vehicles. Existing techniques rely on simulated rollouts, which can be inefficient for finding rare failure events, while other techniques are designed to only discover a single failure. In this work, we present a new safety validation approach that attempts to estimate the distribution over failures of an autonomous policy using approximate dynamic programming. Knowledge of this distribution allows for the efficient discovery of many failure examples. To address the problem of scalability, we decompose complex driving scenarios into subproblems consisting of only the ego vehicle and one other vehicle. These subproblems can be solved with approximate dynamic programming and their solutions are recombined to approximate the solution to the full scenario. We apply our approach to a simple two-vehicle scenario to demonstrate the technique as well as a more complex five-vehicle scenario to demonstrate scalability. In both experiments, we observed an increase in the number of failures discovered compared to baseline approaches.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

One common practice for automated vehicle (AV) safety validation is to maintain a suite of challenging driving scenarios that the vehicle must successfully navigate after each update to the driving policy. Although useful, this approach will miss any failures that are not already included in the test suite. Automated testing procedures that treat the vehicle as a black box must be developed to catch unknown and unexpected failure modes of the AV which could dramatically decrease testing time and improve the safety of autonomous vehicles.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Much of the literature on black box testing focuses on falsification where inputs are generated that cause a system to violate a safety specification. Those inputs serve as a counter example to the hypothesis that the system is safe. For autonomous driving, it is not feasible to create an agent that can avoid all possible accidents, so rather than find any failure of an AV, it is preferable to find the most likely failures. Traditional falsification techniques do not consider the probability of the failures they find and are therefore ill-suited to this goal. Adaptive stress testing tries to find the most-likely failure of an autonomous system. This approach can improve the likelihood of discovered failures but does not necessarily explore the range of possible failures of the system. The goal of this work is to develop a safety validation approach that can reliably find all of the most relevant failures of an autonomous vehicle.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our approach attempts to estimate the distribution over failures of an autonomous vehicle operating in a stochastic environment. If we assume that the vehicle's policy and simulator are Markov then we show that the problem simplifies to estimating the probability of failure at each state, a computation which can be performed using approximate dynamic programming (DP). Approximate DP is particularly effective at finding failures because it can start at a failure and work backward to see what led to it. Unfortunately, this approach has difficulty scaling to large state spaces. To improve scalability, we use the structure of driving scenarios by decomposing the simulation into pairwise interactions between the ego vehicle and other agents on the road. These subproblems are tractable for approximate DP, and their solutions can be recombined to approximate the solution for the full problem. To account for the approximation error due to multi-agent interactions, we combine the subproblems using a learned set of weights.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We apply our approach to two driving scenarios: a simple two-vehicle scenario to demonstrate the effectiveness of DP, and a more complex five-vehicle scenario to demonstrate the favorable scaling of the approach. In both experiments, we observed increases in the number of failures discovered compared to baseline approaches, and the discovered failure had comparatively high likelihood. The main contributions of this work are: A safety validation approach that estimates the distribution over failures using approximate DP.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An algorithm for problem decomposition and reconstruction to scale approximate DP to complex driving scenarios.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Demonstration of these techniques on two realistic driving scenarios and observation of a significant increase in rates of discovered failures.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of the paper is organized as follows: section II gives an overview of related work in the field of black-box validation for autonomous driving, section III describes our proposed technique in detail, section IV outlines the two experiments and describes our results, and section V concludes and discusses future work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Safety Validation of Black-Box Systems", "weight": 1.0} -->

Falsification of black box systems involves finding inputs to the system that lead to violation of the system specifications. State-of-the-art approaches cast falsification as a global optimization problem over the input space and try to solve it using surrogate models, deep reinforcement learning, genetic algorithms, Monte Carlo tree search, or cross-entropy optimization. Adaptive stress testing (AST) frames the problem of falsification as a Markov decision process and uses reinforcement learning to find the most-likely failures of a system according to a prescribed probability model. The field of statistical model checking deals with estimating the probability of failure, and in doing so will find inputs to the system that cause it to fail.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Safety Validation of Black-Box Systems", "weight": 1.0} -->

Several approaches rely on sampling-based methods to discover failures. \\Citeauthorhuang2019evaluation use bootstrapping and importance sampling to obtain a low-variance estimate of the probability of failure. Another approach uses importance sampling via the cross-entropy method to increase the number of failures found in simulation. \\Citeauthoruesato2018rigorous use previous versions of an autonomous agent to help find failures in the final version, an approach that works when when agents have learned behavior. Similar to the present work, \\CiteauthorChryssanthacopoulos2010 use DP to estimate the probability of failure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Safety of Autonomous Vehicles", "weight": 1.0} -->

Some work has focused on falsifying components of an autonomous vehicle such as Adaptive Cruise Control or perception systems. Other work has focused on the generation of critical test cases. For example identify regions of the input space that separate distinct types of autonomous agent behavior, and design adversarial agents to minimize the safe available driving space of the autonomous vehicle.

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROPOSED APPROACH", "weight": 1.0} -->

This section describes our approach to the safety validation problem. We start with the problem formulation and definition of notation. Then, we describe our technique for estimating the distribution over failures assuming we know the probability of failure from each state. Lastly, we describe how to compute that probability in a scalable way.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

Suppose we wish to analyze the safety of a black-box autonomous system (system-under-test, or SUT) that operates in a stochastic simulated environment. The state of the SUT and the environment is $s \in \mathcal{S}$ and the disturbances $x \in \mathcal{X}$ are stochastic elements of the environment that influence the behavior of the SUT. A state-disturbance trajectory $\tau = {\{ s_{0},x_{1},{s_{1}\ldots},x_{N},s_{N}\}}$ has a likelihood of occurrence $p{(\tau)}$. We define $E$ as the set of all failure states of the SUT and the notation $s_{N} \in E$ means that the trajectory $\tau$ ends in a failure. Let $T$ be the set of all terminal states where $E \subseteq T$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

We would like to know the distribution over failures where $\mathbb{1}$ is the indicator function and the denominator normalizes the distribution. Note that $f{(\tau)}$ is the minimum-variance importance sampling distribution for estimating the probability of failure.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Estimating the Distribution Over Failures", "weight": 1.0} -->

The space of all trajectories is exponential in the legnth of the trajectory, so it will be challenging to represent the distribution $f{(\tau)}$ directly. To reduce the dimensionality of the distribution we assume that the SUT and environment are Markov. The current disturbance $x$ and next state $s'$ will only depend on the current state $s$ such that If we also assume that the dynamics of the SUT and the environment are deterministic (i.e. all stochasticity is controlled through disturbances), then With these assumptions, the distribution over failures only depends on $p{({x \mid s})}$ and is given by The Markov assumption allows us to find a distribution over disturbances, or stochastic policy, $\pi$ that generates sample trajectories (rollouts) distributed according to $f$. Let where $v{(s)}$ is the probability of failure from state $s$ and $s^{\operatorname{\prime\prime}}$ is the state reached from $s$ after applying disturbance $x'$. The second equality in eq.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Estimating the Distribution Over Failures", "weight": 1.0} -->

5 comes from the observation that the probability of failure in the current state is a sum of the probability of failure over possible next states, weighted by the likelihood of reaching that state.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Computing the Probability of Failure", "weight": 1.0} -->

The feasibility of computing the probability of failure $v{(s)}$ depends on the size of the state and disturbance spaces. If those spaces are discrete and relatively small, then DP can be used to compute $v$ to any desired level of accuracy. If the state space is continuous, but is small enough to be discretized, then local approximation DP can be used to estimate $v{(s)}$. As will be demonstrated by our experiments, this approach is feasible for interactions between two vehicles on the road. For more vehicles, discretizing the state space becomes intractable and we must rely on further approximation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Computing the Probability of Failure", "weight": 1.0} -->

When scaling to much larger state-spaces, we can leverage the structure of the problem to improve scalability. We propose to decompose a complicated driving scenario into pairwise interactions between the ego vehicle and other agents on the road, similar to the decomposition approach used. Each subproblem can then be solved for the probability of failure between the $i$th vehicle and the ego vehicle yielding $v_{i}{(s^{(i)})}$, where $s^{(i)}$ is the subset of the state representing only those vehicles. To combine the probability of failure from each of $m$ subproblems, we can use the transfer learning approach called attend, adapt and transfer (A2T). A2T combines the solutions of $m$ problems with a solution learned from scratch $v_{base}$ using a learned set of state-dependent attention weights $w{(s)}$. The estimated probability of failure for a state $s$, $\overset{\sim}{v}{(s)}$, is then given by where $w_{i}$ and $v_{base}$ have parameters that can be learned.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Computing the Probability of Failure", "weight": 1.0} -->

The use of attention weights allows A2T to learn which solutions are most relevant in which states. If none of the subproblems are providing a good estimate then the base network will learn a good estimate from scratch. The estimate from eq. 12 can be represented as the network architecture shown in fig. 1. The base network has two hidden layers each with $32$ units and relu activations followed by a sigmoid activation to keep the output between $0$ and $1$. The solutions take the state as input and give the probability of failure estimate for each subproblem. The attention network has one hidden layer with $32$ units and a softmax layer to make sure the weights sum to 1. The base network output is concatenated to the subproblem solution outputs to create a vector of values that has $m + 1$ components. The dot product is taken between the values and the $m + 1$ weights to produce the final estimate of the probability of failure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Computing the Probability of Failure", "weight": 1.0} -->

1:function MCPolicyEval(${\overset{\sim}{v}}_{\theta}$, Niter, Nsamp, α) 2: for Niter iterations 3: S, G← Rollouts(${\overset{\sim}{v}}_{\theta}$, Nsamp) 4: $J = {\frac{1}{N_{samp}}{\sum_{j = 1}^{N_{samp}}\left({G_{j} - {v\left(S_{j} \right)}} \right)^{2}}}$ 6: return ${\overset{\sim}{v}}_{\theta}$ Algorithm 1 MC evaluation with function approximation The network can be trained using rollouts from the full driving scenario to estimate the probability of failure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Computing the Probability of Failure", "weight": 1.0} -->

The training procedure we used is Monte Carlo policy evaluation with function approximation and is shown in algorithm 1. The algorithm takes as input the network that estimates the probability of failure ${\overset{\sim}{v}}_{\theta}$ with trainable parameters $\theta$, the number of training iterations $N_{iter}$, the number of sampled transitions per iteration $N_{samp}$, and the learning rate $\alpha$. On each iteration, a series of rollouts are performed (line 3). The rollout policy is $\pi$ from eq. 5 where $v{(s)}$ is replaced with the current estimate ${\overset{\sim}{v}}_{\theta}{(s)}$. As the estimate of the probability of failure is improved, the rollout policy will produce more failure examples. All of the states visited during the rollouts are concatenated into a vector $S$. The return is computed for each state $s_{j} \in S$ as where $N$ is the length of the episode that contained state $s_{j}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Computing the Probability of Failure", "weight": 1.0} -->

The estimate $G$ is a Bernoulli sample weighted by the likelihood ratio of the current sampling policy so the expected value of of $G{(s)}$ is the probability of failure from state $s$. The cost $J$ is the mean squared error between the estimated probability of failure ${\overset{\sim}{v}}_{\theta}{(s)}$ and $G{(s)}$ (line 4). The parameters of the network are updated using the gradient of the cost function to improve the estimate (line 5).

<!-- chunk {"id": "body-0024", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

This section describes two experimental driving scenarios, a simple scenario with two vehicles, and a more complex scenario with five vehicles. The simulations were designed with AutomotiveSimulator.jl, an open-source julia package. Both simulations rely on the same road geometry and autonomous driving policy. The SUT is an autonomous vehicle referred to as the ego vehicle and a failure refers to any instance where the ego vehicle collides with another vehicle.

<!-- chunk {"id": "body-0025", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

The road geometry and initial vehicle configurations are pictured in figs. 2, 3, 4 and 5. The driving scenario an unprotected left turn of the ego vehicle (in blue) onto a two-lane road. Other vehicles (referred to adversarial vehicles) are initialized on the through-road and can either continue straight or turn (the yellow dot represents a turn signal). The right-of-way rules are 1) vehicles on the through-road have right-of-way over vehicles turning on to the through-road, and 2) vehicles turning right have right-of-way over vehicles turning left.

<!-- chunk {"id": "body-0026", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

The state of each vehicle can be described with four variables: position along the lane, velocity along the lane, a Boolean indicating if the turn signal is, an integer indicating the lane. For approximate DP, the position and velocity were each discretized into $15$ values and each vehicle can be in one of two lanes so each vehicle had a total of $900$ states.

<!-- chunk {"id": "body-0027", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Each vehicle on the road including the ego vehicle, follows a modified version of the intelligent driver model (IDM). The IDM is a vehicle-following algorithm that tries to drive at a specified velocity while avoiding collisions with leading vehicles. In our experiments, the IDM is parameterized by a desired velocity of $29\ {m/s}$, a minimum spacing of $5\ m$, a maximum acceleration of $3\ {m/s^{2}}$ and a comfortable braking deceleration of ${- 2}\ {m/s^{2}}$, and a simulation timestep of ${\Deltat} = {0.18\ s}$. The IDM was modified with a rule-based algorithm (algorithm 2) for navigating the T-intersection. Each vehicle reasons about right-of-way and turning intention of other vehicles based on the state of their blinker, and uses current vehicle speeds to calculate if the intersection is safe to cross.

<!-- chunk {"id": "body-0028", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

3: vlead, Δ slead← leading_vehicle(v e h, s c e n e) 4: a c c← IDM_acceleration(Δ slead, v, vlead) 5: if v e h does not have right of way 6: t t c ← time_to_cross_intersection(v e h) 7: Δ sint ← distance_to_intersection(v e h) 10: t t e n t e r ← time_to_enter_intersection(a g e n t) 11: t t e x i t ← time_to_exit_intersection(a g e n t) 13: a c c← IDM_acceleration(Δ sint, v, 0) Algorithm 2 Intersection navigation algorithm The disturbances in the environment correspond to disturbances to the deterministic actions of all adversarial vehicles. The disturbances and their corresponding probabilities are shown in table I. The first produces no disturbance, so the adversary accelerates by $a_{IDM}$, the acceleration computed by the modified IDM.

<!-- chunk {"id": "body-0029", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

The next four disturbances perturb the adversary's acceleration by an amount ${\deltaa} \in {\lbrack{{- 3}\ {m/s^{2}}},{3\ {m/s^{2}}}\rbrack}$ so that the actual acceleration of the adversary is $a_{IDM} + {\deltaa}$. The next disturbance toggles the adversary's turn signal which is observed by other vehicles and used to determine the adversary's intention. The final disturbance changes the hidden adversary intention as to whether or not it will turn.

<!-- chunk {"id": "body-0030", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

The choice of a disturbance probability model should be driven by real-world driving data. In absence of that data, we chose a simple probability model that made disturbances rare according to their magnitude (see MC Probability in table I). Medium slowdowns and speedups were give a probability of $1\text{×}10^{- 2}$ per timestep while major slowdowns and speedups, toggling the blinker, and toggling turn intention had a per-timestep probability of occurrence of $1\text{×}10^{- 3}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Toggle turn intent TABLE I: Action space for adversarial vehicles The two metrics we chose to evaluate our approach are the rate of failures found and the log-likelihood of adversary disturbances for failure trajectories. The failure rates are computed from $1000$ rollouts and the average log-likelihood of disturbances is computed from $100$ failure examples. The mean and standard deviations are reported. We compare our approach against three baselines: Monte Carlo: rollouts with the true probability distribution over disturbances.

<!-- chunk {"id": "body-0032", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Uniform importance sampling: rollouts with a uniform distribution over disturbances.

<!-- chunk {"id": "body-0033", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Cross entropy method: rollouts with a distribution over disturbances that has been optimized using the cross entropy method.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Two-Vehicle Interaction", "weight": 1.0} -->

The first scenario is an interaction between the ego vehicle and one adversarial vehicle over a range of initial conditions. Figure 2 shows one mode of expected behavior in the scenario: the ego vehicle correctly predicts it can cross the intersection before the other driver arrives so it proceeds with the left turn. A sample failure is shown in fig. 3. We can see that the adversary had to accelerate early in the simulation to cause a collision with the ego vehicle, which did not predict that an acceleration would occur.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Two-Vehicle Interaction", "weight": 1.0} -->

Table II shows the number of failures observed with each approach. Monte Carlo sampling finds the fewest failures with a rate of $8\text{×}10^{- 3}$ but the failure trajectories have a comparatively large log-likelihood. The uniform importance sampling approach increases the number of failures found by making rare disturbances more likely, but causes the found failures to be extremely unlikely due to these rare disturbances. The cross entropy method finds slightly more failures than the Monte Carlo approach with a larger log likelihood than uniform importance sampling. The DP approach was most successful with a failure rate of $1.67\text{×}10^{- 1}$ while still retaining a large value of log likelihood.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B 5 Vehicle Interaction", "weight": 1.0} -->

The second scenario involves the interaction of the ego vehicle with four adversarial drivers. A sample of normal behavior for the scenario is shown in fig. 4 where the cars on the left and the trailing car on the right go straight, while the leading car on the right turns onto the vertical road segment. The ego vehicle gives way to all four vehicles and completes the left turn after they have passed. A sample failure is shown in fig. 5. The failure shows that the last car on the left turns it signal on while continuing straight through the intersection, tricking the ego vehicle into initiating the left turn too early.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B 5 Vehicle Interaction", "weight": 1.0} -->

The driving scenario was broken into four subproblems, one for each adversarial vehicle. The probability of failure was computed for each driving scenario using approximate DP and the solutions were combined using an A2T network trained on rollouts of the full simulator. One challenge for this approach is the exponential scaling of the disturbance space of the full system. If there are 4 subproblems each with $7$ disturbances then the full problem must consider $2401$ disturbances per step. To mitigate this problem, we only let one agent act at each timestep, reducing the possible disturbances to $28$. This design choice reduces the complexity of possible failure modes, but makes the problem tractable while still finding failures.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B 5 Vehicle Interaction", "weight": 1.0} -->

The results are shown in table III. We first note that the failure rate in the scenario is lower than the previous scenario as indicated by the failure rate of the Monte Carlo approach ($1.1\text{×}10^{- 3}$). The uniform importance sampling approach improves failure rate significantly but finds failures with very low likelihood due to the increased number of rare disturbances. The cross entropy method has twice the failure rate as the Monte Carlo approach with a similar log-likelihood. Our approach (DP combined with A2T) has a much larger failure rate ($2.22\text{×}10^{- 1}$) while finding relatively likely failures, demonstrating that scene decomposition combined with A2T is an effective strategy for finding failures of an autonomous vehicle in a complex driving scenario.

<!-- chunk {"id": "body-0039", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this work, we have made progress toward the goal of automated testing of autonomous vehicles. We introduced a safety validation formulation that uses approximate dynamic programming to estimate the distribution over failures and create sequences of disturbances that cause an autonomous system to fail. The problem of scalability was addressed by decomposing the driving scenario into pairwise interactions between the ego vehicles and other agents on the road. These subproblems were solved and recombined to estimate the probability of failure of the full system. To correct for errors in this estimate, we trained an A2T network with Monte Carlo policy evaluation to weight each subproblem based on the state. We observed $1$ to $2$ orders of magnitude increase in the number of failures found compared to importance sampling baselines in a two-vehicle driving scenario and a more complex five-vehicle driving scenario, demonstrating the benefit of this approach. Future work will use the calculated policy to obtain a low-variance estimate of the probability of failure, test performance on more complicated driving scenarios with many agents, and attempt to interpret the attention weights parameters to understand the cause of failures.
