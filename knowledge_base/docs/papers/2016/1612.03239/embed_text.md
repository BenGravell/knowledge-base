## Introduction

We consider the control and stabilization of a system observed over a multiplicative noise channel. Specifically, we analyze the following system, $\mathcal{S}_{a}$, with initial state $X_{0} \sim {\mathcal{N}{}}$: In the preceding formulation, the system state is represented by $X_{n}$ at time $n$, and the control $U_{n}$ can be any function of the current and previous observations $Y_{0}$ to $Y_{n}$. The $Z_{n}$'s are i.i.d. random variables with a known continuous distribution. The realization of the noise $Z_{n}$ is unknown to the controller, much like the fading coefficient (gain) of a channel might be unknown to the transmitter or receiver in non-coherent communication. The constant $a$ captures the growth of the system. The controller's objective is to stabilize the system in the second-moment sense, i.e. to ensure that ${\sup_{n}{{\mathbb{E}}{\lbrack{|X_{n}|}^{2}\rbrack}}} < \infty$. Our objective is to understand the largest growth factor $a$ that can be tolerated for a given distribution on $Z_{n}$. Fig. [1 represents a block diagram for this system.

Figure 1: The state Xn is observed over a multiplicative noise channel Yn = Xn Zn.

Our main theorem provides an impossibility result for stabilizing the system $\mathcal{S}_{a}$.

### Theorem 1.1

Let the $Z_{n}$ be i.i.d. random variables with finite mean and variance and with bounded density ${f_{Z}{(z)}} = e^{- {\phi{(z)}}}$, where $\phi{( \cdot )}$ is a polynomial of even degree with positive leading coefficient. Then, there exists $a \in {\mathbb{R}}$, $a < \infty$ such that $|X_{n}|$ in (1.1) satisfies ${{\mathbb{P}}{({{|X_{n}|} < M})}}\rightarrow 0$ for all $M < \infty$.

Thm. 5.1 generalizes this result to a larger class of distributions for $Z_{n}$. Note that the conditions on $\phi{( \cdot )}$ in Thm. 1.1 are satisfied by $Z_{n} \sim {\mathcal{N}{(1,\sigma^{2})}}$.

We also discuss a few sufficient conditions for second-moment stability of the system in this paper. When $Z_{n}$ has mean $1$ and variance $\sigma^{2}$, we observe that that a system growth of $a^{\ast} = \sqrt{1 + \frac{1}{\sigma^{2}}}$ can be stabilized in the second-moment sense using a simple *linear* strategy (Prop. 3.1. ‣ 3 Linear schemes ‣ When Multiplicative Noise Stymies Control")). Further, we show that the best linear strategy to control the system $\mathcal{S}_{a}$ in (1.1) is memoryless (Thm. 3.2). Our second main result (Thm. 4.1) shows that a *non-linear* controller can improve on the performance of the best linear strategy. We state this here for the case where $Z_{n} \sim {\mathcal{N}{}}$.

### Theorem 1.2

Let $Z_{n} \sim {\mathcal{N}{}}$. Then the system $\mathcal{S}_{a}$ in (1.1) with $a \leq \sqrt{2}$ can be stabilized in the second-moment sense by a linear control strategy. Further, there exists $a > \sqrt{2}$ for which a non-linear controller can stabilize the system in a second-moment sense.

In particular, there exists a non-linear strategy with memory that can stabilize $\mathcal{S}_{a}$ in a second-moment sense with $a = {\sqrt{2} + {1.6 \times 10^{- 3}}}$.

We further believe that non-linear schemes without memory cannot stabilize the system for $a < a^{\ast}$, and some evidence in this direction is provided in Thm. 4.5. Finally, in the case where the $Z_{n}$ have mean zero, a linear strategy cannot stabilize the system in the second-moment sense for any growth factor $a$ (Thm. 3.3), but a non-linear scheme with memory can stabilize it for some value of the growth factor $a$ (Thm. 4.3).

### Model motivation

Multiplicative noise on the observation channel can model the effects of a fast-fading communication channel (rapidly changing channel gain), as well as the impact of sampling and quantization errors. A more detailed discussion of multiplicative noise models is available .

We illustrate below how synchronization or sampling errors can lead to multiplicative noise, following a discussion. Consider the nearly trivial continuous-time system, which is sampled at regular intervals of $t_{0}$. The difference equation corresponding to the state at the $n$th time step is given by ${X_{n + 1} = {e^{at_{0}} \cdot X_{n}}}.$ However, in the presence of synchronization error the $n$th sample, $Y_{n}$, might be collected at time ${nt_{0}} + \Delta$ instead of precisely at $nt_{0}$. Then, where $Z_{n}$ is a continuous random variable, since the jitter $\Delta$ is a continuous random variable.

### Proof approach

We introduce a new converse approach in the proof of Thm. 5.1; instead of focusing on the second-moment, our proof bounds the density of the state and thus shows the instability of any moment of the state. We believe these techniques are a primary contribution of the work.

A key element of the proof is that a "genie" observes the state of the system and provides a quantized version of the logarithm of the state to the controller at each time as extra side-information in addition to the multiplicative noise observation. This side-information bounds the state in intervals of size $2^{- k}$ (with $k$ increasing as time increases). We know from results on non-coherent communication and carry-free models that only the order of magnitude of the message can be recovered from a transmission with multiplicative noise. As a result, this side-information does not effectively provide much extra information, but it allows us to quantify the rate at which the controller may make progress.

### Related work

Our problem is connected to the body of work on data-rate theorems and control with communication constraints as studied . These data-rate theorems tell us that a noiseless observation data rate $R > {\log{|a|}}$ is necessary and sufficient to stabilize a system in the second-moment sense. Our setup considers multiplicative noise on the observation channel instead of observations over a noiseless but rate-limited channel. Paralleling the data-rate theorems, Prop. 3.1. ‣ 3 Linear schemes ‣ When Multiplicative Noise Stymies Control") provides a control strategy that can stabilize the system when ${\frac{1}{2}{\log{({1 + \frac{1}{\sigma^{2}}})}}} > {\log{|a|}}$ for $Z_{n}$ with mean $1$ and variance $\sigma^{2}$.

Our problem is also inspired by the intermittent Kalman filtering problem, as well the problem of control over lossy networks (i.e. estimation and control over Bernoulli multiplicative noise channels). The setup in our paper generalizes those setups to consider a general continuous multiplicative noise on the observation.

The uncertainty threshold principle considers a systems with Gaussian uncertainty on the system growth factor and the control gain, and provides limits for when the system is stabilizable in a second-moment sense. Our work complements this result by considering uncertainty on the observation gain.

A related problem is that of estimating a linear system over multiplicative noise. While early work on this had been limited to exploring linear estimation strategies, some recent work show a general converse result for the estimation problem over multiplicative noise for both linear and non-linear strategies. We note that our problem can also be interpreted as an "active" estimation problem for $X_{0}$, and our impossibility result applies to both linear and non-linear control strategies. However, techniques from the estimation converse result or the data-rate theorems do not work for our setup here. Unlike the estimation problem, we cannot describe the distribution of $X_{n}$ in our problem since the control $U_{n}$ is arbitrary. For the same reason, we also cannot bound the range of $X_{n}$ or the rate across the observation channel to use a data-rate theorem approach.

Some of our results and methods are summarized .

## Problem statement

Consider the system $\mathcal{S}_{a}$ in (1.1). For simplicity, let the initial state $X_{0}$ be distributed as $X_{0} \sim {\mathcal{N}{}}$. Let $Z_{n}$ be i.i.d. random variables with finite second moment and bounded density ${f_{Z}{(z)}} = e^{- {\phi{(z)}}}$. Without loss of generality, we will use the scaling ${{\mathbb{E}}Z_{n}} = 1$ and ${{Var}{(Z_{n})}} = \sigma^{2}$. The notation $Z_{n}$, $f_{Z}$, $\phi$, and $\sigma$ defined here will be used throughout the paper.

We introduce two definitions for stability of the system. The first is the notion of stability that is most commonly studied in control theory, i.e. second-moment stability.

### Definition 2.1

The system $\mathcal{S}_{a}$ in (1.1) is said to be second-moment stabilizable if there exists an adapted control strategy $U_{0},\cdots,U_{n}$ (a control strategy where $U_{k}$ is a function of $Y_{0},\cdots,Y_{k}$ for each $0 \leq k \leq n$) such that

### Definition 2.2

We say the controller can keep the system $\mathcal{S}_{a}$ in (1.1) tight if for every $\epsilon$ and for every $n$ there exists an adapted control strategy $U_{0},\cdots,U_{n}$, and there exist ${M_{\epsilon},N_{\epsilon}} < \infty$ such that

## Linear schemes

This section first provides a simple memoryless linear strategy that can stabilize the system in a second-moment sense in Prop. 3.1. ‣ 3 Linear schemes ‣ When Multiplicative Noise Stymies Control"). We show in Thm. 3.2 that this strategy is optimal among linear strategies. In Thm. 3.3, we highlight the limitations of linear strategies by showing that when ${{\mathbb{E}}Z_{n}} = 0$, linear strategies cannot stabilize the system for any growth factor $a > 1$. Finally, we consider stability in the sense of keeping the system tight and provide a scheme that achieves this in Thm. 3.4.

### Proposition 3.1 (A linear memoryless strategy)

The controller given by $U_{n} = {d^{\ast}Y_{n}}$ where $d^{\ast} = \frac{a}{1 + \sigma^{2}}$, can stabilize the system $\mathcal{S}_{a}$ in (1.1) in a second-moment sense (Def. 2.1) if $a \leq a^{\ast}$, where $a^{\ast} = \sqrt{1 + \frac{1}{\sigma^{2}}}$.

### Proof

The above strategy gives us $X_{n + 1} = {{({a - {d^{\ast}Z_{n}}})}X_{n}}$. Since $Z_{n}$ is independent of $X_{n}$, we can write: Under this control strategy $\sup_{n}{{\mathbb{E}}{\lbrack{|X_{n}|}^{2}\rbrack}}$ is bounded if and only if\$a^{2} \leq {1 + \frac{1}{\sigma^{2}}}$. ∎ Note that the above controller is linear in that $U_{n}$ is a linear function of the $Y_{i}$ and memoryless in that $U_{n}$ depends only on $Y_{n}$ and not $Y_{i}$ for $i < n$. We might expect an improvement in the achievable performance of a linear strategy if we also allow it to use memory, i.e. the past $Y_{n}$'s. However, it turns out that the optimal linear strategy is in fact memoryless.

### Theorem 3.2

The control strategy given by $U_{n} = {d^{\ast}Y_{n}}$ where $d^{\ast} = \frac{a}{1 + \sigma^{2}}$ is the optimal linear strategy to stabilize $\mathcal{S}_{a}$ in a second-moment sense, in particular, for all $a > \sqrt{1 + \frac{1}{\sigma^{2}}}$ the system $\mathcal{S}_{a}$ in (1.1) cannot be second-moment stabilized (Def. 2.1) using a linear strategy.

### Proof

Suppose the system $\mathcal{S}_{a}$ evolves following some linear strategy of the form $U_{n} = {\sum_{i = 1}^{n}{\alpha_{n,i}Y_{i}}}$.

We define a system $\overset{\sim}{\mathcal{S}}$ such that ${\overset{\sim}{X}}_{n}$ that evolves in parallel with $X_{n}$ and tracks the behavior of the strategy $U_{n} = {d^{\ast}Y_{n}}$. Formally, $\overset{\sim}{\mathcal{S}}$ is defined as: where the $Z_{n}$'s are the same as those acting on $X_{n}$. Then, we can write We will show that ${\mathbb{E}}{\lbrack{|{\overset{\sim}{X}}_{n}|}^{2}\rbrack}$ is the minimum achievable second moment at any time $n$. Since ${{\mathbb{E}}{\lbrack{|{\overset{\sim}{X}}_{n}|}^{2}\rbrack}} < \infty$ only when $a \leq \sqrt{1 + \frac{1}{\sigma^{2}}}$, we are done once we show this.

Our approach is to inductively show that ${{\mathbb{E}}{\lbrack{{({X_{n} - {\overset{\sim}{X}}_{n}})}{\overset{\sim}{X}}_{n}}\rbrack}} = 0$ for all $n$ and for any linear control strategy applied to the system $\mathcal{S}$, from which it follows that Base case: $n = 0$ is trivially true, since $X_{0} = {\overset{\sim}{X}}_{0}$. Assume that our hypothesis is true for $n = k$. Now, consider $n = {k + 1}$: We will show that all three expectations in the final expression are zero. The first term in (3.2) is by the induction hypothesis. Because $Z_{k}$ is independent of $X_{k}$ and ${\overset{\sim}{X}}_{k}$, we may compute the above expectation as To handle the second term, for each $1 \leq i \leq k$ we can apply (3.1) to obtain where again we have used the independence of $Z_{i}$ from the other terms in the product, and ${{\mathbb{E}}{\lbrack{Z_{i}{({a - {d^{\ast}Z_{i}}})}}\rbrack}} = 0$ from the definition of $d^{\ast}$. Finally, the last term may be computed in a similar manner as by the definition of $d^{\ast}$.

Equations (3.3), (3.4), and (3.5), establish that all three terms in (3.2) are zero. Hence, ${{\mathbb{E}}{\lbrack{{({X_{n} - {\overset{\sim}{X}}_{n}})}{\overset{\sim}{X}}_{n}}\rbrack}} = 0$ for all $n$, and we are done. ∎ A similar analysis illustrates the limitations of linear strategies when ${{\mathbb{E}}Z_{n}} = 0$, in contrast with nonlinear strategies to be described in the next section.

### Theorem 3.3

Suppose that instead of ${{\mathbb{E}}Z_{n}} = 1$, we have ${{\mathbb{E}}Z_{n}} = 0$. Then, for all $a > 1$, the system $\mathcal{S}_{a}$ in (1.1) cannot be second-moment stabilized using a linear strategy. In other words, linear strategies cannot tolerate any growth in the system.

### Proof

Suppose the system $\mathcal{S}_{a}$ evolves following some linear strategy of the form $U_{n} = {\sum_{i = 1}^{n}{\alpha_{n,i}Y_{i}}}$.

We will show by induction that for each $n$, we may write $X_{n} = {W_{n}X_{0}}$, where $W_{n}$ is a function of $Z_{0},Z_{1},\ldots,Z_{n - 1}$, and ${{\mathbb{E}}W_{n}} = a^{n}$. Clearly, this holds for $n = 0$ with $W_{0} = 1$. For the inductive step, note that so we may take $W_{n + 1} = {{aW_{n}} - {\sum_{i = 1}^{n}{\alpha_{n,i}Z_{i}W_{i}}}}$. Since $Z_{i}$ is independent of $W_{i}$ for each $i$, we have completing the induction. It follows that and so ${\mathbb{E}}\left\lbrack X_{n}^{2} \right\rbrack$ grows without bound when $a > 1$. ∎ Finally, the next theorem considers the weaker sense of stability of keeping the system tight, which is the sense of stability that the impossibility results in Section 5 use.

### Theorem 3.4

Suppose that the density function $f_{Z}$ of $Z_{n}$ is bounded, and consider linear memoryless strategies of the form $U_{n} = {{ad} \cdot Y_{n}}$ for a constant $d > 0$. Let $d^{\star} = {{argmin}_{d}{\mathbb{E}}{\lbrack{\log{|{1 - {d \cdot Z_{n}}}|}}\rbrack}}$ and $a^{\star} = e^{- {{\mathbb{E}}{\lbrack{\log{|{1 - {d^{\star} \cdot Z_{n}}}|}}\rbrack}}}$. If $d = d^{\star}$, then the system $\mathcal{S}_{a}$ in (1.1) can be kept tight (Def. 2.2) provided that ${|a|} < a^{\star}$. Further, no such strategy can keep the system tight if ${|a|} \geq a^{\star}$.

### Proof

Applying the control law $U_{n} = {adY_{n}}$, we calculate that Let $W_{i} = {\log{|{1 - {dZ_{i}}}|}}$, and let $S_{n} = {\sum_{i = 1}^{n}{({W_{i} + {\log{|a|}}})}}$. Taking logarithms gives us almost surely, so as will be seen shortly, it suffices to analyze $S_{n}$.

Take $C$ to be an upper bound on the density of $Z_{i}$. Then, we have so that $W_{i}$ has an exponentially decaying left tail. Similarly, so $W_{i}$ also has an exponentially decaying right tail.

Thus, $W_{i}$ has finite first and second moments. Let $\mu_{d}$ and $\sigma_{d}$ denote the mean and variance of $W_{i}$, respectively. Defining ${\overset{\sim}{S}}_{n} = {\sum_{i = 1}^{n}{({W_{i} - \mu_{d}})}}$, the central limit theorem gives us that If ${|a|} < a^{\star}$ and we take $d = d^{\star}$, then we see that ${\log{|a|}} < {\log a^{\star}} = {- \mu_{d^{\star}}} = {- \mu_{d}}$. Thus, there exists $\epsilon > 0$ such that ${{{\log{|a|}} + \mu_{d}} < {- {2\epsilon}}}.$ Using the union bound we then have: We have that ${{\mathbb{P}}\left({{\log{|X_{0}|}} > {n\epsilon}} \right)}\rightarrow 0$ as $n\rightarrow\infty$, and also by the law of large numbers ${{\mathbb{P}}\left({S_{n} \geq {- {2n\epsilon}}} \right)}\rightarrow 0$ almost surely. Hence, ${{\mathbb{P}}\left({{\log{|X_{n}|}} < {- {n\epsilon}}} \right)}\rightarrow 1$ and the system is kept tight.

On the other hand, suppose that ${|a|} \geq a^{\star}$. Then, we have ${\log{|a|}} \geq {\log a^{\star}} = {- \mu_{d^{\star}}} \geq {- \mu_{d}}$, so $S_{n} \geq {\overset{\sim}{S}}_{n}$. Consider $\delta > 0$. For $n$ large enough we have that: where we used the union bound and the fact that $S_{n} \geq {\overset{\sim}{S}}_{n}$ to get the two inequalities. Now, ${{\mathbb{P}}\left({{\log{|X_{0}|}} \leq {- {\delta\sqrt{n}}}} \right)}\rightarrow 0$ as $n\rightarrow\infty$ and ${{\mathbb{P}}\left({{\overset{\sim}{S}}_{n} \leq {2\delta\sqrt{n}}} \right)}\rightarrow{\Phi\left(\frac{2\delta}{\sigma_{d}} \right)}$, by (3.6). Hence, which gives that Thus, in this case the system is not kept tight.

## Non-linear schemes

In the previous section, we focused on linear strategies, where $U_{n}$ is taken to be a linear combination of $Y_{i}$ for $0 \leq i \leq n$. We now consider whether more general strategies can do better. Thm. 4.1 shows that when $Z_{n}$ is Gaussian, a perturbation of the linear strategy indeed does better in the second-moment sense. (The same result should hold for rather general $Z_{n}$; see Remark 4.1.) In the setting where ${{\mathbb{E}}Z_{n}} = 0$, Thm. 4.3 exhibits a nonlinear strategy that achieves a non-trivial growth factor $a > 1$. This contrasts with Thm. 3.3, which showed that linear strategies cannot achieve any gain in this setting. In both Thm. 4.1 and Thm. 4.3, improvement is achieved by taking into account information from the previous round while choosing the control.

On the other hand, Thm. 4.5 shows that when $a > a^{\ast} = \sqrt{1 + \frac{1}{\sigma^{2}}}$, for any memoryless strategy (in the sense that $U_{n}$ is a function of only $Y_{n}$), we cannot guarantee for all distributions of $X_{n}$ that ${{\mathbb{E}}\left\lbrack X_{n + 1}^{2} \right\rbrack} \leq {{\mathbb{E}}\left\lbrack X_{n}^{2} \right\rbrack}$. This suggests that in the memoryless setting, the linear strategy from the previous section may be optimal. However, it does not rule out the possibility for an increase in second moment after one round to be compensated by a larger decrease later.

### Theorem 4.1

Let $a^{\ast} = \sqrt{1 + \frac{1}{\sigma^{2}}}$ be as in Prop. 3.1. ‣ 3 Linear schemes ‣ When Multiplicative Noise Stymies Control"). Suppose that our multiplicative noise $Z_{n}$ has a Gaussian law $Z_{n} \sim {\mathcal{N}{(1,\sigma^{2})}}$. Then, there exists $a > a^{\ast}$ for which a (non-linear) controller can stabilize the system in a second-moment sense.

We first establish an elementary inequality for Gaussian variables. In what follows, we define the signum function ${sgn}{(x)}$ to be $1$ if $x \geq 0$ and $- 1$ otherwise.

### Lemma 4.2

Let $Z \sim {\mathcal{N}{(1,\sigma^{2})}}$, with $\sigma > 0$. We have

### Proof

It is convenient to write $Z = {1 - {\sigma\overset{\sim}{Z}}}$, where $\overset{\sim}{Z} \sim {\mathcal{N}{}}$. Let $s = \frac{1}{\sigma}$, and let $\gamma$ denote the standard Gaussian density. Note that for all $x$. Hence, It can be checked by elementary calculations that for any $s > 0$, (4.1) is always strictly greater than (4.2). Indeed, for $s < \sqrt{2}$ use ${e^{- \frac{s^{2}}{2}} < {{1 - \frac{s^{2}}{2}} + \frac{s^{4}}{8}} < {1 - \frac{s^{2}}{6}}},$ and for $s > \sqrt{2}$ note that $se^{- \frac{s^{2}}{2}}$ is decaying. Thus, Let us rewrite the above equation in terms of $Z$ and $\sigma$, noting that\$\mathbb{1}_{\overset{\sim}{Z} \geq s} = {\frac{1}{2}{({1 - {\text{sgn}{(Z)}}})}}$. We obtain Finally, multiplying both sides by $\frac{1 + \sigma^{2}}{\sigma^{2}}$ yields

### Proof of Thm. 4.1

To show second-moment stability, it suffices to exhibit controls $U_{n}$ and $U_{n + 1}$ which ensure that ${{\mathbb{E}}X_{n + 2}^{2}} \leq {{\mathbb{E}}X_{n}^{2}}$ for all possible distributions of $X_{n}$. For a positive $\epsilon$ to be specified later, choose For our controls, we take Note that the expression for $U_{n}$ and the first term in the expression for $U_{n + 1}$ are the same as in the linear strategy from Prop. 3.1. ‣ 3 Linear schemes ‣ When Multiplicative Noise Stymies Control"). However, here we have added a small perturbation to $U_{n + 1}$. For convenience, define the function ${g{(x)}} = {1 - \frac{x}{1 + \sigma^{2}}}$. Then, We will compute the second moment of (4.3). Let where the inequality in the last line follows from Lemma 4.2 and the fact that ${g{(Z_{n})}^{2}} \cdot \left| \frac{Z_{n}}{g{(Z_{n})}} \right|$ is almost surely positive.

Recall that the $Z_{n}$ and $Z_{n + 1}$ are both independent of $X_{n}$, so taking second-moments in (4.3), we have Since ${{\mathbb{E}}AB} > 0$, when $\epsilon$ is a sufficiently small positive number, this gives ${{\mathbb{E}}X_{n + 2}^{2}} \leq {{\mathbb{E}}X_{n}^{2}}$, showing second-moment stability. ∎

### Remark 4.1

We actually suspect that Thm. 4.1 applies to all continuous distributions of $Z_{n}$. Indeed, the above analysis can be carried out for a more general class of control strategies. Consider instead where $h$ is any function (above, we used ${h{(x)}} = {|x|}$). Then, we would carry out the same analysis except with The crucial properties we needed were that ${{\mathbb{E}}B^{2}} < \infty$ and ${{\mathbb{E}}AB} \neq 0$. Thus, for all distributions of $Z_{n}$, as long as there exists some function $h$ verifying those two properties, the conclusion of Thm. 4.1 applies.

The next theorem shows that a perturbation can also improve upon linear strategies when ${{\mathbb{E}}Z_{n}} = 0$.

### Theorem 4.3

Suppose that instead of ${{\mathbb{E}}Z_{n}} = 1$, we have ${{\mathbb{E}}Z_{n}} = 0$. Then, as long as $Z_{n}$ has finite second moment, there exists $a > 1$ for which a (non-linear) controller can stabilize the system in a second-moment sense.

We first prove a technical lemma.

### Lemma 4.4

Let $Z$ be a random variable with ${{\mathbb{E}}Z} = 0$ and finite first moment. Then, for all sufficiently small $\epsilon > 0$, we have

### Proof

For $0 \leq t \leq \frac{1}{2}$, define the function Note that for each $x \neq 0$ and each $t$, we have Thus, letting ${F{(t)}} = {{\mathbb{E}}f{(Z,t)}}$, the dominated convergence theorem implies Consequently, for all sufficiently small $t$, we have ${F{(t)}} < 0$, as desired. ∎

### Proof of Thm. 4.3

We take an approach similar to the proof of Thm. 4.1. Again, it suffices to exhibit controls $U_{n}$ and $U_{n + 1}$ which ensure that ${{\mathbb{E}}\left\lbrack X_{n + 2}^{2} \right\rbrack} \leq {{\mathbb{E}}\left\lbrack X_{n}^{2} \right\rbrack}$ for all possible distributions of $X_{n}$. By Lemma 4.4, take a small enough $\epsilon_{0} > 0$ so that Let $\epsilon > 0$ be another small number to be specified later, and take $a = {1 + \epsilon^{2}}$. For our controls, we take For convenience, let $A = {{\epsilon_{0}^{- 1} \cdot {|Z_{n + 1}|} \cdot Z_{n}}\left| {\frac{\epsilon_{0}}{Z_{n}} - 1} \right|}$, and note that ${{\mathbb{E}}A^{2}} < \infty$ since $Z_{n}$ and $Z_{n + 1}$ have finite second moments. Substituting this definition for $A$, we calculate By (4.4), we have that ${\mathbb{E}}A$ is strictly negative. Thus, for small enough positive $\epsilon$, we obtain ${{\mathbb{E}}\left\lbrack X_{n + 2}^{2} \right\rbrack} \leq {{\mathbb{E}}\left\lbrack X_{n}^{2} \right\rbrack}$, as desired. ∎ The next theorem pertains to schemes of the form $U_{n} = {h{(Y_{n})}}$, where $h:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is *any* fixed function.

### Theorem 4.5

Consider any $a > a^{\ast} = \sqrt{1 + \frac{1}{\sigma^{2}}}$ and any measurable function $h:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$. Then, there exists a random variable $X$ with finite second moment for which In particular, we cannot guarantee ${{\mathbb{E}}X_{n + 1}^{2}} \leq {{\mathbb{E}}X_{n}^{2}}$ for the scheme $U_{n} = {h{(Y_{n})}}$.

### Proof

Let $M$ be a large parameter to be specified later. Consider the probability density We will take $X$ to have density $\rho$, and for appropriate $M$, we will find that Recall our notation ${f_{Z}{(x)}} = e^{- {\phi{(x)}}}$ for the density of $Z_{n}$. To aid in our calculations, for each integer $k \geq 0$ and real number $y \neq 0$, we consider the quantity where we have made the substitution $x = {y/s}$. Let $\epsilon > 0$ be a small parameter. Consider a fixed $t$ with $\epsilon \leq t \leq {1 - \epsilon}$, and set $y = {\pm M^{t}}$. We find that uniformly over $\epsilon \leq t \leq {1 - \epsilon}$, where we have taken care to ensure that the above holds for both possible signs of $y$. Let $\delta > 0$ also be a small parameter. We now choose $M$ to be sufficiently large so that and also for all $y$ with $M^{\epsilon} \leq {|y|} \leq M^{1 - \epsilon}$ (in light of (4.5)), Note that the integrand in the last expression is a quadratic function in $h{(y)}$ whose minimum possible value is ${\alpha_{2}{(y)}} - \frac{\alpha_{1}{(y)}^{2}}{\alpha_{0}{(y)}}$, and note also that this quantity is non-negative since ${\alpha_{2}{(y)}\alpha_{0}{(y)}} \geq {\alpha_{1}{(y)}^{2}}$ by the Cauchy-Schwarz inequality. Thus, where we have plugged in the bound from (4.6). Consequently, Since $a > \sqrt{1 + \frac{1}{\sigma^{2}}}$, the right hand side is strictly greater than $1$ when $\epsilon$ and $\delta$ are sufficiently small. This completes the proof. ∎

## An impossibility result

### Theorem 5.1

For the system $\mathcal{S}_{a}$, suppose that $\phi$ is differentiable and satisfies ${|{{z \cdot \phi'}{(z)}}|} \leq {C_{1} + {{C_{2} \cdot \phi}{(z)}}}$ for all $z$, and also $e^{- {\phi{(z)}}} \leq {|z|}^{{- 1} - \delta}$ for some $\delta > 0$. We additionally assume $\phi{( \cdot )}$ satisfies a doubling condition on $\phi'{( \cdot )}$ such that if ${\frac{z_{1}}{2} \leq z_{2} \leq {2z_{1}}},$ then ${\phi'{(z_{2})}} \leq {{C_{3} \cdot \phi'}{(z_{1})}}$.

Then, there exists $a \in {\mathbb{R}}$, $a < \infty$ such that ${{\mathbb{P}}{({{|X_{n}|} < M})}}\rightarrow 0$ for all $M < \infty$.

Note that the conditions on $\phi{( \cdot )}$ above imply the conditions in Thm. 1.1.

We rewrite the system $\mathcal{S}_{a}$ from (1.1) here, with state denoted as $X_{a,n}$, to emphasize the dependence on $a$: Now define $U_{n}:={a^{- n}U_{a,n}}$, and consider the system $\mathcal{S}$, which is the system $\mathcal{S}_{a}$ scaled by $a$: The $Z_{n}$'s and the initial state $X_{0} = X_{a,0}$ are identical in both systems. Then, the scaled system satisfies $X_{n} = {a^{- n}X_{a,n}}$. Thus we have that: As a result it suffices bound the probability that the state of the of system $\mathcal{S}$, i.e. $|X_{n}|$, is contained in intervals that are shrinking by a factor of $a$ at each time step. The rest of this section uses the notation $X_{n}$ to refer to the state of the the system $\mathcal{S}$ and $X_{a.n}$ to refer the the state of the system $\mathcal{S}_{a}$.

### Definitions

Let $S_{n}:={\sum_{i = 0}^{n - 1}U_{i}}$. Hence, $X_{n} = {X_{0} - S_{n}}$.

The goal of the controller is to have $S_{n}$ be as close to $X_{0}$ as possible. We will track the progress of the controller through intervals $I_{n}$ that contain $X_{0}$ and are decreasing in length.

Let ${d{(I_{n},S)}}:={\inf_{x \in I_{n}}{|{S - x}|}}$ denote the distance of a point $S$ from the interval $I_{n}$.

### Definition 5.1

For all $n \geq 0$ and for $k \in {\mathbb{Z}}$, there exists a unique integer $h{(k)}$ such that $\left. {X_{0} \in \lbrack}\frac{h{(k)}}{2^{k}},\frac{{h{(k)}} + 1}{2^{k}} \right)$. Let $\left. {J{(k)}:=\lbrack}\frac{h{(k)}}{2^{k}},\frac{{h{(k)}} + 1}{2^{k}} \right)$. We now inductively define Write $H_{n}:={h{(K_{n})}}$ and $\left. {I_{n}:=J{(K_{n})} = \lbrack}\frac{H_{n}}{2^{K_{n}}},\frac{H_{n} + 1}{2^{K_{n}}} \right)$.

Let $Y_{0}^{n}$ indicate the observations $Y_{0}$ to $Y_{n}$, and let $\mathcal{F}_{n}:={\{ Y_{0}^{n},K_{0}^{n},H_{0}^{n}\}}$, which is the total information available to the controller at time $n$. Let $f_{X_{n}}{(\left. x \middle| \mathcal{F}_{n} \right.)}$ be the conditional density of $X_{n}$ given $\mathcal{F}_{n}$.

Figure 2: A caricature illustrating the intervals In and In − Sn.

### Relationships between $I_{n}$, $K_{n}$, $S_{n}$, and $X_{n}$

We state and prove two lemmas that will be used in the main proof. The first lemma uses $K_{n}$ to bound how fast $S_{n}$ approaches $X_{0}$.

### Lemma 5.2

### Proof

From the definition of $I_{n}$, we know that ${d{(I_{n},S_{n})}} \geq 2^{- K_{n}}$. This gives $2^{- K_{n}} \leq {|{X_{0} - S_{n}}|}$, since $X_{0} \in I_{n}$.

To show the second half of the inequality, suppose that ${|{X_{0} - S_{n}}|} > 2^{2 - K_{n}}$. Then, Hence, there exists a larger interval $J{({K_{n} - 1})}$ that contains $X_{0}$ such that where $J{({K_{n} - 1})}$ is an interval of length $2^{1 - K_{n}} > 2^{- K_{n}}$. Since we also assumed that $K_{n} > {K_{n - 1} + 1}$, this contradicts the assumption that $K_{n}$ was the minimal $k > K_{n - 1}$ such that ${d{({J{(k)}},S_{n})}} \geq 2^{- k}$. ∎ The second lemma bounds the ratio between two points in the interval of interest.

### Lemma 5.3

For $t \in {I_{n} - S_{n}}$ we have that $\frac{1}{2} \leq \frac{X_{n}}{t} \leq 2$.

### Proof

We have from Lemma 5.2 that $2^{- K_{n}} \leq {|X_{n}|}$. The lemma follows since the length of the interval $I_{n} - S_{n}$ is $2^{- K_{n}}$. ∎

### Preliminary estimates of the $Z_{i}$

We also require some basic estimates for the $Z_{i}$, which we record here. Recall that we assumed the existence of a number $\delta > 0$ such that $e^{- {\phi{(z)}}} \leq {|z|}^{{- 1} - \delta}$.

### Lemma 5.4

Let $\delta' = {\delta/{({1 + \delta})}}$. For each $i$ and any $t \geq 0$, we have

### Proof

Let $s = e^{t/{({1 + \delta})}}$, so that $s^{{- 1} - \delta} = e^{- t}$. We have

### Lemma 5.5

For each $i$, the random variable $\phi{(Z_{i})}$ has finite moments of all orders.

### Proof

The condition ${|{Z_{i}\phi'{(Z_{i})}}|} \leq {C_{1} + {C_{2}\phi{(Z_{i})}}}$ implies ${\phi{(Z_{i})}} \geq {- \frac{C_{1}}{C_{2}}}$. According to Lemma 5.4, we also know that $\phi{(Z_{i})}$ has exponentially decaying upper tails. Thus, $\phi{(Z_{i})}$ has finite moments of all orders. ∎

### Proof of the main result

The key element of the proof is to provide the interval $I_{n}$ to the controller at time $n$ as side-information in addition to $Y_{n}$. Our strategy is to first bound the density $f_{X_{n}}{(\left. x \middle| \mathcal{F}_{n} \right.)}$ by comparing the change in density from time $n$ to $n + 1$. This bound helps us generate bounds for the probabilities of three events that cover the event of interest $\{{{|X_{n}|} < {a^{- n}M}}\}$. We will show that for large enough $a$ the probabilities of all three of these events go to $0$ as $n\rightarrow\infty$.

### Proof of Thm. 5.1

Since $X_{0} \in I_{n}$, the controller knows that $X_{n} \in {I_{n} - S_{n}}$, where $I_{n} - S_{n}$ represents the interval $I_{n}$ shifted by $S_{n}$. We can calculate the ratio of the densities at ${x,w} \in {I_{n} - S_{n}}$ as: Since $K_{n}$ and $H_{n}$ are defined by $I_{n}$, the conditional distributions of $K_{n}$ and $H_{n}$ given $X_{n} = x$ and $X_{n} = w$ are equal for ${x,w} \in {I_{n} - S_{n}}$. So these terms cancel when we consider a ratio, giving (5.3).

Taking logarithms and using the triangle inequality gives the following recursive lemma.

### Lemma 5.6

The proof is deferred to Section 6 to improve readability. This lemma helps us establish the recursive step, since the control law gives us that: since $U_{n - 1}$ is $\mathcal{F}_{n - 1}$ measurable. Substituting this into (5.4) and unfolding recursively gives: The inequality (5.5) separates the effect of the uncertainty due to $X_{0}$ and the subsequent uncertainty due to the observations and control.

Let $\eta_{n} = {\max_{{x,w} \in {I_{n} - S_{n}}}\left| {\log\frac{f_{X_{0}}{({x + S_{n}})}}{f_{X_{0}}{({w + S_{n}})}}} \right|}$. Since $I_{n}$ is an interval of size at most $2^{- n}$ which contains $X_{0}$, we get that We will need the following lemma to bound the crucial quantity $\Psi_{n}$.

### Lemma 5.7

For a sufficiently large constant $T$, the expectation ${\mathbb{E}}{\lbrack e^{\Psi_{n}2^{- T}}\rbrack}$ is uniformly bounded for all $n$.

The proof of this lemma is deferred to Section 6. Henceforth, let $T$ denote a constant that is sufficiently large for Lemma 5.7 to apply.

Finally, we are in a position to get a bound on $f_{X_{n}}{({x \mid \mathcal{F}_{n}})}$: Now, we integrate (5.8) over an interval of length $\gamma = 2^{({{- K_{n}} - T})}$ with $x$ at one end point. So ${|{x - w}|} \leq 2^{({{- K_{n}} - T})}$. Such an interval can be fit into $I_{n}$ to the left or right of any $x$ depending on where $x$ is in the interval. Assuming without loss of generality that $x$ is the left endpoint of the integration interval we compute that We bound $|{x - w}|$ on the RHS by $\gamma = 2^{({{- K_{n}} - T})}$ to get The last step follows since the density integrates out to $1$. Hence, This gives us a bound on the density of $X_{n}$ in terms of $K_{n}$.

It now remains to bound the rate at which the $K_{n}$ are growing. The following lemma shows that the $K_{n}$ grow essentially at most linearly.

### Lemma 5.8

There exists a constant $C$ such that

### Proof

By construction, $K_{n + 1} \geq {K_{n} + 1}$. In the case where $K_{n + 1} > {K_{n} + 1}$, we can apply Lemma 5.2 and get that for $\ell \geq 2$ This is because the control $U_{n}$ must have been very close to $X_{n}$ for $K_{n + 1}$ to be much larger than $K_{n}$. Then we calculate this probability by integrating out the density as: Combined with (5.9), this gives us that Write $D_{n} = {K_{n + 1} - K_{n}}$, and let It is clear that $({\overset{\sim}{K}}_{n})$ is a martingale with respect to $\mathcal{F}_{n}$. In addition, (5.10) yields that the conditional distribution of $D_{n}$ given $\mathcal{F}_{n}$ is stochastically dominated by the distribution of where $G_{n}$ is an independent geometric variable with mean 2.

By (5.6) and Lemma 5.7, both $\eta_{n}$ and $\Psi_{n}2^{- T}$ have bounded second moments, and so for some constant $\overset{\sim}{C}$, we have Summing over $i$, this implies that ${{\mathbb{E}}{\lbrack{\overset{\sim}{K}}_{n}^{2}\rbrack}} \leq {\overset{\sim}{C}n}$, and so We now turn our attention to terms of the form ${\mathbb{E}}{\lbrack{D_{i} \mid \mathcal{F}_{i}}\rbrack}$. Using (5.11) again, we get that Observe that from the definition of $\Psi_{i}$ given in (5.7), we have where in the last step we have used the fact that the $K_{i}$ increase by at least $1$ in each step, so that ${K_{i} - K_{j}} \geq {i - j}$. Then, applying the bound ${|{{Z_{j} \cdot \phi'}{(Z_{j})}}|} \leq {C_{1} + {C_{2}\phi{(Z_{j})}}}$ to (5.4) yields Summing (5.13) over $i$ and applying the above bound gives for a constant $C_{D,1}$. Now, recalling (5.6), we see that the quantity has mean and variance bounded by a constant, which we call $C_{\eta}$. In addition, by Lemma 5.5, there exists another constant $C_{\phi}$ which upper bounds the mean and variance of $\phi{(Z_{i})}$. We conclude that where $C_{D,2} = {{C_{D,1}C_{\phi}} + 1}$. Finally, setting $C = {C_{D,2} + 1}$, we have where the last expression goes to $0$ as $n\rightarrow\infty$ by (5.12) and (5.15). ∎ This bound on the growth of the $K_{n}$ variables allows us to complete the proof of Thm. 5.1.

Let $G_{n}$ denote the event that ${K_{n} - K_{0}} > {Cn}$, and $G_{n}^{c}$ its complement. Then we can cover the event of interest by three events, and get that We evaluate the three terms one by one. For the first term in (5.16), we have ${{\mathbb{P}}{(G_{n})}} = {{\mathbb{P}}{({{K_{n} - K_{0}} > {Cn}})}}\rightarrow 0$ as $n\rightarrow\infty$ from Lemma 5.8.

The second term, ${\mathbb{P}}{({K_{0} > n})}$, captures the case where the initial state $X_{0}$ might be very close to zero. However, eventually this advantage dies out for large enough $n$, since ${{\mathbb{P}}{({X_{0} < 2^{- n}})}}\rightarrow 0$ as $n\rightarrow\infty$.

The last term in (5.16) remains. By the law of iterated expectation: We focus on the term conditioned on $\mathcal{F}_{n}$: Now, we can apply (5.9) to get Then we can bound (5.17) as since $K_{n} \leq {{Cn} + K_{0}}$ and $K_{0} \leq n$ implies $K_{n} \leq {{({C + 1})}n}$. Taking expectations on both sides we get: By Lemma 5.7 and (5.6), the above expression (5.18) tends to 0 for $a > 2^{C + 1}$.

Thus, all three probabilities in (5.16) converge to $0$ as $n\rightarrow\infty$. Hence, if $a > 2^{C + 1}$ then ${{\mathbb{P}}{({{|X_{n}|} < {a^{- n}M}})}}\rightarrow 0$ for all $M$. ∎

## Bounding the likelihood ratio

Here we provide the proofs of two lemmas used to bound the term $\left| \log\frac{f_{X_{n}}{({x \mid \mathcal{F}_{n}})}}{f_{X_{n}}{({w \mid \mathcal{F}_{n}})}} \right|$.

### Proof of Lemma 5.6

We take logarithms on both sides of (5.3) and apply the triangle inequality to get The form of the density of $Z$ gives, We can use the derivatives of the functions to bound the two function differences above. Since ${\frac{d}{dx}\phi\left(\frac{Y_{n}}{x} \right)} = {\frac{Y_{n}}{x^{2}}\phi'\left(\frac{Y_{n}}{x} \right)}$, we bound (6.2) as below. Since $X_{n} \in {I_{n} - S_{n}}$, the maximizations are over $t \in {I_{n} - S_{n}}$.

For all $t \in {I_{n} - S_{n}}$, by Lemma 5.3, we have $\frac{1}{2} \leq \frac{X_{n}}{t} \leq 2$. Using this and $Y_{n} = {Z_{n}X_{n}}$, we get the following bound on (6.3): (6.4) follows from the doubling property of $\phi'{(\cdot)}$, since $\frac{Z_{n}X_{n}}{t}$ and $Z_{n}$ are within a factor of two from each other by Lemma 5.3. Now note that Applying this to the bound from (6.4) we get: This now gives a bound for (6.1) as below:

### Proof of Lemma 5.7

Recall that our goal is to estimate the quantity Since the $K_{i}$'s must increase by at least one in each step, we have ${K_{n} - K_{i}} \geq {n - i}$, and so where we have also used the assumption ${|{{z \cdot \phi'}{(z)}}|} \leq {C_{1} + {C_{2}\phi{(z)}}}$.

Let $\delta' = {\delta/{({1 + \delta})}}$ as in Lemma 5.4. Consider any $\theta < {\delta'/2}$. Applying Lemma 5.4, we have for each $i$ that Now, choose $T$ large enough so that ${2^{1 - T}C_{2}C_{3}} < {\delta'/2}$. We can then apply (6.7) to each term in (6.6) by taking $\theta = {{2^{- T}C_{3}C_{2}} \cdot 2^{{1 + i} - n}}$. This yields for a constant $C$ not depending on $n$. We then have which is a (finite) constant not depending on $n$. ∎

## Conclusion

This paper provides a first proof-of-concept converse for a control system observed over continuous multiplicative noise. However, there is an exponential gap between the scaling behavior of the achievable strategy and the converse.

We note that if the system $\mathcal{S}_{a}$ in (1.1) is restricted to using linear control strategies, then its performance limit is the same as that of a system with the same multiplicative actuation noise (i.e. the control $U_{n}$ is multiplied by a random scaling factor) but perfect observations (as in ). Previous work has shown how to compute the control capacity for systems with multiplicative noise on the actuation channel. However, computing the control capacity of the system $\mathcal{S}_{a}$, i.e. computing tight upper and lower bounds on the system growth factor $a$, remains open.
