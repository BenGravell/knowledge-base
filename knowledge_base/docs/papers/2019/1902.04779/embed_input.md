<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample-Optimal Parametric Q-Learning Using Linearly Additive Features

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Consider a Markov decision process (MDP) that admits a set of state-action features, which can linearly express the process's probabilistic transition model. We propose a parametric Q-learning algorithm that finds an approximate-optimal policy using a sample size proportional to the feature dimension K and invariant with respect to the size of the state space. To further improve its sample efficiency, we exploit the monotonicity property and intrinsic noise structure of the Bellman operator, provided the existence of anchor state-actions that imply implicit non-negativity in the feature space. We augment the algorithm using techniques of variance reduction, monotonicity preservation, and confidence bounds. It is proved to find a policy which is epsilon-optimal from any initial state with high probability using O~(K/epsilon^(1-gamma)^) sample transitions for arbitrarily large-scale MDP with a discount factor gamma . A matching information-theoretical lower bound is proved, confirming the sample optimality of the proposed method with respect to all parameters (up to polylog factors).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Markov decision problems (MDP) are known to suffer from the curse of dimensionality. A basic theoretical question is: Suppose that one can query sample transitions from any state of the system using any action, how many samples are needed for learning a good policy? In the tabular setting where the MDP has $S$ states and $A$ actions, the necessary and sufficient sample size for finding an approximate-optimal policy is $\overset{\sim}{\Theta}{(\frac{SA}{{({1 - \gamma})}^{3}})}$ ^11^1$\overset{\sim}{f{(\cdot)}}$ ignores ${{poly}{\log f}}{( \cdot )}$ factors. where $\gamma \in {}$ is a discount factor Azar et al.; Sidford et al.. However, this theoretical-sharp result does not generalize to practical problems where $S,A$ can be arbitrarily large or infinite.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let us consider MDP with structural knowledges. Suppose that each state-action pair $(s,a)$ admits a feature vector ${\phi{(s,a)}} \in {\mathbb{R}}^{K}$ that can express the transition dynamics conditioning on $(s,a)$. In practice, the abstract state variable $s$ can be a sequence of historical records or a raw-pixel image, containing much information that is not related to the decision process. More general settings of MDP with structural knowledges have been considered in Azizzadenesheli et al.; Jiang et al. and references therein.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus on an important and very basic class of structured MDP, where the features can represent transition distributions $P{( \cdot \mid \cdot )}$ through an unknown linear additive model. The feature-based linear transition model is related to the commonly used linear Q-function model. We show that they are essentially equivalent when there is zero Bellman error (a notion introduced in Munos and Szepesvári ). A similar argument has been made in Parr et al.. It also contains as a special case the soft state aggregation model Singh et al.; Duan et al.. In this setting, we will study the theoretic sample complexity for learning a good policy by querying state-transition samples. We also aim to develop efficient policy learning algorithms with provable sample efficiency.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Q1: How many observations of state-action-state transitions are necessary for finding an $\epsilon$-optimal policy?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Q2: How many samples are sufficient for finding an $\epsilon$-optimal policy with high probability and how to find it?

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To answer Q1, an information-theoretic lower bound is provided (Theorem 1. ‣ 3 Information-Theoretic Sample Complexity ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")), suggesting that, regardless of the learning algorithm, the necessary sample size for finding a good policy with high probability is $\overset{\sim}{\Omega}\left( \frac{K}{{({1 - \gamma})}^{3} \cdot \epsilon^{2}} \right)$ where $K$ is the dimension of feature space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To answer Q2, we develop Q-learning-like algorithms that take as input state-transition samples and output a parameterized policy. A basic parametric Q-learning algorithm performs approximate value-iteration estimates on a few points of the Q function, so that actual updates happen on the parameters. This idea originates from the phased Q-learning Kearns and Singh and the fitted value iteration Munos and Szepesvári; Antos et al.. Our algorithm is simpler and does not require function fitting. Convergence and approximation error analysis is provided even when the MDP cannot be fully expressed using the features. Despite its simplicity, the basic algorithm has complexity $\overset{\sim}{O}\left( \frac{K}{{({1 - \gamma})}^{7} \cdot \epsilon^{2}} \right)$, which is not sample-optimal.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we develop an accelerated version of parametric Q-learning that involves taking mini-batches, computing confidence bounds, and using monotonicity-preserving and variance reduction techniques. It uses some ideas from fast solvers of tabular MDP Sidford et al.. To fully exploit the monotonicity property of the Bellman operator in the algorithm, we need an additional "anchor" assumption, i.e., there exists a (small) set of state-actions that can represent the remaining ones using convex combinations. The "anchors" can be viewed as vertices of the state-action space, and implies an intrinsic nonnegativity in the feature space which is needed for monotonic policy improvement. We show that the algorithm takes just enough samples per update to keep the value/policy iterates within a sequence of narrow confidence regions that monotonically improve to the near-optimal solutions. It finds an $\epsilon$-optimal policy (regardless of the initial state) with probability at least $1 - \delta$ using

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

samples. It matches the information-theoretic lower bound up to $\log{( \cdot )}$ factors, thus the algorithm is nearly sample-optimal. If $\gamma = 0.99$, this algorithm is ${({1 - \gamma})}^{- 4} = 10^{8}$ times faster than the basic algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our model, algorithms and analyses relate to previous literatures on the sample complexity of tabular MDP, reinforcement learning with function approximation, linear models and etc. A detailed account for the related literatures is given in Section 6. All technical proofs are given in the appendix. To our best knowledge, this work provides the first sample-optimal algorithm and sharp complexity analysis (up to polylog factors) for MDP with linear models.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Markov Decision Process, Features, Linear Models", "weight": 1.0} -->

In this section we introduce the basics of Markov decision process and the feature-based linear transition model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Feature-based Linear Transition Model", "weight": 1.0} -->

We study Markov decision processes with structural knowledges. Suppose that the learning agent is given a set of $K$ feature functions ${\phi_{1},\phi_{2},\ldots,\phi_{K}}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$. The feature $\phi$ maps the raw state and action $(s,a)$ into the $K$-dimensional vector

<!-- chunk {"id": "body-0015", "role": "body", "section": "Feature-based Linear Transition Model", "weight": 1.0} -->

Suppose the feature vector $\phi{(s,a)}$ is sufficient to express the future dynamics of the process conditioning on the current raw state and action. In particular, we focus on a basic linear model given below.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1 (Independence of rewards)", "weight": 1.0} -->

The feature representations $\phi{(s,a)}$ in Definition 1. ‣ 2.2 Feature-based Linear Transition Model ‣ 2 Markov Decision Process, Features, Linear Models ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") capture the transition dynamics of the Markov process under different actions. It is a form of structural knowledge about the environment. It has nothing to do with the rewards $r{(s,a)}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 2 (Combining state features and action features)", "weight": 1.0} -->

