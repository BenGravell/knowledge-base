<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Least-square Method for Non-asymptotic Identification in Linear Switching Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The focus of this paper is on linear system identification in the setting where it is known that the underlying partially-observed linear dynamical system lies within a finite collection of known candidate models. We first consider the problem of identification from a given trajectory, which in this setting reduces to identifying the index of the true model with high probability. We characterize the finite-time sample complexity of this problem by leveraging recent advances in the non-asymptotic analysis of linear least-square methods in the literature. In comparison to the earlier results that assume no prior knowledge of the system, our approach takes advantage of the smaller hypothesis class and leads to the design of a learner with a dimension-free sample complexity bound. Next, we consider the switching control of linear systems, where there is a candidate controller for each of the candidate models and data is collected through interaction of the system with a collection of potentially destabilizing controllers. We develop a dimension-dependent criterion that can detect those destabilizing controllers in finite time. By leveraging these results, we propose a data-driven switching strategy that identifies the unknown parameters of the underlying system.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We then provide a non-asymptotic analysis of its performance and discuss its implications on the classical method of estimator-based supervisory control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification --- the problem of estimating the parameters of an unknown dynamical system from a single trajectory of input/output data --- plays an important role in many problem domains such as control theory, robotics, and reinforcement learning. There has been tremendous progress in analyzing the performance of various system identification schemes --- classical results showed asymptotic convergence, whereas recent advances in non-asymptotic theory quantified the sample complexity of learning accurate estimates from data. However, these works all narrowly focus on system identification itself without accounting for the requirements for control applications. In this work, we consider a problem setting where linear system identification meets switching control so that we develop a data-driven approach to simultaneously achieve desirable control and system identification objectives.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We assume that the initial state $x_{1} \sim {\mathcal{N}{(0,I_{d_{x} \times d_{x}})}}$, process noise $w_{t} \sim {\mathcal{N}{(0,{\sigma_{w}^{2}I_{d_{x} \times d_{x}}})}}$, and observation noise $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{\eta}^{2}I_{d_{y} \times d_{y}}})}}$ come from Gaussian distributions. In many complex systems, e.g. power systems, autonomous vehicles, and public health, it is not practical to design a single controller that achieves satisfactory performance for all candidate models in the collection. To this end, in a linear switched system, each candidate model has an associated linear controller giving satisfactory performance on this model. We also note that a mismatched pair of a model and a controller can result in an unstable closed-loop system.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following the convention of, we use the multi-controller framework $K{(p_{t};{\check{x}}_{t},y_{t})}$, where ${\check{x}}_{t}$ is the internal state of the controller, $p_{t} \in {\lbrack N\rbrack}$ is the piece-wise constant switching signal that determines which candidate linear controller is applied, and $y_{t}$ is the system's output. And for reasons that will be discussed later, we keep an input signal $u_{t}$ that is equal to an additive control action on top of the multi-controller.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As illustrated in Figure 1, with an open-loop system $(C,A,B)$ and a fixed switching signal $p_{t} = j$, the closed-loop system becomes $(\overset{\sim}{C},{\overset{\sim}{A}}^{(j)},\overset{\sim}{B})$, where ${\overset{\sim}{A}}^{(j)}$ encapsulates both the dynamics $(C,A,B)$ and the controller $K{(i; \cdot )}$ and $\overset{\sim}{C},\overset{\sim}{B}$ only depend on $C,B$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Then, the set of all possible closed-loop dynamics is ${\{{\{{({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})}\}}_{i = 1}^{N}\}}_{j = 1}^{N}$ and can be pre-computed. Our goal is then to design a switching strategy that collects the data necessary for identifying the true open-loop parameters $(C_{\star},A_{\star},B_{\star})$ and comes with non-asymptotic performance guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fortunately, there has been extensive work on leveraging the particular properties of switched systems. Among the existing literature, one popular switching strategy that shares many similarities to our problem setup is the so-called estimator-based supervisory control (see the surveys ). The estimator-based supervisory control scheme periodically picks the candidate model that most closely matches the observations and applies its associated controller. While it has been shown that this strategy asymptotically stabilizes the switched system, there are no non-asymptotic guarantees for its performance. So, we lack a precise characterization of how long this method may take to converge to satisfactory performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we focus on the interplay of these two threads of work and derive a novel approach to the study of non-asymptotic system identification in switching control. To this end, we make the following technical contributions: In Section 3, we present a least-square-based method for linear model identification with prior knowledge that the ground truth is contained in a finite collection of candidate models. Under this setting, we derive a sample complexity bound that is dimension-free.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

