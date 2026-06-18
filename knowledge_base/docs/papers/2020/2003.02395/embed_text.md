## Introduction

First-order methods with adaptive step sizes have proved useful in many fields of machine learning, be it for sparse optimization, tensor factorization or deep learning. Duchi et al. introduced Adagrad, which rescales each coordinate by a sum of squared past gradient values. While Adagrad proved effective for sparse optimization, experiments showed that it under-performed when applied to deep learning. RMSProp proposed an exponential moving average instead of a cumulative sum to solve this. Kingma & Ba developed Adam, one of the most popular adaptive methods in deep learning, built upon RMSProp and added corrective terms at the beginning of training, together with heavy-ball style momentum.

In the online convex optimization setting, Duchi et al. showed that Adagrad achieves optimal regret for online convex optimization. Kingma & Ba provided a similar proof for Adam when using a decreasing overall step size, although this proof was later shown to be incorrect by Reddi et al., who introduced AMSGrad as a convergent alternative. Ward et al. proved that Adagrad also converges to a critical point for non convex objectives with a rate $O{({{\ln{(N)}}/\sqrt{N}})}$ when using a scalar adaptive step-size, instead of diagonal. Zou et al. extended this proof to the vector case, while Zou et al. displayed a bound for Adam, showing convergence when the decay of the exponential moving average scales as $1 - {1/N}$ and the learning rate as $1/\sqrt{N}$.

In this paper, we present a simplified and unified proof of convergence to a critical point for Adagrad and Adam for stochastic non-convex smooth optimization. We assume that the objective function is lower bounded, smooth and the stochastic gradients are almost surely bounded. We recover the standard $O{({{\ln{(N)}}/\sqrt{N}})}$ convergence rate for Adagrad for all step sizes, and the same rate with Adam with an appropriate choice of the step sizes and decay parameters, in particular, Adam can converge without using the AMSGrad variant. Compared to previous work, our bound significantly improves the dependency on the momentum parameter $\beta_{1}$. The best known bounds for Adagrad and Adam are respectively in $O{({({1 - \beta_{1}})}^{- 3})}$ and $O{({({1 - \beta_{1}})}^{- 5})}$ (see Section 3), while our result is in $O{({({1 - \beta_{1}})}^{- 1})}$ for both algorithms. This improvement is a step toward understanding the practical efficiency of heavy-ball momentum.

### Outline

The precise setting and assumptions are stated in the next section, and previous work is then described in Section 3. The main theorems are presented in Section 4, followed by a full proof for the case without momentum in Section 5 ‣ A Simple Convergence Proof of Adam and Adagrad"). The proof of the convergence with momentum is deferred to the supplementary material, Section A. Finally we compare our bounds with experimental results, both on toy and real life problems in Section 6.

## Setup

### Notation

Let $d \in {\mathbb{N}}$ be the dimension of the problem (i.e. the number of parameters of the function to optimize) and take ${\lbrack d\rbrack} = {\{ 1,2,\ldots,d\}}$. Given a function $h:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, we denote by $\nabla h$ its gradient and $\nabla_{i}h$ the $i$-th component of the gradient. We use a small constant $\epsilon$, e.g. $10^{- 8}$, for numerical stability. Given a sequence ${(u_{n})}_{n \in {\mathbb{N}}}$ with ${{\forall n} \in {\mathbb{N}}},{u_{n} \in {\mathbb{R}}^{d}}$, we denote $u_{n,i}$ for $n \in {\mathbb{N}}$ and $i \in {\lbrack d\rbrack}$ the $i$-th component of the $n$-th element of the sequence.

We want to optimize a function $F:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$. We assume there exists a random function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ such that ${{\mathbb{E}}\left\lbrack {{\nabla f}{(x)}} \right\rbrack} = {{\nabla F}{(x)}}$ for all $x \in {\mathbb{R}}^{d}$, and that we have access to an oracle providing i.i.d. samples ${(f_{n})}_{n \in {\mathbb{N}}^{\ast}}$. We note ${\mathbb{E}}_{n - 1}\lbrack \cdot \rbrack$ the conditional expectation knowing $f_{1},\ldots,f_{n - 1}$. In machine learning, $x$ typically represents the weights of a linear or deep model, $f$ represents the loss from individual training examples or minibatches, and $F$ is the full training objective function. The goal is to find a critical point of $F$.

### Adaptive methods

We study both Adagrad and Adam using a unified formulation. We assume we have $0 < \beta_{2} \leq 1$, $0 \leq \beta_{1} < \beta_{2}$, and a non negative sequence ${(\alpha_{n})}_{n \in {\mathbb{N}}^{\ast}}$. We define three vectors ${m_{n},v_{n},x_{n}} \in {\mathbb{R}}^{d}$ iteratively. Given $x_{0} \in {\mathbb{R}}^{d}$ our starting point, $m_{0} = 0$, and $v_{0} = 0$, we define for all iterations $n \in {\mathbb{N}}^{\ast}$,

