<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scalar Federated Learning for Linear Quadratic Regulator

Topics include Federated learning, Control, Learning, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose ScalarFedLQR, a communication-efficient federated algorithm for model-free learning of a common policy in linear quadratic regulator (LQR) control of heterogeneous agents. The method builds on a decomposed projected gradient mechanism, in which each agent communicates only a scalar projection of a local zeroth-order gradient estimate. The server aggregates these scalar messages to reconstruct a global descent direction, reducing per-agent uplink communication from O(d) to O, independent of the policy dimension. Crucially, the projection-induced approximation error diminishes as the number of participating agents increases, yielding a favorable scaling law: larger fleets enable more accurate gradient recovery, admit larger stepsizes, and achieve faster linear convergence despite high dimensionality. Under standard regularity conditions, all iterates remain stabilizing and the average LQR cost decreases linearly fast. Numerical results demonstrate performance comparable to full-gradient federated LQR with substantially reduced communication.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy optimization (PO) is a promising paradigm for data-driven control. Despite nonconvexity, policy gradient (PG) methods enjoy global convergence in structured settings such as LQR. However, large-scale deployment on physical systems is constrained by two fundamental bottlenecks: (i) communication overload, as transmitting high-dimensional gradients under limited bandwidth becomes prohibitive and scales with fleet size; and (ii) sample inefficiency, since model-free PG requires $\mathcal{O}(1/\epsilon^{2})$ trajectory rollouts per step---untenable in real-world operation. Recent work partially mitigates these challenges: D2SPI addresses homogeneous networks, while FedLQR extends to heterogeneous but similar agents.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central, often underemphasized limitation underlying these bottlenecks is the *physical cost of each gradient sample*. In zeroth-order (ZO) model-free LQR, estimating $\nabla J(K)$ for $K\in\mathbb{R}^{n_{u}\times n_{x}}$ requires executing perturbed policies $\widehat{K}_{s}=K+U_{s}$, collecting trajectories, and averaging costs over $n_{s}$ perturbations via where $\widehat{J}_{s}=J(\widehat{K}_{s})$, achieving $\epsilon$-accurate gradients with $n_{s}=\mathcal{O}(1/\epsilon^{2})$. Crucially, each "sample" is not a cheap computation but a full trajectory rollout of length $\tau$ on a live system.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, this cost is tangible: a drone must interrupt its mission and expend battery, a power grid controller applies perturbations that stress equipment, and a robotic arm incurs production downtime. Reducing sample complexity is therefore not merely theoretical but essential for safe, continuous deployment of learning-based control. A key opportunity arises in large-scale multi-agent systems: when $M$ agents with similar (but not necessarily identical) dynamics pool trajectory data, the per-agent sampling burden decreases by a factor of $M$. As shown by Wang et al. in FedLQR, the requirement improves from $\mathcal{O}(1/\epsilon^{2})$ to $\mathcal{O}(1/(M\epsilon^{2}))$ by exploiting independent gradient noise across agents while optimizing average fleet performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its strengths, FedLQR faces two limitations at scale. First, requiring all $M$ agents to sample each round enforces continuous exploration, though this can be mitigated by subsampling since per-agent sample complexity already scales as $\mathcal{O}(1/(M\epsilon^{2}))$. Second, and more fundamentally, each agent must transmit a full gradient matrix $\Delta^{(i)}\in\mathbb{R}^{n_{u}\times n_{x}}$, incurring $\mathcal{O}(d)$ uplink cost and a total server burden of $\mathcal{O}(Md)$ with $d=n_{u}n_{x}$. This cost grows with both fleet size and system dimension---precisely where collaboration is most valuable---and additionally exposes sensitive local dynamics through gradient inversion attacks. These limitations motivate our approach: achieving constant-size uplink with built-in structural privacy, decoupling communication from system dimension while retaining guaranteed fast federated learning and iterative stability.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose ScalarFedLQR, which resolves this tension by compressing the uplink via *projected directional derivatives*. Rather than transmitting the full gradient $\nabla J(K)\in\mathbb{R}^{d}$, each participating agent computes a local zeroth-order estimate $\widehat{\nabla}J(K)$, samples a Rademacher direction $v\in{\pm 1}^{d}$ using a shared pseudorandom generator, and sends only the scalar projection $\langle v,\widehat{\nabla}J(K)\rangle$ along with the seed. The server reconstructs $v$ deterministically from the seed and aggregates these scalar messages to obtain a global descent direction. This reduces per-agent communication from $\mathcal{O}(d)$ to $\mathcal{O}$ and total server cost from $\mathcal{O}(Md)$ to $\mathcal{O}(M)$ for $M$ active agents, independent of system dimension.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The induced error decomposes into projection distortion and zeroth-order estimation noise, jointly governed by sample size, dimension, and fleet size.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under standard regularity conditions on the average LQR cost (e.g., a Polyak--Łojasiewicz condition with constant $\mu_{c}$ and local Lipschitz continuity with $L_{c}$ over a stabilizing sublevel set), we establish linear convergence: Theorem. (Linear convergence---Informal) *If the local zeroth-order relative errors are bounded by $\epsilon$ and* *then, with a suitable constant stepsize and probability at least $1-\delta$, ScalarFedLQR achieves geometric decay of the average cost at rate $1-(\mu_{c}/L_{c}){(1-\beta)^{2}}/{(1+\beta)^{2}}.$ $\Box$* This result highlights a key large-scale advantage: although scalar projection introduces dimension-dependent error, averaging across agents reduces its impact as $M$ grows. Consequently, larger fleets admit smaller $\beta$, enabling larger stepsizes and faster linear convergence---even in high dimensions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, smaller or noisier settings require more conservative updates. Thus, ScalarFedLQR achieves a compounding benefit at scale: scalar per-agent communication with improving stability and convergence as fleet size increases.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. §II formulates the federated model-free LQR problem and introduces the stabilizing set and similarity assumptions. §III presents the ScalarFedLQR algorithm and §IV analyzes its stability and convergence properties, including high-probability bounds on the scalar-projection error and linear convergence under a PL condition. §V provides numerical experiments comparing ScalarFedLQR with FedLQR under varying levels of heterogeneity and communication budgets. §VI concludes the paper and outlines directions for future work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation and Objective", "weight": 1.0} -->

