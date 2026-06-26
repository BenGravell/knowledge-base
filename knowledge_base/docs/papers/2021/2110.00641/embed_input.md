<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Batch Size-invariance for Policy Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We say an algorithm is batch size-invariant if changes to the batch size can largely be compensated for by changes to other hyperparameters. Stochastic gradient descent is well-known to have this property at small batch sizes, via the learning rate. However, some policy optimization algorithms (such as PPO) do not have this property, because of how they control the size of policy updates. In this work we show how to make these algorithms batch size-invariant. Our key insight is to decouple the proximal policy (used for controlling policy updates) from the behavior policy (used for off-policy corrections). Our experiments help explain why these algorithms work, and additionally show how they can make more efficient use of stale data.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\usepackage[final]{neurips\_2022} \usepackage[utf8]{inputenc} % allow utf-8 input \usepackage[T1]{fontenc} % use 8-bit T1 fonts \usepackage{hyperref} % hyperlinks \usepackage{url} % simple URL typesetting \usepackage{booktabs} % professional-quality tables \usepackage{amsfonts} % blackboard math symbols \usepackage{nicefrac} % compact symbols for 1/2, etc. \usepackage{microtype} % microtypography \usepackage{amsmath, xcolor, tikz, pgfplots, caption, subcaption, algorithm, algpseudocode} \captionsetup[table]{skip=10pt} \def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item} \let\endchangemargin=\endlist \title{Batch size-invariance for policy

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

optimization} \texttt{jhilton@openai.com} \\\texttt{karl@openai.com} \\\texttt{joschu@openai.com} \\We say an algorithm is \textit{batch size-invariant} if changes to the batch size can largely be compensated for by changes to other hyperparameters.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Stochastic gradient descent is well-known to have this property at small batch sizes, via the learning rate. However, some policy optimization algorithms (such as PPO) do not have this property, because of how they control the size of policy updates. In this work we show how to make these algorithms batch size-invariant. Our key insight is to decouple the proximal policy (used for controlling policy updates) from the behavior policy (used for off-policy corrections). Our experiments help explain why these algorithms work, and additionally show how they can make more efficient use of stale data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Policy gradient-based methods for reinforcement learning have enjoyed great success in recent years. The stability and reliability of these methods is typically improved by controlling the size of policy updates, using either a ``trust region'' (TRPO) or a surrogate objective (PPO). The usual justification for this is that we cannot trust updates that take us too far from the policy used to collect experience, called the \textit{behavior policy}. In this work we identify a subtle flaw with this: the behavior policy is irrelevant to the justification. Instead, what matters is that we control \textit{how fast} the policy is updated, or put another way, that we approximate the natural policy gradient.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our key insight is that the ``old'' policy in these methods serves two independent purposes. The first purpose is for off-policy corrections, via importance sampling, for which the old policy must be the behavior policy. The second purpose is to control the size of policy updates, for which the old policy can be any recent policy, which we call the \textit{proximal policy}. It does not matter whether the proximal policy is also the behavior policy; it only matters \textit{how old} the proximal policy is. We demonstrate this by running PPO with stale data collected using a policy from multiple iterations ago, which causes performance to quickly degrade unless the proximal policy is decoupled from the behavior policy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our insight allows us to make PPO \textit{batch size-invariant}, meaning that when the batch size is changed, we can preserve behavior, as a function of the number of examples processed, by changing other hyperparameters (as long as the batch size is sufficiently small). We achieve this by using an exponentially-weighted moving average (EWMA) of the policy network's weights as the network for the proximal policy. Batch size-invariance has been studied many times before (see Section invariancesgd), sometimes under the name ``perfect scaling''. It is of practical benefit because the batch size has a big influence on training, but is often constrained by computational resources such as GPU memory. If an algorithm is batch size-invariant, then the batch size may be freely adjusted according to computational constraints, while other hyperparameters are adjusted formulaically to compensate.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The remainder of the paper is structured as follows.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In Section decouple, we explain the difference between the proximal and behavior policies, and show how to decouple them in PPO's objectives. In Section invariance, we explain the concept of batch size-invariance, and how it applies to SGD and Adam. In Section ewma, we introduce PPO-EWMA and PPG-EWMA, variants of PPO and PPG that make use of our decoupled objectives, and show how to make them batch size-invariant at small batch sizes. In Section experiments, we provide experimental evidence for our central claims: that decoupling the proximal policy from the behavior policy can be beneficial, and that it allows us to achieve batch size-invariant policy optimization. Finally, in Section discussion, we discuss the theoretical and practical implications of our results.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Decoupled policy objectives}\label{decouple} In this section we explain the difference between the proximal and behavior policies, and introduce new versions of PPO's objectives in which they have been decoupled.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Body", "weight": 1.0} -->

