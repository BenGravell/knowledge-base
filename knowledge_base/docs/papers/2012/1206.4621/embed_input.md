<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Integral Policy Improvement with Covariance Matrix Adaptation

Topics include Path integral control, Policy optimization, Reinforcement learning, Covariance matrix adaptation, Exploration noise, Continuous control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that PI2, CEM, and CMA-ES all share the concept of probability-weighted averaging for parameter updates, unifying them into a common family. Derives PI2-CMA, which inherits PI2's stochastic optimal control foundations while automatically adapting the exploration noise covariance, eliminating the need to manually tune exploration magnitude.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

There has been a recent focus in reinforcement learning on addressing continuous state and action problems by optimizing parameterized policies. PI2 is a recent example of this approach. It combines a derivation from first principles of stochastic optimal control with tools from statistical estimation theory. In this paper, we consider PI2 as a member of the wider family of methods which share the concept of probability-weighted averaging to iteratively update parameters to optimize a cost function. We compare PI2 to other members of the same family - Cross-Entropy Methods and CMAES - at the conceptual level and in terms of performance. The comparison suggests the derivation of a novel algorithm which we call PI2-CMA for "Path Integral Policy Improvement with Covariance Matrix Adaptation". PI2-CMA's main advantage is that it determines the magnitude of the exploration noise automatically.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scaling reinforcement learning (RL) methods to continuous state-action problems, such as humanoid robotics tasks, has been the focus of numerous recent studies. Most of the progress in the domain comes from direct policy search methods based on trajectory rollouts. The recently proposed direct 'Policy Improvement with Path Integrals' algorithm (PI 2) is derived Appearing in Proceedings of the 29 th International Conference on Machine Learning, Edinburgh, Scotland, UK, 2012. Copyright 2012 by the author(s)/owner(s). from first principles of stochastic optimal control, and is able to outperform gradient-based RL algorithms such as REINFORCE and Natural Actor-Critic by an order of magnitude in terms of convergence speed and quality of the final solution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

What sets PI 2 apart from other direct policy improvement algorithms is its use of probability-weighted averaging to perform a parameter update, rather than using an estimate of the gradient. Interestingly enough, 'Covariance Matrix Adaptation - Evolutionary Strategy ( CMAES )' and 'Cross-Entropy Methods ( CEM )' are also based on this concept. It is striking that these algorithms, despite having been derived from very different principles, have converged to almost identical parameter update rules. To the best of our knowledge, this paper is the first to make this relationship between the three algorithms explicit (Section 2). This hinges on 1) re-interpreting CEM as performing probability-weighted averaging; 2) demonstrating that CEM is a special case of CMAES, by setting certain CMAES parameters to extreme values.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A further contribution of this paper is that we conceptually and empirically investigate the differences and similarities between PI 2, CEM, and CMAES (Section 3). These comparisons suggest a new algorithm, PI 2 -CMA, which has the algorithm structure of PI 2, but uses covariance matrix adaptation as found in CEM and CMAES. A practical contribution of this paper is that we show how PI 2 -CMA automatically determines the exploration magnitude, the only parameter which is not straightforward to tune in PI 2.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Cross-Entropy Method (CEM)", "weight": 1.0} -->

Given a n -dimensional parameter vector θ and a cost function J: R n ↦→ R, the Cross-Entropy Method ( CEM ) for optimization searches for the global minimum with the following steps: Sample - Take K samples θ k =1...K from a distribution. Sort - Sort the samples in ascending order with respect to the evaluation of the cost function J ( θ k ). Update - Recompute the distribution parameters, based only on the first K e 'elite' samples in the sorted list. Iterate - return to the first step with the new distribution, until costs converge, or up to a certain number of iterations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Cross-Entropy Method (CEM)", "weight": 1.0} -->

