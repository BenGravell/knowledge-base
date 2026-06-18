<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach

Topics include Convex optimization, Motion planning, Lyapunov methods, Stability analysis, Robustness, Neural networks, Online algorithms, Optimization, Planning, Control, Learning, Stability, LAG-ROS, Lyapunov functions, Euclidean distance, Robust control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents Learning-based Autonomous Guidance with RObustness and Stability guarantees (LAG-ROS), which provides machine learning-based nonlinear motion planners with formal robustness and stability guarantees, by designing a differential Lyapunov function using contraction theory. LAG-ROS utilizes a neural network to model a robust tracking controller independently of a target trajectory, for which we show that the Euclidean distance between the target and controlled trajectories is exponentially bounded linearly in the learning error, even under the existence of bounded external disturbances. We also present a convex optimization approach that minimizes the steady-state bound of the tracking error to construct the robust control law for neural network training. In numerical simulations, it is demonstrated that the proposed method indeed possesses superior properties of robustness and nonlinear stability resulting from contraction theory, whilst retaining the computational efficiency of existing learning-based motion planners.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the near future of robotic exploration, teams of robots are expected to perform complex decision-making tasks autonomously in extreme environments, where their motions are typically governed by nonlinear dynamics with external disturbances. For such operations to be successful, they need to compute optimal motion plans online while robustly guaranteeing convergence to the target trajectory, both with their limited onboard computational resources. Thus, this work aims to propose a learning-based robust motion planning and control algorithm that meets these challenging requirements.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we present Learning-based Autonomous Guidance with RObustness and Stability guarantees (LAG-ROS) as a novel way to bridge the gap between the learning-based and robust tube-based motion planners. In particular, while LAG-ROS requires one neural network evaluation to get its control input as in the learning schemes, its contraction theory-based architecture still allows obtaining formal robustness and stability guarantees as. This framework depicted in Fig. 1 is summarized as follows.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

Motion planning scheme
State tracking error ∥x − xd∥

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

(a) Learning-based motion planner
Increases exponentially (Lemma 1)
One neural net evaluation

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

(b) Robust tube-based motion planner
Exponentially bounded (Theorem 2)
Computation required to get (xd,ud)

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

(c) Proposed method (LAG-ROS)
Exponentially bounded (Theorem 1)
One neural net evaluation

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-1 Robustness and Stability Guarantees", "weight": 1.0} -->

The theoretical foundation of LAG-ROS rests on contraction theory, which utilizes a contraction metric to characterize a necessary and sufficient condition of exponential incremental stability of nonlinear system trajectories. The central result of this paper is that, if there exists a control law which renders a nonlinear system contracting, or equivalently, the closed-loop system has a contraction metric, then LAG-ROS trained to model the controller ensures the Euclidean distance between the target and controlled trajectories to be bounded exponentially with time, linearly in the learning error and size of perturbation. This property helps quantify how small the learning error should be in practice, giving some guidance in choosing design parameters of neural net training. We further show that such a contracting control law and its corresponding contraction metric can be designed explicitly via convex optimization, using the method of CV-STEM to minimize a steady-state upper bound of the LAG-ROS tracking error.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-2 State Constraint Satisfaction", "weight": 1.0} -->

We further exploit the computed bound on the tracking error in generating expert demonstrations for training, so that the learned policy will not violate given state constraints even with the learning error and external disturbances. In this phase, LAG-ROS learns the contracting control law independently of a target trajectory, making it implementable without solving any motion planning problems online unlike. The performance of LAG-ROS is evaluated in cart-pole balancing and nonlinear motion planning of multiple robotic agents in a cluttered environment, demonstrating that LAG-ROS indeed satisfies the formal exponential bound as in with its computational load as low as that of existing learning-based motion planners. In particular, LAG-ROS requires less than $0.1$s for computation in all of these tasks and achieves higher control performances and task success rates (see Sec. V-A3), when compared with the existing motion planners in Table I which outlines the differences of these schemes from our proposed method.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Problem Formulation of LAG-ROS", "weight": 1.0} -->