PPO alternates between sampling data through interaction with the environment, and optimizing a surrogate objective. The policy used for sampling is denoted $\pi_{\theta_{\mathrm{old}}}$, and is used by the objective in two different ways.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The first use of $\pi_{\theta_{\mathrm{old}}}$ in this expression is as part of an importance sampling ratio. In order for the policy gradient estimate to be unbiased, this policy needs to be the one that was used for sampling, so we call this the \textit{behavior policy} $\pi_{\theta_{\mathrm{behav}}}$. The second use of $\pi_{\theta_{\mathrm{old}}}$ is as a recent target to pull the current policy towards, so we call this the \textit{proximal policy} $\pi_{\theta_{\mathrm{prox}}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our key insight is that \textbf{the proximal policy need not equal the behavior policy}. As we will show experimentally, it matters \textit{how old} the proximal policy is, but it does not matter whether or not the proximal policy was used for sampling.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It is less obvious how to decouple the clipped PPO objective, because $\pi_{\theta_{\mathrm{old}}}$ only appears once in that expression: \[L^{\mathrm{CLIP}}\left(\theta\right):=\hat{\mathbb E}\_t\left[\min\left(r\_t\left(\theta\right)\hat A\_t,\operatorname{clip}\left(r\_t\left(\theta\right),1-\epsilon,1+\epsilon\right)\hat A\_t\right)\right],\] where $r_t\left(\theta\right):=\frac{\pi_\theta\left(a_t\mid s_t\right)}{\pi_{\theta_{\mathrm{old}}}\left(a_t\mid s_t\right)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Now the first use of $\pi_{\theta_{\mathrm{old}}}$ is as part of an importance sampling ratio, for which we must use the behavior policy, and the second and third uses are in applying the implicit KL penalty, for which we can use the proximal policy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As a sanity check, note that if we set the KL penalty coefficient $\beta=0$ or the clipping parameter $\epsilon=\infty$, then the dependence on the proximal policy disappears, and we recover the vanilla (importance-sampled) policy gradient objective.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Batch size-invariance}\label{invariance} We say an algorithm is \textit{batch size-invariant} to mean that when the batch size is changed, the original behavior can be approximately recovered by adjusting other hyperparameters to compensate. Here we consider behavior as a function of the total number of examples processed, so another way to put this is that doubling the batch size halves the number of steps needed. and refer to this as ``perfect scaling''.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We treat batch size-invariance as a descriptive property that can hold to some degree, rather than as a binary property. In practice, the original behavior can never be recovered perfectly, and the extent to which it can be recovered depends on both how much and the direction in which the batch size is changed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Batch size-invariance for stochastic gradient descent}\label{invariancesgd} Stochastic gradient descent (SGD) is batch size-invariant, up until the batch size approaches some critical batch size. This is the batch size at which the gradient has a signal-to-noise ratio of around 1. At smaller batch sizes than this, changes to the batch size can be compensated for by a directly proportional adjustment to the learning rate. This core observation has been made many times before. A discussion of this and other previous work can be found in Section previousinvariance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\textbf{Sketch explanation.} For the benefit of the reader's intuition, we sketch the explanation for SGD's batch size-invariance. For a much more thorough explanation, we refer the reader to.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider running SGD on a loss function $L\left(\theta;x\right)$ of a parameter vector $\theta$ and a data point $x$. Two steps with batch size $n$ and learning rate $\alpha$ corresponds to the update rule \[\theta\_{t+2}=\theta\_t-\frac\alpha n\sum\_{x\in B\_t}\nabla\_\theta L\left(\theta\_t;x\right)-\frac\alpha n\sum\_{x\in B\_{t+1}}\nabla\_\theta L\left(\theta\_{\color{red}t+1};x\right),\] where $B_t$ and $B_{t+1}$ are the next two batches of size $n$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paper Body", "weight": 1.0} -->

On the other hand, a single step with batch size $2n$ and learning rate $2\alpha$ corresponds to the update rule \[\theta\_{t+2}=\theta\_t-\frac{2\alpha}{2n}\sum\_{x\in B\_t\cup B\_{t+1}}\nabla\_\theta L\left(\theta\_{\color{red}t};x\right).\] These update rules are very similar, the only difference being whether the gradient for $B_{t+1}$ is evaluated at $\theta_t$ or $\theta_{t+1}$. If the batch size is small compared to the critical batch size, then the difference between $\theta_t$ and $\theta_{t+1}$ is mostly noise, and moreover this noise is small compared to the total noise accumulated by $\theta_t$ over previous updates. Hence the two update rules behave very similarly.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A good mental model of SGD in this small-batch regime is of the parameter vector making small, mostly random steps around the loss landscape. Over many steps, the noise is canceled out and the parameter vector gradually moves in the direction of steepest descent. But a single additional step makes almost no difference to gradient evaluations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In more formal terms, SGD is numerically integrating a stochastic differential equation (SDE). Changing the learning rate in proportion the batch size leaves the SDE unchanged, and only affects the step size of the numerical integration. Once the step size is small enough (the condition that gives rise to the critical batch size), the discretization error is dominated by the noise, and so the step size stops mattering.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Batch size-invariance for Adam} Adam is a popular variant of SGD, and is also batch size-invariant until the batch size approaches a critical batch size (which may be different to the critical batch size for SGD). To compensate for the batch size being divided by some constant $c$, one must make the following adjustments: Divide the step size $\alpha$ by $\sqrt c$. (Raise the exponential decay rates $\beta_1$ and $\beta_2$ to the power of $\nicefrac{1}{c}$.)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The first adjustment should be contrasted with the linear learning rate adjustment for vanilla SGD. We discuss the reason for this difference and provide empirical support for the square root rule in Appendix linearlr.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The second adjustment is much less important in practice, since Adam is fairly robust to the $\beta_1$ and $\beta_2$ hyperparameters (hence it has been parenthesized). Note also that $\beta_1$ also affects the relationship between the current policy and the proximal policy in policy optimization. For simplicity, we omitted this adjustment in most of our experiments, but included it in some additional experiments that are detailed in Appendix adambetas.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Batch size-invariance for policy optimization} In policy optimization algorithms like PPO, there are two different batch sizes: the number of environment steps in each gradient step, which we call the \textit{optimization batch size}, and the number of environment steps in each alternation between sampling and optimization, which we call the \textit{iteration batch size}. When we say that such an algorithm is batch size-invariant, we mean that changes to both batch sizes \textit{by the same factor simultaneously} can be compensated. The motivation for this definition is that this is the effect of changing the degree of data-parallelism.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If the optimization algorithm (such as SGD or Adam) used by PPO is batch size-invariant, then by definition this makes PPO \textit{optimization} batch size-invariant. In the next section, we show how to make PPO \textit{iteration} batch size-invariant, and therefore batch size-invariant outright.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To measure batch size-invariance for policy optimization, there are many features of the algorithm's behavior we could look. As a simple metric, we use the final performance of the algorithm, since this is the primary quantity of interest to most practitioners. If an algorithm has a high degree of batch size-invariance, then the difference in final performance at different batch sizes should be small.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{PPO-EWMA and PPG-EWMA}\label{ewma} We now introduce a simple modification that can be made to any PPO-based algorithm: Maintain an exponentially-weighted moving average (EWMA) of the policy network, updating it after every policy gradient step using some decay rate $\beta_{\mathrm{prox}}$. Use this as the network for the proximal policy in one of the decoupled policy objectives.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The motivation for using an EWMA is as follows. We would like to be able to use a policy from some fixed number of steps ago as the proximal policy, but this requires storing a copy of the network from every intermediate step, which is prohibitive if this number of steps is large. Using an EWMA allows us to approximate this policy using more reasonable memory requirements. Although this approximation is not exact, averaging in parameter space may actually improve the proximal policy, and the age of the proximal policy can still be controlled by adjusting $\beta_{\mathrm{prox}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We refer to this modification using the -EWMA suffix. Thus from PPO we obtain PPO-EWMA, and from Phasic Policy Gradient (PPG) we obtain PPG-EWMA. Pseudocode for PPO-EWMA may be found in Appendix pseudocode, and code may be found.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To see how this modification helps us to achieve batch size-invariance, note that the main effect of changing the iteration batch size in PPO is to change the age of the behavior and proximal policies (which are coupled). The age of the behavior policy affects how on-policy the data is, but this does not matter much, as long as it is not too large. However, the age of the proximal policy affects the strength of the KL penalty (or the implicit KL penalty in the case of the clipped objective), which influences how fast the policy can change. We therefore need to maintain the age of the proximal policy as the iteration batch size is changed, which is what our modification enables.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Paper Body", "weight": 1.0} -->

