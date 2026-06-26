## Introduction

Motion planning in environments with complex geometric constraints -- arising from obstacles, workspace boundaries, and configuration space structure -- remains a fundamental challenge in robotics.

Classical sampling-based methods such as probabilistic roadmaps (PRM) and rapidly-exploring random trees (RRT) are simple to implement and widely used, but suffer from certain limitations. In particular, they are inherently finite in their representation: RRTs are generated from a fixed start position (single-query) while PRMs can handle a finitely-many sampled start and end positions (multi-query). They do not define a smooth feedback policy from all possible start and end positions (all-pairs). Furthermore, they are inherently model-based and difficult to adapt to learning-based methodologies such as learning from demonstration (LfD).

An emerging paradigm represents the desired motion via a continuous dynamical system whose solutions serve directly as executable trajectories, see e.g.. This approach has the advantage that it effectively defines a feedback policy, so it is robust, adaptable, and real-time implementable, and compatible with learning frameworks such as LfD when the dynamical models are parameterized, e.g. neural ordinary differential equations (neural ODEs).

The dynamical systems approach to robot motion generation can be traced back to classical approaches such as potential fields which combine attractive and repulsive forces but suffer can from local minima and instability in narrow passages. Mitigating these issues remains an ongoing research activity. Navigation function, introduced by Koditschek and Rimon, provide a theoretical foundation that is closely related to the concept of a Lyapunov function. They provide a construction of for simplified "sphere worlds", and showed how they can in principle be adapted to more complex but topologically-equivalent spaces via diffeomorphisms, however at the time constructive methods were lacking.

Figure 1: Our approach is based on learning a bi-Lipschitz diffeomorphism g that maps a geometrically complex safe set 𝒳safe in the 𝒳-space (left) onto the unit ball in the 𝒵-space (right). Then simple straight-line point-to-point motions in 𝒵-space can be smoothly pulled back to 𝒳 space, defining a goal-conditioned neural ODE which guarantees stability and safety and takes the form of a natural gradient flow.

The central challenge therefore is designing (or learning) a dynamical system with the required properties: it should be sufficiently smooth, flexible enough to reproduce the desired task behavior, have some (preferably global) stability properties, and provide the ability to avoid obstacles or other unsafe regions.

Lyapunov stability theory provides a principled framework for designing stable dynamical systems. The classical work of Wilson, combined with the resolution of the generalized Poincaré Conjecture established that all Lyapunov functions have level sets homeomorphic to spheres, and diffeomorphic for all dimensions other than five. Such results are closely related to the problem of global linearization of nonlinear systems, see and references therein. This naturally suggests parameterizing Lyapunov functions as the composition of a diffeomorphism and a simple quadratic.

Early work ensuring stability in the dynamical systems approach to motion planning relied on quadratic Lyapunov functions, limiting flexibility. Increasing flexibility via state diffeomorphisms has been explored from several directions. To our knowledge it was first applied the context of stable nonlinear system identification: learned contracting dynamics via polynomial diffeomorphisms of the state space, enforced via sum-of-squares programming. The idea was explicitly applied to robot motion planning , by integrating diffeomorphisms with the method of, however the class of diffeomorphisms was quite limited. A more flexible class of diffeomorphisms based on Gaussian radial basis function kernels was investigated .

More recently, neural network methods based on normalizing flows have been developed and extended to limit cycles and adaptation to environmental changes. The present paper builds most directly , which proposed a class of exponentially stable neural dynamics constructed using bi-Lipschitz neural networks. This model class provides not only certified stability but explicit bounds on the rate of stability and potential overshoot, as well as fast splitting-based algorithms for inversion.

Robotics includes many potentially safety-critical or mission-critical applications, and certifying safety of learning-based methods is a major area of current research (see, e.g., the reviews and references therein). In the context of the dynamical systems approach to motion planning, a recent work proposed combining learned neural ODEs with control Lyapunov functions (CLFs) and control barrier functions (CBFs). On the other hand, it is known that existence of a CLF and a CBF separately does not guarantee existence of a compatible CLF-CBF pair, which complicates the learning setup.