We consider a network of $M$ agents, each governed by discrete-time linear time-invariant (LTI) dynamics where $x^{(n)}_{t}\in\mathbb{R}^{n_{x}}$ and $u^{(n)}_{t}\in\mathbb{R}^{n_{u}}$ denote the state and control input of agent $n$, and the system matrices $(A^{(n)},B^{(n)})$ are unknown and may vary across agents. All agents share the same state and input dimensions but may exhibit heterogeneous dynamics.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (Similarity of dynamics)", "weight": 1.0} -->

There exists a nominal linear model $(A,B)$ such that for all agents $n$, for some heterogeneity parameters $\epsilon_{1},\epsilon_{2}\geq 0$. $\Box$ This similarity assumption captures the setting in which agents have distinct but closely related dynamics, ensuring the existence of a meaningful common policy.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Similarity of dynamics)", "weight": 1.0} -->

Each agent applies a static state-feedback control law $u^{(n)}_{t}=-Kx^{(n)}_{t}$, where $K\in\mathbb{R}^{n_{u}\times n_{x}}$ is a common policy gain to be learned cooperatively. Under this policy, agent $n$ incurs the infinite-horizon quadratic cost where $Q\succeq 0$ and $R\succ 0$ are fixed cost matrices shared by all agents. The goal of federated learning is to compute a *single* policy gain $K$ that minimizes the average LQR cost We emphasize that this objective differs from classical distributed control, where each agent learns its own policy. Here, we instead learn a *common policy* across agents, leveraging similarity in dynamics to accelerate learning through data aggregation. While such a policy is not individually optimal, it provides a robust baseline that generalizes across agents and can be locally fine-tuned if needed. This setup enables fast fleet-level learning while retaining adaptability.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1 (Similarity of dynamics)", "weight": 1.0} -->

