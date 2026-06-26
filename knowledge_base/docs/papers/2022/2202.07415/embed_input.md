<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

NeuPL: Neural Population Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning in strategy games (e.g. StarCraft, poker) requires the discovery of diverse policies. This is often achieved by iteratively training new policies against existing ones, growing a policy population that is robust to exploit. This iterative approach suffers from two issues in real-world games: a) under finite budget, approximate best-response operators at each iteration needs truncating, resulting in under-trained good-responses populating the population; b) repeated learning of basic skills at each iteration is wasteful and becomes intractable in the presence of increasingly strong opponents. In this work, we propose Neural Population Learning (NeuPL) as a solution to both issues. NeuPL offers convergence guarantees to a population of best-responses under mild assumptions. By representing a population of policies within a single conditional model, NeuPL enables transfer learning across policies. Empirically, we show the generality, improved performance and efficiency of NeuPL across several test domains. Most interestingly, we show that novel strategies become more accessible, not less, as the neural population expands.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

Learning in strategy games (e.g. StarCraft, poker) requires the discovery of diverse policies. This is often achieved by iteratively training new policies against existing ones, growing a policy population that is robust to exploit. This iterative approach suffers from two issues in real-world games: a) under finite budget, approximate best-response operators at each iteration needs truncating, resulting in under-trained good-responses populating the population; b) repeated learning of basic skills at each iteration is wasteful and becomes intractable in the presence of increasingly strong opponents. In this work, we propose Neural Population Learning (NeuPL) as a solution to both issues. NeuPL offers convergence guarantees to a population of best-responses under mild assumptions. By representing a population of policies within a single conditional model, NeuPL enables transfer learning across policies. Empirically, we show the generality, improved performance and efficiency of NeuPL across several test domains^11^1See for supplementary illustrations.. Most interestingly, we show that novel strategies become more accessible, not less, as the neural population expands.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

The need for learning not one, but a population of strategies is rooted in classical game theory. Consider the purely cyclical game of rock-paper-scissors, the performance of individual strategies is meaningless as improving against one entails losing to another. By contrast, performance can be meaningfully examined between populations. A population consisting of pure strategies $\{\text{rock},\text{paper}\}$ does well against a singleton population of $\{\text{scissors}\}$ because in the meta-game where both populations are revealed, a player picking strategies from the former can always beat a player choosing from the latter^22^2This is formally quantified by Relative Population Performance, see Definition A.1. ‣ A.2 Relative Population Performance ‣ Appendix A Methods ‣ NeuPL: Neural Population Learning").. This observation underpins the unifying population learning framework of Policy Space Response Oracle (PSRO) where a new policy is trained to best-respond to a mixture over previous policies at each iteration, following a meta-strategy solver. Most impressively, Vinyals et al. explored the strategy game of StarCraft with a league of policies, using a practical variation of PSRO.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

The league counted close to a thousand sophisticated deep RL agents as the population collectively became robust to exploits.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

Unfortunately, such empirical successes often come at considerable costs. Population learning algorithms with theoretical guarantees are traditionally studied in normal-form games where best-responses can be solved exactly. This is in stark contrast to real-world Game-of-Skills --- such games are often temporal in nature, where best-responses can only be approximated with computationally intensive methods (e.g. deep RL). This has two implications. First, for a given opponent, one cannot efficiently tell apart good-responses that temporarily plateaued at local optima from globally optimal best-responses. As a result, approximate best-response operators are often truncated prematurely, according to hand-crafted schedules. Second, real-world games often afford strategy-agnostic transitive skills that are pre-requisite to strategic reasoning. Learning such skills from scratch at each iteration in the presence of evermore skillful opponents quickly becomes intractable beyond a few iterations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Abstract", "weight": 1.5} -->

This iterative and isolated approach is fundamentally at odds with human learning. For humans, mastering diverse strategies often facilitates incremental strategic innovation and learning about new strategies does not stop us from revisiting and improving upon known ones. In this work, we make progress towards endowing artificial agents with similar capability by extending population learning to real-world games. Specifically, we propose NeuPL, an efficient and general framework that learns and represents diverse policies in symmetric zero-sum games within a single conditional network, using the computational infrastructure of simple self-play (Section 1.2). Theoretically, we show that NeuPL converges to a sequence of iterative best-responses under certain conditions (Section 1.3). Empirically, we illustrate the generality of NeuPL by replicating known results of population learning algorithms on the classical domain of rock-paper-scissors as well as its partially-observed, spatiotemporal counterpart running-with-scissors (Section 2.1). Most interestingly, we show that NeuPL enables transfer learning across policies, discovering exploiters to strong opponents that would have been inaccessible to comparable baselines (Section 2.2).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Abstract", "weight": 1.5} -->

