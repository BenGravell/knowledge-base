<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory

Topics include Motion planning, Output feedback, Learned perception, Contraction theory, Safety guarantees, RGB-D perception.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Integrates learned perception error bounds, contraction-based tracking, and sampling-based planning to provide safety and reachability guarantees from high-dimensional observations. The paper is a useful template for treating perception uncertainty as part of the motion-planning certificate rather than as a separate preprocessing concern.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a motion planning algorithm for a class of uncertain control-affine nonlinear systems which guarantees runtime safety and goal reachability when using high-dimensional sensor measurements (e.g., RGB-D images) and a learned perception module in the feedback control loop. First, given a dataset of states and observations, we train a perception system that seeks to invert a subset of the state from an observation, and estimate an upper bound on the perception error which is valid with high probability in a trusted domain near the data. Next, we use contraction theory to design a stabilizing state feedback controller and a convergent dynamic state observer which uses the learned perception system to update its state estimate. We derive a bound on the trajectory tracking error when this controller is subjected to errors in the dynamics and incorrect state estimates. Finally, we integrate this bound into a sampling-based motion planner, guiding it to return trajectories that can be safely tracked at runtime using sensor data.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate our approach in simulation on a 4D car, a 6D planar quadrotor, and a 17D manipulation task with RGB(-D) sensor measurements, demonstrating that our method safely and reliably steers the system to the goal, while baselines that fail to consider the trusted domain or state estimation errors can be unsafe.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safely and reliably deploying an autonomous robot requires a systematic analysis of the uncertainties that it may face across its perception, planning, and feedback control modules. State-of-the-art methods largely analyze each module separately; e.g., by first certifying perception, finding a safe plan under a nominal dynamics model, and then using a stable tracking controller. However, this ignores how the errors in each module can propagate. Inaccuracies in the dynamics and perception can destabilize the downstream feedback controller and lead to failure, revealing a need to unify perception, planning, and control to guarantee safety for the end-to-end autonomy pipeline.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this gap, we consider one such unified approach: the Output Feedback Motion Planning problem (OFMP), which jointly plans nominal trajectories and designs feedback controllers which safely stabilize the system to some goal when using imperfect state information (i.e., output feedback). A concrete way to solve the OFMP is to bound the set of states that the system may reach while tracking a plan using output feedback, that is, a closed-loop output feedback trajectory tracking tube, and ensure it is collision-free.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The tracking tubes should be efficiently computable for arbitrary trajectories so that they can be used in the planning loop to restrict the set of states that can be safely visited. However, solving this reachability problem is computationally demanding.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Processing rich sensor data (e.g., images, depth maps, etc.) at runtime is often done via deep learning-based perception modules, which are powerful but error-prone. Bounding this error and bounding its effect on trajectory tracking error is difficult.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the first challenge, we use contraction theory, which is of specific interest for the OFMP as it enables the 1) design of stabilizing feedback controllers and convergent state estimators and 2) fast computation of tracking/estimation tubes, given a bound on the disturbances that the controller and observer are subjected to. Estimating this bound is central to our solution of the second challenge, where we use data to 1) estimate a bound on the error of a learned perception module which is valid with high probability and 2) bound the level to which incorrect state estimates can destabilize the controller. Combining these solutions provides accurate tubes that can be used in planning. In summary, we develop a contraction-based output feedback motion planning algorithm for control-affine systems stabilized from image observations, which retains guarantees on safety and goal reachability.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A learning-based framework for integrating high-dimensional observations into contraction-based control and estimation that can generalize across environments

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A trajectory tracking error bound for contraction-based feedback controllers in output feedback, subjected to a disturbance that accurately reflects the perception error

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A sampling-based planner which solves the OFMP, returning plans that can be safely tracked and that reliably reach the goal at runtime using image observations

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Validation in simulation on a 4D nonholonomic car, a 6D planar quadrotor, and a 17D manipulation task, guaranteeing safety whereas baseline approaches fail

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem statement", "weight": 1.0} -->