A commonly used distribution is a multi-variate Gaussian distribution N ( θ, Σ) with parameters θ (mean) and Σ (covariance matrix), such that these three steps are implemented as in -. An example of one iteration of CEM is visualized in Figure 1, with a multivariate Gaussian distribution in a 2D search space 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Cross-Entropy Method (one iteration)", "weight": 1.0} -->

Throughout this paper, it is useful to think of CEM as performing probability-weighted averaging, where the elite samples have probability 1 /K e, and the non-elite have probability 0. With these values of P k, - can be rewritten as in the left algorithm in Table 1. Here we use Q K e /K to denote the K e th quantile of the distribution J k =1...K. This notation is chosen for brevity; it simply means that in the sorted array of ascending J k, P k is 1 /K e if K ≤ K e, and 0 otherwise, as. The resulting parameter updates are equivalent to those in and, but this representation makes the relation to PI 2 more obvious.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Cross-Entropy Method (one iteration)", "weight": 1.0} -->

CEM for Policy Improvement. Because CEM is a very general algorithm, it is used in many different contexts in robot planning and control. CEM for policy optimization was introduced by Mannor et al.. Although their focus is on solving finite small Markov Decision Processes (MDPs), they also propose to use CEM with parameterized policies to solve MDPs with large state spaces. Busoniu et al. extend this work, and use CEM to learn a mapping from continuous states to discrete actions, where the centers and widths of the basis functions are automatically adapted. The main difference with our work is that we use continuous action spaces of higher dimensionality, and compare CEM to PI 2 and CMAES. CEM has also been used in combination with sampling-based motion planning. An interesting aspect of this work is that it uses a mixture of Gaussians rather than a single distribution to avoid premature convergence to a local minimum. In, a CEM is extended to optimize a controller that generates trajectories to any point of the reachable space of the system.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Cross-Entropy Method (one iteration)", "weight": 1.0} -->

1 Note that, the unbiased estimate of the covariance is acquired by multiplying with 1 K e, rather than 1 K e -1, because we know the true mean to be θ.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Covariance Matrix Adaptation Evolution Strategy", "weight": 1.0} -->

The Covariance Matrix Adaptation - Evolution Strategy algorithm is very similar to CEM, but uses a more sophisticated method to update the covariance matrix, as listed in Table 2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Covariance Matrix Adaptation Evolution Strategy", "weight": 1.0} -->

Table 1. Comparison of the CEM and PI 2. This pseudo-code represents one iteration of the algorithm, consisting of an exploration phase and a parameter update phase. Both algorithms iterate these two phases until costs have converged, or up to a certain number of iterations. The green equations - and - are only used in PI 2 -CMA (to be explained in Section 3.4), and not part of 'standard' PI 2.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Covariance Matrix Adaptation Evolution Strategy", "weight": 1.0} -->

| | Cross-Entropy Method | Description | PI 2 | | There are three differences to CEM: · The probabilities in CMAES do not have to be P k = 1 /K e as for CEM, but can be chosen by the user, as long as the constraints ∑ K e k =1 P k = 1 and P 1 ≥ ··· ≥ P K e are met. Here, we use the default suggested by Hansen & Ostermeier, i.e. P k = ln (0. 5(K +1)) -ln (k). · Sampling is done from a distribution N (θ, σ 2 Σ), i.e. the covariance matrix of the normal distribution is multiplied with a scalar step-size σ. These components govern the magnitude (σ) and shape (Σ) of the exploration, and are updated separately. · For both step-size and covariance matrix an 'evolution path' is maintained (p σ and p Σ respectively), which stores information about previous updates to θ. Using the information in the evolution path leads to significant improvements in terms of convergence speed, because it enables the algorithm to exploit correlations between consecutive steps.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Covariance Matrix Adaptation Evolution Strategy", "weight": 1.0} -->

For a full explanation of the algorithm we refer to Hansen & Ostermeier.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Covariance Matrix Adaptation Evolution Strategy", "weight": 1.0} -->