In the aforementioned approaches to ensuring stability and safety in dynamical systems LfD, it is generally assumed that the goal-state of the motion is fixed before the learning process, i.e. it is a single-query setup. Changes to the goal state can sometimes be incorporated, but would generally require retraining and/or fresh certification of stability and safety of the resulting motion.

Contributions. In this paper, we propose a class of goal-conditioned neural dynamical systems that incorporate built-in guarantees of global exponential stability and safety (safe set forward invariance), for all combinations of initial state and goal state within the safe set. The models are compatible with learning-based paradigms for motion planning, such as learning from demonstration. The main contributions are: a systematic approach for constructing goal-conditioned dynamical systems via diffeomorphisms; theoretical results establishing guarantees of safety and exponential stability regardless of goal location; a tractable machine learning formulation for a diffeomorphism; empirical validation confirming the effectiveness of the proposed approach.

Notation. A mapping $f:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m}$ is said to be of class $C^{k}$ if it has up to $k$th continuous derivatives. A continuously differentiable mapping $g:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ is called a diffeomorphism if it is a bijection and its inverse $g^{-1}$ is also differentiable. Given a $C^{1}$ function $V:\mathbb{R}^{n}\rightarrow\mathbb{R}$, its gradient is taken as $\nabla V:=\bigl(\partial V/\partial x\bigr)^{\top}$. We denote unit ball as $\mathcal{B}^{n}=\{x\in\mathbb{R}^{n}:|x|\leq 1\}$, where $|\cdot|$ is the Euclidean norm. Given a set $X\subset\mathbb{R}^{n}$, we use $\partial X$ and $\mathrm{Int}(X)$ to denote its boundary and interior, respectively.

## Preliminaries and Problem Formulation

### II-A The Dynamic Approach for Motion Planning

The basic motion planning problem in robotics usually considers the robot dynamics to be fully-actuated and velocity-controlled, i.e. where $x(t)\in\mathcal{X}\subseteq\mathbb{R}^{n}$ is the state, e.g., $x(t)$ could be the position of a robot arm's end effector.

While the dynamics are very simple, the difficulty comes from two sources. Firstly, the requirement for collision avoidance and other safety constraints, which can be represented as where $\mathcal{X}_{\text{safe}}\subset\mathcal{X}$ is a safe set that may have complex geometry. We denote by $\mathcal{X}_{\text{unsafe}}$ its complement $\mathcal{X}_{\text{unsafe}}=\mathcal{X}\setminus\mathcal{X}_{\text{safe}}$, i.e., the set of unsafe states.

Secondly, the motion task may be complex and only partially specified. While it usually includes motion towards a goal position $x_{\star}$, among the infinite variety of possible motions approach the same goal, the desirable ones may be specified only indirectly via a limited set of demonstration data. The robot motion should not only accurately reproduce the training demonstrations, but also generalize to new conditions and react gracefully to disturbances. This generally requires some form of smoothness and stability of the dynamics.

### II-B Problem Statement

In this work, we focus on a learning-based *all-pairs* motion planning problem, where both $x_{0}$ and $x_{\star}$ are allowed to be arbitrary points in $\mathcal{X}_{\text{safe}}$. Specifically, we aim to learn a smooth goal-conditioned dynamical system of the form where $f(x_{\star},x_{\star})=0$ for all $x_{\star}\in\mathcal{X}_{\text{safe}}$, i.e. the goal state is an equilibrium.

To formalize the desired properties of, we first recall the following standard definition:

### Definition 1

For a given dynamical system with state $x(t)$, a set $\mathcal{S}$ is called forward invariant if $x\in\mathcal{S}$ implies $x(t)\in\mathcal{S}$ for all $t\geq 0$.

We use the following notions of safety and stability for a goal-conditioned system:

### Definition 2

System is called *safe* w.r.t. the set $\mathcal{X}_{\text{safe}}$ if for any goal state $x_{\star}\in\mathcal{X}_{\text{safe}}$, the set $\mathcal{X}_{\text{safe}}$ is forward invariant.

### Definition 3

System is globally *equilibrium-independent exponentially stable* if for any initial state $x_{0}\in\mathcal{X}$ and any equilibrium $x_{\star}\in\mathcal{X}$, the solution $x(t)$ satisfies for some $\kappa\geq 1$ and $\lambda>0$.

Here we are interested in the following problem.

### Problem 1

