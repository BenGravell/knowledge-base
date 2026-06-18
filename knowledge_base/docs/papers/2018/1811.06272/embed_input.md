<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning policies on data synthesized by models can in principle quench the thirst of reinforcement learning algorithms for large amounts of real experience, which is often costly to acquire. However, simulating plausible experience de novo is a hard problem for many complex environments, often resulting in biases for model-based policy evaluation and search. Instead of de novo synthesis of data, here we assume logged, real experience and model alternative outcomes of this experience under counterfactual actions, actions that were not actually taken. Based on this, we propose the Counterfactually-Guided Policy Search (CF-GPS) algorithm for learning policies in POMDPs from off-policy experience. It leverages structural causal models for counterfactual evaluation of arbitrary policies on individual off-policy episodes. CF-GPS can improve on vanilla model-based RL algorithms by making use of available logged data to de-bias model predictions. In contrast to off-policy algorithms based on Importance Sampling which re-weight data, CF-GPS leverages a model to explicitly consider alternative outcomes, allowing the algorithm to make better use of experience data. We find empirically that these advantages translate into improved policy evaluation and search results on a non-trivial grid-world task.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we show that CF-GPS generalizes the previously proposed Guided Policy Search and that reparameterization-based algorithms such Stochastic Value Gradient can be interpreted as counterfactual methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imagine that a month ago Alice had two job offers from companies $a_{1}$ and $a_{2}$. She decided to join $a_{1}$ because of the larger salary, in spite of an awkward feeling during the job interview. Since then she learned a lot about $a_{1}$ and recently received information about $a_{2}$ from a friend, prodding her now to imagine what would have happened had she joined $a_{2}$. Re-evaluating her decision in hindsight in this way, she concludes that she made a regrettable decision. She could and should have known that $a_{2}$ was a better choice, had she only interpreted the cues during the interview correctly... This example tries to illustrate the everyday human capacity to reason about alternate, counterfactual outcomes of past experience with the goal of "mining worlds that could have been". Social psychologists theorize that such cognitive processes are beneficial for improving future decision making. In this paper we aim to leverage possible advantages of counterfactual reasoning for learning decision making in the reinforcement learning (RL) framework.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In spite of recent success, learning policies with standard, model-free RL algorithms can be notoriously data inefficient. This issue can in principle be addressed by learning policies on data synthesized from a model. However, a mismatch between the model and the true environment, often unavoidable in practice, can cause this approach to fail, resulting in policies that do not generalize to the real environment. Motivated by the introductory example, we propose the Counterfactually-Guided Policy Search (CF-GPS) algorithm: Instead of relying on data synthesized *from scratch* by a model, we train policies on model predictions of alternate outcomes of past experience from the true environment under *counterfactual* actions, i.e. actions that had not actually been taken, while everything else remaining the same. At the heart of CF-GPS are structural causal models (SCMs) which model the environment with two ingredients: 1) Independent random variables, called *scenarios* here, summarize all aspects of the environment that cannot be influenced by the agent, e.g. the properties of the companies in Alice's job search example.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

2) Deterministic transition functions (also called *causal mechanisms*) take these scenarios, together with the agent's actions, as input and produce the predicted outcome. The central idea of CF-GPS is that, instead of running an agent on scenarios sampled de novo from a model, we infer scenarios in hindsight from given off-policy data, and then evaluate and improve the agent on these *specific* scenarios using given or learned causal mechanisms. We show that CF-GPS generalizes and empirically improves on a vanilla model-base RL algorithm, by mitigating model mismatch via "grounding" or "anchoring" model-based predictions in inferred scenarios. As a result, this approach explicitly allows to trade-off historical data for model bias. CF-GPS differs substantially from standard off-policy RL algorithms based on Importance Sampling (IS), where historical data is *re-weighted* with respect to the importance weights to evaluate or learn new policies. In contrast, CF-GPS explicitly reasons counterfactually about given off-policy data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We formulate model-based RL in POMDPs in terms of structural causal models, thereby connecting concepts from reinforcement learning and causal inference.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide the first results, to the best of our knowledge, showing that counterfactual reasoning in structural causal models on off-policy data can facilitate solving non-trivial RL tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that two previously proposed classes of RL algorithms, namely Guided Policy Search and Stochastic Value Gradient methods, can be interpreted as counterfactual methods, opening up possible generalizations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is structured as follows. We first give a self-contained, high-level recapitulation of structural causal models and counterfactual inference, as these are less widely known in the RL and generative model communities. In particular we show how to model POMDPs with SCMs. Based on this exposition, we first consider the task of policy evaluation and discuss how we can leverage counterfactual inference in SCMs to improve over naive model-based methods. We then generalize this approach to the policy search setting resulting in the CF-GPS algorithm. We close by highlighting connections to previously proposed algorithms and by discussing assumptions and limitations of the proposed method.

