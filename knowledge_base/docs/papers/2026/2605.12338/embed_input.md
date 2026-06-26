<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Manifold Sampling via Entropy Maximization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling from constrained distributions has a wide range of applications, including in Bayesian optimization and robotics. Prior work establishes convergence and feasibility guarantees for constrained sampling, but assumes that the feasible set is connected. However, in practice, the feasible set often decomposes into multiple disconnected components, which makes efficient sampling under constraints challenging. In this paper, we propose MAnifold Sampling via Entropy Maximization (MASEM) for sampling on a manifold with an unknown number of disconnected components, implicitly defined by smooth equality and inequality constraints. The presented method uses a resampling scheme to maximize the entropy of the empirical distribution based on k-nearest neighbor density estimation. We show that, in the mean field, MASEM decreases the KL-divergence between the empirical distribution and the maximum-entropy target exponentially in the number of resampling steps. We instantiate MASEM with multiple local samplers and demonstrate its versatility and efficiency on synthetic and robotics-based benchmarks. MASEM enables fast and scalable mixing across a range of constrained sampling problems, improving over alternatives by an order of magnitude in Sinkhorn distance with competitive runtime.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling from constrained distributions is a fundamental problem in machine learning, with applications including Bayesian inference and molecular design as well as robotics and trajectory optimization. In particular, many tasks in robotics require sampling kinematically feasible states or trajectories, for instance, to generate data for behavior cloning or to sample reset states for reinforcement learning. The feasible set is usually given implicitly by constraint functions, which can only be evaluated point-wise. This makes sampling from it a challenging problem, as we have no prior knowledge about many of its properties, like the number of connected components.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

When no constraints are present, the dominant sampling paradigm is built around Markov Chain Monte Carlo (MCMC) methods such as Metropolis-Hastings, Langevin dynamics, and Hamiltonian Monte Carlo. To handle constraints, these approaches are typically combined with projections or landing mechanisms that ensure samples remain feasible. However, all such methods rely on local MCMC kernels, which limits them to moves within a single connected region of the feasible set, and as a result they struggle with infeasibility barriers. As a result, even if such kernels mix well locally, they cannot determine how much probability mass to assign to each component (as illustrated in Figure 1). This makes them ill-suited in many practical scenarios, where such disconnected feasible sets arise naturally.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We tackle this problem by maximizing sample entropy across the feasible set. This provides empirical coverage of the feasible set, as the samples are distributed approximately uniformly. It enables estimation of component volumes and may serve as unbiased initialization for sampling from arbitrary distributions across components. The key idea is to combine local k -nearest-neighbor density estimates with Sequential Monte Carlo (SMC)-inspired resampling: particles in underrepresented components receive higher importance weights, encouraging redistribution of mass toward a uniform allocation. Crucially, the resampling step is modular and can be composed with generic constrained MCMCsamplers. Adding this method to a constrained sampler is minimally invasive in the sense that it only incurs a small runtime overhead and does not degrade performance on compact and connected manifolds. Our main contributions are as follows: ∗ Equal contribution; Authors in alphabetical order.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We introduce Ma nifold S ampling via E ntropy M aximization (MASEM), an algorithm for uniform sampling on manifolds with disconnected components. - We show that, under mild assumptions, the induced resampling operator contracts the KLdivergence to the uniform distribution at a geometric rate of (1 -τ/p) per iteration, where τ is a temperature parameter and p is the intrinsic dimension of the manifold. - We validate the approach empirically on synthetic and robotics benchmarks and compare performance across different local samplers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Manifold Sampling via Entropy Maximization", "weight": 1.0} -->

We now introduce Manifold Sampling via Entropy Maximization (MASEM), a framework for uniform sampling on a constrained set Σ as defined in Section 3. Our goal is to construct a particle system whose empirical distribution approximates the uniform density u Σ on Σ. Given an existing strong local sampler that preserves feasibility, the main challenge for constrained uniform sampling is global mass allocation. As Σ is only defined implicitly via constraints, this is a hard problem, since the measures of components or even their number are not known a priori, so local samplers cannot calibrate probability mass across disconnected components efficiently. Thus, MASEM introduces a mechanism that redistributes particles across components to ensure that each component receives mass proportional to its measure.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Manifold Sampling via Entropy Maximization", "weight": 1.0} -->