In many settings one may be given a state-only feature map $\phi_{1}$ and an action-only feature map $\phi_{2}$. In this case, one can construct the joint state-action feature by ${\phi{(s,a)}} = {\phi_{1}{(s)}\phi_{2}{(a)}}$. As long as the MDP admits a linear transition model in both $\phi_{1},\phi_{2}$, it also admits a linear representation in the product feature $\phi = {\phi_{1} \times \phi_{2}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 3 (Relation to soft state aggregation)", "weight": 1.0} -->

The feature-based linear transition model (Definition 1. ‣ 2.2 Feature-based Linear Transition Model ‣ 2 Markov Decision Process, Features, Linear Models ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")) contains a worth-noting special case. When each ${\phi{(s,a)}} \in {\mathbb{R}}^{K}$ and $\psi_{k} \in {\mathbb{R}}^{S}$ is a probability density function, the linear transition model reduces to a soft state aggregation model Singh et al.; Duan et al.. In the soft state aggregation model, each state can be represented by a mixture of latent meta-states, through aggregation and disaggregation distributions. There would be $K$ meta-states, which can be viewed as the leading "modes" of the process. In contrast, our feature-based transition model is much more general. Our feature map $\phi$ can be anything as long as it is representative of the transition distributions. It captures information about not only the states but also the actions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Relation to Linear Q-function Model", "weight": 1.0} -->

Linear models are commonly used for approximating value functions or Q-functions using given features (sometimes referred to as basis functions). The proposed linear transition model is closely related to the linear Q-function model, where $Q^{\pi}$'s are assumed to admit a linear representation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Relation to Linear Q-function Model", "weight": 1.0} -->

First it is easy to see that if the MDP admits a linear transition model using $\phi$, the Q-functions admit a linear model.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Information-Theoretic Sample Complexity", "weight": 1.0} -->

Let us study the feature-based MDP model (Definition 1. ‣ 2.2 Feature-based Linear Transition Model ‣ 2 Markov Decision Process, Features, Linear Models ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")). It comes with the structural knowledge that each state-action pair $(s,a)$ can be represented by the feature vector ${\phi{(s,a)}} \in {\mathbb{R}}^{K}$. However, this model can not be parameterized by a small number of parameters. The full transition model with known feature map $\phi$ can not be specified unless all the unknown parameters ${\psi_{k}{(s^{\prime})}},$ for ${s^{\prime} \in S},{k \in {\lbrack K\rbrack}}$ are given. Its model size is ${S \times K},$ which can be arbitrarily large for arbitrarily large $S$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Information-Theoretic Sample Complexity", "weight": 1.0} -->

Given the state-action features, we aim to learn a near-optimal parametrized policy using a small number of samples, which hopefully depends on $K$ but not $S$. Suppose that we are given a *generative model* Kakade where the agent is able to query transition samples and reward from any state-action pair ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$. Such a generative model is commonly available in simulation systems. To this end, we ask how many samples are necessary to obtain an approximate-optimal policy? Our first theorem provides a firm answer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Basic Parametric Q-Learning Method", "weight": 1.0} -->

We develop a Q-learning algorithm for MDP admitting feature representations provided with a generative model.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Given the feature map $\phi:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}^{K}}$, we parameterize the Q-functions, value functions and policies using $w \in {\mathbb{R}}^{K}$ by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm", "weight": 1.0} -->

