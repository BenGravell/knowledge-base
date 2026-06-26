<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

State Space Models, Emergence, and Ergodicity: How Many Parameters Are Needed for Stable Predictions?

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

How many parameters are required for a model to execute a given task? It has been argued that large language models, pre-trained via self-supervised learning, exhibit emergent capabilities such as multi-step reasoning as their number of parameters reach a critical scale. In the present work, we explore whether this phenomenon can analogously be replicated in a simple theoretical model. We show that the problem of learning linear dynamical systems - a simple instance of self-supervised learning - exhibits a corresponding phase transition. Namely, for every non-ergodic linear system there exists a critical threshold such that a learner using fewer parameters than said threshold cannot achieve bounded error for large sequence lengths. Put differently, in our model we find that tasks exhibiting substantial long-range correlation require a certain critical number of parameters - a phenomenon akin to emergence. We also investigate the role of the learner's parametrization and consider a simple version of a linear dynamical system with hidden state - an imperfectly observed random walk in R. For this situation, we show that there exists no learner using a linear filter which can succesfully learn the random walk unless the filter length exceeds a certain threshold depending on the effective memory length and horizon of the problem.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider a pre-trained large language model (LLM) obtained via self-supervised learning by predicting the next word or token. While the performance on pre-training loss exhibits rather predictable behavior, Wei et al. observe that such models often exhibit a phase transition in their downstream capabilities as the number of trainable parameters (or training FLOPs) reaches a critical scale---they exhibit emergent capabilities such as successful in-context learning. While these models are typically extremely large in terms of their number of parameters, a recent line of work has shown that such behavior can also be recovered in smaller models by considering appropriately simplified tasks. Here, we offer a possible mechanistic explanation for this phenomenon by restricting to a simple class of auto-regressive learning models.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Namely, we point out that certain tasks---or more precisely, predicting in certain generative models---exhibiting long-range correlations and a lack of ergodicity can only be executed successfully once model scale reaches a certain critical threshold. One may think of our result as the bias term in the bias-variance trade-off exhibiting a sharp jump---a phase transition---depending on whether the model class is rich enough to be fully descriptive of this lack of stochastic stability. We illustrate this phenomenon by a simple problem: learning a linear dynamical system. Incidentally, such linear systems are also fundamental building blocks in the increasingly popular state state model architectures for sequence modelling---an alternative to the popular transformer architecture.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here and in the sequel we study generative modelling of tasks $\mathsf{P}_{Z}$ corresponding to distributions over sequences of tokens $Z_{1:T}$. A learner has pre-trained a (compressed) generative model $\mathsf{Q}_{Z}$ using data not necessarily coming from $\mathsf{P}_{Z}$. The performance of such a model $\mathsf{Q}_{Z}$ on a task $\mathsf{P}_{Z}$ will be measured by its divergence from the ground truth: We ask the following question: > Q: Suppose that $\mathsf{Q}$ comes from a parametric hypothesis class. Does there exist a critical threshold in terms of the number parameters such that ${T^{- 1}d_{\mathsf{K}\mathsf{L}}{({\mathsf{P}_{Z} \parallel \mathsf{Q}})}}\rightarrow\infty$ as $T\rightarrow\infty$ unless the parameter count exceeds said threshold?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In other words, we ask whether a given task-hypothesis class combination admits *stable learners*---learners for which the KL-risk does not diverge as the sequence length $T$ becomes long (notice that the normalization $T^{- 1}$ is necessary to avoid trivial behavior for product measures). Our view here is that language, arriving in discrete packages such as articles and books, is non-ergodic when viewed at the package level. In this view, a single book forms a single trajectory of data in which the first word (or token) is the first data point and the last word the last data point. The distribution of words in the beginning of the book (introducing the suspects) may well be quite different from the distribution at the end of the book (who did it?)---there is different meaning to be conveyed.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is our hypothesis that it is exactly this lack of ergodicity that leads to emergent behavior. Our main simplifying assumption in relating non-ergodicity to model complexity is that the task $\mathsf{P}_{Z}$ has a latent state space model representation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

Models of this form are standard in time series prediction tasks and systems modelling, but have also recently been popularized as building blocks in LLMs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