More specifically, to achieve batch size-invariance for PPO- and PPG-EWMA, we make the following adjustments to compensate for the optimization and iteration batch sizes being divided by some constant $c$: Adjust the optimization hyperparameters as described in the previous section, i.e., divide the vanilla SGD learning rate by $c$ or the Adam step size by $\sqrt c$. (We use Adam.) Modify $\beta_{\mathrm{prox}}$ such that $\frac 1{1-\beta_{\mathrm{prox}}}-1$ is multiplied by $c$. (This expression is the center of mass of the proximal policy EWMA, measured in gradient steps.) This adjustment is what keeps the age of the proximal policy constant, measured in environment steps. If using advantage normalization, multiply the number of iterations used to estimate the advantage mean variance by $c$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Paper Body", "weight": 1.0} -->

(In practice, we use EWMAs to estimate the mean and variance, and multiply their effective sample sizes, measured in iterations, by $c$.\footnote{The effective sample size, sometimes called the span, of an EWMA with decay rate $\beta$ is equal to $\frac 2{1-\beta}-1$.}) This keeps the overall sample sizes of these estimates constant, preventing their standard errors becoming too large. For PPG, multiply the number of policy iterations per phase $N_\pi$ by $c$. (We use PPG.)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For these adjustments to work, we require that the optimization batch size is sufficiently small. We also require that the number of policy epochs (denoted $E$ in PPO or $E_\pi$ in PPG) is 1. This is because when the iteration batch size is very small, using multiple policy epochs essentially amounts to training on the same data multiple times in a row, which is redundant (modulo changing the learning rate). Our batch size-invariance experiments therefore use PPG-EWMA, where $E_\pi=1$ is the default.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that PPG has a third batch size: the number of environment steps in each alternation between phases, which we call the \textit{phase batch size}. The effect of our adjustment to $N_\pi$ is to simply hold the phase batch size constant, thereby preserving the dynamics of the policy and auxiliary phases.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Experiments}\label{experiments} To validate our analysis, we ran several experiments on Procgen Benchmark, which we found to serve as a useful testbed due to the difficulty and diversity of the environments. Hyperparameters for all of our experiments can be found in Appendix hyperparameters, and full results on each of the individual environments can be found in Appendix resultsbyenv.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Artificial staleness} To investigate our decoupled policy objectives, we introduced artificial staleness. By this we mean that once data has been sampled through interacting with the environment, it is not immediately used for optimization, but is instead placed in a buffer to be used a fixed number of steps later. Despite being artificial, similar staleness is often encountered in asynchronous training setups, where it is known to cause problems for on-policy algorithms like PPO. We measure staleness in iterations, with one iteration being a single alternation between sampling and optimization.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With artificial staleness, the original PPO objectives are underspecified, since there are two natural choices for $\pi_{\theta_{\mathrm{old}}}$: the policy immediately preceding the current iteration, denoted $\pi_{\theta_{\mathrm{recent}}}$, and the behavior policy $\pi_{\theta_{\mathrm{behav}}}$. However, the decoupled objectives allow us to take the proximal policy $\pi_{\theta_{\mathrm{prox}}}$ to be the recent policy, while continuing to use the behavior policy for importance sampling. This allows the KL penalty (or clipping) to have a consistent effect in terms of controlling how fast the policy changes, while avoiding harmful bias from incorrect importance sampling.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In our experiments, we compare the decoupled objective to both choices for the original objective. Our results are shown in Figure stalenessfigure. With both choices for the original objective, even a small amount of staleness hurts performance. However, with the decoupled objective, performance is robust to a surprising amount of staleness, with minimal degradation until a staleness of around 8 iterations (over 500,000 environment steps). This demonstrates that the decoupling the proximal policy from the behavior policy can be beneficial.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our results are shown in Figures batchsizeinvariancefigure and batchsizeinvariancesummaryfigure. We were able to achieve a high degree of batch size-invariance, with a difference in final mean normalized return between the largest and smallest batch sizes of 0.052. Moreover, there was a single outlier environment, Heist, without which this difference is reduced to 0.019. We conducted further experiments to try to explain this outlier, which we discuss in Appendix adambetas, but we were not successful.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To check the statistical significance of the effects produced by our ablations, we conducted hypothesis tests, which we describe in Appendix hypothesistests. Our null hypothesis was that the ablation had no effect on the difference in final normalized return at different batch sizes in any of the environments. For the comparison between the largest and smallest batch sizes, we rejected the null hypothesis for all of the ablations at the 0.1\% level.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{EWMA comparison} Finally, we tested the outright benefit of the EWMA modification by doing a head-to-head comparison of PPO against PPO-EWMA and of PPG against PPG-EWMA. It is important to note that the EWMA introduces an additional hyperparameter $\beta_{\mathrm{prox}}$, but that this was tuned only on the first 8 of the 16 Procgen environments (and only on PPG), and so the algorithms are ``complete'' on the last 8 environments in the sense of. Our results are shown in Figure headtoheadfigure.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that this benefit comes at the cost of additional memory to store the weights of the EWMA network, and an additional forward pass of the EWMA network for each policy gradient step. With our hyperparameters, this increases the computational cost of PPO by 30\% and of PPG by 2.3\%, not including the cost of stepping the environment.\footnote{These costs are calculated as follows. PPO has 1 forward-only and 3 forward-backward passes per environment step, to which PPO-EWMA adds 3 forward-only passes. PPG has 1 forward-only and 7 forward-backward passes of both networks per environment step, to which PPG-EWMA adds 1 forward-only pass of the policy network.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A forward-backward pass has 3 times the cost of a forward-only pass.} \footnote{In practice, including the time taken to step the environment, the EWMA increased wall-clock time by 19\% for PPO and by 3\% for PPG, but our PPG-EWMA implementation included an additional unnecessary forward pass of an EWMA of the value network.} \section{Discussion}\label{discussion} \subsection{PPO as a natural policy gradient method} Our experiments provide strong empirical support that decoupling the proximal policy from the behavior policy can be beneficial: it can be used to make more efficient use of stale data, to achieve batch size-invariance, and to slightly improve sample efficiency outright. This implies that the usual justification for PPO's surrogate objectives, that they approximate trust region methods, is subtly flawed. Trust region methods keep the policy close to the behavior policy, but it does not matter how far from the behavior policy we move specifically, only that we stay close to \textit{some} recent policy, or in other words, that we do not move too fast.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Instead, we speculate that PPO is better viewed as a natural policy gradient method. These methods select updates that \textit{efficiently} improve performance relative to how much the policy is changed.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This conflicts with the results of, which found constraining updates relative to the behavior policy to be beneficial. With the benefit of hindsight, we believe that at that time, constraint methods had hyperparameters that were easier to tune, but that with the advent of PPO's clipped objective and various normalization schemes, this tends to no longer be the case.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Practical advice for policy optimization at small batch sizes} Batch size is an important hyperparameter in reinforcement learning, since it controls gradient variance, which can be high in challenging environments. But it is often constrained by computational resources such as GPU memory. The benefit of batch size-invariance is that it allows hyperparameters to be tuned at one batch size, and then adjusted to work at a different batch size, which can be selected based on computational constraints.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Paper Body", "weight": 1.0} -->