Given training data characterising the safe and unsafe sets: and additionally some task-relevant data for the system's desired behaviour inside the safe set, e.g. demonstration data: the goal is to learn a smooth dynamical system of the form with the following properties: The system is safe w.r.t. the set $\mathcal{X}_{\text{safe}}$.

The system has a known bound on velocity on the safe set: $|f(x,x_{\star})|\leq B$ for all $x,x_{\star}\in\mathcal{X}_{\text{safe}}$.

The system is globally equilibrium-independent exponentially stable.

The system effectively mimics the demonstration data $\mathcal{D}_{\text{demo}}$ inside $\mathcal{X}_{\text{safe}}$, or otherwise meets the training objectives, and generalizes smoothly.

We note that the first three objectives can be considered hard constraints, with the caveat that the first requirement depends on the extent that the data sets $\mathcal{D}_{\text{safe}}$ and $\mathcal{D}_{\text{unsafe}}$ accurately represent the true sets $\mathcal{X}_{\text{safe}},\mathcal{X}_{\text{unsafe}}$.

The fourth requirement is somewhat loose, but will generally be supported by having a sufficiently flexible class of models to meet the training objective while ensuring satisfaction of the first three requirements, as well as some possibility to tune the smoothness of the model.

### II-C Preliminaries on Bi-Lipschitz Diffeomorphisms

To formulate our approach, we first require some technical machinery. We extensively utilise bi-Lipschitz diffeomorphisms:

### Definition 4

The diffeomorphism $g:\mathbb{R}^{n}\to\mathbb{R}^{n}$ is said to be *bi-Lipschitz* if for all $x_{1},x_{2}\in\mathbb{R}^{n}$, we have for some $\nu\geq\mu>0$.

Note that $g^{-1}$ is also a bi-Lipschitz diffeomorphism as Moreover, $g$ also induces a Riemmanian metric with $G(x)=\partial g(x)/\partial x$ as the Jacobian of $g$ at $x$, where $M$ gives a notion of local distance. Since $g$ is bi-Lipschitz, $M$ is uniformly bounded, i.e.,

## Main Theoretical Results

In this section, we provide a systematic approach to construct an all-pairs motion planner using bi-Lipschitz diffeomorphisms.

### III-A All-Pairs Motion Planning via Natural Gradient Flow

Let $g:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ be a bi-Lipschitz diffeomorphism. We take the candidate Lyapunov function as follows where $\lambda>0$ is a tunable parameter. We then construct the dynamics based on the natural gradient flow of $V(x,x_{\star})$, i.e., The matrix inverse is well-defined due to, and the system has a unique equilibrium point at $x_{\star}$. Our main theoretical result is as follows.

### Theorem 1

If there exists a bi-Lipschitz diffeomorphism $g:\mathcal{X}_{\text{safe}}\rightarrow\mathcal{B}^{n}$, then the following statements hold: System is safe w.r.t. the set $\mathcal{X}_{\text{safe}}$.

The vector field in is bounded System is globally equilibrium-independent exponentially stable.

### Proof

As shown, under the coordinate transformation $z=g(x)$, system is equivalent to with $z_{\star}=g(x_{\star})$. Thus, system has explicit solutions of Statement 1): The main idea is that under the diffeomorphism $g$, the transformed safe set $\mathcal{Z}_{\text{safe}}:=\mathcal{B}^{n}$ which is convex, and from we have that $z(t)$ is a straight line from $z_{0}$ to $z_{\star}$. Hence for any $z_{0}$ and $z_{\star}$ in $\mathcal{Z}_{\text{safe}}$ the path between them remains in $\mathcal{Z}_{\text{safe}}$, i.e. $z(t)\in\mathcal{Z}_{\text{safe}}$ for all $t\geq 0$. Passing back to $x(t)=g^{-1}(z(t))$, this implies that $x(t)\in\mathcal{X}_{\text{safe}}$ for all $t\geq 0$.

Statement 2): The $\mathcal{Z}$-space dynamics is a push forward map of: which further implies since $z,z_{\star}\in\mathcal{B}^{n}$ and $g$ has lower Lipschitz bound of $\mu$.

Statement 3): Since $g$ is bi-Lipschitz, we obtain System is equilibrium-independent exponentially stable. ∎

