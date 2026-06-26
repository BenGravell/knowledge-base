## INTRODUCTION

Learning-based control plays an increasingly important role in many application domains such as power systems, robotics, self-driving cars, where it might be hard to perfectly model the system and its environment. Many learning-based control algorithms assume the existence of an initial stabilizing controller in order to simplify their analysis. Such simplifying assumptions are prevalent both in model-based and model-free learning-based control algorithms. However, learning to stabilize is a fundamental problem in learning-based control, with several algorithms tackling this issue.

Understanding the fundamental limits or the corner cases of learning-to-stabilize algorithms can inform future algorithm design and is crucial for applications of these algorithms in safety-critical domains. Therefore, it is important to understand how the system properties affect the performance of the learning-to-stabilize algorithms. In particular, we are interested in the number of samples required to learn a stabilizing controller with a given probability as a performance measure. We say a class of systems is hard to learn to stabilize if this number grows exponentially with the system dimension, independent of the algorithm choice.

We focus on fully observed linear time-invariant systems and consider the task of learning a static stabilizing linear state-feedback controller from a single trajectory. In this setting, Tsiamis et al. show that when the process noise is degenerate, i.e. the noise covariance matrix being singular, there are some classes of systems that are hard to learn to stabilize, by transferring the hardness of learning-to-stabilize into the hardness of system identification. The system classes constructed in their work are based on a (marginally) stable hard-to-stabilize pair. In this work, we significantly extend the class of systems that are hard to learn to stabilize by considering systems that are, even though close in the parameter space and generate similar state-input trajectories, not co-stabilizable with the same controller. This is achieved by a novel analysis technique that uses Ackermann's formula to compute all stabilizing linear state-feedback gains analytically and characterize the minimal level of perturbations to the parameters that render co-stabilizability infeasible. Different from the prior work, our analysis allows us to consider system classes that may only include systems with eigenvalues strictly outside of the unit circle, for which stabilizability is arguably more critical.

Notation: We use lower case, lower case boldface, and upper case boldface letters to denote scalars, vectors, and matrices respectively. For a matrix $\mathbf{M} \in {\mathbb{R}}^{m \times n}$, $\mathbf{M}^{\top}$ denotes its transpose, $M^{(i,j)}$ denotes its element in the $i^{th}$ row and the $j^{th}$ column. For a square matrix $\mathbf{M} \in {\mathbb{R}}^{n \times n}$, $\mathbf{M} \succ 0$ ($\succeq 0$) denotes that $\mathbf{M}$ is positive definite (positive semidefinite), $\rho{(\mathbf{M})}$ denotes its spectral radius, and $\det{(\mathbf{M})}$ denotes its determinant. For a vector $\mathbf{v} \in {\mathbb{R}}^{n}$, its $i^{th}$ element is denoted by $v^{(i)}$. By ${poly}{( \cdot )}$ we denote a polynomial function of its arguments. By $\exp{( \cdot )}$ we denote an exponential function of its arguments. We use $\mathbf{I}_{n}$ to denote the identity matrix in ${\mathbb{R}}^{n \times n}$. A sequence of vectors $\mathbf{x}_{t}$, $\mathbf{x}_{t + 1}$,..., $\mathbf{x}_{t + N}$ is denoted by $\mathbf{x}_{t:{t + N}}$ for short. By convention, $\mathbf{x}_{i:j}$ is an empty set if $j < i$.

## Problem Setup and Preliminary Notions

We consider the following fully-observed discrete-time linear time-invariant (LTI) system: where $\mathbf{x}_{t} \in {\mathbb{R}}^{n}$, $\mathbf{u}_{t} \in {\mathbb{R}}^{p}$, $\mathbf{w}_{t} \in {\mathbb{R}}^{n}$ are the state, input, and process noise at time $t$. For simplicity, we assume $\mathbf{x}_{0} = \mathbf{0}$. The random process $\mathbf{w}_{t}$ over $t$ is zero-mean i.i.d. Gaussian, with covariance matrix $\sigma_{w}^{2}\mathbf{I}_{n}$. In the remainder of the paper, we denote a system in the form by the tuple $(\mathbf{A},\mathbf{B})$.

Let $\mathcal{C}_{n}$ be a class of systems $(\mathbf{A},\mathbf{B})$ in dimension $n$, parameterized by some unknown parameters.

### Definition 1

