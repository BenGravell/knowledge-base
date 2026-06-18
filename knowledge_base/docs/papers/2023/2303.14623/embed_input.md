<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Inverse Reinforcement Learning without Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse Reinforcement Learning (IRL) is a powerful set of techniques for imitation learning that aims to learn a reward function that rationalizes expert demonstrations. Unfortunately, traditional IRL methods suffer from a computational weakness: they require repeatedly solving a hard reinforcement learning (RL) problem as a subroutine. This is counter-intuitive from the viewpoint of reductions: we have reduced the easier problem of imitation learning to repeatedly solving the harder problem of RL. Another thread of work has proved that access to the side-information of the distribution of states where a strong policy spends time can dramatically reduce the sample and computational complexities of solving an RL problem. In this work, we demonstrate for the first time a more informed imitation learning reduction where we utilize the state distribution of the expert to alleviate the global exploration component of the RL subroutine, providing an exponential speedup in theory. In practice, we find that we are able to significantly speed up the prior art on continuous control tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse Reinforcement Learning (IRL), also known as Inverse Optimal Control (Kalman Bagnell, ) or Structural Estimation, is the problem of finding a reward function that rationalizes (i.e. makes optimal) demonstrated behavior. Such approaches build on the lengthy history of trying to understand intelligent behavior as approximate optimization of some cost function. While economists and cognitive scientists are often interested in analyzing the recovered reward function, it is more common in machine learning to view IRL algorithms as methods to imitate or forecast expert behavior.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are three key benefits to the IRL approach to imitation. The first is policy space structuring: effectively, IRL reduces our (often large) policy class to just those policies that are (approximately) optimal under some member of our (relatively small) reward function class.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second is transfer across problems: for many practical applications (e.g. robotics (Silver et al. Ratliff et al. Kolter et al. Ng et al. Zucker et al., ), computer vision, and human-computer interaction ), one is able to learn a single reward function across multiple instances and then use it to forecast or imitate expert behavior in new problems that arise at test time. As Ng et al. put it, "the entire field of reinforcement learning is founded on the presupposition that the reward function, rather than the policy is the most succinct, robust, and transferable definition of the task" (italics ours). The third is robustness to compounding errors: as IRL methods involve the learner performing rollouts in the environment, they cannot end up in states they didn't expect to at test time and therefore will not suffer from compounding errors. Taken together, these three reasons help explain why IRL methods continue to provide state-of-the-art results on challenging imitation learning problems (e.g. in autonomous driving (Bronstein et al. Igl et al. Vinitsky et al., )).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The most widely used approaches to IRL are fundamentally game-theoretic. An RL algorithm generates trajectories by optimizing (i.e. decoding) the current reward function. In response, a reward function selector picks a new reward function that discriminates between learner and expert trajectories. As pointed out by Finn et al., the IRL setup generalizes a GAN with a dynamics model in the generation stem. More specifically, if one looks at the typical structure of an IRL algorithm, one performs the decoding-via-RL operation repeatedly in an inner loop, tweaking the current estimate of the reward function in the outer loop to produce behavior that more closely resembles that of the expert.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For some problems, highly optimized planners or optimal controller synthesis procedures allow an efficient implementation of this inner loop. More generally however, one might want to tackle problems that don't have efficient algorithms to decode behavior and therefore be forced to rely on sample-based RL algorithms. Unfortunately, this can make each inner loop iteration quite inefficient (both in terms of computational and sample efficiency) as it requires solving the global exploration problem inherent in RL. From the lens of reductions, such an approach is counter-intuitive as we've turned the relatively easy problem of imitating an expert into the repeated solving of the hard problem of RL.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work (Kakade and Langford Bagnell et al. Ross et al., ) has shown that access to a good exploration distribution (i.e. the states where a strong policy spends much of its time) can dramatically reduce the complexity of RL as the learner doesn't have to explore for as long: knowing a set of waypoints along the shortest path through a maze should speed up your attempt to solve it. In the imitation learning setup, we have access to just such a distribution: the expert's visitation distribution. Our key insight is that expert demonstrations can dramatically improve the efficiency of the RL subroutine of IRL.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

1\. We derive two algorithms that reset the learner to states from the expert visitation distribution for more efficient IRL. MMDP (Moment Matching by Dynamic Programming) produces a sequence of policies. NRMM (No-Regret Moment Matching) produces a single, stationary policy. Both come in primal and dual variants.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