We seek to find $u$ that is computable with one neural network evaluation and guarantees exponential boundedness of $\|{x - x_{d}}\|$ in (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), robustly against the learning error and external disturbances. The objective is thus not to develop new learning-based planners that compute $(x_{d},u_{d})$, but to augment them with formal robustness and stability guarantees.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Problem Formulation of LAG-ROS", "weight": 1.0} -->

Robust tube-based motion planner or:\
${(x,x_{d},u_{d},t)}\mapsto{u^{\ast}{(x,x_{d},u_{d},t)}}$, where $u^{\ast}$ is a contraction theory-based tracking controller, e.g., in Theorem 2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Problem Formulation of LAG-ROS", "weight": 1.0} -->

The robust tube-based motion planner (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") ensures that the perturbed trajectories $x$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) stay in an exponentially bounded error tube around the target trajectory $x_{d}$ of (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) (see Theorem 2). However, it requires the online computation of $(x_{d},u_{d})$ as an input to their control policy, which is not realistic for systems with limited computational resources.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Problem Formulation of LAG-ROS", "weight": 1.0} -->

The learning-based motion planner (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") circumvents this issue by modeling the target policy ${(x,o_{\ell},t)}\mapsto u_{d}$ by a neural network. In essence, our approach, to be proposed in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), is for providing (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") with the contraction theory-based stability guarantees (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Problem Formulation of LAG-ROS", "weight": 1.0} -->

We remark that (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") can only assure the tracking error $\|{x - x_{d}}\|$ to be bounded by a function which exponentially increases with time, as to be shown in Lemma 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") for comparison with LAG-ROS of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Stability Guarantees of LAG-ROS", "weight": 1.0} -->

The approach of LAG-ROS bridges the gap between (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") and (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") by ensuring that the distance between the target and controlled trajectories to be exponentially bounded.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Stability Guarantees of LAG-ROS", "weight": 1.0} -->

Proposed approach (LAG-ROS, see Fig. 1):\ ${(x,{o_{\ell}{(x,o_{g})}},t)}\mapsto{u^{\ast}{(x,{x_{d}{(o_{g},t)}},{u_{d}{({x_{d}{(o_{g},t)}},o_{g},t)}},t)}}$ with $o_{\ell}$ of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), modeled by a neural network $u_{L}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), where $u^{\ast}$ of (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Stability Guarantees of LAG-ROS", "weight": 1.0} -->

(LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") is viewed as a function of $(x,o_{\ell},t)$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

$\epsilon_{\ell}$ of (3 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) can only be found empirically in practice, and thus we propose one way to generate training data with (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and use the test error of $u_{L}$ as $\epsilon_{\ell}$ (see Sec. IV-B and Sec. V). Note that models $f{(x,t)}$ learned by system identification for a more accurate description of the nominal dynamics, e.g. is still utilizable in (4 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) as long as the learned system is contracting, and the modeling error is bounded. Other types of perturbations, such as stochastic or parametric uncertainty, could be handled using.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To appreciate the importance of the guarantees in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), let us additionally show that (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), which models ${(x,o_{\ell},t)}\mapsto u_{d}$, only leads to an exponentially diverging bound.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contraction Theory-based Robust and Optimal Tracking Control", "weight": 1.0} -->

Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") is subject to the assumption that we have a contraction theory-based robust tracking control law $u^{\ast}$, which satisfies (5 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and (6 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) for a given $(x_{d},u_{d})$. This section thus delineates one way to extend the method called ConVex Optimization-based Steady-state Tracking Error Minimization (CV-STEM) to find a contraction metric $M$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), which minimizes an upper bound of the steady-state error of (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) via convex optimization.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Contraction Theory-based Robust and Optimal Tracking Control", "weight": 1.0} -->

Minimizing the bound renders the tube-based planning of Theorem 3 to be given in Sec. IV for sampling training data less conservative, resulting in a better optimal solution for $(x_{d},u_{d})$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contraction Theory-based Robust and Optimal Tracking Control", "weight": 1.0} -->

In addition, we modify the CV-STEM in to derive a robust control input $u^{\ast}$ which also greedily minimizes the deviation of $u^{\ast}$ from the target $u_{d}$, using the computed contraction metric $M$ to construct a differential Lyapunov function $V = {\deltay^{\top}M\deltay}$. Note that $u^{\ast}$ is to be modeled by a neural network which maps $(x,o_{\ell},t)$ to $u^{\ast}$ implicitly accounting for $(x_{d},u_{d})$ as described in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), although $u^{\ast}$ takes $(x,x_{d},u_{d},t)$ as its inputs (see Sec. IV-B).

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Problem Formulation of CV-STEM Tracking Control", "weight": 1.0} -->