A *learning-to-stabilize algorithm* $\pi$ with respect to the class $\mathcal{C}_{n}$ is a sequence of functions $\pi = {\{\pi_{t}\}}_{t = 0}^{N}$. For ${t = 0},$..., $N - 1$, $\pi_{t}{(\mathbf{u}_{0:{t - 1}},\mathbf{x}_{0:t})}$ specifies the probability distribution of the input $\mathbf{u}_{t} \in {\mathbb{R}}^{p}$ at time $t$, conditioned on the previous state-input trajectory $\mathbf{u}_{0:{t - 1}}$ and $\mathbf{x}_{0:t}$. Then at $t = N$, the function $\pi_{N}$ maps the entire state-input trajectory $\mathbf{u}_{0:{N - 1}}$ and $\mathbf{x}_{0:N}$ to a state-feedback gain in ${\mathbb{R}}^{p \times n}$. This learned state-feedback gain ${\hat{\mathbf{K}}}_{N} = {\pi_{N}{(\mathbf{u}_{0:{N - 1}},\mathbf{x}_{1:N})}}$ is called *stabilizing* if ${\rho{({\mathbf{A} + {\mathbf{B}{\hat{\mathbf{K}}}_{N}}})}} < 1$.

Intuitively, the algorithm $\pi$ consists of an exploration policy in the first $N - 1$ steps and decides on the gain ${\hat{\mathbf{K}}}_{N}$ using the data generated during exploration at step $N$. As such, exciting the system with some open-loop persistently exciting input as in data-driven control, applying some i.i.d. input and computing the gain afterward using the generated data, or active learning policies can all be considered as special types of learning-to-stabilize algorithms.

Given a system $\mathcal{S} = {(\mathbf{A},\mathbf{B})} \in \mathcal{C}_{n}$ and a learning-to-stabilize algorithm $\pi$, let ${\mathbb{P}}_{\mathcal{S},\pi}^{N}$ denote the probability measure of the input-state samples $\mathbf{u}_{0:{N - 1}}$ and $\mathbf{x}_{1:N}$ (with $f_{\mathcal{S},\pi}^{N}$ denoting the corresponding probability density function), and ${\mathbb{E}}_{\mathcal{S},\pi}^{N}$ denote the expectation of the respective probability measure. We make the following assumptions on the class $\mathcal{C}_{n}$ and the algorithm $\pi$.

### Assumption 1

For all $n \geq 1$ and all ${(\mathbf{A},\mathbf{B})} \in \mathcal{C}_{n}$, the norm of matrices $\mathbf{A},\mathbf{B}$ is bounded by a positive constant $M$, that is, ${\max_{{n \geq 1},{{(\mathbf{A},\mathbf{B})} \in \mathcal{C}_{n}}}{\max\left\{ {\|\mathbf{A}\|}_{2},{\|\mathbf{B}\|}_{2} \right\}}} \leq M$.

### Assumption 2

The second moment of the norm of the input signal $\mathbf{u}_{t}$, generated by the algorithm $\pi$, is bounded by some constant $\sigma_{u}^{2} > 0$. That is, ${{\mathbb{E}}_{\mathcal{S},\pi}\left\lbrack \left\| \mathbf{u}_{t} \right\|_{2}^{2} \right\rbrack} \leq \sigma_{u}^{2}$.

Next, we recall the definition of ${poly}{(n)}$-stabilizable system classes . If a class $\mathcal{C}_{n}$ of discrete-time LTI systems is ${poly}{(n)}$-stabilizable, it is statistically easy to learn linear state-feedback controllers to stabilize systems in this class.

### Definition 2 (${poly}{(n)}$-stabilizable system classes )

Under Assumptions 1 and 2, a class $\mathcal{C}_{n}$ of systems is ${poly}{(n)}$-stabilizable if there exists a learning-to-stabilize algorithm $\pi$ such that for all confidence levels $0 \leq \delta < 1$ if the sample size $N$ satisfies ${{N\sigma_{u}^{2}} \geq {{poly}{(n,{\log{({1/\delta})}},M)}}}.$ This definition essentially tells that a class is ${poly}{(n)}$-stabilizable if it is possible to find an algorithm that can learn a stabilizing linear state-feedback controller with high probability, even for the worst-case system in this class, as long as there are polynomially many samples in the system dimension $n$. Since the polynomial dependency on $n$ is mild, we say learning to stabilize is *easy* for this class. On the other hand, being *hard* refers to a class that is not $\text{poly}{(n)}$-stabilizable.