<!-- chunk {"id": "body-0011", "role": "body", "section": "SCM representation of POMDPs", "weight": 1.0} -->

We can represent any given POMDP (under a policy $\pi$) by an SCM $\mathcal{M}$ over trajectories $\mathcal{T}$ in the following way. We express all conditional distributions, e.g. the transition kernel $P_{S_{t + 1}|{S_{t},A_{t}}}$, as deterministic functions with independent noise variables $U$, such as $S_{t + 1} = {f_{st}{(S_{t},A_{t},U_{st})}}$. This is always possible using auto-regressive uniformization, see Lemma 2. ‣ Appendix B Details on casting a POMDP into SCM form ‣ Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search") in the appendix. The DAG $\mathcal{G}$ of the resulting SCM is shown in fig. 1. This procedure is closely related to the 'reparameterization trick' for models with location-scale distributions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "SCM representation of POMDPs", "weight": 1.0} -->

We denote the distribution over $\mathcal{T}$ entailed by the SCM with $P^{\pi}$ and its density by $p^{\pi}$ to highlight the role of $\pi$; note the difference to the true environment distribution ${\mathfrak{P}}^{\pi}$ with density ${\mathfrak{p}}^{\pi}$. Running a different policy $\mu$ instead of $\pi$ in the environment can be expressed as an intervention $I{({\pi\rightarrow\mu})}$ consisting of replacing $A_{t} = {f_{\pi}{(H_{t},U_{at})}}$ by $A_{t} = {f_{\mu}{(H_{t},U_{at})}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Intuition", "weight": 1.0} -->

Here, we illustrate the main advantage of SCMs using the example of Alice's job choice from the introduction. We model it as contextual bandit with feedback shown in fig. 1. Alice has some initial knowledge given by the context $U_{c}$ that is available to her before taking action $A$ of joining company $A = a_{1}$ or $A = a_{2}$. We model Alice's decision as $A = {f_{\pi}{(U_{c},U_{a})}}$, where $U_{a}$ captures potential indeterminacy in Alice's decision making.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Intuition", "weight": 1.0} -->

The outcome $O = {f_{o}{(A,U_{c},U_{o})}}$ also depends on the scenario $U_{o}$, capturing all relevant, unobserved and highly complex properties of the two companies such as working conditions etc. Given this model, we can reason about alternate outcomes $f_{o}{(a_{1},u_{c},u_{o})}$ and $f_{o}{(a_{2},u_{c},u_{o})}$ for *same* the scenario $u_{o}$. This is not possible if we only model the outcome on the level of the conditional distribution $P_{O|{A,U_{c}}}.$

<!-- chunk {"id": "body-0015", "role": "body", "section": "Counterfactual inference in SCMs", "weight": 1.0} -->

For an SCM over $X$, we define a *counterfactual query* as a triple $({\hat{x}}_{o},I,X_{q})$ of observations ${\hat{x}}_{o}$ of some variables $X_{o} \subset X$, an intervention $I$ and query variables $X_{q} \subset X$. The semantics of the query are that, having observed ${\hat{x}}_{o}$, we want to infer what $X_{q}$ would have been had we done intervention $I$, while '*keeping everything else the same*'.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Counterfactual inference in SCMs", "weight": 1.0} -->

Note that our definition explicitly allows for partial observations $X_{o} \subset X$ in accordance with Pearl. A sampled-based version, denoted as CFI, is presented in Algorithm 1. An interesting property of the counterfactual distribution $p^{{{do}{(I)}}|{\hat{x}}_{o}}$ is that marginalizing it over observations ${\hat{x}}_{o}$ yields an unbiased estimator of the density of $X_{q}$ under intervention $I$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Intuition", "weight": 1.0} -->

Returning to Alice's job example from the introduction, we give some intuition for counterfactual inference in SCMs. Given the concrete outcome $\hat{o}$, under observed context ${\hat{u}}_{c}$ and having joined company $\hat{a} = a_{1}$, Alice can try to infer the underlying scenario $u_{o} \sim {p{(\left. u_{o} \middle| {a_{1},{\hat{u}}_{c},\hat{o}} \right.)}}$ that she experiences; this includes factors such as work conditions etc. She can then reason counterfactually about the outcome had she joined the other company, which is given by $f_{o}{(a_{2},{\hat{u}}_{c},u_{o})}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Intuition", "weight": 1.0} -->

This can in principle enable her to make better decisions in the future in similar scenarios by changing her policy $f_{\pi}{(A,U_{c},U_{a})}$ such that the action with the preferred outcome becomes more likely under ${\hat{u}}_{c},u_{o}$. In particular she can do so without having to use her (likely imperfect) prior model over possible companies $p{(U_{o})}$. She can use the counterfactual predictions discussed above instead to learn from her experience. We use this insight for counterfactual policy evaluation and search below.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Off-policy evaluation: Model-free, model-based and counterfactual", "weight": 1.0} -->

If we have access to a model $\mathcal{M}$, then we can evaluate the policy on synthetic data, i.e. we can estimate ${\mathbb{E}}_{p^{\pi}}{\lbrack G\rbrack}$. This is called model-based policy evaluation (MB-PE). However, any bias in $\mathcal{M}$ propagates from $p^{\pi}$ to the estimate ${\mathbb{E}}_{p^{\pi}}{\lbrack G\rbrack}$. In the following, we assume that $\mathcal{M}$ is a SCM and we show that we can use counterfactual reasoning for off-policy evaluation (CF-PE). As the main result for this section, we argue that we expect CF-PE to be less biased than MB-PE, and we illustrate this point with experiments.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Counterfactual off-policy evaluation", "weight": 1.0} -->

1:// Counterfactual inference (CFI)
2:procedure CFI(data x̂o, SCM ℳ, intervention I, query Xq)
3: û ∼ p (u|x̂o) ⊳ Sample noise variables from posterior
4: p (u) ← δ (u−û) ⊳ Replace noise distribution in p with û
5: fi ← fiI ⊳ Perform intervention I
6: return xq ∼ pdo (I) (xq|û) ⊳ Simulate from the resulting model ℳx̂oI

<!-- chunk {"id": "body-0021", "role": "body", "section": "Counterfactual off-policy evaluation", "weight": 1.0} -->

8:// Counterfactual Policy Evaluation (CF-PE)
9:procedure CF-PE(SCM ℳ, policy π, replay buffer D, number of samples N)
11: ĥTi ∼ D ⊳ Sample from the replay buffer
12: gi = CFI (ĥTi,ℳ,I (μ→π),G) ⊳ Counterfactual evaluation of return
14: return $\frac{1}{N}{\sum_{i = 1}^{N}g_{i}}$

<!-- chunk {"id": "body-0022", "role": "body", "section": "Counterfactual off-policy evaluation", "weight": 1.0} -->

16:// Counterfactually-Guided Policy Search (CF-GPS)
17:procedure CF-GPS(SCM ℳ, initial policy π0, number of trajectory samples N)
20: μ ← πk ⊳ Update behavior policy
23: ĥTi ∼ 𝔭μ ⊳ Get off-policy data from the true environment
24: τi = CFI (ĥTi,ℳ,I (μ→πλ),𝒯) ⊳ Counterfactual rollouts under planner
26: πk← policy improvement on trajectories τi = 1, …, N using eqn. 1
Algorithm 1 Counterfactual policy evaluation and search

<!-- chunk {"id": "body-0023", "role": "body", "section": "Counterfactual off-policy evaluation", "weight": 1.0} -->

Naive MB-PE with a SCM $\mathcal{M}$ simply consist of sampling the scenarios $U \sim P_{U}$ from the prior, and then simulating a trajectory $\tau$ from the functions $f_{i}$ and computing its return. However, given data $D$ from ${\mathfrak{p}}^{\mu}$, our discussion of counterfactual inference in SCMs suggests the following alternative strategy: Assuming no model mismatch, i.e. ${\mathfrak{p}}^{\mu} = p^{\mu}$, we can regard the task of off-policy evaluation of $\pi$ as a counterfactual query with data ${\hat{h}}_{T}^{i}$, intervention $I{({\mu\rightarrow\pi})}$ and query variable $G$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Counterfactual off-policy evaluation", "weight": 1.0} -->

In other words, instead of sampling from the prior as in MB-PE, we are free to the scenarios from the posterior $u^{i} \sim p^{\mu}{( \cdot |{\hat{h}}_{T}^{i})}$. The algorithm is given in Algorithm 1. Lemma 1. ‣ 2.2

<!-- chunk {"id": "body-0025", "role": "body", "section": "Motivation", "weight": 1.0} -->

When should one prefer CF-PE over the more straightforward MB-PE? Assuming a perfect model, Corollary 2. ‣ 3.1 Counterfactual off-policy evaluation ‣ 3 Off-policy evaluation: Model-free, model-based and counterfactual ‣ Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search") states that both yield the same answer in expectation for perfect models. For imperfect models however, these algorithms can differ substantially. MB-PE relies on purely synthetic data, sampled from the noise distribution $p{(U)}$. In practice, this is usually approximated by a parametric density model, which can lead to under-fitting in case of complex distributions. This is a well-known effect in generative models with latent variables: In spite of recent research progress, e.g. models of natural images are still unable to accurately model the variability of the true data. In contrast, CF-PE samples from the posterior $N^{- 1}{\sum_{i = 1}^{N}{p^{\mu}{(\left.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Motivation", "weight": 1.0} -->

