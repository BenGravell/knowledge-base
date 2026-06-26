<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Domain Randomization Is Sample Efficient for Linear Quadratic Control

Topics include Robotics, Robustness, Benchmarks, Control, Learning, Sampling, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the sample efficiency of domain randomization and robust control for the benchmark problem of learning the linear quadratic regulator (LQR). Domain randomization, which synthesizes controllers by minimizing average performance over a distribution of model parameters, has achieved empirical success in robotics, but its theoretical properties remain poorly understood. We establish that with an appropriately chosen sampling distribution, domain randomization achieves the optimal asymptotic rate of decay in the excess cost, matching certainty equivalence. We further demonstrate that robust control, while potentially overly conservative, exhibits superior performance in the low-data regime due to its ability to stabilize uncertain systems with coarse parameter estimates. We propose a gradient-based algorithm for domain randomization that performs well in numerical experiments, which enables us to validate the trends predicted by our analysis. These results provide insights into the use of domain randomization in learning-enabled control, and highlight several open questions about its application to broader classes of systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The use of learned world models to synthesize controllers via policy optimization is becoming increasingly prevalent in reinforcement learning. The performance of the resulting controller depends heavily upon the synthesis procedure. Simple approaches that do not account for uncertainty, known as certainty equivalence, can overfit to errors in the learned model. Robust control approaches can tolerate some error in the learned model, but may be overly conservative and computationally demanding. Consequently, *domain randomization* has emerged as a dominant paradigm in robotics for enabling transfer of policies optimized in simulation on a learned or physics-based simulator to the real world by randomizing system parameters during policy optimization. Despite the empirical success of domain randomization, it remains poorly understood how to select the randomization distribution, and how much of a discrepancy between the learned model and the real world can be tolerated.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We seek to address these issues by restricting attention to the benchmark problem of learning the linear quadratic regulator (LQR). This problem consists of collecting experimental interaction data from a linear dynamical system, and using this data to synthesize a controller that optimizes a control objective. The linear dynamical system is described by where $X_{t} \in {\mathbb{R}}^{d_{\mathsf{X}}}$ is the system state, $U_{t} \in {\mathbb{R}}^{d_{\mathsf{U}}}$ is the control input, $W_{t} \in {\mathbb{R}}^{d_{\mathsf{X}}}$ is i.i.d. mean zero Gaussian noise, and $\theta^{\star} \in {\mathbb{R}}^{d_{\theta}}$ is an unknown parameter.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal is to design a controller $K$ to minimize the objective $C{(K,\theta^{\star})}$, defined as for $Q$ and $R$ positive definite weight matrices. The subscript on the expectation denotes that the states evolves according to $X_{t + 1} = {{A{(\theta)}X_{t}} + {B{(\theta)}U_{t}} + W_{t}}$, and the superscript denotes that the inputs are selected according to the linear feedback $U_{t} = {KX_{t}}$. This benchmark problem has been used to study the sample efficiency of certainty equivalence and robust control by quantifying how many experiments from the system are sufficient to achieve some level of control performance. In this work, we study the sample efficiency of domain randomization, which chooses a control policy as for a sampling distribution $\mathcal{D}$ determined using the dataset of experiments collected.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our contribution is to study the sample efficiency of domain randomization and robust control to establish the relationships visualized as a conceptual diagram in Figure 1. In particular, we achieve the following: Sample Effiency of Domain Randomization: We prove that with an appropriately chosen sampling distribution $\mathcal{D}$, the domain randomization procedure of achieves the optimal asymptotic rate of decay with the number of samples, thereby matching the performance of certainty equivalence in the large sample regime. We further conjecture that the burn-in time for DR lies between that of RC and CE. We leave proving this to future work, but verify this conjecture numerically.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

