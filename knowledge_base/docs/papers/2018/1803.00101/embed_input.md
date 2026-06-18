<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning

Topics include Reinforcement learning, Uncertainty, Sample complexity, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent model-free reinforcement learning algorithms have proposed incorporating learned dynamics models as a source of additional data with the intention of reducing sample complexity. Such methods hold the promise of incorporating imagined data coupled with a notion of model uncertainty to accelerate the learning of continuous control tasks. Unfortunately, they rely on heuristics that limit usage of the dynamics model. We present model-based value expansion, which controls for uncertainty in the model by only allowing imagination to fixed depth. By enabling wider use of learned dynamics models within a model-free reinforcement learning algorithm, we improve value estimation, which, in turn, reduces the sample complexity of learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress in model-free (MF) reinforcement learning has demonstrated the capacity of rich value function approximators to master complex tasks. However, these model-free approaches require access to an impractically large number of training interactions for most real-world problems. In contrast, model-based (MB) methods can quickly arrive at near-optimal control with learned models under fairly restricted dynamics classes. In settings with nonlinear dynamics, fundamental issues arise with the MB approach: *complex dynamics demand high-capacity models, which in turn are prone to overfitting in precisely those low-data regimes where they are most needed.* Model inaccuracy is further exacerbated by the difficulty of long-term dynamics predictions (Fig. 1).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The MF and MB approaches have distinct strengths and weaknesses: expressive value estimation MF methods can achieve good asymptotic performance but have poor sample complexity, while MB methods exhibit efficient learning but struggle on complex tasks. In this paper, we seek to *reduce sample complexity while supporting complex non-linear dynamics by combining MB and MF learning techniques through disciplined model use for value estimation*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present model-based value expansion (MVE), a hybrid algorithm that uses a dynamics model to simulate the short-term horizon and Q-learning to estimate the long-term value beyond the simulation horizon. This improves Q-learning by providing higher-quality target values for training. Splitting value estimates into a near-future MB component and a distant-future MF component offers a model-based value estimate that creates a decoupled interface between value estimation and model use and does not require differentiable dynamics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this scheme, our trust in the model informs the selection of the horizon up to which we believe the model can make accurate estimates. This horizon is an interpretable metric applicable to many dynamics model classes. Prior approaches that combine model-based and model-free RL, such as model-based acceleration, incorporate data from the model directly into the model-free RL algorithm, which we show can lead to poor results. Alternatively, imagination-augmented agents (I2A) offloads all uncertainty estimation and model use into an implicit neural network training process, inheriting the inefficiency of model-free methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By incorporating the model into Q-value target estimation, we only require the model to be able to make forward predictions. In contrast to stochastic value gradients (SVG), we make no differentiability assumptions on the underlying dynamics, which usually include non-differentiable phenomena such as contact interactions. Using an approximate, few-step simulation of a reward-dense environment, the improved value estimate provides enough signal for faster learning for an actor-critic method (Fig. 6). Our experimental results show that our method can outperform both fully model-free RL algorithms and prior approaches to combining real-world and model-based rollouts for accelerated learning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A general method to reduce the value estimation error in algorithms with model-free critics (Sec. 3).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