Reducing CMAES to CEM. This is done by setting certain parameters to extreme values: 1) set the time horizon c σ = 0. This makes collapse to σ new = σ × exp, which means the step-size stays equal over time. Initially setting the step-size σ init = 1 means σ will always be 1, thus having no effect during sampling. 2) For the covariance matrix update, we set c 1 = 0 and c µ = 1. The first two terms of then drop, and what remains is ∑ K e k =1 P k (θ k -θ)(θ k -θ) ᵀ, Table 2. The step-size and covariance matrix adaptation update rule of CMAES, which make use of the evolution paths and. µ P is the variance effective selection mass, with µ P = 1 / ∑ K e k =1 P 2 k. The entire CMAES algorithm is acquired by replacing of CEM in Table 1 with these four equations, and multiplying Σ with σ 2. which is equivalent to in CEM, if P k is chosen as.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Covariance Matrix Adaptation Evolution Strategy", "weight": 1.0} -->

CMAES for Policy Improvement. HeidrichMeisner and Igel use CMAES to directly learn a policy for a double pole-balancing task. R¨ uckstiess et al. use Natural Evolution Strategies (NES), which has comparable results with CMAES, to di- rectly learn policies for pole balancing, robust standing, and ball catching. The results above are compared with various gradient-based methods, such as REINFORCE and NAC. To the best of our knowledge, our paper is the first to directly compare CMAES with CEM and PI 2. Also, we use Dynamic Movement Primitives as the underlying policy representation, which 1) enables us to scale to higher-dimensional problems, as demonstrated; 2) requires us to perform temporal averaging, cf. and.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy Improvement with Path Integrals", "weight": 1.0} -->

A recent trend in reinforcement learning is to use parameterized policies in combination with probabilityweighted averaging; the PI 2 algorithm is a recent example of this approach. Using parameterized policies avoids the curse of dimensionality associated with (discrete) state-action spaces, and using probabilityweighted averaging avoids having to estimate a gradient, which can be difficult for noisy and discontinuous cost functions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy Improvement with Path Integrals", "weight": 1.0} -->

PI 2 is derived from first principles of optimal control, and gets its name from the application of the Feynman-Kac lemma to transform the HamiltonJacobi-Bellman equations into a so-called path integral, which can be approximated with Monte Carlo methods. The PI 2 algorithm is listed to the right in Table 1. As in CEM, K samples θ k =1...K are taken from a Gaussian distribution. In PI 2, the vector θ represents the parameters of a policy, which, when executed, yields a trajectory τ i =1...N with N time steps. This multi-dimensional trajectory may represent the joint angles of a n -DOF arm, or the 3-D position of an end-effector.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Improvement with Path Integrals", "weight": 1.0} -->

So far, PI 2 has mainly been applied to policies represented as Dynamic Movement Primitives (DMPs), where θ determines the shape of the movement. Although PI 2 searches in the space of θ, the costs are defined in terms of the trajectory τ generated by the DMP when it is integrated over time. The cost of a trajectory is determined by evaluating J for every time step i, where the cost-to-go of a trajectory at time step i is defined as the sum over all future costs S ( τ i,k ) = ∑ N j = i J ( τ j,k ), as in 2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy Improvement with Path Integrals", "weight": 1.0} -->

Analogously, the parameter update is applied to every time step i with respect to the cost-to-go S ( τ i ). The probability of a trajectory at i is computed by exponentiating the cost, as. This assigns high probability to low-cost trials, and vice versa. In prac- tice, -1 λ S i,k is implemented with optimal baselining as -h ( S i,k -min( S i,k )) max( S i,k ) -min( S i,k ) cf..

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy Improvement with Path Integrals", "weight": 1.0} -->

