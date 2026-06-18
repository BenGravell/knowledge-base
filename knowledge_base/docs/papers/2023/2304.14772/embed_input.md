<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multisample Flow Matching: Straightening Flows with Minibatch Couplings

Topics include Generalization, Matching, Generative model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulation-free methods for training continuous-time generative models construct probability paths that go between noise distributions and individual data samples. Recent works, such as Flow Matching, derived paths that are optimal for each data sample. However, these algorithms rely on independent data and noise samples, and do not exploit underlying structure in the data distribution for constructing probability paths. We propose Multisample Flow Matching, a more general framework that uses non-trivial couplings between data and noise samples while satisfying the correct marginal constraints. At very small overhead costs, this generalization allows us to (i) reduce gradient variance during training, (ii) obtain straighter flows for the learned vector field, which allows us to generate high-quality samples using fewer function evaluations, and (iii) obtain transport maps with lower cost in high dimensions, which has applications beyond generative modeling. Importantly, we do so in a completely simulation-free manner with a simple minimization objective. We show that our proposed methods improve sample consistency on downsampled ImageNet data sets, and lead to better low-cost sample generation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep generative models offer an attractive family of paradigms that can approximate a data distribution and produce high quality samples, with impressive results in recent years. In particular, these works have made use of simulation-free training methods for diffusion models. A number of works have also adopted and generalized these simulation-free methods for continuous normalizing flows (CNF; Chen et al. ), a family of continuous-time deep generative models that parameterizes a vector field which flows noise samples into data samples.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Lipman et al. proposed *Flow Matching* (FM), a method to train CNFs based on constructing explicit *conditional probability paths* between the noise distribution (at time $t = 0$) and each data sample (at time $t = 1$). Furthermore, they showed that these conditional probability paths can be taken to be the optimal transport path when the noise distribution is a standard Gaussian, a typical assumption in generative modeling. However, this does not imply that the *marginal probability path* (marginalized over the data distribution) is anywhere close to the optimal transport path between the noise and data distributions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most existing works, including diffusion models and Flow Matching, have only considered conditional sample paths where the endpoints (a noise sample and a data sample) are sampled independently. However, this results in non-zero gradient variances even at convergence, slow training times, and in particular limits the design of probability paths. In turn, it becomes difficult to create paths that are fast to simulate, a desirable property for both likelihood evaluation and sampling.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a tractable instance of Flow Matching with joint distributions, which we call *Multisample Flow Matching*. Our proposed method generalizes the construction of probability paths by considering non-independent couplings of $k$-sample empirical distributions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among other theoretical results, we show that if an appropriate optimal transport (OT) inspired coupling is chosen, then sample paths become straight as the batch size $k\rightarrow\infty$, leading to more efficient simulation. In practice, we observe both improved sample quality on ImageNet using adaptive ODE solvers and using simple Euler discretizations with a low budget number of function evaluations. Empirically, we find that on ImageNet, we can *reduce the required sampling cost by 30% to 60%* for achieving a low Fréchet Inception Distance (FID) compared to a baseline Flow Matching model, while introducing only 4% more training time. This improvement in sample efficiency comes at no degradation in performance, e.g. log-likelihood and sample quality.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Within the deep generative modeling paradigm, this allows us to regularize towards the optimal vector field in a completely simulation-free manner (unlike e.g. Finlay et al.; Liu et al. ), and avoids adversarial formulations (unlike e.g. Makkuva et al.; Albergo & Vanden-Eijnden ). In particular, we are the first work to be able to make use of solutions from optimal solutions on minibatches while preserving the correct marginal distributions, whereas prior works would only fit to the barycentric average (see detailed discussion in Section 5.1). Beyond generative modeling, we also show how our method can be seen as a new way to compute approximately optimal transport maps between arbitrary distributions in settings where the cost function is completely unknown and only minibatch optimal transport solutions are provided.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Continuous Normalizing Flow", "weight": 1.0} -->

