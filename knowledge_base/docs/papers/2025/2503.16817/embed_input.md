<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

System Identification under Bounded Noise: Optimal Rates beyond Least Squares

Topics include System identification, Bounded noise, Least squares, Sample complexity, Linear systems, Optimality, Robustness.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies system identification when disturbances are bounded rather than stochastic in the usual least-squares-friendly way. The paper gives optimal-rate results beyond classical least squares, clarifying what estimators can exploit under adversarial or deterministic noise bounds.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

System identification is a fundamental problem in control and learning, particularly in high-stakes applications where data efficiency is critical. Classical approaches, such as the ordinary least squares estimator (OLS), achieve an O(1/sqrt(T)) convergence rate under Gaussian noise assumptions, where T is the number of samples. This rate has been shown to match the lower bound. However, in many practical scenarios, noise is known to be bounded, opening the possibility of improving sample complexity. In this work, we establish the minimax lower bound for system identification under bounded noise, proving that the O(1/T) convergence rate is indeed optimal. We further demonstrate that OLS remains limited to an (1/sqrt(T)) convergence rate, making it fundamentally suboptimal in the presence of bounded noise. Finally, we instantiate two natural variations of OLS that obtain the optimal sample complexity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification plays a crucial role in modern control design, especially in applications where accurate models of unknown dynamical systems must be learned from data. In high-stakes and safety-critical systems, where data collection can be costly or risky, sample efficiency is of particular importance. While classical results in system identification provide asymptotic convergence guarantees, they often fail to capture the finite-sample behavior. As a result, recent efforts have focused on analyzing the sample complexity of common system identification methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fundamental system identification problem is to estimate the unknown system parameter $\mathbf{A} \in {\mathbb{R}}^{n \times n}$ for an autonomous linear time-invariant (LTI) system: where $\mathbf{x}_{t} \in {\mathbb{R}}^{n}$ and $\mathbf{w}_{t} \in {\mathbb{R}}^{n}$ are the state and the noise at time $t$. When the noise $\mathbf{w}_{t}$ are independent and identically distributed (i.i.d.) Gaussian random variables, it has been shown that the ordinary least squares estimator (OLS) achieves the optimal convergence rate of $O{({1/\sqrt{T}})}$ (see, e.g.,). Consequently, many learning-based control methods have leveraged OLS as a core system identification subroutine, enabling stability, safety, and performance guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, in many applications, system designers have prior knowledge on the noise characteristics. Therefore, alternative system identification approaches seek to harness this information to improve sample efficiency. Among these, set membership estimation (SME) algorithms leverage noise boundedness for estimation. One of the key advantages of SME is its ability to provide consistent uncertainty set estimation with convergence guarantees, whereas OLS fails to do so for irregular explosive systems. Moreover, Li et al. recently show that a version of SME breaks through the $\Omega{({1/\sqrt{T}})}$ convergence rate lower bound attained by OLS for Gaussian noise, achieving a significantly faster $O{({1/T})}$ convergence rate when the noise has bounded support.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated, in this paper, we derive a minimax convergence rate lower bound for system identification when $\mathbf{w}_{t}$ is i.i.d. zero-mean with bounded support. We prove that indeed $\Omega{({1/T})}$ is the minimax lower bound for stable linear dynamical systems with bounded noise (Theorem 1. ‣ 3.1 Minimax Sample Complexity Lower Bound ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares")), establishing that the rate achieved by SME is indeed optimal. Furthermore, we demonstrate that the convergence rate lower bound for OLS remains $\Omega{({1/\sqrt{T}})}$ in this setting, revealing an inherent limitation of OLS for system identification problems with bounded noise (Theorem 2. ‣ 3.2 Optimality Gap for OLS ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares")). To put our results in perspective, we summarize some of the related lower bound results, including more traditional ones for linear regression with i.i.d. samples, in Table 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\Omega{({1/\sqrt{T}})}$ (Thm. 2) Table 1: Convergence Rate Lower Bound (LB) Summary.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation We use lower case, lower case boldface, and upper case boldface letters to denote scalars, vectors, and matrices, respectively. For a vector $\mathbf{x} \in {\mathbb{R}}^{n}$, ${\|\mathbf{x}\|}_{\infty}$ denotes its infinity norm. Identity matrices of dimension $n$ are denoted as $\mathbf{I}_{n}$. We use ${diag}{(\mathbf{v})}$ for converting a vector $\mathbf{v} \in {\mathbb{R}}^{n}$ into a diagonal matrix in ${\mathbb{R}}^{n \times n}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 1 (Open-Loop Stable)", "weight": 1.0} -->

In this paper, we are particularly interested in understanding the fundamental limit of system identification under i.i.d. bounded noise.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 3 (Probability Upper Bound of Approaching Boundary)", "weight": 1.0} -->

There exists $C_{\overline{w}} > 0$ such that for all $\epsilon \in {\lbrack 0,\overline{w}\rbrack}$ and for all $1 \leq j \leq n$, we have where $w_{t}^{(j)}$ denotes the $j$th entry of vector $\mathbf{w}_{t}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 3 (Probability Upper Bound of Approaching Boundary)", "weight": 1.0} -->