Under 1.1, a version of the maximum entropy principle yields the following. For every nondegenerate distribution $\mathsf{Q}_{Z}$ over $Z_{1:T}$ under 1.1 the following are true: For $Y_{1:T} \sim \mathsf{P}_{Y} = \mathsf{P}_{g^{- 1}{(Z)}}$ then: The Gaussian measure $\mathsf{Q}_{Y}$ with the same mean and covariance as $\mathsf{Q}_{g^{- 1}{(Z)}}$ satisfies The first statement follows by bijection and the second statement is simply observing that Gaussian measures minimize KL subject to constraints on the first two moments. Our next observation is the standard (trivial yet powerful!) equivalence between generative modeling and next-token-prediction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

Otherwise, either the term ${tr}\left({\Sigma_{\mathsf{Q}_{t}}^{- 1}\Sigma_{\mathsf{P}_{t}}} \right)$ grows unbounded (as we will see that $\Sigma_{\mathsf{P}_{t}}$ is well-conditioned in our examples), or the variance of the predictor becomes arbitrarily large. Combining the above we have that It will be convenient to denote By the above reasoning via (1.5)-(1.6), $\ell_{T}$ defined above in (1.7) constitutes a lower bound on the KL-divergence risk (1.1) in which a learner---by picking a hypothesis in $\mathcal{F}$---competes with an adversary selecting a generative model from $\mathcal{P}$. Thus, imposing these additional constraints above, an instantiation of the above question Q becomes as follows.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

> Q': Fix a family of parametric hypothesis classes ${\{\mathcal{F}_{d}\}}_{d \in {\mathbb{N}}}$ and a family of possible generative models $\mathcal{P}$. Does there exist a critical threshold $d_{\star}$ in terms of the number parameters such that > $${T^{- 1}\ell_{T}{(\mathcal{F}_{d},\mathcal{P})}}\rightarrow\infty$$ > as $T\rightarrow\infty$ unless the parameter count exceeds said threshold ($d > d_{\star}$)?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

In the sequel we focus on identifying task-hypothesis pairs ($\mathcal{P}$, ${\{\mathcal{F}_{d}\}}_{d \in {\mathbb{N}}}$) where this divergence occurs. We will think of a task as exhibiting emergent behavior if it admits a nontrivial threshhold $d_{\star}$ mentioned in Q' above.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

Finally, before we proceed let us also remark that there is some degree of necessity to our choice of considering an adversarial model class $\mathcal{P}$ that we use to obtain meaningful lower bounds. To make this concrete, consider a parametric class of distributions $\mathcal{P}$ parametrized by some set of parameters, say $\theta \in \mathcal{P}$. Suppose the generative model corresponds to the parameter $\theta_{\star}$. As long as $\mathcal{F}$ contains this parameter the only lower bound that can be obtained without including the supremum in (1.7) is $0$. In other words, we need to model the fact that the learner does not have access to the parameter a priori. We accomplish this by letting an adversary pick a parameter against which the learner must compete.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contribution", "weight": 1.0} -->

Our contributions can be stated informally as follows.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 2.1", "weight": 1.0} -->

As a byproduct of our analysis, we note in passing that Theorem 4.1 shows that the truncation level used in Tsiamis and Pappas for improper linear system identification cannot be much improved in general. In particular, improper learning with a finite length filter always (unless further constraints are added to the hypothesis class) incurs an extra approximation-theoretically induced logarithmic factor as opposed to the maximum likelihood estimator.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Emergence in Fully Observed Systems", "weight": 1.0} -->

As a first example, let us consider a fully observed state space model. In this case, $C_{\star}$ in (1.1) is simply the identity and $V_{t}$ is identically zero: We consider the setting in which a learner observes the trajectory $X_{1:T}$ and seeks to learn the generative model by recovering $A_{\star}$. We suppose that each $\mathcal{F}_{d}$ is given by a map $A_{d}:{\mathsf{M}\mapsto{\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{X}}}}$ such that ${\mathbf{E}_{\mathsf{Q}}^{t - 1}Y_{t}} = {A{(\theta)}X_{t}}$ where $\mathsf{M}$ is some smooth manifold of dimension $d_{\mathsf{M}}$. In this case the prediction risk becomes

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The spectral radius of $A_{\star}$ is at least unity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

We now show that when the generative model (3.1) is not ergodic---3.1 holds---the risk exhibits a phase transition in how it scales with the trajectory length $T$ as a function of the number of trainable parameters---the dimension of $\mathsf{M}$, $d_{\mathsf{M}}$. In both cases below we abuse notation and write ${\ell_{T}{(\mathsf{M},A_{\star})}} = {\ell_{T}{(\mathsf{M},\mathsf{P}_{\star})}}$ where $\mathsf{P}_{\star}$ is the distribution of $X_{1:T}$ with the parametrizing matrix $A_{\star}$ in the generative model (3.1).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Hidden States and the Role of the Parametrization", "weight": 1.0} -->

