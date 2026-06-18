<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Goal-Conditioned Neural ODEs with Guaranteed Safety and Stability for Learning-Based All-Pairs Motion Planning

Topics include Motion planning, Stability analysis, Safety, Neural networks, Planning, Learning, Exponential stability, Ordinary differential equation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a learning-based approach for all-pairs motion planning, where the initial and goal states are allowed to be arbitrary points in a safe set. We construct smooth goal-conditioned neural ordinary differential equations (neural ODEs) via bi-Lipschitz diffeomorphisms. Theoretical results show that the proposed model can provide guarantees of global exponential stability and safety (safe set forward invariance) regardless of goal location. Moreover, explicit bounds on convergence rate, tracking error, and vector field magnitude are established. Our approach admits a tractable learning implementation using bi-Lipschitz neural networks and can incorporate demonstration data. We illustrate the effectiveness of the proposed method on a 2D corridor navigation task.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning in environments with complex geometric constraints -- arising from obstacles, workspace boundaries, and configuration space structure -- remains a fundamental challenge in robotics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical sampling-based methods such as probabilistic roadmaps (PRM) and rapidly-exploring random trees (RRT) are simple to implement and widely used, but suffer from certain limitations. In particular, they are inherently finite in their representation: RRTs are generated from a fixed start position (single-query) while PRMs can handle a finitely-many sampled start and end positions (multi-query). They do not define a smooth feedback policy from all possible start and end positions (all-pairs). Furthermore, they are inherently model-based and difficult to adapt to learning-based methodologies such as learning from demonstration (LfD).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An emerging paradigm represents the desired motion via a continuous dynamical system whose solutions serve directly as executable trajectories, see e.g.. This approach has the advantage that it effectively defines a feedback policy, so it is robust, adaptable, and real-time implementable, and compatible with learning frameworks such as LfD when the dynamical models are parameterized, e.g. neural ordinary differential equations (neural ODEs).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The dynamical systems approach to robot motion generation can be traced back to classical approaches such as potential fields which combine attractive and repulsive forces but suffer can from local minima and instability in narrow passages. Mitigating these issues remains an ongoing research activity. Navigation function, introduced by Koditschek and Rimon, provide a theoretical foundation that is closely related to the concept of a Lyapunov function. They provide a construction of for simplified "sphere worlds", and showed how they can in principle be adapted to more complex but topologically-equivalent spaces via diffeomorphisms, however at the time constructive methods were lacking.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The central challenge therefore is designing (or learning) a dynamical system with the required properties: it should be sufficiently smooth, flexible enough to reproduce the desired task behavior, have some (preferably global) stability properties, and provide the ability to avoid obstacles or other unsafe regions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lyapunov stability theory provides a principled framework for designing stable dynamical systems. The classical work of Wilson, combined with the resolution of the generalized Poincaré Conjecture established that all Lyapunov functions have level sets homeomorphic to spheres, and diffeomorphic for all dimensions other than five. Such results are closely related to the problem of global linearization of nonlinear systems, see and references therein. This naturally suggests parameterizing Lyapunov functions as the composition of a diffeomorphism and a simple quadratic.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Early work ensuring stability in the dynamical systems approach to motion planning relied on quadratic Lyapunov functions, limiting flexibility. Increasing flexibility via state diffeomorphisms has been explored from several directions. To our knowledge it was first applied the context of stable nonlinear system identification: learned contracting dynamics via polynomial diffeomorphisms of the state space, enforced via sum-of-squares programming. The idea was explicitly applied to robot motion planning, by integrating diffeomorphisms with the method of, however the class of diffeomorphisms was quite limited. A more flexible class of diffeomorphisms based on Gaussian radial basis function kernels was investigated.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, neural network methods based on normalizing flows have been developed and extended to limit cycles and adaptation to environmental changes. The present paper builds most directly, which proposed a class of exponentially stable neural dynamics constructed using bi-Lipschitz neural networks. This model class provides not only certified stability but explicit bounds on the rate of stability and potential overshoot, as well as fast splitting-based algorithms for inversion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotics includes many potentially safety-critical or mission-critical applications, and certifying safety of learning-based methods is a major area of current research (see, e.g., the reviews and references therein). In the context of the dynamical systems approach to motion planning, a recent work proposed combining learned neural ODEs with control Lyapunov functions (CLFs) and control barrier functions (CBFs). On the other hand, it is known that existence of a CLF and a CBF separately does not guarantee existence of a compatible CLF-CBF pair, which complicates the learning setup.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the aforementioned approaches to ensuring stability and safety in dynamical systems LfD, it is generally assumed that the goal-state of the motion is fixed before the learning process, i.e. it is a single-query setup. Changes to the goal state can sometimes be incorporated, but would generally require retraining and/or fresh certification of stability and safety of the resulting motion.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. In this paper, we propose a class of goal-conditioned neural dynamical systems that incorporate built-in guarantees of global exponential stability and safety (safe set forward invariance), for all combinations of initial state and goal state within the safe set. The models are compatible with learning-based paradigms for motion planning, such as learning from demonstration. The main contributions are: a systematic approach for constructing goal-conditioned dynamical systems via diffeomorphisms; theoretical results establishing guarantees of safety and exponential stability regardless of goal location; a tractable machine learning formulation for a diffeomorphism; empirical validation confirming the effectiveness of the proposed approach.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A The Dynamic Approach for Motion Planning", "weight": 1.0} -->