A scalable learning algorithm should keep track of only the parameters $w$, from which one can decode the high-dimensional value and policy functions according to (1-3).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Algorithm 1 gives a parametric phased Q-learning method. It queries state-action transitions and makes Q-learning-like updates on the parameter $w$. Each iteration picks a small set of state-action pairs $\mathcal{K}$, and performs approximate value iteration on $\mathcal{K}$. The set $\mathcal{K}$ can be picked almost arbitrarily. To obtain a convergence bound, we assume that the state-action pairs in $\mathcal{K}$ cannot be too alike, i.e., the regularity condition (4. ‣ 4.1 Algorithm ‣ 4 A Basic Parametric Q-Learning Method ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")) holds for some value $L > 0$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1 (Representative States and Regularity of Features)", "weight": 1.0} -->

There exists a representative state-action set $\mathcal{K} \subset {\mathcal{S} \times \mathcal{A}}$ with ${|\mathcal{K}|} = K$ and a scalar $L > 0$ such that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1 (Representative States and Regularity of Features)", "weight": 1.0} -->

1: Input: A DMDP ℳ = (𝒮,𝒜,P,r,γ) with a generative model
4: Initialize: $R\leftarrow{\Theta\left\lbrack \frac{\log N}{1 - \gamma} \right\rbrack}$, w ← 0 ∈ ℝK;
7: Pick a representative set 𝒦 ⊂ 𝒮 × 𝒜 satisfying. 10: Obtain $\frac{N}{KR}$ samples {s(j)} i.i.d.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1 (Representative States and Regularity of Features)", "weight": 1.0} -->

from P(⋅|s,a);
11: ${Q\left\lbrack (s,a) \right\rbrack}\leftarrow{\frac{KR}{N}{\sum_{j = 1}^{{N/K}R}{\Pi_{\lbrack 0,{({1 - \gamma})}^{- 1}\rbrack}\left\lbrack {V_{w}\left( s^{(j)} \right)} \right\rbrack}}}$;
12: ⊳ Π[a, b] projects a number onto [a, b]
Algorithm 1 Phased Parametric Q-Learning (PPQ-Learning)

<!-- chunk {"id": "body-0030", "role": "body", "section": "Error Bound and Sample Complexity", "weight": 1.0} -->

We show that the basic parametric Q-learning method enjoys the following error bound.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4 (Policy optimality guarantee)", "weight": 1.0} -->

Our bound applies to $v^{\pi_{w}}$, i.e., the actual performance of the policy $\pi_{w}$ in the real MDP. It is for the $\ell_{\infty}$ norm, i.e., the policy is $\epsilon$-optimal from every initial state. This is the strongest form of optimality guarantee for solving MDP.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 5 (Approximation error due to model misspecification)", "weight": 1.0} -->

