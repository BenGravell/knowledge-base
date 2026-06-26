<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Being Optimistic to Be Conservative: Quickly Learning a CVaR Policy

Topics include Reinforcement learning, Bellman equations, Uncertainty, Learning, Conservative, Conditional value at risk, Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While maximizing expected return is the goal in most reinforcement learning approaches, risk-sensitive objectives such as conditional value at risk (CVaR) are more suitable for many high-stakes applications. However, relatively little is known about how to explore to quickly learn policies with good CVaR. In this paper, we present the first algorithm for sample-efficient learning of CVaR-optimal policies in Markov decision processes based on the optimism in the face of uncertainty principle. This method relies on a novel optimistic version of the distributional Bellman operator that moves probability mass from the lower to the upper tail of the return distribution. We prove asymptotic convergence and optimism of this operator for the tabular policy evaluation case. We further demonstrate that our algorithm finds CVaR-optimal policies substantially faster than existing baselines in several simulated environments with discrete and continuous state spaces.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key goal in reinforcement learning (RL) is to quickly learn to make good decisions by interacting with an environment. In most cases the quality of the decision policy is evaluated with respect to its expected (discounted) sum of rewards. However, in many interesting cases, it is important to consider the full distributions over the potential sum of rewards, and the desired objective may be a risk-sensitive measure of this distribution. For example, a patient undergoing a surgery for a knee replacement will (hopefully) only experience that procedure once or twice, and may will be interested in the distribution of potential results for a single procedure, rather than what may happen on average if he or she were to undertake that procedure hundreds of time. Finance and (machine) control are other cases where interest in risk-sensitive outcomes are common.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A popular risk-sensitive measure of a distribution of outcomes is the Conditional Value at Risk (CVaR) (?). Intuitively, CVaR is the expected reward in the worst $\alpha$-fraction of outcomes, and has seen extensive use in financial portfolio optimization (?), often under the name "expected shortfall". While there has been recent interest in the RL community in learning to converge or identify good CVaR decision policies in Markov decision processes (?; ?; ?; ?), interestingly we are unaware of prior work focused on how to quickly learn such CVaR MDP policies, even though sample efficient RL for maximizing expected outcomes is a deep and well studied theoretical (?; ?) and empirical (?) topic. Sample efficient exploration seems of equal or even more importance in the case when the goal is risk-averse outcomes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we work towards sample efficient reinforcement learning algorithms that can quickly identify a policy with an optimal CVaR. Our focus is in minimizing the amount of experience needed to find such a policy, similar in spirit to probably approximately correct RL methods for expected reward. Note that this is different than another important topic in risk-sensitive RL, which focuses on safe exploration: algorithms that focus on avoiding any potentially very poor outcomes during learning. These typically rely on local smoothness assumptions and do not typically focus on sample efficiency (?; ?); an interesting question for future work is whether one can do both safe and efficient learning of a CVaR policy. Our work is suitable for the many settings where some outcomes are undesirable but not catastrophic.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach is inspired by the popular and effective principle of optimism in the face of uncertainty (OFU) in sample efficient RL for maximizing expected outcomes (?; ?). Such work typically works by considering uncertainty over the MDP model parameters or state-action value function, and constructing an optimistic value function given that uncertainty that is then used to guide decision making. To take a similar idea for rapidly learning the optimal CVaR policy, we seek to consider the uncertainty in the distribution of outcomes possible and the resulting CVaR value. To do so, we use the Dvoretzky-Kiefer-Wolfowitz (DKW) inequality---while to our knowledge this has not been previously used in reinforcement learning settings, it is a very useful concentration inequality for our purposes as it provides bounds on the true cumulative distribution function (CDF) given a set of sampled outcomes. We leverage these bounds in order to compute optimistic estimates of the optimal CVaR.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our interest is in creating empirically efficient and scalable algorithms that have a theoretically sound grounding. To that end, we introduce a new algorithm for quickly learning a CVaR policy in MDPs and show that at least in the evaluation case in tabular MDPs, this algorithm indeed produces optimistic estimates of the CVaR. We also show that it does converge eventually. We accompany the theoretical evidence with an empirical evaluation. We provide encouraging empirical results on a machine replacement task (?), a classic MDP where risk sensitive policies are critical, as well as a well validated simulator for type 1 diabetes (?) and a simulated treatment optimization task for HIV (?). In all cases we find a substantial benefit over simpler exploration strategies. To our knowledge this is the first algorithm that performs strategic exploration to learn good CVaR MDP policies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Distributional Reinforcement Learning", "weight": 1.0} -->

