<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Equivalence between Policy Gradients and Soft Q-Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Two of the leading approaches for model-free reinforcement learning are policy gradient methods and Q-learning methods. Q-learning methods can be effective and sample-efficient when they work, however, it is not well-understood why they work, since empirically, the Q-values they estimate are very inaccurate. A partial explanation may be that Q-learning methods are secretly implementing policy gradient updates: we show that there is a precise equivalence between Q-learning and policy gradient methods in the setting of entropy-regularized reinforcement learning, that "soft" (entropy-regularized) Q-learning is exactly equivalent to a policy gradient method. We also point out a connection between Q-learning methods and natural policy gradient methods. Experimentally, we explore the entropy-regularized versions of Q-learning and policy gradients, and we find them to perform as well as (or slightly better than) the standard variants on the Atari benchmark. We also show that the equivalence holds in practical settings by constructing a Q-learning method that closely matches the learning dynamics of A3C without using a target network or epsilon-greedy exploration schedule.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods (PG) and $Q$-learning (QL) methods perform updates that are qualitatively similar. In both cases, if the return following an action $a_{t}$ is high, then that action is reinforced: in policy gradient methods, the probability $\pi{(\left. a_{t} \middle| s_{t} \right.)}$ is increased; whereas in $Q$-learning methods, the $Q$-value $Q{(s_{t},a_{t})}$ is increased. The connection becomes closer when we add entropy regularization to these algorithms. With an entropy cost added to the returns, the optimal policy has the form ${\pi{(\left. a \middle| s \right.)}} \propto {\exp{({Q{(s,a)}})}}$; hence policy gradient methods solve for the optimal $Q$-function, up to an additive constant (Ziebart ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

O'Donoghue et al. also discuss the connection between the fixed points and updates of PG and QL methods, though the discussion of fixed points is restricted to the tabular setting, and the discussion comparing updates is informal and shows an approximate equivalence. Going beyond past work, this paper shows that under appropriate conditions, the gradient of the loss function used in $n$-step $Q$-learning is equal to the gradient of the loss used in an $n$-step policy gradient method, including a squared-error term on the value function. Altogether, the update matches what is typically done in "actor-critic" policy gradient methods such as A3C, which explains why Mnih et al. obtained qualitatively similar results from policy gradients and $n$-step $Q$-learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 2 uses the bandit setting to provide the reader with a simplified version of our main calculation. (The main calculation applies to the MDP setting.) Section 3 discusses the entropy-regularized formulation of RL, which is not original to this work, but is included for the reader's convenience. Section 4 shows that the soft $Q$-learning loss gradient can be interpreted as a policy gradient term plus a baseline-error-gradient term, corresponding to policy gradient instantiations such as A3C. Section 5 draws a connection between QL methods that use batch updates or replay-buffers, and natural policy gradient methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some previous work on entropy regularized reinforcement learning (e.g., O'Donoghue et al.; Nachum et al. ) uses entropy bonuses, whereas we use a penalty on Kullback-Leibler (KL) divergence, which is a bit more general. However, in the text, we often refer to "entropy" terms; this refers to "relative entropy", i.e., the KL divergence.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

Let's consider a bandit problem with a discrete or continuous action space: at each timestep the agent chooses an action $a$, and the reward $r$ is sampled according to $P{(\left. r \middle| a \right.)}$, where $P$ is unknown to the agent. Let ${\overline{r}{(a)}} = {{\mathbb{E}}\left\lbrack r \middle| a \right\rbrack}$, and let $\pi$ denote a policy, where $\pi{(a)}$ is the probability of action $a$. Then, the expected per-timestep reward of the policy $\pi$ is ${{\mathbb{E}}_{a \sim \pi}\lbrack r\rbrack} = {\sum_{a}{\pi{(a)}\overline{r}{(a)}}}$ or $\int{{da}\pi{(a)}\overline{r}{(a)}}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

Let's suppose we are maximizing $\eta{(\pi)}$, an entropy-regularized version of this objective: where $\overline{\pi}$ is some "reference" policy, $\tau$ is a "temperature" parameter, and $D_{KL}$ is the Kullback-Leibler divergence. Note that the temperature $\tau$ can be eliminated by rescaling the rewards. However, we will leave it so that our calculations are checkable through dimensional analysis, and to make the temperature-dependence more explicit.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

First, let us calculate the policy $\pi$ that maximizes $\eta$. We claim that $\eta{(\pi)}$ is maximized by $\pi_{\overline{r}}^{\mathcal{B}}$, defined as To derive this, consider the KL divergence between $\pi$ and $\pi_{\overline{r}}^{\mathcal{B}}$: Rearranging and multiplying by $\tau$, Clearly the left-hand side is maximized (with respect to $\pi$) when the KL term on the right-hand side is minimized (as the other term does not depend on $\pi$), and $D_{KL}\left\lbrack \pi\parallel\pi_{\overline{r}}^{\mathcal{B}} \right\rbrack$ is minimized at $\pi = \pi_{\overline{r}}^{\mathcal{B}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

The preceding calculation gives us the optimal policy when $\overline{r}$ is known, but in the entropy-regularized bandit problem, it is initially unknown, and the agent learns about it by sampling. There are two approaches for solving the entropy-regularized bandit problem: A direct, policy-based approach, where we incrementally update the agent's policy $\pi$ based on stochastic gradient ascent on $\eta$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

An indirect, value-based approach, where we learn an action-value function $q_{\theta}$ that estimates and approximates $\overline{r}$, and we define $\pi$ based on our current estimate of $q_{\theta}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

For the policy-based approach, we can obtain unbiased estimates the gradient of $\eta$. For a parameterized policy $\pi_{\theta}$, the gradient is given by We can obtain an unbiased gradient estimate using a single sample $(a,r)$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

In the indirect, value-based approach approach, it is natural to use a squared-error loss: Taking the gradient of this loss, with respect to the parameters of $q_{\theta}$, we get Soon, we will calculate the relationship between this loss gradient and the policy gradient from Equation 7.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

In the indirect, value-based approach, a natural choice for policy $\pi$ is the one that would be optimal if $q_{\theta} = \overline{r}$. Let's denote this policy, called the Boltzmann policy, by $\pi_{q_{\theta}}^{\mathcal{B}}$, where It will be convenient to introduce a bit of notation for the normalizing factor; namely, we define the scalar Then the Boltzmann policy can be written as Note that the term $\tau{\log{\mathbb{E}}_{a \sim \overline{\pi}}}\left\lbrack {\exp{({{\overline{r}{(a)}}/\tau})}} \right\rbrack$, appeared earlier in Equation 6).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

Repeating the calculation from Equation 2 through Equation 6, but with $q_{\theta}$ instead of $\overline{r}$, Hence, $v_{\theta}$ is an estimate of $\eta{(\pi_{q_{\theta}}^{\mathcal{B}})}$, plugging in $q_{\theta}$ for $\overline{r}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

Now we shall show the connection between the gradient of the squared-error loss (Equation 9) and the policy gradient (Equation 7). Rearranging Equation 12, we can write $q_{\theta}$ in terms of $v_{\theta}$ and the Boltzmann policy $\pi_{q_{\theta}}^{\mathcal{B}}$: Let's substitute this expression for $q_{\theta}$ into the squared-error loss gradient (Equation 9).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

Note that we have not yet decided on a sampling distribution $\pi$. Henceforth, we'll assume actions were sampled by $\pi = \pi_{q_{\theta}}^{\mathcal{B}}$. Also, note the derivative of the KL-divergence: Continuing from Equation 17 but setting $\pi = \pi_{q_{\theta}}^{\mathcal{B}}$, Hence, the gradient of the squared error for our action-value function can be broken into two parts: the first part is the policy gradient of the Boltzmann policy corresponding to $q_{\theta}$, the second part arises from a squared error objective, where we are fitting $v_{\theta}$ to the entropy-augmented expected reward $\overline{r}{(a)} - \tau D_{KL}\left\lbrack \pi_{q_{\theta}}^{\mathcal{B}}\parallel\overline{\pi} \right\rbrack$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Bandit Setting", "weight": 1.0} -->

Soon we will derive an equivalent interpretation of $Q$-function regression in the MDP setting, where we are approximating the state-value function $Q^{\pi,\gamma}$. However, we first need to introduce an entropy-regularized version of the reinforcement learning problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Entropy-Regularized Reinforcement Learning", "weight": 1.0} -->

We shall consider an entropy-regularized version of the reinforcement learning problem, following various prior work (Ziebart; Fox et al.; Haarnoja et al.; Nachum et al. ).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Entropy-Regularized Reinforcement Learning", "weight": 1.0} -->

Specifically, let us define the entropy-augmented return to be $\sum_{t = 0}^{\infty}{\gamma^{t}{({r_{t} - {\tau{KL}_{t}}})}}$ where $r_{t}$ is the reward, $\gamma \in {\lbrack 0,1\rbrack}$ is the discount factor, $\tau$ is a scalar temperature coefficient, and ${KL}_{t}$ is the Kullback-Leibler divergence between the current policy $\pi$ and a reference policy $\overline{\pi}$ at timestep $t$: ${KL}_{t} = D_{KL}\left\lbrack \pi{( \cdot |s_{t})}\parallel\overline{\pi}{( \cdot |s_{t})} \right\rbrack$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Entropy-Regularized Reinforcement Learning", "weight": 1.0} -->

We will sometimes use the notation ${KL}{(s)} = D_{KL}\left\lbrack \pi\parallel\overline{\pi} \right\rbrack{(s)} = D_{KL}\left\lbrack \pi{( \cdot |s)}\parallel\overline{\pi}{( \cdot |s)} \right\rbrack$. To emulate the effect of a standard entropy bonus (up to a constant), one can define $\overline{\pi}$ to be the uniform distribution. The subsequent sections will generalize some of the concepts from reinforcement learning to the setting where we are maximizing the entropy-augmented discounted return.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Value Functions", "weight": 1.0} -->

We are obliged to alter our definitions of value functions to include the new KL penalty terms. We shall define the state-value function as the expected return: and we shall define the $Q$-function as Note that this $Q$-function does not include the first KL penalty term, which does not depend on the action $a_{0}$. This definition makes some later expressions simpler, and it leads to the following relationship between $Q_{\pi}$ and $V_{\pi}$: which follows from matching terms in the sums in Equations 24 and 25.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Boltzmann Policy", "weight": 1.0} -->

In standard reinforcement learning, the "greedy policy" for $Q$ is defined as ${{\lbrack{\mathcal{G}Q}\rbrack}{(s)}} = {{{\arg\max}_{a}Q}{(s,a)}}$. With entropy regularization, we need to alter our notion of a greedy policy, as the optimal policy is stochastic. Since $Q_{\pi}$ omits the first entropy term, it is natural to define the following stochastic policy, which is called the Boltzmann policy, and is analogous to the greedy policy: where the second equation is analogous to Equation 2 from the bandit setting.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Boltzmann Policy", "weight": 1.0} -->

Also analogously to the bandit setting, it is natural to define $V_{Q}$ (a function of $Q$) as Under this definition, it also holds that in analogy with Equation 13. Hence, $V_{Q}{(s)}$ can be interpreted as an estimate of the expected entropy-augmented return, under the Boltzmann policy $\pi_{Q}^{\mathcal{B}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Fixed-Policy Backup Operators", "weight": 1.0} -->

The $\mathcal{T}_{\pi}$ operators (for $Q$ and $V$) in standard reinforcement learning correspond to computing the expected return with a one-step lookahead: they take the expectation over one step of dynamics, and then fall back on the value function at the next timestep. We can easily generalize these operators to the entropy-regularized setting. We define Repeatedly applying the $\mathcal{T}_{\pi}$ operator ${{(\mathcal{T}_{\pi}^{n}V = \underset{n\text{~times}}{\underbrace{\mathcal{T}_{\pi}{(\mathcal{T}_{\pi}{(\ldots\mathcal{T}_{\pi}}}}}{(V)})})})$ corresponds to computing the expected return with a multi-step lookahead.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Fixed-Policy Backup Operators", "weight": 1.0} -->

That is, repeatedly expanding the definition of $\mathcal{T}_{\pi}$, we obtain As a sanity check, note that in both equations, the left-hand side and right-hand side correspond to estimates of the total discounted return $\sum_{t = 0}^{\infty}{\gamma^{t}{({r_{t} - {\tau{KL}_{t}}})}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Fixed-Policy Backup Operators", "weight": 1.0} -->

The right-hand side of these backup formulas can be rewritten using "Bellman error" terms $\delta_{t}$. To rewrite the state-value ($V$) backup, define

<!-- chunk {"id": "body-0028", "role": "body", "section": "Boltzmann Backups", "weight": 1.0} -->

We can define another set of backup operators corresponding to the Boltzmann policy, ${\pi{(\left. a \middle| s \right.)}} \propto {\overline{\pi}{(\left. a \middle| s \right.)}{\exp{({{Q{(s,a)}}/\tau})}}}$. We define the following Boltzmann backup operator: where the simplification from $(\ast)$ to $(\ast \ast)$ follows from the same calculation that we performed in the bandit setting (Equations 11 and 13).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Boltzmann Backups", "weight": 1.0} -->

One can similarly define the TD($\lambda$) version of this backup operator One can straightforwardly verify by comparing terms that it satisfies

<!-- chunk {"id": "body-0030", "role": "body", "section": "Policy Gradients", "weight": 1.0} -->

Entropy regularization is often used in policy gradient algorithms, with gradient estimators of the form However, these are not proper estimators of the entropy-augmented return $\sum_{t}{({r_{t} - {\tau{KL}_{t}}})}$, since they don't account for how actions affect entropy at future timesteps. Intuitively, one can think of the KL terms as a cost for "mental effort". Equation 48 only accounts for the instantaneous effect of actions on mental effort, not delayed effects.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Policy Gradients", "weight": 1.0} -->

To compute proper gradient estimators, we need to include the entropy terms in the return. We will define the discounted policy gradient in the following two equivalent ways---first, in terms of the empirical return; second, in terms of the value functions $V_{\pi}$ and $Q_{\pi}$: In the special case of a finite-horizon problem---i.e., $r_{t} = {KL}_{t} = 0$ for all $t \geq T$---the undiscounted ($\gamma = 1$) return is finite, and it is meaningful to compute its gradient. In this case, $g_{1}{(\pi_{\theta})}$ equals the undiscounted policy gradient: This result is obtained directly by considering the stochastic computation graph for the loss (Schulman et al.), shown in the figure on the right.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy Gradients", "weight": 1.0} -->

Since $g_{1}{(\pi_{\theta})}$ computes the gradient of the entropy-regularized return, one interpretation of $g_{\gamma}{(\pi_{\theta})}$ is that it is an approximation of the undiscounted policy gradient $g_{1}{(\pi_{\theta})}$, but that it allows for lower-variance gradient estimators by ignoring some long-term dependencies. A different interpretation of $g_{\gamma}{(\pi)}$ is that it gives a gradient flow such that $\pi^{\ast} = \pi_{Q_{\ast}}^{\mathcal{B}}$ is the (possibly unique) fixed point.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy Gradients", "weight": 1.0} -->

As in the standard MDP setting, one can define approximations to $g_{\gamma}$ that use a value function to truncate the returns for variance reduction. These approximations can take the form of $n$-step methods (Mnih et al.) or TD($\lambda$)-like methods (Schulman et al.), though we will focus on $n$-step returns here. Based on the definition of $g_{\gamma}$ above, the natural choice of variance-reduced estimator is where $\delta_{t}$ was defined in Equation 36.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Gradients", "weight": 1.0} -->

The state-value function $V$ we use in the above formulas should approximate the entropy augmented return $\sum_{t = 0}^{\infty}{\gamma^{t}{({r_{t} - {\tau{KL}_{t}}})}}$. We can fit $V$ iteratively by approximating the $n$-step backup $V\leftarrow{\mathcal{T}_{\pi}^{n}V}$, by minimizing a squared-error loss

<!-- chunk {"id": "body-0035", "role": "body", "section": "Soft $Q$-learning Gradient Equals Policy Gradient", "weight": 1.0} -->

This section shows that the gradient of the squared-error loss from soft $Q$-learning (Section 3.5) equals the policy gradient (in the family of policy gradients described in Section 3.6) plus the gradient of a squared-error term for fitting the value function. We will not make any assumption about the parameterization of the $Q$-function, but we define $V_{\theta}$ and $\pi_{\theta}$ as the following functions of the parameterized $Q$-function $Q_{\theta}$: Here, $\pi_{\theta}$ is the Boltzmann policy for $Q_{\theta}$, and $V_{\theta}$ is the normalizing factor we described above. From these definitions, it follows that the $Q$-function can be written as We will substitute this expression into the squared-error loss function. First, for convenience, let us define $\Delta_{t} = {\sum_{d = 0}^{n - 1}{\gamma^{d}\delta_{t + d}}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Soft $Q$-learning Gradient Equals Policy Gradient", "weight": 1.0} -->

Now, let's consider the gradient of the $n$-step soft $Q$-learning objective: Note that the equivalent policy gradient method multiplies the policy gradient by a factor of $\tau$, relative to the value function error. Effectively, the value function error has a coefficient of $\tau^{- 1}$, which is larger than what is typically used in practice (Mnih et al.). We will analyze this choice of coefficient in the experiments.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Soft $Q$-learning and Natural Policy Gradients", "weight": 1.0} -->

The previous section gave a first-order view on the equivalence between policy gradients and soft $Q$-learning; this section gives a second-order, coordinate-free view. As previous work has pointed out, the natural gradient is the solution to a regression problem; here we will explore the relation between that problem and the nonlinear regression in soft $Q$-learning.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Soft $Q$-learning and Natural Policy Gradients", "weight": 1.0} -->

Now let us interpret the least-squares problem in Equation 66. $\mathbf{\Psi}\mathbf{w}$ is the vector whose $t^{\text{th}}$ row is ${{{\nabla_{\theta}\log}\pi_{\theta}}{(\left. a \middle| s \right.)}} \cdot \mathbf{w}$. According to the definition of the gradient, if we perform a parameter update with ${\theta - \theta_{\text{old}}} = {\epsilon\mathbf{w}}$, the change in ${\log\pi_{\theta}}{(\left. a \middle| s \right.)}$ is as follows, to first order in $\epsilon$: Thus, we can interpret the least squares problem (Equation 66) as solving That is, we are adjusting each log-probility ${\log\pi_{\theta_{\text{old}}}}{(\left.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Soft $Q$-learning and Natural Policy Gradients", "weight": 1.0} -->

In entropy-regularized reinforcement learning, we have an additional term for the gradient of the KL-divergence: where the second line used the formula for the KL-divergence (Equation 21) and the identity that\${{\mathbb{E}}_{a_{t} \sim \pi_{\theta}}\left\lbrack {{{{\nabla_{\theta}\log}\pi_{\theta}}{(\left. a_{t} \middle| s_{t} \right.)}} \cdot {const}} \right\rbrack} = 0$ (where the KL term is the constant.) In this case, the corresponding least squares problem (to compute $F^{- 1}g$) is Now let's consider $Q$-learning. Let's assume that the value function is unchanged by optimization, so $V_{\theta} = V_{\theta_{\text{old}}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Soft $Q$-learning and Natural Policy Gradients", "weight": 1.0} -->

(Otherwise, the equivalence will not hold, since the value function will try to explain the measured advantage $\Delta$, shrinking the advantage update.)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Soft $Q$-learning and Natural Policy Gradients", "weight": 1.0} -->

We can recover the natural policy gradient by instead solving a damped version of the $Q$-function regression problem. Define ${\hat{Q}}_{t}^{\epsilon} = {{{({1 - \epsilon})}Q_{\theta_{\text{old}}}{(s_{t},a_{t})}} + {\epsilon{\hat{Q}}_{t}}}$, i.e., we are interpolating between the old value and the backed-up value. which exactly matches the expression in the least squares problem in Equation 71, corresponding to entropy-regularized natural policy gradient. Hence, the "damped" $Q$-learning update corresponds to a natural gradient step.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

To complement our theoretical analyses, we designed experiments to study the following questions: Though one-step entropy bonuses are used in PG methods for neural network policies (Williams; Mnih et al.), how do the entropy-regularized RL versions of policy gradients and $Q$-learning described in Section 3 perform on challenging RL benchmark problems? How does the "proper" entropy-regularized policy gradient method (with entropy in the returns) compare to the naive one (with one-step entropy bonus)? (Section 6.1) How do the entropy-regularized versions of $Q$-learning (with logsumexp) compare to the standard DQN of Mnih et al. ? (Section 6.2) The equivalence between PG and soft $Q$-learning is established in expectation, however, the actual gradient estimators are slightly different due to sampling. Furthermore, soft $Q$-learning is equivalent to PG with a particular penalty coefficient on the value function error. Does the equivalence hold under practical conditions? (Section 6.3)

<!-- chunk {"id": "body-0043", "role": "body", "section": "A2C on Atari: Naive vs Proper Entropy Bonuses", "weight": 1.0} -->

Here we investigated whether there is an empirical effect of including entropy terms when computing returns, as described in Section 3. In this section, we compare the naive and proper policy gradient estimators: In the experiments on Atari, we take $\overline{\pi}$ to be the uniform distribution, which gives a standard entropy bonus up to a constant.

<!-- chunk {"id": "body-0044", "role": "body", "section": "A2C on Atari: Naive vs Proper Entropy Bonuses", "weight": 1.0} -->

We start with a well-tuned (synchronous, deterministic) version of A3C (Mnih et al. ), henceforth called A2C (advantage actor critic), to optimize the entropy-regularized return. We use the parameter $\tau = 0.01$ and train for $320$ million frames. We did not tune any hyperparameters for the "proper" algorithm---we used the same hyperparameters that had been tuned for the "naive" algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "A2C on Atari: Naive vs Proper Entropy Bonuses", "weight": 1.0} -->

As shown in Figure 1, the "proper" version yields performance that is the same or possibly greater than the "naive" version. Hence, besides being attractive theoretically, the entropy-regularized formulation could lead to practical performance gains.

<!-- chunk {"id": "body-0046", "role": "body", "section": "DQN on Atari: Standard vs Soft", "weight": 1.0} -->

Here we investigated whether soft $Q$-learning (which optimizes the entropy-augmented return) performs differently from standard "hard" $Q$-learning on Atari. We made a one-line change to a DQN implementation: The difference between the entropy bonus and KL penalty (against uniform) is simply a constant, however, this constant made a big difference in the experiments, since a positive constant added to the reward encourages longer episodes. Note that we use the same epsilon-greedy exploration in all conditions; the only difference is the backup equation used for computing $y_{t}$ and defining the loss function.

<!-- chunk {"id": "body-0047", "role": "body", "section": "DQN on Atari: Standard vs Soft", "weight": 1.0} -->

The results of two runs on each game are shown in Figure 2. The entropy-bonus version with $\tau = 0.1$ seems to perform a bit better than standard DQN, however, the KL-bonus version performs worse, so the benefit may be due to the effect of adding a small constant to the reward. We have also shown the results for $5$-step $Q$-learning, where the algorithm is otherwise the same. The performance is better on Pong and $Q$-bert but worse on other games---this is the same pattern of performance found with $n$-step policy gradients. (E.g., see the A2C results in the preceding section.)

<!-- chunk {"id": "body-0048", "role": "body", "section": "Entropy Regularized PG vs Online $Q$-Learning on Atari", "weight": 1.0} -->

Next we investigate if the equivalence between soft $Q$-learning and PG is relevant in practice---we showed above that the gradients are the same in expectation, but their variance might be different, causing different learning dynamics. For these experiments, we modified the gradient update rule used in A2C while making no changes to any algorithmic component, i.e. parallel rollouts, updating parameters every $5$ steps, etc. The $Q$-function was represented as: ${Q_{\theta}{(s,a)}} = {{V_{\theta}{(s)}} + {\tau{\log\pi_{\theta}}{(\left. a \middle| s \right.)}}}$, which can be seen as a form of dueling architecture with $\tau{\log\pi_{\theta}}{(\left. a \middle| s \right.)}$ being the "advantage stream" (Wang et al. ).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Entropy Regularized PG vs Online $Q$-Learning on Atari", "weight": 1.0} -->

$V_{\theta},\pi_{\theta}$ are parametrized as the same neural network as A2C, where convolutional layers and the first fully connected layer are shared. $\pi_{\theta}{(\left. a \middle| s \right.)}$ is used as behavior policy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Entropy Regularized PG vs Online $Q$-Learning on Atari", "weight": 1.0} -->

A2C can be seen as optimizing a combination of a policy surrogate loss and a value function loss, weighted by hyperparameter $c$: In normal A2C, we have found $c = 0.5$ to be a robust setting that works across multiple environments. On the other hand, our theory suggests that if we use this $Q$-function parametrization, soft $Q$-learning has the same expected gradient as entropy-regularized A2C with a specific weighting $c = \frac{1}{\tau}$. Hence, for the usual entropy bonus coefficient setting $\tau = 0.01$, soft $Q$-learning is implicitly weighting value function loss a lot more than usual A2C setup ($c = 100$ versus $c = 0.5$). We have found that such emphasis on value function ($c = 100$) results in unstable learning for both soft $Q$-learning and entropy-regularized A2C.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Entropy Regularized PG vs Online $Q$-Learning on Atari", "weight": 1.0} -->

Therefore, to make $Q$-learning exactly match known good hyperparameters used in A2C, we scale gradients that go into advantage stream by $\frac{1}{\gamma}$ and scale gradients that go into value function stream by $c = 0.5$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Entropy Regularized PG vs Online $Q$-Learning on Atari", "weight": 1.0} -->

With the same default A2C hyperparameters, learning curves of PG and QL are almost identical in most games (Figure 3), which indicates that the learning dynamics of both update rules are essentially the same even when the gradients are approximated with a small number of samples. Notably, the $Q$-learning method here demonstrates stable learning without the use of target network or $\epsilon$ schedule.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We study the connection between two of the leading families of RL algorithms used with deep neural networks. In a framework of entropy-regularized RL we show that soft $Q$-learning is equivalent to a policy gradient method (with value function fitting) in terms of expected gradients (first-order view). In addition, we also analyze how a damped $Q$-learning method can be interpreted as implementing natural policy gradient (second-order view). Empirically, we show that the entropy regularized formulation considered in our theoretical analysis works in practice on the Atari RL benchmark, and that the equivalence holds in a practically relevant regime.
