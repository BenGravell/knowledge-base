<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Surprising Effects of Risk-Aware Domain Randomization for Contact-Rich Sampling-based Predictive Control

Topics include Predictive control, Robustness, Uncertainty, Sampling-based methods, Control, Learning, Sampling, Domain randomization, DR, SPC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Domain randomization (DR) is widely used in policy learning to improve robustness to modeling error, but remains underexplored in contact-rich sampling-based predictive control (SPC), where rollout quality is highly sensitive to uncertainty. In this work, we take the first step by studying risk-aware DR in predictive sampling on a simple yet representative Push-T task, comparing average, optimistic, and pessimistic rollout aggregations under randomized model instances. Our initial results suggest that DR affects not only robustness to model error, but also the effective cost landscape seen by the sampling-based optimizer, by reshaping the basin of attraction around contact-producing actions. This opens up potential for exploring better grounded risk-aware contact-rich SPC under model uncertainty.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Domain Randomization (DR) has become a standard and powerful tool in reinforcement learning (RL) for robotics, particularly in contact-rich settings where accurate modeling of friction, inertial parameters, and compliance remains difficult. In contrast, the use of DR in trajectory optimization and model predictive control (MPC) is far less explored, especially for contact-rich problems. This gap is notable because the same modeling challenges that motivate DR in RL also arise in contact-rich trajectory optimization and MPC, where performance can be highly sensitive to physical parameters and contact outcomes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances make this problem timely to study: massively parallel GPU simulators enable efficient evaluation of thousands of rollouts under different model realizations, while sampling-based methods, such as Predictive Sampling, Model Predictive Path Integral (MPPI), and Cross Entropy Method (CEM)-style approaches, have become increasingly attractive for nonlinear contact-rich control because they avoid some of the analytic difficulties of the gradient-based optimization through non-smooth contact and complementarity conditions. Together, these tools enable a simple paradigm: evaluate each candidate control sequence across a randomized ensemble of domains and rank it according to a chosen notion of risk.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present a preliminary study of risk-aware domain randomization for contact-rich sampling-based predictive control (SPC). In particular, our preliminary demonstration focuses on the Push-T task.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Average: mean performance across domains,

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pessimistic: worst-case rollout cost (Risk-averse),

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimistic: best-case rollout cost (Risk-seeking).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this work is a first step toward a systematic study of risk-aware DR in contact-rich sampling-based predictive control through a unified comparison of proposed risk operators. Our motivation is that the intuitive ranking of these strategies does not always hold: although pessimistic aggregation may seem most robust under model mismatch, our initial results suggest that optimistic aggregation can sometimes perform better by promoting high-variance but contact-producing candidates. We hypothesize that this occurs because DR affects not only robustness to modeling error, but also the effective search landscape itself. In contact-rich tasks, pessimistic aggregation can suppress narrow low-cost basins, whereas optimistic aggregation can make them easier for a sampling-based optimizer to discover.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

We consider a finite-horizon optimal control problem at planning time $t$, with current state estimate $\mathbf{x}_{0} = {\hat{\mathbf{x}}{(t)}}$. Let

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

denote a control tape over a horizon of length $N$. The nominal planning problem can be written compactly as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

where $J{(\mathbf{U};\mathbf{x}_{0})}$ denotes the rollout cost over the horizon under the dynamics and task objective. For contact-rich systems, this problem is often highly nonconvex and nonsmooth, making gradient-based optimization difficult. SPC instead evaluates candidate control tapes via forward rollouts and updates the nominal plan according to their costs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

At each MPC step, we draw $K$ samples $\mathbf{U}^{(k)}$ from some proposal distribution, typically a Gaussian centered around the previous nominal control tape. We then simulate a rollout for each sample, yielding the associated costs

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

These costs are used to update the nominal control tape $\mathbf{U}$. In general, SPC updates can be written as

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

where $g:{{\mathbb{R}}\rightarrow{\mathbb{R}}_{+}}$ is a nonnegative weighting function. Different choices of $g{( \cdot )}$ recover different SPC algorithms. In this work, we focus on predictive sampling, the simplest SPC algorithm; predictive sampling merely sets $\mathbf{U}$ as the lowest-cost sample.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sampling-based Predictive Control", "weight": 1.0} -->

Having updated the control tape $\mathbf{U}$, we apply the first action $\mathbf{u}_{0}$ and proceed in receding-horizon fashion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Risk-Aware Domain Randomization", "weight": 1.0} -->