U \middle| {\hat{h}}_{T}^{i} \right.)}}}$, which has access to strictly more information than the prior $p{(U)}$ by taking into account additional data ${\hat{h}}_{T}^{i}$. This semi-nonparametric distribution can help to de-bias the model by effectively winnowing out parts of the domain of $U$ which do not correspond to any real data. We substantiate this intuition with experiments below; a concrete illustration for the difference between the prior and posterior / counterfactual distribution is given in fig. 4 in the appendix and discussed in appendix D. Therefore, we conclude that we expect CF-PE to outperform MB-PE, if the transition and reward kernels $f_{st}$ are accurate models of the environment dynamics, but if the marginal distribution over the noise sources $P_{U}$ is difficult to model.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Environment", "weight": 1.0} -->

As an example, we use a partially-observed variant of the SOKOBAN environment, which we call PO-SOKOBAN. The original SOKOBAN puzzle environment was described in detail by Racanière et al.; we give a brief summary here. The agent is situated in a $10 \times 10$ grid world and its five actions are to move to one of four adjacent tiles and a NOOP. In our variant, the goal is to push all three boxes onto the three targets. As boxes cannot be pulled, many actions result irreversibly in unsolvable states. Episodes are of length $T = 50$, and pushing a box onto a target yields a reward of $1$, removing a box from a target yields $- 1$, and solving a level results in an additional reward of $10$. The state of the environment consists in a $10 \times 10$ matrix of categorical variables taking values in $\{ 0,\ldots,6\}$ indicating if the corresponding tile is empty, a wall, box, target, agent, or a valid combinations thereof (box+target and agent+target).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Environment", "weight": 1.0} -->

