<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning

Topics include Reinforcement learning, Control barrier functions, Safety, Robustness, Uncertainty, Benchmarks, Scalability, Online algorithms, Control, Learning, Robust control, Inverted pendulum.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robust control barrier functions (CBFs) provide a principled mechanism for smooth safety enforcement under worst-case disturbances. However, existing approaches typically rely on explicit, closed-form structure in the dynamics (e.g., control-affine) and uncertainty models. This has led to limited scalability and generality, with most robust CBFs certifying only conservative subsets of the maximal robust safe set. In this paper, we introduce a new robust CBF framework for general nonlinear systems under bounded uncertainty. We first show that the safety value function solving the dynamic programming Isaacs equation is a valid robust discrete-time CBF that enforces safety on the maximal robust safe set. We then adopt the key reinforcement learning (RL) notion of quality function (or Q-function), which removes the need for explicit dynamics by lifting the barrier certificate into state-action space and yields a novel robust Q-CBF constraint for safety filtering. Combined with adversarial RL, this enables the synthesis and deployment of robust Q-CBFs on general nonlinear systems with black-box dynamics and unknown uncertainty structure.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate the framework on a canonical inverted pendulum benchmark and a 36-D quadruped simulator, achieving substantially less conservative safe sets than barrier-based baselines on the pendulum and reliable safety enforcement even under adversarial uncertainty realizations on the quadruped.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safety-critical systems are increasingly deployed in real-world environments, where uncertainty is unavoidable and even a single safety violation may have catastrophic consequences. This calls for a *robust safety filter*, a runtime process that monitors the system's operation and intervenes, when necessary, by modifying the control input to preserve safety against all admissible uncertainty realizations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among robust safety filters, robust control barrier functions (CBFs) are often sought after because they enable smooth intervention by solving a safety-enforcing optimal control problem (OCP) at each timestep. Despite their popularity, however, current robust CBF approaches face important challenges. Most robust CBF schemes require *explicit knowledge* of the control-affine dynamical model for offline synthesis, runtime constraint evaluation, or, in many cases, both. They also rely on domain-specific structural assumptions of the uncertainty to bound or tractably compute its effect on the dynamics or on the barrier derivative. Data-driven extensions alleviate some modeling burden, but still assume substantial model structure, such as closed-form nominal models and known error bounds. As a result, synthesizing and deploying robust CBFs for systems with complex, possibly black-box dynamics and uncertainty structure remains an outstanding challenge. Moreover, depending on how uncertainty is handled, these methods often become *overly conservative* and certify only subsets of the maximal robust safe set.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hamilton--Jacobi--Isaacs (HJI) reachability analysis offers a complementary route to robust safety by formulating safety under bounded disturbance, which represents predictive uncertainty such as unknown model error and external perturbations, as a zero-sum game whose value function encodes the maximal robust safe set. Although classical HJI methods scale poorly with state dimension, recent reinforcement learning (RL)-based methods have shown that safety value functions and best-effort safety policies can be synthesized and deployed on high-dimensional uncertain systems with black-box dynamics. Recent work has also made the connection between reachability analysis and CBFs more precise by showing that safety value functions can themselves serve as barrier-like safety certificates. These developments suggest that reachability analysis can serve as a principled and scalable route to synthesizing robust CBFs that certify and enforce safety over the maximal robust safe set, even for systems with black-box dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we draw a key insight from RL---the quality function ---that lifts the safety value function into a state--control--disturbance representation, enabling CBF-based safety filtering without explicit dynamics or uncertainty models. We consider systems available only as *black-box* transition mechanisms: given the current state, a control input, and a bounded disturbance input, the simulator or physical system returns the next state. Within this setting, we show that the safety value function itself is a valid robust discrete-time control barrier function (DCBF), and that its state--control--disturbance lift yields a novel robust $\mathcal{Q}$-CBF constraint for safety filtering on *black-box systems with unknown dynamics and uncertainty structure*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce the robust $\mathcal{Q}$-CBF framework for *black-box* nonlinear systems under bounded uncertainty. We formally show that the safety value function---solution to the dynamic programming Isaacs equation---is a valid robust DCBF on the *maximal* robust safe set, and that its state--action lift yields a novel robust CBF constraint for smooth safety filtering under uncertainty.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging reachability-based adversarial RL, we develop a scalable robust $\mathcal{Q}$-CBF synthesis and deployment pipeline for high-dimensional systems without requiring explicit dynamics, control-affine assumptions, prescribed uncertainty structure, or manual barrier function design.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate the proposed framework on a disturbed inverted pendulum and a high-fidelity quadrupedal locomotion simulation governed by 36-dimensional black-box dynamics. On the pendulum, the learned robust $\mathcal{Q}$-CBF nearly recovers the maximal robust safe set and is substantially less conservative than barrier-based baselines. On the quadruped, it reliably enforces safety under adversarial uncertainty realizations while achieving efficient forward locomotion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Robust Safety under Bounded Uncertainty", "weight": 1.0} -->