At runtime, we do not observe $x{(t)}$; we are only given observations $y{(t)}$ generated by (1b), and must track $x^{\ast}$ using a (dynamic) output feedback controller that we must also design. We assume $f$, $B$, $B_{w}$, and $B_{y}$ are known; $h$ is unknown; $w_{x}$, $w_{y}$ are not measurable but ${\overline{w}}_{x}$ and ${\overline{w}}_{y}$ are known.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem statement", "weight": 1.0} -->

If $n_{r} \leq n_{x}$ of the states can be inferred directly from $y$, we denote these indices as the reduced observation $y_{r} = {C_{r}x} \in {\mathbb{R}}^{n_{r}}$, where $C_{r} \in {\{ 0,1\}}^{n_{r} \times n_{x}}$ is a boolean matrix that selects the observable dimensions of $x$. We assume that we are given $C_{r}$. Let $x{(t)}$ be the executed trajectory of (1a), and let $\hat{x}{(t)}$ be the trajectory of the state estimate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem statement", "weight": 1.0} -->

We are given upper bounds ${\overline{d}}_{c}{}$, ${\overline{d}}_{e}{}$on the Riemannian distance between the true and estimated initial state $d_{e}{({x{}},{\hat{x}{}})}$ and between the true/planned initial state $d_{c}{({x^{\ast}{}},{x{}})}$; $d_{e}{( \cdot, \cdot )}$ and $d_{e}{( \cdot, \cdot )}$ are defined with respect to (w.r.t.) metrics $M_{c}$ and $M_{e}$, defined in Sec. 3.2 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory").

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem statement", "weight": 1.0} -->

To help solve the OFMP, we are given two datasets. The first is $\mathcal{S} = {\{{h{(x_{i},\theta_{i})}},x_{i},\theta_{i}\}}_{i = 1}^{N_{\text{data}}}$, a dataset of noiseless (cf. Sec. 6 for discussion on how to relax this assumption) observation-state-parameter triplets, where $x_{i} \in D_{p} \subseteq \mathcal{X}$, $\theta_{i} \in D_{\theta} \subseteq \Theta$ are collected by any means (sampling, demonstrations, etc.). We assume $D_{p}$ and $D_{\theta}$ (the domains where $\mathcal{S}$ is drawn from) are known, though this can be relaxed by estimating these sets as.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Ultimately, $D_{x}$ is a set where a stabilizing controller (in $D_{c}$) and state estimator (in $D_{e}$) exist, and where the perception is valid (in $D_{r}$).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Control/observer contraction metrics (CCMs/OCMs)", "weight": 1.0} -->

As our approach builds on contraction theory, we provide an overview here. Control contraction theory studies incremental stabilizability by measuring the distances between trajectories w.r.t. a Riemannian metric $M_{c}:{\mathcal{X}\rightarrow{\mathbb{S}}_{n_{x}}^{> 0}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Control/observer contraction metrics (CCMs/OCMs)", "weight": 1.0} -->

By setting $q = \hat{x}$, we recover the estimator dynamics (3 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")); if we set $q = x$, we recover $\overset{˙}{x} = {{f{(x)}} + {Bu{(\hat{x},x^{\ast},u^{\ast})}}}$. We can then analyze the convergence of $\hat{x}$ to $x$ via (5 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")), and shows that if (4 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")) holds, then $\hat{x}{(t)}$ contracts at some rate $\gamma \in {(0,\lambda_{e}\rbrack}$ towards $x{(t)}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Control/observer contraction metrics (CCMs/OCMs)", "weight": 1.0} -->

If $M_{e}{(x)}$ and $C{(x)}$ are constant, one can show that this holds for $\gamma = \lambda_{e}$. In particular, ${\|{{x{(t)}} - {\hat{x}{(t)}}}\|} \leq {\alpha_{e}{\|{{x{}} - {\hat{x}{}}}\|}e^{- {\lambda_{e}t}}}$ for $\alpha_{e} > 0$, and $\hat{x}{(t)}$ remains in a tube around $x{(t)}$ if (3 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")) is perturbed. For polynomial systems of moderate dimension ($n_{x} \lesssim 12$) with polynomial observation maps, CCMs and OCMs can be found via convex Sum of Squares (SoS) programs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Control/observer contraction metrics (CCMs/OCMs)", "weight": 1.0} -->