The central challenge, however, is stability: under heterogeneous dynamics, a policy that stabilizes one agent may destabilize another, making the design of a *commonly stabilizing policy* the key difficulty in federated LQR. We therefore define the per-agent stabilizing set and let $\mathcal{S}:=\bigcap_{n=1}^{M}\mathcal{S}^{(n)}$ denote the set of gains that stabilize all agents simultaneously. Each $\mathcal{S}^{(n)}$ is nonempty and open whenever $(A^{(n)},B^{(n)})$ is stabilizable, and $\mathcal{S}$ inherits these properties under the following assumption.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2 (Initial stabilizing policy)", "weight": 1.0} -->

There exists $K_{0}\in\mathcal{S}$ that stabilizes all agents simultaneously. $\Box$ This assumption is standard in policy optimization and can be satisfied via conservative model-based design, offline analysis, or a simple baseline controller when the dynamics are open-loop stable. Fully online stabilization is beyond the scope of this work. Additional topological properties of $\mathcal{S}$---particularly under the *similar dynamics* hypothesis---are of independent interest but not central to our analysis.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2 (Initial stabilizing policy)", "weight": 1.0} -->

Given $K_{0}\in\mathcal{S}$, the federated optimization problem is We additionally impose a *communication constraint*: agents may not transmit full policy gains or high-dimensional gradient vectors to the server and are instead restricted to a constant-size message per round. This models realistic bandwidth and energy limitations in large-scale multi-agent systems and is treated as integral to the problem formulation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2 (Initial stabilizing policy)", "weight": 1.0} -->

Accordingly, the objective of this work is to design a federated policy optimization scheme that (i) minimizes the average LQR cost, (ii) maintains all iterates within the common stabilizing set $\mathcal{S}$, and (iii) operates under a communication model in which each agent transmits only $\mathcal{O}$ information per round. In the next section, we present a federated algorithm that operates under this communication model and analyze its stability and convergence properties.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2 (Initial stabilizing policy)", "weight": 1.0} -->

1:Input: initial stabilizing gain K0, learning rate η, rounds T 2:for each round t = 0, 1, …, T − 1 do 3: Server broadcasts Kt to all n ∈ [M] 4: for each client n ∈ [M] in parallel do 5: Generate i.i.d.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2 (Initial stabilizing policy)", "weight": 1.0} -->

$\bar{g}_{t}\leftarrow\frac{d}{M}\,\Delta_{\mathrm{sum}}$ Algorithm 1 ScalarFedLQR: Federated LQR via Scalar Gradient Projections

<!-- chunk {"id": "body-0021", "role": "body", "section": "ScalarFedLQR Algorithm", "weight": 1.0} -->

We present ScalarFedLQR (Algorithm 1), a communication-efficient federated policy optimization method for LQR systems. At each round $t$, the server broadcasts the current policy gain $K_{t}$ to all agents. Each agent $n$ computes a local zeroth-order estimate of its policy gradient, using trajectory rollouts under the current policy.

<!-- chunk {"id": "body-0022", "role": "body", "section": "ScalarFedLQR Algorithm", "weight": 1.0} -->

Instead of transmitting the full gradient vector, each agent samples a random Rademacher direction $v_{t,n}\in\{-1,+1\}^{d}$ using a locally generated random seed, normalizes it, and forms the scalar projection The agent uploads only this scalar together with the corresponding seed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "ScalarFedLQR Algorithm", "weight": 1.0} -->

On the server side, the same random directions are deterministically regenerated using the received seeds. The server then constructs an aggregated descent direction according to The shared policy is updated via the gradient descent step where $\eta>0$ is the stepsize.

<!-- chunk {"id": "body-0024", "role": "body", "section": "ScalarFedLQR Algorithm", "weight": 1.0} -->