Distributional RL methods apply a sample-based approximation to distributional versions of the usual Bellman operators. For example, one can define a distributional Bellman operator (?) as $\mathcal{T}^{\pi}:{\mathcal{Z}\rightarrow\mathcal{Z}}$ as where $\overset{D}{=}$ denotes equality in distribution, and the transition operator is defined as ${P^{\pi}Z{(s,a)}}\overset{D}{:=}{Z{(s',a')}}$ with $s' \sim P{(\cdot |s,a)}$, $a' \sim {\pi{(s)}}$. The optimality version $\mathcal{T}$ is similarly any ${\mathcal{T}Z} = {\mathcal{T}^{\pi}Z}$ where $\pi$ is an optimal policy w.r.t. expected return. Note that this is not necessarily unique when there are multiple optimal policies.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Distributional Reinforcement Learning", "weight": 1.0} -->

(?) showed that $\mathcal{T}^{\pi}$ is a $\sqrt{\gamma}$-contraction in the Cramér-metric, ${\overline{\ell}}_{2}$ One of the canonical algorithms in distributional RL is CDRL or C51 (?) which represent the return distribution $Z^{\pi}$ as a discrete distribution with fixed support on $N$ atoms ${{\{{z_{i} = {V_{\min} + {i\Deltaz}}}:{0 \leq i < N}\}},{\Deltaz}}:=\frac{V_{\max} - V_{\min}}{N - 1}$ the discrete distribution is parameterized as $\theta:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}^{N}}$: Essentially, C51 uses a sample transition $(s,a,r,s')$ to perform an approximate Bellman backup

<!-- chunk {"id": "body-0010", "role": "body", "section": "Optimistic Distributional Operator", "weight": 1.0} -->

In contrast to the typical RL setup where an agent tries to maximize its expected return, we seek to learn a stationary policy that maximizes the ${CVaR}_{\alpha}$ of the return at risk level $\alpha$.^11^1Note that the $CVaR$-optimal policy at any state can be non-stationary (?), as it depends on the sum of rewards achieved up to that state. For simplicity, as (?) we instead seek a stationary policy, which will generally can be suboptimal but typically still achieve high CVaR, as observed in our experiments. To find such policies quickly, we follow the optimism-in-the-face-of-uncertainty (OFU) principle and introduce optimism in our CVaR estimates to guide exploration. While adding a bonus to rewards is a popular approach for optimism in the standard expected return case (?), we here follow a different approach and introduce optimism into our return estimates by shifting the empirical CDFs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Optimistic Distributional Operator", "weight": 1.0} -->

Formally, consider a return distribution ${Z{(s,a)}} \in \mathcal{Z}$ with CDF $F_{Z{(s,a)}}{(x)}$. We define the optimism operator $O_{c}:{\mathcal{Z}\rightarrow\mathcal{Z}}$ as where $c$ is a constant and ${(\cdot)}^{+}$ is short for $\max{\{ \cdot,0\}}$. In the definition above, $n{(s,a)}$ is the number of times the pair $(s,a)$ has been observed so far or an approximation such as pseudo-counts (?). By shifting the cumulative distribution function down, this operator essentially puts probability mass from the lower tail to the highest possible value $V_{\max}$. An illustration is provided in Figure 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimistic Distributional Operator", "weight": 1.0} -->

This approach to optimism is motivated by an application of the DKW-inequality to the empirical CDF. As shown recently by (?), this can yield tighter upper confidence bounds on the CVaR.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

The optimistic operator introduced above operates on the entire return distribution and our algorithm introduced in the next section combines this optimistic operator to estimated return-to-go distributions. As such, it belongs to the family of distributional RL methods (?). These methods are a recent development and come with strong asymptotic convergence guarantees when used for *policy evaluation* in tabular MDPs (?). Yet, finite sample guarantees such as regret or PAC bounds still remain elusive for distributional RL policy optimization algorithms.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

A key technical challenge in proving performing bounds for distributionally robust policy optimization during RL is that convergence of the distributional Bellman optimality operator can generally not be guaranteed. Prior results have only showed that if the optimization process itself is to compute a policy which maximizes expected returns, such as Q-learning, then convergence of the distirbutional Bellman optimality operator is guaranteed to converge. (?, Theorem 2). Note however that if the goal is to leverage distributional information to compute a policy to maximize something other than expected outcomes, such as a risk sensitive policy like we consider here, no prior theoretical results are known in the reinforcement learning setting to our knowledge. However, it is promising that there is some empirical evidence that one can compute risk-sensitive policies using distributional Bellman operators (?) which suggests that more theoretical results may be possible.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Here we take a first step towards this goal. Our primary aim in this work is to provide tools to introduce optimism into distributional return-to-go estimates to guide sample-efficient exploration for CVaR. Therefore, our theoretical analysis focuses on showing that this form of optimism does not harm convergence and is indeed a principled way to obtain optimistic CVaR estimates.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

First, we prove that the optimism operator is a non-expansion in the Cramér distance. This results shows that this operator can be used with other contraction operators without negatively impacting the convergence behaviour. Specifically we can guarantee convergence with distributional Bellman backup.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Algorithm", "weight": 1.0} -->

In the policy evaluation case where we would like to compute optimistic estimates of the CVaR of a given observed policy $\pi$, our algorithm essentially performs an approximate version of the optimistic Bellman update $O_{c}\mathcal{T}^{\pi}$ where $\mathcal{T}^{\pi}$ is the distributional Bellman operator. For the control case where we would like to learn a policy that maximizes CVaR, we instead define a distributional Bellman optimality operator $\mathcal{T}_{\alpha}$. Analogous to prior work (?), $\mathcal{T}_{\alpha}$ is any operator that satisfies ${\mathcal{T}_{\alpha}Z} = {\mathcal{T}^{\pi}Z}$ for some policy $\pi$ that is greedy w.r.t. CVaR at level $\alpha$. Our algorithm then performs an approximate version of the optimistic Bellman backup $O_{c}\mathcal{T}_{\alpha}$, shown in Algorithm 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The main structure of our algorithm resembles categorical distributional reinforcement learning (C51) (?). In a similar vein, our algorithm also maintains a return distribution estimate for each state-action pair, represented as a set of $N$ weights $p_{i}{(s,a)}$ for $i \in {\lbrack N\rbrack}$. These weights represent a discrete distribution with outcomes at $N$ equally spaced locations $z_{0} < z_{1} < \cdots < z_{N - 1}$, each ${\Deltaz} = \frac{V_{\max} - V_{\min}}{N - 1}$ apart. The current probability assigned to outcome $z_{i}$ in $(s,a)$ is denoted by $p_{i}{(s,a)}$, where the atom probabilities $p_{1:N}{(s,a)}$ are given by a differentiable model such as a neural network, similar to C51. Note that other parameterized representations of the weights (?) are straightforward to incorporate.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The main differences between Algorithm 1 and existing distributional RL algorithms (e.g. C51) are highlighted in red. We first apply an optimism operator to our successor distribution $F_{Z{(s_{t + 1},a)}}$ (Lines 1--1) to form an optimistic CDF ${\overset{\sim}{F}}_{Z{(s_{t + 1},a)}}$ for all actions $a \in \mathcal{A}$. This operator should encourage exploring actions that might lead to higher CVaR policies for our input $\alpha$. These optimistic CDFs are also used to decide on the successor action in the control setting (Line 1).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm", "weight": 1.0} -->

In tabular settings, the counts n(s,a) can be directly stored and used; however, this is not the case in continuous settings. For this reason, we adopt the pseudo-count estimation method proposed by (?) and replace $n{(s,a)}$ by a pseudo-count ${\hat{N}}_{t}{(s,a)}$ in the optimistic distributional operator (Equation 4). Let $\rho$ be a density model and $\rho_{t}{(s,a)}$ the probability assigned to the state action pair $(s,a)$ by the model after $t$ training steps. The prediction gain $PG$ of $\rho$ is defined Where $\rho_{t}'{(s,a)}$ is the probability assigned to $(s,a)$ if it were trained on that same $(s,a)$ one more time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Now we define the pseudo count of $(s,a)$ as where $\kappa$ is a constant hyper-parameter, and ${({PG{(s,a)}})}_{+}$ thresholds the value of the prediction gain at 0.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Our setting differs from (?) in the sense that we have to compute the count before taking the action $a$. A naive way would be to try all actions and train the model to compute the counts but this method is slow and requires the environment to support an undo action. Instead, we can estimate $PG$ for all actions as follows. Consider the density model parametrized by $\theta$, $\rho{(s,a;\theta)}$. After observing $(s,a)$, the training step to maximize the log likelihood will update the parameters by $\theta' = {\theta + {\alpha{{\nabla_{\theta}\log}\rho}{(s,a;\theta)}}}$, where $\alpha$ is the learning rate.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Algorithm", "weight": 1.0} -->

So we can approximate the new log probability using a first-order Taylor expansion This calculation suggests that the prediction gain can be estimated just by computing the gradient of the log likelihood given a state-action pair, i.e., ${PG{(s,a)}} \approx {\alpha{({{{\nabla_{\theta}\log}\rho}{(s,a;\theta)}})}^{2}}$. As discussed in (?) this estimate of prediction gain is biased, but empirically we have found this method to perform well.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We validate our algorithm empirically in three simulated environments against baseline approaches. Finance, health and operations are common areas where risk-sensitive strategies are important, and we focus on two health domains and one operations domain. Details, where omitted, are provided in the supplemental material.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Machine Replacement", "weight": 1.0} -->

Machine repair and replacement is a classic example in the risk sensitive literature, though to our knowledge no prior work has considered how to quickly learn a good risk-sensitive policy for such domains. Here we consider a minor variant of a prior setting (?). Specifically, as shown in Figure 2, the environment consists of a chain of $n$ (25 in our experiments) states. There are two actions: *replace* and *don't replace* the machine. Choosing *replace* at any state terminates the episode, while choosing *don't replace* moves the agent to the next state in the chain. At the end of the chain, choosing *don't replace* terminates the episode with a high variance cost, and choosing *replace* terminates the episode with a higher cost but lower variance. This environment is especially a challenging exploration task due to the chain structure of the MDP, as well as the high variance of the reward distributions when taking actions in the last state. Additionally in this MDP it is feasible to exactly compute the ${CVaR}_{0.25}$-optimal policy, which allows us to compare the learned policy to the true optimal CVaR policy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Machine Replacement", "weight": 1.0} -->

Note here that the optimal policy for maximizing ${CVaR}_{0.25}$ is to *replace* on the final state in the chain to avoid the high variance alternative; in contrast, the optimal policy for expected return always chooses *don't replace*.

<!-- chunk {"id": "body-0027", "role": "body", "section": "HIV Treatment", "weight": 1.0} -->

In order to test our algorithm on a larger continuous state space, we leverage an HIV Treatment simulator. The environment is based on the implementation by (?) of the physical model described in (?). The patient state is represented as a $6$-dimensional continuous vector and the reward is a function of number of free HIV viruses, immune response of the body to HIV, and side effects. There are four actions, each determining which drugs are administered for the next $20$ day period: Reverse Transcriptase Inhibitors (RTI), Protease Inhibitors (PI), neither, or both. There are $50$ time steps in total per episode, for a total of $1000$ days. We chose here a larger number of days per time step compared to the typical setup ($200$ steps of $5$ days each) to facilitate faster experimentation. This design choice also makes the exploration task harder, since taking one wrong action can drastically destabilize a patient's trajectory. The original proposed model was deterministic, which makes the CVaR policy identical to the policy optimizing the expected value.

<!-- chunk {"id": "body-0028", "role": "body", "section": "HIV Treatment", "weight": 1.0} -->

Such simulators are rarely a perfect proxy for real systems, and in our setting we add Gaussian noise $\sim {\mathcal{N}{(0,0.01)}}$ to the efficacy of each drug (RTI: $\epsilon_{1}$ and PI: $\epsilon_{2}$ in (?)). This change necessitates risk-sensitive policies in this environment.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Diabetes 1 Treatment", "weight": 1.0} -->

Patients with type 1 diabetes regulate their blood glucose level with insulin in order to avoid hypoglycemia or hyperglycemia (very low or very high blood glucose level, respectively). A simulator has been created (?) that is an open source version of a simulator that was approved by the FDA as a substitute for certain pre-clinical trials. The state is continuous-valued vector of the current blood glucose level and the amount of carbohydrate intake (through food). The action space is discretized into 6 levels of a bolus insulin injection. The reward function is defined similar to the prior work (?) as following: Where ${bg'} = {{bg}/18.018018}$ which is the estimate of bg (blood glucose) in mmol/L.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Diabetes 1 Treatment", "weight": 1.0} -->

Additionally we inject two source of stochasticity into the taken action: First, we add Gaussian noise $\mathcal{N}{}$ to the action. Second, we delay the time of the injection by at most 5 steps, where the probability of injection at time $t$ is higher than time ${{t + i},i} \geq 1$ following the power law. Each simulation lasts for 200 steps, during which a patient eats five meals. The agent chooses an action after each meal, and after the 200 steps each patient resets to its initial state.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Diabetes 1 Treatment", "weight": 1.0} -->

This domain also readily offers a suite of related tasks, since the environment simulates 30 patients with slightly different dynamics. Tuning hyper-parameters on the same task can be misleading (?), as is the case in our two previous benchmarks. In this setting we tune baselines and our method on one patient, and test the performance on different patients.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

The majority of prior risk-sensitive RL work has not focused on efficient exploration, and there has been very little deep distributional RL work focused on risk sensitivity. Our key contribution is to evaluate the impact of more strategic exploration on the efficiency with which a risk-sensitive policy can be learned. We compare to following approaches: $\epsilon$-greedy CVaR: In this benchmark we use the same algorithm, except we do not introduce an optimism operator, instead using an $\epsilon$-greedy approach for exploration. This benchmark can be viewed as analogous to the distributional RL methods of C51 (?) if the computed policy had optimized for CVaR instead of expected reward.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

IQN-$\epsilon$-greedy CVaR: In this benchmark we use implicit quantile network (IQN) that also uses $\epsilon$-greedy method for exploration (?). We adopted the dopamine implementation of IQN (?).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

CVaR-AC: An actor-critic method proposed by (?) that maximizes the expected return while satisfying an inequality constraint on the $CVaR$. This method relies on the stochasticity of the policy for exploration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

Note that a comparison to an expectation maximizing algorithm is uninformative since such approaches are maximizing different (non-risk-sensitive) objectives.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

All of these algorithms use hyperparameters, and it is well recognized that $\epsilon$-greedy algorithms can often perform quite well if their hyperparameters are well-tuned. To provide a fair comparison, we evaluated across a number of schedules for reducing the $\epsilon$ parameter for both $\epsilon$-greedy and IQN, and a small set of parameters (4-7) for the optimism value $c$ for our method. We used the specification described in Appendix C of (?) for CVaR-AC.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

The system architectures used in continuous settings are identical for Baseline 1 ($\epsilon$-greedy) and our method. This consists of 2 hidden layers of size 32 with ReLU activation for Diabetes 1 Treatment, and 4 hidden layers of size 128 with ReLU activation for HIV Treatment, both followed by a softmax layer for each action. Similarly for IQN we used the same architecture, followed by a cosine embedding function and a fully connected layer of size 128 for HIV Treatment (32 for Diabetes 1 Treatment) with ReLU activation, followed by a softmax layer. The density model is a realNVP (?) with 3 hidden layers each of size 64.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

All results are averaged over 10 runs and we report 95% confidence intervals. We report the performance of $\epsilon$-greedy at evaluation time (setting $\epsilon$ = 0), which is the best performance of $\epsilon$-greedy.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Baselines and Experimental Setup", "weight": 1.0} -->

For the Diabetes Treatment domain, hyperparameters are optimized only on adult#001. We then report results of the methods using those hyperparameters on adult#003, adult#004 and adult#005.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Results on machine replacement environment (Figure 3), HIV Treatment (Figure 4) and Diabetes 1 Treatment (Figure 5) all show our optimistic algorithm achieves better performance much faster than the baselines.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

In Machine Replacement (Figure 3) we see that our method quickly converges to the optimal CVaR performance. Unfortunately despite our best efforts, our implementation of CVaR-AC did not perform well even on the simplest environment, so we did not show the performance of this method on other environments. One challenge here is that CVaR-AC has a significant number of hyper-parameters, including 3 different learning rates schedule for the optimization process, initial Lagrange multipliers and the kernel functions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

In the HIV Treatment we also see a clear and substantial benefit to our optimistic approach over the baseline $\epsilon$-greedy approach and IQN(Figure 4).

<!-- chunk {"id": "body-0043", "role": "body", "section": "\"Safer\" Exploration", "weight": 1.0} -->

Our primary contribution is a new algorithm to learn risk-sensitive policies quickly, with less data. However, an interesting side benefit of such a method might be that the number of extremely poor outcomes experienced over time may also be reduced, not due to explicitly prioritizing a form of safe exploration, but because our algorithm may enable a faster convergence to a safe policy. To evaluate this, we consider a risk measure proposed by (?), which quantifies the risk of a severe medical condition based on how close their glucose level is to hypoglycemia (blood glucose, $\leq$`<!-- -->`{=html}3.9 mmol/l) and hyperglycemia (blood glucose, $\geq$`<!-- -->`{=html}10 mmol/l).

<!-- chunk {"id": "body-0044", "role": "body", "section": "\"Safer\" Exploration", "weight": 1.0} -->

Table 6 shows the fraction of episodes in which each patient experienced a severely poor outcome for each algorithm while learning. Optimism-based exploration approximately halves the number of episodes with severely poor outcomes, highlighting a side benefit of our optimistic approach of more quickly learning a good safe policy.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present a new algorithm for quickly learning CVaR-optimal policies in Markov decision processes. This algorithm is the first to leverage optimism in combination with distributional reinforcement learning to learn risk-averse policies in a sample-efficient manner. Unlike existing work on expected return criteria which rely on reward bonuses for optimism, We introduce optimism by directly modifying the target return distribution and provide a theoretical justification that in the evaluation case for finite MDPs, this indeed yields optimistic estimates. We further empirically observe significantly faster learning of CVaR-optimal policies by our algorithm compared to existing baselines on several benchmark tasks. This includes simulated healthcare tasks where risk-averse policies are of particular interest: HIV medication treatment and insulin pump control for diabetes type 1 patients.