Sample Effiency of Robust Control: We prove the tightest known bound on robust control, improving the asymptotic rate of decay with the number of samples $N$ from $1/\sqrt{N}$ to $1/N$. The upper bounds indicate a gap between the asymptotic rate of decay for robust control, and the rate of decay for domain randomization and certainty equivalence in terms of system-theoretic quantities. We conjecture that this gap is fundamental, due to the conservative nature of robust control. However, we establish that robust control can achieve a smaller burn-in time relative to certainty equivalence, due to its ability to stabilize the system with a coarse estimate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Algorithm for Domain Randomization: We propose an algorithm to solve which proves effective in numerical experiments. This enables verification of the trends predicted in the aforementioned results, and aligns with the conceptual diagram in Figure 1. While the focus of this work is restricted to linear systems, the proposed algorithm can in principle extend to general nonlinear systems, whereas similar extensions for robust control face computational challenges.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

By providing this characterization, our work demonstrates the potential of domain randomization in learning-enabled control, and partially explains the empirical success that it has achieved in robotics applications. We therefore conclude by highlighting several interesting open questions regarding the use of domain randomization for learning-enabled control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Domain Randomization", "weight": 1.0} -->

Domain randomization, introduced by Tobin et al., is widely used for *sim-to-real transfer*. By randomizing simulator parameters during training, it aims to produce policies robust to simulator variations, thereby enabling transfer to the real-world. This approach has been applied in areas like autonomous racing and robotic control. However, its success depends heavily on selecting an effective sampling strategy, which is often challenging. While previous work has explored generalization of domain randomization in discrete Markov Decision Processes, formalizing generalization for continuous control remains an open problem, which we address in this work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Identification and Control", "weight": 1.0} -->

The linear quadratic regulator problem has become a key benchmark for evaluating reinforcement learning in continuous control. The offline setting has been extensively studied: Dean et al. analyzed the sample efficiency of robust control, while Mania et al.; Wagenmaker et al.; Lee et al. showed that certainty equivalence is asymptotically instance-optimal, achieving the best possible sample efficiency with respect to system-theoretic quantities. Extensions to smooth nonlinear systems were made by Wagenmaker et al.; Lee et al.. However, certainty equivalence can perform poorly with limited data. Alternative Bayesian approaches can mitigate such limitations. We therefore show that such uncertainty-aware synthesis methods can match the asymptotic efficiency of certainty equivalence while achieving better performance in low-data regimes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Robust Control", "weight": 1.0} -->

The control community has traditionally addressed policy synthesis with imperfect models using methods like $\mathcal{H}_{\infty}$ control, which focuses on worst-case uncertainty. Randomized approaches to robust control emphasizing high-probability guarantees have also been explored. Vidyasagar proposed an average performance metric similar to domain randomization but focused on a fixed distribution rather than one informed by data. Early data-driven synthesis efforts combined classical system identification with worst-case robust control, while recent work has developed robust synthesis methods that bypass explicit models. To the best of our knowledge, existing analyses of statistical efficiency in robust control yield suboptimal rates, with excess control cost decreasing at $1/\sqrt{N}$, compared to the faster $1/N$ rate achieved by certainty equivalence. This work refines robust synthesis analysis, demonstrating the $1/N$ rate and a short burn-in period, highlighting its advantages with limited data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider the linear dynamical system. We assume that$({A{(\theta^{\star})}},{B{(\theta^{\star})}})$ is stabilizable. For ease of exposition, we restrict attention to the case where $\begin{bmatrix} \end{bmatrix} = {{\mathsf{v}\mathsf{e}\mathsf{c}}^{- 1}{(\theta,d_{\mathsf{X}})}}$, i.e. all entries of the state and input matrices are unknown. We additionally assume that $\Sigma_{w} = I$, and the cost matrices $Q \succeq I$ and $R = I$ are known.^11^1Generalizing to arbitrary $\Sigma_{w} \succ 0$, $Q \succ 0$, and $R \succ 0$ can be performed by scaling the cost and changing the state and input basis.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