### Remark 1

While can be considered as a feedback controller to be implemented in real-time for the system, there is also often need to predict future motions in simulation. For this case, we can sample the analytic solution for $z(t)$ at a grid of points, and pass them in parallel through $g^{-1}$ to obtain $x(t)$. When a fast inverse algorithm is available $g$, as , this can be done in parallel on a GPU.

### Remark 2

It can be shown that system is incrementally exponentially stable w.r.t. the incremental Lyapunov $V(x_{1},x_{2})$. From the contraction theory perspective, system is contracting w.r.t. the metric $M(x)$ in \[33, Thm. 1\], see also.

It is clear from the proof that without any additional effort, we can extend the above theorem by replacing the set $\mathcal{B}^{n}$ to any convex, compact set $\mathcal{Z}_{\text{safe}}$ so that $\mathcal{X}_{\text{safe}}$ admits more complicated shapes (e.g., with sharp corners).

### Corollary 1

Suppose that $g:\mathcal{X}_{\text{safe}}\rightarrow\mathcal{Z}_{\text{safe}}$ is a bi-Lipschitz diffeomorphism, where $\mathcal{Z}_{\text{safe}}\subset\mathbb{R}^{n}$ is a convex and compact set. Then, Statement 1) and 3) hold. For Statement 2), the vector field is bound where $D$ is the diameter of $\mathcal{Z}_{\text{safe}}$, i.e.,

### Remark 3

If $\mathcal{X}_{\text{safe}}$ is not diffeomorphic to a ball, e.g., $\mathcal{X}_{\text{safe}}$ contains holes, then the approach needs to be modified. The navigation function approach includes strategies for dealing with this via diffeomorphism to a "sphere world" in which the free space is a ball with a finite number of ball-shaped obstacles removed. Under certain conditions, almost-global stability can still be certified. We leave the details of the extension for a future work.

### III-B Safety Properties

The key property of our approach is that it guarantees safety for arbitrary start/goal pairs. In the control literature, safety in the form of forward invariance of a set is often certified by a barrier function, as defined below (see e.g. ):

### Definition 5

Consider a nonlinear system $\dot{x}=f(x,t)$. A continuously differentiable function $h:\mathbb{R}^{n}\rightarrow\mathbb{R}$ is called a *barrier function* of $\mathcal{X}_{\text{safe}}$ if there exist a class $\mathcal{K}$ function $\alpha(\cdot)$ such that Note that the Lyapunov function $V(x,x_{\star})$ in is not a barrier function for $\mathcal{X}_{\text{safe}}$ as $V(x,x_{\star})$ may not be a constant for all $x\in\partial\mathcal{X}_{\text{safe}}$. The following result gives an explicit construction of barrier function for the proposed goal-conditioned neural ODE.

### Proposition 1

Suppose that conditions of Theorem 1 hold. Then, the forward invariance of $\mathcal{X}_{\text{safe}}$ can be certified by the following barrier function

### Proof

Since $g:\mathcal{X}_{\text{safe}}\rightarrow\mathcal{B}^{n}$ is a bi-Lipschitz diffeomorphism, then $h(x)$ satisfies (19a) - (19b). The time derivative of $h$ yields For $x\in\mathcal{X}_{\text{safe}}$, we have where the last inequality follows by $g(x),g(x_{\star})\in\mathcal{B}^{n}$. For $x\in\mathcal{X}_{\text{unsafe}}$ (i.e. $|g(x)|>1$ and $h(x)<0$), we can obtain Thus, (19c) holds and $h(x)$ is a barrier function of $\mathcal{X}_{\text{safe}}$. ∎

### III-C Time-Varying Goal Location

When the goal position is time-varying with uncertain but bounded velocity, e.g. to reach for a moving object, the following result shows that our approach still guarantees safety and converges to a bounded region around the goal.

### Theorem 2

Consider system with time-varying goal $x_{\star}(t)$ with $|\dot{x}_{\star}(t)|\leq b$ for all $t\geq 0$. If $g:\mathcal{X}_{\text{safe}}\rightarrow\mathcal{Z}_{\text{safe}}$ is a bi-Lipschitz diffeomorphism, where $\mathcal{Z}_{\text{safe}}$ is a convex compact set, then the following statements hold: The set $\mathcal{X}_{\text{safe}}$ is forward invariant.