CCMs/OCMs can also be found for high-dimensional non-polynomial systems via learning-based methods (e.g., ).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

We describe our solution to the OFMP (cf. Fig. 2). Using dataset $\mathcal{S}$, we first train a perception system that returns a reduced-order observation that simplifies the search for the contraction metrics (Sec. 4.1). Second, we bound the error of the learned perception module, and propagate this perception error bound through the system to derive bounds on the tracking and estimation error when using a CCM-/OCM-based controller/estimator (Sec. 4.2). Third, we obtain a CCM and OCM which optimizes this bound via SoS programming (Sec. 4.3). Finally, we use these bounds to constrain a planner to return trajectories that enable safe runtime tracking and robust goal reachability from observations (Sec. 4.4). For space, all proofs for the theoretical results are in App. 0.C.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

Let us reconsider the observer (3 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")), which updates its estimate directly using $y - {h{(\hat{x},\theta)}}$ in the rich observation space.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

To implement (3 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")), one can use $\mathcal{S}$ to train a deep approximation of $h$, denoted $\hat{h}$, design an OCM satisfying (4 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")) for ${C{(\hat{x})}} = \frac{\partial{\hat{h}{(\hat{x},\theta)}}}{\partial x}$, and plug $\hat{h}$ and the OCM into (3 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

This naïve solution is flawed: 1) as $n_{y}$ is large, learning an accurate $\hat{h}$ can be difficult; 2) the $C{(\hat{x})}$ in (4 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")) becomes the Jacobian of a (non-polynomial) deep network, complicating OCM synthesis by precluding the use of SoS programming.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

We can take a more structured approach if we know which states can be directly inferred from $y$; this is reasonable if the states have semantic meaning (e.g., poses, velocities). Recall $C_{r}$ (Sec. 3.1) defines this reduced observation as $y_{r} = {C_{r}x} \in {\mathbb{R}}^{n_{r}}$. We can then learn an approximate inverse ${{\hat{h}}^{- 1}{(y,\theta)}}:{{{\mathbb{R}}^{n_{y}} \times {\mathbb{R}}^{n_{p}}}\rightarrow{\mathbb{R}}^{n_{r}}}$ which maps a $y$ and $\theta$ to the reduced observation. Note that if each unique $y$ corresponds to a unique $y_{r}$, this inverse is well-defined and does not require the full state to be invertible from a single $y$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

Concretely, consider a car with position, orientation, and velocity states $\lbrack p_{x},p_{y},\phi,v\rbrack$ and RGB-D data from an onboard camera (Fig. 1.A) driving in several obstacle fields. In this case, $y_{r} = {\lbrack p_{x},p_{y},\phi\rbrack}^{\top}$ and $\theta$ could be the obstacle locations. We model ${\hat{h}}^{- 1}$ as a neural network and train it via the mean squared error between ${\hat{h}}^{- 1}{(y_{i},\theta_{i})}$ and $C_{r}x_{i}$ for all $i \in {1,\ldots,N_{\text{data}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

(4 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")) is SoS-representable, despite ${\hat{h}}^{- 1}$ being non-polynomial. Compared to the nominal reduced observer, the true observer we use,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning a perception module for contraction-based estimation", "weight": 1.0} -->

experiences disturbance from model error $B_{w}w_{x}$, sensor noise $B_{y}w_{y}$, and learning error $\|{{{\hat{h}}^{- 1}{({h{(x,\theta)}},\theta)}} - {C_{r}x}}\|$. Quantifying these errors for our vision-based observer is one of our core contributions and is key in deriving tracking bounds useful for planning.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bounding tracking error and state estimation error for planning", "weight": 1.0} -->

To begin, assume we have a CCM $M_{c}$ and an OCM $M_{e}$ that are valid in $D_{c} \subseteq \mathcal{X}$ and $D_{e} \subseteq \mathcal{X}$ and which contract at rate $\lambda_{c}$ and $\lambda_{e}$, respectively. We discuss CCM/OCM synthesis in Sec. 4.3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Bounding tracking error and state estimation error for planning", "weight": 1.0} -->

We will use and to obtain upper bounds on the tracking/estimation Riemannian distances, denoted as ${\overline{d}}_{c}{(t)}$ and ${\overline{d}}_{e}{(t)}$, respectively.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Bounding tracking error and state estimation error for planning", "weight": 1.0} -->

These tubes are crucial in informing where the planner can safely visit, since tracking any $\Omega_{c}$-buffered candidate trajectory within $D_{x}$ which remains in $\mathcal{X}_{\text{safe}}$ is guaranteed to remain safe. However, for these tubes to be usable in a planner, we need explicit bounds on the integral terms in and.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Bounding tracking error and state estimation error for planning", "weight": 1.0} -->

In this section, we first present the final derived bounds on the integrals (Lemmas 4.1). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") and 4.2). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")), describe the ideas behind the derivations, and postpone the full mathematical details to App. 0.B ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory").

<!-- chunk {"id": "body-0035", "role": "body", "section": "Bounding tracking error", "weight": 1.0} -->

We explain more details behind Lemma 4.1). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory"). As Lemma 4.1). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") relies on a bound for $w_{c}{(t)}$, we first break down the components that make up $w_{c}{(t)}$. Relative to the nominal closed-loop dynamics (7a), our true closed-loop system