The parameter $\beta_{1}$ is a heavy-ball style momentum parameter, while $\beta_{2}$ controls the decay rate of the per-coordinate exponential moving average of the squared gradients. Taking $\beta_{1} = 0$, $\beta_{2} = 1$ and $\alpha_{n} = \alpha$ gives Adagrad. While the original Adagrad algorithm did not include a heavy-ball-like momentum, our analysis also applies to the case $\beta_{1} > 0$.

### Adam and its corrective terms

The original Adam algorithm uses a weighed average, rather than a weighted sum for and, i.e. it uses

We can achieve the same definition by taking $\alpha_{\text{adam}} = {\alpha \cdot \frac{1 - \beta_{1}}{\sqrt{1 - \beta_{2}}}}$. The original Adam algorithm further includes two corrective terms to account for the fact that $m_{n}$ and $v_{n}$ are biased towards 0 for the first few iterations. Those corrective terms are equivalent to taking a step-size $\alpha_{n}$ of the form

Those corrective terms can be seen as the normalization factors for the weighted sum given by and Note that each term goes to its limit value within a few times $1/{({1 - \beta})}$ updates (with $\beta \in {\{\beta_{1},\beta_{2}\}}$). which explains the $({1 - \beta_{1}})$ term in. In the present work, we propose to drop the corrective term for $m_{n}$, and to keep only the one for $v_{n}$, thus using the alternative step size

This simplification motivated by several observations:

By dropping either corrective terms, $\alpha_{n}$ becomes monotonic, which simplifies the proof.

For typical values of $\beta_{1}$ and $\beta_{2}$ (e.g. 0.9 and 0.999), the corrective term for $m_{n}$ converges to its limit value much faster than the one for $v_{n}$.

Removing the corrective term for $m_{n}$ is equivalent to a learning-rate warmup, which is popular in deep learning, while removing the one for $v_{n}$ would lead to an increased step size during early training. For values of $\beta_{2}$ close to 1, this can lead to divergence in practice.

We experimentally verify in Section 6.3 that dropping the corrective term for $m_{n}$ has no observable effect on the training process, while dropping the corrective term for $v_{n}$ leads to observable perturbations. In the following, we thus consider the variation of Adam obtained by taking $\alpha_{n}$ provided by.

### Assumptions

We make three assumptions. We first assume $F$ is bounded below by $F_{\ast}$, that is,

We then assume *the $\ell_{\infty}$ norm of the stochastic gradients is uniformly almost surely bounded*, i.e. there is $R \geq \sqrt{\epsilon}$ ($\sqrt{\epsilon}$ is used here to simplify the final bounds) so that

and finally, the *smoothness of the objective function*, e.g., its gradient is $L$-Liptchitz-continuous with respect to the $\ell_{2}$-norm:

We discuss the use of assumption in Section 4.2.

## Related work

Early work on adaptive methods showed that Adagrad achieves an optimal rate of convergence of $O{({1/\sqrt{N}})}$ for convex optimization. Later, RMSProp and Adam were developed for training deep neural networks, using an exponential moving average of the past squared gradients.

Kingma & Ba offered a proof that Adam with a decreasing step size converges for convex objectives. However, the proof contained a mistake spotted by Reddi et al., who also gave examples of convex problems where Adam does not converge to an optimal solution. They proposed AMSGrad as a convergent variant, which consisted in retaining the maximum value of the exponential moving average. When $\alpha$ goes to zero, AMSGrad is shown to converge in the convex and non-convex setting. Despite this apparent flaw in the Adam algorithm, it remains a widely popular optimizer, raising the question as to whether it converges. When $\beta_{2}$ goes to $1$ and $\alpha$ to 0, our results and previous work show that Adam does converge with the same rate as Adagrad. This is coherent with the counter examples of Reddi et al., because they uses a small exponential decay parameter $\beta_{2} < {1/5}$.

The convergence of Adagrad for non-convex objectives was first tackled by Li & Orabona, who proved its convergence, but under restrictive conditions (e.g., $\alpha \leq {\sqrt{\epsilon}/L}$). The proof technique was improved by Ward et al., who showed the convergence of "scalar" Adagrad, i.e., with a single learning rate, for any value of $\alpha$ with a rate of $O{({{\ln{(N)}}/\sqrt{N}})}$. Our approach builds on this work but we extend it to both Adagrad and Adam, in their coordinate-wise version, as used in practice, while also supporting heavy-ball momentum.

The coordinate-wise version of Adagrad was also tackled by Zou et al., offering a convergence result for Adagrad with either heavy-ball or Nesterov style momentum. We obtain the same rate for heavy-ball momentum with respect to $N$ (i.e., $O{({{\ln{(N)}}/\sqrt{N}})}$), but we improve the dependence on the momentum parameter $\beta_{1}$ from $O{({({1 - \beta_{1}})}^{- 3})}$ to $O{({({1 - \beta_{1}})}^{- 1})}$. Chen et al. also provided a bound for Adagrad and Adam, but without convergence guarantees for Adam for any hyper-parameter choice, and with a worse dependency on $\beta_{1}$. Zhou et al. also cover Adagrad in the stochastic setting, however their proof technique leads to a $\sqrt{1/\epsilon}$ term in their bound, typically with $\epsilon = 10^{- 8}$. Finally, a convergence bound for Adam was introduced by Zou et al.. We recover the same scaling of the bound with respect to $\alpha$ and $\beta_{2}$. However their bound has a dependency of $O{({({1 - \beta_{1}})}^{- 5})}$ with respect to $\beta_{1}$, while we get $O{({({1 - \beta_{1}})}^{- 1})}$, a significant improvement. Shi et al. obtain similar convergence results for RMSProp and Adam when considering the random shuffling setup. They use an affine growth condition (i.e. norm of the stochastic gradient is bounded by an affine function of the norm of the deterministic gradient) instead of the boundness of the gradient, but their bound decays with the number of total epochs, not stochastic updates leading to an overall $\sqrt{s}$ extra term with $s$ the size of the dataset. Finally, Faw et al. use the same affine growth assumption to derive high probability bounds for scalar Adagrad.

