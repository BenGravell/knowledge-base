<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Apprenticeship Learning Using Inverse Reinforcement Learning and Gradient Methods

Topics include Inverse reinforcement learning, Apprenticeship learning, Natural gradients, Subgradient methods, Markov decision process, Reward learning, Policy matching.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Frames apprenticeship learning as a nonsmooth optimization problem over reward parameters and uses subgradients plus natural gradients to deal with policy non-smoothness and reward redundancy. The contribution is a more direct gradient-based IRL procedure that can match expert behavior reliably without repeatedly solving the max-margin style formulations common in earlier approaches.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we propose a novel gradient algorithm to learn a policy from an expert's observed behavior assuming that the expert behaves optimally with respect to some unknown reward function of a Markovian Decision Problem. The algorithm's aim is to find a reward function such that the resulting optimal policy matches well the expert's observed behavior. The main difficulty is that the mapping from the parameters to policies is both nonsmooth and highly redundant. Resorting to subdifferentials solves the first difficulty, while the second one is overcome by computing natural gradients. We tested the proposed method in two artificial domains and found it to be more reliable and efficient than some previous methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The aim of apprenticeship learning is to estimate a policy of an expert based on samples of the expert's behavior. This problem has been studied in the field of robotics for a long time and due to the lack of space we cannot give an overview of the literature. The interested reader might find a short overview in the paper by Abbeel and Ng.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In apprenticeship learning (a.k.a. imitation learning) one can distinguish between direct and indirect approaches. Direct methods attempt to learn the policy (as a mapping from states, or features describing states to actions) by resorting to a supervised learning method. They do this by optimizing some loss function that measures the deviation between the expert's ∗ Computer and Automation Research Institute of the Hungarian Academy of Sciences, Kende u. 13-17, Budapest 1111, Hungary

<!-- chunk {"id": "body-0006", "role": "body", "section": "Csaba Szepesv´ ari ∗", "weight": 1.0} -->

Department of Computing Science University of Alberta Edmonton T6G 2E8, AB, Canada policy and the policy chosen. The main problem then is that in parts of the state space that the expert tends to avoid the samples are sparse and hence these methods may have difficulties with learning a good policy at such places.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Csaba Szepesv´ ari ∗", "weight": 1.0} -->

In an indirect method it is assumed that the expert is acting optimally in the environment. In particular, in inverse reinforcement learning the environment is modelled as a Markovian decision problem (MDP). The dynamics of the environment is assumed to be known (or it could be learnt from samples which might even be unrelated to the samples come from the expert). However, the reward function that the expert is using is unknown. Recently Abbeel and Ng gave an algorithm which was proven to produce a policy which performs almost as well as the expert, even though it is not guaranteed to recover the expert's reward function (recovering the reward function is an ill-posed problem). This approach might work with less data since it makes use of the knowledge of model of the environment, which can help it in generalizing to the less frequently visited parts of the state space. One problem is that the algorithm of Abbeel and Ng relies on the precise knowledge of the features describing the reward function, which is not a realistic assumption (for a discussion of this, see Section 6). In particular, we will show that even the correct scales of the features have to be known.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Csaba Szepesv´ ari ∗", "weight": 1.0} -->

In this paper we propose a gradient algorithm that combines the two approaches by minimizing a loss function that penalizes deviations from the expert's policy like in supervised learning, but the policy is obtained by tuning a reward function and solving the resulting MDP, instead of finding the parameters of a policy. We will demonstrate that this combination can unify the advantages of the two approaches in that it can be both sample efficient and work even when the features are just vaguely known.