To create a deep generative model, Chen et al. suggested modeling the vector field $u_{t}$ with a neural network, leading to a deep parametric model of the flow $\psi_{t}$, referred to as a *Continuous Normalizing Flow* (CNF). A CNF is often used to transform a density $p_{0}$ to a different one, $p_{1}$, via the push-forward equation

<!-- chunk {"id": "body-0010", "role": "body", "section": "Continuous Normalizing Flow", "weight": 1.0} -->

where the second equality defines the push-forward (or change of variables) operator $\sharp$. A vector field $u_{t}$ is said to *generate* a probability path $p_{t}$ if its flow $\psi_{t}$ satisfies.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

A simple simulation-free method for training CNFs is the *Flow Matching* algorithm, which regresses onto an (implicitly-defined) target vector field that generates the desired probability density path $p_{t}$. Given two marginal distributions $q_{0}{(x_{0})}$ and $q_{1}{(x_{1})}$ for which we would like to learn a CNF to transport between, Flow Matching seeks to optimize the simple regression objective,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

where $v_{t}{(x;\theta)}$ is the parametric vector field for the CNF, and $u_{t}{(x)}$ is a vector field that generates a probability path $p_{t}$ under the two marginal constraints that $p_{t = 0} = q_{0}$ and $p_{t = 1} = q_{1}$. While Equation 3 is the ideal objective function to optimize, not knowing $(p_{t},u_{t})$ makes this computationally intractable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

Lipman et al. proposed a tractable method of optimizing, which first defines *conditional* probability paths and vector fields, such that when marginalized over $q_{0}{(x_{0})}$ and $q_{1}{(x_{1})}$, provide both $p_{t}{(x)}$ and $u_{t}{(x)}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

where the conditional probability path is chosen such that

<!-- chunk {"id": "body-0015", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

where $\delta{({x - a})}$ is a Dirac mass centered at $a \in {\mathbb{R}}^{d}$. By construction, $p_{t}{(\left. x \middle| x_{1} \right.)}$ now satisfies both marginal constraints.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

with $x_{t} = {\psi_{t}{(\left. x_{0} \middle| x_{1} \right.)}}$; see 2.2.1 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings") for more details. Note that this objective has the same gradient with respect to the model parameters $\theta$ as Eq..

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conditional OT (CondOT) path", "weight": 1.0} -->

One particular choice of conditional path $p_{t}{(\left. x \middle| x_{1} \right.)}$ is to use the flow that corresponds to the optimal transport displacement interpolant when $q_{0}{(x_{0})}$ is the standard Gaussian, a common convention in generative modeling. The vector field that corresponds to this is

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conditional OT (CondOT) path", "weight": 1.0} -->

Using this conditional vector field, this gives the conditional flow

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conditional OT (CondOT) path", "weight": 1.0} -->

Substituting (9 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings")) into (8 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings")), one can also express the value of this vector field using a simpler expression,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Conditional OT (CondOT) path", "weight": 1.0} -->

It is evident that this results in conditional flows that (i) tranports all points $x_{0}$ from $t = 0$ to $x_{1}$ at exactly $t = 1$ and (ii) are straight paths between the samples $x_{0}$ and $x_{1}$. This particular case of straight paths was also studied by Liu et al. and Albergo & Vanden-Eijnden, where the conditional flow (9 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings")) is referred to as a stochastic interpolant. Lipman et al. additionally showed that the conditional construction can be applied to a large class of Gaussian conditional probability paths, namely when ${p_{t}{(\left. x \middle| x_{1} \right.)}} = {\mathcal{N}{(\left.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conditional OT (CondOT) path", "weight": 1.0} -->

x \middle| {{\mu_{t}{(x_{1})}},{\sigma_{t}{(x_{1})}^{2}I}} \right.)}}$. This family of probability paths encompasses most prior diffusion models where probability paths are induced by simple diffusion processes with linear drift and constant diffusion (e.g. Ho et al.; Song et al. ). However, existing works mostly consider settings where $q_{0}{(x_{0})}$ and $q_{1}{(x_{1})}$ are sampled independently when computing training objectives such as.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal Transport: Static & Dynamic", "weight": 1.0} -->