When $\theta$ is known, the optimal controller that minimizes $C{(K,\theta)}$ is given by where $P{(\theta)}$ is the positive definite solution to the discrete algebraic Ricatti equation, and $K{(\theta)}$ is the LQR solution corresponding to a system with parameters $\theta$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To design a controller for the unknown system, we suppose that we have run $N$ experiments with control input $U_{t} \sim {\mathcal{N}{(0,\Sigma_{u})}}$ for $\Sigma_{u} \succ 0$. From these experiments, we collect a dataset consisting of $N$ trajectories of length $T$. We use this dataset to design a controller $\hat{K}$ such that the cost, $C{(\hat{K},\theta^{\star})}$, is small. In our analysis, we consider several approaches to achieve this objective. The approaches will be contrasted by examining the rate at which this cost decays to the optimal cost as the number of experiments in the dataset increases.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Controller Synthesis Approaches", "weight": 1.0} -->

All the synthesis approaches under consideration are model-based approaches which determine $\hat{\theta}$ from the dataset via the following least squares problem: The estimation error for $\hat{\theta}$ can be characterized using the Fisher information matrix: see, e.g. Lee et al.. Since this quantity depends on the unknown parameter, we define the estimate which quantifies the uncertainty of the estimation procedure.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Controller Synthesis Approaches", "weight": 1.0} -->

We consider three approaches to control synthesis using the estimates $\hat{\theta}$ and $\hat{\mathsf{F}\mathsf{I}}$: Certainty Equivalence (CE) uses the estimate $\hat{\theta}$ to minimize the control objective by treating the estimate as though it were ground truth: ${{K_{\mathsf{C}\mathsf{E}}{(\hat{\theta})}} = {{}_{K}C{(K,\hat{\theta})}}}.$ Robust Control (RC) constructs a high confidence ellipsoid around the nominal estimate $\hat{\theta}$ using the estimated fisher information matrix $\hat{\mathsf{F}\mathsf{I}}$ as Such a set can be shown to contain the true parameter $\theta^{\star}$ with probability at least $1 - \delta$ as long as the number of experiments, $N$, is sufficiently large (see Appendix C).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Controller Synthesis Approaches", "weight": 1.0} -->

Robust control then uses the confidence ellipsoid to determine a controller that minimizes the worst case value of the control objective over all members of the confidence set as This formulation is nonstandard, as the controller minimizes the worst-case suboptimality gap, rather than the worst case cost. However, it simplifies the analysis.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Controller Synthesis Approaches", "weight": 1.0} -->

Domain Randomization (DR) constructs a sampling distribution $\mathcal{D}$ using the least squares estimate $\hat{\theta}$ and the estimated Fisher Information $\hat{\mathsf{F}\mathsf{I}}$. It then synthesizes a controller by minimizing the average control cost as. By ensuring good performance on average over a sampling distribution, domain randomization serves as a middle ground between certainty equivalence and robust control. In particular, it can be interpreted as enforcing a high probability robust stability constraint over the sampling region.^22^2If the controller is not stabilizing for a subset of systems with nonzero mass, the cost will be infinite. Careful choice of the sampling distribution is therefore critical for downstream performance. Our analysis informs this choice.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Controller Synthesis Approaches", "weight": 1.0} -->

The goal of this paper is to study the sample efficiency of these three approaches. In particular, we consider upper bounds on the gap ${C{(\hat{K},\theta^{\star})}} - {C{({K{(\theta^{\star})}},\theta^{\star})}}$, where $\hat{K}$ is a controller synthesized with CE, RC, or DR. We express these bounds in terms of system-theoretic quantities, and the number of experiments collected from the system. Doing so provides an indication of the types of systems on which these methods perform well. We focus our attention on two key quantities: the burn-in time required to ensure finite bounds, and the asymptotic rate of decay in these bounds.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