The design of MASEM is intentionally lightweight. Its key mechanism is an importance-resampling step that moves particles towards the maximum entropy target. This target is the uniform density p = u Σ (Lemma 1). Let q denote the current particle density on Σ. Since the target density is uniform, importance-resampling with weights w i ∝ p (x i) /q (x i) reduces to resampling according to w i ∝ q (x) -1. While the current density itself is unknown, we can estimate it using the k -nearest neighbor estimator. This leads to q (x i) ∝ ε -p i,k in probability in the large particle limit, where ε i,k denotes the distance of sample x i to its k th neighbor. Replacing the potentially unknown dimension p by a temperature parameter τ yields Algorithm 1 Entropy-based uniform sampling on disconnected manifolds Input: Initialization scale σ 2, number of samples N, number of iterations T, neighborhood parameter k, temperature τ, rejuvenation kernel K, rejuvenation step number M, constraint functions h, g.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Manifold Sampling via Entropy Maximization", "weight": 1.0} -->

- 3: Project the particles onto Σ (e.g., with Gauss-Newton method) - 4: Apply a manifold-constrained rejuvenation kernel K - 5: // Iterative entropy maximization - 7: Compute weights w i t from the entropy-based rule in - 8: Resample particles according to the normalized weights w i t - 9: Apply a manifold-constrained rejuvenation kernel K for M steps - 11: return fi nal particle set X (T) Thus, particles in low-density regions have larger k -NN radii and receive larger resampling weights, encouraging redistribution toward underrepresented connected components. The temperature τ controls the aggressiveness of the resampling step. When τ is small, the update is conservative and moves mass more slowly. Larger values of τ accelerate mass redistribution but can amplify errors in the k -NN density estimate when the number of particles or mixing steps is insufficient.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Manifold Sampling via Entropy Maximization", "weight": 1.0} -->

MASEM, described in pseudocode in Algorithm 1, works by first initializing feasible particles and then iterating resampling followed by manifold sampling rejuvenation. We initialize the particles by random i.i.d. sampling followed by projection onto the feasible set using Gauss-Newton steps on the squared slack to ensure approximate constraint feasibility. After initialization, we apply a feasibility-preserving kernel K for rejuvenation. This ensures that the particles are approximately uniformly distributed within components. Then, at each iteration, particles are resampled using the entropy-based resampling weights. After resampling, we apply K again to obtain mixed samples within each component. As local kernels are only approximately feasible in practice, we use a slack-penalized variant of the resampling weights to avoid over-replicating particles with large constraint violations in our experiments. These practical modifications are described in Appendix D.5.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Our theoretical guarantees address the global mass-redistribution problem, which cannot be solved by existing local samplers. We analyze Algorithm 1 in the mean-field regime, where the N →∞ limit reduces the particle system to a deterministic evolution on the simplex of component weights. This parallels the idealized-limit viewpoint taken in related work on particle-based constrained sampling. Our main result (Theorem 1) shows that a single resampling step contracts the KL divergence to the uniform distribution on Σ contracts at rate (1 -τ/p ), leading to exponential convergence. All proofs for this section can be found in Appendix A.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

We first derive the deterministic map that governs the evolution of α under resampling, then show that its iterates contract in KL divergence.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

Proposition 1 (Mean-field resampling map). Under Assumption 2, the k -NN radius of a particle x i ∈ Σ c concentrates at ε i,k ≍ (kσ c / (NV p α c)) 1 /p in the limit N → ∞ with k N → ∞, k N /N → 0 [27, Ch. 2]. Consequently, the resampling weights w i ∝ ε τ i,k induce the map The map is a geometric mean of the current distribution α and the target α ∗. Its unique fi xed point on ∆ C -1 is α ∗. Thus, iterating Φ contracts α towards α ∗, with the parameter β = τ/p controlling the aggressiveness of rebalancing. We show that iterating Φ drives α to α ∗ at a geometric rate.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

