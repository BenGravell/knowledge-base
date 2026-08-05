<!-- arxiv-full-text:v1 {"arxiv_id": "2605.03290", "source": "arxiv-html"} -->

## Introduction

Domain Randomization (DR) has become a standard and powerful tool in reinforcement learning (RL) for robotics, particularly in contact-rich settings where accurate modeling of friction, inertial parameters, and compliance remains difficult. In contrast, the use of DR in trajectory optimization and model predictive control (MPC) is far less explored, especially for contact-rich problems. This gap is notable because the same modeling challenges that motivate DR in RL also arise in contact-rich trajectory optimization and MPC, where performance can be highly sensitive to physical parameters and contact outcomes.

Recent advances make this problem timely to study: massively parallel GPU simulators enable efficient evaluation of thousands of rollouts under different model realizations, while sampling-based methods, such as Predictive Sampling, Model Predictive Path Integral (MPPI), and Cross Entropy Method (CEM)-style approaches, have become increasingly attractive for nonlinear contact-rich control because they avoid some of the analytic difficulties of the gradient-based optimization through non-smooth contact and complementarity conditions. Together, these tools enable a simple paradigm: evaluate each candidate control sequence across a randomized ensemble of domains and rank it according to a chosen notion of risk.

In this work, we present a preliminary study of risk-aware domain randomization for contact-rich sampling-based predictive control (SPC). In particular, our preliminary demonstration focuses on the Push-T task. For each candidate input sequence, we evaluate rollout cost across multiple randomized model instances and aggregate the results using three risk operators: Average: mean performance across domains, Pessimistic: worst-case rollout cost (Risk-averse), Optimistic: best-case rollout cost (Risk-seeking).

Figure 1: In contact-rich control settings, successful contact may correspond to a narrow low-cost region. We hypothesize that while risk-averse aggregation can suppress this region and shrink its basin of attraction, risk-seeking aggregation can enlarge the basin around promising contact-producing actions.

The main contribution of this work is a first step toward a systematic study of risk-aware DR in contact-rich sampling-based predictive control through a unified comparison of proposed risk operators. Our motivation is that the intuitive ranking of these strategies does not always hold: although pessimistic aggregation may seem most robust under model mismatch, our initial results suggest that optimistic aggregation can sometimes perform better by promoting high-variance but contact-producing candidates. We hypothesize that this occurs because DR affects not only robustness to modeling error, but also the effective search landscape itself. In contact-rich tasks, pessimistic aggregation can suppress narrow low-cost basins, whereas optimistic aggregation can make them easier for a sampling-based optimizer to discover.

## Related Work

Domain randomization is most established in robot learning for sim-to-real transfer, where visual or dynamics variation during training improves robustness to the reality gap. Subsequent work has made DR more adaptive, but the current literature remains focused on policy learning in general.

In contrast, this work is closely related to the growing body of sampling-based predictive control methods for nonlinear planning in robotics, including MPPI, Predictive Sampling, and recent GPU-parallel frameworks such as Hydrax. The closest prior works are robust and risk-aware MPPI variants, which mainly study robustness and safety in domains such as rally car racing or obstacle avoidance. In contrast, our focus is on contact-rich predictive control, and specifically on how risk-aware aggregation across randomized domains reshapes the search landscape of a sampling-based optimizer.

More broadly, this paper relates to robust trajectory optimization and motion planning under uncertainty, including Monte Carlo, risk-bounded, scenario-based, and risk-averse planning methods. It is also connected to planning through contact, where recent work has used smoothing or contact-implicit formulations to address the nonsmooth, highly nonconvex structure induced by impacts and friction. Our perspective is complementary to both lines of work: rather than estimating collision risk or smoothing contact gradients, we study how risk-aware DR reshapes the cost landscape in contact-rich SPC (Fig. 1).

## Sampling-based Predictive Control