Under this protocol, each agent transmits only a single real-valued scalar and an integer-valued seed per round. As a result, the uplink communication cost per agent is $\mathcal{O}$, independent of the policy dimension $d=n_{u}n_{x}$. The server-side computation scales linearly with the number of participating agents.

<!-- chunk {"id": "body-0025", "role": "body", "section": "ScalarFedLQR Algorithm", "weight": 1.0} -->

The following sections analyze how the approximation error introduced by scalar projection and zeroth-order estimation affects stability and convergence, and establish conditions under which the iterates produced by ScalarFedLQR remain stabilizing and converge to the average optimal policy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stability analysis and convergence of ScalarFedLQR", "weight": 1.0} -->

We now study the stability and convergence properties of ScalarFedLQR. For technical reasons that becomes apparent later, our analysis essentially will focus on the $c$ sublevel set defined as which contains $K_{0}$ and will be contained in $\mathcal{S}$ given that $Q\succ 0$ and $R\succ 0$. Our goal is to show that, under suitable conditions on the stepsize and the gradient approximation error, the server-side iterates generated by Algorithm 1 remain within a stabilizing sublevel set $\mathcal{S}_{c}$ of the average cost $J_{\mathrm{avg}}$. Compared with standard FedLQR, the main technical challenge is that the server does *not* receive full local gradient vectors. Instead, it reconstructs an aggregated update direction from scalar projections.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stability analysis and convergence of ScalarFedLQR", "weight": 1.0} -->

To analyze the effect of this approximation, we first quantify how a single iteration of ScalarFedLQR changes the average cost when the server updates the policy along the approximate direction $\bar{g}_{t}$ rather than the exact gradient $\nabla J_{\mathrm{avg}}(K_{t})$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Stability analysis and convergence of ScalarFedLQR", "weight": 1.0} -->

Our analysis relays on standard local smoothness and local Polyak--Łojasiewicz (PL) condition of $J_{\mathrm{avg}}$ that needs to hold only on the sublevel set $\mathcal{S}_{c}$---rather than on entire $S$. Subsequently, these conditions will be used to guarantee iterative stability and linear decay rate, respectively.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3 (Local smoothness and local PL condition on $\\mathcal{S}_{c}$)", "weight": 1.0} -->

There exist constants $L_{c}>0$ and $\mu_{c}>0$ such that for all $K\in\mathcal{S}_{c}$, where $J_{\mathrm{avg}}^{\star}:=\inf_{K\in\mathcal{S}_{c}}J_{\mathrm{avg}}(K)$. $\Box$ This assumption is known to hold in the absence of heterogeneity (i.e., when $\epsilon_{1}=\epsilon_{2}=0$ in (3. ‣ II Problem Formulation and Objective ‣ Scalar Federated Learning for Linear Quadratic Regulator"))) provided that $Q\succ 0$ and $R\succ 0$. While it is also expected to hold in the heterogeneous case, we defer its detailed analysis to our future work.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3 (Local smoothness and local PL condition on $\\mathcal{S}_{c}$)", "weight": 1.0} -->

Let $\tilde{g}_{t}$ denotes the average of the local zeroth-order gradient estimators, while $g_{t}$ is the exact gradient of the average cost at the current policy $K_{t}$: The discrepancy between the server-side aggregated direction $\bar{g}_{t}$ and the true gradient $g_{t}$ reflects both the scalar-projection reconstruction error and the zeroth-order gradient estimation error.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3 (Local smoothness and local PL condition on $\\mathcal{S}_{c}$)", "weight": 1.0} -->

The following result gives a one-step descent guarantee for $J_{\mathrm{avg}}$ under the scalar-projection aggregated update. In particular, it shows that descent is ensured when the total error is sufficiently small relative to $\|g_{t}\|_{2}$ and the stepsize is chosen appropriately.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 4 (Bounded gradient heterogeneity)", "weight": 1.0} -->

For each round $t$, let $\Delta_{t,n}:=\tilde{g}_{t,n}-\tilde{g}_{t},$ and $\tilde{g}_{t}:=\frac{1}{M}\sum_{n=1}^{M}\tilde{g}_{t,n}.$ Assume that there exist nonnegative quantities $\sigma_{t}$ and $B_{t}$ such that Such bounded gradient heterogeneity (gradient dissimilarity) assumptions are common in federated optimization. They quantify how much each client's local gradient $\tilde{g}_{t,n}$ can deviate from the round average $\tilde{g}_{t}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Linear convergence under a PL condition", "weight": 1.0} -->

Theorem 1. ‣ IV Stability analysis and convergence of ScalarFedLQR ‣ Scalar Federated Learning for Linear Quadratic Regulator") establishes that, under a suitable uniform control of the total gradient error and an appropriate stepsize choice, the iterates of ScalarFedLQR remain in the stabilizing set $\mathcal{S}_{c}$ throughout the optimization horizon. Having secured this global stability guarantee, we now turn to the convergence behavior of the algorithm within $\mathcal{S}_{c}$. In particular, combining the one-step descent result of Lemma 1. ‣ IV Stability analysis and convergence of ScalarFedLQR ‣ Scalar Federated Learning for Linear Quadratic Regulator") with the PL condition on $J_{\mathrm{avg}}$, we strengthen the stability result to a linear convergence rate.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