The basic motion planning problem in robotics usually considers the robot dynamics to be fully-actuated and velocity-controlled, i.e.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A The Dynamic Approach for Motion Planning", "weight": 1.0} -->

where ${x{(t)}} \in \mathcal{X} \subseteq {\mathbb{R}}^{n}$ is the state, e.g., $x{(t)}$ could be the position of a robot arm's end effector.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A The Dynamic Approach for Motion Planning", "weight": 1.0} -->

While the dynamics are very simple, the difficulty comes from two sources. Firstly, the requirement for collision avoidance and other safety constraints, which can be represented as

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A The Dynamic Approach for Motion Planning", "weight": 1.0} -->

where $\mathcal{X}_{\text{safe}} \subset \mathcal{X}$ is a safe set that may have complex geometry. We denote by $\mathcal{X}_{\text{unsafe}}$ its complement $\mathcal{X}_{\text{unsafe}} = {\mathcal{X} \smallsetminus \mathcal{X}_{\text{safe}}}$, i.e., the set of unsafe states.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A The Dynamic Approach for Motion Planning", "weight": 1.0} -->

Secondly, the motion task may be complex and only partially specified. While it usually includes motion towards a goal position $x_{\star}$, among the infinite variety of possible motions approach the same goal, the desirable ones may be specified only indirectly via a limited set of demonstration data. The robot motion should not only accurately reproduce the training demonstrations, but also generalize to new conditions and react gracefully to disturbances. This generally requires some form of smoothness and stability of the dynamics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Problem Statement", "weight": 1.0} -->

In this work, we focus on a learning-based *all-pairs* motion planning problem, where both $x_{0}$ and $x_{\star}$ are allowed to be arbitrary points in $\mathcal{X}_{\text{safe}}$. Specifically, we aim to learn a smooth goal-conditioned dynamical system of the form

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 1", "weight": 1.0} -->

and additionally some task-relevant data for the system's desired behaviour inside the safe set, e.g.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem 1", "weight": 1.0} -->