In order to introduce partial observability, we define the observations as the state corrupted by i.i.d. (for each tile and time step) flipping each categorical variable to the "empty" state with probability $0.9$. Therefore, the state of the game is largely unobserved at any given time, and a successful agent has to integrate observations over tens of time steps. Initial states $U_{s1}$, also called *levels*, which are the scenarios in this environment, are generated randomly by a generator algorithm which guarantees solvability (i.e. all boxes can be pushed onto targets). The environment is visualized in fig. 3 in the appendix.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Environment", "weight": 1.0} -->

Given the full state of PO-SOKOBAN, the transition kernel is deterministic and quite simple as only the agent and potentially an adjacent box moves. Inferring the belief state, i.e. the distribution over states given the history of observations and actions, can however range from trivial to very challenging, depending on the amount of available history. In the limit of a long observed history, every tile is eventually observed and the belief state concentrates on a single state (the true state) that can be easily inferred. With limited observed history however, inferring the posterior distribution over states (belief state) is very complex. Consider e.g. the situation in the beginning of an episode (before pushing the first box). Only the first observation is available, however we know that all PO-SOKOBAN levels are initially guaranteed to be solvable and therefore satisfy many combinatorial constraints reflecting that the agent is still able to push all boxes onto targets. Learning a compact parametric model of the initial state distribution from empirical data is therefore difficult and likely results in large mismatch between the learned model and the true environment.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