Throughout this work, we consider a discrete-time system with nonlinear dynamics

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Robust Safety under Bounded Uncertainty", "weight": 1.0} -->

where at each time $t$, $x_{t} \in \mathcal{X}$ is the system's state, $u_{t} \in \mathcal{U}$ is the control input, and $d_{t} \in \mathcal{D}$ is an unknown but bounded disturbance input representing predictive uncertainty. We further consider a failure set $\mathcal{F} \subset \mathcal{X}$ of states that are deemed unacceptable and must be categorically avoided at all times. The geometry of $\mathcal{F}$ may be arbitrary; by convention, we assume only that it is an open set and can therefore be characterized through some continuous margin function $g:{\mathcal{X}\rightarrow{\mathbb{R}}}$ (e.g., a signed distance function) as

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Robust Safety under Bounded Uncertainty", "weight": 1.0} -->

These assumptions can be viewed as specifying an *operational design domain (ODD)*, namely the set of operating conditions under which the system is expected to function correctly and safely. In particular, the bounded disturbance set $\mathcal{D}$, together with the modeling assumptions, delineates the operating conditions under which the guarantees are intended to hold.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Robust Safety under Bounded Uncertainty", "weight": 1.0} -->

A widely used approach to enforcing safety under uncertainty is robust CBF, which certifies forward invariance of a (usually conservative) subset of the maximal robust safe set.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Robust Continuous-Time Control Barrier Function", "weight": 1.0} -->

The existing robust-CBF literature is predominantly formulated in continuous time, so we begin by recalling the robust continuous-time CBF before returning to the discrete-time setting of primary interest in subsection II-C.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

Since (5. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) is imposed only on $\Omega$, $\alpha$ may be taken from the standard class-$\mathcal{K}$ family. Extended class-$\mathcal{K}$ or extended class-$\mathcal{K}_{\infty}$ functions are needed when the barrier condition is imposed globally on $\mathcal{X}$, so that negative values of $h$ are also allowed, while class-$\mathcal{K}_{\infty}$ or extended class-$\mathcal{K}_{\infty}$ choices are natural when the range of $h$ is unbounded. Such global formulations may additionally encode set-attractiveness properties, but this loses significance when $h$ encodes $\Omega^{\ast}$, since outside $\Omega^{\ast}$ there exists no control policy that can guarantee safety against all admissible disturbances.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

Now, we explain why existing robust CBF formulations can be viewed as special cases of Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning").

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