A closely related concept is the hardness of identification, i.e., whether the system can be learned with $\epsilon$ accuracy using $\text{poly}{(n,{\log{({1/\delta})}},{1/\epsilon})}$ many samples. When the process noise is degenerate, by transferring the hardness of learning to stabilize into the hardness of system identification, Tsiamis et al. prove that there exists a class of systems, for which the worst-case sample complexity of learning to stabilize is at least exponential with the system dimension. Our work is complementary as we seek to answer the following question.

### Problem 1

Is there a class of linear systems that are not ${poly}{(n)}$-stabilizable when the process noise $\mathbf{w}_{t}$ is non-degenerate?

The following lemma follows directly from Definition 2-stabilizable system classes ). ‣ II Problem Setup and Preliminary Notions ‣ On the Hardness of Learning to Stabilize Linear Systems").

### Lemma 1

For two classes of systems $\mathcal{C}_{n}^{1}$ and $\mathcal{C}_{n}^{2}$, if $\mathcal{C}_{n}^{1}$ is a subset of $\mathcal{C}_{n}^{2}$ and $\mathcal{C}_{n}^{1}$ is not ${poly}{(n)}$-stabilizable, neither is $\mathcal{C}_{n}^{2}$.

Lemma 1 turns Problem 1 into the problem of finding a pair of systems that are not ${poly}{(n)}$-stabilizable. Specifically, if a pair of systems is not ${poly}{(n)}$-stabilizable, then any class containing this pair of systems is also not ${poly}{(n)}$-stabilizable.

The next two definitions are related to the co-stabilizability and distinguishability of a pair of systems.

### Definition 3 (Co-stabilizability)

A pair of systems $\mathcal{S}_{1} = {(\mathbf{A}_{1},\mathbf{B}_{1})}$ and $\mathcal{S}_{2} = {(\mathbf{A}_{2},\mathbf{B}_{2})}$ is co-stabilizable if there exists a state-feedback gain $\mathbf{K}$ such that both $\mathbf{A}_{1} + {\mathbf{B}_{1}\mathbf{K}}$ and $\mathbf{A}_{2} + {\mathbf{B}_{2}\mathbf{K}}$ are stable.

### Remark 1

Co-stabilization problem for two dynamical systems has been studied in robust control, e.g., by using the gap metric.

We will use $KL$ divergence to measure the distance between the distributions of state-input trajectories generated when the same exploration policy is applied to two different systems. A small $KL$ divergence means that it is hard to distinguish two systems.

### Definition 4 (Kullback--Leibler (KL) divergence)

The KL divergence between the continuous distributions $\mathbb{P}$ and $\mathbb{Q}$ is defined as where $p{(x)}$ and $q{(x)}$ denote the probability densities of $\mathbb{P}$ and $\mathbb{Q}$ and $p{(x)}$ is absolutely continuous with respect to $q{(x)}$.

Our main insight behind constructing not ${poly}{(n)}$-stabilizable pairs in the next section is as follows. If we have two different systems and excite all the modes of these systems, as we increase the trajectory length $N$, we expect that the $KL$ divergence between the trajectories will increase and we will be able to distinguish the systems. On the other hand, if the $KL$ divergence remains small independent of the exploration policy, then we cannot expect the learning-to-stabilize algorithm to result in significantly different controller gains. Moreover, if these two systems are not co-stabilizable, then learning to stabilize these systems will be hard.

## Hard to Learn to Stabilize Systems

Consider the following system of the form with $(\mathbf{A},\mathbf{B})$ defined parametrically as where $n \geq 2$, $r > 1$, $0 < v < \frac{r - 1}{2}$, and $b^{} \geq 0$.

### Remark 2

When $b^{} = {- {v^{n}/r^{n - 1}}}$, the system in is uncontrollable. To avoid this trivially hard-to-stabilize case, we let $b^{} \geq 0$.

The following proposition proves that there exist two systems in the parametric family differing only in $b^{}$, such that for a feedback gain to be able to stabilize both systems at the same time, the difference in $b^{}$ should be exponentially small in the system dimension.

### Proposition 1