The time-varying vector field is bounded For any $x_{0}\in\mathcal{X}_{\text{safe}}$, the tracking error $\epsilon(t):=x(t)-x_{\star}(t)$ satisfies

### Proof

Statement 1): System with time-varying $x_{\star}(t)$ can also be transformed into $\dot{z}=\lambda(z_{\star}(t)-z)$ with $z_{\star}(t)=g(x_{\star}(t))$. Since $\mathcal{Z}_{\text{safe}}$ is compact and convex, then the time-varying vector field $\lambda(z_{\star}(t)-z)$ always points into $\mathcal{Z}_{\text{safe}}$ or is tangent to $\partial\mathcal{Z}_{\text{safe}}$ for any $z\in\partial\mathcal{Z}_{\text{safe}}$ and $z_{\star}(t)\in\mathcal{Z}_{\text{safe}}$. By Nagumo's theorem we obtain that $\mathcal{Z}_{\text{safe}}$ is forward invariant, implying that $\mathcal{X}_{\text{safe}}$ is forward invariant under.

Statement 2) follows directly by and. We now focus on Statement 3). First, the dynamics of $\epsilon_{z}(t):=z(t)-z_{\star}(t)$ in the $\mathcal{Z}$-space can be rewritten as where $|\dot{z}_{\star}(t)|\leq\nu b$. This implies $|\epsilon_{z}(t)|\leq|\epsilon_{z}|e^{-\lambda t}+\nu b/\lambda$. Finally, following the procedure in yields

### III-D Finite-time Convergence via Euclidean Norm Potential

Similar to, the proposed Lyapunov function $V(x,x_{\star})$ can incorporate a more general potential function $\Phi:\mathbb{R}^{n}\rightarrow\mathbb{R}$, i.e., Then, the dynamics of in the $\mathcal{Z}$-space becomes which can be pulled back in to $\mathcal{X}$ space. If $\Phi$ continuously differentiable and satisfies the *Polyak-Łojasiewicz* (PL) condition, then global exponential stability can still be established.

If finite-time convergence is desired, then $\Phi$ can be taken as the Euclidean norm (i.e., $\Phi(z)=\lambda|z|$), instead of the norm squared, and then system becomes although the dynamics is not smooth at the goal $z_{\star}$. Since the resulting trajectory has unit velocity in $\mathcal{Z}$ space, we can, analogously to Theorem 1, obtain simple upper and lower bounds on the vector field velocity in the $\mathcal{X}$-space, i.e.,

### III-E Natural Gradient Flow v.s. Gradient Flow

A natural question for the proposed approach is: what advantages does natural gradient flow offer over standard gradient flow? Our answer is as follows: standard gradient flow does not provide safety guarantees when $x_{\star}$ varies.

Given a Lyapunov function $V(x,x_{\star})$, we consider the following gradient flow dynamics: From \[19, Thm. 1\], we can conclude that the above system achieves equilibrium-independent exponential stability. However, it cannot provide safety guarantees for all $x_{\star}\in\mathcal{X}_{\text{safe}}$, see the example below.

### Example 1

Consider the mapping $g:\mathbb{R}^{2}\to\mathbb{R}^{2}$ defined by where $h(x_{1})=2\sin(x_{1})+\cos(5x_{1})-3x_{1}$. It is a bi-Lipschitz diffeomorphism with $g^{-1}$ defined by $x_{1}=z_{1}$ and $x_{2}=z_{2}-h(z_{1})z_{1}$. We take $\mathcal{Z}_{\text{safe}}=\mathcal{B}^{2}$ and $\mathcal{X}_{\text{safe}}=g^{-1}(\mathcal{Z}_{\text{safe}})$.

Figure 2: Trajectory samples and vector field on the boundary for the natural gradient flow (blue) and the gradient flow (black) with different goal points, where red curves are the boundaries.