The leading term is stated up to universal constants. The burn-in time reports the components which are different between the three approaches. We use the shorthand τB(θ⋆) = ∥B(θ⋆)∥ ∨ 1. We classify algorithms as scalable if they are possible to implement via first order gradient-based approaches.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

Our sample efficiency bounds are summarized in Table 1, where they are compared with existing bounds for certainty equivalence. The leading term in the bound characterizes the asymptotic rate of decay. For all three synthesis approaches described in Section 2.1, the leading term depends on four quantities: the parameter dimension, $d_{\theta}$, the number of experiments, $N$, the Fisher Information matrix ${\mathsf{F}\mathsf{I}}{(\theta^{\star})}$, and a matrix $H{(\theta^{\star})}$, which captures the sensitivity of control synthesis to the estimation error.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

In particular, $H{(\theta^{\star})}$ is given by Wagenmaker et al. show that $\frac{1}{N}{}\left({H{(\theta^{\star})}{\mathsf{F}\mathsf{I}}{(\theta^{\star})}^{- 1}} \right)$ is the optimal asymptotic rate achievable by any algorithm mapping a dataset to a controller.^44^4This lower bound is specified to our setting in Appendix D. Accordingly, both certainty equivalence and domain randomization can be classified as sample-efficient, as they achieve this optimal rate of decay with respect to system-theoretic quantities.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

The bound on robust control instead has a leading term of ${d_{\theta}\left\| {H{(\theta^{\star})}{\mathsf{F}\mathsf{I}}{(\theta^{\star})}^{- 1}} \right\|} \geq {\left({H{(\theta^{\star})}{\mathsf{F}\mathsf{I}}{(\theta^{\star})}^{- 1}} \right)}$, and therefore cannot be classified as efficient.^55^5While we lack a formal lower bound proving the inefficiency of RC, experiments support this conclusion (see Fig. 2).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

Table 1 also highlights the burn-in time, the number of samples that suffice for the sample efficiency bounds to hold. The reported values omit terms common to all three methods. Among the differing quantities, the burn-in for CE scales with $\left\| {P{(\theta^{\star})}} \right\|^{10}$, for DR it scales with $\left\| {P{(\theta^{\star})}} \right\|^{11}\tau_{B{(\theta^{\star})}}^{12}$, and for RC it scales with the max of $\left\| {P{(\theta^{\star})}} \right\|^{4}$ and $\frac{1}{r^{2}}$, a term quantifying the robust stabilizability of $\theta^{\star}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

Although $\frac{1}{r^{2}}$ can be as large as $\left\| {P{(\theta^{\star})}} \right\|^{10}$, it is often much smaller (see Section 3.2), suggesting that robust control can achieve a much lower burn-in than the alternative approaches for many system instances.^66^6We emphasize that these burn-in conditions are sufficient but not necessary; refining them is left to future work. Experiments further suggest that domain randomization's burn-in can potentially fall between that of certainty equivalence and robust control.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sample Efficiency Bounds for Controller Synthesis Approaches", "weight": 1.0} -->

Finally, Table 1 highlights that certainty equivalence and domain randomization give rise to scalable gradient-based policy optimization algorithms, which can easily be extended to nonlinear and high dimensional systems. In contrast, the solving the robust control problem requires computationally challenging LMI-based approaches, even for fully observed linear systems.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sample Efficiency of Domain Randomization", "weight": 1.0} -->

We now establish the characterization of domain randomization in the final row of Table 1. To this end, we first define a burn-in time which enables a bound on the the least squares error: A bound on least squares using this quantity is shown in Appendix C. Proofs for the remainder of the results in this section may be found in Appendix G.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Sample Efficiency of Domain Randomization", "weight": 1.0} -->

We first state a bound on the performance of domain randomization that holds for general sampling distributions centered at $\hat{\theta}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sample Efficiency of Robust Control", "weight": 1.0} -->