Theorem 1. Consider twice differentiable constraints h, g fulfilling LICQ, which define a bounded constrained set Σ that decomposes into a finite number of connected components. Suppose all components have positive measure with respect to the induced Hausdorff measure on Σ. Under Assumption 2 for any τ ∈ (0, p) and any schedule k N →∞, k N /N → 0, the mean-field iterates α t +1 = Φ(α t) of Algorithm 1 satisfy the following bound for the initial component weights α c after the projection step of the algorithm. In particular, p α t → u Σ in KL as t →∞.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

Proof sketch. We define the relative estimation error y t,c:= α t,c α ∗ c as well as and z c:= log y 0,c and show using induction that y t,c = y (1 -β) t 0,c / ∑ j α ∗ j y (1 -β) t 0,j. Writing a t:= (1 -β) t, this admits the exponential closed form from which we can see α t is an exponential tilt of α ∗, with inverse temperature a t, which shrinks geometrically to zero.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

Substituting into the definition of KL gives the decomposition so it suffices to upper-bound ¯ z t and lower-bound log Z (a t). Both bounds follow from properties of the cumulant generating function (CGF) Λ(a):= log Z (a) of z under α ∗. For the lower bound, Jensen's inequality applied to the convex function e az gives log Z (a t) ≥ a t ∑ c α ∗ z c. For the upper bound, we use basic properties of the CGF and Popoviciu's variance inequality to obtain a bound of Λ ′′ (a) = V ν a [z] ≤ R 2 / 4, where R:= max c log(α c /α ∗ c) -min c log(α c /α ∗ c). Integrating then gives ¯ z t ≤ ¯ z α ∗ + a t R 2 / 4. As the linear terms cancel, we end with D Σ KL (p α t | p α ∗) ≤ (R 2 / 4)(1 -β) 2 t, which is the bound.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

Using this result we derive an asymptotic bound on the worst case number of iterations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

Corollary 1. Assume the conditions of Theorem 1 hold. In the worst case, the number of iterations t to reach a KL-divergence D Σ KL (p α t | p α ∗) ≤ ε is Proof sketch. We show C 0 ∈ O ((log N) 2). Bounding from above by ε lets us derive Component loss We note that Theorem 1 is only stated in the mean field. It might happen that no particles of a particular component are sampled, resulting in that component vanishing. The probability of this extinction is P c = (1 -(Φ α) c) N ≤ exp (-N (Φ α) c). Using Proposition 1 we get (Φ α) c ∝ α 1 -β c (α ∗ c) β. By Lemma 2, each component contains at least one sample, bounding α c = N c /N ≥ N -1. Since α ∗ c is constant, we can derive an asymptotic upper bound on the extinction-probability as P c ∈ O (exp(-Nα 1 -β c)) = O (exp(-N β)).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convergence Guarantees", "weight": 1.0} -->

We investigated this effect and found that, in practice, just four chains per component is enough (see Appendix C.1).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experimental Analysis", "weight": 1.0} -->

To demonstrate how MASEM improves existing manifold samplers, we consider Non-Linear Hit&-Run (NHR) and OLLA with- and without the proposed resampling logic. In addition, we compare against Sequentially Constrained MC (SCMC) which anneals soft constraints. To understand how MASEM compares against explicit component discovery and importance sampling, we implement Cluster-NHR, which clusters samples and computes resampling weights based on the estimated cluster volumes. We report the squared Sinkhorn distance and the averaged maximum slack violation. Since SCMC cannot guarantee exact constraint feasibility, we perform an additional projection step before reporting the metrics. Implementation details are listed in Appendix D and additional figures can be found in Appendix B.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental Analysis", "weight": 1.0} -->

| Problem | NHR | MASEM-NHR | OLLA | MASEM-OLLA |

<!-- chunk {"id": "body-0022", "role": "body", "section": "Synthetic Benchmarks", "weight": 1.0} -->