To illustrate the potential advantages of CF-PE over MB-PE we perform policy evaluation in the PO-SOKOBAN environment. We first generate a policy $\pi$ that we wish to evaluate, by training it using a previously-proposed distributed RL algorithm. The policy is parameterized as a deep, recurrent neural network consisting of a 3-layer deep convolutional LSTM with 32 channels per layer and kernel size of 3. To further increase computational power, the LSTM ticks twice for each environment step. The output of the agent is a value function and a softmax yielding the probabilities of taking the 5 actions. In order to obtain an SCM of the environment, for the sake of simplicity, we assume that the ground-truth transition, observation and reward kernels are given. Therefore the only part of the model that we need to learn is the distribution $p{(U_{s1})}$ of initial states $S_{1} = U_{s1}$ (for regular MB-PE), and the density $p{(\left.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

U_{s1} \middle| {\hat{h}}_{t}^{i} \right.)}$ for inferring levels in hindsight for CF-PE. We vary the amount of true data $t$ that we condition this inference, ranging from $t = 0$ (no real data, equivalent to MB-PE) to $t = T = 50$ (a full episode of real data is used to infer the initial state $U_{s1}$). We train a separate model for each $t \in {\{ 0,5,10,20,30,40,50\}}$. To simplify model learning, both models were given access to the unobserved state during training, but not at test time. The models are chosen to be powerful, multi-layer, generative DRAW models trained by approximate maximum likelihood learning. The models take as input the (potentially empty) data ${\hat{h}}_{t}^{i}$ summarized by a backward RNN (a standard convolutional LSTM model with 32 units). The model is shown in fig.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

3 in the appendix and additional details are given in appendix C. The data ${\hat{h}}_{T}^{i}$ was collected under a uniform random policy $\mu$. For all policy evaluations, we use $\approx > 10^{5}$ levels $u^{i}$ from the inferred model. In order to evaluate policies of different proficiency, we derive from the original (trained) $\pi$ three policies $\pi_{0},\pi_{1},\pi_{2}$ ranging from almost perfect to almost random performance by introducing additional stochasticity during action selection.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

The policy evaluation results are shown in fig. 2. We found that for $t = 0$, in spite of extensive hyper-parameter search, the model $p{(U_{s1})}$ was unable to accurately capture the marginal distribution of initial levels in PO-SOKOBAN. As argued above, a solvable level satisfies a large number of complex constraints that span the entire grid world, which are hard for a parametric model to capture. Empirically, we found that the model mismatch manifested itself in samples from $p{(U_{s1})}$ not being well-formed, e.g. not solvable, and hence the performance of the policies $\pi_{i}$ are very different on these synthetic levels compared to levels sampled form $\mathfrak{p}$. However, inferring levels from full observed episodes i.e. $p{(\left. U_{s1} \middle| {\hat{h}}_{50}^{i} \right.)}$ was reliable, and running $\pi$ on these resulted in accurate policy evaluation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

