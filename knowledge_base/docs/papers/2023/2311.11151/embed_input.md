<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Hardness of Learning to Stabilize Linear Systems

Topics include Linear systems, Stabilization, Sample complexity, System identification, Robust control, Machine learning theory, Control theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Constructs linear-system classes where learning a stabilizing controller is statistically hard even when identification itself is not the bottleneck. The paper separates stabilization difficulty from estimation difficulty by tying the lower bound to co-stabilizability and robust-control structure.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inspired by the work of Tsiamis et al., in this paper we study the statistical hardness of learning to stabilize linear time-invariant systems. Hardness is measured by the number of samples required to achieve a learning task with a given probability. The work in shows that there exist system classes that are hard to learn to stabilize with the core reason being the hardness of identification. Here we present a class of systems that can be easy to identify, thanks to a non-degenerate noise process that excites all modes, but the sample complexity of stabilization still increases exponentially with the system dimension. We tie this result to the hardness of co-stabilizability for this class of systems using ideas from robust control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Learning-based control plays an increasingly important role in many application domains such as power systems, robotics, self-driving cars, where it might be hard to perfectly model the system and its environment. Many learning-based control algorithms assume the existence of an initial stabilizing controller in order to simplify their analysis. Such simplifying assumptions are prevalent both in model-based and model-free learning-based control algorithms. However, learning to stabilize is a fundamental problem in learning-based control, with several algorithms tackling this issue.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Understanding the fundamental limits or the corner cases of learning-to-stabilize algorithms can inform future algorithm design and is crucial for applications of these algorithms in safety-critical domains. Therefore, it is important to understand how the system properties affect the performance of the learning-to-stabilize algorithms. In particular, we are interested in the number of samples required to learn a stabilizing controller with a given probability as a performance measure. We say a class of systems is hard to learn to stabilize if this number grows exponentially with the system dimension, independent of the algorithm choice.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We focus on fully observed linear time-invariant systems and consider the task of learning a static stabilizing linear state-feedback controller from a single trajectory. In this setting, Tsiamis et al. show that when the process noise is degenerate, i.e. the noise covariance matrix being singular, there are some classes of systems that are hard to learn to stabilize, by transferring the hardness of learning-to-stabilize into the hardness of system identification. The system classes constructed in their work are based on a (marginally) stable hard-to-stabilize pair. In this work, we significantly extend the class of systems that are hard to learn to stabilize by considering systems that are, even though close in the parameter space and generate similar state-input trajectories, not co-stabilizable with the same controller. This is achieved by a novel analysis technique that uses Ackermann's formula to compute all stabilizing linear state-feedback gains analytically and characterize the minimal level of perturbations to the parameters that render co-stabilizability infeasible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Different from the prior work, our analysis allows us to consider system classes that may only include systems with eigenvalues strictly outside of the unit circle, for which stabilizability is arguably more critical.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Notation: We use lower case, lower case boldface, and upper case boldface letters to denote scalars, vectors, and matrices respectively. For a matrix $\mathbf{M} \in {\mathbb{R}}^{m \times n}$, $\mathbf{M}^{\top}$ denotes its transpose, $M^{(i,j)}$ denotes its element in the $i^{th}$ row and the $j^{th}$ column. For a square matrix $\mathbf{M} \in {\mathbb{R}}^{n \times n}$, $\mathbf{M} \succ 0$ ($\succeq 0$) denotes that $\mathbf{M}$ is positive definite (positive semidefinite), $\rho{(\mathbf{M})}$ denotes its spectral radius, and $\det{(\mathbf{M})}$ denotes its determinant.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

For a vector $\mathbf{v} \in {\mathbb{R}}^{n}$, its $i^{th}$ element is denoted by $v^{(i)}$. By ${poly}{( \cdot )}$ we denote a polynomial function of its arguments. By $\exp{( \cdot )}$ we denote an exponential function of its arguments. We use $\mathbf{I}_{n}$ to denote the identity matrix in ${\mathbb{R}}^{n \times n}$. A sequence of vectors $\mathbf{x}_{t}$, $\mathbf{x}_{t + 1}$,..., $\mathbf{x}_{t + N}$ is denoted by $\mathbf{x}_{t:{t + N}}$ for short. By convention, $\mathbf{x}_{i:j}$ is an empty set if $j < i$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup and Preliminary Notions", "weight": 1.0} -->

We consider the following fully-observed discrete-time linear time-invariant (LTI) system: where $\mathbf{x}_{t} \in {\mathbb{R}}^{n}$, $\mathbf{u}_{t} \in {\mathbb{R}}^{p}$, $\mathbf{w}_{t} \in {\mathbb{R}}^{n}$ are the state, input, and process noise at time $t$. For simplicity, we assume $\mathbf{x}_{0} = \mathbf{0}$. The random process $\mathbf{w}_{t}$ over $t$ is zero-mean i.i.d. Gaussian, with covariance matrix $\sigma_{w}^{2}\mathbf{I}_{n}$. In the remainder of the paper, we denote a system in the form by the tuple $(\mathbf{A},\mathbf{B})$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup and Preliminary Notions", "weight": 1.0} -->