Non adaptive methods like SGD are also well studied in the non convex setting, with a convergence rate of $O{({1/\sqrt{N}})}$ for a smooth objective with bounded variance of the gradients. Unlike adaptive methods, SGD requires knowing the smoothness constant. When adding heavy-ball momentum, Yang et al. showed that the convergence bound degrades as $O{({({1 - \beta_{1}})}^{- 2})}$, assuming that the gradients are bounded. We apply our proof technique for momentum to SGD in the Appendix, Section B and improve this dependency to $O{({({1 - \beta_{1}})}^{- 1})}$. Recent work by Liu et al. achieves the same dependency with weaker assumptions. Defazio provided an in-depth analysis of SGD-M with a tight Liapunov analysis.

## Main results

For a number of iterations $N \in {\mathbb{N}}^{\ast}$, we note $\tau_{N}$ a random index with value in $\{ 0,\ldots,{N - 1}\}$, so that

If $\beta_{1} = 0$, this is equivalent to sampling $\tau$ uniformly in $\{ 0,\ldots,{N - 1}\}$. If $\beta_{1} > 0$, the last few $\frac{1}{1 - \beta_{1}}$ iterations are sampled rarely, and iterations older than a few times that number are sampled almost uniformly. Our results bound the expected squared norm of the gradient at iteration $\tau$, which is standard for non convex stochastic optimization.

### Convergence bounds

For simplicity, we first give convergence results for $\beta_{1} = 0$, along with a complete proof in Section 5 ‣ A Simple Convergence Proof of Adam and Adagrad"). We then provide the results with momentum, with their proofs in the Appendix, Section A.6. We also provide a bound on the convergence of SGD with a $O{(1/{(1 - \beta_{1})}}$ dependency in the Appendix, Section B.2, along with its proof in Section B.4.

### No heavy-ball momentum

### Theorem 1 (Convergence of Adagrad without momentum)

Given the assumptions from Section 2.3, the iterates $x_{n}$ defined in Section 2.2 with hyper-parameters verifying $\beta_{2} = 1$, $\alpha_{n} = \alpha$ with $\alpha > 0$ and $\beta_{1} = 0$, and $\tau$ defined by, we have for any $N \in {\mathbb{N}}^{\ast}$,

### Theorem 2 (Convergence of Adam without momentum)

Given the assumptions from Section 2.3, the iterates $x_{n}$ defined in Section 2.2 with hyper-parameters verifying $0 < \beta_{2} < 1$, $\alpha_{n} = {\alpha\sqrt{\frac{1 - \beta_{2}^{n}}{1 - \beta_{2}}}}$ with $\alpha > 0$ and $\beta_{1} = 0$, and $\tau$ defined by, we have for any $N \in {\mathbb{N}}^{\ast}$,

### With heavy-ball momentum

### Theorem 3 (Convergence of Adagrad with momentum)

Given the assumptions from Section 2.3, the iterates $x_{n}$ defined in Section 2.2 with hyper-parameters verifying $\beta_{2} = 1$, $\alpha_{n} = \alpha$ with $\alpha > 0$ and $0 \leq \beta_{1} < 1$, and $\tau$ defined by, we have for any $N \in {\mathbb{N}}^{\ast}$ such that $N > \frac{\beta_{1}}{1 - \beta_{1}}$,

with $\overset{\sim}{N} = {N - \frac{\beta_{1}}{1 - \beta_{1}}}$, and,

### Theorem 4 (Convergence of Adam with momentum)

Given the assumptions from Section 2.3, the iterates $x_{n}$ defined in Section 2.2 with hyper-parameters verifying $0 < \beta_{2} < 1$, $0 \leq \beta_{1} < \beta_{2}$, and, $\alpha_{n} = {\alpha{({1 - \beta_{1}})}\sqrt{\frac{1 - \beta_{2}^{n}}{1 - \beta_{2}}}}$ with $\alpha > 0$, and $\tau$ defined by, we have for any $N \in {\mathbb{N}}^{\ast}$ such that $N > \frac{\beta_{1}}{1 - \beta_{1}}$,

with $\overset{\sim}{N} = {N - \frac{\beta_{1}}{1 - \beta_{1}}}$, and

### Analysis of the bounds

### Dependency on $d$

