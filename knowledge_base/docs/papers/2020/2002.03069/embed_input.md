<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Adaptive Approximate Policy Iteration

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-free reinforcement learning algorithms combined with value function approximation have recently achieved impressive performance in a variety of application domains. However, the theoretical understanding of such algorithms is limited, and existing results are largely focused on episodic or discounted Markov decision processes (MDPs). In this work, we present adaptive approximate policy iteration (AAPI), a learning scheme which enjoys a tildeO(T^(2/3)) regret bound for undiscounted, continuing learning in uniformly ergodic MDPs. This is an improvement over the best existing bound of tildeO(T^(3/4)) for the average-reward case with function approximation. Our algorithm and analysis rely on online learning techniques, where value functions are treated as losses. The main technical novelty is the use of a data-dependent adaptive learning rate coupled with a so-called optimistic prediction of upcoming losses. In addition to theoretical guarantees, we demonstrate the advantages of our approach empirically on several environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our work focuses on model-free algorithms for learning in infinite-horizon undiscounted Markov decision processes (MDPs), also known as average-reward MDPs. Although model-free algorithms have recently achieved impressive advances in multiple applications [Mnih et al., 2015, Van Hasselt et al., 2016], few performance guarantees exist, especially in the average-reward case with function approximation. In this work, we propose Adaptive Approximate Policy Proceedings of the 24 th International Conference on Artificial Intelligence and Statistics (AISTATS) 2021, San Diego, California, USA. PMLR: Volume 130. Copyright 2021 by the author(s).

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Iteration (AAPI), a model-free learning scheme that can work with function approximation, and utilizes an adaptive data-dependent learning rate. We analyze the performance of AAPI in infinite-horizon undiscounted MDPs in terms of high-probability regret.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our approach follows the 'online MDP' line of work [EvenDar et al., 2009, Neu et al., 2014, Abbasi-Yadkori et al., 2019a], where the agent iteratively selects policies by running an online learning algorithm in each state, and the loss fed to each algorithm is the policy Q-function in that state. This results in a variant of approximate policy iteration (API), where the policy improvement step produces a policy optimal in hindsight w.r.t. the average of all previous Q-functions rather than just the most recent one. The original work of Even-Dar et al. studied this scheme with known dynamics, tabular representation, and adversarial reward functions. More recent works [Abbasi-Yadkori et al., 2019a,b] have adapted this approach to the case of unknown dynamics, stochastic rewards, and value function approximation. The averaging of value functions is further justified theoretically and empirically by Vieillard et al. and Vieillard et al..

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A notable feature of our algorithm is that we exploit the fact that losses (Q-function estimates) are slow-changing. In particular, our policy improvement step relies on the adaptive optimistic follow-the-regularized-leader (AO-FTRL) update [Mohri and Yang, 2016]. The resulting policies are Boltzmann distributions over the sum of past estimated Q-functions, coupled with an optimistic prediction of the upcoming loss and a state-dependent adaptive learning rate (softmax temperature). Our policy improvement step can also be seen as regularizing each policy by the KLdivergence to the previous policy; the reduction to online learning offers a principled way to scale such regularization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