<!-- chunk {"id": "body-0036", "role": "body", "section": "Bounding tracking error", "weight": 1.0} -->

See Rem. 1. ‣ 4.2.3 Integrating the differential inequalities: ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") for details on estimating $L_{\Deltak}$. In estimating $L_{\Deltak}$, we measure input distances w.r.t. $W_{e}$; this reduces conservativeness due to the form of our estimation error bound. Combining - yields Lemma 4.1). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory"); see App. 0.C for the detailed proof.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Bounding estimation error", "weight": 1.0} -->

Two errors drive $w_{e}{(t)}$: the perception error ${{\hat{h}}^{- 1}{({h{(x,\theta)}},\theta)}} - {C_{r}x}$, and the runtime observation noise $B_{y}w_{y}$. Combining with the dynamics error gives ${w_{q}{(t)}} \doteq {{B_{w}{(t)}w_{x}{(t)}} + {w_{e}{(t)}}}$. $B_{w}{(t)}w_{x}{(t)}$ can be bounded as in Lemma 4.1). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory"), but $w_{e}{(t)}$ is harder to bound.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Bounding estimation error", "weight": 1.0} -->

Here, $L_{{\hat{h}}^{- 1}}$ is the local Lipschitz constant of the learned inverse function in $y$, i.e.,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Bounding estimation error", "weight": 1.0} -->

Now, consider the second braced term. How can we bound the learned perception module error ${\epsilon{(x,\theta)}} \doteq {\|{{{\hat{h}}^{- 1}\left( {h{(x,\theta)}},\theta \right)} - {C_{r}x}}\|}$ over $D_{r} \times D_{\theta}$? We describe three options (Fig. 4) at a high level, highlight their strengths/drawbacks, and provide the details in App. 0.B ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory"). The first bound, denoted ${\overline{\epsilon}}_{1}$, is a constant bound on $\epsilon{(x,\theta)}$ globally over $D_{r} \times D_{\theta}$ (Fig. 4.A). This works well if the error is consistent, but is loose if there are any error spikes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Bounding estimation error", "weight": 1.0} -->