This section evaluates the performance of ScalarFedLQR in the model-free federated LQR setting. To ensure a fair and direct comparison, we adopt the same numerical setup and system-generation procedure as in the FedLQR framework. In particular, all experiments use identical system dynamics, heterogeneity construction, and cost matrices, with the only difference being the learning algorithm and communication mechanism.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-1 System Generation", "weight": 1.0} -->

We consider a collection of $M$ heterogeneous discrete-time linear time-invariant (LTI) systems of the form where each system has state dimension $n_{x}=3$ and input dimension $n_{u}=3$. Following the construction, the agent dynamics are generated to satisfy a bounded heterogeneity condition. Specifically, a nominal pair $(A_{0},B_{0})$ is fixed, from which the heterogeneous agent dynamics are generated by structured perturbation: where $Z_{1},Z_{2}\in\mathbb{R}^{3\times 3}$ are fixed modification masks, and $\gamma_{1}^{(n)}\sim\mathcal{U}(0,\epsilon_{1})$ and $\gamma_{2}^{(n)}\sim\mathcal{U}(0,\epsilon_{2})$ are random perturbation levels.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-1 System Generation", "weight": 1.0} -->

The parameters $\epsilon_{1},\epsilon_{2}>0$ control the degree of heterogeneity across agents in (3. ‣ II Problem Formulation and Objective ‣ Scalar Federated Learning for Linear Quadratic Regulator")). The nominal system itself is included in the population by setting $(A^{},B^{})=(A_{0},B_{0})$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-1 System Generation", "weight": 1.0} -->

The nominal system and cost matrices are given by and $Q=2I_{3},R=\tfrac{1}{2}I_{3}.$ Throughout our simulations, we consider the following initial stabilizing controller $K_{0}=1.62I_{3}$. This control gain is used only to initialize a stabilizing policy for both algorithms, and is ensured to be stabilizing for all agents provided that $\epsilon_{1}$ and $\epsilon_{2}$ are small enough.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-2 Experimental Protocol", "weight": 1.0} -->

All agents perform model-free PO using local trajectory rollouts to estimate policy gradients. Unless otherwise stated, all methods are evaluated under the same simulation and sampling configuration as. In particular, the number of agents is fixed to $M=10$, the total number of communication rounds is $T=2000$, and the stepsize is set to $\eta=0.01$ for both algorithms. For the zeroth-order gradient estimator, each local gradient estimate is computed using $N_{\mathrm{traj}}=5$ trajectories, rollout length $\tau=15$, and smoothing radius $r=0.1$. Each reported curve is averaged over $10$ independent Monte Carlo runs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-2 Experimental Protocol", "weight": 1.0} -->