When $x_{\star}=$, we have that $V(x,x_{\star})$ is a barrier function for both and. Thus, $\mathcal{X}_{\text{safe}}$ is forward invariant in both cases, see Fig. 2(a). When $x_{\star}$ changes, it is no longer a barrier function as $V(x,x_{\star})$ is not a constant for $x\in\partial\mathcal{X}_{\text{safe}}$. Fig. 2(b) shows that $\mathcal{X}_{\text{safe}}$ is no longer a forward-invariant set . This is also supported by the fact that its vector field points outward at some part of the boundary. For the proposed approach, $\mathcal{X}_{\text{safe}}$ is forward invariant as the vector field of always points inward for all $x_{\star}\in\mathcal{X}_{\text{safe}}$. A barrier function $h(x)$ can be constructed via.

### III-F Comparison with Navigation Function based Approach

When the goal state $x_{\star}$ is fixed, a classical approach to construct system is via gradient flow where $\phi:\mathcal{X}_{\text{safe}}\to$ is a *navigation function* satisfying the following conditions: $\phi$ is Morse function (i.e., $\phi$ is smooth and it has no degenerate critical point); $\phi$ has a unique minimum on $\mathcal{X}_{\text{safe}}$ at $x_{\star}$ and no other critical points; $\nabla\phi$ is bounded on $\mathcal{X}_{\text{safe}}$; $\phi(x)=1$ for all $x\in\partial\mathcal{X}_{\text{safe}}$.

The navigation function $\phi$ serves as both a Lyapunov function and a barrier function since Note that $\phi(x)=|g(x)|^{2}$ with $g:\mathcal{X}_{\text{safe}}\rightarrow\mathcal{B}^{n}$ and $g(x_{\star})=0$ is a validate navigation function. However, one needs to recompute $g$ when $x_{\star}$ changes.

Compared with the navigation based approach, our method is more flexible as it does not require recomputing $g$ when $x_{\star}$ changes since it uses different certificate functions for stability and safety, although both are expressed in terms of a single learned diffeomorphism $g$.

### III-G Compared with Existing Diffeomorphism based Dynamical Approaches

The diffeomorphism based approach has also been recently explored for learning stable neural ODE from demonstration, see. Specifically, those approaches take the following gradient flow in the $\mathcal{Z}$-space: where the potential function $\Phi$ is positive definite, convex, continuously differentiable, and radially unbounded. And a natural gradient dynamics in the $\mathcal{X}$-space is constructed by pulling back to the $\mathcal{X}_{\text{safe}}$-space via a diffeomorphism $g$. The primary goal of those approaches is to learn stable dynamics that mimics the demonstration data.

Different from those approaches, our method can learn both stable and safe dynamics from data. The second difference is that our approach can generalize to unseen goal point without retraining the model. Finally, our approach imposes explicit bounds on the diffeomorphism $g$, which can be seen as effective regularization preventing overfitting. Meanwhile, explicit bounds on tracking error and vector field magnitude can be obtained, which is useful for practical applications.

## Learning an All-Pairs Motion Planner

In this section, we aim to translate the above theoretical construction into a tractable machine learning setup, detailing the choice of training data, model class, and loss functions.

We parameterize the diffeomorphism $g$ by some smooth bi-Lipschitz neural network $g_{\theta}:\mathbb{R}^{n}\to\mathbb{R}^{n}$ with $\theta\in\mathbb{R}^{p}$ as the learnable parameter. By construction, system is smooth and globally equilibrium-independent experientially stable, as shown in Theorem 1. To ensure safety, one needs to learn a $g_{\theta}$ that can be used to characterize the set $\mathcal{X}_{\text{safe}}$. Since a candidate Lyapunov function $V(x,x_{\star})$ is used in the model construct, we seek to separate the safe and unsafe datasets in via a Lyapunov sublevel set of $V$. Specifically, we pick up a point $\hat{x}_{\star}\in\mathcal{D}_{\text{safe}}$ as the goal and take $g_{\theta}(\hat{x}_{\star})=0$. Then, the Lyapunov function in can be written as whose sublevel sets are $\Omega_{\theta}^{c}=\{x:\tilde{V}_{\theta}(x)\leq c\}$ with $c>0$. Note that $\Omega_{\theta}^{c}$ is diffeomorphic to $\mathcal{B}^{n}$ for any $\theta\in\mathbb{R}^{p}$ and $c>0$. Now, the learning problem becomes: find a pair $(c,\theta)$ such that

### IV-A Training Data