The second bound (Fig. 4.B), denoted ${\overline{\epsilon}}_{2}{(x^{\ast},\theta)}$, bounds the error only in the tube $\Omega_{c}$ around a nominal $x^{\ast}$, using the Lipschitz constant of $\epsilon{(x,\theta)}$ (denoted $L_{p}$). Due to its locality, ${\overline{\epsilon}}_{2}{(x^{\ast},\theta)}$ can be tighter than ${\overline{\epsilon}}_{1}$; however, it scales linearly with the size of $\Omega_{c}$, even if $\epsilon{(x,\theta)}$ remains constant.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Bounding estimation error", "weight": 1.0} -->

The third bound, ${\overline{\epsilon}}_{3}{(x^{\ast},\theta)}$ (Fig. 4.C), also bounds the error in the tube but avoids the linear scaling by taking the worst training error in $\Omega_{c}$ and buffering it with a constant value, which depends on $L_{p}$ and the dataset dispersion $\mathcal{R}$. Each of these bounds ${\overline{\epsilon}}_{\{ 1,2,3\}}$ on $\epsilon{(x,\theta)}$ can be plugged into Lemma 4.2). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") to upper bound $\epsilon{(x,\theta)}$; see App. 0.B ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") for details.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Integrating the differential inequalities", "weight": 1.0} -->

Now that we can bound the RHSs of the differential inequalities and via Lemmas 4.1). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") and 4.2). ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory"), we show how these bounds on ${\overset{˙}{d}}_{c}$ and ${\overset{˙}{d}}_{e}$ bound the values of $d_{c}$ and $d_{e}$, thereby providing the desired tubes. By grouping terms in -, we have the following affine vector-valued differential inequality,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 1 (Estimating constants from data)", "weight": 1.0} -->

The derived bounds depend on several constants that are unknown a priori, such as $L_{\Deltak}$ and $L_{{\hat{h}}^{- 1}}$, and if ${\overline{\epsilon}}_{1}$, ${\overline{\epsilon}}_{2}$, or ${\overline{\epsilon}}_{3}$ is being used, ${\overline{\epsilon}}_{1}$, $L_{p}$, and $\{ L_{p},\mathcal{R}\}$ also need to be estimated, respectively. As overapproximating each constant also yields valid (and looser) bounds, we use the i.i.d. validation set $\mathcal{V}$ to overestimate each constant via a sampling-based approach based on extreme value theory. This returns a value which overestimates the true constant with a user-desired probability $\delta$, where $\delta$ holds in the limit of infinite samples. See for details.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimizing CCMs and OCMs for output feedback", "weight": 1.0} -->

We briefly discuss how we obtain the CCM/OCM that define the controller/observer; for space, we detail our method in App. 0.D. We write two SoS programs to independently synthesize the CCM/OCM, which are approximately optimized to minimize their tube sizes. We search over polynomial CCMs and constant OCMs. For polynomial dual CCMs $W_{c}{(x)}$, we also find a constant metric ${\overline{W}}_{c} \succeq {W_{c}{(x)}}$, for all $x$, in order to simplify constraint checking in Sec. 4.4. For linear systems, these SoS programs simplify to a standard semidefinite program (SDP), which scale to higher-dimensional systems.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Solving the OFMP", "weight": 1.0} -->

Given the CCM, OCM, and the ability to compute tracking tubes, we can now solve the OFMP. Our solution builds upon a kinodynamic RRT \[, though we note that the tubes derived in Sec. 4.2 are planner-agnostic. We grow a search tree $\mathcal{T}$ by integrating sampled controls held for sampled dwell-times until $\mathcal{G}$ is reached. To ensure we stay in $\mathcal{X}_{\text{safe}}$ at runtime, we impose extra constraints on each candidate transition, which are informed by the tubes; this translates to a restriction on where $\mathcal{T}$ can grow (cf. Fig. 5).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Solving the OFMP", "weight": 1.0} -->

To remain collision-free at runtime, we must add extra constraints on $\mathcal{T}$ to ensure the tubes are valid, as discussed in Sec. 4.2. We describe these constraints now, and prove they are sufficient in Thm. 4.2. ‣ 4.4 Solving the OFMP ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory"). At a high level, the estimated constants, CCM, and OCM must be valid for any $x$ and $\hat{x}$ that can be reached at runtime. Thus, in line 8, we ensure $d_{c}{(t)}$ and $d_{e}{(t)}$ remain less than $\overline{c}$ and $\overline{e}$ for all time, so that $L_{\Deltak}$ is valid.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Solving the OFMP", "weight": 1.0} -->