In practice, the model we use to simulate rollouts is never perfect. Instead, we aim to improve robustness via DR. In particular, we assume that some model parameters $\mathbf{θ}$ (friction coefficients, body masses, etc.) are drawn from some distribution $\mathcal{D}$. In this setting, the cost

<!-- chunk {"id": "body-0018", "role": "body", "section": "Risk-Aware Domain Randomization", "weight": 1.0} -->

is determined by the value of these parameters as well as the initial condition $\mathbf{x}_{0}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Sampled Control Inputs and Domain Randomization", "weight": 1.0} -->

To apply DR to SPC, we randomly sample $R$ sets of parameters

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Sampled Control Inputs and Domain Randomization", "weight": 1.0} -->

resulting in $R$ "domains", each with different dynamics.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Sampled Control Inputs and Domain Randomization", "weight": 1.0} -->

We roll out each control tape $\mathbf{U}^{(k)}$ in each domain, performing $K \times R$ total rollouts to produce costs

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Sampled Control Inputs and Domain Randomization", "weight": 1.0} -->

indexed by both sample $k$ and randomized domain $r$. All $R \times K$ rollouts can be performed in parallel.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Risk Strategies", "weight": 1.0} -->

To apply SPC, we must aggregate the rollout costs across domains. We do so via a risk operator

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Risk Strategies", "weight": 1.0} -->

This provides a single scalar score for each sample, which we can then feed into to perform SPC.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Risk Strategies", "weight": 1.0} -->

While there are many possibilities for the ${Risk}{( \cdot )}$ operator, we focus here on three simple strategies: average, pessimistic, and optimistic.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B1 Average", "weight": 1.0} -->

This is most similar to the DR used in RL, which optimizes performance in expectation over randomized domains.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B2 Pessimistic", "weight": 1.0} -->

This is a risk-averse strategy: costs are only low if they are low across all domains.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B3 Optimistic", "weight": 1.0} -->

This is a risk-seeking strategy and may seem like a strictly bad idea, especially under modeling error. However, as we show below, risk-seeking DR can produce strong and even superior performance on contact-rich tasks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Risk metrics such as VaR and CVaR can interpolate between risk-seeking (optimistic), risk-neutral (average), and risk-averse behavior (pessimistic), and are a natural direction for future study.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Algorithm 1 summarizes the overall procedure. Note that both loops in this algorithm are trivially parallelizable. In practice, performant SPC implementation requires spline-based dimensionality reduction and careful treatment of time shifts between replanning steps. We omit these details for space and refer the interested reader to.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Implementation Details", "weight": 1.0} -->

We implement the proposed MPC framework in Hydrax, using MuJoCo MJX as the backend for parallel rollout evaluation across sampled input tapes and domain-randomized model instances.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-D Experiment Setup", "weight": 1.0} -->

The Push-T task consists of two bodies: a T-shaped block and a spherical pusher, both governed by second-order mechanical dynamics. The goal is for the spherical pusher to drive the T-shaped block to a desired pose through contact. As illustrated in Fig. 1, the spherical pusher has configuration $\mathbf{q}_{p} = \mathbf{p}_{p} \in {\mathbb{R}}^{2}$, where $\mathbf{p}_{p}$ denotes its planar position. The T-block has configuration $\mathbf{q}_{b} = {\lbrack\mathbf{p}_{b},\phi\rbrack} \in {SE{}}$, where $\mathbf{p}_{b} \in {\mathbb{R}}^{2}$ denotes its planar position and $\phi \in {\mathbb{S}}^{1}$ its orientation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Experiment Setup", "weight": 1.0} -->

We compare the three risk-aware DR strategies from Sec. IV using predictive sampling, with controller parameters given in Table I and cost terms given in Table II. To model parametric uncertainty, we define the DR terms as

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Experiment Setup", "weight": 1.0} -->

where $\mathbf{λ}$ and $\mathbf{τ}$ are the sliding-friction and contact-time-constant vectors, and $\mathbf{m}$ and $\mathbf{k}_{v}$ are the body-mass and actuator-gain vectors. The sampling strategy associated with each component of $\mathbf{θ}$ is summarized in Table III.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-D Experiment Setup", "weight": 1.0} -->

To evaluate robustness to model mismatch, each trial is associated with a unique seed that specifies both the collision-free initial condition (Table IV) and a fixed "true" model realization sampled from the randomization distribution. At planning time, the controller evaluates candidate actions over an ensemble of $R$ randomized models, whereas execution takes place on the single fixed true model realization, thereby introducing model mismatch. We consider $R \in {\{ 0,4,16,32,64\}}$ together with the three risk strategies. For $S = 20$ seeded trials, we simulate for $T_{sim} = 7.0$ seconds.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-E Results", "weight": 1.0} -->

