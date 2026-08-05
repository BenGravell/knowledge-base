<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning

Topics include Reinforcement learning, Uncertainty, Sample complexity, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent model-free reinforcement learning algorithms have proposed incorporating learned dynamics models as a source of additional data with the intention of reducing sample complexity. Such methods hold the promise of incorporating imagined data coupled with a notion of model uncertainty to accelerate the learning of continuous control tasks. Unfortunately, they rely on heuristics that limit usage of the dynamics model. We present model-based value expansion, which controls for uncertainty in the model by only allowing imagination to fixed depth. By enabling wider use of learned dynamics models within a model-free reinforcement learning algorithm, we improve value estimation, which, in turn, reduces the sample complexity of learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress in model-free (MF) reinforcement learning has demonstrated the capacity of rich value function approximators to master complex tasks. However, these model-free approaches require access to an impractically large number of training interactions for most real-world problems. In contrast, model-based (MB) methods can quickly arrive at near-optimal control with learned models under fairly restricted dynamics classes [lqr]. In settings with nonlinear dynamics, fundamental issues arise with the MB approach: complex dynamics demand high-capacity models, which in turn are prone to overfitting in precisely those low-data regimes where they are most needed. Model inaccuracy is further exacerbated by the difficulty of long-term dynamics predictions (Fig.[fig:dynmse]).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The MF and MB approaches have distinct strengths and weaknesses: expressive value estimation MF methods can achieve good asymptotic performance but have poor sample complexity, while MB methods exhibit efficient learning but struggle on complex tasks. In this paper, we seek to reduce sample complexity while supporting complex non-linear dynamics by combining MB and MF learning techniques through disciplined model use for value estimation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The mean $L_2$ error, with standard deviation, for open-loop dynamics prediction of a cheetah agent increases in the prediction horizon.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present model-based value expansion (MVE), a hybrid algorithm that uses a dynamics model to simulate the short-term horizon and Q-learning to estimate the long-term value beyond the simulation horizon.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This improves Q-learning by providing higher-quality target values for training. Splitting value estimates into a near-future MB component and a distant-future MF component offers a model-based value estimate that creates a decoupled interface between value estimation and model use and does not require differentiable dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this scheme, our trust in the model informs the selection of the horizon up to which we believe the model can make accurate estimates.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This horizon is an interpretable metric applicable to many dynamics model classes. Prior approaches that combine model-based and model-free RL, such as model-based acceleration [naf], incorporate data from the model directly into the model-free RL algorithm, which we show can lead to poor results. Alternatively, imagination-augmented agents (I2A) offloads all uncertainty estimation and model use into an implicit neural network training process, inheriting the inefficiency of model-free methods [i2a].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

By incorporating the model into Q-value target estimation, we only require the model to be able to make forward predictions. In contrast to stochastic value gradients (SVG), we make no differentiability assumptions on the underlying dynamics, which usually include non-differentiable phenomena such as contact interactions [svg]. Using an approximate, few-step simulation of a reward-dense environment, the improved value estimate provides enough signal for faster learning for an actor-critic method (Fig.[fig:hc-true]). Our experimental results show that our method can outperform both fully model-free RL algorithms and prior approaches to combining real-world and model-based rollouts for accelerated learning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

- A general method to reduce the value estimation error in algorithms with model-free critics (Sec.[sec:mve]). - An evaluation of the reduced sample complexity resulting from better value estimation (Sec.[sec:mve-perf]). - A characterization of the error that arises from value-based methods applied to imaginary data (Sec.[sec:critic-improve]).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deterministic Policy Gradients (DPG)", "weight": 1.0} -->

[dpg] describe an off-policy actor-critic MF algorithm. For a deterministic, parameterized policy $\pi_\theta$ and parameterized critic $\hat Q$ (we leave its parameters implicit), [dpg] prove that a tractable form of the policy gradient $\nabla_\theta J_{d_0}(\theta)$ exists when $f$is continuously differentiable with respect to actions taken by the policy. This result, the deterministic policy gradient theorem, expresses the policy gradient as an expectation over on-policy data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Deterministic Policy Gradients (DPG)", "weight": 1.0} -->