However, when working in a new domain, we may be constrained to use a small batch size, without having first been able to tune hyperparameters at a larger batch size. We therefore attempt to distill our findings into practical advice for getting policy optimization to work well in a new domain at small batch sizes. Our advice, much of which is already folklore, is as follows: By far the most important hyperparameter to tune is the learning rate (or Adam step size). Once it has been tuned for a certain batch size, it can be adjusted formulaically for use at other batch sizes using the rules given in Section invariance, as long as the batch size remains small. Consider setting the number of policy epochs ($E$ in PPO or $E_\pi$ in PPG) to 1, at least initially. This is the easiest way to maintain stability even if not enough ratios are being clipped. Furthermore, multiple policy epochs are less likely to be beneficial when the iteration batch size is small. If using clipping, monitor the fraction of ratios clipped.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If it is much less than 1\%, then it is probably beneficial to increase the iteration batch size\footnote{The iteration batch size can be increased without changing the sampling or optimization batch size by simultaneously increasing the number of timesteps per rollout ($T$) and the number of minibatches per epoch. However, $T$ also affects the amount of bootstrapping performed, and so the GAE bootstrapping parameter ($\lambda$) may also need to be adjusted to compensate.}, or to use PPO-EWMA with a high $\beta_{\mathrm{prox}}$. If it is much more than 10\% with 1 policy epoch or 20\% with multiple policy epochs, then this is often a sign that the learning rate is too high. If using advantage normalization, monitor the advantage standard deviation estimates. If estimates oscillate by a factor of 10 or more, then it is probably beneficial to perform normalization using data from more iterations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Related work} \subsection{Policy optimization} Policy gradient methods have a long history, going at least as far back as, and were introduced in their modern formulation. Trust regions were introduced into policy optimization, who already noted the similarity with natural policy gradient methods. The trust region approach was simplified by the use of surrogate objectives in PPO, which was introduced. Other key ingredients of PPO include an actor-critic setup similar to that of, and generalized advantage estimation, which was introduced.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Paper Body", "weight": 1.0} -->