Let $\mathcal{S}_{1} = {(\mathbf{A},\mathbf{B}_{1})}$, and $\mathcal{S}_{2} = {(\mathbf{A},\mathbf{B}_{2})}$, where $\mathbf{A}$ is as, and $\mathbf{B}_{1}$ and $\mathbf{B}_{2}$ equal to $\mathbf{B}$ in with $b^{} = 0$ and $b^{} = m \geq 0$, respectively. Let $\mathbf{K} \in {\mathbb{R}}^{1 \times n}$ be any stabilizing linear state-feedback gain for $\mathcal{S}_{1}$ such that ${\rho{({\mathbf{A} + {\mathbf{B}_{1}\mathbf{K}}})}} < 1$. Let $p_{1}^{cl},p_{2}^{cl},\ldots,p_{n}^{cl}$ be the eigenvalues of $\mathbf{A} + {\mathbf{B}_{1}\mathbf{K}}$ with ${0 \leq {{|p_{1}^{cl}|},{|p_{2}^{cl}|},\ldots}},{{|p_{n}^{cl}|} < 1}$. Then ${\rho{({\mathbf{A} + {\mathbf{B}_{2}\mathbf{K}}})}} < 1$ only if The proof, which uses Ackermann's formula (Lemma 2. ‣ -A Proof of Proposition 4 ‣ V Conclusion and Future Work ‣ On the Hardness of Learning to Stabilize Linear Systems")) to analytically compute any stabilizing feedback gain of ($\mathbf{A},\mathbf{B}_{1}$) and Jury stability test (Lemma 18. ‣ -A Proof of Proposition 4 ‣ V Conclusion and Future Work ‣ On the Hardness of Learning to Stabilize Linear Systems")) to verify the closed-loop stability of ($\mathbf{A},\mathbf{B}_{2}$) when using the stabilizing gain of the former, is given in Appendix -A.

Next, we upper bound the $KL$ divergence between the probability distributions of length $N$ input-state trajectories generated by the two LTI systems defined in Proposition 4. Similar upper bounds of the $KL$ divergence between two LTI systems can also be found .

### Proposition 2

Let the systems $\mathcal{S}_{1}$, and $\mathcal{S}_{2}$ be the same as those defined in Proposition 4. Let $\pi$ be any learning-to-stabilize algorithm that satisfies Assumption 2. Then, the $KL$ divergence between ${\mathbb{P}}_{\mathcal{S}_{1},\pi}^{N}$ and ${\mathbb{P}}_{\mathcal{S}_{2},\pi}^{N}$ satisfies The proof is given in Appendix -B.

The next theorem states that there exist some classes of systems with non-degenerate process noise, for which the worst-case sample complexity of learning to stabilize is at least exponential with the system dimension $n$.

### Theorem 1

Consider $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$ defined in Proposition 4, with $m = {2\left(\frac{2v}{r - 1} \right)^{n}}$. Consider any class $\mathcal{C}_{n}$ of systems including $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, which satisfies Assumption 1. Then, for all learning-to-stabilize algorithms $\pi$ satisfying Assumption 2 and for all confidence levels $0 < \delta < {1/2}$, the requirement where $n \geq 2$, $r > 1$, and $0 < v < \frac{r - 1}{2}$.

The proof of Theorem 1 can be found in Appendix -C. In the proof we show that if the same algorithm $\pi$ is applied to $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, for the stabilization probability in to be high for both, exponentially many samples are needed. This indicates that for any class containing $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, polynomially many samples will not be sufficient for the satisfaction of requirement, therefore such classes cannot be $\text{poly}{(n)}$-stabilizable.

Comparing the systems $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$ in our proof to corresponding system pairs , our pairs are individually not necessarily "hard to identify" but the distance $m$ in the parameter space between the pairs shrinks exponentially fast as we increase $n$. As shown in Proposition 2, the input-state trajectory distributions our pairs of systems generate look very similar; this is expected since the system parameters get closer with $n$. In general, one may expect if two systems are close to each other in the parameter space, they can be co-stabilized by the same controller $\mathbf{K}$. However, our pairs cannot be co-stabilized (as shown in Proposition 4) with a single gain $\mathbf{K}$ although the systems are very close in parameter space, which is the main source of hardness.

### Remark 3

Our proof technique can also be extended to show the hardness of learning to stabilize for classes of systems containing single-input systems with diagonal state matrices and $n$ unstable eigenvalues in a compact range, presented . In that case, when the input vector is the all-one vector, the controllability matrix of the system is a Vandermonde matrix, which allows us to again use Ackermann's formula to obtain the explicit form of all stabilizing linear state-feedback gains. Results similar to Proposition 4 and Theorem 1 can be established in this case too.

## Numerical Experiments

In this section, we implement two numerical experiments, i.e., certainty equivalent linear quadratic regulator (LQR) and robust control, to show the hardness of stabilization.

### IV-A Certainty Equivalent LQR

Since solving LQR problems always gives stabilizing controllers (under mild regularity conditions), the first experiment considers the certainty equivalent LQR control. Specifically, a controller is computed by solving an LQR problem using some estimated system dynamics and then applied to the ground truth system. The infinite-horizon LQR problem, simplified as $dLQR{(\mathbf{A},\mathbf{B},\mathbf{Q},\mathbf{R})}$, is as follows.