When the feature-based transition model is inexact up to $\xi$ total variation, there is an approximation gap in the policy's performance ${O\left\lbrack {L \cdot \xi \cdot \frac{{poly}{\log{({NK\delta^{- 1}})}}}{{({1 - \gamma})}^{3}}} \right\rbrack}.$ It suggests that, even if the observed feature values $\phi{(s,a)}$ cannot fully express the state and action, the Q-learning method can still find approximate-optimal policies. The level of degradation depends on the total-variation divergence between the true transition distribution and its closest feature-based transition model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 6 (Sample complexity of Algorithm 1)", "weight": 1.0} -->

When the MDP is fully realizable under the features, we have $\xi = 0$. Then the number of samples needed for achieving $\epsilon$ policy error is

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 6 (Sample complexity of Algorithm 1)", "weight": 1.0} -->

It is independent of size of the original state space, but depends linearly on $K$. Its dependence on $\frac{1}{1 - \gamma}$ matches the tabular phased Q-learning Kearns and Singh which has complexity $O{(\frac{SA}{{({1 - \gamma})}^{7}\epsilon^{2}})}$ Sidford et al.. Despite the fact that the MDP model has $S \times K$ unknown parameters, the basic parametric Q-learning method can produce good policies even with small data. However, there remains a gap between the current achievable sample complexity (Theorem 2. ‣ 4.2 Error Bound and Sample Complexity ‣ 4 A Basic Parametric Q-Learning Method ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")) and the lower bound (Theorem 1. ‣ 3 Information-Theoretic Sample Complexity ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sample-Optimal Parametric Q-Learning", "weight": 1.0} -->

In this section we will accelerate the basic parametric Q-learning algorithm to maximize its sample efficiency. To do so, we need to modify the algorithm in nontrivial ways in order to take full advantage of the MDP's structure.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Anchor States and Monotonicity", "weight": 1.0} -->

In order to use samples more efficiently, we need to leverage monotonicity of the Bellman operator (i.e., ${\mathcal{T}v_{1}} \leq {\mathcal{T}v_{2}}$ if $v_{1} \leq v_{2}$). However, when the $Q$ function is parameterized as a linear function in $w$, noisy updates on $w$ may easily break the pointwise monotonicity in the $Q$ space. To remedy this issue, we will impose an additional assumption to ensure that monotonicity can be preserved implicitly.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 2 (Anchor State-Action Pairs)", "weight": 1.0} -->

The anchoring $(s_{k},a_{k})$'s can be viewed as "vertices" of the state-action space. They imply that the transition kernel $P$ admits a nonnegative factorization, which can be seen by transforming $\phi$ linearly such that each anchor corresponds to a unit feature vector. This implicit non-negativity is a key to pointwisely monotonic policy/value updates.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2 (Anchor State-Action Pairs)", "weight": 1.0} -->

The notion of "anchor" is a natural analog of the anchor word condition from topic modeling Arora et al. and nonnegative matrix factorization Donoho and Stodden. A similar notion of "anchor state" has been studied in the context of soft state aggregation models to uniquely identify latent meta-states Duan et al.. Under the anchor assumption, without loss of generality, we will assume that $\phi$'s are nonnegative, each $\phi{(s,a)}$ is a vector of probabilities, and there are $K$ anchors with unit feature vectors.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

We develop a sample-optimal algorithm which is implemented in Algorithm 2. Let us explain the features that enable it to find more accurate policies. Some of the ideas are due to Sidford et al., where they were used to develop fast solvers for the tabular MDP.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Parametrization. For the purpose of preserving monotonicity, Algorithm 2 employs a new parametric form. It uses a collection of parameters $\theta = {\{ w^{(i)}\}}_{i = 1}^{Z}$ instead of a single vector, with $Z = {\overset{\sim}{O}{(\frac{1}{1 - \gamma})}}$. The parameterized policy and value functions take the form