PPO's surrogate objectives can also be viewed through the lens of mirror descent, as explained. This perspective also makes it clear that decoupling the proximal policy from the behavior policy is a possibility. Indeed, a similar decoupled objective is proposed in concurrent work of that is motivated by this perspective.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Batch size-invariance}\label{previousinvariance} There has been much previous work on batch size-invariance. The underlying idea of modeling SGD as numerically integrating a stochastic differential equation (SDE) is long-established, going at least as far back as. More recently, and observed that changing the learning rate in proportion the batch size leaves the SDE unchanged, and therefore that SGD is batch size-invariant at small batch sizes. Meanwhile, empirically validated this invariance on ImageNet. and provided further empirical validation for this, as well as for rules describing how the optimal learning rate changes with momentum and training set size.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The term \textit{critical batch size} for the batch size beyond which SGD is no longer batch size-invariant was introduced. Since then a number of works have studied how the critical batch size varies between problems, mostly with the motivation of improving training efficiency at large batch sizes (in contrast to our work, which focuses on maintaining performance at small batch sizes). studied the effect of architectures, datasets and different forms of momentum on the critical batch size, and introduced the term \textit{perfect scaling} for the regime of batch size-invariance. also studied the effect of dataset complexity and size on the critical batch size. measured the critical batch size in a range of domains, and showed that it can be predicted using a measure of the noise-to-signal ratio of the gradient known as the \textit{gradient noise scale}. Finally, studied the effect of curvature on the critical batch size using a noisy quadratic model, and showed that preconditioning can be used to increase the critical batch size.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Policy optimization algorithms such as PPO typically control the size of policy updates using a recent policy we call the proximal policy. We have shown that this policy can be safely decoupled from the behavior policy, which is used to collect experience. We introduced PPO-EWMA and PPG-EWMA, variants of PPO and PPG in which the proximal policy is an exponentially-weighted moving average of the current policy. These variants allow stale data to be used more efficiently, and are slightly more sample efficient outright. Finally, we showed how to make these algorithms batch size-invariant, meaning that when the batch size is changed, we can preserve behavior, as a function of the number of examples processed, by changing other hyperparameters (as long as the batch size is not too large). We discussed our findings, which have both theoretical and practical implications for policy optimization.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We thank David Farhi, Chris Hardin and Holly Mandel for helpful discussions and comments, and anonymous reviewers for helpful and detailed feedback.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%% \item For all authors...%% \item Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?%% \item Did you describe the limitations of your work?%% \answerYes{There are careful ablations and a discussion of the additional computational cost in Section experiments.}%% \item Did you discuss any potential negative societal impacts of your work?%% \answerNo{The main impact of the work is via an improved understanding of policy optimization in general, and the experiments are all on toy environments.}%% \item Have you read the ethics review guidelines and ensured that your paper conforms to them?