In line 9, we ensure that ${\Omega_{c}{(t)}} \subseteq {D_{c} \cap D_{r}}$, i.e., the system remains where the controller can contract $x$ towards $x^{\ast}$, and ${\overline{\epsilon}}_{i}$ is valid. In line 10, we ensure $\hat{x}$ remains in $D_{e} \cap D_{c}$; this ensures that contracts towards the true state $x$ via (2 ‣ 3 Preliminaries and Problem Statement ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")), and that a feasible feedback control exists; ensuring this at planning time (when we only know $x^{\ast}{(t)}$) requires a Minkowski sum of $\Omega_{c}$ and $\Omega_{e} \ominus {\{{x{(t)}}\}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Solving the OFMP", "weight": 1.0} -->

Constraint-satisfying candidate extensions are added to $\mathcal{T}$ (line 11); else, they are rejected (line 12). This continues until the goal is reached (line 13). We visualize our planner (Fig. 5), Contraction-based Output feedback RRT (CORRT), detailed in Alg. 1. Finally, Thm. 4.2. ‣ 4.4 Solving the OFMP ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory") shows our method ensures safety and goal reachability if all estimated constants are valid; as our estimates are probabilistically-valid, the overall guarantees are probabilistic (cf. Rem. 2. ‣ Appendix 0.C

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate CORRT on a 4D car with RGB-D observations, a 6D quadrotor with RGB observations, and a 14D acceleration-controlled 7DOF arm with RGB observations. All observations are rendered in PyBullet. We compare with three baselines; two are shared across experiments, so we overview them here. To show the need to plan where the CCM/OCM are valid and the error bounds are accurate, Baseline 1 (B1) plans using the tracking tubes from (20. ‣ 4.2.3 Integrating the differential inequalities: ‣ 4.2 Bounding tracking error and state estimation error for planning ‣ 4 Method ‣ Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory")) inside Alg. 1 but is not constrained to stay within $D$, i.e., the checks in line 8-10 of Alg. 1 are relaxed. To show the need to consider estimation error in planning, Baseline 2 (B2) assumes perfect state knowledge in computing its tubes, i.e., ${d_{e}{(t)}} \equiv 0$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

All baselines execute with the same CCM/OCM as our method. See Table 1 for error statistics and the video for visualizations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "4D nonholonomic car", "weight": 1.0} -->

We plan for 150 start/goals in $D$; our unoptimized implementation takes 2.5 minutes on average. This is done offline; the tracking controller is computed at real-time rates following Sec. 4.2.1 and. For each trial, the obstacle map $\theta$ is selected uniformly within $D_{\theta}$. See Table 1 for error statistics. Over all trials, our method ensures $x{(t)}$ and $x^{\ast}{(t)}$ always remain within the CORRT-computed $\Omega_{c}{(t)}$ and $\Omega_{e}{(t)}$, respectively, and reduces the initial tracking/estimation error by a factor of $> 5$ and $30$, respectively. In contrast, B1 violates its $\Omega_{c}{(t)}$ and $\Omega_{e}{(t)}$ in 90/150 and 101/150 trials, respectively, fails to reduce tracking/estimation error, and can crash.

<!-- chunk {"id": "body-0052", "role": "body", "section": "4D nonholonomic car", "weight": 1.0} -->