As can be seen, a different parameter update θ new i is computed for each time step i. To acquire the single parameter update θ new, the final step is therefore to average over all time steps. This average is weighted such that earlier parameter updates in the trajectory contribute more than later updates, i.e. the weight at time step i is T i = ( N -1) / ∑ N j =1 ( N -1). The intuition is that earlier updates affect a larger time horizon and have more influence on the trajectory cost.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy Improvement with Path Integrals", "weight": 1.0} -->

PoWeR is another recent policy improvement algorithm that uses probability-weighted averaging. In PoWeR, the immediate costs must behave like an improper probability, i.e. sum to a constant number and always be positive. This can make the design of cost functions difficult in practice; for instance cannot be used with PoWeR. PI 2 places no such constraint on the cost function, which may be discontinuous. When a cost function is compatible with both PoWeR and PI 2, they perform essentially identical.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison of PI 2, CEM and CMAES", "weight": 1.0} -->

When comparing CEM, CMAES and PI 2, there are some interesting similarities and differences. All sample from a Gaussian to explore parameter space - and are identical - and both use probabilityweighted averaging to update the parameters - and. It is striking that these algorithms, which have been derived within very different frameworks, have converged towards the same principle of probability-weighted averaging.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison of PI 2, CEM and CMAES", "weight": 1.0} -->

We would like to emphasize that PI 2 's properties follow directly from first principles of stochastic optimal control. For instance, the eliteness mapping follows from the application of the Feymann-Kac lemma to the (linearized) Hamilton Jacobi Bellmann equations, as does the concept of probability-weighted averaging. Whereas in other works the motivation for using CEM / CMAES for policy improvement is based on its empirical performance (e.g. it is shown to outperform a particular gradientbased method), the PI 2 derivation demonstrates that there is a theoretically sound motivation for using methods based on probabilityweighted averaging, as this principle follows directly from first principles of stochastic optimal control.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison of PI 2, CEM and CMAES", "weight": 1.0} -->

Whereas Section 2 has mainly highlighted the similarities between the algorithms, this section focuses on the differences. Note that any differences between PI 2 and CEM / CMAES in general also apply to the specific application of CEM / CMAES to policy improvement, as done for instance by Busoniu et al. or Heidrich-Meisner and Igel. Before comparing the algorithms, we first present the evaluation task used in the paper.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation Task", "weight": 1.0} -->

For evaluation purposes, we use a viapoint task with a 10-DOF arm. The task is visualized and described in Figure 2. This viapoint task is taken, where it is used to compare PI 2 with PoWeR, NAC, and REINFORCE.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluation Task", "weight": 1.0} -->

The goal of this task is expressed with the cost function, where a represents the joint angles, x and y the coordinates of the end-effector, and D = 10 the number of DOF. The weighting term ( D +1 -d ) penalizes DOFs closer to the origin, the underlying motivation being that wrist movements are less costly than shoulder movements for humans, cf..

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluation Task", "weight": 1.0} -->

The 10 joint angles trajectories are generated by a 10dimensional DMP, where each dimension has B = 5 basis functions. The parameter vectors θ (one 1 × 5 vector for each of the 10 dimensions), are initialized by training the DMP with a minimum-jerk movement. During learning, we run 10 trials per update K = 10, where the first of these 10 trials is a noise-free trial used for evaluation purposes. For PI 2, the eliteness parameter is h = 10, and for CEM and CMAES it is K e = K/ 2 = 5. The initial exploration noise is set to Σ = 10 4 I B =5 for each dimension of the DMP.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Exploration Noise", "weight": 1.0} -->

A first difference between CEM / CMAES and PI 2 is the way exploration noise is generated. In CEM and CMAES, time does not play a role, so only one exploration vector θ k is generated per trial. In stochastic optimal control, from which PI 2 is derived, θ i represents a motor command at time i, and the stochasticity θ i + ϵ i is caused by executing command in the environment. When applying PI 2 to DMPs, this stochasticity rather represents controlled noise to foster exploration, which the algorithm samples from θ i ∼ N ( θ, Σ). We call this time-varying exploration noise. Since this exploration noise is under our control, we need not vary it at every time step. In the work by Theodorou et al. for instance, only one exploration vector θ k is generated at the beginning of a trial, and exploration is only applied to the DMP basis function that has the highest activation. We call this per-basis exploration noise.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Exploration Noise", "weight": 1.0} -->