| | | $\min\limits_{\mathbf{u}_{0},\mathbf{u}_{1},\cdots}{\lim\limits_{T\rightarrow\infty}{{\mathbb{E}}\left\lbrack {\frac{1}{T}{\sum\limits_{t = 0}^{T}\left({{\mathbf{x}_{t}^{\top}{\mathbf{Q}\mathbf{x}}_{t}} + {\mathbf{u}_{t}^{\top}{\mathbf{R}\mathbf{u}}_{t}}} \right)}} \right\rbrack}}$ | | \(6\) | | | | $\begin{array}{rrcc} | | | where $\mathbf{Q},\mathbf{R}$ are positive semi-definite cost matrices. Its solution is given by $\mathbf{u}_{t} = {\mathbf{K}\mathbf{x}}_{t}$ where the controller $\mathbf{K}$ can be computed by solving the Riccati equation. Consider the system $(\mathbf{A},\mathbf{B}_{1})$ defined in Proposition 4, and let $\mathbf{Q} = \mathbf{I}_{n}$, and $\mathbf{R} = 1$. Since the analysis of Theorem 1 is established on perturbing $b^{}$ in $\mathbf{B}_{1}$, we consider a simplified setting where only $b^{}$ is unknown and to be estimated using the least squares estimator, which is denoted by ${\hat{b}}^{}$. Let ${\hat{\mathbf{B}}}_{1}$ denote the matrix by replacing $b^{}$ with ${\hat{b}}^{}$ and $\hat{\mathbf{K}}$ denote the certainty equivalent controller for $(\mathbf{A},\mathbf{B}_{1})$ obtained by solving $dLQR{(\mathbf{A},{\hat{\mathbf{B}}}_{1},\mathbf{Q},\mathbf{R})}$. We let the input $u_{t}\overset{i.i.d.}{\sim}\mathcal{N}{(0,\sigma_{u}^{2})}$. Since there is only a single unknown parameter and its regressor $u_{t}$ is independent, this system is trivially easy to identify.