Optimal transport generally considers methodologies that define some notion of distance on the space of probability measures. Letting $\mathcal{P}{({\mathbb{R}}^{d})}$ be the space of probability measures over ${\mathbb{R}}^{d}$, we define the Wasserstein distance with respect to a cost function $c:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}_{+}}$ between two measures ${q_{0},q_{1}} \in {\mathcal{P}{({\mathbb{R}}^{d})}}$ as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal Transport: Static & Dynamic", "weight": 1.0} -->

where $\Gamma{(q_{0},q_{1})}$ is the set of joint measures with left marginal equal to $q_{0}$ and right marginal equal to $q_{1}$, called the set of *couplings*. The minimizer to Equation 11 is called the optimal coupling, which we denote by $q_{c}^{\ast}$. In the case where ${c{(x_{0},x_{1})}} ≔ {\|{x_{0} - x_{1}}\|}^{2}$, the squared-Euclidean distance, Equation 11 amounts to the (squared) $2$-Wasserstein distance $W_{2}^{2}{(q_{0},q_{1})}$, and we simply write the optimal transport plan as $q^{\ast}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimal Transport: Static & Dynamic", "weight": 1.0} -->

Considering again the squared-Euclidean cost, in the case where $q_{0}$ exhibits a density over ${\mathbb{R}}^{d}$ (e.g. if $q_{0}$ is the standard normal distribution), Benamou & Brenier states that $W_{2}^{2}{(q_{0},q_{1})}$ can be equivalently expressed as a *dynamic* formulation,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimal Transport: Static & Dynamic", "weight": 1.0} -->

where $u_{t}$ generates $p_{t}$, and $p_{t}$ satisfies boundary conditions $p_{t = 0} = q_{0}$ and $p_{t = 1} = q_{1}$. The optimality condition ensures that sample paths $x_{t}$ are straight lines, i.e. minimize the length of the path, and leads to paths that are much easier to simulate. Some prior approaches have sought to regularize the model using this optimality objective (e.g. Tong et al.; Finlay et al. ). In contrast, instead of directly minimizing, we will discuss an approach based on using solutions of the optimal coupling $q^{\ast}$ on minibatch problems, while leaving the marginal constraints intact.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

While Conditional Flow Matching in leads to an unbiased gradient estimator for the Flow Matching objective, it was designed with independently sampled $x_{0}$ and $x_{1}$ in mind. We generalize the framework from Subsection 2.2 to a construction that uses arbitrary joint distributions of $q{(x_{0},x_{1})}$ which satisfy the correct marginal constraints, i.e.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

We will show in Subsection 4 that this can potentially lead to lower gradient variance during training and allow us to design more optimal marginal vector fields $u_{t}{(x)}$ with desirable properties such as improved sample efficiency.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

Building on top of Flow Matching, we propose modifying the conditional probability path construction so that at $t = 0$, we define