<!-- chunk {"id": "body-0041", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Given $\theta$, one can compute ${V_{\theta}{(s)}},{\pi_{\theta}{(s)}}$ by solving an one-step optimization problem. If $a$ takes continuous values, it needs to solve a nonlinear optimization problem.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Computing confidence bounds. In Step 13 and Step 18, the algorithm computes confidence bounds $\epsilon^{(i,j)}$'s for the estimated values of ${PV_{\theta}}.$ These bounds tightly measure the distance from $V_{\theta}$ to the desired solution path, according to probaiblistic concentration arguments. With these bounds, we can precisely shift our estimator downwards so that certain properties would hold (e.g. monotonicity to be explained later) while not incurring additional error.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

We call this property the *monotonicity* property, which together with monotonicity of the Bellman operator guarantees that (by an induction proof)

<!-- chunk {"id": "body-0044", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Algorithm 2 uses two algorithmic tricks to preserve the monotonicity property throughout the iterations. First, the parametric forms of $V_{\theta}$ and $\pi_{\theta}$ (eq.(5.2)) take the maximum across all previous parameters (indexed by $h = {(i,j)}$). It guarantees that $V_{\theta}$ is monotonically improving throughout the outer and inner iterations. Second, the algorithm shifts all the estimated $V_{\theta}$ downwards by a term corresponding to its confidence bound (last equation of Line 13 and Line 18 of Algorithm 2. ‣ 5.1 Anchor States and Monotonicity ‣ 5 Sample-Optimal Parametric Q-Learning ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")). As a result, the estimated expectation is always smaller than the true expected value. By virtue of the nonnegativity (due to Assumption 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

‣ 5.1 Anchor States and Monotonicity ‣ 5 Sample-Optimal Parametric Q-Learning ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features")), the estimate, $\phi{(s,a)}^{\top}{\overline{w}}^{(i,j)}$, of the exact inner product $P{( \cdot |s,a)}^{\top}V^{(i,{j - 1})}$ for arbitrary $(s,a)$ is also shifted downwards. Then we have

<!-- chunk {"id": "body-0046", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

By maximizing the lefthandside over $a$, we see that the monotonicity property is preserved inductively. See Lemma 7. ‣ D.3 Monotonicity Preservation ‣ Appendix D Proof of Theorem 3 ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") for a more detailed proof.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Variance reduction. The algorithm uses an outer loop and an inner loop for approximately iterating the Bellman operator. Each outer iteration performs pre-estimation of a reference vector $PV_{\theta^{(i,0)}}$ (Step 13), which is used throughout the inner loop. For instance, let $\theta^{(i,j)}$ be the parameters at outer iteration $i$ and inner iteration $j$. To obtain an entry $Q^{(i,j)}{(s,a)}$ of the new Q-function, we need to estimate $P{( \cdot |s,a)}^{\top}V_{\theta^{(i,{j - 1})}}$ with sufficient accuracy, so we have

<!-- chunk {"id": "body-0048", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Note that the reference $P{( \cdot |s,a)}^{\top}V_{\theta^{(i,0)}}$ is already approximated with high accuracy in Step 13. This allows the inner loop to successively refine the value and policy, while each inner iteration uses a smaller number of sample transitions to estimate the offset $P{( \cdot |s,a)}^{\top}{(V_{\theta^{(i,{j - 1})}} - V_{\theta^{(i,0)}})}$ (Step 18).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Putting together the preceding techniques, Algorithm 2 performs carefully controlled Bellman updates so that the estimated value-policy functions monotonically improve to the optimal ones. The algorithm contains $R^{\prime} = {\Theta{({\log{\lbrack{\epsilon^{- 1}{({1 - \gamma})}^{- 1}}\rbrack}})}}$ many outer loops.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

Each outer loop (indexed by $i$) starts with a policy ${\|{v^{\ast} - V_{\theta^{(i,0)}}}\|}_{\infty} \lesssim {H/2^{i}}$ and ends with a policy ${\|{v^{\ast} - V_{\theta^{({i + 1},0)}}}\|}_{\infty} \lesssim {H/2^{i + 1}}$.The algorithm takes multiple rounds of mini-batches, where the sample size of each mini-batch is picked just enough to guarantee the accumulation of total error is within $\epsilon$. The algorithm fully exploits the monotonicity property of the Bellman operator as well as the error accumulation in the Markov process (to be explained later in the proof outline).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

1: Input: A DMDP ℳ = (𝒮,𝒜,P,r,γ) with anchor state-action pairs 𝒦; feature map ϕ: 𝒮 × 𝒜 → ℝ; 3: Output: θ ⊂ ℝK with |θ| = Θ [(1−γ)−1 log2ϵ−1] 5: Initialize: R′ ← Θ (log[ϵ−1 (1−γ)−1]), R ← Θ [R′ (1−γ)−1] ⊳ initialize the numbers of iterations 6: ${\{ w^{(i,j)},\epsilon^{(i,j)},{\overline{w}}^{(i,j)}\}}_{{i \in {\lbrack 0,R^{\prime}\rbrack}},{j \in {\lbrack 0,R\rbrack}}} \subset {\mathbb{R}}^{K}$ as 0 vectors ⊳ initialize parameters 7: $m\leftarrow{C \cdot \frac{1}{\epsilon^{2}} \cdot

<!-- chunk {"id": "body-0052", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

\frac{\log{(R^{\prime}RK\delta^{- 1})}^{4/3}}{{({1 - \gamma})}^{3}}}$, ⊳ mini-batch size for outer loop $m_{1}\leftarrow{C \cdot \frac{\log{({R^{\prime}RK\delta^{- 1}})}}{{({1 - \gamma})}^{2}}}$ for some constant C; ⊳ mini-batch size for inner loop 8: θ ← {0} ⊂ ℝK ⊳ initialize the output to contain a single 0-vector 13: Obtain state samples xk, xk, …, xk(m) ∈ 𝒮 from P(⋅|sk,ak) for (sk,ak) ∈ 𝒦. Let

<!-- chunk {"id": "body-0053", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

⊳ estimate of the confidence bound of the emprical estimator w(i,0)

<!-- chunk {"id": "body-0054", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

← max {0,min {w(i,0) (k) − ϵ(i,0) (k),(1−γ)−1}} ⊳ shift and clip the estimate

<!-- chunk {"id": "body-0055", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

18: Obtain state samples xk, xk, …, xk(m1) ∈ 𝒮 from P′(⋅|sk,ak) for (sk,ak) ∈ 𝒦. Let

<!-- chunk {"id": "body-0056", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

← max {0,min {w(i,j) (k) − ϵ(i,j) (k),(1−γ)−1}} ⊳ shift and clip the estimate

<!-- chunk {"id": "body-0057", "role": "body", "section": "Achieving The Optimal Sample Complexity", "weight": 1.0} -->

20: $\theta^{(i,j)}\leftarrow{\theta^{(i,{j - 1})} \cup {\{{\overline{w}}^{(i,j)}\}}}$ ⊳ attach the newly estimated parameter to θ
22: θ(i + 1,0) ← θ(i,R) ⊳ prepare the next outer loop
Algorithm 2 Optimal Phased Parametric Q-Learning (OPPQ-Learning)

<!-- chunk {"id": "body-0058", "role": "body", "section": "Optimal Sample Complexity Guarantee", "weight": 1.0} -->

In this section, we analyze the sample complexity of the algorithm provided in the last section.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 7 (Sample Optimality of Algorithm 2)", "weight": 1.0} -->

Theorem 3. ‣ 5.3 Optimal Sample Complexity Guarantee ‣ 5 Sample-Optimal Parametric Q-Learning ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") matches the information-theoretic lower bound of Theorem 1. ‣ 3 Information-Theoretic Sample Complexity ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") up to polylog factors with respect to all parameters $S,A,K,\epsilon,{1 - \gamma}$ (note that Theorem 1. ‣ 3 Information-Theoretic Sample Complexity ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") still holds under the anchor restriction). Therefore it is a sample-optimal method for solving the feature-based MDP. No other method can outperform it by more than polylog factors.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 8 (About Anchor State-Actions)", "weight": 1.0} -->

The proof of Theorem 3. ‣ 5.3 Optimal Sample Complexity Guarantee ‣ 5 Sample-Optimal Parametric Q-Learning ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") relies on the anchor assumption. The monotonicity property can be preserved because the anchor state-action pairs imply an implicit non-negative factorization of the transition kernel. The convex combination property of anchor state-actions is used in analyzing the error accumulation, needed by the conditional law of total variance. Anchor condition is commonly believed to be a key to identifying nonnegative models; see for example Donoho and Stodden. We believe this is the first observation that it also relates to sample-optimal reinforcement learning.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 8 (About Anchor State-Actions)", "weight": 1.0} -->

Note that it is possible that the number of anchors is greater than the number of features $K$, then one can append new (dependent) features to make them equal. In this sense Assumption 2. ‣ 5.1 Anchor States and Monotonicity ‣ 5 Sample-Optimal Parametric Q-Learning ‣ Sample-Optimal Parametric Q-Learning Using Linearly Additive Features") always holds and the actual sample complexity depends on the number of anchors (instead of features). In addition, the anchors can be pre-computed as long as the $\phi$ feature map is known.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 9 (Significance of ${({1 - \\gamma})}^{- 4}$ Improvement)", "weight": 1.0} -->

Let us compare the sample complexities of Algorithms 1, 2. They differ by a multiplicative gap ${({1 - \gamma})}^{- 4}$. Recall that $\gamma \in {}$ is the discount factor. One can view ${({1 - \gamma})}^{- 1} = {1 + \gamma + \gamma^{2} + \cdots}$ as an approximate horizon. If $\gamma = 0.99$, the MDP essentially has $100$ time steps, and

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 9 (Significance of ${({1 - \\gamma})}^{- 4}$ Improvement)", "weight": 1.0} -->

i.e., Algorithm 2 is $10^{8}$ times faster. It only needs a tiny portion ($1/10^{8}$) of the samples as needed by the basic algorithm. We see that clever algorithmic usage of monotonicity and variance structures of the MDP saves big.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Related Literatures", "weight": 1.0} -->

There is a body of works studying the sample complexity of tabular DMDP (i.e., the finite-state finite-action case without structural knowledge). Sample-based algorithms for learning value and policy functions have been studied in Kearns and Singh; Kakade; Singh and Yee; Azar et al.; Sidford et al. and many others. Among these papers, Azar et al. obtains the first tight sample bound for finding an $\epsilon$-optimal value function, Sidford et al. obtains the first tight sample bound for finding an $\epsilon$-optimal policy; both complexities are of the form $\overset{\sim}{O}{\lbrack{{|\mathcal{S}|}{|\mathcal{A}|}{({1 - \gamma})}^{- 3}}\rbrack}$. Lower bounds have been shown in Azar et al.; Even-Dar et al. and Azar et al..

<!-- chunk {"id": "body-0065", "role": "body", "section": "Related Literatures", "weight": 1.0} -->

Our result is relevant to the large body of works using linear models and basis functions to approximate value and Q functions. For instance, Tsitsiklis and Van Roy; Nedić and Bertsekas; Lagoudakis and Parr; Melo et al.; Parr et al.; Sutton et al.; Lazaric et al.; Tagorti and Scherrer and Maei et al. studies both policy evaluation and optimization by assuming values are from a linear space. Tsitsiklis and Van Roy studied the convergence of the temporal-difference learning algorithm for approximating the value function for a fixed policy. Nedić and Bertsekas studies the policy evaluation problem using least square. Parr et al. studies the relationships of using linear functions to represent values and to represent transition models. Melo et al. studies the almost sure convergence of $Q$-learning-like methods using linear function approximation. Sutton et al. shows off-policy temporal-difference learning is convergent with linear function approximation. These earlier works primarily focused on convergence using linear function approximation, without analyzing the sample complexity.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Related Literatures", "weight": 1.0} -->

Fitted value iteration (VI) applies to more general function approximators of the value function Munos and Szepesvári; Antos et al.; Farahmand et al.; Antos et al., where $v$ is approximated within a low-dimensional function space $\mathcal{F}$. They have shown that the error of the fitted-VI is affected by the Bellman error of the space $\mathcal{F}$. Their result applies to a general set of functional spaces, where the statistical error depends on a polynomial of ${1/\epsilon},{1/{({1 - \gamma})}}$ and the intrinsic dimension of the functional space. It appears that their result works for the $\ell_{p}$ norm of the policy error, which is proportional to $\epsilon^{- {\Theta{(p)}}}$ with high probability. Their result does not apply to the $\ell_{\infty}$ policy error which is the focus of the current paper.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Related Literatures", "weight": 1.0} -->

More recently, Lazaric et al.; Tagorti and Scherrer analyzes the sample complexity of temporal difference least square for evaluating a fixed policy. Recently, a work by Jiang et al. studies the case when a form of Bellman error' is decomposable and has a small rank. They show that the number of trajectories needed depends on the Bellman rank rather than the number of states. Chen et al. proposes a primal-dual method for policy learning that uses linear models and state-action features for both the value and state-action distribution. To our best knowledge, there is no existing result that solves the linear-model MDP with provable-optimal sample complexity.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remarks", "weight": 1.0} -->

The paper studies the information-theoretic sample complexity for solving MDP with feature-based linear transition model. It provides the first sharp sample complexity upper and lower bounds for learning the policy using a generative model. It also provides a sample-optimal parametric Q-learning method that involves computing confidence bounds, variance reduction and monotonic improvement. We hope that establishing sharp results for the basic linear model would shed lights on more general structured models and motivate faster solutions.