On the theoretical side, we prove the first ˜ O ( T 2 / 3 ) regret upper bound in the undiscounted, continuing setting with function approximation. This is an improvement over the best existing ˜ O ( T 3 / 4 ) bound of Abbasi-Yadkori et al. [2019a] for the same setting, which ignores the slow-changing na- ture of the estimated Q-functions. Our analysis exploits the fact that the change in consecutive Q-function estimates can be bounded by the change in policies. We rely on the results of Rakhlin and Sridharan, but employ a different regret decomposition, with additional information provided by MDPproperties. We emphasize that our learning framework is not limited to a particular function approximation method, and that in practice it serves the purpose of appropriately regularizing the policy improvement step of API.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Related work. Most no-regret algorithms for infinitehorizon undiscounted MDPs are model-based, and only applicable to tabular representations [Bartlett, 2009, Jaksch et al., 2010, Ouyang et al., 2017, Fruit et al., 2018, Jian et al., 2019, Talebi and Maillard, 2018]. In the modelfree tabular setting, Wei et al. show optimistic Qlearning achieves O ( sp ( V ∗ )( XA ) 1 / 3 T 2 / 3 ) regret in weaklycommunicating MDPs, where sp ( V ∗ ) is the span of the optimal state-value function, X,A are the size of state and action spaces. In the case of uniformly ergodic MDPs, they show a bound of O ( √ t 3 mix ρAT ) on the expected regret, where t mix is the mixing time and ρ is the stationary distribution mismatch coefficient. In the model-free setting with function approximation, Abbasi-Yadkori et al. [2019a] achieve O ( d 1 / 2 T 3 / 4 ) regret in ergodic MDPs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Here d is the size of the compressed state-action space ( XA for tabular representation, number of features for linear Q -functions).

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In episodic MDPs with horizon H, Jin et al. show an O ( √ H 3 XAT ) regret bound for Q-learning with tabular representation. With linear function approximation, Yang and Wang [2019b], Jin et al., Cai et al. show an O ( √ d 3 H 3 T ) regret bound for an optimistic version of least-squares value/policy iteration under linear MDPs assumption. The RLSVI algorithm [Osband et al., 2016] performs exploration in the value function parameter space, and therefore can be applied with function approximation. Its worse-case regret bound of O ( √ H 5 X 3 AT ) holds in the tabular setting [Russo, 2019] and O ( d 2 √ H 4 T ) holds under the linear MDPs assumption [Zanette et al., 2020].

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Another thread of the literature [Ross et al., 2011, Ross and Bagnell, 2014] proposes a reduction of model-free RL to any no-regret online learning. While Ross et al. mainly focus on imitation learning, Ross and Bagnell consider the finite-horizon case and uses a generic no-regret online learner that may result in a worse regret guarantee. Very recently, Cheng et al. exploit optimistic mirror descent to speed up policy optimization in RL, but do not provide a regret analysis in average-reward case.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

AAPI is also similar to the conservative policy iteration works, which attempt to stabilize API by regularizing each policy towards the previous policy [Kakade and Langford, 2002, Schulman et al., 2015, 2017, Abdolmaleki et al., 2018, Geist et al., 2019, Vieillard et al., 2020]. In particular, Neu et al. identify several state-of-the-art entropyregularized RL algorithms as approximate variants of mirror descent, and Shani et al. provides convergence rates for a mirror descent like algorithm in the discounted setting. Vieillard et al. provides a systematical analysis of regularization in RL. To the best of the authors' knowledge, none of these works use adaptive data-dependent learning rate to accelerate policy learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

We first introduce some notation. We use ∆ S to denote the space of probability distributions defined on the set S and write [ d ] = { 1, 2,..., d }. For vectors u, v ∈ R d, we define the weighted ℓ 2 -norm as ‖ v ‖ 2 u = ∑ d i =1 u i v 2 i and ℓ ∞ -norm as ‖ u ‖ ∞ = max j ∈ [ d ] u j. In general, we treat discrete distributions as row vectors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

Infinite-horizon undiscounted MDPs are often characterized by a finite state space X, a finite action space A, a reward function r: X × A →, and a transition probability function P: X × A → ∆ X. The agent does not know the transition probability and the reward function in advance. A policy π: X → ∆ A is a mapping from a state to a distribution over actions. Let { (x π t, a π t) } ∞ t =1 denote the state-action sequence obtained by following policy π. The expected average reward of policy π is defined as The agent interacts with the environment as follows: at each round t, the agent observes a state x t ∈ X, chooses an action a t ∼ π t (·| x t), and receives a reward r (x t, a t). The environment then transitions to the next state x t +1 with probability P (x t +1 | x t, a t). The initial state x 1 is randomly generated from some unknown distribution. Let π ∗ be an unknown fixed policy. The regret of an algorithm with respect to this fixed policy is defined as where a t ∼ π t (·| x t).