The dependency in $d$ is present in previous works on coordinate wise adaptive methods. Note however that $R$ is defined as the $\ell_{\infty}$ bound on the on the stochastic gradient, so that in the case where the gradient has a similar scale along all dimensions, $dR^{2}$ would be a reasonable bound for $\left\| {{\nabla f}{(x)}} \right\|_{2}^{2}$. However, if many dimensions contribute little to the norm of the gradient, this would still lead to a worse dependency in $d$ that e.g. scalar Adagrad Ward et al. or SGD.

Diving into the technicalities of the proof to come, we will see in Section 5 ‣ A Simple Convergence Proof of Adam and Adagrad") that we apply Lemma 5.2. ‣ 5.1 Technical lemmas ‣ 5 Proofs for 𝛽₁=0 (no momentum) ‣ A Simple Convergence Proof of Adam and Adagrad") once per dimension. The contribution from each coordinate is mostly independent of the actual scale of its gradients (as it only appears in the log), so that the right hand side of the convergence bound will grow as $d$. In contrast, the scalar version of Adagrad has a single learning rate, so that Lemma 5.2. ‣ 5.1 Technical lemmas ‣ 5 Proofs for 𝛽₁=0 (no momentum) ‣ A Simple Convergence Proof of Adam and Adagrad") is only applied once, removing the dependency on $d$. However, this variant is rarely used in practice.

### Almost sure bound on the gradient

We chose to assume the existence of an almost sure uniform $\ell_{\infty}$-bound on the gradients given by. This is a strong assumption, although it is weaker than the one used by Duchi et al. for Adagrad in the convex case, where the iterates were assumed to be almost surely bounded. There exist a few real life problems that verifies this assumption, for instance logistic regression without weight penalty, and with bounded inputs. It is possible instead to assume only a uniform bound on the expected gradient ${\nabla F}{(x)}$, as done by Ward et al. and Zou et al.. This however lead to a bound on ${\mathbb{E}}\left\lbrack \left\| {{\nabla F}{(x_{\tau})}} \right\|_{2}^{4/3} \right\rbrack^{2/3}$ instead of a bound on ${\mathbb{E}}\left\lbrack \left\| {{\nabla F}{(x_{\tau})}} \right\|_{2}^{2} \right\rbrack$, all the other terms staying the same. We provide the sketch of the proof using Hölder inequality in the Appendix, Section A.7.

It is also possible to replace the bound on the gradient with an affine growth condition, i.e. the norm of the stochastic gradient is bounded by an affine function of the norm of the expected gradient. A proof for scalar Adagrad is provided by Faw et al.. Shi et al. do the same for RMSProp, however their convergence bound is decays as $O{({{\log{(T)}}/\sqrt{T}})}$ with $T$ the number of epoch, not the number of updates, leading to a significantly less tight bound for large datasets.

### Impact of heavy-ball momentum

Looking at Theorems 3. ‣ With heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad") and 4. ‣ With heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad"), we see that increasing $\beta_{1}$ always deteriorates the bounds. Taking $\beta_{1} = 0$ in those theorems gives us almost exactly the bound without heavy-ball momentum from Theorems 1. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad") and 2. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad"), up to a factor 3 in the terms of the form $dR^{2}$.

As discussed in Section 3, previous bounds for Adagrad in the non-convex setting deteriorates as $O{({({1 - \beta_{1}})}^{- 3})}$, while bounds for Adam deteriorates as $O{({({1 - \beta_{1}})}^{- 5})}$. Our unified proof for Adam and Adagrad achieves a dependency of $O{({({1 - \beta_{1}})}^{- 1})}$, a significant improvement. We refer the reader to the Appendix, Section A.3, for a detailed analysis. While our dependency still contradicts the benefits of using momentum observed in practice, see Section 6, our tighter analysis is a step in the right direction.

### On sampling of $\tau$

Note that in, we sample with a lower probability the latest iterations. This can be explained by the fact that the proof technique for stochastic optimization in the non-convex case is based on the idea that for every iteration $n$, either ${\nabla F}{(x_{n})}$ is small, or $F{(x_{n + 1})}$ will decrease by some amount. However, when introducing momentum, and especially when taking the limit $\beta_{1}\rightarrow 1$, the latest gradient ${\nabla F}{(x_{n})}$ has almost no influence over $x_{n + 1}$, as the momentum term updates slowly. Momentum *spreads* the influence of the gradients over time, and thus, it will take a few updates for a gradient to have fully influenced the iterate $x_{n}$ and thus the value of the function $F{(x_{n})}$. From a formal point of view, the sampling weights given by naturally appear as part of the proof which is presented in Section A.6.

### Optimal finite horizon Adam is Adagrad

