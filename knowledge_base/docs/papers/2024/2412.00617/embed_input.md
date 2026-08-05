<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Flow Matching for Stochastic Linear Control Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper addresses the problem of steering an initial probability distribution to a target probability distribution through a deterministic or stochastic linear control system. Our proposed approach is inspired by the flow matching methodology, with the difference that we can only affect the flow through the given control channels. The motivation comes from applications such as robotic swarms and stochastic thermodynamics, where agents or particles can only be manipulated through control actions. The feedback control law that achieves the task is characterized as the conditional expectation of the control inputs for the stochastic bridges that respect the given control system dynamics. Explicit forms are derived for special cases, and a numerical procedure is presented to approximate the control law, illustrated with examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Flow matching has recently gained attention as a promising method for generative modeling due to its simplicity and flexibility. From a control-theoretic perspective, the methodology can be understood as follows. Consider the control system: where { X t ∈ R n; 0 ≤ t ≤ 1 } is the state, { u t ∈ R n; 0 ≤ t ≤ 1 } is the control input, and P initial is the distribution of the initial state X 0. The control objective is to find a control input u t such that the terminal state X 1 follows a desired target distribution P target. Flow matching offers a straightforward solution. First, a probability flow { P t; 0 ≤ t ≤ 1 } is constructed on the space of probability distributions. This flow is chosen to interpolate between the initial and target distributions, i.e. P 0 = P initial and P 1 = P target, and is easy to sample. A standard choice for P t is the probability law of the linear interpolation process X z t = (1 -t) x + ty where z = (x, y) ∼ Π:= P initial ⊗ P target.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Then, the control input u t is identified so that the probability of X t, and P t, both satisfy the same continuity equation. The resulting control input takes the form u t = k (t, X t) where the feedback control law k: × R n → R n has the probabilistic representation Through this procedure, the probability law of X t matches P t, for all t ∈, achieving the control objective X 1 ∼ P 1 = P target. A key computational advantage of flow matching is that the feedback control law k (t, ·) can be numerically approximated by solving a least-squares regression problem: The aim of this paper is to extend the flow matching methodology to the general control setting where the simple control system is replaced by a general deterministic or stochastic linear control system of the form or. The notable difference from traditional flow matching is that here, adjustments to the differential equation are limited to control inputs, a constraint arising from engineering applications such as robotic swarms or stochastic thermodynamic systems, where agents or particles can only be manipulated through control actions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of controlling probability distributions has a rich history in control theory, dating back to Roger Brockett's work on the control of Liouville equations. Interest in this area has expanded due to its connections with mean-field games, mean-field control, optimal transportation/Schr¨ odinger bridge problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Namely, our work is closely related to Chen et al. which derives the optimal feedback control law that steers a stochastic linear control system from an initial Gaussian distribution to a Gaussian target distribution in an optimal manner. The flow matching methodology presented here generalizes the framework to non-Gaussian distributions, though it no longer guarantees optimality. Our work is also closely related to Liu et al. where flow matching is used to solve the generalized schr¨ odinger bridge problem in an alternating optimization scheme. The difference in our setup is constraining the dynamics to linear control systems of the form or and forgoing optimality. While some notion of optimality could be introduced by designing an optimal coupling between the initial and target distributions (e.g., using the Sinkhorn algorithm for optimal sample pairing), this is not the focus of our work.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows. Section 2 presents interpolations over deterministic and stochastic linear control system. Section 3 presents the generalization of the flow matching methodology to stochastic linear control systems, followed by the analytical derivation of the control law for special cases of Gaussian and mixture of Gaussian target distribution. Finally, Section 4 presents a numerical procedure which is demonstrated with the aid of several examples.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Consider the linear control system where X t ∈ R n is the state and u t ∈ R m is the control input, at time t. We consider the following control problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Problem 1 Given a pair of points ( x, y ) ∈ R n × R n, find a trajectory { X t; t ∈ } such that X 0 = x, X 1 = y, and is satisfied for some control input { u t; t ∈ }.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