Finally, we show the appeal of NeuPL in the challenge domain of MuJoCo Football where players must continuously refine their movement skills in order to coordinate as a team. In this highly transitive game, NeuPL naturally represents a short sequence of best-responses without the need for a carefully chosen truncation criteria (Section 2.4).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Methods", "weight": 1.0} -->

Our method is designed with two desiderata in mind. First, at convergence, the resulting population of policies should represent a sequence of iterative best-responses under reasonable conditions. Second, transfer learning can occur across policies throughout training. In this section, we define the problem setting of interests as well as necessary terminologies. We then describe NeuPL, our main conceptual algorithm as well as its theoretical properties. To make it concrete, we further consider deep RL specifically and offer two practical implementations of NeuPL for real-world games.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Meta-game Strategies in Population Learning", "weight": 1.0} -->

Given a symmetric zero-sum game and a set of $N$ policies $\Pi: = {\{\pi_{i}\}}_{i = 1}^{N}$, we define a normal-form meta-game where players' $i$-th action corresponds to executing policy $\pi_{i}$ for one episode. A meta-game strategy $\sigma$ thus defines a probability assignment, or an action profile, over $\Pi$. Within $\Pi$, we define $\mathcal{U} \in {\mathbb{R}}^{N \times N}\leftarrow{\text{EVAL}{(\Pi)}}$ to be the expected payoffs between pure strategies of this meta-game or equivalently, $\mathcal{U}_{ij}: = J{(\pi_{i},\pi_{j})}$ in the underlying game.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Meta-game Strategies in Population Learning", "weight": 1.0} -->

Finally, we define $f:{{\mathbb{R}}^{{|\Pi|} \times {|\Pi|}}\rightarrow{\mathbb{R}}^{|\Pi|}}$ to be a meta-strategy solver (MSS) with $\sigma\leftarrow{f{(\mathcal{U})}}$ and $\mathcal{F}:{{\mathbb{R}}^{N \times N}\rightarrow{\mathbb{R}}^{N \times N}}$ a meta-graph solver (MGS) with $\Sigma\leftarrow{\mathcal{F}{(\mathcal{U})}}$. The former formulation is designed for iterative optimization of approximate best-responses as in Lanctot et al. whereas the latter is motivated by concurrent optimization over a set of population-level objectives as in Garnelo et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Meta-game Strategies in Population Learning", "weight": 1.0} -->

In particular, $\Sigma \in {\mathbb{R}}^{N \times N}: = {\{\sigma_{i}\}}_{i = 1}^{N}$ defines $N$ population-level objectives, with $\pi_{i}$ optimized against the mixture policy represented by $\sigma_{i}$ and $\Pi$. As such, $\Sigma \in {\mathbb{R}}^{N \times N}$ corresponds to the adjacency matrix of an interaction graph. Figure 1 illustrates several commonly used population learning algorithms defined by $\Sigma$ or equivalently, their interaction graphs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Neural Population Learning", "weight": 1.0} -->

We now present NeuPL and contrast it with Policy-Space Response Oracles (PSRO, Lanctot et al. ) which similarly focuses on population learning with approximate best-responses by RL.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Neural Population Learning", "weight": 1.0} -->

1:Πθ(⋅|s, σ) ⊳ Conditional neural population net. 2:Σ: = {σi}i = 1N ⊳ Initial interaction graph. 9: 𝒰 ← Eval (ΠθΣ) ⊳ (Optional) if ℱ adaptive. Algorithm 1 Neural Population Learning (Ours) 1:Π: = {π0} ⊳ Initial policy population. 2:σ ← Unif (Π) ⊳ Initial meta-game strategy. 5:for i ∈ [[N]] do ⊳ N-step ABR. 9: 𝒰 ← Eval (Π) ⊳ Empirical payoffs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Neural Population Learning", "weight": 1.0} -->

NeuPL deviates from PSRO in two important ways. First, NeuPL suggests concurrent and continued training of all unique policies such that no good-response features in the population prematurely due to early truncation. Second, NeuPL represents an entire population of policies via a shared conditional network $\Pi_{\theta}{( \cdot |s,\sigma)}$ with each policy $\Pi_{\theta}{( \cdot |s,\sigma_{i})}$ conditioned on and optimised against a meta-game mixture strategy $\sigma_{i}$, enabling transfer learning across policies.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Neural Population Learning", "weight": 1.0} -->