Let us take a closer look at the result from Theorem 2. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad"). It could seem like some quantities can explode but actually not for any reasonable values of $\alpha$, $\beta_{2}$ and $N$. Let us try to find the best possible rate of convergence for Adam for a finite horizon $N$, i.e. $q \in {\mathbb{R}}_{+}$ such that ${{\mathbb{E}}\left\lbrack \left\| {{\nabla F}{(x_{\tau})}} \right\|^{2} \right\rbrack} = {O{({{\ln{(N)}}N^{- q}})}}$ for some choice of the hyper-parameters $\alpha{(N)}$ and $\beta_{2}{(N)}$. Given that the upper bound in (11. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")) is a sum of non-negative terms, we need each term to be of the order of ${\ln{(N)}}N^{- q}$ or negligible. Let us assume that this rate is achieved for $\alpha{(N)}$ and $\beta_{2}{(N)}$. The bound tells us that convergence can only be achieved if ${\lim{\alpha{(N)}}} = 0$ and ${\lim{\beta_{2}{(N)}}} = 1$, with the limits taken for $N\rightarrow\infty$. This motivates us to assume that there exists an asymptotic development of ${\alpha{(N)}} \propto {N^{- a} + {o{(N^{- a})}}}$, and of ${1 - {\beta_{2}{(N)}}} \propto {N^{- b} + {o{(N^{- b})}}}$ for $a$ and $b$ positive. Thus, let us consider only the leading term in those developments, ignoring the leading constant (which is assumed to be non-zero). Let us further assume that $\epsilon \ll R^{2}$, we have

with $E = {{4dR^{2}N^{b/2}} + {dRLN^{b - a}}}$. Let us ignore the log terms for now, and use $\frac{N^{- b}}{1 - N^{- b}} \sim N^{- b}$ for $N\rightarrow\infty$, to get

Adding back the logarithmic term, the best rate we can obtain is $O{({{\ln{(N)}}/\sqrt{N}})}$, and it is only achieved for $a = {1/2}$ and $b = 1$, i.e., $\alpha = {\alpha_{1}/\sqrt{N}}$ and $\beta_{2} = {1 - {1/N}}$. We can see the resemblance between Adagrad on one side and Adam with a finite horizon and such parameters on the other. Indeed, an exponential moving average with a parameter $\beta_{2} = {1 - {1/N}}$ as a typical averaging window length of size $N$, while Adagrad would be an exact average of the past $N$ terms. In particular, the bound for Adam now becomes

