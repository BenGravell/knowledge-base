<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms

Topics include Reinforcement learning, Inverse reinforcement learning, Datasets, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide new perspectives and inference algorithms for Maximum Entropy (MaxEnt) Inverse Reinforcement Learning (IRL), which provides a principled method to find a most non-committal reward function consistent with given expert demonstrations, among many consistent reward functions. We first present a generalized MaxEnt formulation based on minimizing a KL-divergence instead of maximizing an entropy. This improves the previous heuristic derivation of the MaxEnt IRL model (for stochastic MDPs), allows a unified view of MaxEnt IRL and Relative Entropy IRL, and leads to a model-free learning algorithm for the MaxEnt IRL model. Second, a careful review of existing inference algorithms and implementations showed that they approximately compute the marginals required for learning the model. We provide examples to illustrate this, and present an efficient and exact inference algorithm. Our algorithm can handle variable length demonstrations; in addition, while a basic version takes time quadratic in the maximum demonstration length L, an improved version of this algorithm reduces this to linear using a padding trick. Experiments show that our exact algorithm improves reward learning as compared to the approximate ones. Furthermore, our algorithm scales up to a large, real-world dataset involving driver behaviour forecasting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an optimized implementation compatible with the OpenAI Gym interface. Our new insight and algorithms could possibly lead to further interest and exploration of the original MaxEnt IRL model.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse Reinforcement Learning (IRL) searches for a reward or cost function to rationalize observed behaviour. This is challenging because the same reward may be optimized by different behaviors, and optimizing different reward functions can lead to the same behavior. In their seminal work Ziebart et al. developed a principled solution using the Maximum Entropy (MaxEnt) principle to choose the most non-committal consistent reward -- i.e. a reward which matches demonstrated feature counts but makes no additional assumptions about the demonstrated behaviour. Variations of this idea have seen great success in many recent works --- including models based on causal entropy, and efficient sample-based methods that maximize state-conditioned policy entropy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the long line of works based on the original MaxEnt IRL paper, we believe that the full value of the original MaxEnt IRL model might not have been fully realized yet, for two reasons. First, while the MaxEnt IRL model for deterministic Markov Decision Processes (MDPs) has been rigorously derived from the MaxEnt principle, the corresponding model for stochastic MDPs was based on a heuristic argument. While this has motivated alternative formulations such as causal Maximum Causal Entropy (MaxCausalEnt) IRL, we were also interested to know whether there is a simple and rigorous justification of the MaxEnt IRL model for stochastic MDPs, which might bring new insight. Second, the published inference (i.e., marginal computation) algorithms for MaxEnt IRL only approximately compute the marginals required for learning -- as confirmed by the original authors.^11^1Personal correspondence with B. Ziebart. Existing implementations online have largely followed these algorithms and are approximate. While approximate algorithms are often sufficient for achieving good generalization performance, we are interested in developing exact algorithms in this case, and study whether they can achieve better reward learning than approximate algorithms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the above questions, we revisit the MaxEnt IRL model and present some new perspectives, algorithms, and empirical insights.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a simple and rigorous derivation of the original MaxEnt IRL model using the Kullback-Liebler divergence, without using any heuristic argument. Our derivation provides a unified view for MaxEnt IRL and relative entropy IRL, and highlights a key difference between these two frameworks. In addition, the connection between them suggests an model-free importance sampling algorithm for learning a MaxEnt IRL model (Section 4).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present an efficient exact forward-backward inference algorithm. This allows exact computation of the gradients used in reward learning. Unlike previous work, our algorithm does not assume that the demonstrations are of the same length. While this increases the time complexity from linear in $L$ to quadratic in $L$, we bring the time complexity back to linear in $L$ using a padding trick (Section 5).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We illustrate that published MaxEnt IRL algorithms are approximate, and empirically show that exact algorithms improve reward learning. In addition, we show that our algorithm can scale up to a large, real-world dataset involving driver behaviour forecasting (Section 9).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide an open-source optimized reference implementation of our algorithms to allow easy application to other problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we conclude with a discussion on opportunities for future work (Section 10).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