This representation also makes NeuPL general: it delegates the choice of effective population sizes ${|{\text{Unique}{(\Sigma)}}|} \leq {|\Sigma|} = N$ to the meta-graph solver $\mathcal{F}$ as $\sigma_{i} = \sigma_{j}$ implies $\Pi_{\theta}{( \cdot |s,\sigma_{i})} \equiv \Pi_{\theta}{( \cdot |s,\sigma_{j})}$ (cf. Section 2.1). Finally, NeuPL allows for cyclic interaction graphs, beyond the scope of PSRO. We discuss the generality of NeuPL in the context of prior works in further details in Appendix D.

<!-- chunk {"id": "body-0017", "role": "body", "section": "N-step Best-Responses via Lower-Triangular Graphs", "weight": 1.0} -->

A popular class of population learning algorithms seeks to converge to a sequence of $N$ iterative best-responses where each policy $\pi_{i}$ is a best-response to an opponent meta-game strategy $\sigma_{i}$ with support over a subset of the policy population $\Pi_{< i} = {\{\pi_{j}\}}_{j < i}$. In NeuPL, this class of algorithms are implemented with meta-graph solvers that return lower-triangular adjacency matrices $\Sigma$ with $\Sigma_{i \leq j} = 0$. Under this constraint, $\sigma_{0}$ becomes a zero vector, implying that $\Pi_{\theta}{( \cdot |s,\sigma_{0})}$ does not seek to best-respond to any policies.

<!-- chunk {"id": "body-0018", "role": "body", "section": "N-step Best-Responses via Lower-Triangular Graphs", "weight": 1.0} -->

Similar to the role of initial policies $\{\pi_{0}\}$ in PSRO (Algorithm 2), $\Pi_{\theta}{( \cdot |s,\sigma_{0})}$ serves as a starting point for the sequence of N-step best-responses and any fixed policy can be used. We note that this property further allows for incorporating pre-trained policies in NeuPL, as we discuss in Appendix D.1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "N-step Best-Responses via Lower-Triangular Graphs", "weight": 1.0} -->

1:function ℱPSRO-N(𝒰) ⊳ 𝒰 ∈ ℝN × N the empirical payoff matrix. 2: Initialize meta-game strategies Σ ∈ ℝN × N with zeros. 4: Σi + 1, 1: i ← SOLVE-Nash (𝒰1: i, 1: i) ⊳ LP Nash solver, see Shoham & Leyton-Brown. Algorithm 3 A meta-graph solver implementing PSRO-Nash.

<!-- chunk {"id": "body-0020", "role": "body", "section": "N-step Best-Responses via Lower-Triangular Graphs", "weight": 1.0} -->

One prominent example is PSRO-Nash, where $\pi_{i}$ is optimized to best-respond to the Nash mixture policy over $\Pi_{< i}$. This particular meta-graph solver is shown in Algorithm 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Convergence to N-step Best-Responses via NeuPL", "weight": 1.0} -->

Under certain assumptions on the best-response operator, interaction graph, and meta-graph solver (MGS) we can construct proofs that NeuPL converges to an $N$-step best-response. We introduce the term *grounded* (Section C) to refer to interaction graphs and MGS that have a structure that imposes convergence to a unique set of policies. Certain interaction graphs are grounded, in particular, lower-triangular graphs are one such class which describe an $N$-step best response. In addition, certain MGSs are grounded, in particular, ones that operate on the sub-payoff and output a lower-triangular interaction graph, $\mathcal{F}:{\mathcal{U}_{{< i},{< i}}\rightarrow\Sigma_{i,{< i}}}$. The lower-triangular maximum entropy Nash equilibrium (MENE) is one such grounded MGS. Therefore with sufficiently large $N$, NeuPL will converge to a normal-form Nash equilibrium. See Section C for the full definitions, theorems and proofs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Neural Population Learning by RL", "weight": 1.0} -->

We now define the discounted return maximized by $\Pi_{\theta}{( \cdot |o_{\leq t},\sigma_{i})}$ in Equation 1. We denote $P{(\sigma_{i})}$ as the probability distribution over policy $i$'s opponent identities $\sigma_{j} \in {\{\sigma_{1},\ldots,\sigma_{N}\}}$. Intuitively, each policy is maximizing its expected returns in the underlying game under a double expectation: the first is taken over its opponent distribution, with $\sigma_{j} \sim {P{(\sigma_{i})}}$ and the second taken under the game dynamics partly defined by the pair of policies $(\Pi_{\theta}{( \cdot |o_{\leq t},\sigma_{i})},\Pi_{\theta}{( \cdot |o_{\leq t}',\sigma_{j})})$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Neural Population Learning by RL", "weight": 1.0} -->