We first evaluate sampling on lowdimensional manifolds: - two disks that are embedded on a sphere in R 3 and we vary whether the disks are connected or not, the seven lobes density from Jeon et al. with constant f, a sine equality constraint with reducing amplitude cut into disconnected components inequality constraint, and a product of an Archimedean spiral manifold and randomly sampled circles combined with a nonlinear inequality we label swiss roll. The benchmarks are visualized in Figure 6, and we report the specific constraints and ground truth sampling method in Appendix D.2. For each problem, we run 2 000 independent chains in parallel for 5 000 steps and collect the last sample per chain.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Local Kernels Fail Under Disconnected", "weight": 1.0} -->

Components. In Figure 1 we identify a common failure mode of standard manifold samplers: In the presence of disconnected components, these local methods fail to correctly allocate mass; both methods over sample the lower disk on the sphere and under sample the left-most arc of the sine. While the connected disks problem permits the chains to mix well in the single feasible level set, separating the two spheres on the manifold leads to an increase in sampling error, as shown in Table 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Local Kernels Fail Under Disconnected", "weight": 1.0} -->

Sampling Accuracy & Constraint Violation of MASEM. As shown in Table 1, MASEM-NHR and MASEM-OLLA outperform their counterparts across all problems with a disconnected feasible set by an order of magnitude in the Sinkhorn distance W 2 2. Further, MASEM minimizes the constraints, matching (or even outperforming) their local counterparts (Figure 5). We also see in Table 2 that MASEM yields superior performance compared to the global baselines. In particular, we observe that while SCMC effectively yields constraint satisfying samples on the seven lobes problem, it fails to do so in particular on problems with highly non-linear constraints such as the swiss roll problem. Cluster-NHR, in contrast, achieves low constraint violations but higher sampling error than MASEM on all problems.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Local Kernels Fail Under Disconnected", "weight": 1.0} -->

Effect of Hyperparameters τ and M. We further examine the influence of the weight scaling hyperparameter τ and the number of rejuvenation steps M on the seven lobes problem. As shown in Figure 2, our method is robust to variations of both Figure 2: Influence of τ and M hyperparameters for MASEM-NHR on the 7 lobes problem. We mean W 2 2 distance across 5 seeds with 95% CI.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Local Kernels Fail Under Disconnected", "weight": 1.0} -->

| W 2 2 | SCMC | Cluster-NHR | MASEM-NHR | (a) Increasing ambient and fixed manifold dimension with increasing m = d -3.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Local Kernels Fail Under Disconnected", "weight": 1.0} -->

(b) Increasing ambient and manifold dimension with fixed m = 5.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Scaling Under High-Dimensionality and Large Number of Constraints", "weight": 1.0} -->

We assess the robustness and scalability of MASEM-NHR and MASEM-OLLA using a synthetic stress-test problem that enables explicit control of ambient dimension d as well as the number of equality and inequality constraints and number of disconnected components ( m,l, | C | ). In our case, we guarantee different components by sampling a set of | C | disjoint spheres, which we embed into a subspace of R d by random linear projections defined by the m equality constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scaling Under High-Dimensionality and Large Number of Constraints", "weight": 1.0} -->

Scaling Under Increasing Manifold Dimension. With fixed numbers of constraints m = l = 5 we study the effect of an increasing manifold dimension as d increases. Figure 3b shows that MASEM consistently outperforms NHR and OLLA as well as Cluster-NHR by an order of magnitude. In addition, we note that the penalty-based approach of SCMC deteriorates strongly as d increases. Further results in Figure 7 show a similar trend for the KL divergence while the maximum constraint violation stays below 0. 1 for MASEM.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling Under High-Dimensionality and Large Number of Constraints", "weight": 1.0} -->

Scaling Under Number of Constraints. Figure 3a illustrates the performances as the ambient dimension d increases while the manifold dimension is fixed to 2. We see that the gap between MASEMand its counterparts remains constant across dimensions while the W 2 2 distance only slightly increases with d. The wallclock times are competitive compared to the baselines that evaluate the constraint Jacobian (OLLA, NHR, Cluster-NHR). This shows that our method adds only little overhead in practice. Additional plots for the KL divergence and constraint violation in Figure 7 further support these results.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Robotics Applications", "weight": 1.0} -->