2\. We discuss the statistical complexity of expert resets. We prove that in the worst case, traditional IRL algorithms take an exponential number of interactions (in the horizon of the problem) to learn a policy competitive with the expert. In contrast, we prove that our algorithms require only polynomial interactions per iteration to learn policies competitive with the expert.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

3\. We discuss the performance implications of expert resets. We show that in the worst case, neither MMDP nor NRMM can avoid a quadratic compounding of errors with respect to the horizon.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

4\. We derive a practical meta-algorithm that achieves the best of both. We propose FILTER (Fast Inverted Loop Training via Expert Resets) which interpolates between traditional IRL and our own approaches via mixing expert resets with standard resets. This allows use to ease the exploration burden on the learner while mitigating compounding errors. We implement FILTER on continuous control tasks and find it is more efficient than standard IRL.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We begin with a discussion of related work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Expert Resets in Inverse RL", "weight": 1.0} -->

We utilize the moment-matching framework of Swamy et al. to prove performance bounds for our algorithms. Our results allow one to speed up any member of the broad reward-moment-matching phylum of their taxonomy that uses RL (e.g. MaxEnt IRL, GAIL, SQIL ).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Expert Resets in Inverse RL", "weight": 1.0} -->

Input: Demos. 𝒟E, Policy class Π, Reward class ℱr
Output: Trained policy π
// Use any no-regret algo to pick π
$\pi_{i}\leftarrow{\text{𝙼𝚊𝚡𝙴𝚗𝚝𝚁𝙻}{({r = {\frac{1}{i}{\sum_{j = 1}^{i}f_{j}}}})}}$
$f_{i + 1}\leftarrow{{\underset{f\in\mathcal{F}_{r}}{\arg ⁡\max}J{(\pi_{E},f)}} - {J{(\pi_{i},f)}}}$
Return πi with the lowest validation error.
Algorithm 2 IRL (Primal, Syed and Schapire )

<!-- chunk {"id": "body-0016", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

Consider a finite-horizon Markov Decision Process (MDP) parameterized by $\langle\mathcal{S},\mathcal{A},\mathcal{T},r,T\rangle$ where $\mathcal{S}$, $\mathcal{A}$ are the state and action spaces, $\mathcal{T}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$ is the transition operator, $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack{- 1},1\rbrack}}$ is the reward function, and $T$ is the horizon. In the inverse RL setup, we see trajectories generated by an expert policy $\pi^{E}:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$, but do not know the reward function.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

Our goal is to nevertheless learn a policy that performs as well as the expert's, no matter the true reward function.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

Input: Sequence of expert visitation distributions ρE1…ρET, Policy class Π, Reward class ℱr
Output: Sequence of trained policies π = π1: T
Sample a random start state st ∼ ρEt.
Execute a random action at ∼ Unif(𝒜) in st.
Follow πt + 1: T until the end of the horizon.
// (Approximately) solve moment-matching game.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

Algorithm 3 MMDP (Moment Matching by Dynamic Programming): Primal

<!-- chunk {"id": "body-0020", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

We solve the IRL problem via equilibrium computation between a policy player and an adversary that tries to pick out differences between expert and learner policies along certain moments (i.e. potential components of the reward function). More formally, we optimize over (time-varying) policies $\pi = {\{\pi_{1},\ldots,\pi_{T}\}}$, with $\pi_{t}:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}} \in \Pi}$ and reward functions $f:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack{- 1},1\rbrack} \in \mathcal{F}_{r}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

For simplicity, we assume that our strategy spaces ($\Pi$ and $\mathcal{F}_{r}$) are convex and compact, that $\mathcal{F}_{r}$ is closed under negation, and that ${r \in \mathcal{F}_{r}},{\pi_{E} \in \Pi}$. ^11^1If we do not assume realizability, we would get the analogous agnostic bounds throughout the following sections. We solve (i.e. compute an approximate Nash equilibrium) of the two-player zero sum game