We consider IRL in the context of an MDP $\mathcal{M} = {\{\mathcal{S},\mathcal{A},p_{0},T,\gamma,R\}}$, with discrete states $s \in \mathcal{S}$, discrete actions $a \in \mathcal{A}$, starting state distribution $p_{0}{(s)}$, transition dynamics $T = {p{({s' \mid {s,a}})}}$, a discount factor $\gamma \in {\lbrack 0,1)}$, and a reward function denoted $R$, which we define in further detail below.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

For episodic MDPs, we also designate the non-empty sub-set of MDP states that are terminal $\mathcal{S}^{T} \subseteq \mathcal{S}$. I.e. encountering any terminal state $s^{T} \in \mathcal{S}^{T}$ grants the agent reward for encountering that state $R{(s^{T})}$, but then immediately ends the episode of interaction with the MDP. This has important implications for the process by which we assume the IRL dataset is generated -- as we show below.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

A policy $\pi{({a \mid s})}$ provides a (possibly deterministic) mapping from states to actions and describes a strategy to navigate the MDP. We denote a 'sample' from a policy as a state-action trajectory ending with a state $\tau = {({(s_{1},a_{1})},\ldots,{(s_{m},\text{None})})}$, with length denoted by $|\tau|$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

For convenience, we also denote ${\mathcal{P}{(s')}} \triangleq {\{{(s,a)}:{{T{(s,a,s')}} > 0}\}}$ as the set of $(s,a)$ tuples that are valid *parents* of the state $s'$ according to the MDP dynamics, and ${\mathcal{C}{(s)}} \triangleq {\{{(a,s')}:{{T{(s,a,s')}} > 0}\}}$ as the set of $(a,s')$ tuples that are valid *children* of the state $s$ according to the MDP dynamics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

In general, the domain of a reward function could be the set of states $R_{s}{(s)}$, or state-action pairs $R_{sa}{(s,a)}$, or state-action-state tuples $R_{sas'}{(s,a,s')}$. In the interests of completeness and accuracy, the derivations in the following sections proceed with the most general reward structure possible -- i.e. we allow for MDPs that include any combination of these reward function types. Furthermore, we limit our focus to linear reward functions with known basis feature functions, i.e. where we will drop the subscripts for brevity when context provides the needed clarity. E.g. to transform one of our algorithms below to the case of an MDP that contains only state-action rewards, the reader could simply substitute $\theta_{s} = 0$ and $\theta_{sas'} = 0$, then simplify all the equations that contain these terms.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

We also define the application of a reward function to a trajectory (taking into account discounting) as follows; where we have defined In our IRL setting, we are provided with a set of demonstration trajectories $\mathcal{D} = {\{\tau_{1},\ldots,\tau_{N}\}}$, and a partial MDP definition $\mathcal{M}\backslash R$ -- i.e. we know the MDP dynamics, but not the reward function parameter(s) $\Theta = {\{\theta_{s},\theta_{sa},\theta_{sas'}\}}$. The goal is to identify these parameter vectors such that the demonstration data appear 'optimal' according to some criteria (e.g. maximizing cumulative $\gamma$-discounted rewards).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

We make no assumption that the demonstrated paths $\mathcal{D}$ are of equal lengths -- e.g. this can occur naturally in stochastic episodic MDPs where we assume some exogenous process allows the agent to re-start episodes after encountering a terminal state. On the other hand, in a continuing (non-episodic) MDP, the demonstration data should technically consist of one continuous trajectory of interaction data, however we allow that there may be some exogenous process by which the episode of interaction can be terminated at any point and re-started -- a common practice in Reinforcement Learning experiments. Thus, in both the episodic and non-episodic cases, we must be prepared to handle data with trajectories of varying lengths. As we discuss below, previous MaxEnt IRL algorithms only supported datasets where the trajectories are all the same length -- a key limitation that we address in this chapter.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Returning to the general problem statement of Inverse Reinforcement Learning, showed that for an MDP with linear rewards, to learn a policy $\pi$ with the same value as the demonstrator, it suffices to match *feature expectations*, i.e., choose parameters $\Theta$ that induce a policy $\pi$ such that where the RHS are empirical expectations over the demonstration data. While a useful starting point, this problem is ill-posed, because generally, many polices have matching feature expectations. The problem is further complicated by the fact that positive-affine reward 'shaping' transformations do not change the optimal policy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Inverse Reinforcement Learning", "weight": 1.0} -->

Early IRL methods generally relied on heuristics or probabilistic assumptions to resolve the ambiguity of a consistent reward. On the other hand, the Maximum Entropy IRL approach provides a principled way to identify unique reward parameters.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Principle of Maximum Entropy", "weight": 1.0} -->

The MaxEnt IRL model defines a distribution on the set $\mathcal{T}$ of all feasible trajectories as where $q$ is the (un-normalized) distribution induced by MDP dynamics alone is the normalizing constant often known as the partition function. In addition, the parameters $\Theta$ are chosen to maximize the log-likelihood given $\mathcal{D}$, We can interpret $p_{\Theta}{(\tau)}$ as a non-stationary policy, which is more expressive than a stationary policy as it can vary over time-steps. Furthermore, the MaxEnt IRL framework allows all possible behaviors to be jointly learned due to global normalization. This makes it potentially more powerful in complex domains, as compared to models which learn a stationary policy or do not perform global normalization.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Principle of Maximum Entropy", "weight": 1.0} -->

The feature moment matching constraints ensure the learned non-stationary policy $p$ will match the preferences demonstrated in the data, while the minimization objective forces the model close to the natural dynamics of the MDP. This leads to a unique reward parameter solution, thus resolving the reward ambiguity problem. Our proof is straight-forward, and similar in nature to that for RE-IRL.

<!-- chunk {"id": "body-0023", "role": "body", "section": "New Algorithm", "weight": 1.0} -->

To learn the MaxEnt IRL model in Eq. 10, we need to maximize the log-likelihood, which is convex in $\Theta$ and thus can be maximized using standard gradient-based methods --- in our experiments we used L-BFGS-B. The value and the gradient of the log-likelihood, required in the optimization algorithm, can be computed using the partition function $Z{(\Theta)}$ and the marginal distributions $p_{\Theta,t}{(s)}$, $p_{\Theta,t}{(s,a)}$, and $p_{\Theta,t}{(s,a,s')}$, which denote the probability that the $t$-th state / state-action / state-action-state are $s$, $(s,a)$, or $(s,a,s')$ respectively when $\tau$ is sampled from the MaxEnt distribution $p_{\Theta}{(\tau)}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "New Algorithm", "weight": 1.0} -->

Specifically, with the partition function, we can easily compute the log-likelihood using Eq. 10. On the other hand, with the marginals terms, the required gradients are given, Explicit computation of the partition function and marginals grows exponentially in time for longer demonstration paths, however the Markov property of the MDP allows us to decompose the partition and marginal feature values recursively with an efficient forward-backward algorithm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "New Algorithm", "weight": 1.0} -->

This was previously discussed, and in an updated version of that paper, however their algorithm relied on a heuristic for the case of stochastic MDPs. We find that this leads to approximate gradients (see proofs in LABEL:App:MaxEnt) and negatively impacts the reward learning process (see experiments in Section 9). We also note that these algorithms were derived only for the case of un-discounted MDPs with state-based rewards --- our algorithm adds support for discounted MDPs, and for MDPs with reward functions consisting of any combination of state-, state-action, and/or state-action-state features.

<!-- chunk {"id": "body-0026", "role": "body", "section": "New Algorithm", "weight": 1.0} -->

Complementing and extending these previous works, we construct a novel dynamic program that computes MaxEnt IRL gradients that are exact, even for the case of stochastic MDPs. The algorithm utilizes partial versions of the partition function, known as message-passing variables, which we describe below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "An intuition for message-passing algorithms", "weight": 1.0} -->

To illustrate the derivation of our dynamic program, it is helpful to consider an example MDP with four states and a single action Fig. 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An intuition for message-passing algorithms", "weight": 1.0} -->

The set of paths of length $l = 4$ contains a single path, Inspecting the partition contribution from this path, it is evident that we can decompose this term into three components: a 'prefix' that ends with the state $s_{2}$, the central $(s_{2},a,s_{3})$ tuple, and a 'suffix' that begins with the state $s_{3}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "An intuition for message-passing algorithms", "weight": 1.0} -->

The same prefix-suffix pattern holds true when expressing the partition contribution for any path in a general MDP, however the prefix and suffix must sum over *all* possible paths leading up to, or away from the central transition tuple. Specifically, for a set of paths of lengths exactly $l$, the marginal state-action probability for a tuple $(s,a,s')$ occuring a time step $t$ will consist of three components: A path prefix counting the probability mass for all length $t$ paths that end at $s$ The actual probability of the $(s,a,s')$ event A suffix counting the probability mass for all length $l - t$ paths beginning with $s'$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "An intuition for message-passing algorithms", "weight": 1.0} -->

The prefix (suffix) term is known in the dynamic programming literature as the forward (backward) message-passing variable, as it functions to pass probability 'messages' forward (backward) to (from) the central transition tuple. Below, we show that for the Maximum Entropy behaviour model, the forward and backward message passing variables exhibit recursive sub-structure, which allows computing them efficiently with a dynamic program.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Forward message passing variable", "weight": 1.0} -->

We assume all trajectories in $\mathcal{T}$ have length at most $L$. We define a forward message-passing variable that computes the partition contribution for paths of length $l$ that *end* at a given state $s$, Un-rolling this definition (i.e. fixing a base-case and re-writing the recurrence accordingly) leads to an expression for $\alpha_{l}{(s)}$,

<!-- chunk {"id": "body-0032", "role": "body", "section": "Backward message passing variable", "weight": 1.0} -->

We define an analogous backward message-passing variable which counts the partition contribution for length $t$ suffixes within paths of total length $l$, where the path suffix *starts* at a given state $s$, where ${q'{(\tau)}} \triangleq {\prod_{t = 1}^{{|\tau|} - 1}{T{(\left. s_{t + 1} \middle| {s_{t},a_{t}} \right.)}}}$ is the same as $q{(\tau)}$, but does not include the starting state distribution. Un-rolling the definition of $\beta_{l,t}{(s)}$ gives an analogous recurrence;

<!-- chunk {"id": "body-0033", "role": "body", "section": "Partition and marginal calculations", "weight": 1.0} -->

Now we describe the dynamic program to compute the terms of interest. For a set of paths of lengths $1 \leq l \leq L$ the partition function value is given by summing the backward message passing values, and the marginal distributions are given, Before continuing, we briefly illustrate the function of these equations with a simple example.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Worked Example", "weight": 1.0} -->

24 and 25, ${\alpha_{l}{(s)}} = \left\{ \begin{matrix} On the other hand, the backward message passing variable $\beta_{l,t}{(s)}$ must be computed for $1 \leq l \leq L = 4$, and for $1 \leq t < l$. These terms are given by Eqs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Worked Example", "weight": 1.0} -->

27 and 28. For length one paths ($l = 1$), ${\beta_{1,t}{(s)}} = \left\{ \begin{matrix} \end{matrix} \right.$ t = 1 s1 eR (s1) s2 eR (s2) s3 eR (s3) s4 eR (s4) For length two paths ($l = 2$), ${\beta_{2,t}{(s)}} = \left\{ \begin{matrix} For length three paths ($l = 3$), ${\beta_{3,t}{(s)}} = \left\{ \begin{matrix} And for length four paths ($l = 4$), ${\beta_{4,t}{(s)}} = \left\{ \begin{matrix} We are now able to sum the forward message $\alpha_{l}{(s)}$ to compute the partition function value (Eq. 29), Recalling that $\mathcal{T} = \mathcal{D}$ in our example, and

<!-- chunk {"id": "body-0036", "role": "body", "section": "Worked Example", "weight": 1.0} -->

comparing with the set of paths (Eq. 33), we can see that the partition value correctly accounts for the contributions of each of the four paths in $\mathcal{T}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Worked Example", "weight": 1.0} -->

We can then use the message passing variables to compute the marginal terms (Eqs. 30, 31 and 32), where all $t,s,a,s'$ combinations that are not shown are equal to $0$, and intermediate exponential values have been collapsed $(\ldots)$ for brevity. The attentive reader can compare the values computed above with the columns of the partition value calculated in LABEL:eq:example-partition to confirm that the marginals correctly count all path contributions for each $t,s,a,s'$ combination.

<!-- chunk {"id": "body-0038", "role": "body", "section": "More Efficient Algorithm", "weight": 1.0} -->

We now introduce a way to augment episodic and continuing MDPs (and their associated datasets of IRL demonstrations) so that all demonstrations will be of the same length, but the reward parameters learned using our Maximum Entropy IRL algorithm are unchanged. This augmentation (a so-called 'padding trick') has the effect of transforming an episodic MDP to a continuous MDP in a way which means that the demonstration trajectories from agents can all be 'extended' until they all reach some upper length $L$. This is done by adding a new state and action to the MDP, which form a recurrent sub-set of the state-action space of the MDP -- and by updating the transition dynamics and reward structure so that the corresponding Maximum Entropy probability distribution over trajectories is unchanged. Using this approach we are able to transform the dataset of trajectories of varying lengths to a dataset of trajectories of a single fixed size -- which allows a reducing the computational complexity of our MaxEnt IRL dynamic program without changing the value of the calculated partition function or marginals.

<!-- chunk {"id": "body-0039", "role": "body", "section": "A padding trick for episodic and continuing MDPs", "weight": 1.0} -->

Specifically, we augment the MDP by introducing an auxiliary state $s_{a}$ and action $a_{a}$. To keep the derivation clear, we incorporate these elements into our existing notation as follows: We illustrate the hierarchy of state and action sets in Figs. 2(a) and 2(b) ‣ Figure 2 ‣ 6.1 A padding trick for episodic and continuing MDPs ‣ 6 A More Efficient Algorithm ‣ Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms").

<!-- chunk {"id": "body-0040", "role": "body", "section": "A padding trick for episodic and continuing MDPs", "weight": 1.0} -->

Our padding method requires that the auxiliary state and action satisfy the following properties vis-á-vis the dynamics of the augmented MDP; The agent may not start in the auxiliary state $s_{a}$ The auxiliary state $s_{a}$ is absorbing The auxiliary action always transitions deterministically to the auxiliary state Terminal states transition to the auxiliary state no matter what action is taken These rules also imply the following updates to the *Child set* and *Parent set* operators.

<!-- chunk {"id": "body-0041", "role": "body", "section": "A padding trick for episodic and continuing MDPs", "weight": 1.0} -->

*All* states (including terminal states and the auxiliary state) now feature the auxiliary action and state state in their children set The auxiliary state contains all states (including itself) in it's parent set The auxiliary state contains only the auxiliary action and state in it's child set Terminal states now have a child set spanning each of the set of all actions, followed by the auxiliary state E.g. returning to the example of the linear MDP from Fig. 1, the updated MDP transition structure is as follows (note that $s_{4}$, which was formerly terminal, now has a successor state -- $s_{a}$); Figure 3: The linear MDP from Fig. 1, after augmentation with the padding trick. Elements added as part of the padding trick are indicated in dashed lines and/or grey shading. Note that s4 is no longer a terminal state.

<!-- chunk {"id": "body-0042", "role": "body", "section": "A padding trick for episodic and continuing MDPs", "weight": 1.0} -->

To complete the padding trick we must update the reward function in a way that will not modify the reward which is learned under the Maximum Entropy IRL model. The requisite reward function changes are outlined in Tables 1(a), 1(b) ‣ Table 1 ‣ 6.1 A padding trick for episodic and continuing MDPs ‣ 6 A More Efficient Algorithm ‣ Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms") and 1(c) ‣ Table 1 ‣ 6.1 A padding trick for episodic and continuing MDPs ‣ 6 A More Efficient Algorithm ‣ Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms"). Essentially, these changes serve to infinitely discourage any actions that were impossible in the original MDP (e.g. executing actions in $\mathcal{A}$ after a terminal state), however allow the agent to transition to the auxiliary state at any point in time without incurring any modification to their gained reward.

<!-- chunk {"id": "body-0043", "role": "body", "section": "A padding trick for episodic and continuing MDPs", "weight": 1.0} -->

Once the MDP definition has been updated to incorporate the auxiliary state and action, we can adjust the demonstration dataset to allow for a more efficient MaxEnt IRL algorithm, while still computing exact gradients. The updates required for the demonstration trajectories are as follows.

<!-- chunk {"id": "body-0044", "role": "body", "section": "A padding trick for episodic and continuing MDPs", "weight": 1.0} -->

For all sequences shorter than the longest demonstration path length $L = {\max_{\tau \in \mathcal{D}}{|\tau|}}$, we pad them with auxiliary actions and states $({(\cdot,a_{a})},{(s_{a}, \cdot)})$ until the sequence length is $L$. For example, a ${|\tau|} = 2$ sequence would be padded to length $L = 4$ as follows; Once all demonstrations in the data $\mathcal{D}$ are padded to the same length $L$, we can apply a simplified forward-backward algorithm to calculate the partition value exactly, but with better computational space and time complexity. We describe this algorithm now.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Padded message passing variables", "weight": 1.0} -->

The forward message passing variable $\alpha_{l}{(s)}$ is computed as before, for all lengths $1 \leq l < L$ and for states $s \in \mathcal{S}$ (Eqs. 24 and 25) -- n.b. we do not need to bother computing $\alpha_{l}{(s_{a})}$ because these terms are not needed in the partition and marginal calculations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Padded message passing variables", "weight": 1.0} -->

The backward message passing variable $\beta_{l,t}{(s)}$ still needs to be computed for suffix lengths $1 \leq t < l$, however due to the padded sequences, we can fix $l = L$, removing one level of iteration. We therefore drop the $l$ prefix and denote this term with the $t$ prefix only -- i.e. $\beta_{t}{(s)}$, and compute this for states $s \in \mathcal{S}^{+}$. N.b.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Padded message passing variables", "weight": 1.0} -->

we *will* need the terms $\beta_{t}{(s_{a})}$, as they appear within the backward message recurrence and marginal calculations, however a simple inspection of Tables 1(a), 1(b) ‣ Table 1 ‣ 6.1 A padding trick for episodic and continuing MDPs ‣ 6 A More Efficient Algorithm ‣ Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms") and 1(c) ‣ Table 1 ‣ 6.1 A padding trick for episodic and continuing MDPs ‣ 6 A More Efficient Algorithm ‣ Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms") shows that ${\beta_{t}{(s_{a})}} = {1{\forall t}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Padded partition and marginal calculations", "weight": 1.0} -->

With the padded MDP formulation, the partition function is unchanged (Eq. 29), however we note that the inner summand is over the set $\mathcal{S}$, which does *not* include the auxiliary state, but *does* include states that were terminal states before the padding trick was applied.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Padded partition and marginal calculations", "weight": 1.0} -->

The update for state marginal distributions no longer needs a summand over variable suffix lengths, thus reducing the time complexity. That is, which must be computed for states ${s \in \mathcal{S}},{{a \in \mathcal{A}},{s' \in \mathcal{S}}}$ i.e. everything but the auxiliary state and action. We also draw the reader's attention to the fact that the summand over child tuples in Eq. 48 *does* include auxiliary action and state tuples, while the state summand in Eq. 49 does *not* include auxiliary states.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Padded partition and marginal calculations", "weight": 1.0} -->

We now briefly return to the example MDP to illustrate the consistency of the two dynamic programs.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Worked Example Revisited", "weight": 1.0} -->

We return to the example MDP from Figs. 1 and 3 to demonstrate that the dynamic program with the padding trick faithfully computes the same values as the full dynamic program, while requiring less storage and time.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Worked Example Revisited", "weight": 1.0} -->

The path set $\mathcal{T}$ still consists of four paths, however the paths are now padded to be of equal length as follows; The recurrence for the forward message (Eq. 25) sums over parents of states $s \in \mathcal{S}$, which is exclusive of the auxiliary state $s_{a}$, therefore the computed forward message values are unchanged.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Worked Example Revisited", "weight": 1.0} -->

The backward message $\beta_{t}{(s)}$ is computed for $s \in \mathcal{S}^{+}$, as follows; ${\beta_{t}{(s)}} = \left\{ \begin{matrix} As the forward message is unchanged, the calculated value for the partition function will also be unchanged.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Worked Example Revisited", "weight": 1.0} -->

Finally, we compute the marginal terms for ${s \in \mathcal{S}},{{a \in \mathcal{A}},{s' \in \mathcal{S}}}$ as follows, where all $t,s,a,s'$ combinations that are not shown are equal to $0$, and once again the intermediate exponential values have been collapsed $(\ldots)$ for brevity. After re-arranging terms, the reader can verify that the computed marginal terms are indeed identical to those values calculated using the original dynamic program, thus concluding our demonstration.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Implementation Comments", "weight": 1.0} -->

A naïve implementation of *any* MaxEnt algorithm may exhibit numerical floating-point overflow due to repeated exponentiation of rewards, especially for large positive reward values and/or long trajectories. This can be avoided by using (natural) log-space variables and the standard '$\log$-$sum$-$\exp$' transform when implementing the algorithm. E.g.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Implementation Comments", "weight": 1.0} -->

Finally, note that with appropriate modifications to the children and parent set operators $\mathcal{C}{(s)}$ and $\mathcal{P}{(s)}$, our algorithms are also able to generalize to MDPs with state-dependent action sets $\mathcal{A} = {\bigcup_{s \in \mathcal{S}}{\mathcal{A}{(s)}}}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Implementation Comments", "weight": 1.0} -->

We provide an optimized reference implementation of this algorithm as a Python 3.6.9 package at our open-source code repository^22^2 Our implementation utilizes the Numba Just-In-Time optimizing compiler to achieve highly performant vectorized machine code for critical functions.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Inference with the Maximum Entropy Behaviour Distribution", "weight": 1.0} -->

After reward learning (i.e. discovering the parameters for $p_{\Theta}{(\tau)}$), the maximum likelihood path between two states (or state-distributions) can be found using a Viterbi type dynamic program that has polynomial time complexity. If we denote the $i$-th state within a trajectory as $\tau^{(i)}$, and use $i = {- 1}$ to denote the final state of a trajectory, this corresponds to solving the following optimization problem, | | $\underset{\tau \in \mathcal{T}}{\arg\max}$ | $p_{\Theta}{(\tau)}$ | | \(53\) | for given (possibly degenerate) distributions $f$ and $g$. In the special case when the learned weights are such that all $(s,a)$ choices incur a reward less than or equal to zero, any weighted shortest path search algorithm can be used (e.g. Dijkstra's or Bellman-Ford), reducing the complexity for the problem of path inference conditioned on states.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Inference with the Maximum Entropy Behaviour Distribution", "weight": 1.0} -->

We omit these algorithm for brevity, but refer the reader to our project repository.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Inference with the Maximum Entropy Behaviour Distribution", "weight": 1.0} -->

On the other hand, we may wish use the learned maximum entropy path distribution to perform state inference, conditioned on partial paths. E.g. show how Bayes' theorem can be applied to elegantly infer a distribution over destination states given an observation of the first few $(s,a)$ tuples in a trajectory. If we extend our notation from above to use $\tau^{({A\rightarrow B})}$ to denote a path from state $s_{A}$ to state $s_{B}$, then we have the following useful result, where $p{(s_{G})}$ is a prior distribution over destinations. This can be used to rank possible destination states and/or to provide a distribution over expected path lengths -- all of which may be useful in planning or navigation type problems.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Inference with the Maximum Entropy Behaviour Distribution", "weight": 1.0} -->

These examples serve to illustrate the some of benefits of performing reward learning in the context of a distribution over behaviours, rather than an action-based distribution, as in some other IRL schemes.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We verify the function of our algorithm using several synthetic MDPs from the OpenAI Gym library, and demonstrate our algorithm's scalability with a large real-world problem in driver behaviour forecasting.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

First, we verify empirically that the reward function our algorithm learns becomes more accurate as the number of demonstration paths increases.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

As a metric for IRL algorithm performance, we choose the Inverse Learning Error (ILE), first proposed. The ILE measures the quality of a learned reward function $R_{\text{L}}$ by comparing it with the ground truth reward $R_{\text{GT}}$ --- however, naïve comparison of reward values is meaningless due to the reward ambiguity problems discussed in Section 3. Instead, ILE compares *value* of the ground truth optimal policy, with the *value* of the optimal policy w.r.t. the learned reward. The ILE is given, where ${\mathbf{v}}{(\pi)}$ indicates the vector of state-values w.r.t. the *ground truth* reward $R_{\text{GT}}$ for any arbitrary policy $\pi$, and $\pi_{R_{\text{GT}}}^{\ast}$ and $\pi_{R_{\text{L}}}^{\ast}$ denote the optimal policy w.r.t. the ground truth and learned reward functions respectively.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

Note that the ILE is on the range $\lbrack 0,\infty)$, where lower values indicate a closer match to the ground truth reward, and the upper bound is specific to each MDP.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

We evaluated the quality of our algorithm's learned rewards on three discrete state- and action space problems from the OpenAI Gym library (shown in Table 2). For each environment, we find the optimal stationary deterministic policy using value iteration, then sample demonstration datasets containing an increasing number of paths. For each dataset, we learn a reward function, then compute the corresponding ILE. Each experiment is repeated 50 times to average over environment stochasticity, and we plot the ILE mean and 90% confidence intervals over the 50 repeats.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

Stochastic starting state Deterministic transitions Episodic Deterministic starting state Stochastic transitions Episodic Deterministic starting state Stochastic transitions Continuing (non-episodic) Table 2: Environments used for reward recovery experiment.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

The results are shown in Fig. 4 --- our algorithm always converges to a lower ILE as the number of paths increases, indicating that we are able to recover accurate reward representations, and these reward functions are more accurate with increasing numbers of demonstration paths.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Characterizing reward recovery performance", "weight": 1.0} -->

Also of interest is the fact that, for the FrozenLake4x4 environment, our algorithm converges to a non-zero ILE. We verified that this is because optimal policies in this MDP, which are used for sampling demonstrations, only solve the environment (reaching a goal state) in $\sim {82\%}$ of episodes. If we artificially filter the optimal policy rollouts so that the demonstration data contain only successful episodes, our algorithm converges to $0.0 \pm 0.0$ ILE.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Empirical comparison with Ziebart's algorithms", "weight": 1.0} -->

Without modification, the previous MaxEnt IRL algorithms by Ziebart et al. only support state-based reward features. The FrozenLake4x4 environment consists of state-only rewards, which allows a fair comparison of the performance of our algorithm with these previous algorithms.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Empirical comparison with Ziebart's algorithms", "weight": 1.0} -->

For the case of $N = 50$ demonstration paths (not filtered to remove unsuccessful demonstrations), and with $50$ repeat experiments, our algorithm achieves an ILE mean and 90% confidence interval of $55.2 \pm 18.3$, while Ziebart's 2008 algorithm achieves an ILE of $634.0 \pm 0.0$ and the 2010 algorithm achieves an ILE of $596.7 \pm 3.9$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Empirical comparison with Ziebart's algorithms", "weight": 1.0} -->

We also compute the log-likelihood of the demonstration data under each learned reward. Our algorithm achieves a log-likelihood mean and 90% confidence interval of ${- 133} \pm 7.78$ while Ziebart's 2008 and 2010 algorithms achieve log-likelihoods of ${- 336} \pm 31.2$ and ${- 365} \pm 33.0$ respectively.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Empirical comparison with Ziebart's algorithms", "weight": 1.0} -->

For this specific environment, our algorithm out-performs Ziebart's Maximum Entropy algorithms on the ILE metric by a factor of over $10 \times$, and the log-likelihood also confirms that our rewards are a better fit to the demonstrations. These empirical data suggest that the approximate gradients from Ziebart's algorithms can sometimes have a negative effect on reward learning, which is also reflected in the results from our driver forecasting experiment, below.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The padding trick improves computational efficiency", "weight": 1.0} -->

Without the padding trick, our algorithm has a theoretical time complexity of $\mathcal{O}{({{|\mathcal{S}|}^{2}{|\mathcal{A}|}L^{2}})}$, where $L$ is the length of the longest demonstration path. With the padding trick, this dependence on $L$ becomes linear, $\mathcal{O}{({{|\mathcal{S}|}^{2}{|\mathcal{A}|}L})}$. We verify that this difference is important in practice, not just in theory.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The padding trick improves computational efficiency", "weight": 1.0} -->

To illustrate this, we again use the FrozenLake MDP template, but randomly generate unique environments of increasing size across three orders of magnitude. For each problem size, we record the runtime required to learn a reward from a dataset of 10 paths using our algorithm in the padded, and non-padded configurations. We repeat every experiment 30 times to average over variations in processor and memory utilization. The experiments were performed on a Toshiba ThinkPad T480s laptop with an Intel i7-8650U Quad-Core CPU pinned at 2.1GHz, and with 24GB of RAM running Windows 10, 64-bit and using Python 3.6.9.

<!-- chunk {"id": "body-0076", "role": "body", "section": "The padding trick improves computational efficiency", "weight": 1.0} -->

The results are shown in Fig. 5. We plot the runtime mean and 90% confidence interval vs. the problem size on a log-log scale. The empirical behaviour aligns with our theoretical complexity analysis of the algorithm: the growth rate for both versions of our algorithm is slightly higher than linear in problem size ${|\mathcal{S}|}^{2}{|\mathcal{A}|}$ --- a line with linear gradient is shown for comparison. The results show small deviations from monotonic growth (e.g. the drop in runtime for the final point) --- we hypothesise that this is due to the low-level JIT compiler we utilize to optimize the Python code.

<!-- chunk {"id": "body-0077", "role": "body", "section": "The padding trick improves computational efficiency", "weight": 1.0} -->

The results also confirm that the padding trick vastly improves the computational complexity of our algorithm, and that this improvement grows with the problem size. For the small FrozenLake4x4 MDP (problem size $\sim 10^{3}$, third data-point from the left in figure), we see a $\sim 10 \times$ improvement in runtime, while for the larger FrozenLake8x8 MDP (problem size $\sim 10^{4.2}$, rightmost data-point in figure), we see a $\sim 100 \times$ improvement due to the padding trick. These results are very encouraging, and suggest this algorithm is suitable for application to larger, real-world datasets, which we consider next.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example application: forecasting driver behaviour", "weight": 1.0} -->

We demonstrate the utility of our algorithm by application to a large, real-world dataset similar to that used in the original MaxEnt IRL paper. The UCI Taxi Service Prediction dataset (the 'Porto' dataset) contains over 1.7 million time-stamped GPS trajectories collected from the 442 taxis in the city of Porto, Portugal during 2013--14.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Data pre-processing", "weight": 1.0} -->

We adapted the Porto dataset to make it suitable for evaluating discrete state and action IRL algorithms. Continuous GPS trajectories were fit using a particle filter to a discrete road network downloaded from OpenStreetMap.org. Trajectories were removed from the dataset if they contained missing data, were shorter than 2 minutes in duration, contained cyclic paths, ventured outside a $15$km radius from the city, or if the particle filter did not converge. This resulted in an MDP with 292,604 states (road segments), 594,933 actions (unique turns at road intersections), and with a stochastic starting state and deterministic transitions. After filtering, the discretised path dataset contained 19,359 paths ranging in size from 5 to 840 states and length from 0.25 to 29km. We excluded outlier paths with more than 400 states, and segmented into a 70% training set (13551 paths) and 30% held-out test set (5808 paths).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Reward feature selection", "weight": 1.0} -->

To allow comparison with Ziebart's algorithm, we selected a state-only reward feature representation. As state features we utilised the number of lanes ($1$, $2$, or $> \, 2$), road type ('local', 'major', 'highway', or 'other'), speed limit ($< \, 35$km/h, $35 - 55$km/h, $55 - 85$km/h, $> \, 85$km/h, or 'unknown') and toll status ('toll' or 'no toll'), giving a 14-dimensional indicator vector ${\mathbf{I}}{(s)}$ which we multiplied by the distance of a road segment in meters, ${\mathbf{\phi}_{\mathbf{s}}{(s)}} \triangleq {{{{\mathbf{I}}{(s)}} \times \text{dist}}{(s)}}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

The ILE metric used in our synthetic experiments requires that the ground truth reward function be known. In the absence of a ground truth reward function, different evaluation metric(s) must be used. We used two evaluation metrics, as follows: *Distance Match Percentage* $\in {\lbrack 0,100\rbrack}$, higher is better. Measures the percentage of distance of the predicted maximum likelihood path that matches the ground truth path. This is a domain-specific approximate measure of predictive accuracy of the policies induced by a learned reward.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

*Feature Distance* $\in {\lbrack 0,\infty)}$, lower is better, units are km. Measures the $L^{2}$ norm between the predicted maximum likelihood path's feature vector and that of the ground truth path. This is a domain-agnostic metric that quantifies how well the trained model matches the demonstrated preferences in the data.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Results", "weight": 1.0} -->

Using optimized implementations on a 24-core cluster workstation with Intel Xeon E5-2760 v3 CPUs at 2.4Ghz and 384GB of RAM, individual models took $\sim 8$hrs to train to convergence using the L-BFGS-B optimizer, while evaluating a model against the test and the training data took $\sim 60$hrs.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Results", "weight": 1.0} -->

The results are shown in Table 3. We compare the performance of our algorithm with that, as well as two baseline models - an agent that always chooses the shortest (distance) path^33^3This is based on the assumption that taxi drivers (or their customers) might prefer a direct route to a destination., and a MaxEnt model with sampled random normal reward weights. For each model we report the distance match and feature distance metrics to three significant figures. We report the median (and 90% confidence interval of the median) as the result distributions are skewed --- however the non-overlapping confidence intervals and relative performance ranking for each metric are unchanged if the mean is used instead.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Results", "weight": 1.0} -->

The results show that our model outperforms the others on predictive accuracy (the distance match metric), as well as in preference matching (the feature distance metric). For both metrics, the algorithm, and the MaxEnt model with random normal weights perform significantly worse than either our algorithm or the shortest path heuristic --- by $\sim 3$, and $\sim 1$ orders-of-magnitude for the feature distance and distance match metrics respectively.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Results", "weight": 1.0} -->

Distance Match (%) Median (90% C.I.) Feature Distance (km) Median (90% C.I.)

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

We presented new perspective and algorithms, including a new interpretation that unifies MaxEnt IRL and RE-IRL with several implications, and an efficient exact algorithm that leads to improved reward learning and is capable of scaling up to a large real-world dataset. We make an optimized implementation compatible with OpenAI Gym environments publicly available to facilitate further research and applications.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion", "weight": 1.5} -->

We plan to follow up this work with some further developments. First, as mentioned in Section 2, we can develop exact algorithms to handle more complex features by adapting the sum-product algorithm. This can potentially lead to further performance improvement when complex features are indeed necessary. Second, we pointed out that our new interpretation of MaxEnt IRL suggests that we can directly adapt the model-free importance sampling learning algorithm for RE-IRL to MaxEnt IRL. While this may be biased towards short demonstrations, this allows us to deal with continuous MDPs. In addition, in principle, we can choose an alternative reference distribution to encode any other prior preference. This needs to be further explored and empirically evaluated against the exact algorithms. Lastly, the MaxEnt IRL model in fact learns a reward function for a non-stationary policy (that is, the MaxEnt trajectory distribution), however we (and others) treat the learned reward function as suitable for stationary policies, because it is computationally easier to evaluate the performance of a stationary policy. Our experiments suggest that the learned reward function are often suitable for a stationary policy.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

We hope to better understand when the reward function is suitable for a stationary policy, and develop an effective method of using the learned reward together with a non-stationary policy.