In many of these works, the required closed-form structure appears directly through the computation of $\overset{˙}{h}$, for example via Lie-derivative terms such as $L_{f}h{(x)}$ and $L_{g}h{(x)}$, together with a specific description of how uncertainty affects the dynamics or the barrier derivative. The model captures many of the uncertainty descriptions used across the robust CBF literature, including additive or multiplicative disturbances, structured parametric uncertainty, and sector-bounded input uncertainty. These structured system classes can therefore be viewed as special cases of the more general uncertain dynamics (4. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")). In our framework, by contrast, we assume neither control-affine structure, explicit knowledge of the dynamics, nor prescribed uncertainty structure for CBF synthesis or runtime evaluation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

One major line of work handles uncertainty by incorporating a compensation term $\sigma$ into the CBF constraint, for example in the form

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

Constructing $\sigma$ requires sufficient prior knowledge of the uncertainty structure, for example worst-case disturbance bounds, parameter estimation error bounds, or observer error bounds, to upper-bound the contribution of uncertainty to $\overset{˙}{h}$. Such methods fit naturally within Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning"), but they can be conservative because they upper-bound the worst-case effect of uncertainty rather than handling it explicitly. As a result, the robust safe set $\Omega$ is often a strict subset of the maximal robust safe set $\Omega^{\ast}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

A second line of work keeps the worst-case effect of uncertainty explicit by retaining the inner minimization over $d \in \mathcal{D}$ in (5. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")), rather than introducing a compensation term. Representative examples include duality-based reformulations of the inner minimization, sector-bounded input uncertainty, and convex hull disturbance models. Because they preserve the state- and input-dependent worst-case effect of uncertainty, these approaches may be less conservative than compensation-based methods, but they still require a tractable uncertainty representation and sufficient explicit knowledge of the system to validate a robust CBF and evaluate the inner minimization. A particularly relevant reachability-based variant is the robust control barrier-value function framework, which recovers the maximal robust safe set by constructing the certificate as the viscosity solution of a HJI variational inequality.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

Our robust $\mathcal{Q}$-CBF framework improves on this work by removing the need for runtime deployment to rely on control- and disturbance-affine dynamics with known closed-form expressions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

Data-driven approaches have also been adopted for robust barrier or certificate synthesis. Lindemann et al. learn robust output CBFs from safe expert demonstrations, and Taylor et al. develop a broader data-driven robust control synthesis framework based on control certificate functions under actuation uncertainty. Despite leveraging data, these methods still assume substantial model structure, such as known nominal control-affine system models and model error bounds, which are then used to validate the certificates.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1 (Choice of Function $\\alpha$ in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\"))", "weight": 1.0} -->

Taken together, the robust continuous-time CBF formulations reviewed above can all be viewed as instances of Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning"), but only under stronger structural assumptions. To synthesize a robust CBF or evaluate the corresponding constraint online, these methods typically rely on explicit knowledge of the control-affine system dynamics, together with prescribed structure for how uncertainty affects the dynamics or the barrier derivative. Moreover, they are often more conservative than necessary, certifying only subsets of the maximal robust safe set. By contrast, as shown in section III and section IV, our robust $\mathcal{Q}$-CBF framework treats the uncertain system as a *black-box*. For both synthesis and runtime evaluation, it requires neither control-affine assumptions, explicit knowledge of the dynamics, nor prescribed uncertainty structure, while still recovering the maximal robust safe set.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Robust Discrete-Time Control Barrier Function", "weight": 1.0} -->

We now make explicit how the robust continuous-time CBF in Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning") relates to the discrete-time system of interest. If a class-$\mathcal{K}$ function $\alpha$ is locally Lipschitz, then it can be associated with a class-$\mathcal{K}\mathcal{L}$ function $\beta_{\alpha}$ by defining, for each $r \geq 0$, the map $\beta_{\alpha}{(r, \cdot )}$ as the solution of the initial value problem ${\overset{˙}{y} = {- {\alpha{(y)}}}},{{y{}} = r}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Robust Discrete-Time Control Barrier Function", "weight": 1.0} -->