<!-- chunk {"id": "body-0022", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

Swamy et al. describe two different classes of strategies for equilibrium computation: primal, where the policy player follows a no-regret strategy against a best-response discriminative player and dual, where the discriminative player follows a no-regret strategy against a best-response policy player. Most IRL algorithms are dual (e.g. MaxEnt IRL or LEARCH ) but there do exist primal approaches (e.g. MWAL, GAIL ). For both classes of strategies, a best-response corresponds to an inner loop iteration, while a no-regret step corresponds to an outer loop iteration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

For the policy player, a best-response consists of solving the RL problem under the current adversarially chosen reward function, i.e.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

while a no-regret step consists of running any no-regret online learning algorithm over the history of rewards, ^22^2We write down a specific no-regret algorithm here (Follow the Regularized Leader ) but one could use any other (e.g. Multiplicative Weights or Online Gradient Descent ) and have similar guarantees. e.g.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

where $H{(\pi)}$ denotes the entropy of the policy. See Algorithms and for psuedocode, with $R{(f)}$ being a strongly convex regularizer.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Inverse RL as (Inefficient) Game Solving", "weight": 1.0} -->

In both cases, one is solving a full RL problem at each iteration.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Method 1: Dynamic Programming", "weight": 1.0} -->

Dynamic programming in the form of the Bellman Equation forms the basis of $Q$-learning based approaches to RL: one \"backs-up\" $Q$ values backwards-in-time, selecting actions based on the sum of the reward at the current timestep and the already computed value of the next state. More generally however, one can back-up policies rather than just $Q$-values, as in the Policy Search by Dynamic Programming (PSDP) algorithm of Bagnell et al.. Given some roll-in distribution $\nu$, the algorithm draws states from timestep $T$ and selects a policy

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method 1: Dynamic Programming", "weight": 1.0} -->

Then, holding this policy fixed, the algorithm draws states from the roll-in distribution at timestep $T - 1$ and selects a policy for timestep $T - 1$ that maximizes reward over the horizon,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Method 1: Dynamic Programming", "weight": 1.0} -->

where $s^{\prime}$ denotes a successor state. This induction proceeds backwards in time until one reaches the first timestep, at which point a sequence of policies $\pi_{1:T}$ is output. Notice that at each step of this algorithm, we are solving a single-step classification problem. So, instead of the exponential-in-the-horizon complexity one must pay (in hard instances) for RL, one pays only quadratically in the horizon.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Method 1: Dynamic Programming", "weight": 1.0} -->

The careful reader will notice that PSDP requires a reward function. Two strategies come to mind for adversarially picking one for IRL. The first is to choose a reward for each timestep (i.e. each $t \in {\lbrack T\rbrack}$) of PSDP. The second is to run PSDP to completion (i.e. solve for all $T$ policies) and then pick a new reward in an outer loop. We focus on the first, primal strategy in the main text and defer the latter, dual strategy to Appendix B for space reasons. We call the resulting algorithm MMDP: Moment Matching by Dynamic Programming and outline the procedure in Algorithm Game Solving ‣ 3 Expert Resets in Inverse RL ‣ Inverse Reinforcement Learning without Reinforcement Learning"). Throughout our analysis, we define optimization error $\epsilon_{t}$ as the value when $\pi_{t}$ is plugged into Eq. ). Like PSDP, MMDP avoids the exponential sample complexity of RL.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Method 2: No-Regret Moment Matching", "weight": 1.0} -->

For tasks with long horizons, learning a sequence of policies may be significantly more burdensome than learning just one. We now present an algorithm that outputs a single, stationary policy. Our approach is based on the No-Regret Policy Iteration (NRPI) algorithm of Ross et al.. Instead of solving a sequence of optimization problems backwards in time like PSDP, NRPI picks a time to sample from the roll-in distribution uniformly at random, takes a random action, and then follows the previous policy $\pi_{i - 1}$ for the rest of the episode. This gives it sample estimates of $Q^{\pi_{i - 1}}$ on states from the roll-in distribution. To have a no-regret property, NRPI performs (regularized) greedy policy improvement using the history of such samples, i.e.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Method 2: No-Regret Moment Matching", "weight": 1.0} -->

Notice that rather than solving a global exploration problem, NRPI only focuses on picking the best action on states from the roll-in distribution, avoiding the exponential interaction complexity lower bound. NRPI can be seen as an analog of PSDP for stationary policies.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Method 2: No-Regret Moment Matching", "weight": 1.0} -->