We consider a finite-horizon optimal control problem at planning time $t$, with current state estimate $\mathbf{x}_{0}=\hat{\mathbf{x}}(t)$. Let denote a control tape over a horizon of length $N$. The nominal planning problem can be written compactly as where $J(\mathbf{U};\mathbf{x}_{0})$ denotes the rollout cost over the horizon under the dynamics and task objective. For contact-rich systems, this problem is often highly nonconvex and nonsmooth, making gradient-based optimization difficult. SPC instead evaluates candidate control tapes via forward rollouts and updates the nominal plan according to their costs.

At each MPC step, we draw $K$ samples $\mathbf{U}^{(k)}$ from some proposal distribution, typically a Gaussian centered around the previous nominal control tape. We then simulate a rollout for each sample, yielding the associated costs These costs are used to update the nominal control tape $\mathbf{U}$. In general, SPC updates can be written as where $g:\mathbb{R}\to\mathbb{R}_{+}$ is a nonnegative weighting function. Different choices of $g(\cdot)$ recover different SPC algorithms. In this work, we focus on predictive sampling, the simplest SPC algorithm; predictive sampling merely sets $\mathbf{U}$ as the lowest-cost sample.

Having updated the control tape $\mathbf{U}$, we apply the first action $\mathbf{u}_{0}$ and proceed in receding-horizon fashion.

## Risk-Aware Domain Randomization

In practice, the model we use to simulate rollouts is never perfect. Instead, we aim to improve robustness via DR. In particular, we assume that some model parameters $\bm{\theta}$ (friction coefficients, body masses, etc.) are drawn from some distribution $\mathcal{D}$. In this setting, the cost is determined by the value of these parameters as well as the initial condition $\mathbf{x}_{0}$.

2:{θ(r)}r = 1R ∼ 𝒟 ⊳ sample model randomizations 4: $\mathbf{x}_{0}\leftarrow\hat{\mathbf{x}}(t)$ ⊳ update state 6: U(k) ∼ 𝒩(U, σ2) ⊳ sample control tapes 12: $\mathbf{U}\leftarrow\mathbf{U}+\frac{\sum_{k=1}^{K}g(\bar{J}^{(k)})(\mathbf{U}^{(k)}-\mathbf{U})}{\sum_{k=1}^{K}g(\bar{J}^{(k)})}$ ⊳ SPC step Algorithm 1 Risk-Aware Sampling Predictive Control

### IV-A Sampled Control Inputs and Domain Randomization

To apply DR to SPC, we randomly sample $R$ sets of parameters resulting in $R$ "domains", each with different dynamics.

We roll out each control tape $\mathbf{U}^{(k)}$ in each domain, performing $K\times R$ total rollouts to produce costs indexed by both sample $k$ and randomized domain $r$. All $R\times K$ rollouts can be performed in parallel.

### IV-B Risk Strategies

To apply SPC, we must aggregate the rollout costs across domains. We do so via a risk operator This provides a single scalar score for each sample, which we can then feed into to perform SPC.

While there are many possibilities for the $\operatorname{Risk}(\cdot)$ operator, we focus here on three simple strategies: average, pessimistic, and optimistic.

### IV-B1 Average

Strategy that uses the average cost over the randomized domains: This is most similar to the DR used in RL, which optimizes performance in expectation over randomized domains.

### IV-B2 Pessimistic

Strategy that assumes the worst, and uses the highest cost across the randomized models: This is a risk-averse strategy: costs are only low if they are low across all domains.

### IV-B3 Optimistic

Strategy that assumes the best, and uses the lowest cost across the randomized models: This is a risk-seeking strategy and may seem like a strictly bad idea, especially under modeling error. However, as we show below, risk-seeking DR can produce strong and even superior performance on contact-rich tasks.

### Remark 1

Risk metrics such as VaR and CVaR can interpolate between risk-seeking (optimistic), risk-neutral (average), and risk-averse behavior (pessimistic), and are a natural direction for future study.

Algorithm 1 summarizes the overall procedure. Note that both loops in this algorithm are trivially parallelizable. In practice, performant SPC implementation requires spline-based dimensionality reduction and careful treatment of time shifts between replanning steps. We omit these details for space and refer the interested reader to.