Recall that a class-$\mathcal{K}\mathcal{L}$ function is class-$\mathcal{K}$ in its first argument and, for each fixed $r \geq 0$, is nonincreasing in its second argument and converges to $0$ as $t\rightarrow\infty$. Under sampling with period $\Deltat$, the continuous-time robust CBF condition (5. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) induces the one-step discrete-time condition ${h{(x_{t + 1})}} \geq {\beta_{\alpha}{({h{(x_{t})}},{\Deltat})}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Robust Discrete-Time Control Barrier Function", "weight": 1.0} -->

For a fixed sampling period $\Deltat$, the map $r\mapsto{\beta_{\alpha}{(r,{\Deltat})}}$ is itself class-$\mathcal{K}$, and with a slight abuse of notation we denote this induced one-step map simply by $\beta{(r)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Robust Discrete-Time Control Barrier Function", "weight": 1.0} -->

Motivated by this continuous--discrete connection, we now introduce the robust DCBF for the discrete-time uncertain dynamics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

To close the conservativeness gap discussed above, we turn to Hamilton--Jacobi--Isaacs (HJI) reachability analysis.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

where the *safety value function* $V:{\mathcal{X}\rightarrow{\mathbb{R}}}$ encodes the minimal margin that the controller can maintain at all times under the worst-case disturbance. Notably, the inner $\max_{u}\min_{d}$ ordering grants the disturbance an instantaneous *informational advantage* by allowing it to react to the controller's chosen input at each timestep. Consequently, the maximal robust safe set is given by

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

We next adopt a key insight from RL: the quality function (action-value function). Specifically, we define the *state--control--disturbance safety value function* $\mathcal{Q}:{{\mathcal{X} \times \mathcal{U} \times \mathcal{D}}\rightarrow{\mathbb{R}}}$ to satisfy

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

This formulation remains equivalent to in the sense that

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

The introduction of $\mathcal{Q}$ lifts the safety certificate $V$ into a state--control--disturbance representation that directly underlies the robust $\mathcal{Q}$-CBF constraint developed later.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

We will also make use of the corresponding *safe fallback policy*

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-D Hamilton--Jacobi--Isaacs Reachability Analysis", "weight": 1.0} -->

which selects a control input maximizing the worst-case safety value.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Maximal Robust $\\mathcal{Q}$-CBF", "weight": 1.0} -->

In this section, we establish the main theoretical result underlying our robust $\mathcal{Q}$-CBF framework. Our key insight is that the safety value function $V$ itself is a valid robust DCBF whose $0$-superlevel set is the *maximal robust safe set* $\Omega^{\ast}$. It follows that, for every class-$\mathcal{K}$ function $\beta$ satisfying ${\beta{(r)}} \leq r$ for all $r \geq 0$, robust safety on $\Omega^{\ast}$ can be enforced through the state--control--disturbance safety value function $\mathcal{Q}$ via the constraint

<!-- chunk {"id": "body-0037", "role": "body", "section": "Maximal Robust $\\mathcal{Q}$-CBF", "weight": 1.0} -->

Crucially, once $V$ and $\mathcal{Q}$ are available, the $\mathcal{Q}$-CBF constraint can be evaluated from these value functions alone, without explicit closed-form dynamics, control-affine assumptions, or prescribed uncertainty structure. In this sense, the constraint admits *black-box* evaluation. Practical considerations for scalably synthesizing $V$ and $\mathcal{Q}$, together with handling the minimization over $d$ at runtime, are introduced in section IV. We now formalize this result.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 2 (Uncertainty-Free Special Case)", "weight": 1.0} -->

In the absence of uncertainty, the dynamics reduce to $x_{t + 1} = {f{(x_{t},u_{t})}}$ and the minimization over $d_{t}$ in (21b. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) disappears, yielding

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 2 (Uncertainty-Free Special Case)", "weight": 1.0} -->

This recovers the $\mathcal{Q}$-CBF constraint proposed.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2 (Uncertainty-Free Special Case)", "weight": 1.0} -->

We emphasize the key difference between the robust continuous-time CBF constraint (5. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")), the robust DCBF constraint (9b), and the robust $\mathcal{Q}$-CBF constraint (21b. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")). Both (5. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) and (9b) depend explicitly on the system dynamics, and therefore require explicit knowledge of the dynamics and uncertainty in order to evaluate the constraint. By contrast, the robust $\mathcal{Q}$-CBF constraint (21b.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2 (Uncertainty-Free Special Case)", "weight": 1.0} -->

‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) is posed directly in terms of the safety value functions $V$ and $\mathcal{Q}$. Thus, once $V$ and $\mathcal{Q}$ are available, evaluating (21b. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) no longer requires explicit closed-form dynamics, control-affine assumptions, or prescribed uncertainty structure. Together with the practical method introduced in section IV for handling the inner minimization over $d$ at runtime, this formulation enables safety enforcement for black-box dynamical systems.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2 (Uncertainty-Free Special Case)", "weight": 1.0} -->

The recursive feasibility of the robust $\mathcal{Q}$-CBF safety filter on the maximal robust safe set $\Omega^{\ast}$ is a direct consequence of the safety value function $V$ being a valid robust DCBF, as stated in Theorem 1. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning").

<!-- chunk {"id": "body-0043", "role": "body", "section": "Synthesizing and Deploying Robust $\\mathcal{Q}$-CBF", "weight": 1.0} -->

The robust $\mathcal{Q}$-CBF safety filter introduced in Section III is computationally challenging for high-dimensional systems, both during synthesis and at deployment. First, computing safety value function $\mathcal{Q}$ via direct solve of Isaacs equation is intractable due to the curse of dimensionality. In addition, deploying $\mathcal{Q}$-CBF safety filter at runtime requires optimizing disturbance input $d$ when evaluating ${\min_{d \in \mathcal{D}}\mathcal{Q}}{(x,u,d)}$ in the robust $\mathcal{Q}$-CBF constraint (21b. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")). This leads to a *nested* minimization over $d \in \mathcal{D}$, which is computationally intractable for high-dimensional disturbance spaces.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Synthesizing and Deploying Robust $\\mathcal{Q}$-CBF", "weight": 1.0} -->

In this section, we introduce scalable robust $\mathcal{Q}$-CBF synthesis and deployment procedures based on a recently proposed game-theoretic adversarial RL.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

Our robust $\mathcal{Q}$-CBF safety filter design assumes access to the state--control--disturbance safety value function $\mathcal{Q}$. Instead of directly solving the Isaacs equation, we propose to synthesize it through an adversarial RL process, where the controller and disturbance play a zero-sum dynamic game.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

Game-theoretic reinforcement learning. The adversarial RL jointly trains a critic (safety value) $\mathcal{Q}_{\omega}{(x,u,d)}$, controller actor $\pi_{\theta}^{u}{(x)}$, and disturbance actor $\pi_{\psi}^{d}{(x,u)}$. Here, we allow the disturbance to observe and react to the control input, making it a stronger and more targeted adversary.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

where $\xi = {(x,u,d,g^{\prime},x^{\prime})}$ is a transition sampled from the replay buffer $\mathcal{B}$, $u^{\prime} \sim \pi_{\theta}^{u}{( \cdot \mid x^{\prime})}$, $d^{\prime} \sim \pi_{\psi}^{d}{( \cdot \mid x^{\prime},u^{\prime})}$, $g^{\prime}:={g{(x^{\prime})}}$, $\gamma_{ENV} \in {}$ is the discount factor, and $\mathcal{Q}_{\omega^{\prime}}$ is a slowly updated target critic. Following standard adversarial RL practice, the controller maximizes critic $\mathcal{Q}_{\omega}$ (with an additional exploration term) while the disturbance minimizes the same critic.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

GDA with finite timescale separation. In order to seek a minimax equilibrium of the safety game, we leverage gradient descent-ascent (GDA) with finite timescale separation between the learning rates of the controller and disturbance. Specifically, the disturbance's policy parameters $\psi$ are updated on a faster timescale than the controller parameters $\theta$. This strategy stabilizes learning by encouraging the disturbance actor to track a near-best response to the current controller actor. Formally, it has been shown in Wang and Hu et al. that the two-timescale RL training guarantees convergence to a local minimax equilibrium $(\pi_{\theta^{\ast}}^{u},\pi_{\psi^{\ast}}^{d})$ in the policy space. At such an equilibrium, the learned disturbance policy represents a locally best-effort worst-case response to the controller, yielding a principled approximation of the inner minimization ${\min_{d \in D}\mathcal{Q}}{(x,u,d)}$ in constraint (21b.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) and enabling tractable computation of the robust $\mathcal{Q}$-CBF safety filtering at runtime.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

Training a best-response disturbance policy. While the GDA-trained disturbance policy $\pi_{\psi^{\ast}}^{d}:{x\mapsto d}$ is a worst-case response to the equilibrium control policy $\pi_{\theta^{\ast}}^{u}:{x\mapsto u}$, it does not necessarily minimize the critic $\mathcal{Q}_{\omega^{\ast}}$ for arbitrary control inputs generated by $\mathcal{Q}$-CBF optimization (21. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")), which may be exploitable. To ensure local robustness of $\mathcal{Q}$-CBF, we further train a *best-response disturbance policy* $\pi_{\overset{\sim}{\psi}}^{d}$ for a range of diverse control policies.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Synthesizing Robust $\\mathcal{Q}$-CBF via Game-theoretic RL", "weight": 1.0} -->

We do so by training the disturbance policy $\pi_{\psi}^{d}$ by minimizing $\mathcal{Q}_{\omega}{(x,u,d)}$ with respect to $d$, where $(x,u)$ pairs are sampled from a diverse set of control policies that play against the disturbance. In practice, we collect these control policies from checkpoints of multiple RL training runs with different random seeds, thereby exposing the disturbance policy to a broad distribution of controller behaviors. This procedure encourages $\pi_{\overset{\sim}{\psi}}^{d}{(x,u)}$ to approximate a local minimizer of the critic across the entire state--control space.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Real-time Safety Filtering with Robust Neural $\\mathcal{Q}$-CBF", "weight": 1.0} -->

At runtime, the neural-approximated disturbance policy $\pi_{\overset{\sim}{\psi}}^{d}{(x,u)}$ allows for efficient evaluation of ${\min_{d \in \mathcal{D}}\mathcal{Q}}{(x,u,d)}$ inside the robust $\mathcal{Q}$-CBF constraint (21b. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")). Specifically, we use the plug-in approximation $\overset{\sim}{d} = {\pi_{\overset{\sim}{\psi}}^{d}{(x,u)}}$ to obtain $\mathcal{Q}{(x,u,\overset{\sim}{d})}$ as a tractable surrogate of the worst-case safety value. This substitution removes the need for nested optimization in $\mathcal{Q}$-CBF safety filtering (21.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Real-time Safety Filtering with Robust Neural $\\mathcal{Q}$-CBF", "weight": 1.0} -->

‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) by reducing constraint evaluation (21b. ‣ III Maximal Robust 𝒬-CBF ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning")) to a single forward pass through the disturbance policy network and safety critic. Importantly, this plug-in choice is not arbitrary: $\pi_{\overset{\sim}{\psi}}^{d}$ is trained as a best-response policy that minimizes the safety critic against arbitrary control policies within the same safety game defined. Since $\pi_{\overset{\sim}{\psi}}^{d}$ is locally worst-case, any nearby disturbance realization would produce a less adversarial disturbance action at runtime.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Real-time Safety Filtering with Robust Neural $\\mathcal{Q}$-CBF", "weight": 1.0} -->