To encourage exploration, the data collected may be off-policy. To reconcile the use of off-policy data with an on-policy estimator, [dpg] briefly note an analogous off-policy policy improvement theorem in the case of finite state spaces [degris].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Continuous DPG", "weight": 1.0} -->

In the continuous case, the conditions under which the off-policy policy improvement theorem holds are distinct from the discrete case. We emphasize these conditions here and provide a proof for the statement in [dpg] inspired by the discrete case [degris].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Continuous DPG", "weight": 1.0} -->

Let $\beta$ be an off-policy distribution of states and set $$g_\theta(s)=D_{\pi(s)}(\theta)^\top\nabla_a Q^{\pi_\theta}(s, a)\big|_{a=\pi(s)},$$ with $D_{\pi(s)}(\theta)$ the Jacobian of $\theta\mapsto \pi_{\theta}(s)$. Then $\mathExp_\beta g_\theta(S)$ ascends $J_\beta(\theta)$ if the following conditions hold $\beta$-almost always: $Q^{\pi_\theta}$ must be differentiable with respect to the action at $(s, \pi_\theta(s))$, the Jacobian $D_{\pi(s)}(\theta)$ must exist, and $g_\theta(s)$ is nonzero.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Continuous DPG", "weight": 1.0} -->

Proof. See the appendix (Sec.[sec:dpg-continuous]).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Continuous DPG", "weight": 1.0} -->

Critically, we do not require DPG's assumptions of continuous differentiability in the reward or dynamics functions. This will allow model-based value expansion to be both theoretically and practically compatible with arbitrary forward models, including discrete event simulators, and settings with non-differentiable physics. $\hat Q$ may be used as a replacement for the true $Q^\pi$ term to approximate the ascent direction $g_\theta$ in Eq.(eq:ascentdir), as described in deep deterministic policy gradients (DDPG) [ddpg].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model-Based Value Expansion", "weight": 1.0} -->

MVE improves value estimates for a policy $\pi$ by assuming we an approximate dynamical model $\hat f:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}$ and the true reward function $r$. Such an improved value estimate can be used in training a critic for faster task mastery in reward-dense environments (Fig.fig:hc-true). We assume that the model is accurate to depth $H$; that is, for a fixed policy $\pi$, we may use $\hat f$ to evaluate (imagine") future transitions that occur when taking actions according to $\pi$ with $\hat f^\pi=\hat f(\cdot, \pi(\cdot))$. We use these future transitions to estimate value.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model-Based Value Expansion", "weight": 1.0} -->

[$H$-Step Model Value Expansion] Using the imagined rewards reward $\hat r_t=r(\hat s_t,\pi(\hat s_t))$ obtained from our model $\hat s_t=\hat f^\pi(\hat s_{t-1})$ under $\pi$ we define the $H$-step model value expansion (MVE) estimate for the value of a given state $V^\pi(s_0)$: $$\hat V_H(s_0)=\sum_{t=0}^{H-1}\gamma^t\hat r_t + \gamma^H\hat V(\hat s_H)\,.$$ $H$-step model value expansion in Definitiondef:mve decomposes the state-value estimate at $s_0$ into the component predicted by learned dynamics $\sum_{t=0}^{H-1}\gamma^t\hat r_t$ and the tail, estimated by $\hat V$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model-Based Value Expansion", "weight": 1.0} -->

This approach can be extended to stochastic policies and dynamics by integrating Eq.[eq:mve] with a Monte Carlo method, assuming a generative model for the stochastic dynamics and policy. Since $\hat r_t$ is derived from actions $\hat a_t=\pi(\hat s_t)$, this is an on-policy use of the model and, even in the stochastic case, MVE would not require importance weights, as opposed to the case of using traces generated by off-policy trajectories.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Model-Based Value Expansion", "weight": 1.0} -->

While MVE is most useful in settings where the $H$ step horizon is not sparse, even in sparse reward settings predicting the future state will improve critic accuracy. Finally, MVE may be applied to state-action estimates: in this case $\hat a_0\triangleq a_0$ while $\hat a_t=\pi(\hat s_t)$ for $t>0$ and $\hat V(\hat s_H)\triangleq \hat Q(\hat s_H,\hat a_H)$ and may be used for estimating $\hat Q_H(s_0,a_0)$ with a state-action critic $\hat Q$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