In Section 4.2, we establish an instability detection criterion by quantitatively bounding the finite-time input-to-output gain of a stable linear system. This allows us to detect any explosive closed-loop dynamics and remove any controllers that are destabilizing the switched system.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

Most importantly, in Section 4.3, we present a data-driven algorithm for linear system identification problems in switching control. We derive a sample complexity bound on the number of steps for which our strategy finds the correct model with high probability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

In Section 4.4, we compare our approach to the classical method of estimator-based supervisory control and discuss the implications of our non-asymptotic guarantees to the problem of switching control.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations", "weight": 1.0} -->

For a matrix $M$, we denote $\left. \parallel M\parallel \right._{F}$ as its Frobenius norm, $\left. \parallel M\parallel \right._{op} = {\sigma_{\max}{(M)}}$ as its operator norm (equivalently, its largest singular value), $\rho{(M)}$ as its spectral radius, and ${tr}{(M)}$ as its trace. For a stable linear system $(C,A,B)$, we define its $\mathcal{H}$-infinity norm as $\left. \parallel C,A,B\parallel \right._{\mathcal{H}_{\infty}} = {\sup_{{\parallel s\parallel} = 1}{\sigma_{\max}{({C{({{sI} - A})}^{- 1}B})}}}$, and for simplicity, we use shorthand $\left.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Notations", "weight": 1.0} -->

\parallel C,A\parallel \right._{\mathcal{H}_{\infty}} = \left. \parallel C,A,I\parallel \right._{\mathcal{H}_{\infty}}$ and $\left. \parallel A\parallel \right._{\mathcal{H}_{\infty}} = \left. \parallel I,A,I\parallel \right._{\mathcal{H}_{\infty}}$. We also define $P{(C,A)}$ as the solution to the Lyapunov equation ${{{A^{\top}PA} - P} + {C^{\top}C}} = 0$, and we simply write $P$ when parameters $(C,A)$ are clear from the context.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Notations", "weight": 1.0} -->

To simplify our exposition, we sometimes ignore constant factors that do not meaningfully contribute to our conclusions. We define the big-O notation as $f \in {\mathcal{O}(g)}$ if ${\operatorname{lim\ sup}_{x\rightarrow\infty}{{{f{(x)}}/g}{(x)}}} < \infty$ and $f \in {\overset{\sim}{\mathcal{O}}(g)}$ if $f \in {\mathcal{O}\left( {{polylog}{( \cdot )}g{( \cdot )}} \right)}$. Lastly, we write $f \lesssim g$ if $f \leq {c \cdot g}$ for some universal constant $c$. Unless otherwise stated, we will explicitly write out any terms dependent on the problem dimensions. In particular, we consider the Frobenius norm and the trace of a matrix to be dimension-dependent, but the operator norm is not.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Switching control has been studied extensively over the years. Among the existing literature, there are two popular approaches to designing performant switching policies --- estimator-based supervision that picks the candidate model that most closely resembles the observed process, and performance-based falsification through some stability certificate. In this paper, we shall highlight the estimator-based supervision method. This approach was first formalized in the setting of continuous-time linear switched systems and was later extended to nonlinear models, and for discrete-time models. However, all of the works above only provide asymptotic guarantees for their methods.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Literature Review", "weight": 1.0} -->