<!-- chunk {"id": "body-0061", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%% \item If you are including theoretical results...%% \item Did you state the full set of assumptions of all theoretical results?%% \item Did you include complete proofs of all theoretical results?

<!-- chunk {"id": "body-0062", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%% \item If you ran experiments...%% \item Did you include the code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL)?%% \item Did you specify all the training details (e.g., data splits, hyperparameters, how they were chosen)?%% \item Did you report error bars (e.g., with respect to the random seed after running experiments multiple times)?%% \item Did you include the total amount of compute and the type of resources used (e.g., type of GPUs, internal cluster, or cloud provider)?%% \answerNo{The additional computational cost compared to existing methods is clearly described in Section experiments, from which the total computation cost of the experiments can be calculated.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The type of resources used is proprietary information.}%% \item If you are using existing assets (e.g., code, data, models) or curating/releasing new assets...%% \item If your work uses existing assets, did you cite the creators?%% \item Did you mention the license of the assets?%% \item Did you include any new assets either in the supplemental material or as a URL?%% \item Did you discuss whether and how consent was obtained from people whose data you're using/curating?%% \item Did you discuss whether the data you are using/curating contains personally identifiable information or offensive content?

<!-- chunk {"id": "body-0064", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%% \item If you used crowdsourcing or conducted research with human subjects...%% \item Did you include the full text of instructions given to participants and screenshots, if applicable?%% \item Did you describe any potential participant risks, with links to Institutional Review Board (IRB) approvals, if applicable?%% \item Did you include the estimated hourly wage paid to participants and the total amount spent on participant compensation?

<!-- chunk {"id": "body-0065", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For PPG-EWMA, we make the same changes to the policy phase, while leaving the auxiliary phase unchanged. However, \textbf{the EWMA should be reinitialized at the start of each policy phase}, since $\theta$ changes a lot during the auxiliary phase.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Code for both PPO-EWMA and PPG-EWMA may be found.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Hyperparameters}\label{hyperparameters} All experiments were on Procgen's hard difficulty, without frame stack, using the convolutional neural network from IMPALA. Unless stated otherwise, experiments lasted for 100 million environment steps.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\caption{Default hyperparameters shared between PPO and PPG.} Parallel environments per worker & $64$ \\Timesteps per rollout ($T$) & $256$ \\Minibatches per epoch & $8$ \\Adam step size ($\alpha$) & $5\times 10^{-4}$ \\Value function coefficient & $0.5$ \\PPO clipping parameter ($\epsilon$) & $0.2$ \\GAE discount rate ($\gamma$) & $0.999$ \\GAE bootstrapping parameter ($\lambda$) & $0.95$ \\Reward normalization? & Yes \\Advantage normalization?

<!-- chunk {"id": "body-0069", "role": "body", "section": "Paper Body", "weight": 1.0} -->

& Yes \\\caption{Default PPO-specific hyperparameter.} \caption{Default PPG-specific hyperparameters.} Policy iterations per phase ($N_\pi$) & $32$ \\Policy phase policy epochs ($E_\pi$) & $1$ \\Policy phase value function epochs ($E_V$) & $1$ \\Auxiliary phase epochs ($E_{\mathrm{aux}}$) & $6$ \\Auxiliary phase minibatches per epoch & $16N_\pi$ \\Auxiliary phase cloning coefficient ($\beta_{\mathrm{clone}}$) & $1$ \\For the purpose of the artificial staleness experiments, we clipped $\pi_{\theta_{\mathrm{behav}}}$ to keep the ratio $\frac{\pi_\theta}{\pi_{\theta_{\mathrm{behav}}}}$ below 100, for numerical stability.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For PPG-EWMA, we chose the default EWMA decay rate $\beta_{\mathrm{prox}}$ such that the center of mass of the EWMA, $\frac 1{1-\beta_{\mathrm{prox}}}-1$, equaled the number of minibatches per policy phase iteration, so that the maximum age of the proximal policy is the same in PPG and PPG-EWMA. We tuned this on the first 8 of the 16 Procgen environments by also trying $\frac 1{1-\beta_{\mathrm{prox}}}-1=2$ and $\frac 1{1-\beta_{\mathrm{prox}}}-1=32$, but did not find these to perform better. We did not re-tune $\beta_{\mathrm{prox}}$ on the last 8 Procgen environments or on PPO-EWMA.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\caption{Default PPO-EWMA and PPG-EWMA specific hyperparameter.} Proximal policy EWMA decay rate ($\beta_{\mathrm{prox}}$) & $0.889$ \\For the batch size-invariance experiments, we made the following changes to the above defaults: We reduced the number of parallel environments, first by reducing the number of workers from 4 to 1, and then by reducing the number of parallel environments per worker from 64 to 16 to 4 to 1. For the policy phase, we adjusted the Adam step size ($\alpha$), the proximal policy EWMA decay rate ($\beta_{\mathrm{prox}}$), advantage normalization, and the number of policy iterations per phase ($N_\pi$) in the way described in Section ewma. For the auxiliary phase, we initially tried adjusting the Adam step size in the same way as for the policy phase.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This worked well in terms of batch size-invariance, but resulted in prohibitively large wall-clock times at small batch sizes, due to the large number of auxiliary epochs. We therefore simply kept the auxiliary phase minibatch size per worker constant, and only adjusted the Adam step size when reducing the number of workers, not when reducing the number of parallel environments per worker.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Adam square root step size adjustment}\label{linearlr} In Section invariance, we stated that SGD and Adam have different learning rate adjustment rules. To compensate for the batch size being divided by some constant $c$, one must divide the SGD learning rate by $c$, but divide the Adam step size by $\sqrt c$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The reason for the difference is that Adam divides the gradient by a running estimate of the root mean square gradient.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If the gradient vector at the current step is $g_t$, then this denominator is approximately \[\sqrt{\mathbb E\left[g\_t^2\right]}=\sqrt{\mathbb E\left[g\_t\right]^2+\operatorname{Var}\left[g\_t\right]}=\mathbb E\left[g\_t\right]\sqrt{1+\frac{\operatorname{Var}\left[g\_t\right]}{E\left[g\_t\right]^2}}=\mathbb E\left[g\_t\right]\sqrt{1+\frac{\mathcal B}{n}},\] where all operations including the variance operator are applied componentwise, $n$ is the batch size, and $\mathcal B$ is a componentwise version of the \textit{gradient noise scale} defined, a measure of the noise-to-signal ratio of the gradient that approximates the critical batch size.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Hence if the batch size is small compared to the critical batch size, then $\mathcal B\gg n$ for most components, and so the Adam denominator is approximately proportional to $\frac{1}{\sqrt n}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It follows that if the batch size is divided by some constant $c$, then the Adam denominator is multiplied by approximately $\sqrt c$ (providing the batch size is small compared to the critical batch size). Hence Adam is effectively dividing the learning rate by $\sqrt c$ automatically, and so the step size $\alpha$ only needs to be adjusted by an additional $\sqrt c$ to effectively divide the learning rate by $c$ overall.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This all ignores Adam's $\epsilon$ hyperparameter, which is usually negligible, but is sometimes used to interpolate between Adam and momentum SGD.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To verify the square root rule for Adam, we conducted an ablation of our batch size-invariance experiments, in which we made the exact same adjustments, except that we divided the Adam step size by $c$ instead of by $\sqrt c$. Our results are shown in Figure linearlrmeanfigure. When compared with Figure batchsizeinvariancefigure, this clearly shows that the square root rule is superior in our setting. Full results on each of the individual environments can be found in Appendix resultsbyenvbatchsizeinvariance.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\centerline{\scalebox{%% Creator: Matplotlib, PGF backend%% To include the figure in your LaTeX document, write%% \input{<filename>.pgf}%% Make sure the required packages are loaded in your preamble%% Figures using additional raster images can only be included by \input if%% they are in the same directory as the main LaTeX file.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For loading figures%% from other directories you can use the `import` package%% and then include the figures with%% \import{<path to file>}{<filename>.pgf}%% Matplotlib used the following preamble \pgfpathrectangle{\pgfpointorigin}{\pgfqpoint{6.116660in}{4.116660in}}% \pgfusepath{use as bounding box, clip}% \definecolor{currentstroke}{rgb}{1.000000,1.000000,1.000000}% \definecolor{currentfill}{rgb}{1.000000,1.000000,1.000000}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}%

<!-- chunk {"id": "body-0082", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{-0.048611in}}{\pgfqpoint{0.000000in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=1.753107in,y=0.402469in top]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {0.2}\)}%