In the most simple version, called constant exploration noise, we sample θ k,i =0 once at the beginning for i = 0, and leave it unchanged throughout the execution of the movement, i.e. θ k,i = θ k,i =0.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Exploration Noise", "weight": 1.0} -->

The learning curves for these different variants are depicted in Figure 3. We conclude that time-varying exploration convergences substantially slower. Because constant exploration gives the fastest convergence, we use it throughout the rest of the paper.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

We now turn to the most interesting and relevant difference between the algorithms. In CEM / CMAES, both the mean and covariance of the distribution are updated, whereas PI 2 only updates the mean. This is because in PI 2 the shape of the covariance matrix is constrained by the relation Σ = λ R -1, where R is the (fixed) command cost matrix, and λ is a parameter inversely proportional to the parameter h. This constraint is necessary to perform the derivation of PI 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

In this paper, we choose to ignore the constraint Σ = λ R -1, and apply covariance matrix updating to PI 2. Because a covariance matrix update is computed for each time step i, we need to perform temporal averaging for the covariance matrix, just as we do for the mean θ. Temporal averaging over covariance matrices is possible, because 1) every positive-semidefinite matrix is a covariance matrix and vice versa 2) a weighted averaging over positivesemidefinite matrices yields a positive-semidefinite matrix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

Thus, rather than having a fixed covariance matrix, PI 2 now adapts Σ based on the observed costs for the trials, as depicted in Figure 4. This novel algorithm, which we call PI 2 -CMA, for 'Path Integral Policy Improvement with Covariance Matrix Adaptation', is listed in Table 1 (excluding the red indices i = 1... N, and including the green equations and ). A second algorithm, PI 2 -CMAES, is readily acquired by using the more sophisticated covariance matrix updating rule of CMAES. Our next evaluation highlights the main advantage of these algorithms, and compares their performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

In Figure 6, we compare PI 2 (where the covariance matrix is constant 3 ) with PI 2 -CMA ( CEM -style covariance matrix updating) and PI 2 -CMAES (covariance matrix updating with CMAES ). Initially, the covariance matrix for each of the 10 DOFs is set to Σ init = λ init I 5, where 5 is the number of basis functions, and λ init = { 10 2, 10 4, 10 6 } determines the initial exploration magnitude. All experiments are run for 200 updates, with K = 20 trials per update. We chose a higher K because we are now not only computing an update of the mean of the parameters (a 1 × 5 vector for each DOFs), but also its covariance matrix (a 5 × 5 matrix), and thus more information is needed per trial to get a robust update. After each update, a small amount of base level exploration noise is added to the covariance matrix (Σ new ← Σ new + 10 2 I 5 ) to avoid premature convergence, as suggested by Kobilarov.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

When the covariance matrices are not updated, the exploration magnitude remains the same during learning, i.e. λ = λ init (labels A in Figure 6), and the convergence behavior is different for the different exploration magnitudes λ init = { 10 2, 10 4, 10 6 }. For λ init = 10 4 we have nice convergence behavior B, which is not a coincidence - this value has been specifically tuned for this task, and it is the default we have used so far. However, when we set the exploration magnitude very low ( λ init = 10 2 ) convergence is much slower C. When the exploration magnitude is set very high λ init = 10 6, we get quick convergence D. But due to the high stochasticity in sampling, we still have a lot of stochasticity in the cost after convergence in comparison to lower λ init. This can be seen in the inset, where the y -axis has been scaled × 20 for detail E.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