This is a standard problem in control theory, forming the basis for controllability analysis of linear systems, e.g. see. In order to solve this problem, it is useful to define the controllability Gramian and make the following assumption about the system.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Assumption 1 The pair ( A,B ) is controllable. That is to say, the matrix [ B,AB,A 2 B,..., A n -1 B ] is full-rank.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Under the controllability Assumption 1, it is known that the Gramian matrix Φ t is non-singular for all t > 0. The following proposition states a solution to Problem 1. The proof is standard and omitted on account of space.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Proposition 1 Problem 1 is solved with the control input resulting into the interpolating trajectory Moreover, is the control input with minimum L 2 -norm ∫ 1 0 ∥ u t ∥ 2 d t among all the control inputs that solve Problem 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Remark 2 It is useful to express the control input as a feedback control law u t = k (t, X t) where This is obtained by using to solve for x, in terms of X t and y, and substituting the result. The feedback control law steers the system from any given initial point to y. Surprisingly, the same feedback control law achieves this task in the stochastic setting.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Deterministic linear control system", "weight": 1.0} -->

Remark 3 The interpolation formula can be generalized to a linear time-varying system d X t d t = A t X t + B t u t by replacing e ( t -s ) A by the corresponding state transition matrix Ψ t,s where dΨ t,s d t = A t Ψ t,s, Ψ s,s = I, for all t ≥ s ≥ 0, and replacing B by its time-varying counterpart B t.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

Consider the stochastic linear control system: where { W t } t ≥ 0 is n -dimensional Brownian motion and ϵ ∈ R. Let F t:= σ (W s; 0 ≤ s ≤ t) denote the filtration generated by the Brownian motion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

Problem 2 For any pair z = ( x, y ) ∈ R n × R n, find a stochastic trajectory { X t; t ∈ } such that X 0 = x, X 1 = y, and is satisfied for some control input { u t; t ∈ } that is F t -adapted.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

Problem 2 can be solved by constructing stochastic bridges, that is to say, the uncontrolled process X t conditioned at its end-points, X 0 = x and X 1 = y. These stochastic bridges have been developed for general non-degenerate diffusions and for degenerate diffusion of the type in Chen and Georgiou, using a stochastic optimal control formulation of the problem 2. Here, we present an alternative approach using the time-reversal methodology and derive the formula for the feedback control law that solves problem 2. We present this approach for its simplicity and flexibility, while it should be noted that the results are the same as in Chen and Georgiou.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

Proposition 4 Problem 2 is solved with the feedback control law The marginal probability of the resulting trajectory is where Z is normal Gaussian, d = means equality in distribution, and Remark 5 The feedback control law that achieves the deterministic and stochastic interpolation is exactly the same: The expectation of the stochastic interpolation is exactly equal to the deterministic interpolation. Moreover, the deterministic interpolation can be derived from the stochastic interpolation in the limit as ϵ → 0.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

Proof The uncontrolled process X t, starting from X 0 = x, is Gaussian with mean and covariance matrix given: Therefore, conditioning on X 1 = y, X t remains Gaussian with the mean and covariance Figure 1: Interpolations for three linear control systems with modeling parameters specified. concluding the formula.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

In order to obtain the formula for the control input, consider the uncontrolled process ˜ X t satisfying The probability distribution of ˜ X t is Gaussian N (m t, Q t) with mean m t = e -At y and covariance matrix The time-reversal X t:= ˜ X 1 -t satisfies the SDE Note that, by construction, X 1 = ˜ X 0 = y. This is true starting from any initial point X 0 = x. Therefore the control law that achieves the stochastic interpolant is concluding the control law.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stochastic linear control system", "weight": 1.0} -->

Remark 6 Our results hold for the case where we replace ϵ with a matrix. However, we restrict the exposition to stochastic models where the Brownian motion enters the system from the same channels as the control input.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Flow matching for control systems", "weight": 1.0} -->

Our goal is to use the deterministic and stochastic interpolations constructed in Section 2 to find the feedback control law that steers a given initial distribution P 0 to a desired target distribution P 1 through a a deterministic or stochastic linear system. We present the construction for the stochastic case, since the construction for the deterministic case is identical.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Flow matching for control systems", "weight": 1.0} -->