Finally, we propose Algorithm 4 in the setting where the meta-graph solver $\Sigma^{\text{const}}\leftarrow{\mathcal{F}{(\mathcal{U})}}$ is a constant function and extends it to Algorithm 5 where the meta-graph solver is adaptive in $\mathcal{U}$. For instance, population learning algorithms such as Fictitious Play implement static interaction graphs while algorithms such as PSRO rely on adaptive MGS.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we validate different contributions of NeuPL across several domains. First, we verify the generality of NeuPL from two aspects: a) NeuPL recovers expected results of existing population learning algorithms on the classical game of rock-paper-scissors where we can visualize the learned policy population over time and; b) NeuPL generalises to the spatiotemporal, partially observed strategy game of running-with-scissors, where players must infer opponent behaviours through tactical interactions. Second, we show that NeuPL induces skill transfer across policies, enabling the discovery of exploiters to strong opponents that would have been out-of-reach otherwise. This property translates to improved efficiency and performance compared to PSRO-Nash baselines, even under favorable conditions. Lastly, we show that NeuPL scales to the large-scale Game-of-Skills of MuJoCo Football where a concise sequence of best-responses are learned, reflecting the prominent transitive skill dimension of the game.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

In all experiments, we use Maximum A Posterior Optimization (MPO, Abdolmaleki et al. ) as the underlying RL algorithm, though any alternative can be used instead. Similarly, any conditional architecture can be used to implement $\Pi_{\theta}^{\Sigma}$. Our specific proposal reflects the spinning-top geometry so as to encourage positive transfers across polices. Further discussions on the network design is available in Appendix B.2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stochastic Games", "weight": 1.0} -->

running-with-scissors extends rock-paper-scissors to the spatiotemporal and partially-observed setting. Using first-person observations of the game (a 4x4 grid in front of the agent), each player collects resources representing "rock", "paper" and "scissors" so as to counter its opponent's hidden inventory. At the end of an episode or when players confront each other through "tagging", players compare their inventories and receive rewards accordingly. To do well, one must infer opponent behaviours from its partial observation history $o_{\leq t}$ --- if "rock"s went missing, then the opponent may be collecting them; if the opponent ran past "scissors", then it may not be interested in it. We describe the environment in details in Appendix B.1. Figure 4 shows that NeuPL with $\mathcal{F}_{\text{PSRO-N}}$ leads to a population of sophisticated policies. As before, we set the initial sink policy to be exploitable and biased towards picking up "rock"s.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stochastic Games", "weight": 1.0} -->

Early in training, we note that the first three policies of the neural population implement the pure-resource policies of "rock", "paper" and "scissors" respectively, as evidenced by their relative payoffs. In contrast to rock-paper-scissors, the mixture of pure-resource policies is exploitable in the sequential setting, where the player can observe its opponent before implementing a counter strategy. Indeed, policy $\Pi_{\theta}{( \cdot |o_{\leq},\sigma_{4})}$ observes and exploits, beating the mixture policies at epoch 680. Following $\mathcal{F}_{\text{PSRO-N}}$, $\Pi_{\theta}{( \cdot |o_{\leq},\sigma_{5})}$ updates its objective to focus solely on this newfound NE over $\Pi_{\theta}^{\Sigma_{< 5}}$, developing a deceptive counter strategy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Does NeuPL enable Transfer Learning across Policies?", "weight": 1.0} -->

In contrast to prior works that train new policies iteratively from scratch, NeuPL represents diverse policies with explicit parameter sharing. Figure 6 compares the two approaches and illustrates the significance of transfer learning across iterations. Specifically, we verify that the shared representation learned by training against fewer, weaker policies early in training, facilitates the learning of exploiters to stronger, previously unseen opponents. To this end, a set of randomly initialized MPO agents with partially transferred parameters from different epochs of the experiment shown in Figure 4 are trained against fixed mixture policies defined by $\Pi_{\theta^{\ast}}^{\Sigma^{\ast}}$, with $\theta^{\ast}$ and $\Sigma^{\ast} = {\mathcal{F}_{\text{PSRO-N}}{(\mathcal{U}^{\ast})}}$ obtained at epoch 1,200 of the same experiment. In other words, the objective for each agent is to beat a fixed NE over pre-trained policies ${\{{\Pi_{\theta^{\ast}}{(\left.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Does NeuPL enable Transfer Learning across Policies?", "weight": 1.0} -->

a \middle| {o_{\leq},\sigma_{k}^{\ast}} \right.)}}\}}_{k = 1}^{n}$, with a specific $n$. Figure 6 shows the learning progressions of the agents for $n \in {\{ 2,4,7\}}$, with transferred parameters taken at epoch 0 (red) upto 1,000 (green).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Does NeuPL enable Transfer Learning across Policies?", "weight": 1.0} -->