As a result, enforcing the robust $\mathcal{Q}$-CBF constraint assuming the neural disturbance action $\overset{\sim}{d} = {\pi_{\overset{\sim}{\psi}}^{d}{(x,u)}}$ automatically guarantees safety against all disturbance realizations that are sufficiently close. This insight is formalized in the following proposition; the proof follows directly from local optimality of $\pi_{\overset{\sim}{\psi}}^{d}{(x,u)}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 3 (Safety Verification)", "weight": 1.0} -->

While the use of function approximators in neural $\mathcal{Q}$-CBF safety filtering precludes direct reliance on the theoretical properties of the exact solution to, we can inherit some of them in the form of explicit certificates for the approximate control policy and safety value function, obtained through recently developed post-hoc safety verification methods such as offline statistical calibration through conformal prediction and runtime verification using imagined gameplay rollouts with faster-than-real-time, black-box simulators.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

We empirically validate the proposed robust $\mathcal{Q}$-CBF framework on a disturbed inverted pendulum and a simulated 36-dimensional quadruped with black-box dynamics. On the pendulum, the learned robust $\mathcal{Q}$-CBF nearly recovers the maximal robust safe set. On the quadruped, it reliably enforces safety under adversarial uncertainty realizations while preserving forward locomotion.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-A Disturbed Inverted Pendulum", "weight": 1.0} -->