Problem 3 Consider the stochastic linear system. For any pair of distributions ( P 0, P 1 ), find a F t -adapted control input u t so that if X 0 ∼ P 0, then X 1 ∼ P 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Flow matching for control systems", "weight": 1.0} -->

We solve the problem using the flow matching methodology. The first step is to construct a process, denoted by X z t, that has the desired end-point distributions, i.e. X z 0 ∼ P 0 and X z 1 ∼ P 1. The second step is to find the control input u t in so that the probability law of X t is equal to the probability law of X z t.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Flow matching for control systems", "weight": 1.0} -->

In order to achive the first step, let z = (x, y) ∈ R n × R n with the probability distribution Π. Assume the x -marginal and the y -marginal of Π are equal to P 0 and P 1, respectively (e.g. take Π = P 0 ⊗ P 1). For each z ∼ Π, let X z t be the stochastic interpolant with stochastic control input u z t given. Note that, by construction, This achieves the goal of the first step. The second step is presented in the following theorem.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Flow matching for control systems", "weight": 1.0} -->

Theorem 7 Problem 3 is solved with the feedback control law u t = ¯ k (t, X t) where Moreover, X t d = X z t for all t ∈, where d = means equality in distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Flow matching for control systems", "weight": 1.0} -->

Proof Consider a smooth and bounded test function f: R n → R. Let X t be the solution to with the feedback control law. Then, the Itˆ o rule implies On the other hand, taking the time-derivative of E [f (X z t)], while using the fact that, for a fixed z, X z t solves with control input u z t, implies where we used the tower property of conditional expectation in the second identity, and the definition of the control law in the third identity. The two derivations imply that the probability law of X t and X z t follow the same update law. Therefore, due the the equality of the initial distribution of X z 0 ∼ P 0 and X 0 ∼ P 0, the probability law of X t is equal to the probability law of X z t for all t ∈. In particular, probability distribution of X 1 is equal to P 1, the probability distribution of X z 1. This concludes the solution to Problem 3.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Control law for Gaussian and mixture of Gaussians target distribution", "weight": 1.0} -->

In this section, we present the analytical formula for the feedback control law for the special case where P 0 is a Gaussian and P 1 is a mixture of Gaussians. In particular, we assume where η l is N (m l, Q l), for l = 0,..., L, w l ≥ 0, and ∑ L l =1 w l = 1. The case L = 1 corresponds to a Gaussian target, while L > 1 corresponds to a mixture.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Control law for Gaussian and mixture of Gaussians target distribution", "weight": 1.0} -->

In order to achieve this, it is useful to express the feedback control law according to where the formula for u z t is used. Therefore, the problem of finding the feedback control law is reduced to finding the analytical formula for the conditional expectation E [y | X z t = ξ]. To simplify the presentation, we express the relationship according to Corollary 8 Consider Problem 3 where P 0 is a Gaussian and P 1 is a mixture of Gaussians, as described. Then, the feedback control law that solves the problem takes the form where Proof Consider the spacial case where L = 1. In this case, the Gaussian assumption x ∼ N (m 0, Q 0) and y ∼ N (m 1, Q 1), the relationship, and selecting the independent coupling Π = P 0 ⊗ P 1, imply concluding the formula for L = 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Control law for Gaussian and mixture of Gaussians target distribution", "weight": 1.0} -->

The extension to the mixture case L > 1 follows by computing the conditional expectation for each Gaussian member of the mixture, and forming their weighted linear combination, where the weights are appropriately adjusted according to the likelihood of that particular member. The derivation details are removed on account of space. Similar derivations are common in Gaussian sum filters. A similar form of the feedback control law also appears in Salhab et al. in the context of LQG games with multiple choice.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Extension to control affine systems", "weight": 1.0} -->

Consider the control affine stochastic system where a: R n → R n and b: R n → R n × m. Let X z t be the stochastic bridge for this system, with the corresponding control input u z t. Then, the control law can also be used for this system, to steer an initial distribution P 0 to a target distribution P 1. However, in such a general setting, the process of sampling from X z t becomes computationally challenging because an analytical expression for the stochastic bridge is not available.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Algorithm and numerical results", "weight": 1.0} -->

