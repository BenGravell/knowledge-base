<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

When Multiplicative Noise Stymies Control

Topics include Control, Multiplicative noise, Linear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the stabilization of an unstable discrete-time linear system that is observed over a channel corrupted by continuous multiplicative noise. Our main result shows that if the system growth is large enough, then the system cannot be stabilized in a second-moment sense. This is done by showing that the probability that the state magnitude remains bounded must go to zero with time. Our proof technique recursively bounds the conditional density of the system state (instead of focusing on the second moment) to bound the progress the controller can make. This sidesteps the difficulty encountered in using the standard data-rate theorem style approach; that approach does not work because the mutual information per round between the system state and the observation is potentially unbounded. It was known that a system with multiplicative observation noise can be stabilized using a simple memoryless linear strategy if the system growth is suitably bounded. In this paper, we show that while memory cannot improve the performance of a linear scheme, a simple non-linear scheme that uses one-step memory can do better than the best linear scheme.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the control and stabilization of a system observed over a multiplicative noise channel.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the preceding formulation, the system state is represented by $X_{n}$ at time $n$, and the control $U_{n}$ can be any function of the current and previous observations $Y_{0}$ to $Y_{n}$. The $Z_{n}$'s are i.i.d. random variables with a known continuous distribution. The realization of the noise $Z_{n}$ is unknown to the controller, much like the fading coefficient (gain) of a channel might be unknown to the transmitter or receiver in non-coherent communication. The constant $a$ captures the growth of the system. The controller's objective is to stabilize the system in the second-moment sense, i.e. to ensure that ${\sup_{n}{{\mathbb{E}}{\lbrack{|X_{n}|}^{2}\rbrack}}} < \infty$. Our objective is to understand the largest growth factor $a$ that can be tolerated for a given distribution on $Z_{n}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. [1 represents a block diagram for this system.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main theorem provides an impossibility result for stabilizing the system $\mathcal{S}_{a}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Model motivation", "weight": 1.0} -->

Multiplicative noise on the observation channel can model the effects of a fast-fading communication channel (rapidly changing channel gain), as well as the impact of sampling and quantization errors. A more detailed discussion of multiplicative noise models is available.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Model motivation", "weight": 1.0} -->

We illustrate below how synchronization or sampling errors can lead to multiplicative noise, following a discussion. Consider the nearly trivial continuous-time system,

<!-- chunk {"id": "body-0009", "role": "body", "section": "Model motivation", "weight": 1.0} -->

which is sampled at regular intervals of $t_{0}$. The difference equation corresponding to the state at the $n$th time step is given by ${X_{n + 1} = {e^{at_{0}} \cdot X_{n}}}.$ However, in the presence of synchronization error the $n$th sample, $Y_{n}$, might be collected at time ${nt_{0}} + \Delta$ instead of precisely at $nt_{0}$. Then,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Model motivation", "weight": 1.0} -->

where $Z_{n}$ is a continuous random variable, since the jitter $\Delta$ is a continuous random variable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Consider the system $\mathcal{S}_{a}$ in (1.1). For simplicity, let the initial state $X_{0}$ be distributed as $X_{0} \sim {\mathcal{N}{}}$. Let $Z_{n}$ be i.i.d. random variables with finite second moment and bounded density ${f_{Z}{(z)}} = e^{- {\phi{(z)}}}$. Without loss of generality, we will use the scaling ${{\mathbb{E}}Z_{n}} = 1$ and ${{Var}{(Z_{n})}} = \sigma^{2}$. The notation $Z_{n}$, $f_{Z}$, $\phi$, and $\sigma$ defined here will be used throughout the paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem statement", "weight": 1.0} -->

We introduce two definitions for stability of the system. The first is the notion of stability that is most commonly studied in control theory, i.e. second-moment stability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear schemes", "weight": 1.0} -->

This section first provides a simple memoryless linear strategy that can stabilize the system in a second-moment sense in Prop. 3.1. ‣ 3 Linear schemes ‣ When Multiplicative Noise Stymies Control"). We show in Thm. 3.2 that this strategy is optimal among linear strategies. In Thm. 3.3, we highlight the limitations of linear strategies by showing that when ${{\mathbb{E}}Z_{n}} = 0$, linear strategies cannot stabilize the system for any growth factor $a > 1$. Finally, we consider stability in the sense of keeping the system tight and provide a scheme that achieves this in Thm. 3.4.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Non-linear schemes", "weight": 1.0} -->