### IV-C Implementation Details

We implement the proposed MPC framework in Hydrax, using MuJoCo MJX as the backend for parallel rollout evaluation across sampled input tapes and domain-randomized model instances.

### IV-D Experiment Setup

The Push-T task consists of two bodies: a T-shaped block and a spherical pusher, both governed by second-order mechanical dynamics. The goal is for the spherical pusher to drive the T-shaped block to a desired pose through contact. As illustrated in Fig. 1, the spherical pusher has configuration $\mathbf{q}_{p}=\mathbf{p}_{p}\in\mathbb{R}^{2}$, where $\mathbf{p}_{p}$ denotes its planar position. The T-block has configuration $\mathbf{q}_{b}=[\mathbf{p}_{b},\phi]\in SE$, where $\mathbf{p}_{b}\in\mathbb{R}^{2}$ denotes its planar position and $\phi\in\mathbb{S}^{1}$ its orientation.

We compare the three risk-aware DR strategies from Sec. IV using predictive sampling, with controller parameters given in Table I and cost terms given in Table II. To model parametric uncertainty, we define the DR terms as where $\bm{\lambda}$ and $\bm{\tau}$ are the sliding-friction and contact-time-constant vectors, and $\mathbf{m}$ and $\mathbf{k}_{v}$ are the body-mass and actuator-gain vectors. The sampling strategy associated with each component of $\bm{\theta}$ is summarized in Table III.

At each MPC step, predictive sampling returns a pusher planar velocity command $\mathbf{u}_{0}$, which is applied to the pusher through a first-order closed-loop velocity servo: To evaluate robustness to model mismatch, each trial is associated with a unique seed that specifies both the collision-free initial condition (Table IV) and a fixed "true" model realization sampled from the randomization distribution. At planning time, the controller evaluates candidate actions over an ensemble of $R$ randomized models, whereas execution takes place on the single fixed true model realization, thereby introducing model mismatch. We consider $R\in\{0,4,16,32,64\}$ together with the three risk strategies. For $S=20$ seeded trials, we simulate for $T_{\mathrm{sim}}=7.0$ seconds.

Table I: Predictive sampling parameters used in the experiments. $\|\mathbf{p}_{b}^{\rm des}-\mathbf{p}_{b}\|^{2}$ $\|\phi^{\rm des}\ominus\phi\|^{2}$ Table II: Cost terms used in the experiments, where ∥⋅∥ is the Euclidean norm and ⊖ denotes the orientation difference operator.

Contact Time Const.

Actuator Velocity Gain Table III: DR variables for the task. Contact parameters are sampled directly, while body mass and actuator velocity gain are multiplicatively scaled. 𝒰(⋅, ⋅) denotes the uniform distribution and ⊙ denotes the Hadamard product for element-wise multiplication.

Table IV: Initial-condition sampling used in the Push-T experiments. All initial velocities are zero.

### IV-E Results

Figure 2: Comparison of risk-sensitive domain randomization strategies on the Push-T task, averaged over S = 20 simulations with distinct randomization seeds. (a) Time-averaged total cost over Tsim = 7.0 second trajectories (± SE). (b) Block position error over time (± SE) for selected values of R.

All reported metrics are computed on the executed closed-loop simulation rather than on the predicted rollouts, so the risk operator affects performance only indirectly through the planner's sample ranking. Fig. 2(a) shows that the pessimistic strategy generally performs worst and degrades as the number of randomized domains increases, while the average strategy remains intermediate. In contrast, the optimistic strategy consistently achieves the best or near-best mean total cost, with the strongest performance around $R=16$. Fig. 2(b) shows a similar trend in block position error over time. As $R$ increases, the optimistic strategy drives the block toward the goal more quickly, whereas the pessimistic strategy often stalls and fails to make meaningful progress. Accordingly, in difficult Push-T cases, the optimistic controller reaches the low-cost target region much earlier, whereas the pessimistic controller often fails to do so.