For each dimension $n$, we run $M = 200$ independent experiments. Let ${\hat{\mathbf{K}}}_{i,N'}$ denote the controller obtained using the first $N'$ data points, i.e., $\{\mathbf{u}_{0:{N' - 1}},\mathbf{x}_{1:N'}\}$, in the $i^{th}$ experiment. We record the smallest trajectory length $N$ under which at least 90% of the experiments produce stabilizing controllers, i.e. where $\mathbb{I}$ denotes the indicator function.

The results are given in Fig. 1. According to Fig. 1, we have that as the system dimension increases, the required number of samples for a given frequency of stability increases exponentially with the system dimension.

Figure 1: Required trajectory length N for 90% stabilization rate vs. system dimension n: σu2 = 32, σw2 = 0.005, v ∈ {1.01, 1.05, 1.09}

### IV-B LMI-based Sufficient Condition for Co-stabilizability

In this section, we numerically demonstrate the hardness of co-stabilizability of $\mathcal{S}_{1} = {(\mathbf{A},\mathbf{B}_{1})}$ and $\mathcal{S}_{2} = {(\mathbf{A},{\mathbf{B}_{2}{(m)}})}$ using ideas from robust control, where we leave $m$ as a parameter. We use the following feasibility problem, which can be converted to an LMI, to check sufficient conditions of co-stabilizability.

We use the bisection method to find the largest $m$ such that the problem is feasible. The results are shown in Fig. 2. According to this figure, we see that as the system dimension increases, the largest $m$ such that the LMI optimization problem in is feasible decreases exponentially with increasing system dimension, which is consistent with Eq. in Proposition 4.

Figure 2: v = 1.01, 1.05, 1.09, and r = 3.2. The x-axis is the system dimension n and the y-axis is the logarithm of the largest m such that the problem in is feasible.

## Conclusion and Future Work

In this work, we identified an extended class of LTI systems that are hard to learn to stabilize with static state feedback. The main idea in constructing such examples is to find pairs of systems whose parameters become exponentially close to each other as the dimension increases, yet they are not co-stabilizable. One interesting observation is that the entries of stabilizing gains for these pairs are also growing exponentially (see, Eq. ). In the future, we want to investigate the ramifications of this observation in gradient-based learning algorithms used for control as .

*Acknowledgments:* The authors would like to thank Prof. Peter Seiler of University of Michigan for some early discussions that motivated this work.

### A Proof of Proposition 4

We first introduce a few lemmas used in the proof of Proposition 4. The first lemma parameterizes all stabilizing state-feedback gains for single-input controllable LTI systems. Recall that the controllability matrix of a system $(\mathbf{A},\mathbf{B})$ is defined by

### Lemma 2 (Ackermann's formula )

Consider the following order $n$ single-input controllable system $(\mathbf{A},\mathbf{B})$ with state feedback $\mathbf{K} \in {\mathbb{R}}^{1 \times n}$: Given $n$ desired eigenvalues of $\mathbf{A} + {\mathbf{B}\mathbf{K}}$, the unique state feedback that achieves these closed-loop eigenvalues is: where $\mathbf{e}_{n}$ is the last column of the $n \times n$ identity matrix, and $\Delta^{cl}{(\mathbf{A})}$ is the characteristic polynomial of $\mathbf{A} + {\mathbf{B}\mathbf{K}}$ evaluated at $\mathbf{A}$.

The next lemma derives the expression of the first element of any stabilizing state-feedback gains for $(\mathbf{A},\mathbf{B}_{1})$, parameterized by the stable closed-loop poles.

### Lemma 3

For the system $(\mathbf{A},\mathbf{B}_{1})$ defined in Proposition 4 and any stabilizing state feedback $\mathbf{K} \in {\mathbb{R}}^{1 \times n}$, let ${\{ p_{k}^{cl}\}}_{k = 1}^{n}$ be the eigenvalues of $\mathbf{A} + {\mathbf{B}_{1}\mathbf{K}}$, with ${\{ p_{k}^{cl}\}}_{k = 1}^{n}$ all inside the unit circle. Then, the first element $k_{1}$ of the state feedback $\mathbf{K}$ satisfies

### Proof

By Lemma 2. ‣ -A Proof of Proposition 4 ‣ V Conclusion and Future Work ‣ On the Hardness of Learning to Stabilize Linear Systems"), since $(\mathbf{A},\mathbf{B}_{1})$ is single-input and controllable, the state feedback $\mathbf{K}$ satisfies where the characteristic polynomial $\Delta^{cl}{(\mathbf{A})}$ of the closed-loop system $\mathbf{A} + {\mathbf{B}_{1}\mathbf{K}}$ evaluated at $\mathbf{A}$ is By the definition of $\mathbf{A}$, for all $i = 1$, $2$,..., $n$, Based, the element of $\Delta^{cl}{(\mathbf{A})}$ at the first row and the first column is Furthermore, due to the special structures of $(\mathbf{A},\mathbf{B}_{1})$, it can be shown that the last row of the inverse of the controllability matrix ${\mathbf{C}\mathbf{t}\mathbf{r}}_{(\mathbf{A},\mathbf{B}_{1})}$ is Thus, according to and, the first element of the state feedback $\mathbf{K}$ is | | $k_{1}$ | $= {- {v^{- n}\left\lbrack {\Delta^{cl}{(\mathbf{A})}} \right\rbrack^{}}}$ | | \(17\) | | | | ${= {- \frac{\left({r - p_{1}^{cl}} \right)\left({r - p_{2}^{cl}} \right)\cdots\left({r - p_{n}^{cl}} \right)}{v^{n}}}}.$ | | | The next lemma provides a necessary condition for the stability of discrete-time LTI systems.

### Lemma 4 (Jury stability test, Theorem 4.6 in )

For the polynomial with $a_{n} > 0$, the roots of the polynomial are inside the unit circle only if Now, we are ready to present the proof of Proposition 4.

### Proof

Consider the two systems $(\mathbf{A},\mathbf{B}_{1})$ and $(\mathbf{A},\mathbf{B}_{2})$ in Proposition 4.

Let $\mathbf{K}$ be any stabilizing state-feedback gain of $(\mathbf{A},\mathbf{B}_{1})$. By Lemma 3, the first element of $\mathbf{K}$ satisfies where $p_{1}^{cl}$, $p_{2}^{cl}$,..., $p_{n}^{cl}$ are the eigenvalues of $\mathbf{A} + {\mathbf{B}_{1}\mathbf{K}}$ with ${{|p_{1}^{cl}|},{|p_{2}^{cl}|},\ldots,{|p_{n}^{cl}|}} < 1$. Next, it can be shown that the characteristic polynomial $\Delta_{n}^{cl}{(z)}$ of $\mathbf{A} + {\mathbf{B}_{1}\mathbf{K}}$ is Similarly, one can show that the characteristic polynomial ${\hat{\Delta}}_{n}^{cl}{(z)}$ of $\mathbf{A} + {\mathbf{B}_{2}\mathbf{K}}$ satisfies | | ${\hat{\Delta}}_{n}^{cl}{(z)}$ | $:={\det{({{z\mathbf{I}} - \mathbf{A} - {\mathbf{B}_{\mathbf{2}}\mathbf{K}}})}}$ | | \(21\) | By Lemma 18. ‣ -A Proof of Proposition 4 ‣ V Conclusion and Future Work ‣ On the Hardness of Learning to Stabilize Linear Systems"), the matrix $\mathbf{A} + {\mathbf{B}_{2}\mathbf{K}}$ is stable only if Also, note that Combining and, we have that $\mathbf{A} + {\mathbf{B}_{2}\mathbf{K}}$ is stable only if

### B Proof of Proposition 2

For simplicity of notation, we denote ${\mathbb{P}}_{\mathcal{S}_{i},\pi}^{t}$, $f_{\mathcal{S}_{i},\pi}^{t}$, and ${\mathbb{E}}_{\mathcal{S}_{1},\pi}^{t}$ by ${\mathbb{P}}_{i}^{t}$, $f_{i}^{t}$, and ${\mathbb{E}}_{1}^{t}$ respectively, for $i = {1,2}$, and $0 \leq t \leq N$. With this notation, Proposition 2 can be proven as follows.

### Proof

Starting with the definition of KL divergence (i.e., Definition 4 divergence). ‣ II Problem Setup and Preliminary Notions ‣ On the Hardness of Learning to Stabilize Linear Systems")), we have | | {{KL}\left({\mathbb{P}}_{1}^{N},{\mathbb{P}}_{2}^{N} \right)} & {= {{\mathbb{E}}_{1}^{N}\left\lbrack {\log\frac{f_{1}^{N}\left(\mathbf{u}_{0:{N - 1}},\mathbf{x}_{0:N} \right)}{f_{2}^{N}\left(\mathbf{u}_{0:{N - 1}},\mathbf{x}_{0:N} \right)}} \right\rbrack}} \\ | | | | | & {= {{\mathbb{E}}_{1}^{N}\left\lbrack {\log\frac{\prod_{t = 0}^{N}{f_{1}^{t}\left({\mathbf{x}_{t} \mid {\mathbf{x}_{0:{t - 1}},\mathbf{u}_{0:{t - 1}}}} \right)}}{\prod_{t = 0}^{N}{f_{2}^{t}\left({\mathbf{x}_{t} \mid {\mathbf{x}_{0:{t - 1}},\mathbf{u}_{0:{t - 1}}}} \right)}}} \right\rbrack}} \\ | | | | | & {+ {{\mathbb{E}}_{1}^{N}\left\lbrack {\log\frac{\prod_{t = 0}^{N - 1}{f_{1}^{t}\left({\mathbf{u}_{t} \mid {\mathbf{x}_{0:t},\mathbf{u}_{0:{t - 1}}}} \right)}}{\prod_{t = 0}^{N - 1}{f_{2}^{t}\left({\mathbf{u}_{t} \mid {\mathbf{x}_{0:t},\mathbf{u}_{0:{t - 1}}}} \right)}}} \right\rbrack}} \\ | | | | | & {{= {\sum\limits_{t = 0}^{N}{{\mathbb{E}}_{1}^{t}\left\lbrack {\log\frac{f_{1}^{t}\left({\mathbf{x}_{t} \mid {\mathbf{x}_{t - 1},\mathbf{u}_{t - 1}}} \right)}{f_{2}^{t}\left({\mathbf{x}_{t} \mid {\mathbf{x}_{t - 1},\mathbf{u}_{t - 1}}} \right)}} \right\rbrack}}},} | | | where the second equality is from the properties of the conditional probability density functions and the third equality is because the exploration policies of these two systems are the same and the discrete-time LTI system has the Markovian structure.

Based on the special structure of $(\mathbf{A},\mathbf{B})$ of $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, we have the following relationships between every element of state vectors of these systems: Due to, and the fact that $w_{t}^{(j)}$ for $j = {1,\ldots,n}$ are mutually independent, we have for $i = 1$ and $2$, | | | $f_{i}^{t}\left({\mathbf{x}_{t} \mid {\mathbf{x}_{t - 1},\mathbf{u}_{t - 1}}} \right)$ | | \(29\) | According to and, we also have where $\mathcal{N}$ denotes the Gaussian distribution.

| | {{KL}\left({\mathbb{P}}_{1}^{N},{\mathbb{P}}_{2}^{N} \right)} & {= {\sum\limits_{t = 1}^{N}{{\mathbb{E}}_{1}^{t}\left\lbrack {\log\frac{f_{1}^{t}\left({x_{t}^{} \mid {x_{t - 1}^{},x_{t - 1}^{},\mathbf{u}_{t - 1}}} \right)}{f_{2}^{t}\left({x_{t}^{} \mid {x_{t - 1}^{},x_{t - 1}^{},\mathbf{u}_{t - 1}}} \right)}} \right\rbrack}}} \\ | | | | | & {= {\sum\limits_{t = 1}^{N}{{\mathbb{E}}_{1}^{t}\left\lbrack \frac{\left({w_{t - 1}^{} + {m\mathbf{u}_{t - 1}}} \right)^{2} - \left(w_{t - 1}^{} \right)^{2}}{2\sigma_{w}^{2}} \right\rbrack}}} \\ | | | | | & {= {\sum\limits_{t = 1}^{N}{{\mathbb{E}}_{1}^{t}\left\lbrack \frac{\left({m\mathbf{u}_{t - 1}} \right)^{2}}{2\sigma_{w}^{2}} \right\rbrack}}} \\ | | | | | & {{\leq \frac{Nm^{2}\sigma_{u}^{2}}{2\sigma_{w}^{2}}},} | | | where the first equality is due to and, the second equality is due to and the definition of the Gaussian distribution, the third equality is by the noise process being zero mean and $w_{t - 1}^{}$ and $\mathbf{u}_{t - 1}$ being independent, and the last inequality is due to Assumption 2. ∎

### C Proof of Theorem 1

Before presenting the proof of Theorem 1, we first introduce Birgé's inequality, a classical inequality from information theory.

### Lemma 5 (Birgé's Inequality, Theorem 4.21 in )

Let $\Omega$ be a set and $\mathcal{E}$ be a $\sigma$-algebra on the set $\Omega$. Let ${\mathbb{P}}_{1},{\mathbb{P}}_{2}$ be probability measures on the probability space $(\Omega,\mathcal{E})$ and let ${E_{1},E_{2}} \in \mathcal{E}$ be disjoint events. If ${1 - \delta} \triangleq {{\min_{i = {1,2}}{\mathbb{P}}_{i}}\left(E_{i} \right)} \geq {1/2}$ then Next, we present the proof of Theorem 1.

### Proof

Given $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, let us define two events: | | E_{1} & {{= \left\{ {\mathbf{u}_{0:{N - 1}},\mathbf{x}_{1:N}}\mid{{\rho\left({\mathbf{A} + {\mathbf{B}_{1}\pi_{N}{(\mathbf{u}_{0:{N - 1}},\mathbf{x}_{1:N})}}} \right)} < 1} \right\}},} \\ | | | | E_{2} & {{= \left\{ {\mathbf{u}_{0:{N - 1}},\mathbf{x}_{1:N}}\mid{{\rho\left({\mathbf{A} + {\mathbf{B}_{2}\pi_{N}{(\mathbf{u}_{0:{N - 1}},\mathbf{x}_{1:N})}}} \right)} < 1} \right\}}.} | | Since $m = {2\left(\frac{2v}{r - 1} \right)^{n}} > {v^{n}{\prod_{i = 1}^{n}\frac{1 + p_{i}^{cl}}{r - p_{i}^{cl}}}}$ for any stable closed-loop poles, by Proposition 4, $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$ cannot be co-stabilized. Hence, $E_{1}$ and $E_{2}$ are disjoint events.

Suppose is true, which implies Therefore, we can apply Lemma 5. ‣ -C Proof of Theorem 1 ‣ V Conclusion and Future Work ‣ On the Hardness of Learning to Stabilize Linear Systems") to obtain | | ${KL}\left({\mathbb{P}}_{\mathcal{S}_{1},\pi}^{N},{\mathbb{P}}_{\mathcal{S}_{2},\pi}^{N} \right)$ | $\geq {{{({1 - \delta})}{\log\frac{1 - \delta}{\delta}}} + {\delta{\log\frac{\delta}{1 - \delta}}}}$ | | \(34\) | | | | ${\geq {\log\left(\frac{1}{3\delta} \right)}}.$ | | | According to Proposition 2, the KL divergence between ${\mathbb{P}}_{\mathcal{S}_{1},\pi}^{N}$ and ${\mathbb{P}}_{\mathcal{S}_{2},\pi}^{N}$ satisfies Combining and, we have that holds only if