Such $C_{w}$ always exists for any distribution satisfying Assumption 2. ‣ 2 Preliminaries ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares") with a bounded probability density function (pdf). To see this, note that the probabilities in Assumption 3. ‣ 2 Preliminaries ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares") are the areas under the pdf near $\overline{w}$. Since the pdf is bounded, one can always upper bound the area under pdf with a rectangular function, the height of which is $C_{\overline{w}}$. For example, uniform and truncated Gaussian distributions trivially satisfy this assumption.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 4 (Initial Condition)", "weight": 1.0} -->

The system starts with the initial condition $\mathbf{x}_{t} = 0$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Minimax Sample Complexity Lower Bound", "weight": 1.0} -->

Our first result proves that the minimax convergence rate lower bound for the system identification of under bounded i.i.d. noise is indeed $\Omega{({1/T})}$, where the estimation error decreases at least linearly over the number of samples.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimality Gap for OLS", "weight": 1.0} -->

Given single trajectory data ${\{\mathbf{x}_{t}\}}_{t = 1}^{T}$ generated, we study the sample complexity lower bound of OLS for the estimation of the unknown system matrix $\mathbf{A}$: In what follows, we will show that OLS does not achieve the optimal rate for systems under bounded noise. For simplicity of analysis, we will focus on scalar systems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Simulation", "weight": 1.0} -->

Theorem 1. ‣ 3.1 Minimax Sample Complexity Lower Bound ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares") establishes that the optimal rate for identifying the system parameter of is $\Omega{({1/T})}$. Notably, Li et al. show that SME constructs parameter uncertainty sets whose diameters decrease at this optimal rate, where the uncertainty sets are constructed using the data ${\{\text{x}_{t}\}}_{t = 1}^{T}$ as: Therefore, we introduce two natural SME-inspired point estimators that are derived from OLS. We will compare the sample complexity of the standard OLS estimator against the two OLS-SME hybrid methods, highlighting their optimal convergence behavior.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Simulation", "weight": 1.0} -->

System setup. We consider with $\mathbf{A} \in {\mathbb{R}}^{4 \times 4}$ where entries of $\mathbf{A}$ are sampled i.i.d. from uniform distribution bounded by $\lbrack{- 5},\, 5\rbrack$. Then $\mathbf{A}$ is normalized to have ${\rho{(\mathbf{A})}} = 0.7$ to comply with Assumption 1. ‣ 2 Preliminaries ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares"). We use the uniform distribution for the noise with $\overline{w} = 2$ as the noise bound and sample $\text{w}_{t}$ i.i.d. element-wise.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Simulation", "weight": 1.0} -->

Constants in Theorem 1. ‣ 3.1 Minimax Sample Complexity Lower Bound ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares"). To compute the lower bound, we fix the probability in (2. ‣ 3.1 Minimax Sample Complexity Lower Bound ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares")) as $\delta = 0.01$. For uniform distribution in $\lbrack{- 2},\, 2\rbrack$, we have $C_{\overline{w}} = \frac{1}{4}$ for Assumption 3. ‣ 2 Preliminaries ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Simulation", "weight": 1.0} -->

System identification methods. We consider two natural SME-based point estimators. The first estimator is named OLS-SME, where, after performing OLS, we check whether the generated estimation is inside the SME uncertainty set. If it is outside, we project the OLS estimation on the SME set and call the projected point ${\hat{\mathbf{A}}}_{t}^{\text{OLS-SME}}$. Formally, The second estimator is the constrained least squares estimator, which we denote as CLS: Comparison. We plot the error^22^2The code to reproduce the experiment can be found in which is defined to be the $\ell_{2}$ distance between the true system parameter and the estimated parameter, for OLS, OLS-SME, and CLS in Figure 1. Further, we also plot the diameter of $\mathcal{P}_{T}$ ("SME diameter"). This represents the worst-case estimation error of any system identification method that constrains the estimated parameter to be inside the SME uncertainty set. As predicted by Theorems 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simulation", "weight": 1.0} -->

‣ 3.1 Minimax Sample Complexity Lower Bound ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares") and 2. ‣ 3.2 Optimality Gap for OLS ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares"), OLS exhibits a sub-optimal convergence rate while the SME-based methods converge with the same rate as the theoretical lower bound. In particular, the hybrid methods, like OLS-SME or CLS, can offer the best of both worlds: they preserve the low estimation error characteristic of OLS in low-data regime while simultaneously achieving the optimal convergence rate of SME.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work establishes the minimax sample complexity lower bound for system identification under bounded i.i.d. noise, showing that SME-based methods achieve the optimal $\Omega{({1/T})}$ convergence rate while the ordinary least squares estimator remains limited to $\Omega{({1/\sqrt{T}})}$. Future work includes improving the dimension and $\delta$ dependence of the lower bound, which is admittedly loose in our current analysis. It will also be interesting to extend the analysis to more general bounded noise models beyond the infinity norm bound.