To solve the above learning problem, we need to assign labels to the points from the datasets $\mathcal{D}_{\text{safe}}$ and $\mathcal{D}_{\text{unsafe}}$. An intuitive approach is to associate $x_{i}\in\mathcal{D}_{\text{safe}}$ and $x_{j}\in\mathcal{D}_{\text{unsafe}}$ with labels of 0 and 1, respectively. The learning problem in is formulated as a classification task, where $\tilde{V}_{\theta}(x)$ is the classifier. However, those labels do not provide informative geometric information in $\mathcal{D}_{\text{safe}}$ and $\mathcal{D}_{\text{unsafe}}$.

By leveraging the existing sampling-based motion planning algorithms (e.g. PRM or RRT), we can assign each point $x_{i}\in\mathcal{D}_{\text{safe}}$ with a label $c_{i}$ indicating the shortest path length from $x_{i}$ to the targe $\hat{x}_{\star}$. Specifically, we first construct a graph by connecting each $x_{i}$ to a set of its nearby neighbors in $\mathcal{D}_{\text{safe}}$. From this graph, we can define the cost-to-go function $d:\mathcal{D}_{\text{safe}}\to\mathbb{R}_{\geq 0}$ as the shortest path distance from sample $x\in\mathcal{D}_{\text{safe}}$ to the goal $\hat{x}_{\star}$, which is a proxy for the distance between $x_{i}$ and $\hat{x}_{\star}$. The function $d(x)$ naturally reflects the geometry of $\mathcal{X}_{\text{safe}}$: samples near the goal attain small values, while samples that are distant or geometrically separated from $\hat{x}_{\star}$ attain large values. Thus, $d(x)$ provides meaningful information for training $\tilde{V}_{\theta}(x)$. Then, we construct the training datasets as follows: where $\bar{c}$ is the maximum label value in $\bar{\mathcal{D}}_{\text{safe}}$, and $\delta>0$ is a hyperparameter which ensures that there exists $c\in[\bar{c},\bar{c}+\delta]$ satisfying.

### IV-B Model Class

In this work, we use the BiLipNet as the model class for $g_{\theta}$. BiLipNets can enforce certified bi-Lipschitz bounds $\mu$ and $\nu$ via a method derived from which are, to the authors knowledge, the tightest available. The bi-Lipschitz bounds are trainable parameters, and their ratio $\tfrac{\nu}{\mu}$ can be considered a tunable distortion parameter, describing how much the learnt representation of $\mathcal{X}_{\text{safe}}$ distorts from a unit ball, and therefore how much the learnt trajectories can deviate from straight lines -- notice that this also appears in the overshoot constant for our exponential convergence bound. The lower bound $\mu$ also appears in our bound on velocity.

BiLipNets have a number of other advantages: firstly, BiLipNets admits a direct model parameterization, which allows training within the standard unconstrained optimization methods such as stochastic gradient descent. Secondly, the feedthrough layer architecture can improve the model expressivity without suffering from vanishing gradients. Thirdly, BiLipNets have a structure that admits fast splitting-based solvers for computing the model inverse.

### IV-C Loss Function

The loss function will generally include two components. The first component trains the diffeomorphism to map the safe set $\mathcal{X}_{\text{safe}}$ onto the unit ball. However, this leaves substantial flexibility for the shape of the mapping inside $\mathcal{X}_{\text{safe}}$, so a second task-specific loss term can be employed which may take many forms, e.g. training the dynamics to mimic demonstration trajectories.

For the first task, i.e., achieving, we choose the following loss function The term $\mathcal{L}_{\text{safe}}$ penalizes the samples from $\bar{\mathcal{D}}_{\text{safe}}$ for which $\tilde{V}_{\theta}(x_{i})>c_{i}$ is required to ensure (33a), while $\mathcal{L}_{\text{unsafe}}$ penalizes the samples from $\bar{\mathcal{D}}_{\text{unsafe}}$ for which $\tilde{V}_{\theta}(x_{j})<\bar{c}$ to ensure (33b).

The loss function for the second task may take various forms. E.g., when the demonstration dataset is available, we can define where $f_{\theta}$ is the vector filed in with $g_{\theta}$. The total loss is taken as $\mathcal{L}_{t}=\mathcal{L}+\rho\mathcal{L}_{\text{task}}$ with weighting $\rho>0$.