<!-- chunk {"id": "body-0083", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{-0.048611in}}{\pgfqpoint{0.000000in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=3.760526in,y=0.402469in top]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {0.6}\)}%

<!-- chunk {"id": "body-0084", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{-0.048611in}}{\pgfqpoint{0.000000in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=5.767946in,y=0.402469in top]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {1.0}\)}%

<!-- chunk {"id": "body-0085", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{-0.048611in}{0.000000in}}{\pgfqpoint{-0.000000in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=0.279012in, y=1.440486in, left, base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {0.2}\)}%

<!-- chunk {"id": "body-0086", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{-0.048611in}{0.000000in}}{\pgfqpoint{-0.000000in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=0.279012in, y=2.911565in, left, base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {0.6}\)}%

<!-- chunk {"id": "body-0087", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.993248,0.906157,0.143936}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=5.071828in,y=0.659413in,left,base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont Default / 256}% \caption{PPG-EWMA at different batch sizes, averaged over all 16 Procgen environments, with hyperparameters adjusted as in Figure batchsizeinvariancefigure, except with a linear rather than a square root adjustment to the Adam learning rate.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Mean and standard deviation over 3 seeds shown.} Our results are in tension with those of, who verified batch size-invariance for Adam using the linear rather than the square root rule. However, they achieved a lower degree of batch size-invariance with Adam than with SGD (see Figure 4 in that work), and moreover, our results show that the batch size needs to be reduced significantly before the difference between the two rules is noticeable. We believe that this accounts for their experimental results, and that the square root rule is superior in general (with the exception of when Adam's $\epsilon$ hyperparameter is high enough for it to behave like momentum SGD).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Adam \texorpdfstring{$\beta_1$}{beta\_1} and \texorpdfstring{$\beta_2$}{beta\_2} adjustments}\label{adambetas} As discussed in Section invariance, there is an additional adjustment one should make when using Adam, other than to the step size $\alpha$. To compensate for the batch size being divided by some constant $c$, one should also raise the exponential decay rates $\beta_1$ and $\beta_2$ to the power of $\nicefrac{1}{c}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We omitted this adjustment in most of our experiments, and were still able to achieve a high degree of batch size invariance. For all except one environment, the difference in normalized return between the largest and smallest batch sizes at the end of training was at most 0.11 (see Figure batchsizeinvariancesummaryfigure). For these environments, it would probably have required many additional experiments to detect any further improvement that adjusting $\beta_1$ and $\beta_2$ might provide. However, for the Heist environment, this difference was 0.55. We hypothesized that this might be explained by the fact that we did not adjust $\beta_1$ and $\beta_2$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We therefore conducted a version of our batch size-invariance experiments in which we either adjusted only $\beta_2$ using the above rule, or adjusted both $\beta_1$ and $\beta_2$. Our results are shown in Figure adambetasfigure. In both cases there was still a large difference in performance at the largest and smallest batch sizes.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our primary metric for measuring batch size-invariance was the difference in final performance of the algorithm at different batch sizes. To get a complete picture of how important our ablations were at different batch sizes, we compared our default (largest) batch size with each of the other batch sizes, and tested the hypothesis that the difference was larger for the ablation. This resulted in 16 hypotheses, corresponding to the 4 ablations and the 4 non-default batch sizes. To test each hypothesis, we used a van Elteren test, a stratified version of the Mann--Whitney $U$-test, treating the different environments as strata. This gives a non-parametric $Z$-test of the null hypothesis that for each of the environments, the probability of the ablation outperforming the original experiment is the same as the probability of the original experiment outperforming the ablation. To reduce noise (and thereby increase statistical power), we measured average performance over the last 4 million timesteps (the length of a single PPG phase). We used a significance level of 0.1\% and applied a Bonferroni correction to account for multiple comparisons.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our results are shown in Table hypothesistestresults. For ablation (b), the difference is only significant at the smallest batch size. For all other ablations, the difference is significant at every batch size, execpt for the largest batch size for ablation (d).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Paper Body", "weight": 1.0} -->

in the limit as $t\to\infty$, and so if $\theta$ were to follow a straight line path for example, then $\theta-\theta_{\mathrm{prox}}$ would be approximately proportional to $\mathrm{COM}_{\mathrm{prox}}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Suppose then that we halve $\mathrm{COM}_{\mathrm{prox}}$. What is the effect of this?

<!-- chunk {"id": "body-0096", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the gradient of the KL divergence from the current policy to the proximal policy, as a function of the proximal policy parameter vector, \[\operatorname{Grad-KL}\left(\theta\_{\mathrm{prox}}\right):=\nabla\_\theta\operatorname{KL}\left[\pi\_{\theta\_{\mathrm{prox}}}\left(\cdot\mid s\_t\right),\pi\_\theta\left(\cdot\mid s\_t\right)\right].\] Since KL divergence is always greater than or equal to $0$, with equality if and only if the input distributions are equal, $\operatorname{Grad-KL}\left(\theta\right)=0$, and hence, to first-order, $\operatorname{Grad-KL}\left(\theta_{\mathrm{prox}}\right)$ is a linear function of

<!-- chunk {"id": "body-0097", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Therefore halving $\mathrm{COM}_{\mathrm{prox}}$ should have a similar effect to halving the KL penalty coefficient $\beta$. In other words, we should be able to compensate for halving $\mathrm{COM}_{\mathrm{prox}}$ by doubling the KL penalty coefficient.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Intuitively, the KL penalty acts like a rubber band pulling the policy towards the proximal policy. Halving $\mathrm{COM}_{\mathrm{prox}}$ is analogous to attaching the rubber band to a point half as far away, while doubling the KL penalty coefficient is analogous to doubling the thickness of the rubber band. Doing both simultaneously results in the same overall force.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We tested this hypothesis using a hyperparameter grid search over the EWMA center of mass and the KL penalty coefficient, for PPG-EWMA on StarPilot. We used our smallest batch size, along with our corresponding batch size-invariance adjustments, to allow the greatest scope for reducing $C_{\mathrm{prox}}$ without making the EWMA degenerate into averaging over a single data point.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our results are shown in Figure gridsearchfigure. The diagonal banding clearly demonstrates the expected effect. However, the effect only holds locally: as $\mathrm{COM}_{\mathrm{prox}}$ is continually halved and the KL penalty coefficient is continually doubled, performance gradually degrades.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\centerline{\scalebox{%% Creator: Matplotlib, PGF backend%% To include the figure in your LaTeX document, write%% \input{<filename>.pgf}%% Make sure the required packages are loaded in your preamble%% Figures using additional raster images can only be included by \input if%% they are in the same directory as the main LaTeX file.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For loading figures%% from other directories you can use the `import` package%% and then include the figures with%% \import{<path to file>}{<filename>.pgf}%% Matplotlib used the following preamble \pgfpathrectangle{\pgfpointorigin}{\pgfqpoint{5.317887in}{4.786707in}}% \pgfusepath{use as bounding box, clip}% \definecolor{currentstroke}{rgb}{1.000000,1.000000,1.000000}% \definecolor{currentfill}{rgb}{1.000000,1.000000,1.000000}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}%

<!-- chunk {"id": "body-0103", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=4.165278in,y=0.615411in top]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont 2048}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=2.487501in,y=0.436399in top]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont EWMA center of mass \(\displaystyle

<!-- chunk {"id": "body-0104", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\left(\frac{1}{1-\beta\_{\mathrm{prox}}}-1\right)\)}% \definecolor{currentfill}{rgb}{0.000000,0.000000,0.000000}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{-0.048611in}{0.000000in}}{\pgfqpoint{-0.000000in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=0.433334in, y=0.874130in, left,

<!-- chunk {"id": "body-0105", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pgfpathrectangle{\pgfqpoint{4.685001in}{0.712633in}}{\pgfqpoint{0.188750in}{3.775000in}}% \definecolor{currentfill}{rgb}{1.000000,1.000000,1.000000}% \definecolor{currentstroke}{rgb}{1.000000,1.000000,1.000000}% \pgfusepath{stroke,fill}% \pgftext[left,bottom]{\includegraphics[interpolate=true,width=0.194444in,height=3.777778in]{kl\_penalty\_vs\_ewma-img1.png}}% \definecolor{currentfill}{rgb}{0.000000,0.000000,0.000000}%

<!-- chunk {"id": "body-0106", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{0.000000in}}{\pgfqpoint{0.048611in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=4.970973in, y=0.961194in, left, base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {2.5}\)}%

<!-- chunk {"id": "body-0107", "role": "body", "section": "Paper Body", "weight": 1.0} -->

base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {7.5}\)}% \definecolor{currentfill}{rgb}{0.000000,0.000000,0.000000}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{0.000000in}}{\pgfqpoint{0.048611in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=4.970973in,

<!-- chunk {"id": "body-0108", "role": "body", "section": "Paper Body", "weight": 1.0} -->

y=2.521258in, left, base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {10.0}\)}% \definecolor{currentfill}{rgb}{0.000000,0.000000,0.000000}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{0.000000in}}{\pgfqpoint{0.048611in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}%

<!-- chunk {"id": "body-0109", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pgftext[x=4.970973in, y=3.041279in, left, base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {12.5}\)}% \definecolor{currentfill}{rgb}{0.000000,0.000000,0.000000}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \pgfsys@defobject{currentmarker}{\pgfqpoint{0.000000in}{0.000000in}}{\pgfqpoint{0.048611in}{0.000000in}}{% \pgfusepath{stroke,fill}% \pgfsys@useobject{currentmarker}{}%

<!-- chunk {"id": "body-0110", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pgfsys@useobject{currentmarker}{}% \definecolor{textcolor}{rgb}{0.000000,0.000000,0.000000}% \pgftext[x=4.970973in, y=4.081322in, left, base]{\color{textcolor}\rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle {17.5}\)}% \definecolor{currentstroke}{rgb}{0.000000,0.000000,0.000000}% \caption{Performance on PPG-EWMA on StarPilot after 20 million environment timesteps, using a single parallel copy of the environment along with our batch size-invariance adjustments.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The default hyperparameter settings correspond to square in the bottom right corner. Mean over 2 seeds shown.} We believe that this is because reducing $\mathrm{COM}_{\mathrm{prox}}$ has a second-order effect, which is to increase the variance of $\theta-\theta_{\mathrm{prox}}$. This is both because the EWMA is averaging over a smaller effective sample size, and because $\theta_t-\theta_{t-k}$ has a lower signal-to-noise ratio as $k$ decreases. Therefore if $\mathrm{COM}_{\mathrm{prox}}$ has been halved too many times, we should expect to no longer be able to fully compensate for this by continuing to double the KL penalty coefficient.