In the previous section, we focused on linear strategies, where $U_{n}$ is taken to be a linear combination of $Y_{i}$ for $0 \leq i \leq n$. We now consider whether more general strategies can do better. Thm. 4.1 shows that when $Z_{n}$ is Gaussian, a perturbation of the linear strategy indeed does better in the second-moment sense. (The same result should hold for rather general $Z_{n}$; see Remark 4.1.) In the setting where ${{\mathbb{E}}Z_{n}} = 0$, Thm. 4.3 exhibits a nonlinear strategy that achieves a non-trivial growth factor $a > 1$. This contrasts with Thm. 3.3, which showed that linear strategies cannot achieve any gain in this setting. In both Thm. 4.1 and Thm. 4.3, improvement is achieved by taking into account information from the previous round while choosing the control.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Non-linear schemes", "weight": 1.0} -->

On the other hand, Thm. 4.5 shows that when $a > a^{\ast} = \sqrt{1 + \frac{1}{\sigma^{2}}}$, for any memoryless strategy (in the sense that $U_{n}$ is a function of only $Y_{n}$), we cannot guarantee for all distributions of $X_{n}$ that ${{\mathbb{E}}\left\lbrack X_{n + 1}^{2} \right\rbrack} \leq {{\mathbb{E}}\left\lbrack X_{n}^{2} \right\rbrack}$. This suggests that in the memoryless setting, the linear strategy from the previous section may be optimal. However, it does not rule out the possibility for an increase in second moment after one round to be compensated by a larger decrease later.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

We actually suspect that Thm. 4.1 applies to all continuous distributions of $Z_{n}$. Indeed, the above analysis can be carried out for a more general class of control strategies. Consider instead

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

where $h$ is any function (above, we used ${h{(x)}} = {|x|}$). Then, we would carry out the same analysis except with

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

The crucial properties we needed were that ${{\mathbb{E}}B^{2}} < \infty$ and ${{\mathbb{E}}AB} \neq 0$. Thus, for all distributions of $Z_{n}$, as long as there exists some function $h$ verifying those two properties, the conclusion of Thm. 4.1 applies.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

The next theorem shows that a perturbation can also improve upon linear strategies when ${{\mathbb{E}}Z_{n}} = 0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Definitions", "weight": 1.0} -->

The goal of the controller is to have $S_{n}$ be as close to $X_{0}$ as possible. We will track the progress of the controller through intervals $I_{n}$ that contain $X_{0}$ and are decreasing in length.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Relationships between $I_{n}$, $K_{n}$, $S_{n}$, and $X_{n}$", "weight": 1.0} -->

We state and prove two lemmas that will be used in the main proof. The first lemma uses $K_{n}$ to bound how fast $S_{n}$ approaches $X_{0}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Preliminary estimates of the $Z_{i}$", "weight": 1.0} -->

We also require some basic estimates for the $Z_{i}$, which we record here. Recall that we assumed the existence of a number $\delta > 0$ such that $e^{- {\phi{(z)}}} \leq {|z|}^{{- 1} - \delta}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper provides a first proof-of-concept converse for a control system observed over continuous multiplicative noise. However, there is an exponential gap between the scaling behavior of the achievable strategy and the converse.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We note that if the system $\mathcal{S}_{a}$ in (1.1) is restricted to using linear control strategies, then its performance limit is the same as that of a system with the same multiplicative actuation noise (i.e. the control $U_{n}$ is multiplied by a random scaling factor) but perfect observations (as in ). Previous work has shown how to compute the control capacity for systems with multiplicative noise on the actuation channel. However, computing the control capacity of the system $\mathcal{S}_{a}$, i.e. computing tight upper and lower bounds on the system growth factor $a$, remains open.