In this section, we discuss the conditions under which the MVE estimate improves the mean-squared error (MSE): $$\MSE_\nu(V)=\mathExpUnder_{S\sim\nu}\ha{\pa{V(S)-V^\pi(S)}^2},$$ of the original critic $\hat V$ with respect to $\nu$, a distribution of states. We emphasize that, even assuming an ideal model, the mere combination of MB and MF does not guarantee improved estimates. Further, while our analysis will be conducted on state-value estimation, it may be naturally extended to state-action-value estimation. $H$-depth model accuracy assumption: if we observe a state $s_0$ we may imagine $\hat s_t\approx s_t$, so $\hat a_t\approx a_t$ and $\hat r_t\approx r_t$ for $t\le H$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

If the modelling assumption holds for some fixed $s_0$, we have $$\hat V_H(s_0)-V^{\pi}(s_0)\approx \gamma^H\pa{\hat V(s_H)-V^{\pi}(s_H)}\,.$$ This translates to an expression for MVE MSE, $$\MSE_\nu(\hat V_H)\approx \gamma^{2H}\MSE_{(f^\pi)^H\nu} (\hat V)\ $$ where $(f^\pi)^H\nu$ denotes the pushforward measure resulting from playing $\pi$ $H$ times starting from states in $\nu$. This informal presentation demonstrates the relation of MVE MSE to the underlying critic MSE by assuming the model is nearly ideal. We verify that the informal reasoning above is sound in the presence of model error.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

Define $s_t,a_t,r_t$ to be the states, actions, and rewards resulting from following policy $\pi$ using the true dynamics $f$ starting at $s_0\sim\nu$ and analogously define $\hat s_t,\hat a_t,\hat r_t$ using the learned dynamics $\hat f$ in place of $f$. Let the reward function $r$ be $L_r$-Lipschitz and the value function $V^\pi$ be $L_V$-Lipschitz. Let $\epsilon$ be a be an upper bound $$\max_{t\in[H]}{\mathExp\left[\norm{\hat s_t- s_t}^2\right]}\le \epsilon^2,$$ on the model risk for an $H$-step rollout.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

Then $$\MSE_\nu(\hat V_H)\le c_1^2\epsilon^2+ (1+c_2\epsilon)\gamma^{2H}\MSE_{(\hat f^\pi)^H\nu} (\hat V)\ $$ where $c_1,c_2$ grow at most linearly in $L_r,L_V$ and are independent of $H$ for $\gamma <1$. We assume $\MSE_{(\hat f^\pi)^H\nu} (\hat V)\ge \epsilon^2$ for simplicity of presentation, but an analogous result holds when the critic outperforms the model.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

Proof. See the appendix (Sec.[sec:mve-error]).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

Sufficient conditions for improving on the original critic $\MSE_\nu (\hat V)$ are then small $\epsilon$, $\gamma < 1$, and the critic being at least as accurate on imagined states as on those sampled from $\nu$, $$\MSE_\nu (\hat V)\ge \MSE_{(\hat f^\pi)^H\nu} (\hat V).$$ However, if $\nu$ is an arbitrary sampling distribution, such as the one generated by an exploratory policy, the inequality of Eq.[eq:offdist] rarely holds. In particular, this naive choice results in poor performance overall (Fig.[fig:ablation]) and counteracts the benefit of model-based reward estimates, even assuming a perfect oracle dynamics model (Fig.[fig:hc-true]). Thus, if $\hat V$ is trained on Bellman error from $\nu$, then the distribution mismatch between $(f^\pi)^H\nu$ and $\nu$ eclipses the benefit of $\gamma^{2H}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

In effect, any model-based approach evaluating the critic $\hat V$ on imaginary states from $(f^\pi)^H \nu$ must be wary of only training its critic on the real distribution $\nu$. We believe this insight can be incorporated into a variety of works similar to MVE, such as value prediction networks [vpn].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