<!-- chunk {"id": "body-0029", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

where $q{(\left. x_{0} \middle| x_{1} \right.)}$ is the conditional distribution $\frac{q{(x_{0},x_{1})}}{q_{1}{(x_{1})}}$. Using this construction, we still satisfy the marginal constraint,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

i.e. ${p_{t = 0}{(x)}} = {\int{q{(x,x_{1})}{dx_{1}}}} = {q_{0}{(x)}}$ by the assumption made. Then similar to Chen & Lipman, we note that the conditional probability path $p_{t}{(\left. x \middle| x_{1} \right.)}$ *need not be explicitly formulated* for training, and that only an appropriate conditional vector field $u_{t}{(\left. x \middle| x_{1} \right.)}$ needs to be chosen such that all points arrive at $x_{1}$ at $t = 1$, which ensures ${p_{t = 1}{(\left. x \middle| x_{1} \right.)}} = {\delta{({x - x_{1}})}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

As such, we can make use of the same conditional vector field as prior works, e.g. the choice in Equations 8 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings"), 9 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings") and 10 path ‣ 2.2 Flow Matching ‣ 2 Preliminaries ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings").

<!-- chunk {"id": "body-0032", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

We then propose the Joint CFM objective as

<!-- chunk {"id": "body-0033", "role": "body", "section": "Flow Matching with Joint Distributions", "weight": 1.0} -->

A quick sanity check shows that this objective can be used with any choice of joint distribution $q{(x_{0},x_{1})}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Variance reduction", "weight": 1.0} -->

Choosing a good joint distribution can be seen as a way to reduce the variance of the gradient estimate, which improves and speeds up training.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Straight flows", "weight": 1.0} -->

Ideally, the flow $\psi_{t}$ of the marginal vector field $u_{t}$ (and of the learned $v_{\theta}$ by extension) should be close to a straight line. The reason is that ODEs with straight trajectories can be solved with high accuracy using fewer steps (i.e. function evaluations), which speeds up sample generation. The quantity

<!-- chunk {"id": "body-0036", "role": "body", "section": "Straight flows", "weight": 1.0} -->

which we call the *straightness* of the flow and was also studied by Liu, measures how straight the trajectories are. Namely, we can rewrite it as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Straight flows", "weight": 1.0} -->

When $x_{0}$ and $x_{1}$ are sampled independently, the straightness is in general far from zero. This can be seen in the CondOT plots in Figure 2 (right); if flows were close to straight lines, samples generated with one function evaluation (NFE=1) would be of high quality. In Section 4, we show that for certain joint distributions, the straightness of the flow is close to zero.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Near-optimal transport cost", "weight": 1.0} -->

There is no reason to believe that when $x_{0}$ and $x_{1}$ are sampled independently, the transport cost ${\mathbb{E}}_{q_{0}{(x_{0})}}{\|{{\psi_{1}{(x_{0})}} - x_{0}}\|}^{2}$ will be anywhere near the optimal transport cost $W_{2}^{2}{(p_{0},p_{1})}$. Yet, in Section 4 we show that for well chosen $q$, the transport cost for $\psi_{1}$ does approach its optimal value. Computing optimal (or near-optimal) transport maps in high dimensions is a challenging task that extends beyond generative modeling and into the field of optimal transport, and it has applications in computer vision and computational biology, for instance. Hence, Joint CFM may also be viewed as a practical way to obtain approximately optimal transport maps in this context.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Multisample Flow Matching", "weight": 1.0} -->

Constructing a joint distribution satisfying the marginal constraints is difficult, especially since at least one of the marginal distributions is based on empirical data. We thus discuss a method to construct the joint distribution $q{(x_{0},x_{1})}$ implictly by designing a suitable sampling procedure that leaves the marginal distributions invariant. Note that training with only requires sampling from $q{(x_{0},x_{1})}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Multisample Flow Matching", "weight": 1.0} -->

Marginalizing $q^{k}{(x_{0},x_{1})}$ over samples from Step 1, we obtain the implicitly defined $q{(x_{0},x_{1})}$. By choosing different *couplings* $\pi{(i,j)}$, we induce different joint distributions. In this work, we focus on couplings that induce joint distributions which approximates, or at least partially satisfies, the optimal transport joint distribution. The following result, proven in App. D.3, guarantees that $q$ has the right marginals.

<!-- chunk {"id": "body-0041", "role": "body", "section": "CondOT is Uniform Coupling", "weight": 1.0} -->

The aforementioned multisample construction subsumes the independent joint distribution used by prior works, when the joint coupling is taken to be uniformly distributed, i.e. ${\pi{(i,j)}} = \frac{1}{k}$. This is precisely the coupling used by under our introduced notion of Multisample Flow Matching, and acts as a natural reference point.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Batch Optimal Transport (BatchOT) Couplings", "weight": 1.0} -->

The natural connections between optimal transport theory and optimal sampling paths in terms of straight-line interpolations, lead us to the following pseudo-deterministic coupling, which we call Batch Optimal Transport (BatchOT). While it is difficult to solve at the population level, it can efficiently solved on the level of samples. Let ${\{ x_{0}^{(i)}\}}_{i = 1}^{k} \sim {q_{0}{(x_{0})}}$ and ${\{ x_{1}^{(i)}\}}_{i = 1}^{k} \sim {q_{1}{(x_{1})}}$. When defined on batches of samples, the OT problem can be solved exactly and efficiently using standard solvers, as in POT. On a batch of $k$ samples, the runtime complexity is well-understood via either the Hungarian algorithm or network simplex algorithm, with an overall complexity of $\mathcal{O}{(k^{3})}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Batch Optimal Transport (BatchOT) Couplings", "weight": 1.0} -->

The resulting coupling $\pi^{k, \ast}$ from the algorithm is a permutation matrix, which is a type of doubly-stochastic matrix that we can incorporate into Step 3 of our procedure.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Batch Optimal Transport (BatchOT) Couplings", "weight": 1.0} -->

We consider the effect that the sample size $k$ has on the marginal vector field $u_{t}{(x)}$. The following theorem shows that in the limit of $k\rightarrow\infty$, BatchOT satisfies the three criteria that motivate Joint CFM: variance reduction, straight flows, and near-optimal transport cost.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Batch Entropic OT (BatchEOT) Couplings", "weight": 1.0} -->

For $k$ sufficiently large, the cubic complexity of the BatchOT approach is not always desirable, and instead one may consider approximate methods that produce couplings sufficiently close to BatchOT at a lower computational cost.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Batch Entropic OT (BatchEOT) Couplings", "weight": 1.0} -->

where ${H{(q)}} = {- {\sum_{i,j}{q_{i,j}{({{\log{(q_{i,j})}} - 1})}}}}$ is the entropy of the doubly stochastic matrix $q$, and $\varepsilon > 0$ is some finite regularization parameter. The optimality conditions of this strictly convex program leads to Sinkhorn's algorithm, which has a runtime of $\overset{\sim}{\mathcal{O}}{({k^{2}/\varepsilon})}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Batch Entropic OT (BatchEOT) Couplings", "weight": 1.0} -->

The output of performing Sinkhorn's algorithm is a doubly-stochastic matrix. The two limiting regimes of the regularization parameter are well understood (c.f. Peyré & Cuturi, Proposition 4.1, for instance): as $\varepsilon\rightarrow 0$, BatchEOT recovers the BatchOT permutation matrix from Section 4.2 Couplings ‣ 4 Multisample Flow Matching ‣ Multisample Flow Matching: Straightening Flows with Minibatch Couplings"); as $\varepsilon\rightarrow\infty$, BatchEOT recovers the independent coupling on the indices from Section 4.1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Stable and Heuristic Couplings", "weight": 1.0} -->

An alternative approach is to consider faster algorithms that satisfy at least some desirable properties of an optimal coupling. In particular, an optimal coupling is *stable*. A permutation coupling is stable if *no pair of $x_{0}^{(i)}$ and $x_{1}^{(j)}$ favor each other over their assigned pairs based on the coupling.* Such a problem can be solved using the Gale-Shapeley algorithm which has a compute cost of $\mathcal{O}{(k^{2})}$ given the cross set ranking of all samples. Starting from a random assignment, it is an iterative algorithm that reassigns pairs if they violate the stability property and can terminate very early in practice. Note that in a cost-based ranking, one has to sort the coupling costs of each sample with all samples in the opposing set, resulting in an overall $\mathcal{O}{({k^{2}{\log{(k)}}})}$ compute cost.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Stable and Heuristic Couplings", "weight": 1.0} -->

The Gale-Shapeley algorithm is agnostic to any particular costs, however, as stability is only defined in terms of relative rankings of individual samples. We design a modified version of this algorithm based on a heuristic for satisfying the cyclical monotonicity property of optimal transport, namely that should pairs be reassigned, the reassignment should not increase the total cost of already matched pairs. We refer to the output of this modified algorithm as a *heuristic coupling* and discuss the details in Appendix A.2.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Minibatch Couplings for Generative Modeling", "weight": 1.0} -->

Among works that use optimal transport for training generative models are those that make use of batch optimal solutions and their gradients such as Li et al.; Genevay et al.; Fatras et al.; Liu et al.. However, naïvely using solutions to batches only produces, at best, the barycentric map, i.e. the map that fits to average of the batch couplings, and does not correctly match the true marginal distribution. This is a well-known problem and while multiple works (e.g. Fatras et al.; Nguyen et al. ) have attempted to circumvent the issue through alternative formulations of optimality, the lack of marginal preservation has been a major downside of using batch couplings for generative modeling as they do not have the ability to match the target distribution for finite batch sizes. This is due to the use of building models within the *static* setting, where the map is parameterized directly with a neural network. In contrast, we have shown in Lemma 4.1 that in our *dynamic* setting, where we parameterize the map as the solution of a neural ODE, it is possible to preserve the marginal distribution exactly.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Minibatch Couplings for Generative Modeling", "weight": 1.0} -->

Furthermore, we have shown in Proposition D.7 (App. D.5) that our method produces a map that is no higher cost than the joint distribution induced from BatchOT couplings.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Minibatch Couplings for Generative Modeling", "weight": 1.0} -->

Concurrently, Tong et al. motivates the use of BatchOT solutions within a similar framework as our Joint CFM, but from the perspective of obtaining accurate solutions to dynamic optimal transport problems. Similarly, Lee et al. propose to explicitly learn a joint distribution, parameterized with a neural network, with the aim of minimizing trajectory curvature; this is done using through an auxiliary VAE-style objective function. In contrast, we propose a family of couplings that all satisfy the marginal constraints, all of which are easy to implement and have negligible cost during training. Our construction allow us to focus on (i) fixing consistency issues within simulation-free generative models, and (ii) using Joint CFM to obtain more optimal solutions than the original BatchOT solutions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments", "weight": 1.0} -->

We empirically investigate Multisample Flow Matching on a suite of experiments. First, we show how different couplings affect the model on a 2D distribution. We then turn to benchmark, high-dimensional datasets, namely ImageNet. We use the official *face-blurred* ImageNet data and then downsample to 32$\times$`<!-- -->`{=html}32 and 64$\times$`<!-- -->`{=html}64 using the open source preprocessing scripts from Chrabaszcz et al.. Finally, we explore the setting of unknown cost functions while only batch couplings are provided. Full details on the experimental setting can be found in Appendix E.2.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Insights from 2D experiments", "weight": 1.0} -->

The diffusion and CondOT probability paths do not capture intricate details of the data distribution until it is almost at the end of the trajectory, whereas Multisample Flow Matching approaches provide a gradual transition to the target distribution along the flow. We also see that with a fixed step solver, the BatchOT method is able to produce an accurate target distribution in just one Euler step in this low-dimensional setting, while the other coupling approaches also get pretty close. Finally, it is interesting that both Stable and Heuristic exhibit very similar probability paths to optimal transport despite only satisfying weaker conditions.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Image Datasets", "weight": 1.0} -->

We find that Multisample Flow Matching retains the performance of Flow Matching while improving on sample quality, compute cost, and variance. In Table 6 of Section B.1, we report sample quality using the standard Fréchet Inception Distance (FID), negative log-likelihood values using bits per dimension (BPD), and compute cost using number of function evaluations (NFE); these are all standard metrics throughout the literature. Additionally, we report the variance of $u_{t}{(\left. x \middle| {x_{0},x_{1}} \right.)}$, estimated using the Joint CFM loss which is an upper bound on the variance. We do not observe any performance degradations while simulation efficiency improves significantly, even with small batch sizes.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Image Datasets", "weight": 1.0} -->

Additionally, in Section B.5, we include runtime comparisons between Flow Matching and Multisample Flow Matching. On, we only observe a 0.8% relative increase in runtime compared to Flow Matching, and a 4% increase.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Higher sample quality on a compute budget", "weight": 1.0} -->

We observe that with a fixed NFE, models trained using Multisample Flow Matching generally achieve better sample quality. For these experiments, we draw $x_{0} \sim {\mathcal{N}{(0,I_{d})}}$ and simulate $v_{t}{( \cdot,\theta)}$ up to time $t = 1$ using a fixed step solver with a fixed NFE. Figures 3 show that even on high dimensional data distributions, the sample quality of of multisample methods improves over the naïve CondOT approach as the number of function evaluations drops. We compare to the FID of diffusion baseline methods in Table 2, and provide additional results in Section B.4.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Higher sample quality on a compute budget", "weight": 1.0} -->

Interestingly, we find that the Stable coupling actually performs on par, and some times better than the BatchOT coupling, despite having a smaller asymptotic compute cost and only satisfying a weaker condition within each batch.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Higher sample quality on a compute budget", "weight": 1.0} -->

As FID is computed over a full set of samples, it does not show how varying NFE affects individual sample paths. We discuss a notion of consistency next, where we analyze the similarity between low-NFE and high-NFE samples.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Consistency of individual samples", "weight": 1.0} -->

In Figure 1 we show samples at different NFEs, where it can be qualitatively seen that BatchOT produces samples that are more consistent between high- and low-NFE solutions than CondOT, despite achieving similar FID values.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Consistency of individual samples", "weight": 1.0} -->

To evaluate this quantitatively, we define a metric for establishing the consistency of a model with respect to an integration scheme: let $x^{(m)}$ be the output of a numerical solver initialized at $x$ using $m$ function evalutions to reach $t = 1$, and let $x^{( \ast )}$ be a near-exact sample solved using a high-cost solver starting from $x_{0}$ as well. We define

<!-- chunk {"id": "body-0062", "role": "body", "section": "Consistency of individual samples", "weight": 1.0} -->

where $\mathcal{F}{( \cdot )}$ outputs the hidden units from a pretrained InceptionNet^11^1We take the same layer as used in standard FID computation., and $D$ is the number of hidden units. These kinds of perceptual losses have been used before to check the content alignment between two image samples (e.g. Gatys et al.; Johnson et al. ). We find that Multisample Flow Matching has better consistency at all values of NFE, shown in Table 3.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Improved Batch Optimal Couplings", "weight": 1.0} -->

We further explore the usage of Multisample Flow Matching as an approach to improve upon batch optimal solutions. Here, we experiment with a different setting, where the cost is unknown and only samples from a batch optimal coupling are provided. In the real world, it is often the case that the preferences of each person are not known explicitly, but when given a finite number of choices, people can more easily find their best assignments. This motivates us to consider the case of unknown cost functions, and information regarding the optimal coupling is only given by a weak oracle that acts on finite samples, denoted $q_{{OT},c}^{k}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Improved Batch Optimal Couplings", "weight": 1.0} -->

This can be viewed as learning the barycentric projection, i.e. ${\psi^{\ast}{(x_{0})}} = {E_{q_{{OT},c}^{k}{({x_{1}|x_{0}})}}\left\lbrack x_{1} \right\rbrack}$, a well-studied quantity but is known to not preserve the marginal distribution.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Improved Batch Optimal Couplings", "weight": 1.0} -->

We experiment with 4 different cost functions on three synthetic datasets in dimensions $\{ 2,32,64\}$ where both $q_{0}$ and $q_{1}$ are chosen to be Gaussian mixture models. In Table 4 we report both the transport cost and the KL divergence between $q_{1}$ and the distribution induced by the learned map, i.e. ${\lbrack\psi_{1}\rbrack}_{\sharp}q_{0}$. We observe that while B-ST always results in lower transport costs compared to B-FM, its KL divergence is always very high, meaning that the pushed-forward distribution by the learned static map poorly approximates $q_{1}$. Another interesting observation is that B-FM always reduces transport costs compared to B, providing experimental support to the theory (Theorem D.8).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We propose Multisample Flow Matching, building on top of recent works on simulation-free training of continuous normalizing flows. While most prior works make use of training algorithms where data and noise samples are sampled independently, Multisample Flow Matching allows the use of more complex joint distribution. This introduces a new approach to designing probability paths. Our framework increases sample efficiency and sample quality when using low-cost solvers. Unlike prior works, our training method does not rely on simulation of the learned vector field during training, and does not introduce any min-max formulations. Finally, we note that our method of fitting to batch optimal couplings is the first to also preserve the marginal distributions, an important property in both generative modeling and solving transport problems.