We consider the disturbed inverted pendulum benchmark of Alan et al.. Let $\theta \in {\lbrack{- \pi},\pi\rbrack}$ denote the angle from the upright equilibrium and let $\omega = \overset{˙}{\theta}$ denote angular velocity. The dynamics are given by

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Disturbed Inverted Pendulum", "weight": 1.0} -->

where $u \in {\lbrack{- 20},20\rbrack}$ and $F \in {\lbrack{- 2},2\rbrack}$. Unlike the original setup, we impose the control bound explicitly. Failure occurs when ${|\theta|} > {\pi/3}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Disturbed Inverted Pendulum", "weight": 1.0} -->

Heuristic barrier candidate. Following Alan et al., we use ${{h_{heu}{(\theta,\omega)}} = {1 - {16\theta^{2}} - {8\theta\omega} - {4\omega^{2}}}}.$ Because the original setup does not impose the control bound, $h_{heu}$ is not valid under our setting and is included only as a heuristic baseline.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-A Disturbed Inverted Pendulum", "weight": 1.0} -->

Analytically designed CBF. We also include a robust CBF that is valid in the sense of Definition 1. ‣ II-B Robust Continuous-Time Control Barrier Function ‣ II Preliminaries and Related Work ‣ Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning"), derived using the nominal evading maneuver ${u^{\star}{(\omega)}}:={- {20{{sgn}{(\omega)}}}}$: ${{h_{ana}{(\theta,\omega)}} = {{\cos\theta} - \frac{1}{2} - {\frac{\sqrt{3}}{2{({19 - {10\sqrt{3}}})}}\omega^{2}}}}.$

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-A Disturbed Inverted Pendulum", "weight": 1.0} -->