## Numerical Experiments

We illustrate the proposed approach on a 2D corridor navigation task (see Fig. 3), where we aim to generate safe and smooth trajectories from any initial configuration $x_{0}\in\mathcal{X}_{\text{safe}}$ to any goal $x_{\star}\in\mathcal{X}_{\text{safe}}$ in the presence of geometric obstacles. All experiments are implemented in Python using JAX and executed on an NVIDIA RTX 4090 GPU. Code is available at

### V-A Data Generation and Training details

As shown in Fig. 3 (left), we initialized RRT at a fixed goal $\hat{x}_{\star}$ to generate a shortest-path tree over $\mathcal{X}_{\text{safe}}$. This automatically provides the dataset pair $(x_{i},d(x_{i}))$ where $d(x_{i})$ is the cost-to-go with $x_{i}\in\mathcal{X}_{\text{safe}}$, see Fig. 3 (right). We take 2,500 samples to formulate the dataset $\bar{\mathcal{D}}_{\text{safe}}$ in (34a). Another 2,500 samples are uniformly sampled in $\mathcal{X}_{\text{unsafe}}$, which forms $\bar{\mathcal{D}}_{\text{unsafe}}$ in (34b).

Figure 3: RRT data (gray) in the corridor environment. (Left) RRT rooted at x̂⋆, with a representative trajectory (blue) in 𝒳. (Right) Corresponding cost-to-go field d(⋅) visualized via contour lines over 𝒳safe.

We use BiLipNet from to parameterize the bi-Lipschitz diffeomorphism $g_{\theta}$. The network is trained based on the loss function in via the Adam optimizer with a batch size of 16 for 1500 epochs.

### V-B Results and Discussions

Fig. 1 shows the learned mapping $g$ that transforms $\mathcal{X}_{\text{safe}}^{\prime}\subset\mathcal{X}_{\text{safe}}$ in the $\mathcal{X}$-space (Left) to a unit ball $\mathcal{B}^{2}$ in the $\mathcal{Z}$-space (Right). $\partial\mathcal{X}_{\text{safe}}^{\prime}$ and $\partial\mathcal{B}^{2}$ are indicated by red curves while $\partial\mathcal{X}_{\text{safe}}$ is in black. $\partial\mathcal{X}_{\text{safe}}^{\prime}$ conforms to the geometry of the obstacle boundaries, which is neither convex nor star-convex.

Fig. 4 shows that complex trajectories of the natural gradient flow system (left) are equivariant to linear trajectories of system (right) under the coordination change. Pulling back straight lines in $\mathcal{Z}$-space (Fig. 4 right) through $g_{\theta}^{-1}$ yields safe trajectories in $\mathcal{X}_{\text{safe}}$ (Fig. 4 left) that respect the obstacle geometry. All trajectories in Fig. 4 (left) also converge to $\hat{x}_{\star}$.

Figure 4: Trajectories generated by system from multiple initial configurations to the goal x̂⋆ in the training dataset. (Left) Smooth, safe paths in the 𝒳-space. (Right) Those paths are transformed into straight-line trajectories in the 𝒵-space, demonstrating the geometric simplification induced by gθ.

Fig. 5 illustrates that multiple trajectories converge to a distinct, previously unseen goal $x_{\star}$ (red cross). This indicates system is equilibrium-independent stable and safe. Note that the model was trained using data corresponding to a single goal, but it generalizes gracefully to a goal in a completely different location.

Figure 5: Generalization to previously unseen goal x⋆ without retraining. (Left) Smooth, safe paths in the 𝒳-space converging to a new goal x⋆ (red cross) from multiple initial configurations. (Right) In the 𝒵-space, the paths are transformed into straight-line trajectories within the unit ball.

## Conclusion

In this paper, we presented a learning-based approach for safe, stable, and smooth all-pairs motion planning. Our approach uses a bi-Lipschitz diffeomorphism to transform a geometrically complex safe set into the unit ball, and complex motions within this set into simple linear stable dynamics which corresponds to a goal-conditioned natural gradient in the original state space. This approach guarantees that both safety and exponential stability are preserved regardless of the goal location within the safe set. Empirical results in 2D corridor navigation task illustrate the the proposed approach.