The methods of non-asymptotic linear system identification have seen significant progress with modern tools from statistical learning. In the case of a fully-observed linear model, showed that for stable systems, ordinary least square (OLS) achieves estimation error on the order of $\sqrt{T}$, where $T$ is the length of the sample trajectory. And for unstable linear systems, showed that the OLS estimate may be inconsistent. Much of the same machinery can be applied to partially-observed stable linear systems, e.g.. Beyond system identification problems, these methods have been applied to problems such as online LQR and latent state learning. A summary of the recent advances in this field can be found.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Finally, there are some recent works on applying online learning to switching control. For example, considers a switched system with fully-observed non-linear models and, inspired by online bandit algorithms, proposes an approach that optimizes for some quadratic cost functions. We note that the setting of this work differs significantly from ours --- our method applies to partially-observed systems and our ultimate objective is identification so that we do not require access to cost functions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Mathematical Preliminaries", "weight": 1.0} -->

Before we dive into the technical results, we shall briefly introduce some tools from probability and learning theory that are key to our derivations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Mathematical Preliminaries", "weight": 1.0} -->

We first define a generalization of Gaussian random variables. Roughly speaking, a sub-Gaussian random variable has tail concentration that is dominated by a Gaussian distribution.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Linear System Identification", "weight": 1.0} -->

In this section, we first focus our efforts on system identification. Specifically, under any constant switching signal $p_{t} = j$, we identify the index of the true system in the set of possible closed-loop dynamics ${\{{({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})}\}}_{i = 1}^{N}$, which corresponds to the dashed box in Figure 1. We can then use this index to recover the true parameters of the unknown system. We stress that the techniques below are applicable to general partially-observed linear systems. So, in this section, we skip the distinctions between the open-loop vs. closed-loop systems and drop the superscript $\sim$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem setup", "weight": 1.0} -->

Additionally, only for this section, we assume that $A_{\star}$ is stable in the sense that ${\rho{(A_{\star})}} < 1$. This assumption is standard in the literature of non-asymptotic linear system identification. For fully-observed linear systems, gave an example of an unstable linear system that a least-square estimator fails to identify its unknown parameters. And for the partially-observed setting, as we shall see, it is not possible to bound the residual noise terms when the system is unstable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem setup", "weight": 1.0} -->

There has been a considerable amount of work for the no-prior case where the values of the matrices $(C_{\star},A_{\star},B_{\star})$ can be arbitrary (as long as $A_{\star}$ is stable), e.g.. The common approach is to use an exploratory Gaussian noise as the input $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I_{d_{u} \times d_{u}}})}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem setup", "weight": 1.0} -->

Then, we use the system's observed response $y_{t}$ to the sequence of past $h$ Gaussian inputs $z_{t}:={(u_{t - 1},u_{t - 2},\ldots,u_{t - h})}$ to estimate a Markov parameter that is equal to the system's output controllability matrix with time horizon of length $h$: Before we apply ordinary least squares (OLS) to estimate the Markov parameter, we first recursively write out the dynamics: Next, we can show that the random vector $e_{t} = {{C_{\star}A_{\star}^{H}x_{t - H}} + {\sum_{j = 1}^{H}{C_{\star}A_{\star}^{j - 1}w_{t - j}}}}$ is sub-Gaussian.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem setup", "weight": 1.0} -->

In, it was shown that from a trajectory of length $T$, the OLS estimate $\hat{G}$ satisfies $\left. \parallel{\hat{G} - G_{\star}}\parallel \right._{op} \leq {\mathcal{O}\left( \sqrt{{h{({d_{x} + d_{u}})}}/T} \right)}$. This bound contains polynomial dependency on the horizon length $h$ and system dimensions $d_{x},d_{u}$ because the size of the Markov parameter $G_{\star}$ grows with these quantities. In contrast, this work assumes some prior knowledge that the true parameters comes from a finite set and therefore we proceed to present a least-squares-based approach that yields dimension-independent guarantees.

<!-- chunk {"id": "body-0027", "role": "body", "section": "System identification from a finite collection", "weight": 1.0} -->

We first note that certain collections of candidate models are more difficult to identify than others. In particular, more samples would be needed if the collection has a system $(C,A,B)$ whose Markov parameter $G$ is very close to the ground truth $G_{\star}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For all $1 \leq i < j \leq N$, the Markov parameters in the collection satisfy $\left. \parallel{G_{i} - G_{j}}\parallel \right._{op} \geq {2\gamma}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The candidate models would be closer to each other for a smaller value of $\gamma$, which would in turn be harder to distinguish. Under this assumption, any two candidate models within the collection only need to have different responses to just one input sequence. Hence, it suffices to come up with estimates that are accurate only respect to these inputs, contrasting to earlier results where the estimation error are uniformly bounded.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