The figure also shows the trade-off between policy evaluation accuracy and the amount of off-policy data for intermediate amounts of the data ${\hat{h}}_{t}^{i}$. We also want to emphasize that in this setting, model-free policy evaluation by IS fails. The uniform behavior policy $\mu$ was too different from $\pi^{i}$, resulting in a relative error $> 0.8$ for all $i = {1,2,3}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Off-Policy improvement: Counterfactually-guided policy search", "weight": 1.0} -->

In the following we show how we can leverage the insights from counterfactual policy evaluation for policy search. We commence by considering a model-based RL algorithm and discuss how we can generalize it into a counterfactual algorithm to increase its robustness to model mismatch. We chose a particular algorithm to start from to make a connection to the previously proposed Guided Policy Search algorithm, but we think a larger class of MBRL algorithms can be generalized in an analogous manner.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Starting point: Vanilla model-based RL with return weighted regression", "weight": 1.0} -->

We start from the following algorithm. We assume we have a model $\mathcal{M}$ of the environment with trajectory distribution $p^{\pi}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Starting point: Vanilla model-based RL with return weighted regression", "weight": 1.0} -->

where $G{(\tau)}$ is the return of trajectory $\tau$. This policy improvement step can be motivated by the framework of RL as variational inference and is equivalent to minimizing the KL divergence to a trajectory distribution $\propto {{\exp{(G)}}p^{\pi^{k}}}$ which puts additional mass on high-return trajectories. Although not strictly necessary for our exposition, we also allow for a dedicated proposal distribution over trajectories $p^{\lambda}{(\tau)}$, under a policy $\lambda$. We refer to $\lambda$ as a *planner* to highlight that it could consist of a procedure that solves episodes starting from arbitrary, full states $s_{1}$ sampled form the model, by repeatedly calling the model transition kernel, e.g. a search procedure such as MCTS or an expert policy.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Starting point: Vanilla model-based RL with return weighted regression", "weight": 1.0} -->

We refer to this algorithm as model-based policy search (MB-PS). It is based on model rollouts $\tau^{i}$ spanning entire episodes. An alternative would be to consider model rollouts starting from states visited in the real environment (if available). Both versions can be augmented by counterfactual methods, but for the sake of simplicity we focus on the simpler MB-PS version detailed above (also we did not find significant performance differences experimentally between both versions).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Incorporating off-policy data: Counterfactually-guided policy search", "weight": 1.0} -->

Now, we assume that the model $\mathcal{M}$ is an SCM. Based on our discussion of counterfactual policy evaluation, it is straightforward to generalize the MB-PS described above by anchoring the rollouts $\tau^{i}$ under the model $p^{\lambda}$ in off-policy data $D$: Instead of sampling $\tau^{i}$ directly from the prior $p^{\lambda}$, we draw them from counterfactual distribution $p^{\lambda|{\hat{h}}_{T}^{i}}$ with data ${\hat{h}}_{T}^{i} \sim D$ from the replay buffer, i.e. instead of sampling the scenarios $U$ from the prior we infer them from the given data. Again invoking Lemma 1. ‣ 2.2 Counterfactual inference in SCMs ‣ 2 Preliminaries ‣ Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search"), this procedure is unbiased under no model mismatch.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Incorporating off-policy data: Counterfactually-guided policy search", "weight": 1.0} -->

We term the resulting algorithm Counterfactually-Guided Policy Search (CF-GPS), and it is summarized in Algorithm 1. The motivation for using CF-GPS over MB-PS is analogous to the advantage of CF-PE over MB-PE discussed in sec. 3.1. The policy $\pi$ in CF-GPS is optimized on rollouts $\tau^{i}$ that are grounded in data ${\hat{h}}_{T}^{i}$ by sampling them from the counterfactual distribution $p^{\lambda|{\hat{h}}_{T}^{i}}$ instead of the prior $p^{\lambda}$. If this prior is difficult to model, we expect the counterfactual distribution to be more concentrated in regions where there is actual mass under the true environment ${\mathfrak{p}}^{\lambda}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate CF-GPS on the PO-SOKOBAN environment, using a modified distributed actor-learner architecture based on Espeholt et al.: Multiple actors (here 64) collect real data ${\hat{h}}_{T}$ by running the behavior policy $\mu$ in the true environment $\mathfrak{p}$. As in many distributed RL settings, $\mu$ is chosen to be a copy of the policy $\pi$, often slightly outdated, so the data must be considered to be off-policy. The distribution $p{(\left. U_{s1} \middle| {\hat{h}}_{T} \right.)}$ over levels $U_{s1}$ is inferred from the data ${\hat{h}}_{T}$ using from the model $\mathcal{M}$. We sample a scenario $U_{s1}$ for each logged episode, and simulate $10$ counterfactual trajectories $\tau^{1,\ldots,10}$ under the planner $\lambda$ for each such scenario.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