Maximal robust safe set. We solve the Isaacs equation on a grid using OptimizedDP.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-B Quadrupedal Locomotion", "weight": 1.0} -->

To validate that robust $\mathcal{Q}$-CBF can reliably enforce safety on a high-dimensional black-box system under adversarial uncertainty realizations, we consider a high-fidelity simulation of a quadrupedal locomotion task with the 36-dimensional Unitree Go2 robot in MuJoCo. We treat the simulator as a black-box transition mechanism taking as inputs a 12-D control input, given by the joint-position-increment vector $u = {\lbrack{\delta\theta_{J}^{1}},\ldots,{\delta\theta_{J}^{12}}\rbrack}^{\top} \in {\lbrack{- 0.5},0.5\rbrack}^{12}$, and a bounded disturbance input consisting of an external force of magnitude at most $50N$, whose application point on the torso and direction may be chosen arbitrarily. Failure is declared whenever any monitored torso-corner ground clearance falls below $0.10m$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-B Quadrupedal Locomotion", "weight": 1.0} -->

To compare task performance with LRSF, we first train a best-effort fallback policy together with its best-response disturbance through adversarial RL. The resulting best-effort fallback policy is used for the LRSF baseline. For the neural $\mathcal{Q}$-CBF, we further train the best-response disturbance policy following subsection IV-A. All methods are evaluated under this same disturbance policy that was trained adversarially against a spectrum of control policies.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-B Quadrupedal Locomotion", "weight": 1.0} -->

Fig. LABEL:fig:go2_exp_result compares the unfiltered task policy, LRSF, and neural $\mathcal{Q}$-CBF. The task policy is a pure-pursuit controller that drives the robot from the starting point (purple star) toward the right of the map. Under adversarial disturbance, the unfiltered task policy records only a 16% safe rate. LRSF's loss in robustness due to neural approximation error is amplified by the last-minute intervention, yielding a low safe rate of 38%. Moreover, LRSF produces abrupt chattering behaviors due to frequent switches between the task and fallback policies, a widely reported phenomenon, preventing the robot from making meaningful forward progress. By contrast, the neural $\mathcal{Q}$-CBF preserves stable forward locomotion while successfully enforcing safety across all 50 randomized trials.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-B Quadrupedal Locomotion", "weight": 1.0} -->

The histogram of per-step task input deviation ${\|{u^{\text{task}} - u^{\text{CBF}}}\|}^{2}$ is concentrated at substantially smaller values for neural $\mathcal{Q}$-CBF than for LRSF, suggesting that the neural $\mathcal{Q}$-CBF better preserves task performance by enforcing smaller modifications to the task input than the baseline LRSF.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced a new robust CBF framework for general nonlinear systems with bounded uncertainty. We showed that the safety value function characterized by the dynamic programming Isaacs equation is a valid robust DCBF protecting the *maximal robust safe set*. Incorporating insights from RL, we lifted this value function into state--control--disturbance space to derive a novel robust $\mathcal{Q}$-CBF constraint for runtime safety filtering. Coupled with reachability-based adversarial RL, the framework enables robust $\mathcal{Q}$-CBF synthesis and deployment *requiring only black-box access* to a transition mechanism, without closed-form dynamics, control-affine assumptions, or known uncertainty structure. We validated the framework on a disturbed inverted pendulum and a simulated 36-D quadruped. Our results provide a practical recipe for scalable synthesis and deployment of certifiable robust CBF safety filters on high-dimensional nonlinear systems, using neural approximators that can be further strengthened through post-hoc verification.