As a direct implication of this assumption, for each $1 \leq i < j \leq N$, there exist unit vectors $u_{ij},v_{ij}$ so that ${|{u_{ij}^{\top}{({G_{i} - G_{j}})}v_{ij}}|} \geq {2\gamma}$. We call these the critical directions of the collection. It follows that, if an OLS estimate $\hat{G}$ satisfies ${|{u_{ij}^{\top}{({\hat{G} - G_{\star}})}v_{ij}}|} < \gamma$ for all $(i,j)$, then the candidate model that is closest to $\hat{G}$ along the critical directions is the ground truth.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

This implies that it suffices to find a coarser OLS estimate $\hat{G}$ that is close to the true parameter $G_{\star}$ in only $\binom{N}{2}$ directions. We implement this idea as follows: 1:Input: collection of models {Gi}i = 1N and critical directions {(uij, vij}i < j. 2:Input: Data with τ samples {(yH + 1, zH + 1), (yH + 2, zH + 2), …, (yH + τ, zH + τ)}. 3:Compute OLS estimate Ĝ using.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

6: if |uij⊤(Gi − Ĝ)vij| ≤ |uij⊤(Gj − Ĝ)vij| then 7: i ← j ⊳ jth model is closer to the estimated Ĝ Algorithm 1 Linear system model identification with OLS We note that whenever the OLS estimate $\hat{G}$ is accurate along the critical dimensions, the final output given by Algorithm 1 must be the index of the correct model, because every other model was shown to not be the closest to $\hat{G}$ along one of the critical directions. In the following bound, we state the sample complexity of Algorithm 1 to identify the correct model with high probability.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm for identification in switching control", "weight": 1.0} -->

In this section, we return our focus to the setting of linear switching control. Recall that in a switched linear system, we assume the unknown underlying linear dynamics is contained in a finite collection of models ${\{{(C_{i},A_{i},B_{i})}\}}_{i = 1}^{N}$, and for each model there is an associated linear controller giving satisfactory performance. As illustrated in Figure 1, the system $({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})$ represents the closed-loop dynamics when the $j$th controller is applied to the $i$th linear model. Then, switching control seeks to design a switching strategy that stabilizes the system. In this work, we additionally want the switching strategy to yield a finite sample guarantee for identifying the unknown system parameters.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Summary of estimator-based supervisory control", "weight": 1.0} -->

One popular approach to switching control is the so-called estimator-based supervisory control (see surveys). At a high-level, this method can be described as follows: We construct a multi-estimator, where for at each time $t$ and each model $k$, it takes past outputs $y_{t}$ and control inputs $u_{t}$ and makes a prediction $y_{t + 1}^{(k)}$ on the next output as if the true underlying system were the $k$th model.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Summary of estimator-based supervisory control", "weight": 1.0} -->

Let $\hat{i}$ be the index that yields the smallest prediction error according to a time-discounted $\ell_{2}$-norm and then we apply the $\hat{i}$th controller.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Summary of estimator-based supervisory control", "weight": 1.0} -->

To avoid switching too frequently, we also set a dwell time so that we must stick with a switching signal for a prescribed amount of time.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Summary of estimator-based supervisory control", "weight": 1.0} -->

In, it was shown that the closed-loop switched system resulted from this switching strategy is asymptotically stable in the sense that the system states would remain bounded in response to bounded disturbance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Summary of estimator-based supervisory control", "weight": 1.0} -->

We note that when the size of the error sequence $e^{(k)}$'s are instead measured by the $\ell_{2}$-norm without discounting, then this strategy's estimated indexes correspond to the solutions to least-square regression. This observation motivates us to apply Proposition 4 to derive a switching strategy that has non-asymptotic guarantees. However, we do not know if the closed-loop dynamics $({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})$ is actually stable when $i \neq j$. As we discussed in the previous section, on a trajectory generated by an unstable dynamic, we cannot compute any accurate estimates because the signal-to-noise ratio can be arbitrarily low. So, before we can determine whether the closed-loop dynamic is stable, running least-square is as good as random guessing.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Instability detection", "weight": 1.0} -->

The goal of this section is to derive a precise criterion on whether the current closed-loop dynamics is stable, so we can determine if a controller is destabilizing. As we previously discussed, an unstable partially-observed system would have an arbitrarily low signal-to-noise ratio, which is undesirable for system identification. So, we exploit the fact that the norms of an unstable system's states would grow without bound. Under mild assumptions, if the norms of the output are sufficiently large, then we can confidently say that we are facing an unstable system. Following this intuition, we shall quantify the how explosive are the unstable systems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Next, we want to use observability to infer both unstable modes and transient behaviors from past observations. According to the Hautus (PBH) criterion, a system $(C,A)$ is observable if no eigenvector $q$ of $A$ satisfies ${Cq} = 0$. With this in mind, we make the following assumption.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1", "weight": 1.0} -->

As a consequence of the Jordan decomposition of $A$, our formulation of strict observability implies the more common definition that ${\sigma_{\min}{({\lbrack C;{CA};\ldots;{CA^{d_{x} - 1}}\rbrack})}} \geq \varepsilon_{c}$. To see this, we consider an orthonormal basis $\mathcal{B}$ consisting of $A$'s generalized eigenvectors. Suppose a basis vector $q \in \mathcal{B}$ is an generalized eigenvector of order $k \leq d_{x}$ and let $q'$ be the unit eigenvector from the same Jordan block. Then, $\left\langle q',{A^{k - 1}q} \right\rangle = 1$, and from strict observability, we have Then, for a general vector $v$, we consider its decomposition along this basis and conclude that These two assumptions together imply that the outputs from an unstable system would be explosive.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the following result, we employ a threshold corresponding to a high probability bound on the $\ell_{2}$-norm of the outputs $y_{t}$ coming from a stable system. Then, we claim that after a sufficient amount of time, the norms of the outputs exceed this threshold if and only if the dynamics are unstable.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Main algorithm and guarantees", "weight": 1.0} -->

With Propositions 4 and 5 in mind, we present our algorithm for switching control that would find the correct model in finite time.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Main algorithm and guarantees", "weight": 1.0} -->

1:Input: list of dynamics $\mathcal{S} = {\{{\{{({\overset{\sim}{C}}_{i},{\overset{\sim}{A}}_{i}^{(j)},{\overset{\sim}{B}}_{i})}\}}_{i = 1}^{N}\}}_{j = 1}^{N}$. 2:Input: dwell time τ1, …, τN, and τf. 3:Input: upper bound on transients M1, …, Mτ. 4:We apply exploratory input ut ∼ 𝒩(0, σu2Idu × du). 6: Apply jth controller for up to τj steps. 7: if the closed-loop system is stable according to with confidence $1 - \frac{\delta}{2N}$. then 8: Wait for 𝒪(τ1 + ⋯ + τi − 1) steps. 9: Observe for τf more steps.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Main algorithm and guarantees", "weight": 1.0} -->

10: Invoke Algorithm 1 over the collection {(Ci, Ai(j), Bi)}i = 1N with confidence 1 − δ/2. 11: return output of Algorithm 1 Algorithm 2 System identification for switched linear system Firstly, on line 4, we use an exploratory input $u_{t}$ (which we provisioned in Figure 1) to maintain persistency of excitation. Then, this algorithm works in two stages. First, on lines 5 -- 7, because the outputs from an unstable dynamics have very little value for learning, we iterate over the list of candidate controllers in some pre-determined order (according to their indexes) and certify their stability with Proposition 5. Once we find a controller that leads to a stable closed-loop dynamics, then the results in Section 3 are applicable. Then, on lines 9 -- 11, we roll out a trajectory with the current stable closed-loop system and apply least-square estimation over the set of possible closed-loop dynamics to recover the unknown system parameters.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Main algorithm and guarantees", "weight": 1.0} -->

Before we present the main sample complexity bound for Algorithm 2, we first discuss the distinct choices of time $\tau_{j}$ that we must commit to the $j$th controller. Recall that the instability detection criterion has two parts: an upper bound on the transient, and the steady-state input-to-output gain from the process and input noises. The first part depends on the quantity $M$ upper bounding the transient that we must pre-compute. However, because the controllers may be destabilizing, the internal states of the system are explosive as we apply a greater number of controllers, which leads to larger transients following successive switches. Therefore, we need to choose $M_{j}$ that grows with $j$, which in turn requires larger values of $\tau_{j}$ in order to satisfy the conditions of Proposition 5.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Implications for estimator-based supervisory control", "weight": 1.0} -->

In this section, we discuss the implications of our results for estimator-based supervisory control.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Implications for estimator-based supervisory control", "weight": 1.0} -->

First, we note that our approach is conceptually quite similar to the estimator-based supervisory control, in that both approaches attempt to determine the model that best describes the unknown system by minimizing the squared-norm of the candidate models' one-step prediction errors against the observed outputs. But one major difference is that our approach contains an exploratory and noisy input to ensure persistency of excitation. This enables us to derive a non-asymptotic sample complexity bound that precisely determines the number of steps we need to take for our least-square estimate to recover the system parameters. In contrast, the estimator-based supervisory control may not converge to the index of the true model, and thus cannot be used for identification.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Implications for estimator-based supervisory control", "weight": 1.0} -->

Regarding the sample complexity bounds, in Algorithm 2, the times $\tau_{1},{\ldots\tau_{N}}$ and $\tau_{f}$ correspond to the amount of data we must collect to satisfy the conditions of Propositions 4 and 5, so that we can learn the model index from the data. One can view these time values as a precise characterization of dwell time. Under the settings of estimator-based supervisory control, the dwell time is the minimal time interval the switching strategy must commit to a controller before being allowed to switch again. This dwell time constraint was originally imposed to avoid chattering, but our finite-time analysis endows this quantity with a precise statistical meaning.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Implications for estimator-based supervisory control", "weight": 1.0} -->

Finally, our analysis of instability detection reveals the important role of transient behaviors of the system. As we previously discussed, the internal states of the system suffer explosive growth from consecutive applications of destabilizing controllers. Every time there is a switch to a new controller, the past system states introduce a transient effect onto the current closed-loop dynamics. Because the transient would affect the signal-to-noise ratio of the output, it would therefore affect our ability to learn from the data, which results in an increase in the sequence of $\tau_{j}$'s in Algorithm 2. In particular, our bound in Theorem 6 indicates that the difficulty in controlling the transient behaviors represent the dominating factor in the sample complexity of Algorithm 2. On the other hand, due to the asymptotic nature of their analysis, existing results on estimator-based supervisory do not take transient terms into account. One possible solution to this issue would be to use candidate controllers with certain robustness properties so that we are less likely to encounter mismatched pairs of open-loop models and controllers that lead to unstable closed-loop dynamics.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we study the problem of non-asymptotic system identification in the context of linear switching control. We derive a data-driven approach by leveraging ideas from both non-asymptotic system identification and switching control. In particular, our algorithm works in two stages: We reject any controller that is destabilizing the underlying open-loop dynamics by comparing the observations with our explicit bound on the input-to-output gain of stable systems Once we certify the stability of closed-loop dynamics, we provide a sharp analysis of system identification that takes into consideration our knowledge of the collection of candidate models.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These ingredients lead to a non-asymptotic guarantee on the sample complexity for learning the unknown system parameters. From our main results, we reveal new implications on the classical estimator-based supervisory control, particularly regarding to a more precise characterization of the notion of dwell times and the effects of transient behaviors from switching.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, one future research direction is to derive non-asymptotic guarantees for system identification in nonlinear switching control. Compared to the linear case, the results on the non-asymptotic analysis of nonlinear system identification are significantly more limited. While it is known that similar guarantees hold for applying ordinary least squares to fully-observed nonlinear systems, the partially-observed setting is still an open problem to the best of our knowledge. Furthermore, translating our Proposition 5 to a nonlinear version seems to be quite difficult because we cannot easily write the outputs purely in terms of the inputs and noise. So, there many potential works remain in extending the results of this paper to the nonlinear setting.