For given $(x_{d},u_{d})$, we assume that $u^{\ast}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") can be decomposed as ${u^{\ast}{(x,x_{d},u_{d},t)}} = {u_{d} + {K{(x,x_{d},u_{d},t)}{({x - x_{d}})}}}$, the generality of which is guaranteed by the following lemma.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B CV-STEM Contraction Metrics as Lyapunov Functions", "weight": 1.0} -->

The remaining task is to construct $M$ so that it satisfies (5 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and (6 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")). The CV-STEM approach suggests that we can find such $M$ via convex optimization to minimize an upper bound of (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) as $t\rightarrow\infty$ when $\alpha$ of (5 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) is fixed. Theorem 2 proposes using the metric $M$ designed by the CV-STEM for a Lyapunov function, thereby augmenting $u^{\ast}$ with additional optimality to greedily minimize ${\|{u^{\ast} - u_{d}}\|}^{2}$ for $u_{d}$ in (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

and are convex in terms of their respective decision variables and thus can be solved computationally efficiently \[34, pp. 561\]. For systems with a known Lyapunov function (e.g. Lagrangian systems \[35, pp. 392\]), we could simply use it to get robust tracking control $u^{\ast}$ in Theorem 2 without solving, although optimality may no longer be guaranteed in this case.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The contraction metric construction itself can be performed using a neural network, leading to an analogous incremental stability and robustness results to those of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0028", "role": "body", "section": "Generating Expert Demonstrations", "weight": 1.0} -->

This section presents how to sample training data, i.e., the target trajectory $(x_{d},u_{d})$ of (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and corresponding perturbed state and CV-STEM robust control $(x,u^{\ast})$, so that $x$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) controlled by the LAG-ROS control $u_{L}$ will stay in given admissible state space as long as we have ${\|{u_{L} - u^{\ast}}\|} \leq \epsilon_{\ell}$ as in (3 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0029", "role": "body", "section": "Generating Expert Demonstrations", "weight": 1.0} -->

To be specific, since $u^{\ast}$ of Theorem 2 solves to obtain an optimal error tube around $x_{d}$, i.e., (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), we exploit it in the tube-based motion planning for generating training data, which satisfies given state constraints even under the existence of the learning error $\epsilon_{\ell}$ and disturbance $d$ in (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and. Note that the learning error $\epsilon_{\ell}$ and disturbance upper bound $\overline{d}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") are assumed to be selected a priori.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Tube-based State Constraint Satisfaction in LAG-ROS", "weight": 1.0} -->

\{{\xi{(t)}} \middle| {{\|{{v{(t)}} - {\xi{(t)}}}\|} \leq {r_{\ell}{(t)}}}\} \right.},{{\xi{(t)}} \in {\mathcal{X}{(o_{g},t)}}}}\} \right.$, $\mathcal{X}{(o_{g},t)}$ is given admissible state space, $r_{\ell}{(t)}$ is the right-hand side of (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), and $\overline{u} \in {\overline{\mathcal{U}}{(o_{g},t)}}$ is an input constraint.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Tube-based State Constraint Satisfaction in LAG-ROS", "weight": 1.0} -->

The following theorem shows that the LAG-ROS control ensures the perturbed state $x$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) to satisfy state constraints $x \in \mathcal{X}$, due to the contracting property of $u^{\ast}$ in Theorem 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Theorem 3 implies that if $x_{d}$ is sampled, the perturbed trajectory (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) controlled by LAG-ROS $u_{L}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") will not violate the given state constraints as long as LAG-ROS $u_{L}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") satisfies (3 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")). This helps greatly reduce the need for safety control schemes such as.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Learning Contraction Theory-based Robust Control", "weight": 1.0} -->