<!-- chunk {"id": "body-0015", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

The learning goal is to find an algorithm that minimizes the long-term regret R T. Note that R T is still a random variable so we will bound it with high probability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

For each policy π, we denote P π ∈ R |X|×|X| to be the Markov chain induced by π, where the component (P π) x,x ′ is the transition probability from x to x ′ under π, i.e. (P π) x,x ′ = ∑ a ∈A π (a | x) P (x ′ | x, a). For a distribution µ over X, we let µ P π be the distribution over X that results from executing the policy π for one step after the initial state is sampled from µ. A stationary distribution µ π of a policy π over states satisfies µ π P π = µ π. For a policy π, its expected reward can be expressed as In this work, we focus on ergodic MDPs, a sub-class of weakly communicating MDPs. An MDP is ergodic if the Markov chain induced by any policy π is both irreducible and aperiodic, which means any state is reachable from any other state by following a suitable policy. It is wellknown that all ergodic MDPs have an unique stationary state distribution, and so µ π and λ π are well-defined.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

In addition, ergodic MDPs have a finite mixing time, defined below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

Definition 2.1. The mixing time of ergodic MDPs is defined as t mix:= that characterizes how fast MDPs reach stationary distributions from any state under any policy.

<!-- chunk {"id": "body-0019", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

Finally, we define the value function under policy π as where E π is with respect to the sample path induced by π.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm", "weight": 1.0} -->

AAPIis a variant of approximate policy iteration and it proceeds in phases. Suppose the total number of rounds is T. We divide T into K phases of length τ = T/K and assume τ is an integer for simplicity. Within each phase, our algorithm performs two tasks: policy evaluation and policy improvement.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Policy evaluation. In each phase k ∈ [ K ], the algorithm executes the current policy π k for τ time steps, and computes an estimate ̂ Q π k of the true action-value function Q π k.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We leave unspecified the value function estimation method G; for example, one can use incremental algorithms, or both on-policy and off-policy data. AAPI is better interpreted as a learning schema. Our regret analysis will require that longer phase lengths lead to better estimates (made precise in Lemma 5.3).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Policy improvement. For each state x ∈ X, the policy improvement step takes the form of the adaptive optimistic follow-the-regularized-leader (AO-FTRL) update [Mohri and Yang, 2016]: (See Step 3 in Section 5 for a generic description of AOFTRL.) The terms in Eq. (3.1)

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm", "weight": 1.0} -->

- The estimates ̂ Q π s (x, ·) ∈ R |A| are the loss functions fed to the AO-FTRL algorithm. R (f) is the negative entropy regularizer, and F is the probability simplex. - The side-information M k +1 (x, ·) ∈ R |A| is a vector computable based on past information and being predictive of the next loss ̂ Q π k +1 (x, ·). Since the policies are expected to change slowly due to the nature of exponential-weight-average type algorithms, we set M k +1 (x, ·) = ̂ Q π k (x, ·) (better guesses such as offpolicy estimates can be used if available). - The choice of learning rate η k (x) is crucial both theoretically and empirically. In particular, we choose η k (x) in a data-dependent fashion as A notable feature of η k (x) is that it is also statedependent.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Intuitively, for the choice M s (x, ·) = ̂ Q π s -1 (x, ·), the adaptive state-dependent learning rate results in a more exploratory policy for the states on which there is more disagreement between the past consecutive action-value functions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Based on (3.1), the next policy is a Boltzmann distribution (a consequence of negative entropy regularizer) over the sum of all past state-action value estimates and the sideinformation: Remark 3.1. AAPIis similar to the POLITEX algorithm Abbasi-Yadkori et al. [2019a], where the main difference is that POLITEX sets the next policy to π k +1 (a | x) ∝ exp(η -1 ∑ k s =1 ̂ Q π s) in the improvement step. We demonstrate that the use of side-information and adaptive learning rates improves both the theoretical guarantees (Theorem 4.5) and empirical performance (Section 6) over POLITEX. The overall algorithm is summarized in Algorithm 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Algorithm 1 Adaptive approximate policy iteration (AAPI)

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm", "weight": 1.0} -->

- 1: Input: phase length τ, number of phase K, initial state x 0, turning parameter η, value function estimation algorithm G. - 5: Execute π k for τ time steps and collect dataset D k. - 6: Estimate ̂ Q π k from D 1,..., D k using G.

<!-- chunk {"id": "body-0029", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

To derive a regret bound for Algorithm 1, we decompose the cumulative regret (2.1) as follows: The first term captures the sum of differences between observed rewards and their long term averages. If policies are changing slowly, or if they are kept fixed for extended periods of time, we expect this term to capture the noise in the regret. The second term is called pseudo-regret in literature. It measures the difference between the expected reward of a fixed policy and the policies produced by the algorithm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

We first impose a condition on the quality of policy evaluation at each phase. For a probability distribution µ on X and a stochastic policy π, define µ ⊗ π to be the distribution on X × A that puts the probability mass µ ( x ) π ( a | x ) on pair ( x, a ) ∈ X × A. Recall that µ π ∗ is the stationary distribution of π ∗ over the states.

<!-- chunk {"id": "body-0031", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Condition 4.1. For each phase k ∈ [K], denote D π k = ̂ Q π k -Q π k. Weassume the following holds with probability 1 -δ, where ε 0 is the irreducible approximation error and ˜ C is a problem dependent constant. Additionally, there exists a constant b such that ̂ Q π k (x, a) ∈ [b, b + Q max] for any pair (x, a) ∈ X × A and k ∈ [K].

<!-- chunk {"id": "body-0032", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Remark 4.2. The problem dependent constant ˜ C will in general depend on d, t mix, µ π ∗, µ π k. Here, d is the dimension of the representation (e.g. |X||A| for the tabular case, or number of features for the linear value function case).

<!-- chunk {"id": "body-0033", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Remark 4.3. The requirement for the µ π ∗ ⊗ π ∗ -norm and µ π ∗ ⊗ π k -norm has been shown to hold, for example, with linear value function approximation using the LSPE algorithm [Bertsekas and Ioffe, 1996], under Assumptions B.1B.3 given in the Appendix. Lemma B.4 in the Appendix shows that the requirement for ℓ ∞ -norm can also be satisfied, for example, with linear value functions, under similar conditions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Remark 4.4. The estimation error generally depends on the mismatch between distributions µ π k and µ π ∗. With value functions linear in features φ ( x, a ) ∈ R d, this mismatch depends on the spectra of matrices E ν [ φ ( x, a ) φ ( x, a ) ⊤ ] for different distributions ν, and need not scale in the number of state-action pairs. See Assumption A4 in Abbasi-Yadkori et al. [2019a] for a more detailed explanation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Theorem 4.5 (Main result). Consider an ergodic MDP and suppose Condition 4.1 holds. By choosing the phase length τ = (˜ C/ρt 3 mix) 2 / 3 T 2 / 3, we have with probability at least 1 -1 /T, where ρ is the distribution mismatch coefficient that has used in previous work [Kakade and Langford, 2002, Agarwal et al., 2020, Wei et al., 2019] and ˜ O (·) hides universal constants and poly-logarithmic factors.

<!-- chunk {"id": "body-0036", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Remark 4.6. It is worth comparing the above result with the regret bound presented in Abbasi-Yadkori et al. [2019a]. Ignoring the irreducible error ε 0, we improve the leading order of their general result from ˜ O ( T 3 / 4 ) to ˜ O ( T 2 / 3 ). When specialized to linear value function approximation where ˜ C scales with d 1 / 2, we improve their results from ˜ O ( d 1 / 2 T 3 / 4 ) to ˜ O ( d 1 / 3 T 2 / 3 ).

<!-- chunk {"id": "body-0037", "role": "body", "section": "ANALYSIS", "weight": 1.0} -->

Remark 4.7. It is worth to mention that Wei et al. obtains ˜ O ( √ T ) regret in terms of expected regret in the tabular case for ergodic MDPs while we consider highprobability regret. In particular, their analysis does not account for the estimation and approximation errors in Qfunctions that will significantly complicate the analysis and result in a worse regret bound.

<!-- chunk {"id": "body-0038", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

In this section we provide an empirical evaluation of AAPIon several environments. We compare AAPIto POLITEX, which corresponds to updating policies using a mirror descent rule rather than AO-FTRL. We also evaluate RLSVI, where policies are greedy w.r.t. a randomized estimate of Q ∗. Overall, we find that AAPI performs well in discrete-state environments such as DeepSea [Osband et al., 2017], whereas the adaptive per-state learning rate is less helpful in environments such as CartPole [Barto et al., 1983] with continuous states and smooth dynamics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We approximate all value functions using least-squares Monte Carlo, i.e. linear regression from state-action features to empirical returns. For MDPs with a large or continuous state space X, updating per-state learning rates can be impractical. Instead, we store the weights of past Qfunctions in memory, and for each state in the trajectory, we compute the learning rate using a subset of n k ≤ 30 randomly-selected past weight vectors (we correct the scale of the estimate by multiplying with √ k/n k. With rich function approximation such that neural networks, one can keep a fixed buffer with a subset of the previous Q-functions, or train distillation networks that summarize the sum of previous Q-functions. Another possibility is to parameterize π k and optimize the objective w.r.t. the parameters. For Boltzmann policies, we tune the constant η for the learning rate η k ( x ) in the range [0. 01, 100]. For each environment and algorithm we evaluate -∑ t s =1 r t /t and plot the mean and standard deviation over 50 runs. The environments we evaluate on are as follows.

<!-- chunk {"id": "body-0040", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Tabular ergodic MDPs. We consider a simple tabular MDP where r (1, a ) = 1, r ( x, a ) = 0 for x = 1. On any action in state 1, the environment transitions to a randomly chosen state x = 1. On action 1 in a state x = 1, the environment transitions to state x -1 with probability 0.9, and to a randomly chosen state with probability 0.1. On all other actions in x = 1, the environment transitions to a randomly chosen state. We represent state-action pairs using one-hot indicator vectors of size |X||A|, and experiment with different sizes of the state and action spaces X and A.

<!-- chunk {"id": "body-0041", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

DeepSea [Osband et al., 2017]. In the DeepSea environment, states comprise an N × N grid, and there are two actions. The environment transitions and costs are deterministic. The agent starts in the top-left cell. On action 0, the agent transitions down and left, and receives reward 0. On action 1, the agent transitions down and right, and receives reward -1. On transitioning to the bottom-right cell (N -1, N -1), the agent receives reward 2 N. The infinitehorizon version of the environment wraps the environment around the vertical axis. An optimal strategy first takes the action 1 N times (to get to (N -1, N -1)) and then takes an equal number of 0 and 1 actions, and has expected average reward close to 1. 5. A simple strategy that always takes action 1 has an average reward 1, and a suboptimal strategy that only takes action 0 has an average reward of 0. We represent states as length2 N vectors containing onehot indicators for each grid coordinate, and estimate linear Q -functions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

CartPole [Barto et al., 1983]. In the CartPole environment, the goal is to balance an inverted pole attached by an unactuated joint to a cart, which moves along a frictionless rail. There are two actions, corresponding to pushing the cart to the left or right. The observation consists of the position and velocity of the cart, pole angle, and pole velocity at the tip. There is a reward of +1 for every timestep that the pole remains upright. The episodic version of the environment ends if the pole angle is more than 15 degrees from vertical, if the cart moves more than 2.4 units from the center, or after 200 steps. In the infinite-horizon version, if the episode ends after h steps, we return a reward of h -200 and reset. For this task, in addition to the given observation, we extract multivariate Fourier basis features Konidaris et al. of order 4.

<!-- chunk {"id": "body-0043", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Discussion. In most of our experiments, adaptive learning rate speeds up the convergence of approximate policy iteration, compared to using a constant learning rate as in Politex. The adaptive per-state learning rate is less helpful in CartPole, possibly because observations are continuous and dynamics are smooth, so there is higher generalization across states.

<!-- chunk {"id": "body-0044", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have presented AAPI, a model-free learning scheme that can work with function approximation, and enjoys a ˜ O ( T 2 / 3 ) regret guarantee in infinite-horizon undiscounted, ergodic MDPs. AAPIimproves upon previous results for this setting by using the slow-changing property of policies in both theory and practice. One direction for future work is improving the policy evaluation stage. While we estimate each value function solely using the τ on-policy transitions, better estimates can potentially be obtained using all data. Using more sophisticated side-information, such as a weighted average of past Q-estimates or an off-policy estimate of the Q-function may also be helpful in practice. Other future work may include practical implementations of the algorithm when trained with neural networks that maintain only a subset of past networks in memory; one possible practical approach is given by Vieillard et al..