For instance, in Fig. 6.C, the plan leaves $D_{r}$, causing observation error to increase (here, $\hat{h}$ is inaccurate, since it is not trained outside of $D_{r}$), destabilizing $\hat{x}$ (Fig. 6.C, right), in turn destabilizing $x$, leading to the crash. Similarly, B2 violates its computed $\Omega_{c}$ in 60/150 trials (no $\Omega_{e}{(t)}$ is computed for B2, as it assumes perfect state information), fails to shrink tracking/estimation errors, leading to crashes (see Fig. 6). As in B1, this crash also arises from observation error. Overall, this experiment suggests that CORRT ensures safe goal-reaching for nonholonomic systems using RGB-D data, and that it generalizes to different environments (i.e., obstacle layouts), while baselines are unsafe.

<!-- chunk {"id": "body-0053", "role": "body", "section": "6D quadrotor", "weight": 1.0} -->

We plan for 150 start/goals in $D$, taking 6 minutes on average (see Table 1 for statistics). Across all trials, CORRT ensures $x{(t)}$ and $\hat{x}{(t)}$ stay inside the CORRT-computed tubes $\Omega_{c}{(t)}$ and $\Omega_{e}{(t)}$, respectively, and reduces the initial tracking/estimation error by a factor of $> 6$ and $34$. In contrast, B1 violates its computed $\Omega_{c}{(t)}$ and $\Omega_{e}{(t)}$ in 61/150 and 76/150 trials, respectively, fails to reduce error, and can be unsafe (see Fig. 7). Similarly, B2 violates its $\Omega_{c}$ in 142/150 trials.

<!-- chunk {"id": "body-0054", "role": "body", "section": "6D quadrotor", "weight": 1.0} -->

We show concrete examples of this in Fig. 7.C-.D; the plans in both cases exit $D_{r}$, moving to $p_{x}$ and $p_{z}$ values outside of the ${\lbrack{- 4.5},4.5\rbrack} \times {\lbrack 0.5,4.5\rbrack}$ training range, leading to high ${\hat{h}}^{- 1}$ error. The plans also take overly-aggressive turns that bring the velocities outside of $D_{e}$ and $D_{c}$; this further destabilizes the system, causing crashes in both cases. Overall, this experiment suggests the need to ensure that ${\hat{h}}^{- 1}$, the CCM, and the OCM are correct, and that CORRT ensures this to guarantee safety for underactuated systems via RGB observations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "17D manipulation task", "weight": 1.0} -->

We consider an acceleration-controlled 7DOF Kuka arm, where each joint follows double integrator dynamics (0.E.18), which is grasping an object (a rubber duck) with an unknown orientation relative to the end effector. We assume slight noise in the dynamics (0.E.18), ${\overline{w}}_{x} = 0.0125$, due to the weight of the object. Our goal is to estimate the unknown orientation, represented as three Euler angles ${\{\phi_{i}\}}_{i = 1}^{3}$, using our observer, given 80x80 RGB images (Fig. 1.C) of the arm and grasped object (see Fig. 1.C, inset); this makes $y \in {\mathbb{R}}^{19200}$. We may also plan motions for the arm to improve the quality of the observations/state estimates, though in doing so, we also need to counteract the dynamics error.

<!-- chunk {"id": "body-0056", "role": "body", "section": "17D manipulation task", "weight": 1.0} -->

We assume that the joint angles and velocities can be perfectly estimated (i.e., directly measured), given the accuracy of the Kuka joint encoders, focusing instead on estimating the unknown ${\{\phi_{i}\}}_{i = 1}^{3}$ and controlling $j$ and $\overset{˙}{j}$ (the joint angles and velocities) using our method. We assume the object is rigidly attached to the gripper, such that its relative orientation is constant over time.

<!-- chunk {"id": "body-0057", "role": "body", "section": "17D manipulation task", "weight": 1.0} -->

We model ${\hat{h}}^{- 1}$ as a fully-connected neural network, with five hidden layers of width 1024 and softplus activations. We compute a constant CCM for the 14D subsystem: CCM synthesis for the full 17D system fails, as the ${\{\phi_{i}\}}_{i = 1}^{3}$ are not controllable due to the rigid attachment. Since the arm dynamics are linear, the CCM optimization simplifies to a standard semidefinite program that can be quickly solved. We compute a constant OCM for the full 17D system, to enable estimation of ${\{\phi_{i}\}}_{i = 1}^{3}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "17D manipulation task", "weight": 1.0} -->