To meet the learning error requirement (3 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) for the sake of robustness and state constraint satisfaction proposed in Theorems 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") and 3, we should also sample $x$ to get training data for the CV-STEM robust control inputs $u^{\ast}$ of Theorem 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The localization method in allows extracting $o_{\ell}$ of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") by $o_{g}$ of, to render LAG-ROS applicable to different environments in a distributed way (see Sec. V).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The pseudocode for the offline construction of the LAG-ROS control of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") is presented in Algorithm 1 (see Fig. 1 for its visual description). Once we get $u_{L}{(x,o_{\ell},t)}$ by Algorithm 1, $u = u_{L}$ in (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) can be easily computed by only evaluating the neural net $u_{L}$ for a given $(x,o_{\ell},t)$ observed at $(x,t)$, whilst ensuring robustness, stability, and state constraint satisfaction due to Theorems 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), 2, and 3.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Inputs: Random environment information {(og)i}i = 1N
Contraction metric M of Theorem 2
Learning error ϵℓ and disturbance bound $\overline{d}$
Outputs: LAG-ROS control uL of Theorem 1
Solve of Theorem 3 for (og)i using 𝒫 and obtain a target trajectory and environment observation history (xd,ud,og,oℓ,t)i
Sample D robust CV-STEM control {(x,u*)i j}j = 1D using Theorems 2 and 4 (see Fig. 2)
Model (x,oℓ,t)i j ↦ ui j* by a neural net to satisfy ∥uL − u*∥ ≤ ϵℓ as in of Theorem 1 (see Fig. 1)
Algorithm 1 LAG-ROS Algorithm

<!-- chunk {"id": "body-0037", "role": "body", "section": "Simulation", "weight": 1.0} -->

Our proposed LAG-ROS framework is demonstrated using multiple motion planning problems under external disturbances. CVXPY with the MOSEK solver is used to solve optimization problems in Theorems 2 and 3 for sampling training data.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Simulation Setup", "weight": 1.0} -->

The maximum admissible control time interval is selected to be ${\Deltat_{\max}} = 0.1$(s). The computational time of each framework is measured for the Macbook Pro laptop (2.2 GHz Intel Core i7, 16 GB 1600 MHz DDR3 RAM), and each simulation result is the average of $50$ simulations for each random environment and disturbance realization.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A1 Neural Network Training", "weight": 1.0} -->

We use a neural network $u_{L}$ with $3$ layers and $100$ neurons. The network is trained using stochastic gradient descent with training data sampled by Theorems 2--4, and the loss function is defined as $\|{u_{L} - u^{\ast}}\|$ to satisfy the learning error bound $\epsilon_{\ell}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"). We use $50000$ training samples and select $\epsilon_{\ell} = 0.01$ for all the tasks, but these numbers can be modified accordingly depending on situations, considering the required performance for the error bound (3 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"). Note that we can guarantee (3 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) only empirically, using the test error computed with a given test set as in standard neural network training.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A2 Environment Information", "weight": 1.0} -->

$o_{g}$ of (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) is selected as initial states, target terminal states, and states of obstacles and other agents, if any. In Sec. V-C, the deep set framework is used to extract local information $o_{\ell}$ of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") from $o_{g}$ as.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A3 Performance Measure", "weight": 1.0} -->

The objective function of Theorem 3 for sampling $(x_{d},u_{d})$ of (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) is selected as $\int_{0}^{T}{{\|\overline{u}\|}^{2}{dt}}$. Since LAG-ROS is not for proposing a new trajectory optimization solver but for augmenting it with the formal guarantees of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), one could use any other objective, e.g., information-based cost, as long as $(x_{d},u_{d})$ is obtainable.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A3 Performance Measure", "weight": 1.0} -->

We define success of each task as the situation where the agent reaches, avoiding collisions, if any, a given target terminal state $x_{f}$ within a given time horizon $\mathcal{T} \geq T$, i.e. ${\exists t^{\ast}} \in {\lbrack 0,\mathcal{T}\rbrack}$ s.t. ${\|{{x{(t^{\ast})}} - x_{f}}\|} \leq {r_{\ell}{(t^{\ast})}}$ for $r_{\ell}$ in (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), where the value for $r_{\ell}$ is to be defined in the subsequent sections. The success rate is computed as the percentage of successful trials in the total $50$ simulations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A3 Performance Measure", "weight": 1.0} -->

