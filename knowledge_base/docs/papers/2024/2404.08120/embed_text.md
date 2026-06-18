## Introduction

System identification --- the problem of estimating the parameters of an unknown dynamical system from a single trajectory of input/output data --- plays an important role in many problem domains such as control theory, robotics, and reinforcement learning. There has been tremendous progress in analyzing the performance of various system identification schemes --- classical results showed asymptotic convergence \[(https://arxiv.org/html/2404.08120v1#bib.bib13)\], whereas recent advances in non-asymptotic theory quantified the sample complexity of learning accurate estimates from data \[(https://arxiv.org/html/2404.08120v1#bib.bib17), (https://arxiv.org/html/2404.08120v1#bib.bib30)\]. However, these works all narrowly focus on system identification itself without accounting for the requirements for control applications. In this work, we consider a problem setting where linear system identification meets switching control so that we develop a data-driven approach to simultaneously achieve desirable control and system identification objectives.

In this paper, we consider a collection of discrete-time, partially-observed linear systems ${\{{(C_{i},A_{i},B_{i})}\}}_{i = 1}^{N}$ containing the unknown true system parameters $(C_{\star},A_{\star},B_{\star})$. These systems are expressed in terms of:

where the dimensions are ${x_{t} \in {\mathbb{R}}^{d_{x}}},{u_{t} \in {\mathbb{R}}^{d_{u}}}$ and $y_{t} \in {\mathbb{R}}^{d_{y}}$. We assume that the initial state $x_{1} \sim {\mathcal{N}{(0,I_{d_{x} \times d_{x}})}}$, process noise $w_{t} \sim {\mathcal{N}{(0,{\sigma_{w}^{2}I_{d_{x} \times d_{x}}})}}$, and observation noise $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{\eta}^{2}I_{d_{y} \times d_{y}}})}}$ come from Gaussian distributions. In many complex systems, e.g. power systems \[(https://arxiv.org/html/2404.08120v1#bib.bib14)\], autonomous vehicles \[(https://arxiv.org/html/2404.08120v1#bib.bib2)\], and public health \[(https://arxiv.org/html/2404.08120v1#bib.bib5)\], it is not practical to design a single controller that achieves satisfactory performance for all candidate models in the collection. To this end, in a linear switched system, each candidate model has an associated linear controller giving satisfactory performance on this model. We also note that a mismatched pair of a model and a controller can result in an unstable closed-loop system.

Following the convention of \[(https://arxiv.org/html/2404.08120v1#bib.bib8)\], we use the multi-controller framework $K{(p_{t};{\check{x}}_{t},y_{t})}$, where ${\check{x}}_{t}$ is the internal state of the controller, $p_{t} \in {\lbrack N\rbrack}$ is the piece-wise constant switching signal that determines which candidate linear controller is applied, and $y_{t}$ is the system's output. And for reasons that will be discussed later, we keep an input signal $u_{t}$ that is equal to an additive control action on top of the multi-controller. As illustrated in Figure (https://arxiv.org/html/2404.08120v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A least-square method for non-asymptotic identification in linear switching control"), with an open-loop system $(C,A,B)$ and a fixed switching signal $p_{t} = j$, the closed-loop system becomes $(\overset{\sim}{C},{\overset{\sim}{A}}^{(j)},\overset{\sim}{B})$, where ${\overset{\sim}{A}}^{(j)}$ encapsulates both the dynamics $(C,A,B)$ and the controller $K{(i; \cdot )}$ and $\overset{\sim}{C},\overset{\sim}{B}$ only depend on $C,B$. Then, the set of all possible closed-loop dynamics is ${\{{\{{({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})}\}}_{i = 1}^{N}\}}_{j = 1}^{N}$ and can be pre-computed. Our goal is then to design a switching strategy that collects the data necessary for identifying the true open-loop parameters $(C_{\star},A_{\star},B_{\star})$ and comes with non-asymptotic performance guarantees.

Figure 1: Switching control (with a fixed switching signal)

Although there are several works regarding non-asymptotic identification of partially-observed linear systems \[(https://arxiv.org/html/2404.08120v1#bib.bib17), (https://arxiv.org/html/2404.08120v1#bib.bib25), (https://arxiv.org/html/2404.08120v1#bib.bib22), (https://arxiv.org/html/2404.08120v1#bib.bib4)\], these results all assume that the data are collected from a stable linear system. As the closed-loop system is potentially unstable in our setting, we cannot directly apply their results. Furthermore, even under a stabilizing controller, these prior results do not leverage our knowledge that the possible system parameters are contained in a finite set and thus lead to estimation guarantees with sub-optimal dependency on problem dimensions.

Fortunately, there has been extensive work on leveraging the particular properties of switched systems. Among the existing literature, one popular switching strategy that shares many similarities to our problem setup is the so-called estimator-based supervisory control (see the surveys \[(https://arxiv.org/html/2404.08120v1#bib.bib8), (https://arxiv.org/html/2404.08120v1#bib.bib12)\]). The estimator-based supervisory control scheme periodically picks the candidate model that most closely matches the observations and applies its associated controller. While it has been shown that this strategy asymptotically stabilizes the switched system, there are no non-asymptotic guarantees for its performance. So, we lack a precise characterization of how long this method may take to converge to satisfactory performance.

### Contributions

In this paper, we focus on the interplay of these two threads of work and derive a novel approach to the study of non-asymptotic system identification in switching control. To this end, we make the following technical contributions:

In Section (https://arxiv.org/html/2404.08120v1#S3 "3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control"), we present a least-square-based method for linear model identification with prior knowledge that the ground truth is contained in a finite collection of candidate models. Under this setting, we derive a sample complexity bound that is dimension-free.

In Section [4.2](https://arxiv.org/html/2404.08120v1#S4.SS2 "4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), we establish an instability detection criterion by quantitatively bounding the finite-time input-to-output gain of a stable linear system. This allows us to detect any explosive closed-loop dynamics and remove any controllers that are destabilizing the switched system.

Most importantly, in Section [4.3](https://arxiv.org/html/2404.08120v1#S4.SS3 "4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), we present a data-driven algorithm for linear system identification problems in switching control. We derive a sample complexity bound on the number of steps for which our strategy finds the correct model with high probability.

In Section [4.4](https://arxiv.org/html/2404.08120v1#S4.SS4 "4.4 Implications for estimator-based supervisory control ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), we compare our approach to the classical method of estimator-based supervisory control and discuss the implications of our non-asymptotic guarantees to the problem of switching control.

### Notations

For a matrix $M$, we denote $\left. \parallel M\parallel \right._{F}$ as its Frobenius norm, $\left. \parallel M\parallel \right._{op} = {\sigma_{\max}{(M)}}$ as its operator norm (equivalently, its largest singular value), $\rho{(M)}$ as its spectral radius, and ${tr}{(M)}$ as its trace. For a stable linear system $(C,A,B)$, we define its $\mathcal{H}$-infinity norm as $\left. \parallel C,A,B\parallel \right._{\mathcal{H}_{\infty}} = {\sup_{{\parallel s\parallel} = 1}{\sigma_{\max}{({C{({{sI} - A})}^{- 1}B})}}}$, and for simplicity, we use shorthand $\left. \parallel C,A\parallel \right._{\mathcal{H}_{\infty}} = \left. \parallel C,A,I\parallel \right._{\mathcal{H}_{\infty}}$ and $\left. \parallel A\parallel \right._{\mathcal{H}_{\infty}} = \left. \parallel I,A,I\parallel \right._{\mathcal{H}_{\infty}}$. We also define $P{(C,A)}$ as the solution to the Lyapunov equation ${{{A^{\top}PA} - P} + {C^{\top}C}} = 0$, and we simply write $P$ when parameters $(C,A)$ are clear from the context.

To simplify our exposition, we sometimes ignore constant factors that do not meaningfully contribute to our conclusions. We define the big-O notation as $f \in {\mathcal{O}(g)}$ if ${\operatorname{lim\ sup}_{x\rightarrow\infty}{{{f{(x)}}/g}{(x)}}} < \infty$ and $f \in {\overset{\sim}{\mathcal{O}}(g)}$ if $f \in {\mathcal{O}\left( {{polylog}{( \cdot )}g{( \cdot )}} \right)}$. Lastly, we write $f \lesssim g$ if $f \leq {c \cdot g}$ for some universal constant $c$. Unless otherwise stated, we will explicitly write out any terms dependent on the problem dimensions. In particular, we consider the Frobenius norm and the trace of a matrix to be dimension-dependent, but the operator norm is not.

### Literature Review

Switching control has been studied extensively over the years. Among the existing literature, there are two popular approaches to designing performant switching policies --- estimator-based supervision that picks the candidate model that most closely resembles the observed process \[(https://arxiv.org/html/2404.08120v1#bib.bib8), (https://arxiv.org/html/2404.08120v1#bib.bib12)\], and performance-based falsification through some stability certificate \[(https://arxiv.org/html/2404.08120v1#bib.bib3), (https://arxiv.org/html/2404.08120v1#bib.bib18), (https://arxiv.org/html/2404.08120v1#bib.bib26), (https://arxiv.org/html/2404.08120v1#bib.bib20)\]. In this paper, we shall highlight the estimator-based supervision method. This approach was first formalized in the setting of continuous-time linear switched systems \[(https://arxiv.org/html/2404.08120v1#bib.bib15), (https://arxiv.org/html/2404.08120v1#bib.bib16)\] and was later extended to nonlinear models \[(https://arxiv.org/html/2404.08120v1#bib.bib9)\], and for discrete-time models \[(https://arxiv.org/html/2404.08120v1#bib.bib6)\]. However, all of the works above only provide asymptotic guarantees for their methods.

The methods of non-asymptotic linear system identification have seen significant progress with modern tools from statistical learning. In the case of a fully-observed linear model, \[(https://arxiv.org/html/2404.08120v1#bib.bib7), (https://arxiv.org/html/2404.08120v1#bib.bib24)\] showed that for stable systems, ordinary least square (OLS) achieves estimation error on the order of $\sqrt{T}$, where $T$ is the length of the sample trajectory. And for unstable linear systems, \[(https://arxiv.org/html/2404.08120v1#bib.bib21)\] showed that the OLS estimate may be inconsistent. Much of the same machinery can be applied to partially-observed stable linear systems, e.g. \[(https://arxiv.org/html/2404.08120v1#bib.bib17), (https://arxiv.org/html/2404.08120v1#bib.bib25), (https://arxiv.org/html/2404.08120v1#bib.bib22), (https://arxiv.org/html/2404.08120v1#bib.bib4)\]. Beyond system identification problems, these methods have been applied to problems such as online LQR \[(https://arxiv.org/html/2404.08120v1#bib.bib23)\] and latent state learning \[(https://arxiv.org/html/2404.08120v1#bib.bib27)\]. A summary of the recent advances in this field can be found in \[(https://arxiv.org/html/2404.08120v1#bib.bib30)\].

Finally, there are some recent works on applying online learning to switching control. For example, \[(https://arxiv.org/html/2404.08120v1#bib.bib11)\] considers a switched system with fully-observed non-linear models and, inspired by online bandit algorithms, proposes an approach that optimizes for some quadratic cost functions. We note that the setting of this work differs significantly from ours --- our method applies to partially-observed systems and our ultimate objective is identification so that we do not require access to cost functions.

## Mathematical Preliminaries

Before we dive into the technical results, we shall briefly introduce some tools from probability and learning theory that are key to our derivations.

We first define a generalization of Gaussian random variables. Roughly speaking, a sub-Gaussian random variable has tail concentration that is dominated by a Gaussian distribution.

### Definition 1

We say that a zero-mean random vector $X \in {\mathbb{R}}^{d}$ is $\sigma^{2}$-sub-Gaussian if for every unit vector $v$ and real value $\lambda$, we have

In this work, our system identification method is based on ordinary least square (OLS). Consider a linear model

where the sequence of random vectors ${\{ y_{t}\}}_{t = 1}^{T}$ and ${\{ z_{t}\}}_{t = 1}^{T}$ are adapted to a filtration ${\{\mathcal{F}_{t}\}}_{t \geq 0}$ and $r_{t}$ are residuals/noise that are $\sigma^{2}$-sub-Gaussian. Then, OLS seeks to recover the true parameter $\Theta_{\star}$ through the following estimate:

We can bound the estimation error $\hat{\Theta} - \Theta_{\star}$ with the self-normalized martingale tail bound.

### Proposition 1 (Theorem 1 in \[[1](https://arxiv.org/html/2404.08120v1#bib.bib1)\])

Consider ${\{ z_{t}\}}_{t = 1}^{T}$ adapted to a filtration ${\{\mathcal{F}_{t}\}}_{t \geq 0}$. Let $V = {\sum_{t = 1}^{T}{z_{t}z_{t}^{\top}}}$. If the scalar-valued random variable $r_{t} \mid \mathcal{F}_{t - 1}$ is $\sigma^{2}$-sub-Gaussian, then for any $V_{0} \succeq 0$,

with probability $1 - \delta$.

Additionally, a good OLS estimate requires the covariance matrix $V$ to be non-singular. Therefore, we want the input data $z_{t}$'s to be concentrated away from 0, which can also be interpreted as persistency of excitation. We can formalize this concept by the martingale small-ball property.

### Definition 2 (Definition 2.1 in \[[24](https://arxiv.org/html/2404.08120v1#bib.bib24)\])

We say that a sequence of $\mathcal{F}_{t}$-adapted random variables ${(Z_{t})}_{t \geq 1}$ satisfies the $(k,v,q)$-block martingale small-ball (BMSB) property if for any $t \geq 0$, we have ${\frac{1}{k}{\sum_{j = 1}^{k}{\Pr{({Z_{t + j}^{2} > \left. v^{2} \middle| \mathcal{F}_{t} \right.})}}}} \geq q$ almost surely.

This BMSB property implies that the quantity $\sum_{t = 1}^{T}Z_{t}^{2}$ scales linearly in $T$ with high probability. Thus, on average, the random variables $Z_{t}$ with the BMSB property lie outside of some interval around 0.

### Lemma 2 (Proposition 2.5 in \[[24](https://arxiv.org/html/2404.08120v1#bib.bib24)\])

If the sequence of random variables $(Z_{1},\ldots,Z_{T})$ is $(k,v,q)$-BMSB, then

Lastly, in this paper, we would encounter the squares of Gaussian random variables. So, we state a concentration bound on the quadratic form over Guassian random variables.

### Proposition 3 (Corollary 6 in \[[23](https://arxiv.org/html/2404.08120v1#bib.bib23)\])

Consider a symmetric matrix $M \in {\mathbb{S}}^{d \times d}$ and a random vector $g \sim {\mathcal{N}{(0,I_{d \times d})}}$. Then, for any $\delta \in {(0,{1/e})}$,

We note this is a simplified version of the Hanson-Wright inequality, and compare to the sharper statement in \[(https://arxiv.org/html/2404.08120v1#bib.bib19)\], we use the fact that $\left. \parallel \cdot \parallel \right._{F}$ and $\left. \parallel \cdot \parallel \right._{op}$ are bounded by the trace ${tr}{( \cdot )}$.

## Linear System Identification

In this section, we first focus our efforts on system identification. Specifically, under any constant switching signal $p_{t} = j$, we identify the index of the true system in the set of possible closed-loop dynamics ${\{{({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})}\}}_{i = 1}^{N}$, which corresponds to the dashed box in Figure (https://arxiv.org/html/2404.08120v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A least-square method for non-asymptotic identification in linear switching control"). We can then use this index to recover the true parameters of the unknown system. We stress that the techniques below are applicable to general partially-observed linear systems. So, in this section, we skip the distinctions between the open-loop vs. closed-loop systems and drop the superscript $\sim$.

### Problem setup

We consider a collection of partially-observed linear systems written as:

where the dimensions are ${x_{t} \in {\mathbb{R}}^{d_{x}}},{u_{t} \in {\mathbb{R}}^{d_{u}}}$ and $y_{t} \in {\mathbb{R}}^{d_{y}}$. We assume that the initial state $x_{1} \sim {\mathcal{N}{(0,I_{d_{x} \times d_{x}})}}$, process noise $w_{t} \sim {\mathcal{N}{(0,{\sigma_{w}^{2}I_{d_{x} \times d_{x}}})}}$, and observation noise $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{\eta}^{2}I_{d_{y} \times d_{y}}})}}$. The true system parameters $(C_{\star},A_{\star},B_{\star})$ belong to a collection of $N$ candidate modes ${\{{(C_{i},A_{i},B_{i})}\}}_{i = 1}^{N}$.

Additionally, only for this section, we assume that $A_{\star}$ is stable in the sense that ${\rho{(A_{\star})}} < 1$. This assumption is standard in the literature of non-asymptotic linear system identification. For fully-observed linear systems, \[(https://arxiv.org/html/2404.08120v1#bib.bib21)\] gave an example of an unstable linear system that a least-square estimator fails to identify its unknown parameters. And for the partially-observed setting, as we shall see, it is not possible to bound the residual noise terms when the system is unstable.

There has been a considerable amount of work for the no-prior case where the values of the matrices $(C_{\star},A_{\star},B_{\star})$ can be arbitrary (as long as $A_{\star}$ is stable), e.g. \[(https://arxiv.org/html/2404.08120v1#bib.bib17), (https://arxiv.org/html/2404.08120v1#bib.bib25), (https://arxiv.org/html/2404.08120v1#bib.bib22), (https://arxiv.org/html/2404.08120v1#bib.bib4)\]. The common approach is to use an exploratory Gaussian noise as the input $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I_{d_{u} \times d_{u}}})}}$. Then, we use the system's observed response $y_{t}$ to the sequence of past $h$ Gaussian inputs $z_{t}:={(u_{t - 1},u_{t - 2},\ldots,u_{t - h})}$ to estimate a Markov parameter that is equal to the system's output controllability matrix with time horizon of length $h$:

Before we apply ordinary least squares (OLS) to estimate the Markov parameter, we first recursively write out the dynamics:

Next, we can show that the random vector $e_{t} = {{C_{\star}A_{\star}^{H}x_{t - H}} + {\sum_{j = 1}^{H}{C_{\star}A_{\star}^{j - 1}w_{t - j}}}}$ is sub-Gaussian. For convenience, we write $w_{j:k} = {\lbrack w_{j};w_{j - 1};\ldots;w_{k}\rbrack}$, $\mathcal{R}_{k,\ell} = {\lbrack{C_{\star}A_{\star}^{k}},{C_{\star}A_{\star}^{k + 1}},\ldots,{C_{\star}A_{\star}^{{k + \ell} - 1}}\rbrack}$, and ${diag}_{m}{(B)}$ is a block diagonal matrix with $m$ copies of $B$. We note that $\mathcal{R}_{k,\ell}$ is a submatrix of the infinite-dimensional Toeplitz operator

whose operator norm is bounded above by $\left. \parallel C_{\star},A_{\star}\parallel \right._{\mathcal{H}_{\infty}}$ (see Section 4 in \[(https://arxiv.org/html/2404.08120v1#bib.bib28)\]). Therefore, we have $\left. \parallel\mathcal{R}_{k,\ell}\parallel \right._{op} \leq \left. \parallel C_{\star},A_{\star}\parallel \right._{\mathcal{H}_{\infty}}$ for any ${k,\ell} \geq 0$. Now, we write

Since $w_{{t - h - 1}:1}$ is $\sigma_{w}^{2}$-sub-Gaussian, the first term is ${\left. \parallel\mathcal{R}_{h,{t - h - 1}}\parallel \right._{op}^{2}\sigma_{w}^{2}} \leq {\left. \parallel C_{\star},A_{\star}\parallel \right._{\mathcal{H}_{\infty}}^{2}\sigma_{w}^{2}}$-sub-Gaussian. We then apply this argument to the other terms in $e_{t}$ and conclude that $e_{t}$ is $\sigma_{e}^{2}$-sub-Guassian for

We stress that this argument is only valid when $A_{\star}$ is stable, otherwise $e_{t}$ is unbounded. With this in mind, we express the OLS estimate as

where $\Lambda_{\tau} = {\sum_{t}{z_{t}z_{t}^{\top}}}$.

In \[(https://arxiv.org/html/2404.08120v1#bib.bib17)\], it was shown that from a trajectory of length $T$, the OLS estimate $\hat{G}$ satisfies $\left. \parallel{\hat{G} - G_{\star}}\parallel \right._{op} \leq {\mathcal{O}\left( \sqrt{{h{({d_{x} + d_{u}})}}/T} \right)}$. This bound contains polynomial dependency on the horizon length $h$ and system dimensions $d_{x},d_{u}$ because the size of the Markov parameter $G_{\star}$ grows with these quantities. In contrast, this work assumes some prior knowledge that the true parameters comes from a finite set and therefore we proceed to present a least-squares-based approach that yields dimension-independent guarantees.

### System identification from a finite collection

We first note that certain collections of candidate models are more difficult to identify than others. In particular, more samples would be needed if the collection has a system $(C,A,B)$ whose Markov parameter $G$ is very close to the ground truth $G_{\star}$. Thus, we need to quantify how far apart are the models in the given collection in terms of their Markov parameters:

### Assumption 1

For all $1 \leq i < j \leq N$, the Markov parameters in the collection satisfy $\left. \parallel{G_{i} - G_{j}}\parallel \right._{op} \geq {2\gamma}$.

The candidate models would be closer to each other for a smaller value of $\gamma$, which would in turn be harder to distinguish. Under this assumption, any two candidate models within the collection only need to have different responses to just one input sequence. Hence, it suffices to come up with estimates that are accurate only respect to these inputs, contrasting to earlier results where the estimation error are uniformly bounded.

As a direct implication of this assumption, for each $1 \leq i < j \leq N$, there exist unit vectors $u_{ij},v_{ij}$ so that ${|{u_{ij}^{\top}{({G_{i} - G_{j}})}v_{ij}}|} \geq {2\gamma}$. We call these the critical directions of the collection. It follows that, if an OLS estimate $\hat{G}$ satisfies ${|{u_{ij}^{\top}{({\hat{G} - G_{\star}})}v_{ij}}|} < \gamma$ for all $(i,j)$, then the candidate model that is closest to $\hat{G}$ along the critical directions is the ground truth. This implies that it suffices to find a coarser OLS estimate $\hat{G}$ that is close to the true parameter $G_{\star}$ in only $\binom{N}{2}$ directions. We implement this idea as follows:

1:Input: collection of models {Gi}i = 1N and critical directions {(uij, vij}i &lt; j.
2:Input: Data with τ samples {(yH + 1,zH + 1), (yH + 2,zH + 2), …, (yH + τ,zH + τ)}.
3:Compute OLS estimate Ĝ using.
6: if |uij⊤(Gi−Ĝ)vij| ≤ |uij⊤(Gj−Ĝ)vij| then
7: i ← j ⊳ jth model is closer to the estimated Ĝ
Algorithm 1 Linear system model identification with OLS

We note that whenever the OLS estimate $\hat{G}$ is accurate along the critical dimensions, the final output given by Algorithm (https://arxiv.org/html/2404.08120v1#alg1 "Algorithm 1 ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") must be the index of the correct model, because every other model was shown to not be the closest to $\hat{G}$ along one of the critical directions. In the following bound, we state the sample complexity of Algorithm (https://arxiv.org/html/2404.08120v1#alg1 "Algorithm 1 ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") to identify the correct model with high probability.

### Proposition 4

Given an exploratory input $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I_{d_{u} \times d_{u}}})}}$, there exists a time $\tau \leq {\frac{\sigma_{e}^{2} + \sigma_{\eta}^{2}}{\sigma_{u}^{2}\gamma^{2}}{\log\left( \frac{N^{2}}{\delta} \right)}}$, where the inequality holds up to some absolute constants, so that Algorithm (https://arxiv.org/html/2404.08120v1#alg1 "Algorithm 1 ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") outputs the correct model with probability $1 - \delta$.

To interpret this bound, we note that the required number of samples scales quadratically with respect to the "fineness" $\gamma$ of the collection. Also, $\sigma_{e}^{2} + \sigma_{\eta}^{2}$ is the magnitude of the residuals and $\sigma_{u}^{2}$ is the magnitude of our exploratory inputs, so the quantity $\frac{\sigma_{e}^{2} + \sigma_{\eta}^{2}}{\sigma_{u}^{2}}$ corresponds to the inverse of the signal-to-noise ratio of the system. In particular, this explains that OLS fails to identify unstable linear systems because in such cases, the signal-to-noise ratio would be arbitrarily low due to unbounded $\sigma_{e}$. Finally, the bound only scales logarithmically with respect to $N$, and so the size of the candidate of the collection do not significantly affect the efficacy of our least-square-based method.

### Proof sketch

Firstly, we can write the estimation error $\hat{G} - G_{\star}$ purely in terms of the residues $r_{t}:={y_{t} - {G_{\star}z_{t}}}$'s, inputs $z_{t}$'s and the covariance matrix $\Lambda_{t}$:

Then, for any fixed critical direction $(u,v)$, we apply the self-normalized tail bound (Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem1 "Proposition 1 (Theorem 1 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control")) on the quantity $u^{\top}{({\hat{G} - G_{\star}})}v$ so that,

with probability $1 - \delta$. Next, we want to show persistency of exicitation. In particular, if we can pick some value for $V_{0}$ so that ${{v^{\top}\Lambda_{\tau}v} + V_{0}} \leq {2v^{\top}\Lambda_{\tau}v}$, then we have a bound on $u^{\top}{({\hat{G} - G_{\star}})}v$. To this end, we leverage the block martingale small-ball property (Definition (https://arxiv.org/html/2404.08120v1#Thmdefinition2 "Definition 2 (Definition 2.1 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control")). Because $z_{t}$'s are Guassian, they have a known tail probability and we can show that $v^{\top}z_{t}$ is $(1,\sigma_{u}^{2},{3/10})$-BMSB. After applying Lemma (https://arxiv.org/html/2404.08120v1#Thmtheorem2 "Lemma 2 (Proposition 2.5 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control"), we can show that $v^{\top}\Lambda_{\tau}v$ grows linearly in $\tau$ in the sense that there exists some constant $C$ where ${\Pr{({{v^{\top}\Lambda_{\tau}v} \geq {C\tau}})}} \lesssim {\exp{({- \tau})}}$. These steps lead to a high probability bound on the estimation error along the direction $(u,v)$.

Finally, we conclude the proof by using union bound over the estimation error along every critical direction ${(u_{ij},v_{ij})}_{i < j}$.

A complete proof can be found in Appendix [A](https://arxiv.org/html/2404.08120v1#A1 "Appendix A Proof of Proposition 4 ‣ A least-square method for non-asymptotic identification in linear switching control"). ∎

## Algorithm for identification in switching control

In this section, we return our focus to the setting of linear switching control. Recall that in a switched linear system, we assume the unknown underlying linear dynamics is contained in a finite collection of models ${\{{(C_{i},A_{i},B_{i})}\}}_{i = 1}^{N}$, and for each model there is an associated linear controller giving satisfactory performance. As illustrated in Figure (https://arxiv.org/html/2404.08120v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A least-square method for non-asymptotic identification in linear switching control"), the system $({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})$ represents the closed-loop dynamics when the $j$th controller is applied to the $i$th linear model. Then, switching control seeks to design a switching strategy that stabilizes the system. In this work, we additionally want the switching strategy to yield a finite sample guarantee for identifying the unknown system parameters.

### Summary of estimator-based supervisory control

One popular approach to switching control is the so-called estimator-based supervisory control (see surveys \[(https://arxiv.org/html/2404.08120v1#bib.bib8), (https://arxiv.org/html/2404.08120v1#bib.bib12)\]). At a high-level, this method can be described as follows:

We construct a multi-estimator, where for at each time $t$ and each model $k$, it takes past outputs $y_{t}$ and control inputs $u_{t}$ and makes a prediction $y_{t + 1}^{(k)}$ on the next output as if the true underlying system were the $k$th model.

Given the measured outputs $y_{t}$, we can define the prediction error $\left( {e_{t}^{(k)}:={y_{t} - y_{t}^{(k)}}} \right)_{t > 0}$.

Let $\hat{i}$ be the index that yields the smallest prediction error according to a time-discounted $\ell_{2}$-norm and then we apply the $\hat{i}$th controller.

To avoid switching too frequently, we also set a dwell time so that we must stick with a switching signal for a prescribed amount of time.

In \[(https://arxiv.org/html/2404.08120v1#bib.bib15), (https://arxiv.org/html/2404.08120v1#bib.bib16)\], it was shown that the closed-loop switched system resulted from this switching strategy is asymptotically stable in the sense that the system states would remain bounded in response to bounded disturbance.

We note that when the size of the error sequence $e^{(k)}$'s are instead measured by the $\ell_{2}$-norm without discounting, then this strategy's estimated indexes correspond to the solutions to least-square regression. This observation motivates us to apply Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem4 "Proposition 4. ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") to derive a switching strategy that has non-asymptotic guarantees. However, we do not know if the closed-loop dynamics $({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})$ is actually stable when $i \neq j$. As we discussed in the previous section, on a trajectory generated by an unstable dynamic, we cannot compute any accurate estimates because the signal-to-noise ratio can be arbitrarily low. So, before we can determine whether the closed-loop dynamic is stable, running least-square is as good as random guessing.

### Instability detection

The goal of this section is to derive a precise criterion on whether the current closed-loop dynamics is stable, so we can determine if a controller is destabilizing. As we previously discussed, an unstable partially-observed system would have an arbitrarily low signal-to-noise ratio, which is undesirable for system identification. So, we exploit the fact that the norms of an unstable system's states would grow without bound. Under mild assumptions, if the norms of the output are sufficiently large, then we can confidently say that we are facing an unstable system. Following this intuition, we shall quantify the how explosive are the unstable systems.

### Assumption 2

For any unstable closed-loop dynamics $(C_{i},A_{i}^{(j)},B_{i})$, there exists $\varepsilon_{a} > 0$ so that ${\rho{(A_{i}^{(j)})}} \geq {1 + \varepsilon_{a}}$.

Next, we want to use observability to infer both unstable modes and transient behaviors from past observations. According to the Hautus (PBH) criterion, a system $(C,A)$ is observable if no eigenvector $q$ of $A$ satisfies ${Cq} = 0$. With this in mind, we make the following assumption.

### Assumption 3

We say a system $(C,A)$ is strictly observable if for every eigenvector $q$ satisfies $\left. \parallel{Cq}\parallel \right. \geq {\varepsilon_{c}\left. \parallel q\parallel \right.}$. Then, for all ${(i,j)} \in {\lbrack N\rbrack}^{2}$, $({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})$ is strictly observable.

### Remark 1

As a consequence of the Jordan decomposition of $A$, our formulation of strict observability implies the more common definition that ${\sigma_{\min}{({\lbrack C;{CA};\ldots;{CA^{d_{x} - 1}}\rbrack})}} \geq \varepsilon_{c}$. To see this, we consider an orthonormal basis $\mathcal{B}$ consisting of $A$'s generalized eigenvectors. Suppose a basis vector $q \in \mathcal{B}$ is an generalized eigenvector of order $k \leq d_{x}$ and let $q^{\prime}$ be the unit eigenvector from the same Jordan block. Then, $\left\langle q^{\prime},{A^{k - 1}q} \right\rangle = 1$, and from strict observability, we have

Then, for a general vector $v$, we consider its decomposition along this basis and conclude that

These two assumptions together imply that the outputs from an unstable system would be explosive. In the following result, we employ a threshold ((https://arxiv.org/html/2404.08120v1#S4.E3 "3 ‣ Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control")) corresponding to a high probability bound on the $\ell_{2}$-norm of the outputs $y_{t}$ coming from a stable system. Then, we claim that after a sufficient amount of time, the norms of the outputs exceed this threshold if and only if the dynamics are unstable.

### Proposition 5

Consider a linear dynamics $(C^{\prime},A^{\prime},B^{\prime})$ belonging to some finite family $\mathcal{S}$. Let the input be $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I_{d_{u} \times d_{u}}})}}$. Define

where $P$ is the solution to the Lyapunov equation with respect to $(C,A)$. Then, each of the following holds with probability $1 - \delta$:

If the matrix $A^{\prime}$ is stable and $M \geq {x_{1}^{\top}Px_{1}}$ over all stable dynamics in $\mathcal{S}$, then ${\sum_{t = 1}^{\tau}\left. \parallel y_{t}\parallel \right.^{2}} \leq {\xi{(M,\tau,\delta)}}$ for any $\tau > 0$.

If the matrix $A^{\prime}$ is unstable, then ${\sum_{t = 1}^{\tau}\left. \parallel y_{t}\parallel \right.^{2}} \geq {2\xi{(M,\tau,\delta)}}$ for some $\tau \lesssim {\log{({{({{\log{({1/\delta})}} + M})}/\delta})}}$, where the constants have only logarithmic dependency on the dimensions.

We note that the quantity $M$ serves as a bound on the size of the transient. And the threshold in ((https://arxiv.org/html/2404.08120v1#S4.E3 "3 ‣ Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control")) in fact is the finite-time input-to-output gain of a stable system. Therefore, a stable system would not produce outputs that exceed this threshold, whereas the outputs of an unstable system would exceed this threshold after sufficiently large time $\tau$ due to their explosive nature.

### Proof sketch

The first condition follows from direct computation. Specifically, let $\lbrack w_{\lbrack{t - 1}\rbrack};u_{\lbrack{t - 1}\rbrack};\eta_{\lbrack t\rbrack}\rbrack$ be the vector of noises before time $t$. Then, the norms of the output $\sum_{s = 1}^{t}\left. \parallel y_{s}\parallel \right.^{2}$ can be expressed in terms of a quadratic form

where $\Sigma_{1}$ and $\Sigma_{2}$ are positive definite matrices whose blocks consist of submatrices from the Toeplitz operator ((https://arxiv.org/html/2404.08120v1#S3.E1 "1 ‣ 3.1 Problem setup ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control")). We can bound the trace of $\Sigma_{1}$ and $\Sigma_{2}$, and then apply the Hanson-Wright inequality (Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem3 "Proposition 3 (Corollary 6 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control")). To interpret the threshold in ((https://arxiv.org/html/2404.08120v1#S4.E3 "3 ‣ Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control")), we note that the quantity $M$ corresponds to an upper bound on the transient and the second term in ((https://arxiv.org/html/2404.08120v1#S4.E3 "3 ‣ Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control")) corresponds to the steady state response to the process noise and control inputs.

As for the second condition, we note that due to strong observability, the long-term contribution from the process noise $CA^{t}w_{1}$ should grow on the order of ${({1 + \varepsilon_{a}})}^{t}$. Then, we can use this observation to show that $y_{t}$ in fact satisfies the BMSB property (Definition (https://arxiv.org/html/2404.08120v1#Thmdefinition2 "Definition 2 (Definition 2.1 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control")) with a sufficiently large choice of $\tau$. So, the quantity $\frac{1}{\tau}{\sum_{t = 1}^{\tau}\left. \parallel y_{t}\parallel \right.^{2}}$ scales with $\exp{(\tau)}$ with high probability. Taking logarithm on both sides yields the desired conclusion.

A complete proof can be found in Appendix [B](https://arxiv.org/html/2404.08120v1#A2 "Appendix B Proof of Proposition 5 ‣ A least-square method for non-asymptotic identification in linear switching control"). ∎

As a quick example, we consider the case where $x_{1} = 0$ and $M_{1} = 0$. Then, Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control") implies that after some time $\tau \in {\mathcal{O}\left( {{\log{({1/\delta})}} + {\log{\log{({1/\delta})}}}} \right)}$, we can tell if the closed-loop dynamics is stable or not. If we find that we are currently in a stable system, then we can apply the OLS estimation as described in Algorithm (https://arxiv.org/html/2404.08120v1#alg1 "Algorithm 1 ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") to determine the true underlying dynamic and apply its corresponding controller for the most desirable performance.

### Main algorithm and guarantees

With Propositions (https://arxiv.org/html/2404.08120v1#Thmtheorem4 "Proposition 4. ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") and (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control") in mind, we present our algorithm for switching control that would find the correct model in finite time.

1:Input: list of dynamics $\mathcal{S} = {\{{\{{({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})}\}}_{i = 1}^{N}\}}_{j = 1}^{N}$.
2:Input: dwell time τ1, …, τN, and τf.
3:Input: upper bound on transients M1, …, Mτ.
4:We apply exploratory input ut ∼ 𝒩(0,σu2Idu × du).
6: Apply jth controller for up to τj steps.
7: if the closed-loop system is stable according to with confidence $1 - \frac{\delta}{2N}$. then
8: Wait for 𝒪(τ1+⋯+τi − 1) steps.
9: Observe for τf more steps.
10: Invoke Algorithm 1 over the collection {(Ci,Ai(j),Bi)}i = 1N with confidence 1 − δ/2.
11: return output of Algorithm 1
Algorithm 2 System identification for switched linear system

Firstly, on line 4, we use an exploratory input $u_{t}$ (which we provisioned in Figure (https://arxiv.org/html/2404.08120v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A least-square method for non-asymptotic identification in linear switching control")) to maintain persistency of excitation. Then, this algorithm works in two stages. First, on lines 5 -- 7, because the outputs from an unstable dynamics have very little value for learning, we iterate over the list of candidate controllers in some pre-determined order (according to their indexes) and certify their stability with Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"). Once we find a controller that leads to a stable closed-loop dynamics, then the results in Section (https://arxiv.org/html/2404.08120v1#S3 "3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") are applicable. Then, on lines 9 -- 11, we roll out a trajectory with the current stable closed-loop system and apply least-square estimation over the set of possible closed-loop dynamics to recover the unknown system parameters.

Before we present the main sample complexity bound for Algorithm (https://arxiv.org/html/2404.08120v1#alg2 "Algorithm 2 ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), we first discuss the distinct choices of time $\tau_{j}$ that we must commit to the $j$th controller. Recall that the instability detection criterion ((https://arxiv.org/html/2404.08120v1#S4.E3 "3 ‣ Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control")) has two parts: an upper bound on the transient, and the steady-state input-to-output gain from the process and input noises. The first part depends on the quantity $M$ upper bounding the transient that we must pre-compute. However, because the controllers may be destabilizing, the internal states of the system are explosive as we apply a greater number of controllers, which leads to larger transients following successive switches. Therefore, we need to choose $M_{j}$ that grows with $j$, which in turn requires larger values of $\tau_{j}$ in order to satisfy the conditions of Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control").

### Theorem 6

We are given appropriate choices on $\tau_{f}$ according to Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem4 "Proposition 4. ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") and $\tau_{j} = {\overset{\sim}{\mathcal{O}}\left( {{j \cdot d_{x}} + {{\log{({1/\delta})}}d_{x}}} \right)}$. Then, with probability $1 - \delta$, Algorithm (https://arxiv.org/html/2404.08120v1#alg2 "Algorithm 2 ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control") identifies the unknown true system parameters $(C_{\star},A_{\star},B_{\star})$ in

steps, where the ignored constants have only logarithmic dependency on the system dimensions.

There are two components to the sample complexity guarantee in ((https://arxiv.org/html/2404.08120v1#S4.E4 "4 ‣ Theorem 6. ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control")). The first part is a dimension-dependent term on the time we must take to reject the "bad" controllers that are destabilizing. The second part is a dimension-independent sample complexity guarantee on learning the unknown parameters from a stable closed-loop trajectory. We note that, due to the difficulty in leveraging data produced by an unstable dynamics, our bounds on $M_{j}$ are very conservative. This in turn leads to polynomial dependency on both the dimensions and the number of candidate models in the first part of our sample complexity bound.

### Proof sketch

To analyze Algorithm (https://arxiv.org/html/2404.08120v1#alg2 "Algorithm 2 ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), we need to provide upper bound $M_{j}$ over the transient $\max{x_{t_{j}}^{\top}Px_{t_{j}}}$, where we denote $t_{j}$ as the step when the $j$th controller is first applied to the system, and the maximization is taken over all $P$'s that are the solutions to the Lyapunov equations of ${{{(C_{i},A_{i}^{(j)})},i} = 1},{\ldots,N}$. Finding a suitable $M_{1}$ is straight-forward, as we recall that $x_{1} \sim {\mathcal{N}{(0,I_{d_{x} \times d_{x}})}}$, and by Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem3 "Proposition 3 (Corollary 6 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control"), for any positive definite $P$, ${x_{1}^{\top}Px_{1}} \leq {5tr{(P)}{\log{({1/\delta})}}}$ with probability $1 - \delta$. But for subsequent $t_{j}$'s, the magnitudes of the states $x_{t_{j}}$'s may grow exponentially quickly as the previous controllers we applied are all destabilizing. Nevertheless, using observability, we can carefully bound $x_{t_{j}}$'s using the past $d_{x}$ outputs before time $t_{j}$. Note that, if we ensure that $\tau_{j - 1} \geq d_{x}$, we have

Following a similar direct computation as the first part of Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), we can write the quantity

in terms of a quadratic form over $x_{t_{j} - d_{x}}$ and noise terms. After applying Hanson-Wright (Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem3 "Proposition 3 (Corollary 6 in ). ‣ 2 Mathematical Preliminaries ‣ A least-square method for non-asymptotic identification in linear switching control")) and the strict observability property, $\left. \parallel x_{t_{j} - d_{x}}\parallel \right.^{2}$ can be upper bounded in terms of $Y$. It is worth noting that the constants in this proof are necessarily looser than those of the first part of Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control") because the dynamics are unstable. Furthermore, we have $\left. \parallel x_{t_{j}}\parallel \right.^{2} \lesssim {{\exp{(d_{x})}}\left. \parallel x_{t_{j} - d_{x}}\parallel \right.^{2}}$. It follows that, through an induction argument, we can carefully pick the values of $M_{j} \lesssim {{\exp{(d_{x})}}M_{j - 1}}$. Finally, through a union bound over all $N$ phases, we can bound the number of steps required to detect those destabilizing controllers.

Once we find a stabilizing controller, we can leverage our results in Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem4 "Proposition 4. ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control"). Then, from the current stable closed-loop dynamics, we collect a trajectory whose length is dimension independent and use Algorithm (https://arxiv.org/html/2404.08120v1#alg1 "Algorithm 1 ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") to identify the unknown system parameters.

A complete proof can be found in Appendix [C](https://arxiv.org/html/2404.08120v1#A3 "Appendix C Proof of Theorem 6 ‣ A least-square method for non-asymptotic identification in linear switching control") ∎

### Implications for estimator-based supervisory control

In this section, we discuss the implications of our results for estimator-based supervisory control \[(https://arxiv.org/html/2404.08120v1#bib.bib8), (https://arxiv.org/html/2404.08120v1#bib.bib12)\].

First, we note that our approach is conceptually quite similar to the estimator-based supervisory control, in that both approaches attempt to determine the model that best describes the unknown system by minimizing the squared-norm of the candidate models' one-step prediction errors against the observed outputs. But one major difference is that our approach contains an exploratory and noisy input to ensure persistency of excitation. This enables us to derive a non-asymptotic sample complexity bound that precisely determines the number of steps we need to take for our least-square estimate to recover the system parameters. In contrast, the estimator-based supervisory control may not converge to the index of the true model, and thus cannot be used for identification.

Regarding the sample complexity bounds, in Algorithm (https://arxiv.org/html/2404.08120v1#alg2 "Algorithm 2 ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), the times $\tau_{1},{\ldots\tau_{N}}$ and $\tau_{f}$ correspond to the amount of data we must collect to satisfy the conditions of Propositions (https://arxiv.org/html/2404.08120v1#Thmtheorem4 "Proposition 4. ‣ 3.2 System identification from a finite collection ‣ 3 Linear System Identification ‣ A least-square method for non-asymptotic identification in linear switching control") and (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"), so that we can learn the model index from the data. One can view these time values as a precise characterization of dwell time \[(https://arxiv.org/html/2404.08120v1#bib.bib15)\]. Under the settings of estimator-based supervisory control, the dwell time is the minimal time interval the switching strategy must commit to a controller before being allowed to switch again. This dwell time constraint was originally imposed to avoid chattering, but our finite-time analysis endows this quantity with a precise statistical meaning.

Finally, our analysis of instability detection reveals the important role of transient behaviors of the system. As we previously discussed, the internal states of the system suffer explosive growth from consecutive applications of destabilizing controllers. Every time there is a switch to a new controller, the past system states introduce a transient effect onto the current closed-loop dynamics. Because the transient would affect the signal-to-noise ratio of the output, it would therefore affect our ability to learn from the data, which results in an increase in the sequence of $\tau_{j}$'s in Algorithm (https://arxiv.org/html/2404.08120v1#alg2 "Algorithm 2 ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"). In particular, our bound in Theorem (https://arxiv.org/html/2404.08120v1#Thmtheorem6 "Theorem 6. ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control") indicates that the difficulty in controlling the transient behaviors represent the dominating factor in the sample complexity of Algorithm (https://arxiv.org/html/2404.08120v1#alg2 "Algorithm 2 ‣ 4.3 Main algorithm and guarantees ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control"). On the other hand, due to the asymptotic nature of their analysis, existing results on estimator-based supervisory do not take transient terms into account. One possible solution to this issue would be to use candidate controllers with certain robustness properties so that we are less likely to encounter mismatched pairs of open-loop models and controllers that lead to unstable closed-loop dynamics.

## Conclusion

In this paper, we study the problem of non-asymptotic system identification in the context of linear switching control. We derive a data-driven approach by leveraging ideas from both non-asymptotic system identification and switching control. In particular, our algorithm works in two stages:

We reject any controller that is destabilizing the underlying open-loop dynamics by comparing the observations with our explicit bound on the input-to-output gain of stable systems

Once we certify the stability of closed-loop dynamics, we provide a sharp analysis of system identification that takes into consideration our knowledge of the collection of candidate models.

These ingredients lead to a non-asymptotic guarantee on the sample complexity for learning the unknown system parameters. From our main results, we reveal new implications on the classical estimator-based supervisory control, particularly regarding to a more precise characterization of the notion of dwell times and the effects of transient behaviors from switching.

Finally, one future research direction is to derive non-asymptotic guarantees for system identification in nonlinear switching control. Compared to the linear case, the results on the non-asymptotic analysis of nonlinear system identification are significantly more limited. While it is known that similar guarantees hold for applying ordinary least squares to fully-observed nonlinear systems \[(https://arxiv.org/html/2404.08120v1#bib.bib29)\], the partially-observed setting is still an open problem to the best of our knowledge. Furthermore, translating our Proposition (https://arxiv.org/html/2404.08120v1#Thmtheorem5 "Proposition 5. ‣ 4.2 Instability detection ‣ 4 Algorithm for identification in switching control ‣ A least-square method for non-asymptotic identification in linear switching control") to a nonlinear version seems to be quite difficult because we cannot easily write the outputs purely in terms of the inputs and noise. So, there many potential works remain in extending the results of this paper to the nonlinear setting.