All reported metrics are computed on the executed closed-loop simulation rather than on the predicted rollouts, so the risk operator affects performance only indirectly through the planner's sample ranking. Fig. 2(a) shows that the pessimistic strategy generally performs worst and degrades as the number of randomized domains increases, while the average strategy remains intermediate. In contrast, the optimistic strategy consistently achieves the best or near-best mean total cost, with the strongest performance around $R = 16$. Fig. 2(b) shows a similar trend in block position error over time. As $R$ increases, the optimistic strategy drives the block toward the goal more quickly, whereas the pessimistic strategy often stalls and fails to make meaningful progress. Accordingly, in difficult Push-T cases, the optimistic controller reaches the low-cost target region much earlier, whereas the pessimistic controller often fails to do so.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

Intuitively, one might expect a risk-averse strategy to perform best under model error. But this expectation is not supported by data, at least in the case of the Push-T. In fact, the trend that we see in Fig. 2 is quite the opposite: the risk-*seeking* strategy instead achieves the best performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

We hypothesize that this surprising result is due to the fact that domain randomization plays two unique and sometimes conflicting roles: (i) improving robustness to model error, and (ii) shaping the basin of attraction around local minima. The first role is well-known, while the second is less so.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

To illustrate the basin-shaping effect, consider a simple scalar cost $J{(u)}$. Domain randomization warps the cost landscape in complicated ways, but for ease of illustration, assume that DR merely shifts the cost landscape left and right. More precisely, for each randomized domain $r$ we have

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

An example is shown in Fig. 3, along with aggregated costs ${\overline{J}}_{avg}$, ${\overline{J}}_{pes}$, ${\overline{J}}_{opt}$ from each of our three risk strategies.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

The risk-seeking optimistic strategy (${\overline{J}}_{opt}$) expands the basin of attraction around local minima, while the risk-averse pessimistic strategy (${\overline{J}}_{pes}$) makes local minima smaller and narrower. Because contact-rich tasks are dominated by large (nearly) flat regions and narrow minima, clearer information about the location of a local minimum, as provided by a risk-seeking strategy, may be more important than preferring a very robust local minima. However, a risk-seeking strategy can also degrade performance by obscuring the location of a true minimum. This is quite similar to randomized smoothing, though DR perturbs the cost function itself rather than simply adding noise to its arguments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

This effect can be seen from a simple rollout-ranking example in Push-T. Suppose candidate $A$ has randomized costs $\{ 1,8,9\}$, while candidate $B$ has costs $\{ 4,4,4\}$, where lower is better. Candidate $B$ is consistent but mediocre, and is preferred by pessimistic aggregation as ${\max{(A)}} > {\max{(B)}}$. Candidate $A$, however, succeeds in one randomized domain and is preferred by optimistic aggregation as ${\min{(A)}} < {\min{(B)}}$. Fig. 1 illustrates such a scenario. Since local minima are particularly narrow and difficult to hit in contact-rich tasks like the Push-T, taking this risky rollout is often worthwhile; it moves the system closer to a local minimum, where further replanning steps will be more effective.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Future Work and Open Questions", "weight": 1.5} -->

The work presented here is extremely preliminary---a single task, one SPC algorithm, and only a few risk strategies. Future experimental work will focus other contact-rich tasks, more sophisticated SPC algorithms (MPPI, CEM, CMA-ES, etc.), more advanced risk strategies (VaR, CVaR, etc.), and sim-to-real transfer.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Future Work and Open Questions", "weight": 1.5} -->

Our preliminary results also point to a pressing need for more fundamental understanding of risk-aware domain randomization for contact-rich control. What theoretical framework(s) should we leverage? Can we quantify the tradeoff between model robustness and a friendlier cost landscape? Do such tradeoffs occur in policy learning as well as predictive control? How do system dynamics (quasi-static vs unstable, high-dimensional vs low-dimensional, etc.) influence these tradeoffs? And can we use this information to design better SPC algorithms?

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Thanks to recent advances in hardware-accelerated parallel simulation and sampling-based optimization, we finally have the tools to investigate domain randomization in the predictive control setting. In this preliminary study, we demonstrated that risk-aware domain randomization produces some surprising and counter-intuitive effects for contact-rich tasks. While preliminary and limited in scope, these initial results demonstrate striking qualitative differences from the well-known impact of domain randomization on policy learning, pointing toward domain randomized predictive control as an important and fruitful area for further study.