Also, we evaluate the performance of each planner, (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), and (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") in Sec. II ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), by the objective function $\int_{0}^{t^{\ast}}{{\| u\|}^{2}{dt}}$ if the task is successfully completed, and $\int_{0}^{T}{{\|

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A3 Performance Measure", "weight": 1.0} -->

u\|}^{2}{dt}}$ otherwise, where $T$ is the nominal time horizon.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A4 External Disturbances", "weight": 1.0} -->

As shown in Lemma 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") and Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), the tracking error bound of learning-based motion planners (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") increases exponentially with time, whilst it decreases exponentially for the proposed approach (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A4 External Disturbances", "weight": 1.0} -->

To make such a difference clear, we consider the situations where $d{(x,t)}$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) is non-negligible, and thus (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") tends to fail the task of Sec V-A3 due to Lemma 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A4 External Disturbances", "weight": 1.0} -->

This is not to argue that (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") should be replaced by (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), but to imply that they can be improved further to have the guarantees of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A5 Computational Complexity", "weight": 1.0} -->

Since (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") and LAG-ROS (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") are implementable with one neural net evaluation at each $t$, their performance is also compared with (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") which requires solving motion planning problems to get its control input. Its time horizon is selected to make the trajectory optimization solvable online considering the current computational power, for the sake of a fair comparison.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A5 Computational Complexity", "weight": 1.0} -->

We denote the computational time as $\Deltat$ in this section, and it should be less than the maximum control time interval $\Deltat_{\max}$, i.e., ${\Deltat} \leq {\Deltat_{\max}} = 0.1$(s).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Cart-Pole Balancing", "weight": 1.0} -->

We first consider the cart-pole balancing task in Fig. 3 to demonstrate the differences of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") -- (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") summarized in Table I. Its dynamics is given, and we use $g = 9.8$, $m_{c} = 1.0$, $m = 0.1$, $\mu_{c} = 0.5$, $\mu_{p} = 0.002$, and $l = 0.5$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B1 LAG-ROS Training", "weight": 1.0} -->

$T$, $\mathcal{T}$, and $x_{f}$ in Sec. V-A3 are selected as $T = \mathcal{T} = 9$(s) and $x_{f} = {\lbrack p_{f},0,0,0\rbrack}^{\top}$ for $x$ in Fig. 3, where $p_{f}$ is a random terminal position at each episode.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B1 LAG-ROS Training", "weight": 1.0} -->

We let ${\mathcal{R}{}} = 0$ and ${\overline{d}}_{\epsilon} = {{\overline{b}\epsilon_{\ell}} + \overline{d}} = 0.75$ in (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), and train the neural net of Sec. V-A1 to have ${{({{\overline{d}}_{\epsilon}/\alpha})}\sqrt{\chi}} = 3.15$ with $\alpha = 0.60$ using Algorithm 1. The performance of LAG-ROS (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") is compared with the learning-based planner (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B1 LAG-ROS Training", "weight": 1.0} -->

Guaranteed Stability: A Contraction Theory Approach") and robust tube-based planner (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

Note that the robust tube-based motion planner (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") (i.e. $u^{\ast}$ of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) is computable with ${\Deltat} \leq {\Deltat_{\max}}$ (see Sec. V-A5) in this case, and thus we expect that the performance of LAG-ROS (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") should be worse than that of (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), as

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

(c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") is a neural net model that approximates (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

The right-hand side of Fig. 3 shows the tracking error $\|{x - x_{d}}\|$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) averaged over $50$ simulations at each time instant $t$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