As with PSDP, NRPI requires a reward function. We therefore choose one adversarially for IRL. We outline the full procedure in Algorithm. Intuitively, this algorithm is performing primal moment-matching with the learner's start state distribution being the expert's stationary distribution. For space reasons, we postpone the dual algorithm to Appendix B.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Dual Algorithms", "weight": 1.0} -->

A natural question upon reading the preceding sections is whether dual algorithms can leverage expert resets to speed up policy search. Practically, these algorithms would run PSDP or NRPI in their inner loop with a reward function chosen via a no-regret algorithm in their outer loop. Indeed these dual algorithms also work, but for a subtle reason. ^44^4In an earlier draft of this paper, we arrived at the incorrect answer of no to the preceding question. We contain multitudes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dual Algorithms", "weight": 1.0} -->

Recall that NRPI and PSDP only compete with policies that have similar visitation distributions to the expert (Bagnell et al. Ross et al., ). This is fine when selecting policies in the outer loop as the expert policy is an equilibrium strategy. However, the story is less clear when policy search is the inner loop. This is because the expert policy might be quite far from the optimal policy for the adversarially chosen reward. Thus, if we use NRPI/PSDP as our policy search method, the learner may struggle to find the best response needed for equilibrium computation. However, we prove that we're still able to guarantee we learn strong policies on average over iterations via both dual algorithms. Intuitively, one can guarantee doing as well as $\pi_{E}$ under all reward functions simply by doing as well as $\pi_{E}$ at each iteration of a no-regret reward selection algorithm. Note that this does not require finding the truly optimal policy for each adversarially selected reward function. Put differently, an expert-competitive response suffices if a best response is not possible.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Dual Algorithms", "weight": 1.0} -->

We give the full psuedocode for the dual algorithms and prove similar performance bounds to those in the preceding section in Appendix B.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Getting the Best of Both Worlds", "weight": 1.0} -->

In the preceding section, we derived two algorithms, MMDP and NRMM, which can compute policies that match expert behavior in polynomial time. However, in the worst case, both can produce policies that suffer from a quadratic compounding of errors with respect to the horizon. Traditional IRL approaches have complimentary strengths: they can suffer from exponential computation complexity but produce policies with a performance gap linear in the horizon. This begs the question: can we get the best of both worlds?

<!-- chunk {"id": "body-0038", "role": "body", "section": "Getting the Best of Both Worlds", "weight": 1.0} -->

Consider a variation of NRMM where, with probability $\alpha$, we perform an expert reset, otherwise performing a standard rollout (i.e. $s_{t} \sim \rho_{\pi_{i - 1}}^{t}$). By setting $\alpha = 1$, we unsurprisingly recover NRMM. However, if we set $\alpha = 0$, the per-round loss that is passed to the learner becomes

<!-- chunk {"id": "body-0039", "role": "body", "section": "Getting the Best of Both Worlds", "weight": 1.0} -->

This is strikingly similar to the standard approximate policy improvement procedure with an adversarially chosen reward. Recall that in NRMM, we select our discriminator $f$ as in primal IRL. Put together, setting $\alpha = 0$ is effectively using an off-policy RL algorithm in the policy optimization component of Algorithm. One might therefore reasonably expect such an approach to inherit the exponential complexity and linear-in-the-horizon performance gap of standard IRL.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Getting the Best of Both Worlds", "weight": 1.0} -->

It is natural to consider annealing between these extremes by decaying $\alpha$ from $1$ to $0$ over outer-loop iterations. Intuitively, this allows the learner to quickly find a policy with quadratic errors before refining it to a policy with error linear in the horizon. Even more simply, one can interpolate with a fixed $\alpha = 0.5$ probability, reducing the exploration burden on the learner while mitigating compounding errors. We term such annealed / interpolated approaches FILTER: Fast Inverted Loop Training via Expert Resets. Defining $\overline{\epsilon}$ as in Eq. and ${\overline{\epsilon}}_{RL}$ as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Getting the Best of Both Worlds", "weight": 1.0} -->