We propose a solution to the distribution-mismatch problem by observing that the issue disappears if $(f^\pi)^H\nu=\nu$, i.e., the training distribution $\nu$ is a fixed point of $f^\pi$. In practice, given an arbitrary off-policy distribution of state-action pairs $\beta$ we set $\nu=\mathExp\ha{(f^\pi)^T\beta}$ as an approximation to the fixed point, where $T\sim\Uniform\ca{0, \cdots, H-1}$. If we then sample a state $\hat s_T|T\sim \pa{f^\pi}^T\beta$, our model accuracy assumption dictates that we may accurately simulate states $\ca{\hat s_{T+i}}_{i=1}^{H-T}$ arising from playing $\pi$ starting at $\hat{s}_T$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

These simulated states can be used to construct $k$-step MVE targets $\hat V_{k}(\hat s_T)$ accurately while adhering to assumptions about the model by setting $k=H-T$. These targets can then be used to train $\hat V$ on the entire support of $\nu$, instead of just $\beta$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Value Estimation Error", "weight": 1.0} -->

Since we do not have access to the true MSE of $\hat V$, we minimize its Bellman error with respect to $\nu$, using this error as a proxy. In this context, using a target $\hat V_k(\hat s_T)$ is equivalent to training $\hat V$ with imagined TD-$k$ error. This TD-$k$ trick enables us to skirt the distribution mismatch problem to the extent that $\nu$ is an approximate fixed point. We find that the TD-$k$ trick greatly improves task performance relative to training the critic on $\beta$ alone (Fig.[fig:ablation]).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

In the preceding section, we presented an analysis that motivates our model-based value expansion approach. In this section, we will present a practical implementation of this approach for high-dimensional continuous deep reinforcement learning. We demonstrate how to apply MVE in a general actor-critic setting to improve the target $Q$-values, with the intention of achieving faster convergence. Our implementation relies on a parameterized actor $\pi_\theta$ and critic $Q_\varphi$, but note that the separate parameterized actor may be removed if it is feasible to compute $\pi(s)=\argmax_a Q_\varphi(s,a)$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

We assume that the actor critic method supplies a differentiable actor loss $\ell_{\mathrm{actor}}$ and a critic loss $\ell_{\mathrm{critic}}^{\pi,Q}$. These losses are functions of $\theta,\varphi$ as well as transitions $\tau=(S,A,R,S')$ sampled from some distribution $\mathcal{D}$. For instance, in DDPG, the $\theta$ gradient of $\mathExp_\mathcal{D}\ha{\ell_{\mathrm{actor}}(\theta,\varphi, \tau)}=\mathExp_\mathcal{D}\ha{Q_\varphi(S, \pi_\theta(S)}$ approximately ascends $J_{\mathcal{D}}$ per the deterministic continuous policy improvement theorem [ddpg].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

The DDPG critic loss depends on a target actor $\pi$ and critic $Q$: $\ell_{\mathrm{critic}}^{\pi,Q}(\varphi,\tau)=\pa{Q_\varphi(S,A)-\pa{R+\gamma Q(S', \pi(S'))}}^2$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