It is still interesting to see that LAG-ROS of (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") and $u^{\ast}$ of (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") indeed satisfies the exponential bound (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") given as

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

for all $t$ with a small standard deviation $\sigma$, unlike learning-based motion planner (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") with a diverging bound (11 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) and increasing deviation $\sigma$, as can be seen from Fig. 3. Contraction theory enables such quantitative analysis on robustness and stability of learning-based planners, which is one of the major advantages of our proposed technique.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

Table II shows the control performance and computational cost of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") -- (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), which is a good summary of their differences and trade-offs aforementioned in Sec.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

(a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") approximates $u_{d}$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), and thus requires lower computational cost ${\Deltat} = 0.03$(s) with a smaller objective value ${\int{{\| u\|}^{2}{dt}}} = 479$, but robustness is not guaranteed (Lemma 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) resulting in a $40\%$ success rate.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

(b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") computes $u^{\ast}$ of Theorem 2, and thus possesses robustness as in Fig. 3 resulting in a $100\%$ success rate, but requires larger ${\Deltat} = 0.1$(s) to compute $x_{d}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

(c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") approximates $u^{\ast}$ independently of $x_{d}$, and thus possesses robustness of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") as in Fig. 3 resulting in a $100\%$ success rate, even with ${\Deltat} = 0.03$(s) as small as that of (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

It yields $9.2\%$ larger $\int{{\| u\|}^{2}{dt}}$ than (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") as it models ${(x,o_{\ell},t)}\mapsto u^{\ast}$, not ${(x,o_{\ell},t)}\mapsto u_{d}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-B2 Simulation Results and Discussions", "weight": 1.0} -->

It is demonstrated that LAG-ROS indeed possesses the robustness and stability guarantees of $u^{\ast}$ as in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), unlike (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), with significantly lower computational cost than that of (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") as expected.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-C Multi-Agent Nonlinear Motion Planning", "weight": 1.0} -->

The advantages of (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") demonstrated in Sec. V-B are more appreciable in the problem settings where the robust tube-based motion planner (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") is no longer capable of computing a global solution with ${\Deltat} \leq {\Deltat_{\max}}$ (see Sec. V-A5).

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-C Multi-Agent Nonlinear Motion Planning", "weight": 1.0} -->

We thus consider motion planning and collision avoidance of multiple robotic simulators in a cluttered environment with external disturbances, where the agents are supposed to perform tasks based only on local observations $o_{\ell}$ of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"). Note that its nonlinear equation of motion is given in and all of its parameters are normalized to $1$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-C1 LAG-ROS Training", "weight": 1.0} -->

We select $T$, $\mathcal{T}$, and $x_{f}$ in Sec. V-A3 as $T = 30$(s), $\mathcal{T} = 45$(s), and $x_{f} = {\lbrack p_{xf},p_{yf},0,0\rbrack}^{\top}$, where $(p_{xf},p_{yf})$ is a random position in ${} \leq {(p_{xf},p_{yf})} \leq {}$. We let ${\mathcal{R}{}} = 0$, and train the neural network of Sec. V-A1 by Algorithm 1 to get ${{({{\overline{d}}_{\epsilon}/\alpha})}\sqrt{\chi}} = 0.125$ with $\alpha = 0.30$ in (7 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")).

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-C1 LAG-ROS Training", "weight": 1.0} -->

is used for sampling $(x_{d},u_{d})$ by Theorem 3 with an input constraint $u_{i} \geq {0,{\forall i}}$ to avoid collisions with a random number of multiple circular obstacles ($0.5$m in radius) and of other agents, even under the learning error and disturbances. When training LAG-ROS, the input constraint is satisfied by using a ReLU function for the network output, and the localization technique is used to extract $o_{\ell}$ of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") from $o_{g}$ of (1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) for its distributed implementation, with the communication radius $2.0$m.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-C1 LAG-ROS Training", "weight": 1.0} -->

Its performance is compared with (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), and a centralized planner (d) ‣ V-C1 LAG-ROS Training ‣ V-C Multi-Agent Nonlinear Motion Planning ‣ V Simulation ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") which is not computable with ${\Deltat} \leq {\Deltat_{\max}}$, where $\Deltat$ is given in Sec.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-C1 LAG-ROS Training", "weight": 1.0} -->

Centralized robust motion planner:\
${(x,x_{d},u_{d},t)}\mapsto u^{\ast}$, offline centralized solution of (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-C2 Remarks on Sub-optimal Trajectories", "weight": 1.0} -->

Multi-agent problems have sub-optimal solutions with optimal values close to the global optimum, and thus (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") does not necessarily take the same $x_{d}$ as that of the centralized planner (d) ‣ V-C1 LAG-ROS Training ‣ V-C Multi-Agent Nonlinear Motion Planning ‣ V Simulation ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") in the presence of disturbances, as depicted in Fig. 5. However, it implicitly guarantees tracking to its own (sub-)optimal $x_{d}$ due to Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), which means we can still utilize their objective value $\int{{\| u\|}^{2}{dt}}$ and success rate to evaluate their performance.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-C3 Implication of Simulation Results", "weight": 1.0} -->

For (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), the tracking error accumulates exponentially with time due to $\overline{d}$ (Lemma 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), which necessitates the use of safety control for avoiding collisions. Such non-optimal control inputs also increase the error in (11 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) as (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") does not possess any robustness guarantees.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-C3 Implication of Simulation Results", "weight": 1.0} -->

For (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), robustness is guaranteed by Theorem 2 but can only obtain locally optimal $(x_{d},u_{d})$ of (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), as its time horizon has to be small enough to make the problem solvable within ${\Deltat} \leq {\Deltat_{\max}} = 0.1$(s), and the agent only has access to local information. This renders some agents stuck in local minima as depicted in Fig. 4.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-C3 Implication of Simulation Results", "weight": 1.0} -->

LAG-ROS (c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") tackles these two problems by providing formal robustness and stability guarantees of Theorems 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") -- 4, whilst implicitly knowing the global solution (only from the local information $o_{\ell}$ as in ) without computing it online. It satisfies the given state constraints due to Theorem 3 as can be seen from Fig. 4

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-C4 Simulation Results and Discussions", "weight": 1.0} -->

(a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") satisfies the requirement on the computational cost since we have ${\Deltat} \leq {\Deltat_{\max}} = 0.1$(s) as shown in Table III, but its success rate remains the lowest for all $\overline{d} = {\sup_{x,t}{\|{d{(x,t)}}\|}}$ due to the cumulative error (11 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) of Lemma 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), as can be seen in Fig. 5 and Table III.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-C4 Simulation Results and Discussions", "weight": 1.0} -->

Although its objective value is the smallest for $\overline{d} \leq 0.6$ since it models $u_{d}$, it gets larger for larger $\overline{d}$, due to the lack of robustness to keep $x$ around $x_{d}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-C4 Simulation Results and Discussions", "weight": 1.0} -->

(b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") has a success rate higher than that of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), but still lower than $50$% as it can only compute sub-optimal $x_{d}$ under the limited computational capacity. In fact, we have ${\Deltat} \geq {\Deltat_{\max}}$ in this case, which means it requires a slightly better onboard computer. Also, it uses excessive control effort larger than $10^{3}$ due to such sub-optimality.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-C4 Simulation Results and Discussions", "weight": 1.0} -->

(c) ‣ II-B Stability Guarantees of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") achieves more than $90$% success rates for all $\overline{d}$, and its objective value remains only $1.64$ times larger than that of the centralized planner (d) ‣ V-C1 LAG-ROS Training ‣ V-C Multi-Agent Nonlinear Motion Planning ‣ V Simulation ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), even without computing $(x_{d},u_{d})$ of (2 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")) online.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C4 Simulation Results and Discussions", "weight": 1.0} -->

Its computational cost is as low as that of (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), satisfying ${\Deltat} \leq {\Deltat_{\max}} = 0.1$(s) while retaining a standard deviation smaller than (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach").

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C4 Simulation Results and Discussions", "weight": 1.0} -->

These results imply that LAG-ROS indeed enhances learning-based motion planners (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") with robustness and stability guarantees of contraction theory as in (d) ‣ V-C1 LAG-ROS Training ‣ V-C Multi-Agent Nonlinear Motion Planning ‣ V Simulation ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") (and (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach")), thereby bridging the technical gap between them.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we propose a new learning-based motion planning framework, called LAG-ROS, with the formal robustness and stability guarantees of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"). It extensively utilizes contraction theory to provide an explicit exponential bound on the distance between the target and controlled trajectories, even under the existence of the learning error and external disturbances. Simulation results demonstrate that it indeed satisfies the bound in practice, thereby yielding consistently high success rates and control performances in contrast to the existing motion planners (a) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach") and (b) ‣ II-A Problem Formulation of LAG-ROS ‣ II Learning-based Robust Motion Planning with Guaranteed Stability (LAG-ROS) ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"). Note that other types of disturbances can be handled, using for stochastic systems and for parametric uncertain systems.