In general, the conditional expectation does not have an explicit solution. We follow the same procedure as in the flow matching methodology to numerically approximate the conditional expectation as the solution to the least-squares regression problem: where the expectation is approximated using N independent samples of the pair z i = (x i, y i) ∼ Π. In this expression, X z i t represents a sample from with the corresponding control input u z i t given. And F represents a parameterized function class. Across all numerical results, we select F to be the class of neural networks with a 3 block ResNet architecture where each block consists of 2 linear layers of width 32 and an exponential linear unit (ELU)-type activation function.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Algorithm and numerical results", "weight": 1.0} -->

The algorithm has two stages. In the training stage, we use the ADAM optimizer, with initial learning rate 10 -2 and exponential decay of order 0. 999, to solve the optimization problem and find the parameters of the neural net f. The number of iterations is 10 4, with the total sample size N = 2000, and the batch size 64. In the prediction stage, we use the Euler-Maruyama method, with ∆ t = 0. 001, to simulate N ′ = 2000 independent realizations of the SDE using the feedback control law learned in the training stage. The samples are denoted by { X i t } N ′ i =1. The code for reproducing the results is available online 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical results for 2d systems", "weight": 1.0} -->

The numerical results for three different 2-dimensional linear control systems, with model parameters -(a)-(b)-(c), are presented in Figure 2. In all these cases, the coefficient ϵ = 1. The first row shows the results for -(a) where the initial distribution is standard Gaussian and the target distribution is a mixture of two Gaussians. The left panel shows the trajectories { X i t; 0 ≤ t ≤ 1 } generated from the prediction stage. The initial states { X i 0 } N ′ i =1 are samples from the initial distribution and depicted by blue circles. The terminal states { X i 1 } N ′ i =1 are depicted with green circles and are expected to represent samples from the target distribution. For comparison, independent samples from target distribution are shown as red ' × ' markers. A kernel density approximation of the terminal states is compared with the exact target density in the second panel. The result demonstrates a qualitative proof that the proposed algorithm solves Problem 3 for this example.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical results for 2d systems", "weight": 1.0} -->

The right exact target density transported density panel shows a quantitative comparison between the empirical probability distributions of the generated trajectories { X i t } N ′ i =1 and training samples { X z i t } N i =1, using the maximum mean discrepancy (MMD) distance with Gaussian kernel and bandwidth 2. The MMD distance is normalized by the MMD distance between the initial and target distribution. The result highlights the conclusion of Theorem 7 that X t d = X z t for all t ∈.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical results for 2d systems", "weight": 1.0} -->

The second and third rows show the same results for modeling parameters -(b) and (c), respectively. In the second row, the initial distribution is standard Gaussian, while the terminal distribution is a mixture of four Gaussians. In the third row, the initial and target distributions are uniform distributions on circles of different radius. The results serve as a proof of concept that the proposed algorithm solves Problem 3 with a reasonable accuracy among different class of linear systems and probability distributions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical results for higher dimensional systems", "weight": 1.0} -->

We explore the scalability of the algorithm with the problem dimension by considering a massspring model with model parameters as. Figure 3 shows the results for 4 -dimensional and 8 -dimensional mass-spring systems. The target distribution is a mixture of four Gaussians. The left panel shows the approximated and exact densities projected onto the last two components. The panel at the center shows the normalized MMD distance between the empirical distribution of the generated samples and training samples. The right panel shows the Wasserstein-2 2 ( W 2 ) distance between the same samples. The results highlight the ability of the algorithm to scale with the problem dimension.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduced a novel framework for flow matching within the context of deterministic and stochastic linear control systems. By leveraging the structure of these systems, we developed an efficient methodology to steer an initial probability distribution to a desired target distribution while adhering to control constraints. The numerical experiments demonstrated the effectiveness and scalability of our approach across various system parameters and distribution classes. Future research could explore performance enhancements and extensions to control-affine systems or systems with state constraints, to further broaden the applicability of this methodology. 2. The W 2 is computed using the python optimal transport (POT) library with the squared Euclidean distance.