which differ from (10. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")) only by a $+ {N/{({N - 1})}}$ next to the log term.

### Adam and Adagrad are twins

Our analysis highlights an important fact: *Adam is to Adagrad like constant step size SGD is to decaying step size SGD*. While Adagrad is asymptotically optimal, it also leads to a slower decrease of the term proportional to ${F{(x_{0})}} - F_{\ast}$, as $1/\sqrt{N}$ instead of $1/N$ for Adam. During the initial phase of training, it is likely that this term dominates the loss, which could explain the popularity of Adam for training deep neural networks rather than Adagrad. With its default parameters, Adam will not converge. It is however possible to choose $\alpha$ and $\beta_{2}$ to achieve an $\epsilon$ critical point for $\epsilon$ arbitrarily small and, for a known time horizon, they can be chosen to obtain the exact same bound as Adagrad.

## Proofs for $\beta_{1} = 0$ (no momentum)

We assume here for simplicity that $\beta_{1} = 0$, i.e., there is no heavy-ball style momentum. Taking $n \in {\mathbb{N}}^{\ast}$, the recursions introduced in Section 2.2 can be simplified into

Remember that we recover Adagrad when $\alpha_{n} = \alpha$ for $\alpha > 0$ and $\beta_{2} = 1$, while Adam can be obtained taking $0 < \beta_{2} < 1$, $\alpha > 0$,

Throughout the proof we denote by ${\mathbb{E}}_{n - 1}\lbrack \cdot \rbrack$ the conditional expectation with respect to $f_{1},\ldots,f_{n - 1}$. In particular, $x_{n - 1}$ and $v_{n - 1}$ are deterministic knowing $f_{1},\ldots,f_{n - 1}$. For all $n \in {\mathbb{N}}^{\ast}$, we also define ${\overset{\sim}{v}}_{n} \in {\mathbb{R}}^{d}$ so that for all $i \in {\lbrack d\rbrack}$,

i.e., we replace the last gradient contribution by its expected value conditioned on $f_{1},\ldots,f_{n - 1}$.

### Technical lemmas

A problem posed by the update (16 ‣ A Simple Convergence Proof of Adam and Adagrad")) is the correlation between the numerator and denominator. This prevents us from easily computing the conditional expectation and as noted by Reddi et al., the expected direction of update can have a positive dot product with the objective gradient. It is however possible to control the deviation from the descent direction, following Ward et al. with this first lemma.

### Lemma 5.1 (adaptive update approximately follow a descent direction)

For all $n \in {\mathbb{N}}^{\ast}$ and $i \in {\lbrack d\rbrack}$, we have:

### Proof

We take $i \in {\lbrack d\rbrack}$ and note $G = {{\nabla_{i}F}{(x_{n - 1})}}$, $g = {{\nabla_{i}f_{n}}{(x_{n - 1})}}$, $v = v_{n,i}$ and $\overset{\sim}{v} = {\overset{\sim}{v}}_{n,i}$.

Given that $g$ and $\overset{\sim}{v}$ are independent knowing $f_{1},\ldots,f_{n - 1}$, we immediately have

Now we need to control the size of the second term $A$,

The last inequality comes from the fact that ${\sqrt{\epsilon + v} + \sqrt{\epsilon + \overset{\sim}{v}}} \geq {\max{(\sqrt{\epsilon + v},\sqrt{\epsilon + \overset{\sim}{v}})}}$ and $\left| {{{\mathbb{E}}_{n - 1}\left\lbrack g^{2} \right\rbrack} - g^{2}} \right| \leq {{{\mathbb{E}}_{n - 1}\left\lbrack g^{2} \right\rbrack} + g^{2}}$. Following Ward et al., we can use the following inequality to bound $\kappa$ and $\rho$,

First applying (22 ‣ A Simple Convergence Proof of Adam and Adagrad")) to $\kappa$ with

Given that ${\epsilon + \overset{\sim}{v}} \geq {{\mathbb{E}}_{n - 1}\left\lbrack g^{2} \right\rbrack}$ and taking the conditional expectation, we can simplify as

Given that $\sqrt{{\mathbb{E}}_{n - 1}\left\lbrack g^{2} \right\rbrack} \leq \sqrt{\epsilon + \overset{\sim}{v}}$ and $\sqrt{{\mathbb{E}}_{n - 1}\left\lbrack g^{2} \right\rbrack} \leq R$, we can simplify (23 ‣ A Simple Convergence Proof of Adam and Adagrad")) as

Now turning to $\rho$, we use (22 ‣ A Simple Convergence Proof of Adam and Adagrad")) with

Given that ${\epsilon + v} \geq g^{2}$ and taking the conditional expectation we obtain

which we simplify using the same argument as for (24 ‣ A Simple Convergence Proof of Adam and Adagrad")) into

Notice that in (25 ‣ A Simple Convergence Proof of Adam and Adagrad")), we possibly divide by zero. It suffice to notice that if ${{\mathbb{E}}_{n - 1}\left\lbrack g^{2} \right\rbrack} = 0$ then $g^{2} = 0$ a.s. so that $\rho = 0$ and (27 ‣ A Simple Convergence Proof of Adam and Adagrad")) is still verified. Summing (24 ‣ A Simple Convergence Proof of Adam and Adagrad")) and (27 ‣ A Simple Convergence Proof of Adam and Adagrad")) we can bound

Injecting (28 ‣ A Simple Convergence Proof of Adam and Adagrad")) and (21 ‣ A Simple Convergence Proof of Adam and Adagrad")) into (20 ‣ A Simple Convergence Proof of Adam and Adagrad")) finishes the proof. ∎

Anticipating on Section 5.2 ‣ A Simple Convergence Proof of Adam and Adagrad"), the previous Lemma gives us a bound on the deviation from a descent direction. While for a specific iteration, this deviation can take us away from a descent direction, the next lemma tells us that the sum of those deviations cannot grow larger than a logarithmic term. This key insight introduced in Ward et al. is what makes the proof work.

### Lemma 5.2 (sum of ratios with the denominator being the sum of past numerators)

We assume we have $0 < \beta_{2} \leq 1$ and a non-negative sequence ${(a_{n})}_{n \in {\mathbb{N}}^{\ast}}$. We define for all $n \in {\mathbb{N}}^{\ast}$, $b_{n} = {\sum_{j = 1}^{n}{\beta_{2}^{n - j}a_{j}}}$. We have

### Proof

Given that $\ln$ is increasing, and the fact that $b_{j} > a_{j} \geq 0$, we have for all $j \in {\mathbb{N}}^{\ast}$,

The first term forms a telescoping series, while the second one is bounded by $- {\ln{(\beta_{2})}}$. Summing over all $j \in {\lbrack N\rbrack}$ gives the desired result. ∎

### Proof of Adam and Adagrad without momentum

Let us take an iteration $n \in {\mathbb{N}}^{\ast}$, we define the update $u_{n} \in {\mathbb{R}}^{d}$:

### Adagrad

As explained in Section 2.2, we have $\alpha_{n} = \alpha$ for $\alpha > 0$. Using the smoothness of $F$, we have

Taking the conditional expectation with respect to $f_{0},\ldots,f_{n - 1}$ we can apply the descent Lemma 5.1. ‣ 5.1 Technical lemmas ‣ 5 Proofs for 𝛽₁=0 (no momentum) ‣ A Simple Convergence Proof of Adam and Adagrad"). Notice that due to the a.s. $\ell_{\infty}$ bound on the gradients, we have for any $i \in {\lbrack d\rbrack}$, $\sqrt{\epsilon + {\overset{\sim}{v}}_{n,i}} \leq {R\sqrt{n}}$, so that,

Summing the previous inequality for all $n \in {\lbrack N\rbrack}$, taking the complete expectation, and using that $\sqrt{n} \leq \sqrt{N}$ gives us,

From there, we can bound the last sum on the right hand side using Lemma 5.2. ‣ 5.1 Technical lemmas ‣ 5 Proofs for 𝛽₁=0 (no momentum) ‣ A Simple Convergence Proof of Adam and Adagrad") once for each dimension. Rearranging the terms, we obtain the result of Theorem 1. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad").

### Adam

As given by in Section 2.2, we have $\alpha_{n} = {\alpha\sqrt{\frac{1 - \beta_{2}^{n}}{1 - \beta_{2}}}}$ for $\alpha > 0$. Using the smoothness of $F$ defined in, we have

We have for any $i \in {\lbrack d\rbrack}$, $\sqrt{\epsilon + {\overset{\sim}{v}}_{n,i}} \leq {R\sqrt{\sum_{j = 0}^{n - 1}\beta_{2}^{j}}} = {R\sqrt{\frac{1 - \beta_{2}^{n}}{1 - \beta_{2}}}}$, thanks to the a.s. $\ell_{\infty}$ bound on the gradients, so that,

Taking the conditional expectation with respect to $f_{1},\ldots,f_{n - 1}$ we can apply the descent Lemma 5.1. ‣ 5.1 Technical lemmas ‣ 5 Proofs for 𝛽₁=0 (no momentum) ‣ A Simple Convergence Proof of Adam and Adagrad") and use (34 ‣ A Simple Convergence Proof of Adam and Adagrad")) to obtain from (33 ‣ A Simple Convergence Proof of Adam and Adagrad")),

Given that $\beta_{2} < 1$, we have $\alpha_{n} \leq \frac{\alpha}{\sqrt{1 - \beta_{2}}}$. Summing the previous inequality for all $n \in {\lbrack N\rbrack}$ and taking the complete expectation yields

Applying Lemma 5.2. ‣ 5.1 Technical lemmas ‣ 5 Proofs for 𝛽₁=0 (no momentum) ‣ A Simple Convergence Proof of Adam and Adagrad") for each dimension and rearranging the terms finishes the proof of Theorem 2. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad").

(a) Average squared norm of the gradient on a toy task, see Section 6, for more details. For the α and 1 − β2 curves, we initialize close to the optimum to make the F0 − F* term negligible.

(b) Average squared norm of the gradient of a small convolutional model Gitman &amp; Ginsburg trained on CIFAR-10, with a random initialization. The full gradient is evaluated every epoch.

Figure 1: Observed average squared norm of the objective gradients after a fixed number of iterations when varying a single parameter out of α, 1 − β1 and 1 − β2, on a toy task (left, 106 iterations) and on CIFAR-10 (right, 600 epochs with a batch size 128). All curves are averaged over 3 runs, error bars are negligible except for small values of α on CIFAR-10. See Section 6 for details.

Figure 2: Training trajectories for varying values of α ∈ {10−4, 10−3}, β1 ∈ {0., 0.5, 0.8, 0.9, 0.99} and β2 ∈ {0.9, 0.99, 0.999, 0.9999}. The top row (resp. bottom) gives the training loss (resp. squared norm of the expected gradient). The left column uses all corrective terms in the original Adam algorithm, the middle column drops the corrective term on mn (equivalent to our proof setup), and the right column drops the corrective term on vn. We notice a limited impact when dropping the corrective term on mn, but dropping the corrective term on vn has a much stronger impact.

## Experiments

On Figure 1 ‣ A Simple Convergence Proof of Adam and Adagrad"), we compare the effective dependency of the average squared norm of the gradient in the parameters $\alpha$, $\beta_{1}$ and $\beta_{2}$ for Adam, when used on a toy task and CIFAR-10.

### Setup

### Toy problem

In order to support the bounds presented in Section 4, in particular the dependency in $\beta_{2}$, we test Adam on a specifically crafted toy problem. We take $x \in {\mathbb{R}}^{6}$ and define for all $i \in {\lbrack 6\rbrack}$, $p_{i} = 10^{- i}$. We take ${(Q_{i})}_{i \in {\lbrack 6\rbrack}}$, Bernoulli variables with ${{\mathbb{P}}\left\lbrack {Q_{i} = 1} \right\rbrack} = p_{i}$. We then define $f$ for all $x \in {\mathbb{R}}^{d}$ as

with for all $y \in {\mathbb{R}}$,

Intuitively, each coordinate is pointing most of the time towards 1, but exceptionally towards -1 with a weight of $1/\sqrt{p_{i}}$. Those rare events happens less and less often as $i$ increase, but with an increasing weight. Those weights are chosen so that all the coordinates of the gradient have the same variance^11^1We deviate from the a.s. bounded gradient assumption for this experiment, see Section 4.2 for a discussion on a.s. bound vs bound in expectation.. It is necessary to take different probabilities for each coordinate. If we use the same $p$ for all, we observe a phase transition when ${1 - \beta_{2}} \approx p$, but not the continuous improvement we obtain on Figure 1(a) ‣ A Simple Convergence Proof of Adam and Adagrad").

We plot the variation of ${\mathbb{E}}\left\lbrack \left\| {F{(x_{\tau})}} \right\|_{2}^{2} \right\rbrack$ after $10^{6}$ iterations with batch size 1 when varying either $\alpha$, $1 - \beta_{1}$ or $1 - \beta_{2}$ through a range of 13 values uniformly spaced in log-scale between $10^{- 6}$ and $1$. When varying $\alpha$, we take $\beta_{1} = 0$ and $\beta_{2} = {1 - 10^{- 6}}$. When varying $\beta_{1}$, we take $\alpha = 10^{- 5}$ and $\beta_{2} = {1 - 10^{- 6}}$ (i.e. $\beta_{2}$ is so that we are in the Adagrad-like regime). Finally, when varying $\beta_{2}$, we take $\beta_{1} = 0$ and $\alpha = 10^{- 6}$. We start from $x_{0}$ close to the optimum by running first $10^{6}$ iterations with $\alpha = 10^{- 4}$, then $10^{6}$ iterations with $\alpha = 10^{- 5}$, always with $\beta_{2} = {1 - 10^{- 6}}$. This allows to have ${{F{(x_{0})}} - F_{\ast}} \approx 0$ in (11. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")) and (13. ‣ With heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")) and focus on the second part of both bounds. All curves are averaged over three runs. Error bars are plotted but not visible in log-log scale.