We now establish the second row of Table 1 by analyzing the efficiency of robust control. Our goal is to demonstrate how robust control addresses the limitations of certainty equivalence with limited data. To achieve this, we introduce a formal definition of robust stabilizability for the system. In this definition, we denote the state covariance of system $\theta$ under controller $K$ by $\Sigma^{K}{(\theta)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 3.4", "weight": 1.0} -->

However, we can achieve a better characterization for this instance by noting that for any subset $G$ of the interval $\lbrack 0.3,1.8\rbrack$, synthesizing an LQR controller $k$ using the largest value of the parameter in $G$ ensures that ${a + {b^{\star}k}} < 0.97$ for all $a \in G$, thereby ensuring that $\left\| {\Sigma^{k}{(a)}} \right\| \leq \frac{1}{1 -.97^{2}} \leq 20$ for all $a \in G$. Then the instance is $(20,0.75)$-robustly stabilizable by CE.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 3.4", "weight": 1.0} -->

To illustrate the impact on control performance, suppose we have an estimate $\hat{a} = 1.01$. The certainty-equivalent controller derived from this estimate is $k = {- 0.0424}$, which fails to stabilize the true system. In contrast, if we apply robust control over any uncertainty set within the interval $\lbrack 0.3,1.8\rbrack$ that includes $a^{\star}$, we synthesize a controller that stabilizes the system. Therefore, the robust control procedure selects such a controller to avoid infinite cost.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 3.4", "weight": 1.0} -->

With the definition of robust stabilizability by certainty equivalence in hand, we proceed to state an upper bound on the excess cost incurred by the robust controller.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Linear System", "weight": 1.0} -->

We validate the trends predicted in Table 1 through a case study on the linear system We first estimate $A$ and $B$ using least squares identification, then synthesize CE, DR, and RC controllers based on the identified models. Further details are provided in Appendix H.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Linear System", "weight": 1.0} -->

In Figure 2, we plot the median and shade 25 % to 75 % quantile over 500 random seeds. This result reveals two key observations. First, both DR and RC stabilize the system with fewer experiments than CE. While the improved performance of DR in the low-data regime lacks concrete theoretical justification, Theorem 3.5 supports this trend for RC. Second, after an initial period, DR converges faster than RC, eventually matching the convergence rate of CE. This aligns with the conclusion of Theorem 3.2 and is consistent with the conceptual illustration in Figure 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Pendulum", "weight": 1.0} -->

We extend the approach to nonlinear systems of pendulum by applying receding horizon control. For CE, planning occurs by minimizing a finite horizon cost for a trajectory planned using the nominal system estimate. For domain randomization, planning occurs by minimizing the average finite horizon cost for trajectories planned with a collection of systems sampled from a distribution around the system estimate.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Pendulum", "weight": 1.0} -->

The result is shown in Figure 3, which plots the mean and standard error over 100 random seeds. As observed in the linear system, the trends that (i) DR outperforms CE in the low-data regime and (ii) the convergence rate of CE and DR matches hold even for the nonlinear system. Implementation details are deferred to the Appendix H.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithmic considerations", "weight": 1.0} -->

Our numerical experiments use a gradient-based algorithm for DR, detailed in Algorithm 1. This algorithm builds on the scenario approach of Vidyasagar and the policy gradient method introduced for the linear quadratic regulator by Fazel et al.. The algorithm initially samples a number of scenarios from the distribution. At each iteration, the gradient update is performed on the cost summed over all scenarios. Since the control cost gradient becomes infinite if the current iterate does not stabilize a system, we incorporate only the gradients for system which the current iterate stabilizes. While we lack a formal convergence guarantee for this algorithm, numerical experiments indicate that it converges with a sufficiently small step size.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithmic considerations", "weight": 1.0} -->

1:Input: Randomization distribution 𝒟, estimate θ̂, stepsize η, # iterations M, # scenarios N 4:for i = 1, 2, …, M do ∖∖ Gradient descent on stable scenarios Algorithm 1 Domain Randomized Policy-Gradient for the Linear Quadratic Regulator This algorithm raises numerous questions which may be fruitful directions for future work.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithmic considerations", "weight": 1.0} -->

Convergence analysis of Algorithm 1: Extending the convergence analysis of policy gradient methods for LQR by Fazel et al.; Hu et al. to the proposed algorithm could provide theoretical guarantees for convergence to the solution of. Such an analysis would offer strong evidence of the algorithm's applicability beyond the toy numerical example presented here.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithmic considerations", "weight": 1.0} -->

Alternative choices of distribution: We proposed sampling from a uniform distribution over the confidence ellipsoid to maximize the spread of the sampling distribution without sacrificing asymptotic efficiency (Theorem 3.2). Exploring alternative distributions, such as truncated normal distributions, could reveal differences in empirical performance. These alternatives might also enable refined analyses of Theorem 3.2, particularly with respect to burn-in time.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithmic considerations", "weight": 1.0} -->

Extension to nonlinear systems: Algorithm 1 can, in principle, be extended to nonlinear systems, provided that gradients of the control objective can be obtained via Monte Carlo sampling. The least-squares analysis for CE in Table 1 also extends nonlinear systems, suggesting that the proposed domain randomization approach could also be effective for such systems. This may yield sample efficiency guarantees analogous to those studied here.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theoretical extensions", "weight": 1.0} -->

There are additionally numerous directions to tighten the analysis and generalize the setting.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical extensions", "weight": 1.0} -->

Improved burn-in time for domain randomization: While this work empirically demonstrates that DR can stabilize the system even in the low-data regime, the burn-in time derived in Lemma 3.1 does not reflect this advantage, as it is larger than that of CE in Theorem E.1. The only known way to improve the burn-in time is by adopting a robustly stabilizable condition, which considers the worst case but results in a conservative upper bound on the excess cost, as shown in Theorem 3.5. A promising direction for future work is to tighten the analysis for burn-in requirements and higher order terms of DR while maintaining its asymptotic efficiency.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Theoretical extensions", "weight": 1.0} -->

Robust control lower bound: Our upper bounds feature a gap between the asymptotic convergence rate of RC and that of CE and DR. We conjecture that this gap is fundamental; however, a lower bound on the sample efficiency of RC would be required to formalize this.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Theoretical extensions", "weight": 1.0} -->

Misspecification: This work has focused on the use of DR to address model uncertainty arising from variance in model fitting. Specifically, the assumption of the dynamics in imposes a realizability condition, ensuring that a suitably constructed distribution $\mathcal{D}$ contains $\theta^{\star}$ in its support with high probability. However, a key explanation for the empirical success of DR in many robotics applications is its robustness to model misspecification. Investigating this theoretically represents a promising direction for future work.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

By analyzing the sample efficiency of learning the linear quadratic regulator via domain randomization and robust control, our work provides insights into the tradeoffs present for approaches to incorporate uncertainty quantification into learning-enabled control. Our analysis demonstrates that if one is strategic about the design of the sampling distribution, then the benefits of domain randomization over robust control may extend beyond computational considerations, and to the sample efficiency. This is particularly exciting due to the prominence of domain randomization in practice for robot learning. We believe that this line of analysis exposes a wide spread of interesting questions regarding the use of domain randomization for learning-enabled control.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We thank Manfred Morari, Anastasios Tsiamis, Ingvar Ziemann, and Thomas Zhang for several instructive conversations. TF is supported by JASSO Exchange Support program and UTokyo-TOYOTA Study Abroad Scholarship. TF and GP are supported in part by NSF Award SLES 2331880 and NSF TRIPODS EnCORE 2217033. BL and NM are supported by NSF Award SLES-2331880, NSF CAREER award ECCS-2045834 and AFOSR Award FA9550-24-1-0102.