Here, for the sake of simplicity, instead of using search, the planner was assumed to be a mixture between $\pi$ and a pre-trained expert policy $\lambda_{e}$, i.e. $\lambda = {{\beta\lambda_{e}} + {{({1 - \beta})}\pi}}$. The schedule $\beta$ was set to an exponentially decaying parameter with time constant $10^{5}$ episodes. The learner performs policy improvement on $\pi$ using $\tau^{1,\ldots,10}$ according to eqn. 1. $\mathcal{M}$ was trained online, in the same way as in sec. 3.2. $\lambda$ and $\pi$ were parameterized by deep, recurrent neural networks with the same architecture described in sec. 3.2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare CF-GPS with the vanilla MB-PS baseline described in sec. 4.1 (based on the same number of policy updates). MB-PS differs from CF-GPS by just having access to an unconditional model $p{(\left. U_{s1} \middle| \varnothing \right.)}$ over initial states. We also consider a method which conditions the scenario model $p{(\left. U_{s1} \middle| o_{1} \right.)}$ on the very first observation $o_{1}$, which is available when taking the first action and therefore does not involve hindsight reasoning. This is more informed compared to MB-PS; however due to the noise on the observations, the state is still mostly unobserved rendering it very challenging to learn a good parametric model of the belief state $p{(\left. U_{s1} \middle| o_{1} \right.)}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

We refer to this algorithm as Guided Policy Search-like (GPS-like), as it roughly corresponds to the algorithm presented by Levine & Abbeel, as discussed in greater detail in sec. 5. Fig. 2 shows that CF-GPS outperforms these two baselines. As expected from the policy evaluation experiments, initial states sampled from the models for GPS and MB-PS are often not solvable, yielding inferior training data for the policy $\pi$. In CF-GPS, the levels are inferred from hindsight inference $p{(\left. U_{1} \middle| {\hat{h}}_{T} \right.)}$, yielding high quality training data. For reference, we also show a policy trained by the model-free method of Espeholt et al. using the same amount of environment data. Not surprisingly, CF-GPS is able to make better use of the data compared to the model-free baseline as it has access to the true transition and reward kernels (which were not given to the model-free method).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Guided Policy Search (GPS)", "weight": 1.0} -->

CF-GPS is closely related to GPS, in particular we focus on GPS as presented by Levine & Abbeel. Consider CF-GPS in the fully-observed MDP setting where $O_{t} = S_{t}$. Furthermore, assume that the SCM $\mathcal{M}$ is structured as follows: Let $S_{t + 1} = {f_{s}{(S_{t},A_{t},U_{st})}}$ be a linear function in $(S_{t},A_{t})$ with coefficients given by $U_{st}$. Further, assume an i.i.d. Gaussian mixture model on $U_{st}$ for all $t$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Guided Policy Search (GPS)", "weight": 1.0} -->

As the states are fully observed, the inference step in the CFI procedure simplifies: we can infer the noise sources ${\hat{u}}_{st}$ (samples or MAP estimates), i.e. the unknown linear dynamics, from pairs of observed, true states ${\hat{s}}_{t},{\hat{s}}_{t + 1}$. Furthermore assume that the reward is a quadratic function of the state. Then, the counterfactual distribution $p^{\lambda}{(\left. \tau \middle| \hat{u} \right.)}$ is a linear quadratic regulator (LQR) with time-varying coefficients $\hat{u}$. An appropriate choice for the planner $\lambda$ is the optimal linear feedback policy for the given LQR, which can be computed exactly by dynamic programming.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Observation 1", "weight": 1.0} -->