We plan 100 trajectories in $D$ from various initial $j$, $\overset{˙}{j}$, and orientation estimates, taking 45 seconds on average. We summarize the error statistics in Table 1. Across all trials, when planning with CORRT, $x$ and $\hat{x}$ always remain within the computed tubes $\Omega_{c}{(t)}$ and $\Omega_{e}{(t)}$; the CCM keeps the tracking error very small, and the OCM shrinks the error by a factor of $> 18$. Crucially, if a plan is found where $\Omega_{e}{(T)}$ satisfies the estimation accuracy threshold, we can ensure our true state estimate satisfies ${|{{\phi_{i}{(T)}} - {{\hat{\phi}}_{i}{(T)}}}|} \leq 0.1$, $i = {1,2,3}$. We are able to find plans that achieve this threshold for 100/100 trials.

<!-- chunk {"id": "body-0059", "role": "body", "section": "17D manipulation task", "weight": 1.0} -->

We compare with two baselines in this example: B1 (as described before), and B3, which keeps the arm stationary and runs for the same duration as the plan computed using CORRT. The purpose of B3 is to show that the actions taken by the CORRT plan help to reduce estimation error. In contrast to CORRT, B1 violates its computed $\Omega_{e}{(t)}$ in 44/100 trials and can fail to achieve the required estimation accuracy, only satisfying the 0.1 threshold in 79/100 trials (see Fig. 8). One failure example is shown in Fig. 8.B: the arm moves too close to the camera (outside of $D_{r}$), causing the duck to fall out of frame. This causes a sharp increase in ${\hat{h}}^{- 1}$ error, since $\phi_{i}$ cannot be observed; this destabilizes, leading to a failure to satisfy the 0.1 threshold.

<!-- chunk {"id": "body-0060", "role": "body", "section": "17D manipulation task", "weight": 1.0} -->

Note that B1 does not violate $\Omega_{c}$; this is because the controller is not a function of the incorrect $\phi_{i}$ estimates. Similarly, B3 often fails to satisfy the 0.1-estimation accuracy threshold, only satisfying it in 7/100 trials (see Fig. 8.A for a failure example). This shows that passively estimating $\phi_{i}$ without moving the arm cannot achieve the needed estimation accuracy; instead, the arm must be moved towards regions with smaller perception error. Overall, this experiment suggests the applicability of our approach on high-dimensional systems, that it can design actions that improve state estimates, and that our approach can plan paths that guarantee a desired level of state estimation accuracy.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We present a motion planning algorithm for control-affine systems that enables safe tracking at runtime using an output feedback controller with image observations as input. To achieve this, we learn a perception system and use it in an OCM and CCM-based output feedback control loop. We derive tracking tubes for the closed-loop system and use them within an RRT-based planner to compute plans that theoretically guarantee safe goal-reaching at runtime. Our results empirically validate this safety guarantee, and show that ignoring the effects of state estimation error and the local validity of the perception system/estimator/controller can lead to unsafe behavior.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Our method has some weaknesses which reveal directions for future work. While the large dataset $\mathcal{S}$ used to train ${\hat{h}}^{- 1}$ is easy to gather in simulation, sim-to-real is then needed for ${\hat{h}}^{- 1}$ to transfer to the real world. Thus, in future work, we will combine synthetic, domain-randomized perception data with a small real-world labeled dataset to train generalizable perception modules that have calibrated estimates of the sim-to-real error. Our method also assumes noiseless training data, to ensure $L_{p}$ is finite; in the future, we wish to relax this by investigating Lipschitz constant estimation methods robust to input noise. Another drawback is the conservativeness of using worst-case disturbances; to mitigate this, we will integrate stochastic contraction into our method. Finally, we require $\theta$ to be known; in future work, we will aim to jointly estimate $\theta$ and $x$ with similar convergence guarantees.