An evaluation of the reduced sample complexity resulting from better value estimation (Sec. 4.1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A characterization of the error that arises from value-based methods applied to imaginary data (Sec. 4.2).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Deterministic Policy Gradients (DPG)", "weight": 1.0} -->

Silver et al. describe an off-policy actor-critic MF algorithm. For a deterministic, parameterized policy $\pi_{\theta}$ and parameterized critic $\hat{Q}$ (we leave its parameters implicit), Silver et al. prove that a tractable form of the policy gradient ${\nabla_{\theta}J_{d_{0}}}{(\theta)}$ exists when $f$ is continuously differentiable with respect to actions taken by the policy. This result, the deterministic policy gradient theorem, expresses the policy gradient as an expectation over on-policy data.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deterministic Policy Gradients (DPG)", "weight": 1.0} -->

To encourage exploration, the data collected may be off-policy. To reconcile the use of off-policy data with an on-policy estimator, Silver et al. briefly note an analogous off-policy policy improvement theorem in the case of finite state spaces.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Continuous DPG", "weight": 1.0} -->

In the continuous case, the conditions under which the off-policy policy improvement theorem holds are distinct from the discrete case. We emphasize these conditions here and provide a proof for the statement in Silver et al. inspired by the discrete case.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model-Based Value Expansion", "weight": 1.0} -->

MVE improves value estimates for a policy $\pi$ by assuming we an approximate dynamical model $\hat{f}:{{\mathcal{S} \times \mathcal{A}}\rightarrow\mathcal{S}}$ and the true reward function $r$. Such an improved value estimate can be used in training a critic for faster task mastery in reward-dense environments (Fig. 6). We assume that the model is accurate to depth $H$; that is, for a fixed policy $\pi$, we may use $\hat{f}$ to evaluate ("imagine") future transitions that occur when taking actions according to $\pi$ with ${\hat{f}}^{\pi} = {\hat{f}{( \cdot,{\pi{( \cdot )}})}}$. We use these future transitions to estimate value.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

of the original critic $\hat{V}$ with respect to $\nu$, a distribution of states. We emphasize that, even assuming an ideal model, the mere combination of MB and MF does not guarantee improved estimates. Further, while our analysis will be conducted on state-value estimation, it may be naturally extended to state-action-value estimation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

This translates to an expression for MVE MSE,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

where ${(f^{\pi})}^{H}\nu$ denotes the pushforward measure resulting from playing $\pi$ $H$ times starting from states in $\nu$. This informal presentation demonstrates the relation of MVE MSE to the underlying critic MSE by assuming the model is nearly ideal. We verify that the informal reasoning above is sound in the presence of model error.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

In the preceding section, we presented an analysis that motivates our model-based value expansion approach. In this section, we will present a practical implementation of this approach for high-dimensional continuous deep reinforcement learning. We demonstrate how to apply MVE in a general actor-critic setting to improve the target $Q$-values, with the intention of achieving faster convergence. Our implementation relies on a parameterized actor $\pi_{\theta}$ and critic $Q_{\varphi}$, but note that the separate parameterized actor may be removed if it is feasible to compute ${\pi{(s)}} = {{\operatorname{argmax}_{a}Q_{\varphi}}{(s,a)}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

We assume that the actor critic method supplies a differentiable actor loss $\ell_{actor}$ and a critic loss $\ell_{critic}^{\pi,Q}$. These losses are functions of $\theta,\varphi$ as well as transitions $\tau = {(S,A,R,S^{\prime})}$ sampled from some distribution $\mathcal{D}$. For instance, in DDPG, the $\theta$ gradient of ${\mathbb{E}}_{\mathcal{D}}\left\lbrack \ell_{actor}{(\theta,\varphi,\tau)} \right\rbrack = {\mathbb{E}}_{\mathcal{D}}\left\lbrack Q_{\varphi}\left. (S,\pi_{\theta}{(S)} \right\rbrack \right.$ approximately ascends $J_{\mathcal{D}}$ per the deterministic continuous policy improvement theorem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

MVE relies on our approximate fixed point construction from an empirical distribution of transitions $\beta$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

Thus, sampling transitions from $\nu$ is equivalent to sampling from any point up to $H$ imagined steps into the future, when starting from a state sampled from $\beta$. The MVE-augmented method follows the usual actor-critic template, but critic training uses MVE targets and transitions sampled from $\nu$ (Alg. 1).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

We imagine rollouts with the target actor, whose parameters are exponentially weighted averages of previous iterates, for parity with DDPG, which uses a target actor to compute target value estimates. Taking $H = 0$, ${\nu{(\theta^{\prime},\hat{f})}} = \beta$, we recover the original actor-critic algorithm. Our implementation uses multi-layer fully-connected neural networks to represent both the $Q$-function and the policy. We use the actor and critic losses described by DDPG.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

1:procedure MVE-AC(initial θ, φ)
3: Initialize the replay buffer β ← ⌀
4: while not tired do
5: Collect transitions from any exploratory policy
6: Add observed transitions to β
7: Fit the dynamics

<!-- chunk {"id": "body-0024", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

8: for a fixed number of iterations do
10: update θ with ∇θℓactor (πθ,Qφ,τ0)
11: imagine future transitions for t ∈ [H − 1]

<!-- chunk {"id": "body-0025", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

12: ∀k define Q̂k as the k-step MVE of Qφ′
13: update φ with ∇φ ∑tℓcriticπθ′, Q̂H − t (φ,τt)/H
14: update targets θ′, φ′ with some decay
Algorithm 1 Use model-based value expansion to enhance critic target values in a generic actor-critic method abstracted by ℓactor, ℓcritic. Parameterize π, Q with θ, φ, respectively. We assume f̂ is selected from some class of dynamics models and the space 𝒮 is equipped with a norm.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

Importantly, we do not use an imagination buffer to save simulated states, and instead generate simulated states on-the-fly by sampling from $\nu{(\theta^{\prime},\hat{f})}$. We perform a stratified sampling from $\nu{(\theta^{\prime},\hat{f})}$, with $H$ dependent samples at a time, for each $t \in {\{ 0,\cdots,{H - 1}\}}$ in Line 11. First, we sample a real transition $\tau_{0} = {(s_{- 1},a_{- 1},r_{- 1},s_{0})}$ from $\beta$, the empirical distribution of transitions observed from interacting with the environment according to an exploratory policy. We use the learned dynamics model $\hat{f}$ to generate ${\hat{s}}_{t}$ and ${\hat{r}}_{t}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

Since $\pi_{\theta^{\prime}}$ changes during the joint optimization of $\theta,\varphi$, these simulated states are discarded immediately after the batch. We then take a stochastic $\nabla_{\varphi}$ step to minimize $\nu$-based Bellman error of $Q_{\varphi}$,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

where $Q_{\varphi^{\prime}}$ and and ${\hat{a}}_{t} = {\pi_{\theta^{\prime}}{({\hat{s}}_{t})}}$ use target parameter values (Lines 11-13 of Alg. 1). As such, every observation of the Bellman error always relies on some real data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

For the dynamics $\hat{f}$, we use a neural network network with 8 layers of 128 neurons each with a fixed $10^{- 3}$ learning rate trained to predict the difference in real-vector-valued states, similar to previous work. While we expect more accurate and carefully tuned models to allow us to use large $H$, even a weak model with shared hyperparameters across all tasks from a flexible class suffices to demonstrate our point.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate MVE on several continuous control environments. Experimental details are in Sec. A.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

Do the improved estimates result in faster mastery?

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

Does the TD-$k$ trick resolve distribution mismatch?

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

In all of our experiments, we tune the baseline, DDPG, and report its best performance. For exploration, we use parameter-space noise. Every experiment and each setting uses the same adaptive parameter-space noise standard deviation target, so exploration is controlled to be the same in all trials. We then add the MVE extension (we do not tune DDPG parameters to MVE performance). To evaluate the effect of the TD-$k$, we evaluate against the naive approach of using $H$-step MVE $\hat{Q}$ estimates for Bellman error on states sampled from $\beta$. This is equivalent to using only the first term for $t = 0$ in the sum of Line 13 of Alg. 1, i.e., updating critic parameters $\varphi$ with the gradient ${\nabla_{\varphi}\ell_{critic}^{\pi_{\theta^{\prime}},{\hat{Q}}_{H}}}{(\varphi,\tau_{0})}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

Without the TD-$k$ trick the model is still used to simulate to depth $H$, but the opportunity to learn on a distribution of additional support is neglected.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

We plot the mean learning curve, along with the standard deviation. We smooth each graph with a 20 point window (evaluation data is collected at intervals of at most $10^{3}$ timesteps).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Performance", "weight": 1.0} -->

First, we evaluate that MVE-DDPG (with the TD-$k$ trick) improves in terms of raw reward performance by comparing its learning curves to those of the original DDPG, MVE-DDPG without the TD-$k$ trick, and imagination buffer (IB) approaches. We find that MVE-DDPG outperforms the alternatives (Fig. 3).^11^1We run IB with an imaginary-to-real ratio of 4, as used for 2 of 3 environments. We tested lower ratios on cheetah but found they performed worse. Note that for parity with DDPG we ran MVE-DDPG with only 4 gradient steps. Our result shows that incorporating synthetic samples from a learned model can drastically improve the performance of model-free RL, greatly reducing the number of samples required to attain good performance. As illustrated by the comparison to the IB baseline, this improvement is obtained only when carefully incorporating this synthetic experience via a short horizon and the TD-$k$ trick. As we will discuss in the next section, the specific design decisions here are critical for good results, which helps to explain the lack of success with learned neural network models observed with related methods in prior work.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Performance", "weight": 1.0} -->

MVE-DDPG improves on similar approaches, such as MA-DDPG, by its treatment of synthetic data obtained from the dynamics model. This alternative approach adds simulated data back into a separate imagination buffer, effectively modifying $\beta$ from Alg. 1 into a mixture between $\beta$ and simulated data (where the mixture is dependent on the relative number of samples taken from each buffer). This is problematic because the policy changes during training, so the data from this mixed distribution of real and fake data is stale relative to $\nu$ in terms of representing actions that would be taken by $\pi$. In our implementation of MA-DDPG, we do not reuse imagined states in this manner, but MVE-DDPG still outperforms MA-DDPG. We suspect this is due to two factors: the staleness of the imaginary states in the IB approach, and the delicate interaction between using more imaginary data and overtraining the actor. In order to use the additional synthetic data, an IB approach must take more gradient steps with imaginary batches.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Performance", "weight": 1.0} -->

On the other hand, since MVE-DDPG uses a gradient averaged over both real and simulated data, the choice to make additional gradient steps becomes an independent consideration dependent on the stability of the actor-critic method being trained.

<!-- chunk {"id": "body-0039", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

We make sure that MVE can make use of accurate models to improve the critic value estimate (Fig. 4). The improved critic performance results in faster training compared to the $H = 0$ DDPG baseline on cheetah. Also, we replicate the density plot from DDPG to analyze $Q$ accuracy directly, from which it is clear that MVE improves the critic by providing better target values (Fig. 5).

<!-- chunk {"id": "body-0040", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

In addition, we verify that the TD-$k$ trick is essential to training $\hat{Q}$ appropriately. To do so, we conduct an ablation analysis on the cheetah environment: we hold all parameters constant and substitute the learned dynamics model $\hat{f}$ with the true dynamics model $f$, making model error zero. If ${\operatorname{MSE}_{\beta}{(\hat{Q})}} \approx {\operatorname{MSE}_{{(f^{\pi})}^{H}\beta}{(\hat{Q})}}$, the MVE estimates must improve exponentially in $H$, even without the TD-$k$ trick. However, this is not the case. With the TD-$k$ trick, increasing $H$ yields increasing but diminishing returns (Fig. 6). Without the adjustment for distribution mismatch, past a certain point, increasing $H$ hurts performance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

Because the dynamics model is ideal in these cases, the only difference is that the critic $\hat{Q}$ is trained on the distribution of states $\nu = {\frac{1}{H}{\sum_{t = 0}^{H - 1}{{(f^{\pi})}^{t}\beta}}}$ instead of $\beta$, where $\beta$ is the empirical distribution resulting from the replay buffer. Since the TD-$k$ trick increases the support of the training data on which $\hat{Q}$ is trained, the function class for the critic may need to have sufficient capacity to capture the new distribution, but we did not find this to be an issue in our experiments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduce the model-based value expansion (MVE) method, an algorithm for incorporating predictive models of system dynamics into model-free value function estimation. Our approach provides for improved sample complexity on a range of continuous action benchmark tasks, and our analysis illuminates some of the design decisions that are involved in choosing how to combine model-based predictions with model-free value function learning.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Existing approaches following a general Dyna-like approach to using imagination rollouts for improvement of model-free value estimates either use stale data in an imagination buffer or use the model to imagine past horizons where the prediction is accurate. Multiple heuristics have been proposed to reduce model usage to combat such problems, but these techniques generally involve a complex combination of uncertainty estimation and additional hyperparameters and may not always appropriately restrict model usage to reasonable horizon lengths. MVE offers a single, simple, and adjustable notion of model trust ($H$), and fully utilizes the model to that extent. MVE also demonstrates that state dynamics prediction enables on-policy imagination via the TD-$k$ trick starting from off-policy data.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work justifies further exploration in model use for model-free sample complexity reduction. In particular, estimating uncertainty in the dynamics model explicitly would enable automatic selection of $H$. To deal with sparse reward signals, we also believe it is important to consider exploration with the model, not just refinement of value estimates. Finally, MVE admits extensions into domains with probabilistic dynamics models and stochastic policies via Monte Carlo integration over imagined rollouts.