In the MDP setting, CF-GPS with a linear SCM and a dynamic programming planner for LQRs $\lambda$ is equivalent to GPS.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Observation 1", "weight": 1.0} -->

Another perspective is that GPS is the counterfactual version of the MB-PS procedure from sec. 4.1:

<!-- chunk {"id": "body-0049", "role": "body", "section": "Observation 2", "weight": 1.0} -->

In the MDP setting with a linear SCM and a dynamic programming planner for LQRs $\lambda$, GPS is the counterfactual variant of the MB-PS procedure outlined above.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Observation 2", "weight": 1.0} -->

The fact that GPS is a successful algorithm in practice shows that the 'grounding' of model-based search / rollouts in real, off-policy data afforded by counterfactual reasoning massively improves the naive, 'prior sample'-based MB-PS algorithm. These considerations also suggest when we expect CF-GPS to be superior compared to regular GPS: If the uncertainty in the environment transition $U_{st}$ cannot be reliably identified from subsequent pairs of observations ${\hat{o}}_{t},{\hat{o}}_{t + 1}$ alone, we expect benefits of inferring $U_{st}$ from a larger context of observations, in the extreme case from the entire history ${\hat{h}}_{T}$ as described above.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Stochastic Value Gradient methods", "weight": 1.0} -->

There are multiple interesting connections of CF-GPS to Stochastic Value Gradient (SVG) methods. In SVG, a policy $\pi$ for a MDP is learned by gradient ascent on the expected return under a model $p$. Instead of using the score-function estimator, SVG relies on a reparameterization of the stochastic model and policy. We note that this reparameterization casts $p$ into an SCM. As in GPS, the noise sources $U_{st}$ are inferred from two subsequent observed states ${\hat{s}}_{t},{\hat{s}}_{t + 1}$ from the true environment, and the action noise $U_{at}$ is kept frozen. As pointed out in the GPS discussion, this procedure corresponds to the inference step in a counterfactual query. Given inferred values $u$ for $U$, gradients $\partial_{\theta}G$ of the return under the model are taken with respect to the policy parameters $\theta$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Stochastic Value Gradient methods", "weight": 1.0} -->

We can loosely interpret these gradients as $2\dim{(\theta)}$ counterfactual policy evaluations of policies $\pi{({\theta \pm {\Delta\theta_{i}}})}$ where a single dimension $i$ of the parameter vector $\theta$ is perturbed.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

Simulating plausible synthetic experience de novo is a hard problem for many environments, often resulting in biases for model-based RL algorithms. The main takeaway from this work is that we can improve policy learning by evaluating counterfactual actions in concrete, past scenarios. Compared to only considering synthetic scenarios, this procedure mitigates model bias. However, it relies on some crucial assumptions that we want to briefly discuss here. The first assumption is that off-policy experience is available at all. In cases where this is e.g. too costly to acquire, we cannot use any of the proposed methods and have to exclusively rely on the simulator / model. We also assumed that there are no additional hidden confounders in the environment and that the main challenge in modelling the environment is capturing the distribution of the noise sources $p{(U)}$, whereas we assumed that the transition and reward kernels given the noise is easy to model. This seems a reasonable assumption in some environments, such as the partially observed grid-world considered here, but not all. Probably the most restrictive assumption is that we require the inference over the noise $U$ given data ${\hat{h}}_{T}$ to be sufficiently accurate.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion", "weight": 1.5} -->

We showed in our example, that we could learn a parametric model of this distribution from privileged information, i.e. from joint samples $u,h_{T}$ from the true environment. However, imperfect inference over the scenario $U$ could result e.g. in wrongly attributing a negative outcome to the agent's actions, instead environment factors. This could in turn result in too optimistic predictions for counterfactual actions. Future research is needed to investigate if learning a sufficiently strong SCM is possible without privileged information for interesting RL domains. If, however, we can trust the transition and reward kernels of the model, we can substantially improve model-based RL methods by counterfactual reasoning on off-policy data, as demonstrated in our experiments and by the success of Guided Policy Search and Stochastic Value Gradient methods.