The system is safe w.r.t. the set $\mathcal{X}_{\text{safe}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem 1", "weight": 1.0} -->

The system is globally equilibrium-independent exponentially stable.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem 1", "weight": 1.0} -->

The system effectively mimics the demonstration data $\mathcal{D}_{\text{demo}}$ inside $\mathcal{X}_{\text{safe}}$, or otherwise meets the training objectives, and generalizes smoothly.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem 1", "weight": 1.0} -->

We note that the first three objectives can be considered hard constraints, with the caveat that the first requirement depends on the extent that the data sets $\mathcal{D}_{\text{safe}}$ and $\mathcal{D}_{\text{unsafe}}$ accurately represent the true sets $\mathcal{X}_{\text{safe}},\mathcal{X}_{\text{unsafe}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem 1", "weight": 1.0} -->

The fourth requirement is somewhat loose, but will generally be supported by having a sufficiently flexible class of models to meet the training objective while ensuring satisfaction of the first three requirements, as well as some possibility to tune the smoothness of the model.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Preliminaries on Bi-Lipschitz Diffeomorphisms", "weight": 1.0} -->

To formulate our approach, we first require some technical machinery.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main Theoretical Results", "weight": 1.0} -->

In this section, we provide a systematic approach to construct an all-pairs motion planner using bi-Lipschitz diffeomorphisms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A All-Pairs Motion Planning via Natural Gradient Flow", "weight": 1.0} -->

Let $g:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ be a bi-Lipschitz diffeomorphism. We take the candidate Lyapunov function as follows

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A All-Pairs Motion Planning via Natural Gradient Flow", "weight": 1.0} -->

where $\lambda > 0$ is a tunable parameter. We then construct the dynamics based on the natural gradient flow of $V{(x,x_{\star})}$, i.e.,

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A All-Pairs Motion Planning via Natural Gradient Flow", "weight": 1.0} -->

The matrix inverse is well-defined due to, and the system has a unique equilibrium point at $x_{\star}$. Our main theoretical result is as follows.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

While can be considered as a feedback controller to be implemented in real-time for the system, there is also often need to predict future motions in simulation. For this case, we can sample the analytic solution for $z{(t)}$ at a grid of points, and pass them in parallel through $g^{- 1}$ to obtain $x{(t)}$. When a fast inverse algorithm is available $g$, as, this can be done in parallel on a GPU.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It can be shown that system is incrementally exponentially stable w.r.t. the incremental Lyapunov $V{(x_{1},x_{2})}$. From the contraction theory perspective, system is contracting w.r.t. the metric $M{(x)}$ in \[33, Thm. 1\], see also.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It is clear from the proof that without any additional effort, we can extend the above theorem by replacing the set $\mathcal{B}^{n}$ to any convex, compact set $\mathcal{Z}_{\text{safe}}$ so that $\mathcal{X}_{\text{safe}}$ admits more complicated shapes (e.g., with sharp corners).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3", "weight": 1.0} -->

If $\mathcal{X}_{\text{safe}}$ is not diffeomorphic to a ball, e.g., $\mathcal{X}_{\text{safe}}$ contains holes, then the approach needs to be modified. The navigation function approach includes strategies for dealing with this via diffeomorphism to a "sphere world" in which the free space is a ball with a finite number of ball-shaped obstacles removed. Under certain conditions, almost-global stability can still be certified. We leave the details of the extension for a future work.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Safety Properties", "weight": 1.0} -->

The key property of our approach is that it guarantees safety for arbitrary start/goal pairs. In the control literature, safety in the form of forward invariance of a set is often certified by a barrier function, as defined below (see e.g.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Time-Varying Goal Location", "weight": 1.0} -->

When the goal position is time-varying with uncertain but bounded velocity, e.g. to reach for a moving object, the following result shows that our approach still guarantees safety and converges to a bounded region around the goal.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D Finite-time Convergence via Euclidean Norm Potential", "weight": 1.0} -->

Similar to, the proposed Lyapunov function $V{(x,x_{\star})}$ can incorporate a more general potential function $\Phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, i.e.,

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-D Finite-time Convergence via Euclidean Norm Potential", "weight": 1.0} -->

Then, the dynamics of in the $\mathcal{Z}$-space becomes

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-D Finite-time Convergence via Euclidean Norm Potential", "weight": 1.0} -->

which can be pulled back in to $\mathcal{X}$ space. If $\Phi$ continuously differentiable and satisfies the *Polyak-Łojasiewicz* (PL) condition, then global exponential stability can still be established.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-D Finite-time Convergence via Euclidean Norm Potential", "weight": 1.0} -->

If finite-time convergence is desired, then $\Phi$ can be taken as the Euclidean norm (i.e., ${\Phi{(z)}} = {\lambda{|z|}}$), instead of the norm squared, and then system becomes

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-D Finite-time Convergence via Euclidean Norm Potential", "weight": 1.0} -->

although the dynamics is not smooth at the goal $z_{\star}$. Since the resulting trajectory has unit velocity in $\mathcal{Z}$ space, we can, analogously to Theorem 1, obtain simple upper and lower bounds on the vector field velocity in the $\mathcal{X}$-space, i.e.,

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-E Natural Gradient Flow v.s. Gradient Flow", "weight": 1.0} -->

A natural question for the proposed approach is: what advantages does natural gradient flow offer over standard gradient flow? Our answer is as follows: standard gradient flow does not provide safety guarantees when $x_{\star}$ varies.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-E Natural Gradient Flow v.s. Gradient Flow", "weight": 1.0} -->

From \[19, Thm. 1\], we can conclude that the above system achieves equilibrium-independent exponential stability. However, it cannot provide safety guarantees for all $x_{\star} \in \mathcal{X}_{\text{safe}}$, see the example below.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1", "weight": 1.0} -->

When $x_{\star} = {}$, we have that $V{(x,x_{\star})}$ is a barrier function for both and. Thus, $\mathcal{X}_{\text{safe}}$ is forward invariant in both cases, see Fig. 2(a). When $x_{\star}$ changes, it is no longer a barrier function as $V{(x,x_{\star})}$ is not a constant for $x \in {\partial\mathcal{X}_{\text{safe}}}$. Fig. 2(b) shows that $\mathcal{X}_{\text{safe}}$ is no longer a forward-invariant set. This is also supported by the fact that its vector field points outward at some part of the boundary. For the proposed approach, $\mathcal{X}_{\text{safe}}$ is forward invariant as the vector field of always points inward for all $x_{\star} \in \mathcal{X}_{\text{safe}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 1", "weight": 1.0} -->

A barrier function $h{(x)}$ can be constructed via.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-F Comparison with Navigation Function based Approach", "weight": 1.0} -->

When the goal state $x_{\star}$ is fixed, a classical approach to construct system is via gradient flow

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-F Comparison with Navigation Function based Approach", "weight": 1.0} -->

$\phi$ is Morse function (i.e., $\phi$ is smooth and it has no degenerate critical point);

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-F Comparison with Navigation Function based Approach", "weight": 1.0} -->

$\phi$ has a unique minimum on $\mathcal{X}_{\text{safe}}$ at $x_{\star}$ and no other critical points;

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-F Comparison with Navigation Function based Approach", "weight": 1.0} -->

The navigation function $\phi$ serves as both a Lyapunov function and a barrier function since

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-F Comparison with Navigation Function based Approach", "weight": 1.0} -->

Compared with the navigation based approach, our method is more flexible as it does not require recomputing $g$ when $x_{\star}$ changes since it uses different certificate functions for stability and safety, although both are expressed in terms of a single learned diffeomorphism $g$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-G Compared with Existing Diffeomorphism based Dynamical Approaches", "weight": 1.0} -->

The diffeomorphism based approach has also been recently explored for learning stable neural ODE from demonstration, see.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-G Compared with Existing Diffeomorphism based Dynamical Approaches", "weight": 1.0} -->

where the potential function $\Phi$ is positive definite, convex, continuously differentiable, and radially unbounded. And a natural gradient dynamics in the $\mathcal{X}$-space is constructed by pulling back to the $\mathcal{X}_{\text{safe}}$-space via a diffeomorphism $g$. The primary goal of those approaches is to learn stable dynamics that mimics the demonstration data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-G Compared with Existing Diffeomorphism based Dynamical Approaches", "weight": 1.0} -->

Different from those approaches, our method can learn both stable and safe dynamics from data. The second difference is that our approach can generalize to unseen goal point without retraining the model. Finally, our approach imposes explicit bounds on the diffeomorphism $g$, which can be seen as effective regularization preventing overfitting. Meanwhile, explicit bounds on tracking error and vector field magnitude can be obtained, which is useful for practical applications.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Learning an All-Pairs Motion Planner", "weight": 1.0} -->

In this section, we aim to translate the above theoretical construction into a tractable machine learning setup, detailing the choice of training data, model class, and loss functions.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Learning an All-Pairs Motion Planner", "weight": 1.0} -->

We parameterize the diffeomorphism $g$ by some smooth bi-Lipschitz neural network $g_{\theta}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ with $\theta \in {\mathbb{R}}^{p}$ as the learnable parameter. By construction, system is smooth and globally equilibrium-independent experientially stable, as shown in Theorem 1. To ensure safety, one needs to learn a $g_{\theta}$ that can be used to characterize the set $\mathcal{X}_{\text{safe}}$. Since a candidate Lyapunov function $V{(x,x_{\star})}$ is used in the model construct, we seek to separate the safe and unsafe datasets in via a Lyapunov sublevel set of $V$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A Training Data", "weight": 1.0} -->

To solve the above learning problem, we need to assign labels to the points from the datasets $\mathcal{D}_{\text{safe}}$ and $\mathcal{D}_{\text{unsafe}}$. An intuitive approach is to associate $x_{i} \in \mathcal{D}_{\text{safe}}$ and $x_{j} \in \mathcal{D}_{\text{unsafe}}$ with labels of 0 and 1, respectively. The learning problem in is formulated as a classification task, where ${\overset{\sim}{V}}_{\theta}{(x)}$ is the classifier. However, those labels do not provide informative geometric information in $\mathcal{D}_{\text{safe}}$ and $\mathcal{D}_{\text{unsafe}}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-A Training Data", "weight": 1.0} -->

By leveraging the existing sampling-based motion planning algorithms (e.g. PRM or RRT ), we can assign each point $x_{i} \in \mathcal{D}_{\text{safe}}$ with a label $c_{i}$ indicating the shortest path length from $x_{i}$ to the targe ${\hat{x}}_{\star}$. Specifically, we first construct a graph by connecting each $x_{i}$ to a set of its nearby neighbors in $\mathcal{D}_{\text{safe}}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A Training Data", "weight": 1.0} -->

From this graph, we can define the cost-to-go function $d:{\mathcal{D}_{\text{safe}}\rightarrow{\mathbb{R}}_{\geq 0}}$ as the shortest path distance from sample $x \in \mathcal{D}_{\text{safe}}$ to the goal ${\hat{x}}_{\star}$, which is a proxy for the distance between $x_{i}$ and ${\hat{x}}_{\star}$. The function $d{(x)}$ naturally reflects the geometry of $\mathcal{X}_{\text{safe}}$: samples near the goal attain small values, while samples that are distant or geometrically separated from ${\hat{x}}_{\star}$ attain large values. Thus, $d{(x)}$ provides meaningful information for training ${\overset{\sim}{V}}_{\theta}{(x)}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Training Data", "weight": 1.0} -->

where $\overline{c}$ is the maximum label value in ${\overline{\mathcal{D}}}_{\text{safe}}$, and $\delta > 0$ is a hyperparameter which ensures that there exists $c \in {\lbrack\overline{c},{\overline{c} + \delta}\rbrack}$ satisfying.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Model Class", "weight": 1.0} -->

In this work, we use the BiLipNet as the model class for $g_{\theta}$. BiLipNets can enforce certified bi-Lipschitz bounds $\mu$ and $\nu$ via a method derived from which are, to the authors knowledge, the tightest available. The bi-Lipschitz bounds are trainable parameters, and their ratio $\frac{\nu}{\mu}$ can be considered a tunable distortion parameter, describing how much the learnt representation of $\mathcal{X}_{\text{safe}}$ distorts from a unit ball, and therefore how much the learnt trajectories can deviate from straight lines -- notice that this also appears in the overshoot constant for our exponential convergence bound. The lower bound $\mu$ also appears in our bound on velocity.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B Model Class", "weight": 1.0} -->

BiLipNets have a number of other advantages: firstly, BiLipNets admits a direct model parameterization, which allows training within the standard unconstrained optimization methods such as stochastic gradient descent. Secondly, the feedthrough layer architecture can improve the model expressivity without suffering from vanishing gradients. Thirdly, BiLipNets have a structure that admits fast splitting-based solvers for computing the model inverse.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-C Loss Function", "weight": 1.0} -->

The loss function will generally include two components. The first component trains the diffeomorphism to map the safe set $\mathcal{X}_{\text{safe}}$ onto the unit ball. However, this leaves substantial flexibility for the shape of the mapping inside $\mathcal{X}_{\text{safe}}$, so a second task-specific loss term can be employed which may take many forms, e.g. training the dynamics to mimic demonstration trajectories.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-C Loss Function", "weight": 1.0} -->

For the first task, i.e., achieving, we choose the following loss function

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-C Loss Function", "weight": 1.0} -->

The loss function for the second task may take various forms. E.g., when the demonstration dataset is available, we can define

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We illustrate the proposed approach on a 2D corridor navigation task (see Fig. 3), where we aim to generate safe and smooth trajectories from any initial configuration $x_{0} \in \mathcal{X}_{\text{safe}}$ to any goal $x_{\star} \in \mathcal{X}_{\text{safe}}$ in the presence of geometric obstacles. All experiments are implemented in Python using JAX and executed on an NVIDIA RTX 4090 GPU. Code is available at

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-A Data Generation and Training details", "weight": 1.0} -->

As shown in Fig. 3 (left), we initialized RRT at a fixed goal ${\hat{x}}_{\star}$ to generate a shortest-path tree over $\mathcal{X}_{\text{safe}}$. This automatically provides the dataset pair $(x_{i},{d{(x_{i})}})$ where $d{(x_{i})}$ is the cost-to-go with $x_{i} \in \mathcal{X}_{\text{safe}}$, see Fig. 3 (right). We take 2,500 samples to formulate the dataset ${\overline{\mathcal{D}}}_{\text{safe}}$ in (34a). Another 2,500 samples are uniformly sampled in $\mathcal{X}_{\text{unsafe}}$, which forms ${\overline{\mathcal{D}}}_{\text{unsafe}}$ in (34b).

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A Data Generation and Training details", "weight": 1.0} -->

We use BiLipNet from to parameterize the bi-Lipschitz diffeomorphism $g_{\theta}$. The network is trained based on the loss function in via the Adam optimizer with a batch size of 16 for 1500 epochs.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-B Results and Discussions", "weight": 1.0} -->

Fig. 1 shows the learned mapping $g$ that transforms $\mathcal{X}_{\text{safe}}^{\prime} \subset \mathcal{X}_{\text{safe}}$ in the $\mathcal{X}$-space (Left) to a unit ball $\mathcal{B}^{2}$ in the $\mathcal{Z}$-space (Right). $\partial\mathcal{X}_{\text{safe}}^{\prime}$ and $\partial\mathcal{B}^{2}$ are indicated by red curves while $\partial\mathcal{X}_{\text{safe}}$ is in black. $\partial\mathcal{X}_{\text{safe}}^{\prime}$ conforms to the geometry of the obstacle boundaries, which is neither convex nor star-convex.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-B Results and Discussions", "weight": 1.0} -->

Fig. 4 shows that complex trajectories of the natural gradient flow system (left) are equivariant to linear trajectories of system (right) under the coordination change. Pulling back straight lines in $\mathcal{Z}$-space (Fig. 4 right) through $g_{\theta}^{- 1}$ yields safe trajectories in $\mathcal{X}_{\text{safe}}$ (Fig. 4 left) that respect the obstacle geometry. All trajectories in Fig. 4 (left) also converge to ${\hat{x}}_{\star}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-B Results and Discussions", "weight": 1.0} -->

Fig. 5 illustrates that multiple trajectories converge to a distinct, previously unseen goal $x_{\star}$ (red cross). This indicates system is equilibrium-independent stable and safe. Note that the model was trained using data corresponding to a single goal, but it generalizes gracefully to a goal in a completely different location.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we presented a learning-based approach for safe, stable, and smooth all-pairs motion planning. Our approach uses a bi-Lipschitz diffeomorphism to transform a geometrically complex safe set into the unit ball, and complex motions within this set into simple linear stable dynamics which corresponds to a goal-conditioned natural gradient in the original state space. This approach guarantees that both safety and exponential stability are preserved regardless of the goal location within the safe set. Empirical results in 2D corridor navigation task illustrate the the proposed approach.