<!-- chunk {"id": "body-0009", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

Assume that we observe a sequence of state-action pairs (X t, A t) 0 ≤ t ≤ T, the 'trace' of some expert. We assume that the expert selects the actions by some unknown policy π E: A t ∼ π E (·| X t). The goal is to recover π E from the observed trace. The simplest solution is of course to use a supervised learning approach: we select a parametric class of policies, (π θ) θ, π θ ∈ Π, θ ∈ R d, and try to tune the parameters so as to minimize some loss J T (π θ), such as where ˆ µ T (x) could be defined by ˆ µ T (x) = 1 / (T + 1) ∑ T t =0 I { X t = x } are the empirical occupation frequencies under the expert's policy and ˆ π E,T (a | x) = ∑ T t =0 I { X t = x,A t = a } / ∑ T t =0 I { X t = x } is the empirical estimate of the expert's policy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

2 It is easy to see that J T approximates the squared loss uniformly in π (the usual concentration results hold for J T, e.g. Gy¨ orfi et al.).

<!-- chunk {"id": "body-0011", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

The reason ˆ π E,T is not used directly as a 'solution' is that if the state space is large then it will be undefined for a large number of states (where ˆ µ E,T ( x ) = 0) with high probability unless the number of samples is enormous.

<!-- chunk {"id": "body-0012", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

An alternative to direct policy learning is inverse reinforcement learning. The idea is that given the expert's trace, we find a reward function that can be used to explain the performance of the expert. More precisely, the problem is to find a reward function that the behavior of the expert is optimal. Once the reward function is found, existing algorithms are used to find a behavior that is optimal with respect to it.

<!-- chunk {"id": "body-0013", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

2 If a state is not visited by the expert, the policy is defined arbitrarily.

<!-- chunk {"id": "body-0014", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

One difficulty in IRL is that solutions are non-unique: e.g. if r is a reward function that recovers the expert's policy then for any λ ≥ 0, λr is also a solution ( r = 0 is always a solution). For non-trivial problems there are many solutions besides the variants that differ in their scale only.

<!-- chunk {"id": "body-0015", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

We propose here to unify the advantages of the direct and indirect approaches by (i) taking it seriously that we would like to recover the expert's policy and (ii) achieve this through IRL so that we can achieve good generalization at parts of the state space avoided by the expert. We thus propose to find the parameters given a parametric family of rewards (r θ) θ ∈ Θ such that the corresponding (near) optimal policy, π θ, matches the expert's policy π E (more precisely, it's empirical estimate). The proposed method can be written succinctly as the optimization problem where J is a loss function (such as or) aimed at measuring the distance of π E and its argument, Q ∗ θ is the optimal action-value function corresponding to the reward function r θ and G is a suitable smooth mapping that returns (near) greedy policies with respect to its argument. One possibility, utilized in our experiments, is to use Boltzmann action-selection policies (see). 3 In this paper we consider gradient methods to solve the above optimization problem. One difficulty with such an approach is that there could be many parameterizations that yield to the same loss.

<!-- chunk {"id": "body-0016", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

This will be helped with the method of natural gradients, for which the theory is worked out in the next section.

<!-- chunk {"id": "body-0017", "role": "body", "section": "APPRENTICESHIP LEARNING", "weight": 1.0} -->

Another difficulty is that the mapping θ ↦→ Q ∗ θ is nondifferentiable.We will, however, show that it is Lipschitz when r θ is Lipschitz and hence, by Rademacher's theorem it is differentiable almost everywhere (w.r.t. the Lebesgue measure).

<!-- chunk {"id": "body-0018", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

Our ultimate goal is to find some parameters θ in a parameter space Θ ⊂ R d such that the policy π θ determined by θ matches the expert's policy π E. For facilitating the discussion let us denote the map from the parameter space Θ to the policy space by h (i.e., h ( θ ) = π θ ). Thus, our objective function can be written as ˜ J ( θ ) = J ( h ( θ )), where J: Π → R is a (differentiable) objective function defined over Π (such as ) and the goal is to minimize ˜ J. Incremental gradient methods implement θ t +1 = θ t -α t g t, where α t ≥ 0 is an appropriate step-size sequence and g t = g ( θ ) points in the direction of steepest ascent on the surface ( θ, ˜ J ( θ )) θ.

<!-- chunk {"id": "body-0019", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

3 The benefit of choosing strictly stochastic policies is that if the expert's policy is deterministic, they force the uniqueness of the solution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

The gradient method with an infinitesimal step-size gives rise to a trajectory ( θ ( t )) t ≥ 0. This in turn determines a trajectory ( π ( t )) t ≥ 0 in the policy space, where π ( t ) = h ( θ ( t )). Since our primary interest is the trajectory in the policy state, it makes sense to determine the gradient direction g in each step such that π ( t ) moves in the steepest descent direction on the surface of ( π, J ( π )) π. We call g = g ( θ ) the natural gradient if this holds. Amari gives a method to find the natural gradients using the formalism of Riemannian spaces.

<!-- chunk {"id": "body-0021", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

The advantage of this procedure is that the resulting trajectories will be the same for any equivalent parameterization (i.e., if the parameter space is replaced by some other space that is related to the first one through a smooth invertible mapping, with a smooth inverse). In addition, the gradient algorithm that uses natural gradients can be proven to be asymptotically efficient in a probabilistic sense and has the tendency to alleviate the problem of 'plateaus'.

<!-- chunk {"id": "body-0022", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

In order to define natural gradients we need some definitions. First, we need the generalization of derivatives for mappings f between Banach spaces. 4 The underlying idea is that the gradient (derivative) of f: U → V provides a linear approximation to the change f (u + h) -f (u): Definition 1 (Fr´ echet derivative). Let U, V be Banach spaces. A is the Fr´ echet-derivative of f at u if A: U → V is a bounded linear operator and ‖ f (u + h) -f (u) -Ah ‖ V = o (‖ h ‖ U). The mapping f then is called Fr´ echet differentiable at u.

<!-- chunk {"id": "body-0023", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

In what follows we view Π both as a vector space and a complete metric space with some metric d. In our application this metirc will be derived from the (unweighted) ℓ 2 -norm, but other choices would also work. The following definition suggests a geometry induced on Θ: Definition 2 (Induced metric). Let Θ ⊂ R d, θ ∈ Θ ◦. We say that G θ ∈ R d × d is a pseudo-metric induced by 4 A Banach space is a complete normed vector space. In our case it will usually be a Euclidean space, e.g. R d.

<!-- chunk {"id": "body-0024", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

(h, Π, d) at θ if G θ is positive semidefinite and The essence of this definition is that if the 'distance' between θ and θ + ∆ is given by ∆ T G θ ∆ then this distance will match the distance of h (θ) and h (θ +∆), as ‖ ∆ ‖ → 0. It follows from the definition that the induced pseudo-metric is unique.

<!-- chunk {"id": "body-0025", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

In the rest of the paper we assume that Π is finite dimensional to make the presentation of the results easier. The following proposition is an immediate consequence of the definition of induced pseudo-metrics and the definition of Fr´ echet differentiability: Proposition 1. Assume that h: Θ → Π is Fr´ echet differentiable at θ ∈ Θ ◦, Θ ⊂ R d, Π = (Π, d) is a complete, linear metric space. Then h ′ (θ) T h ′ (θ) is the pseudo-metric induced by (h, Π, d) at θ.

<!-- chunk {"id": "body-0026", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

Natural gradients can be obtained by the following procedure: Let g (θ; ε) = argmax ∆ ∈ ˜ S (θ,ε) ˜ J (θ + ∆) -˜ J (θ) be the direction of steepest ascent over the 'warped sphere' ˜ S (θ, ε) = { ∆ ∈ R d | ‖ h (θ +∆) -h (θ) ‖ = ε }. 5 Then the set of natural gradients is given by Here the limes inferior of the sets (g (θ; ε)) ε> 0 is meant in the sense of the Painlev´ e-Kuratowski convergence: It then holds that no matter how ε converges to zero, g ∈ ˜ ∇ (h) ˜ J (θ) defines a direction of steepest ascent on the surface of J at h (θ).

<!-- chunk {"id": "body-0027", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

The following theorem holds: Theorem 1. Let J: Π → R, h: Θ → Π, ˜ J = J ◦ h. Assume that J is Fr´ echet differentiable and locally Lipschitz and h: Θ → Π is Fr´ echet differentiable at θ ∈ Θ ◦. Let G θ = h ′ (θ) T h ′ (θ) be the pseudo-metric at θ induced by (h, Π, d). Then G † θ ∇ ˜ J (θ) ∈ ˜ ∇ (h) ˜ J (θ), where ∇ ˜ J (θ) is the ordinary gradient of ˜ J at θ and G † θ denotes the Moore-Penrose generalized inverse of G θ.

<!-- chunk {"id": "body-0028", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

For the sake of specificity, when it does not cause confusion, we call G † θ ∇ ˜ J ( θ ) the natural gradient of ˜ J at θ. Note that from the construction it follows immediately that the trajectories of ˙ θ = G † θ ∇ ˜ J ( θ ) are covariant for any initial condition.

<!-- chunk {"id": "body-0029", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

The proof borrows some ideas from the proof of Theorem 1. In order to spare some space we only give an outline here: The basic idea is to replace the warped sphere ˜ S (θ, ε) by the 'sphere' 5 Note that g (θ; ε) is set-valued.

<!-- chunk {"id": "body-0030", "role": "body", "section": "NATURAL GRADIENTS", "weight": 1.0} -->

S G θ ( θ, ε ) = { ∆ ∈ R d | ∆ T G θ ∆ = ε 2 }. This is justified since the 'sphere' S G θ ( θ, ε ) becomes arbitrarily close to ˜ S ( θ, ε ) as ε → 0 and ˜ J is sufficiently regular. The next step is to show that for some C > 0, CεG † θ ∇ ˜ J ( θ ) is a solution of the optimization problem argmax ∆ ∈ S G θ ( θ,ε ) ˜ J ′ ( θ )∆, and this solution tracks closely that of argmax ∆ ∈ S Gθ ( θ,ε ) ˜ J ( θ +∆) -˜ J ( θ ) when ε → 0.

<!-- chunk {"id": "body-0031", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

In order to calculate the natural gradient we need to calculate the (Fr´ echet) derivative of h (θ) = G (Q ∗ θ) and the gradient of J (h (θ)). 6 By the chain rule we obtain ∇ J (h (θ)) = J ′ (h (θ)) h ′ (θ). Since calculating the derivative of J (or J T) is trivial, we are left with calculating the derivative of h (θ). As suggested previously, we use a smooth mapping G. One specific proposal, that we actually used in the experiments assigns Boltzmann policies to the action-value functions: where β > 0 is a parameter that controls how close G (Q) is to a greedy action selection. With this choice Hence, we are left with calculating ∂Q ∗ θ (x, a) /∂θ k. We will show that these derivatives can be calculated almost everywhere on Θ by solving some fixed-point equations similar to the Bellman-optimality equations. For this, we will need the concept of subdifferentials and some basic facts: Definition 3 (Fr´ echet Subdifferentials).

<!-- chunk {"id": "body-0032", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

Let U be a Banach space, U ∗ be its topological dual. 7 The Fr´ echet subdifferential of f: U → R at u ∈ U, denoted by ∂ -f (u) is the set of u ∗ ∈ U ∗ such that The following elementary properties follow immediately from the definition: Proposition 2. Let (f i) i ∈ I be a family of real-valued functions defined over U and let f (u) = max i ∈ I f i (u).

<!-- chunk {"id": "body-0033", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

6 Remember that G maps action-value functions to policies and J measures deviations to the expert's policy.

<!-- chunk {"id": "body-0034", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

7 When U = R d with the ℓ 2 -norm then U ∗ = R d and for u ∈ U, v ∗ ∈ U ∗, 〈 v ∗, v 〉 is the normal inner product.

<!-- chunk {"id": "body-0035", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

The next result states some conditions under which, in a generalized sense, 'taking a derivative and a limit is interchangeable'. It is extracted from the proof of Proposition 3.4 of Penot: Proposition 3. Assume that (f n) n is a sequence of real-valued functions over U which converge to some function f pointwise. Let u ∈ U, u ∗ n ∈ ∂ -f n (u) and assume that (u ∗ n) is weak ∗ -convergent to u ∗ and is bounded. Further, assume that the following holds at u: For any ε > 0, there exists some index N > 0 and a real number δ > 0 such that for any n ≥ N, h ∈ B U (0, δ), Now, we state the main result of this section: Proposition 4. Assume that the reward function r θ is differentiable w.r.t. θ with uniformly bounded derivatives: sup (θ,x,a) ∈ R d ×X×A ‖ r ′ θ (x, a) ‖ < + ∞.

<!-- chunk {"id": "body-0036", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

- Q ∗ θ is uniformly Lipschitz-continuous as a function of θ in the sense that for any (x, a) pair, θ, θ ′ ∈ R d, | Q ∗ θ (x, a) -Q ∗ θ ′ (x, a) | ≤ L ′ ‖ θ -θ ′ ‖ with some L ′ > 0; - Except on a set of measure zero, the gradient, ∇ θ Q ∗ θ, is given by the solution of the following fixed-point equation: where π is any policy that is greedy with respect to Q θ.

<!-- chunk {"id": "body-0037", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

Note that (r ′ θ (x, a)) T ∈ R d. In fact, the above equation can be solved componentwise: The k th component of the derivative can be obtained computing the actionvalue function for the policy π using r ′ θ,k in place of the reward function. 8 Proof. Let T: R X×A → R X×A be the Bellman operator 8 Here r ′ θ,k is the k th component of the derivative of the reward function with respect to θ. We also note in passing that if r θ is convex in θ then so is Q θ. This follows with the reasoning followed in the proof of the first part.

<!-- chunk {"id": "body-0038", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

By elementary arguments, if Q is L -Lipschitz in θ, then TQ is R + γL -Lipschitz in θ, where R is such that for any θ, θ ′ ∈ R d, ( x, a ) ∈ X × A, | r θ ( x, a ) -r θ ′ ( x, a ) | ≤ R ‖ θ -θ ′ ‖. Choose Q 0 = 0. As is well known (e.g., Puterman ), Q n = T n Q 0 converges to Q ∗: Q ∗ θ = lim n →∞ T n Q 0. Hence, by the previous argument Q ∗ is R + γR + γ 2 R +... = R/ (1 -γ )-Lipschitz, proving the first part of the statement.

<!-- chunk {"id": "body-0039", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

For the second part, for a policy π, let us define the operator S π, acting over the space of functions φ: X × A → R d, by Let π denote a greedy policy w.r.t. Q ∗ θ and let π n be a sequence of policies that are greedy w.r.t. Q n and where ties are broken so that ∑ x ∈X,a ∈A | π (a | x) -π n (a | x) | is minimized. It follows that for n large enough, π n = π. Now, consider the sequence ϕ 0 = 0, ϕ n +1 = S π n ϕ n. Then for n large enough we have ϕ n +1 = S π ϕ n. By induction, ϕ n (x, a) ∈ ∂ -θ Q n (x, a) holds for any n ≥ 0. Indeed, this clearly holds for n = 0, while the general case follows by Proposition 2. Now, observe that S π acts separately on each of the d components of its argument and when it is restricted to any of these components, it is a contraction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "CALCULATING THE GRADIENT", "weight": 1.0} -->

Hence, ϕ n converges to the fixed point of S π, i.e., the solution of. By Proposition 3 the limit is a subdifferential of lim n →∞ Q n = Q ∗ θ (that the condition of this proposition is satisfied follows from the uniform convergence of ϕ n in θ, which follows since ‖ r ′ θ ‖ is uniformly bounded in both θ and (x, a)). Now, since by the first part Q ∗ θ is Lipschitz-continuous in θ, by Rademacher's theorem it is differentiable almost everywhere. It is well-known that if a function is differentiable then its subderivative coincides with its derivative (see e.g. Kruger). This finishes the proof of the statement. □

<!-- chunk {"id": "body-0041", "role": "body", "section": "COMPUTER EXPERIMENTS", "weight": 1.0} -->

The goal of the experiments was to assess the efficiency of the algorithm and to test its robustness. We were also interested in how it compares with the algorithm of Abbeel and Ng.

<!-- chunk {"id": "body-0042", "role": "body", "section": "COMPUTER EXPERIMENTS", "weight": 1.0} -->

We have implemented three versions of our algorithm: (i) gradient descent using plain gradients, (ii) gradient descent using natural gradients (iii) RPROP using plain gradients. 9 RPROP is a popular adaptive step-size selection algorithm that proved to be very competitive in a number of settings Riedmiller and Braun. We have implemented the variant described in Igel and H¨ usken. We also implemented the 'max margin' and the 'projection' algorithms described in Abbeel and Ng to be able to compare the different approaches. Results will be shown for 'max margin'. The projection algorithm is computationally more efficient, but we have found it less reliable and less data efficient.

<!-- chunk {"id": "body-0043", "role": "body", "section": "COMPUTER EXPERIMENTS", "weight": 1.0} -->

9 We tried a 'natural RPROP' variant as well (RPROP using natural gradients), but perhaps suprisingly, it give much poorer results than the other algorithms.

<!-- chunk {"id": "body-0044", "role": "body", "section": "COMPUTER EXPERIMENTS", "weight": 1.0} -->

We decided to use two test environments: The familiar grid world that has also been used by Abbeel and Ng and the sailing problem due Vanderbei. The reward function was linear in the unknown parameters.

<!-- chunk {"id": "body-0045", "role": "body", "section": "GRID WORLD", "weight": 1.0} -->

We have run the first series of experiments in grid worlds, where each state is a grid square and the four actions correspond to moves in the four compass directions with 70% success. We constructed the reward function as a linear combination of 5 features ( φ i: X → R, i = 1,..., 5), where the features were essentially randomly constructed. The optimal parameter vector θ ∗ consists of evenly distributed random values. In general we try to approximate the reward function with the use of the same set of features that has been used to construct it, but we also examine the situation of unprecisely known features. The size 10 of the grid worlds was set to 10 × 10. Value iteration was used for finding the optimal policy (or gradients) in all cases. Unless otherwise stated the data consists of 10 independent trajectories following the optimal policy, each having a length of 100 steps. The learning rate was hand-tuned (with a little effort) and the number of iterations is kept at 100 (usually, convergence happens much earlier). In all cases, the performance measure is the error function J E, defined by and we measure the performance of the optimal policy computed for the found reward function.

<!-- chunk {"id": "body-0046", "role": "body", "section": "GRID WORLD", "weight": 1.0} -->

For the 'max margin' algorithm we show the performance of the overall best policy found during the first 100 iterations, thus optimistically biasing these measurements.

<!-- chunk {"id": "body-0047", "role": "body", "section": "GRID WORLD", "weight": 1.0} -->

We examined the algorithms' behavior when (i) the number of the training samples was varied (Figure 1), (ii) the features were linearly transformed (Figure 2, Table 1, row 2), and when (iii) the features were perturbed (Table 1, row 3).

<!-- chunk {"id": "body-0048", "role": "body", "section": "GRID WORLD", "weight": 1.0} -->

We see from Figure 1 that for small sample sizes plain gradient is doing the best, while eventually natural gradient becomes the winner. Note that the scale on the y axis is logarithmic, so the differences between these algorithms is not big. 'Max margin' also catches up at the end, just like RPROP.

<!-- chunk {"id": "body-0049", "role": "body", "section": "GRID WORLD", "weight": 1.0} -->

10 Preliminary experiments confirm that our conclusions would not change significantly for other sizes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "GRID WORLD", "weight": 1.0} -->

In practice, it is not realistic to assume that a subspace containing the reward function is known. To test how the algorithms behave without this assumption we perturbed the features by adding uniform [ -max( φ i ) / 2, max( φ i ) / 2] random numbers to them. Results are shown in row 3 of Table 1. The results indicate the robustness of natural gradients and RPROP. Both plain gradients and 'max margin' suffer large losses under these adverse conditions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "SAILING", "weight": 1.0} -->

We also applied the algorithms to the problem of 'sailing' proposed by Vanderbei. In this problem the task is to navigate a boat from one point to another in the shortest possible time. Thus, this is a stochastic shortest path (SSP) problem. Formally, we have a grid of waypoints connected by legs, at each waypoint the sailor has to select one of these eight legs to move on to the next waypoint. The state space in this setting is constructed from the actual situation of the boat and the direction from where the wind is blowing at the specific moment. The eight actions of selecting the next waypoint have different costs depending on the direction of the wind: e.g. it costs more time to sail 45 degrees against the wind than to sail 45 degrees in the wind direction etc.. We assume that the wind changes follow a Markov process. The reward function is given using a linear combination of the six features of ( away,down,cross,up,into, delay ), as defined in Vanderbei (all defined as a map φ: X × A → R ).

<!-- chunk {"id": "body-0052", "role": "body", "section": "SAILING", "weight": 1.0} -->

The following weighting was used in the experiments: θ ∗ = ( -1, -2, -3, -4, -100000, -3) T.

<!-- chunk {"id": "body-0053", "role": "body", "section": "SAILING", "weight": 1.0} -->

| | Natural gradients | Natural gradients | RPROP | RPROP | Plain gradients | Plain gradients | Max margin | Max margin | Figure 2: Performance with linearly transformed features. The features were transformed by a (nonsingular) square matrix with uniform random elements. Each curve is an average of 25 runs with different scalings of the features, the 1/10 s.e. error bars are also plotted.

<!-- chunk {"id": "body-0054", "role": "body", "section": "SAILING", "weight": 1.0} -->

Results as a function of the number of episodes is shown in Figure 3 for natural gradients and the 'max margin' algorithm. In this case the number of iterations is set to 1000 and we again computed the optimal policy with the reward found by the algorithm. As a more tangible performance measure in this case, we show the number of states where the actions selected by the found policy differ from the ones selected by the policy followed by the expert. The results here are shown fro a small lake of size 4 × 4. 11 The conclusion is again that the gradient method outperforms the 'max margin' algorithm by a significant amount.

<!-- chunk {"id": "body-0055", "role": "body", "section": "SAILING", "weight": 1.0} -->

11 Our preliminary experiments show that the new algorithm performs reasonably for larger problems, too.

<!-- chunk {"id": "body-0056", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In the paper we have argued for the advantages of unifying the direct and indirect approaches to apprenticeship learning. The proposed procedure attempts to optimize a cost function, yet it chooses the policy based on a model and thus may overcome problems usually associated with method that directly try to match the expert's policy. Although our method has shown stable behaviour in our experiments, more work is needed to fully explore the limitations of the method. One significant barrier for applying the method (as well as other methods based on IRL) is that it needs to solve MDPs many times. This is problematic since solving an MDP is a challenging problem on its own. One idea is to turn to two time-scale algorithms that run two incremental procedures in parallel, exploiting that a small change to the parameters would likely cause small changes in the solutions; as confirmed by our theoretical results. There are many important direc- tions to continue this work: The present work assumed that states are observed. This could be replaced by the assumption that sufficiently rich features are observed, however, when this is not satisfied the method won't work. For large state-spaces one needs to use function approximation techniques to carry out the computations.

<!-- chunk {"id": "body-0057", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

It is an open question if the methods would generalize to such settings. Another important direction is to consider infinite MDPs. This presents some technical difficulties, but we expect that the methods could still be generalized to such settings. Yet another interesting direction is to replace the parametric framework with a non-parametric one.