(i.e. the errors on the expert and start state distributions) we can derive a performance bound for FILTER by taking the minimum over the NRMM and IRL bounds.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct experiments with the PyBullet Suite. We train experts using RL and then present all learners with 25 expert demonstrations to remove small-data concerns. As a simple behavioral cloning baseline matches expert performance under these conditions, we harden the problem by introducing randomization: with probability $p_{tremble}$, a random action gets executed in the environment rather than the one the policy chose. Our expert data is free from these corruptions. We also conduct experiments on the antmaze-large tasks from Fu et al., but with $p_{tremble} = 0$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare 4 algorithms: FILTER(BR), FILTER(NR), MM (i.e. Algorithm, or, equivalently, FILTER(NR) with $\alpha = 0$), and BC. ^55^5In practice, rather than perform policy improvement on just the first state from the learner suffix, we instead perform policy improvement on states from the entire suffix (i.e. standard $Q$-learning). While in the worst case, this means that our performance bounds could degrade by a factor of $T$, in practice the benefits of leveraging the entire suffix often outweighs the potential cost. See Appendix C for details. We do not implement MMDP as these tasks can all last for $T = 1000$ timesteps. We plot the performance of the policy as a function of the number of environment interactions used for policy optimization. ^66^6In some implementations of algorithms like GAIL, trajectories from the policy's replay buffer are used for training the discriminator rather than trajectories sampled post-policy-update.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

For FILTER, as we may only observe suffixes when $\alpha > 0$, we need to separately sample whole trajectories post-policy-update. To make the comparison fair, we do this for MM as well. As recommended by Agarwal et al., we plot a robust statistic (i.e. the interquartile mean). Standard errors are computed across 10 runs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

For our baseline moment-matching algorithm, we use a significantly improved version of GAIL. Specifically, we switch from the Jensen-Shannon divergence to an integral probability metric (as recommended by Swamy et al. ), use the more efficient Soft Actor Critic or TD3+BC as our policy optimizers, add a gradient penalty to the discriminator, and use Optimistic Mirror Descent to optimize both players for fast and last iterate convergence. See the appendix of Swamy et al. for an ablation of these changes. Taken together, these changes make our baseline a strong point of comparison, over which improvement is non-trivial.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Figure, we see that FILTER(BR) and FILTER(NR) perform comparably and are significantly faster at finding strong policies than MM on 4/5 environments. We would recommend trying both variants when applying the algorithm in practice. To the best of our knowledge, the performance of FILTER on both variants of antmaze is the highest performance ever achieved by an algorithm that doesn't use any reward information. ^77^7We note that the performance we report for behavioral cloning on these environments is significantly higher than what is usually reported in the literature -- see Appendix C for details.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

It is also interesting to consider the difference in results between the environments we consider. In the Bullet locomotion environments, we found that $\alpha = 0.5$ worked better than $\alpha = 1$. We hypothesize that this is because the learner is able to learn to connect their initial state to sampled expert states more easily. For locomotion tasks, this might correspond to learning to accelerate before matching the expert's gait. We tried a more complex annealing strategy but found that it did not outperform a fixed $\alpha = 0.5$. However, we believe that for other problems, the annealing strategy could perform better than a fixed $\alpha$. For the AntMaze environments, we found that $\alpha = 1$ worked better than lower values. We hypothesize that this is because of the difficulty of exploration in a maze, for which expert resets can help a lot. In general, we would recommend that the harder exploration is in a problem, the higher $\alpha$ should be set.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

We release the code we used for all of our experiments at Of particular interest are the gym wrappers, which should be easily transferable to other algorithms / implementations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

In summary, we provide multiple algorithms for more sample efficient inverse reinforcement learning, both in theory and practice. Our key insight is speeding up policy optimization via resetting the learner to states from expert demonstrations. We emphasize that due to the reduction-based analysis we perform, one could apply this technique to an arbitrary inverse reinforcement learning algorithm and not just the GAIL-like approach we use for experiments.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

One interesting avenue for future work is developing an algorithm with stronger guarantees in the interpolated case -- for example, one could imagine training two discriminators (one on trajectories from each start state distribution) and using the more pessimistic during learning.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another is to address an assumption fundamental to our approach: the ability to reset the learner to an arbitrary initial state. While this is possible in many (if not most) simulators, it is not clear how to do this in the real world or when one only has the \"trace\" model of access (i.e. resets only to a fixed initial state distribution).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

Lastly, one could also further investigate where sub-optimal data could be used in our procedure. For example, one could mix it with the expert data and use this mixture distribution for resets if only a limited number of demonstrations are available. As long as we still use the expert data for reward selection, we conjecture that similar guarantees to the ones we prove above would hold.