## Discussion

Figure 3: Effect of risk-sensitive domain randomization on a scalar cost landscape J(u) with two local minima. Each row corresponds to a different perturbation magnitude δ. The optimistic strategy J̄opt widens the basins of attraction around local minima, while the pessimistic strategy J̄pes narrows them. As δ increases, these basin-shaping effects become more pronounced.

Intuitively, one might expect a risk-averse strategy to perform best under model error. But this expectation is not supported by data, at least in the case of the Push-T. In fact, the trend that we see in Fig. 2 is quite the opposite: the risk-*seeking* strategy instead achieves the best performance.

We hypothesize that this surprising result is due to the fact that domain randomization plays two unique and sometimes conflicting roles: (i) improving robustness to model error, and (ii) shaping the basin of attraction around local minima. The first role is well-known, while the second is less so.

To illustrate the basin-shaping effect, consider a simple scalar cost $J(u)$. Domain randomization warps the cost landscape in complicated ways, but for ease of illustration, assume that DR merely shifts the cost landscape left and right. More precisely, for each randomized domain $r$ we have An example is shown in Fig. 3, along with aggregated costs $\bar{J}_{\mathrm{avg}}$, $\bar{J}_{\mathrm{pes}}$, $\bar{J}_{\mathrm{opt}}$ from each of our three risk strategies.

The risk-seeking optimistic strategy ($\bar{J}_{\mathrm{opt}}$) expands the basin of attraction around local minima, while the risk-averse pessimistic strategy ($\bar{J}_{\mathrm{pes}}$) makes local minima smaller and narrower. Because contact-rich tasks are dominated by large (nearly) flat regions and narrow minima, clearer information about the location of a local minimum, as provided by a risk-seeking strategy, may be more important than preferring a very robust local minima. However, a risk-seeking strategy can also degrade performance by obscuring the location of a true minimum. This is quite similar to randomized smoothing, though DR perturbs the cost function itself rather than simply adding noise to its arguments.

This effect can be seen from a simple rollout-ranking example in Push-T. Suppose candidate $A$ has randomized costs $\{1,8,9\}$, while candidate $B$ has costs $\{4,4,4\}$, where lower is better. Candidate $B$ is consistent but mediocre, and is preferred by pessimistic aggregation as $\max(A)>\max(B)$. Candidate $A$, however, succeeds in one randomized domain and is preferred by optimistic aggregation as $\min(A)<\min(B)$. Fig. 1 illustrates such a scenario. Since local minima are particularly narrow and difficult to hit in contact-rich tasks like the Push-T, taking this risky rollout is often worthwhile; it moves the system closer to a local minimum, where further replanning steps will be more effective.

## Future Work and Open Questions

The work presented here is extremely preliminary---a single task, one SPC algorithm, and only a few risk strategies. Future experimental work will focus other contact-rich tasks, more sophisticated SPC algorithms (MPPI, CEM, CMA-ES, etc.), more advanced risk strategies (VaR, CVaR, etc.), and sim-to-real transfer.

Our preliminary results also point to a pressing need for more fundamental understanding of risk-aware domain randomization for contact-rich control. What theoretical framework(s) should we leverage? Can we quantify the tradeoff between model robustness and a friendlier cost landscape? Do such tradeoffs occur in policy learning as well as predictive control? How do system dynamics (quasi-static vs unstable, high-dimensional vs low-dimensional, etc.) influence these tradeoffs? And can we use this information to design better SPC algorithms?

## Conclusion

Thanks to recent advances in hardware-accelerated parallel simulation and sampling-based optimization, we finally have the tools to investigate domain randomization in the predictive control setting. In this preliminary study, we demonstrated that risk-aware domain randomization produces some surprising and counter-intuitive effects for contact-rich tasks. While preliminary and limited in scope, these initial results demonstrate striking qualitative differences from the well-known impact of domain randomization on policy learning, pointing toward domain randomized predictive control as an important and fruitful area for further study.