To quantify communication, we count each transmitted scalar as a $32$-bit floating-point number. Therefore, FedLQR incurs an uplink cost proportional to the full gradient dimension (here $n_{u}\times n_{x}=9$), whereas ScalarFedLQR incurs only scalar-level communication per agent per round.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-2 Experimental Protocol", "weight": 1.0} -->

To assess the performance of the algorithms, we consider the *normalized optimality gap* ${[J_{\mathrm{avg}}(K)-J_{\mathrm{avg}}(K_{\mathrm{avg}}^{\star})]}/{J_{\mathrm{avg}}(K_{\mathrm{avg}}^{\star})}$ versus iteration rounds as a measure of convergence. In practice, however, the population-optimal common controller $K_{\mathrm{avg}}^{\star}$ is generally hard to compute exactly for a heterogeneous collection of systems.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-2 Experimental Protocol", "weight": 1.0} -->

Therefore, in the numerical experiments we instead use the optimal controller of the nominal system (equivalently, agent $1$), denoted by $K_{1}^{\star}$, as a feasible reference policy, and we report the normalized reference gap ${[J_{1}(K)-J_{1}(K_{1}^{\star})]}/{J_{1}(K_{1}^{\star})}.$ Explicitly, $K_{1}^{*}$ is obtained by solving the discrete algebraic Riccati equation (DARE) with parameter $(A_{0},B_{0},Q,R)$. Thus, the plotted quantity measures suboptimality relative to the nominal-agent optimum rather than the exact population-average optimum.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-3 Results", "weight": 1.0} -->

In order to also compare the communication requirement, we look at the percentages of cost improvement versus total number of bits transferred by each algorithm. The main advantage of ScalarFedLQR appears when performance is measured against communication cost. As shown in Fig. 2(a), for a fixed number of transmitted bits, ScalarFedLQR consistently attains a higher recovery percentage $1-\text{normalized optimality gap}$ than FedLQR. This reflects the fact that ScalarFedLQR replaces full uplink gradient transmission by scalar communication, thereby using the available communication budget much more efficiently. The benefit is especially clear at the fixed budget of $6\times 10^{5}$ bits. In the low heterogeneity setting, Fig. 2(b) shows that ScalarFedLQR achieves $54.2\%$ recovery, compared with $29.1\%$ for FedLQR, which corresponds to a gain of $25.1$ percentage points.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-3 Results", "weight": 1.0} -->

In the higher-heterogeneity setting, Fig. 2(c) shows that ScalarFedLQR still achieves $30.7\%$ recovery, compared with $13.6\%$ for FedLQR, corresponding to a gain of $17.1$ percentage points.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-3 Results", "weight": 1.0} -->

Overall, these results show that ScalarFedLQR preserves performance comparable to FedLQR when measured by communication rounds, while yielding a substantial reduction in communication cost and significantly higher recovery under a fixed bit budget regardless of heterogeneity levels. Finally, although the present experiments keep the model-free oracle fixed across methods, the results can be further improved by strengthening the zeroth-order gradient estimates, for example by increasing the number of rollouts or the trajectory length. We emphasize, however, that this is not the main focus of the paper; the central claim is the communication-efficiency gain achieved by scalar uplink transmission. The simulation code is available online.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced ScalarFedLQR, a communication-efficient federated algorithm for model-free linear quadratic regulator (LQR) control with heterogeneous agents. By replacing full policy-gradient transmission with a single scalar projection of each local zeroth-order gradient estimate, the proposed method reduces the per-agent uplink communication cost from $\mathcal{O}(d)$ to $\mathcal{O}$, independently of the policy dimension. We showed that the aggregated scalar-projection update defines a valid descent direction whose approximation error improves with the number of participating agents. Under standard stability and regularity conditions, we established that all iterates remain stabilizing and that ScalarFedLQR converges linearly to the optimal average policy. Numerical experiments further confirmed that the proposed method achieves performance comparable to full-gradient federated LQR while significantly reducing communication. Future work includes sharpening the convergence analysis of ScalarFedLQR under more general heterogeneity and oracle conditions while preserving its communication-efficiency advantages.