Motion Planning. We consider trajectory sampling, where we sample constraint satisfying trajectories through an obstacle course. We sample the trajectories of a 2d pointmass across two different obstacle courses, one that is a regular 4 × 4 grid and another one with 20 randomly placed obstacles (Figure 4). Each trajectory is parameterized by a spline defined by 3 waypoints, resulting in a 9 dimensional problem. Random obstacle motion planning has 934 constraints in total, while grid based planning has 774 inequality constraints.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Robotics Applications", "weight": 1.0} -->

Grasp Sampling. Secondly, we evaluate MASEM for grasping. We optimize grasps on a capsule geometry (a common shape for collision checking) with three fingers. A band around the capsule shall not be touched, mirroring grasping in the real world, where certain objects cannot be grasped at arbitrary points. 2 Each finger applies a force, such that in the end the fingers counteract gravity pulling on the object. This results in a 18 -dimensional problem, with 9 equality and 48 inequality constraints.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Robotics Applications", "weight": 1.0} -->

Results. Due to the lack of ground truth samples, we report the feasible entropy instead of the Sinkhorn distance. We compute it by multiplying the entropy of the feasible samples and the fraction of feasible samples (made precise in Appendix D.1). Table 3 shows an increase of sample entropy when applying MASEM, regardless of sampler. This is illustrated in Figure 4 for random obstacles. We observe that MASEM-NHR samples trajectories through the narrow gaps at the center of the course, which are missed by standard NHR. For OLLA the performance gap is even larger, as the default sampler only generates a locally distributed sample sets but fails to sample the outer regions of the domain. Moreover, OLLA generates many paths crossing over obstacles. While MASEM-NHR outperforms MASEM-OLLA on all problems, OLLA benefits more from the resampling applied by MASEM. This suggests two things: first, NHR-based samplers are more suited for robotics than OLLA-based samplers (at least within this evaluation set), and secondly, MASEM greatly improves previously unsuited samplers and makes them competitive in this domain.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Robotics Applications", "weight": 1.0} -->

We believe these are valuable for future research on sampling in robotics. Further, our approach outperforms alternative global sample allocation strategies: SCMC performs poorly on all tasks; MASEM-NHR outperforms its clustering counterpart on all tasks as well, with a large gap on the regular grid design. The performance of MASEM on the motion planning problems demonstrates its ability to scale to problems with a high number of constraints.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Robotics Applications", "weight": 1.0} -->

2 For example, a robot grasping a plate should not put its finger into the food.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Robotics Applications", "weight": 1.0} -->

| Method | Planning Random Obst. | Planning Random Obst. | Planning Grid Obst. | Planning Grid Obst. | Grasping | Grasping | Figure 4: Plots of 50 samples on the random motion planning problem. MASEM-based approaches yield the highest sample entropy across all methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

Wepresented Manifold Sampling via Entropy Maximization (MASEM), a resampling-based approach for uniform sampling on disconnected manifolds implicitly defined by constraints. We proved that MASEM minimizes the KL divergence to the uniform target distribution exponentially in the number of resampling steps and provided worst-case bounds in the mean-field. Building on this, we analyzed two instantiations of MASEM on several synthetic and real world problems. While the method introduces new parameters to tune and a small runtime overhead (which we discuss together with theoretical limitations in Appendix E), it results in a significantly lower Sinkhorn distance to the ground truth distribution compared to the baselines. Moreover, it is designed to work with any constrained MCMC-Sampler. Future research could investigate which properties make a sampler work well with MASEM. In this work we focus on entropy maximization, which leads to uniform sampling across the manifold. Future work could explore generalizations to non-uniform distributions. We see potential in applying MASEM as a data generation method in robotics and other application domains. An intriguing avenue of research is investigating practical design choices and comparing them to current heuristic approaches in practical applications.