Let $\mathcal{C}_{n}$ be a class of systems $(\mathbf{A},\mathbf{B})$ in dimension $n$, parameterized by some unknown parameters.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Next, we recall the definition of ${poly}{(n)}$-stabilizable system classes. If a class $\mathcal{C}_{n}$ of discrete-time LTI systems is ${poly}{(n)}$-stabilizable, it is statistically easy to learn linear state-feedback controllers to stabilize systems in this class.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Is there a class of linear systems that are not ${poly}{(n)}$-stabilizable when the process noise $\mathbf{w}_{t}$ is non-degenerate?

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1", "weight": 1.0} -->

The following lemma follows directly from Definition 2-stabilizable system classes ). ‣ II Problem Setup and Preliminary Notions ‣ On the Hardness of Learning to Stabilize Linear Systems").

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Co-stabilization problem for two dynamical systems has been studied in robust control, e.g., by using the gap metric.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We will use $KL$ divergence to measure the distance between the distributions of state-input trajectories generated when the same exploration policy is applied to two different systems. A small $KL$ divergence means that it is hard to distinguish two systems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Hard to Learn to Stabilize Systems", "weight": 1.0} -->

Consider the following system of the form with $(\mathbf{A},\mathbf{B})$ defined parametrically as where $n \geq 2$, $r > 1$, $0 < v < \frac{r - 1}{2}$, and $b^{} \geq 0$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 2", "weight": 1.0} -->

When $b^{} = {- {v^{n}/r^{n - 1}}}$, the system in is uncontrollable. To avoid this trivially hard-to-stabilize case, we let $b^{} \geq 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The following proposition proves that there exist two systems in the parametric family differing only in $b^{}$, such that for a feedback gain to be able to stabilize both systems at the same time, the difference in $b^{}$ should be exponentially small in the system dimension.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Our proof technique can also be extended to show the hardness of learning to stabilize for classes of systems containing single-input systems with diagonal state matrices and $n$ unstable eigenvalues in a compact range, presented. In that case, when the input vector is the all-one vector, the controllability matrix of the system is a Vandermonde matrix, which allows us to again use Ackermann's formula to obtain the explicit form of all stabilizing linear state-feedback gains. Results similar to Proposition 4 and Theorem 1 can be established in this case too.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we implement two numerical experiments, i.e., certainty equivalent linear quadratic regulator (LQR) and robust control, to show the hardness of stabilization.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Certainty Equivalent LQR", "weight": 1.0} -->

Since solving LQR problems always gives stabilizing controllers (under mild regularity conditions), the first experiment considers the certainty equivalent LQR control. Specifically, a controller is computed by solving an LQR problem using some estimated system dynamics and then applied to the ground truth system. The infinite-horizon LQR problem, simplified as $dLQR{(\mathbf{A},\mathbf{B},\mathbf{Q},\mathbf{R})}$, is as follows.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Certainty Equivalent LQR", "weight": 1.0} -->

For each dimension $n$, we run $M = 200$ independent experiments. Let ${\hat{\mathbf{K}}}_{i,N'}$ denote the controller obtained using the first $N'$ data points, i.e., $\{\mathbf{u}_{0:{N' - 1}},\mathbf{x}_{1:N'}\}$, in the $i^{th}$ experiment. We record the smallest trajectory length $N$ under which at least 90% of the experiments produce stabilizing controllers, i.e. where $\mathbb{I}$ denotes the indicator function.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Certainty Equivalent LQR", "weight": 1.0} -->

The results are given in Fig. 1. According to Fig. 1, we have that as the system dimension increases, the required number of samples for a given frequency of stability increases exponentially with the system dimension.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B LMI-based Sufficient Condition for Co-stabilizability", "weight": 1.0} -->

In this section, we numerically demonstrate the hardness of co-stabilizability of $\mathcal{S}_{1} = {(\mathbf{A},\mathbf{B}_{1})}$ and $\mathcal{S}_{2} = {(\mathbf{A},{\mathbf{B}_{2}{(m)}})}$ using ideas from robust control, where we leave $m$ as a parameter. We use the following feasibility problem, which can be converted to an LMI, to check sufficient conditions of co-stabilizability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B LMI-based Sufficient Condition for Co-stabilizability", "weight": 1.0} -->

We use the bisection method to find the largest $m$ such that the problem is feasible. The results are shown in Fig. 2. According to this figure, we see that as the system dimension increases, the largest $m$ such that the LMI optimization problem in is feasible decreases exponentially with increasing system dimension, which is consistent with Eq. in Proposition 4.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we identified an extended class of LTI systems that are hard to learn to stabilize with static state feedback. The main idea in constructing such examples is to find pairs of systems whose parameters become exponentially close to each other as the dimension increases, yet they are not co-stabilizable. One interesting observation is that the entries of stabilizing gains for these pairs are also growing exponentially (see, Eq. ). In the future, we want to investigate the ramifications of this observation in gradient-based learning algorithms used for control as.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

*Acknowledgments:* The authors would like to thank Prof. Peter Seiler of University of Michigan for some early discussions that motivated this work.