For PI 2 -CMA, i.e. with covariance matrix updating, we see that the exploration magnitude λ changes over time (bottom graph), whereby λ is computed as the mean of the eigenvalues of the covariance matrix. For λ init = 10 2, λ rapidly increases F until a maximum value is reached, after which it decreases and converges to a value of 10 2. 8 G. The same holds for λ init = 10 4, but the initial increase is not so rapid H. For λ init = 10 6, λ only decreases I, but converges to 10 2. 8 as the others.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

3 Please note the difference between 1) constant exploration as in Section 3.2, where a sampled parameter vector θ k is not varied during the movement made in one trial; 2) constant covariance matrix, where Σ is not updated and thus constant during an entire learning session.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

From these results we derive three conclusions: 1) with PI 2 -CMA, the convergence speed does not depend as much on the initial exploration magnitude λ init, i.e. after 500 updates the µ ± σ cost for PI 2 -CMA over all λ init is 10 5 · (8 ± 7), whereas for PI 2 without covariance matrix updating it is 10 5 · (35 ± 43) J. 2) PI 2 -CMA automatically increases λ if more exploration leads to quicker convergence F H. 3) PI 2 -CMA automatically decreases λ once the task has been learned G K. Note that 2) and 3) are emergent properties of covariance matrix updating, and has not been explicitly encoded in the algorithm. In summary, PI 2 -CMA is able to find a good exploration/exploitation trade-off, independent of the initial exploration magnitude.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

This is an important property, because setting the exploration magnitude by hand is not straightforward, because it is highly task-dependent, and might require several evaluations to tune. One of the main contributions of this paper is that we demonstrate how using probability-weighted averaging to update the covariance matrix (as is done in CEM ) allows PI 2 to autonomously tune the exploration magnitude - the user thus no longer needs to tune this parameter. The only remaining parameters of PI 2 are K (number of trials per update) and h (eliteness parameter), but choosing them is not critical. Although an initial Σ must be given, Figure 6 shows that with an initial exploration magnitude two orders of magnitude higher/lower than a tuned value, PI 2 -CMA still converges to the same cost and exploration magnitude, with only slight differences in the initial speed of convergence.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Covariance Matrix Adaptation", "weight": 1.0} -->

When comparing PI 2 -CMA and PI 2 -CMAES, we only see a very small difference in terms of convergence when the initial exploration is low λ init = 10 2 L. This is because the covariance update rule of CMAES is damped, and, and it makes more conservative updates than CEM, cf. I and N. In our experiments, PI 2 -CMAES uses the default parameters suggested by Hansen & Ostermeier. We have tried different parameters for PI 2 -CMAES, the conclusion being that the best parameters are those that reduce CMAES to CEM, cf. Section 2.2. In general, we do not claim that PI 2 -CMAES outperforms PI 2, and Hansen & Ostermeier also conclude that there are tasks where CMAES has identical performance to simpler algorithms. Our results on comparing PI 2 -CMAES and PI 2 -CMA are therefore not conclusive. An interesting question is whether typical cost functions found in robotics problems have properties that do not allow CMAES to leverage the advantages it has on benchmark problems used in optimization.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we have scrutinized the recent stateof-the-art direct policy improvement algorithm PI 2 from the specific perspective of belonging to a family of methods based on the concept of probabilityweighted averaging. We have discussed similarities and differences between three algorithms in this family, being PI 2, CMAES and CEM. In particular, we have demonstrated that using probability-weighted averaging to update the covariance matrix, as is done in CEM and CMAES, allows PI 2 to autonomously tune the exploration magnitude. The resulting algorithm PI 2 -CMA shows more consistent convergence under varying initial conditions, and alleviates the user from having to tune the exploration magnitude parameter by hand. We are currently applying PI 2 -CMA to challenging tasks on a physical humanoid robot. Given the ability of PI 2 to learn complex, high-dimensional tasks on real robots, we are con- fident that PI 2 -CMA can also successfully be applied to such tasks.