In Theorem 3.1 we saw that we require a quadratic amount of parameters in the number of unstable modes. However, this was assuming direct access to the internal system state. If instead the state is hidden, the observations are no longer Markovian and exhibit longer range memory. We will now turn to investigating the appearance of such memory interacts with the potential instability (non-ergodicity) of $A_{\star}$. Let us also restrict attention to hypothesis classes consisting of finite-dimensional filters of the form ${f_{t}{(Y_{1:{t - 1}})}} = {\sum_{k = 1}^{h}{F_{k}Y_{t - k}}}$ for every $t$ (where $F_{k}$ is the decision-variable that does not depend on $t$). Finite memory of this type is present in many popular architectures, including transformers, where it is referred to as the context length. We denote these classes $\mathsf{M}_{h}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Hidden States and the Role of the Parametrization", "weight": 1.0} -->

In this setting, for a fixed integer $h$ and hypothesis $f \in \mathsf{M}_{h}$, with representation $F_{1:h}$, we have that: At this stage it must be pointed out that it is not just the dimensionality of the parametrization that matters but also the parametrization itself. There certainly exists a hypothesis class using no more than $d_{\mathsf{X}}{({d_{\mathsf{X}} + d_{\mathsf{Y}}})}$-many parameters rendering (4.1) null. On the other hand, the dimension of the internal state may be large or not even known a priori in which case it is appropriate to approximate (1.2) by a finite-dimensional filter---the question then becomes: *what is the minimal filter length such that (4.1) remains stable?* The analysis in the sequel passes via the Kalman filter. The next assumption guarantees that this can be represented by a linear time-invariant system.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hidden States and the Role of the Parametrization", "weight": 1.0} -->

The part of the assumption dealing with time-invariance does not meaningfully restrict the generality of our results since the filter parameters convergence to their steady-state values at a super-exponential rate.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The pair ($C,A$) is observable and ${\Sigma_{W},\Sigma_{V}} \succ 0$. Moreover, the covariance of the initial state satisfies $\Sigma_{W_{1}} = \Sigma_{ss}$, where $\Sigma_{ss}$ solves the filter discrete algebraic Riccati equation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have proposed a mechanistic explanation of emergence in a relatively simple class of autoregressive learning models. Crucially, and somewhat in parallel to empirical observation, we find that tasks requiring long-range prediction (put differently: multi-step reasoning) are precisely those which \"emerge\" at a critical model scale. We also note that our findings are not at all in contrast with the recent theoretical model offered by Arora and Goyal. They take scaling laws for loss functions as a given, and illustrate how such scaling laws can naturally lead to the emergence of more complex reasoning. In the present work we argue directly about the loss. Consequently, we offer a complementary perspective to theirs and try rather to understand whether certain tasks intrinsically require a critical scale.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our work also begs a number of further interesting questions and future directions are abound. We believe that there are many opportunities in exploring LLM related phenomena through the lens of systems modelling. This has also been pointed out by e.g., Soatto et al. and Alonso et al.. It would certainly be interesting to study more concrete emergent skills from this lens, such as in-context learning. Garg et al. show that standard transformer models---such as the GPT-2 family ---can perform linear regression from iid examples without explicit supervision. How does the situation change when the examples are drawn sequentially and possibly lack ergodicity? Another interesting phenomenon in which one may want to understand the role of ergodicity, and in which sequence modelling may help, are language model \"hallucinations\". Kalai and Vempala find that there is no necessary statistical reason for these to occur in an iid generative model---does this change if we adopt a structured sequential perspective?

<!-- chunk {"id": "body-0025", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our study also has a number of interesting extensions to other model classes. It may for instance be worthwhile to instantiate the Markovianesque model of Ildiz et al. and see if similar results can be derived. It may also be interesting to consider other function classes allowing for some degree of nonlinearity. Goel and Bartlett prove than an attention-style architecture can approximate a stabilizing Kalman filter with sufficient context length---can we find corresponding lower bounds? Arguably, one would also like to incorporate some degree of representation learning into the present analysis. Ildiz et al. study how multiple tasks compete for \"representation capacity\" via the spectral properties of certain tasks. It is natural to ask how phenomena such as lack of ergodicity and instability affect this competition.