Against an easily exploitable opponent mixture (NE over the first two pure-resource policies), an agent with randomly initialized parameters (red) remains capable of learning an effective best response, albeit at a slower pace. This difference becomes much more apparent against competent mixture policies that execute sophisticated strategies (NE over the first 4 or 7 policies) --- the randomly initialized agent failed to counter its opponent despite prolonged training while agents with partially transferred parameters successfully identified exploits, leveraging effective representation of the environment dynamics and of diverse opponent strategies. By transferring skills that support sophisticated strategic decisions across iterations, NeuPL enables the discovery of novel policies that are inaccessible to a randomly initialized agent. In other words, learning incremental best responses becomes easier, not harder, as the population expands. This is particularly attractive in games where strategy-agnostic skill learning is challenging in itself.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Does NeuPL Outperform Comparable Baselines?", "weight": 1.0} -->

We compare a NeuPL population implementing $\mathcal{F}_{\text{PSRO-N}}$ to 4 comparable baselines implementing variants of PSRO. Since PSRO does not prescribe a truncation criteria at each iteration, we investigate PSRO baselines with 100k and 200k gradient steps per iteration respectively. Further, we consider the effect of continued training across iterations, by initializing new policies with the policy obtained at the end of the preceding iteration instead of random initialization. We refer to this continued variant as PSRO-C. All PSRO populations are initialized with the same initial policy used for the NeuPL population. Figure 7 illustrates the quantitative benefits of NeuPL, measuring RPP between a NeuPL population of maximum population size of 8 against the final population of 8 policies obtained via PSRO after 7 iterations. The vertical dashed lines indicate that both the NeuPL population and the PSRO population have cumulatively undergone identical amount of training to allow for fair comparison.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Does NeuPL Outperform Comparable Baselines?", "weight": 1.0} -->

In purple, we show the effective population size of the NeuPL population which has been shown previously in Figure 5. We make the following observations: i) with a population size of 8, the NeuPL population successfully exploits PSRO baselines representing an equal number of policies, even if the latter performed twice as many gradient updates; ii) the increase in RPP coincides with an increase in the effective population size, from 5 to 8, reaching the maximum number of distinct policies that this NeuPL population can represent; iii) the amount of training each PSRO generation received has limited impact on the robustness of policy populations at convergence. This corroborates our observations in Figure 6, where the agent (in red) failed to exploit strong opponents despite continued training. Interestingly, PSRO-C proves equally exploitable. We hypothesize that the learned policies failed to develop reusable representations that can support diverse strategic decisions. Details of the PSRO baselines across 3 seeds are available in Appendix B.4, demonstrating the strategic complexities captured by the PSRO baseline populations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Does NeuPL Scale to Highly Transitive Game-of-Skills?", "weight": 1.0} -->

If a game is purely transitive, all policies share the same best-response policy. In this case, self-play offers a natural curriculum that efficiently converges to this best-response. Nevertheless, this approach is infeasible in real-world games as one cannot rule out strategic cycles in the game without exhaustive policy search. The MuJoCo Football domain is one such example: it challenges agents to continuously refine their motor control skills while coordinated team-play intuitively suggests the presence of strategic cycles. In such games, PSRO is a challenging proposal as it requires carefully designed truncation criteria. If an iteration terminates prematurely due to temporary plateaus in performance, good-responses are introduced and convergence is slowed unnecessarily; if iterations rarely terminate, then the population may unduly delay the representation of strategic cycles. In such games, NeuPL offers an attractive proposal that retains the ability to capture strategic cycles, but also falls back to self-play if the game appears transitive.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We proposed an efficient, general and principled framework that learns and represents strategically diverse policies in real-world games within a single conditional-model, making progress towards scalable policy space exploration. In addition to exploring suitable technique from the multi-task, continual learning literature, going beyond the symmetric zero-sum setting remain interesting future works, too, as discussed in Appendix D.