### CIFAR-10

We train a simple convolutional network on the CIFAR-10^22^2[https://www.cs.toronto.edu/\~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html) image classification dataset. Starting from a random initialization, we train the model on a single V100 for 600 epochs with a batch size of 128, evaluating the full training gradient after each epoch. This is a proxy for ${\mathbb{E}}\left\lbrack \left\| {F{(x_{\tau})}} \right\|_{2}^{2} \right\rbrack$, which would be to costly to evaluate exactly. All runs use the default config $\alpha = 10^{- 3}$, $\beta_{2} = 0.999$ and $\beta_{1} = 0.9$, and we then change one of the parameter.

We take $\alpha$ from a uniform range in log-space between $10^{- 6}$ and $10^{- 2}$ with 9 values, for $1 - \beta_{1}$ the range is from $10^{- 5}$ to $0.3$ with 9 values, and for $1 - \beta_{2}$, from $10^{- 6}$ to $10^{- 1}$ with 11 values. Unlike for the toy problem, we do not initialize close to the optimum, as even after 600 epochs, the norm of the gradients indicates that we are not at a critical point. All curves are averaged over three runs. Error bars are plotted but not visible in log-log scale, except for large values of $\alpha$.

### Analysis

### Toy problem

Looking at Figure 1(a) ‣ A Simple Convergence Proof of Adam and Adagrad"), we observe a continual improvement as $\beta_{2}$ increases. Fitting a linear regression in log-log scale of ${\mathbb{E}}{\lbrack\left\| {{\nabla F}{(x_{\tau})}} \right\|_{2}^{2}\rbrack}$ with respect to $1 - \beta_{2}$ gives a slope of 0.56 which is compatible with our bound (11. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")), in particular the dependency in $O{({1/\sqrt{1 - \beta_{2}}})}$. As we initialize close to the optimum, a small step size $\alpha$ yields as expected the best performance. Doing the same regression in log-log scale, we find a slope of 0.87, which is again compatible with the $O{(\alpha)}$ dependency of the second term in (11. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")). Finally, we observe a limited impact of $\beta_{1}$, except when $1 - \beta_{1}$ is small. The regression in log-log scale gives a slope of -0.16, while our bound predicts a slope of -1.

### CIFAR 10

Let us now turn to Figure 1(b) ‣ A Simple Convergence Proof of Adam and Adagrad"). As we start from random weights for this problem, we observe that a large step size gives the best performance, although we observe a high variance for the largest $\alpha$. This indicates that training becomes unstable for large $\alpha$, which is not predicted by the theory. This is likely a consequence of the bounded gradient assumption not being verified for deep neural networks. We observe a small improvement as $1 - \beta_{2}$ decreases, although nowhere near what we observed on our toy problem. Finally, we observe a sweet spot for the momentum $\beta_{1}$, not predicted by our theory. We conjecture that this is due to the variance reduction effect of momentum (averaging of the gradients over multiple mini-batches, while the weights have not moved so much as to invalidate past information).

### Impact of the Adam corrective terms

Using the same experimental setup on CIFAR-10, we compare the impact of removing either of the corrective term of the original Adam algorithm, as discussed in Section 2.2. We ran a cartesian product of training for 100 epochs, with $\beta_{1} \in {\{ 0,0.5,0.8,0.9,0.99\}}$, $\beta_{2} \in {\{ 0.9,0.99,0.999,0.9999\}}$, and $\alpha \in {\{ 10^{- 4},10^{- 3}\}}$. We report both the training loss and norm of the expected gradient on Figure 2 ‣ A Simple Convergence Proof of Adam and Adagrad"). We notice a limited difference when dropping the corrective term on $m_{n}$, but dropping the term $v_{n}$ has an important impact on the training trajectories. This confirm our motivation for simplifying the proof by removing the corrective term on the momentum.

## Conclusion

We provide a simple proof on the convergence of Adam and Adagrad without heavy-ball style momentum. Our analysis highlights a link between the two algorithms: with right the hyper-parameters, Adam converges like Adagrad. The extension to heavy-ball momentum is more complex, but we significantly improve the dependence on the momentum parameter for Adam, Adagrad, as well as SGD. We exhibit a toy problem where the dependency on $\alpha$ and $\beta_{2}$ experimentally matches our prediction. However, we do not predict the practical interest of momentum, so that improvements to the proof are needed for future work.

### Broader Impact Statement

The present theoretical results on the optimization of non convex losses in a stochastic settings impact our understanding of the training of deep neural network. It might allow a deeper understanding of neural network training dynamics and thus reinforce any existing deep learning applications. There would be however no direct possible negative impact to society.