MVE relies on our approximate fixed point construction from an empirical distribution of transitions $\beta$. Recall our approximation from the previous section, which relies on the current policy to imagine up to $H$ steps ahead: $\nu(\theta',\hat f)=\frac{1}{H}\sum_{t=0}^{H-1}(\hat f^{\pi_{\theta'}})^t\beta$, where $\hat f^{\pi_{\theta'}}(\tau)=(S', A', r(S', A'), \hat f(S', A'))$ and $A'=\pi_{\theta'}(S')$. Thus, sampling transitions from $\nu$ is equivalent to sampling from any point up to $H$ imagined steps into the future, when starting from a state sampled from $\beta$. The MVE-augmented method follows the usual actor-critic template, but critic training uses MVE targets and transitions sampled from $\nu$ (Alg.[alg:mve]).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

We imagine rollouts with the target actor, whose parameters are exponentially weighted averages of previous iterates, for parity with DDPG, which uses a target actor to compute target value estimates. Taking $H=0$, $\nu(\theta', \hat f)=\beta$, we recover the original actor-critic algorithm. Our implementation uses multi-layer fully-connected neural networks to represent both the $Q$-function and the policy. We use the actor and critic losses described by DDPG [ddpg].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

Use model-based value expansion to enhance critic target values in a generic actor-critic method abstracted by $\ell_{\mathrm{actor}},\ell_{\mathrm{critic}}$. Parameterize $\pi,Q$ with $\theta,\varphi$, respectively. We assume $\hat f$ is selected from some class of dynamics models and the space $\mathcal{S}$ is equipped with a norm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

MVE-ACinitial $\theta,\varphi$ Initialize targets $\theta'=\theta,\varphi'=\varphi$ Initialize the replay buffer $\beta\gets \emptyset$ Collect transitions from any exploratory policy Add observed transitions to $\beta$ Fit the dynamics $$\hat f\gets\argmin_{f}\mathExpUnder_\beta\ha{\norm{f(S,A)-S'}^2}$$ a fixed number of iterations sample $\tau_0\sim\beta$ update $\theta$ with $\nabla_\theta \ell_{\mathrm{actor}}\pa{\pi_\theta,Q_\varphi,\tau_0}$ imagine future transitions for $t\in [H-1]$ $$\tau_{t}=\hat f^{\pi_{\theta'}}(\tau_{t-1})$$ $\forall k$ define $\hat Q_k$ as the $k$-step MVE of

<!-- chunk {"id": "body-0039", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

$Q_{\varphi'}$ update $\varphi$ with $\nabla_\varphi\sum_t\ell_{\mathrm{critic}}^{\pi_{\theta'},\hat Q_{H-t}}\pa{\varphi,\tau_t}/H$ update targets $\theta',\varphi'$ with some decay Importantly, we do not use an imagination buffer to save simulated states, and instead generate simulated states on-the-fly by sampling from $\nu(\theta',\hat f)$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

We perform a stratified sampling from $\nu(\theta',\hat f)$, with $H$ dependent samples at a time, for each $t\in \{0,\cdots,H-1\}$ in Line[line:sample]. First, we sample a real transition $\tau_0=(s_{-1},a_{-1},r_{-1},s_0)$ from $\beta$, the empirical distribution of transitions observed from interacting with the environment according to an exploratory policy. We use the learned dynamics model $\hat f$ to generate $\hat s_t$ and $\hat r_t$. Since $\pi_{\theta'}$ changes during the joint optimization of $\theta,\varphi$, these simulated states are discarded immediately after the batch.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

We then take a stochastic $\nabla_\varphi$ step to minimize $\nu$-based Bellman error of $Q_\varphi$, $$\frac{1}{H}\sum_{t=-1}^{H-1}\pa{ Q_\varphi (\hat s_t, \hat a_t)- \pa{\sum_{k=t}^{H-1}\gamma^{k-t}\hat r_k+\gamma^H Q_{\varphi'}\pa{\hat s_H,\hat a_H}}}^2\ $$ where $Q_{\varphi'}$ and and $\hat a_t=\pi_{\theta'}(\hat s_t)$ use target parameter values (Lines[line:sample]-[line:critic-update] of Alg.[alg:mve]). As such, every observation of the Bellman error always relies on some real data.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Deep Reinforcement Learning Implementation", "weight": 1.0} -->

For the dynamics $\hat f$, we use a neural network network with 8 layers of 128 neurons each with a fixed $10^{-3}$ learning rate trained to predict the difference in real-vector-valued states, similar to previous work [metrpo]. While we expect more accurate and carefully tuned models to allow us to use large $H$, even a weak model with shared hyperparameters across all tasks from a flexible class suffices to demonstrate our point.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate MVE on several continuous control environments. Experimental details are in Sec. [sec:exp-det].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results", "weight": 1.0} -->

- Does MVE improve estimates of $Q^\pi$? - Do the improved estimates result in faster mastery? - Does the TD-$k$ trick resolve distribution mismatch?

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results", "weight": 1.0} -->

In all of our experiments, we tune the baseline, DDPG, and report its best performance. For exploration, we use parameter-space noise [paramnoise]. Every experiment and each setting uses the same adaptive parameter-space noise standard deviation target, so exploration is controlled to be the same in all trials. We then add the MVE extension (we do not tune DDPG parameters to MVE performance). To evaluate the effect of the TD-$k$, we evaluate against the naive approach of using $H$-step MVE $\hat Q$ estimates for Bellman error on states sampled from $\beta$. This is equivalent to using only the first term for $t=0$ in the sum of Line[line:critic-update] of Alg.[alg:mve], i.e., updating critic parameters $\varphi$ with the gradient $\nabla_\varphi\ell_{\mathrm{critic}}^{\pi_{\theta'},\hat Q_H}(\varphi, \tau_0)$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

Without the TD-$k$ trick the model is still used to simulate to depth $H$, but the opportunity to learn on a distribution of additional support is neglected.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

We plot the mean learning curve, along with the standard deviation. We smooth each graph with a 20 point window (evaluation data is collected at intervals of at most We use fully-observable analogues of typical Gym environments. By default, the environments excerpt certain observed dimensions, such as the abscissa of (a), which are requisite for reward calculation. This is done as a supervised imposition of policy invariance to certain dimensions, which we remove for full observability. (a) shows Fully Observable Half Cheetah (cheetah); (b), Fully Observable Swimmer (swimmer); (c), Fully Observable Walker, 2-D (walker). Agents are rewarded for forward motion. We detail our changes in the Appendix (Sec.sec:exp-det).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Performance", "weight": 1.0} -->

First, we evaluate that MVE-DDPG (with the TD- $k$ trick) improves in terms of raw reward performance by comparing its learning curves to those of the original DDPG, MVE-DDPG without the TD-$k$ trick, and imagination buffer (IB) approaches [kalweit]. We find that MVE-DDPG outperforms the alternatives (Fig.[fig:ablation]).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Performance", "weight": 1.0} -->

We run IB with an imaginary-to-real ratio of 4, as used for 2 of 3 environments. We tested lower ratios on cheetah but found they performed worse. Note that for parity with DDPG we ran MVE-DDPG with only 4 gradient steps.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Performance", "weight": 1.0} -->

Our result shows that incorporating synthetic samples from a learned model can drastically improve the performance of model-free RL, greatly reducing the number of samples required to attain good performance. As illustrated by the comparison to the IB baseline, this improvement is obtained only when carefully incorporating this synthetic experience via a short horizon and the TD-$k$ trick. As we will discuss in the next section, the specific design decisions here are critical for good results, which helps to explain the lack of success with learned neural network models observed with related methods in prior work[naf].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Performance", "weight": 1.0} -->

MVE-DDPG improves on similar approaches, such as MA-DDPG, by its treatment of synthetic data obtained from the dynamics model. This alternative approach adds simulated data back into a separate imagination buffer, effectively modifying $\beta$ from Alg.[alg:mve] into a mixture between $\beta$ and simulated data (where the mixture is dependent on the relative number of samples taken from each buffer). This is problematic because the policy changes during training, so the data from this mixed distribution of real and fake data is stale relative to $\nu$ in terms of representing actions that would be taken by $\pi$. In our implementation of MA-DDPG, we do not reuse imagined states in this manner, but MVE-DDPG still outperforms MA-DDPG. We suspect this is due to two factors: the staleness of the imaginary states in the IB approach, and the delicate interaction between using more imaginary data and overtraining the actor. In order to use the additional synthetic data, an IB approach must take more gradient steps with imaginary batches.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Performance", "weight": 1.0} -->

On the other hand, since MVE-DDPG uses a gradient averaged over both real and simulated data, the choice to make additional gradient steps becomes an independent consideration dependent on the stability of the actor-critic method being trained.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance", "weight": 1.0} -->

Learning curves comparing MVE with learned dynamics (purple), MVE without the TD-$k$ trick (orange), IB (blue), and DDPG (black) on (a) cheetah, (b) swimmer, and (b) walker. We used $H=10$ for (a,b), but found the same dynamics class inadequate for walker, reducing walker experiments to $H=3$ reduces the improvement MVE has to offer over DDPG, but it still exhibits greater robustness to the poor model fit than IB. Note that we use MA-DDPG, not MA-BDDPG in the IB approach. The bootstrap estimation in MA-BDDPG may reduce model use in some cases, so it is possible that MA-BDDPG would have improved performance in walker, where the learned dynamics are poor compared to the other environments.

<!-- chunk {"id": "body-0054", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

We make sure that MVE can make use of accurate models to improve the critic value estimate (Fig. [fig:learned-hc-hs]). The improved critic performance results in faster training compared to the $H=0$ DDPG baseline on cheetah. Also, we replicate the density plot from DDPG to analyze $Q$ accuracy directly, from which it is clear that MVE improves the critic by providing better target values (Fig.[fig:qdensity]).

<!-- chunk {"id": "body-0055", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

In addition, we verify that the TD- $k$ trick is essential to training $\hat Q$ appropriately. To do so, we conduct an ablation analysis on the cheetah environment: we hold all parameters constant and substitute the learned dynamics model $\hat f$ with the true dynamics model $f$, making model error zero. If $\MSE_{\beta}(\hat Q)\approx \MSE_{(f^\pi)^H\beta}(\hat Q)$, the MVE estimates must improve exponentially in $H$, even without the TD-$k$ trick. However, this is not the case. With the TD-$k$ trick, increasing $H$ yields increasing but diminishing returns (Fig.[fig:hc-true]). Without the adjustment for distribution mismatch, past a certain point, increasing $H$ hurts performance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

Because the dynamics model is ideal in these cases, the only difference is that the critic $\hat Q$ is trained on the distribution of states $\nu=\frac{1}{H}\sum_{t=0}^{H-1}(f^\pi)^t\beta$ instead of $\beta$, where $\beta$ is the empirical distribution resulting from the replay buffer. Since the TD-$k$ trick increases the support of the training data on which $\hat Q$ is trained, the function class for the critic may need to have sufficient capacity to capture the new distribution, but we did not find this to be an issue in our experiments.

<!-- chunk {"id": "body-0057", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

Learning curves from cheetah for MVE-DDPG with learned dynamics at different model horizons $H$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

We plot the true observed cumulative discounted returns against those predicted by the critic for cheetah at the end of training (both values are normalized), reconstructing Fig.3 of. The dotted black line represents unity. An ideal critic concentrates over the line. We verify that with MVE at $H=30$ with the true dynamics model trains a critic with improved $Q$ values relative to the original DDPG algorithm. Both of the above runs use a reduced mini-batch size because oracle dynamics are expensive to compute.

<!-- chunk {"id": "body-0059", "role": "body", "section": "MVE as Critic Improvement", "weight": 1.0} -->

Learning curves for the cheetah environment for MVE-DDPG with an ideal, oracle dynamical model at different horizons $H$ of model prediction. We examine performance (a) with and (b) without the TD-$k$ trick. $H=0$ implies no model use; this is the original DDPG. First, (a) exemplifies that improving value estimation with a model has a marked effect on performance in dense reward environments and offers an upper bound to the improvement that can result from learned-dynamics MVE. Note that as mentioned in Fig.fig:qdensity the batch size for oracle dynamics evaluations was reduced out of computational necessity, so these curves are not comparable to Fig.fig:learned-hc-hs. The diminishing returns for increases in $H$ that we observe further emphasize that model improvement is captured even with a short horizon. Second, (b) demonstrates the value of the TD-$k$ trick: for small $H$, distribution mismatch is small so (b) still shows a performance improvement, but as $H$ increases we lose the monotonic improvements observed in (a).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduce the model-based value expansion (MVE) method, an algorithm for incorporating predictive models of system dynamics into model-free value function estimation. Our approach provides for improved sample complexity on a range of continuous action benchmark tasks, and our analysis illuminates some of the design decisions that are involved in choosing how to combine model-based predictions with model-free value function learning.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Existing approaches following a general Dyna-like approach to using imagination rollouts for improvement of model-free value estimates either use stale data in an imagination buffer or use the model to imagine past horizons where the prediction is accurate. Multiple heuristics [metrpo,kalweit] have been proposed to reduce model usage to combat such problems, but these techniques generally involve a complex combination of uncertainty estimation and additional hyperparameters and may not always appropriately restrict model usage to reasonable horizon lengths. MVE offers a single, simple, and adjustable notion of model trust ($H$), and fully utilizes the model to that extent. MVE also demonstrates that state dynamics prediction enables on-policy imagination via the TD-$k$ trick starting from off-policy data.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work justifies further exploration in model use for model-free sample complexity reduction. In particular, estimating uncertainty in the dynamics model explicitly would enable automatic selection of $H$. To deal with sparse reward signals, we also believe it is important to consider exploration with the model, not just refinement of value estimates. Finally, MVE admits extensions into domains with probabilistic dynamics models and stochastic policies via Monte Carlo integration over imagined rollouts.
