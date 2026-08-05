<!-- arxiv-full-text:v1 {"arxiv_id": "1101.3039", "source": "ar5iv"} -->

## Abstract

Freedman's inequality is a martingale counterpart to Bernstein's inequality. This result shows that the large-deviation behavior of a martingale is controlled by the predictable quadratic variation and a uniform upper bound for the martingale difference sequence. Oliveira has recently established a natural extension of Freedman's inequality that provides tail bounds for the maximum singular value of a matrix-valued martingale. This note describes a different proof of the matrix Freedman inequality that depends on a deep theorem of Lieb from matrix analysis. This argument delivers sharp constants in the matrix Freedman inequality, and it also yields tail bounds for other types of matrix martingales. The new techniques are adapted from recent work by the present author.

### Key words and phrases

Discrete-time martingale, large deviation, probability inequality, random matrix, sum of independent random variables 2010 Mathematics Subject Classification. Primary: 60B20. Secondary: 60F10, 60G50, 60G42 JAT is with Computing & Mathematical Sciences, MC 305-16, California Inst. Technology, Pasadena, CA 91125. E-mail: jtropp@acm.caltech.edu. Research supported by ONR award N00014-08-1-0883, DARPA award N66001-08-1-2065, and AFOSR award FA9550-09-1-0643.

## An Introduction to Freedman's Inequality

The Freedman inequality \[, Thm. (1.6)\] is a martingale extension of the Bernstein inequality. This result demonstrates that a martingale exhibits normal-type concentration near its mean value on a scale determined by the predictable quadratic variation, and the upper tail has Poisson-type decay on a scale determined by a uniform bound on the difference sequence.

Oliveira \[, Thm. 1.2\] proves that Freedman's inequality extends, in a certain form, to the matrix setting. The purpose of this note is to demonstrate that the methods from the author's paper can be used to establish a sharper version of the matrix Freedman inequality. Furthermore, this approach offers a transparent way to obtain other probability inequalities for adapted sequences.

Let us introduce some notation and background on martingales so that we can state Freedman's original result rigorously. Afterward, we continue with a statement of our main results and a presentation of the methods that we need to prove the matrix generalization.

### Martingales

Let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a probability space, and let $\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2} \subset \cdots \subset \mathcal{F}$ be a filtration of the master sigma algebra. We write ${\mathbb{E}}_{k}$ for the expectation conditioned on $\mathcal{F}_{k}$. A *martingale* is a (real-valued) random process $\{ Y_{k}:{k = {0,1,2,\ldots}}\}$ that is adapted to the filtration and that satisfies two properties: For simplicity, we assume that the initial value of a martingale is null: $Y_{0} = 0$. The *difference sequence* is the random process defined by Roughly, the present value of a martingale depends only on the past values, and the martingale has the status quo property: today, on average, is the same as yesterday.

### Freedman's Inequality

Freedman uses a powerful stopping-time argument to establish the following theorem for scalar martingales \[, Thm. (1.6)\].

### Theorem 1.1 (Freedman)

Consider a real-valued martingale $\{ Y_{k}:{k = {0,1,2,\ldots}}\}$ with difference sequence $\{ X_{k}:{k = {1,2,3,\ldots}}\}$. Assume that the difference sequence is uniformly bounded: Define the predictable quadratic variation process of the martingale: Then, for all $t \geq 0$ and $\sigma^{2} > 0$, When the difference sequence $\{ X_{k}\}$ consists of independent random variables, the predictable quadratic variation is no longer random. In this case, Freedman's inequality reduces to the usual Bernstein inequality \[, Thm. 6\].

### Matrix Martingales

Matrix martingales are defined in much the same manner as scalar martingales. Consider a random process $\{{\mathbf{Y}}_{k}:{k = {0,1,2,\ldots}}\}$ whose values are matrices of finite dimension. We say that the process is a *matrix martingale* when We write $\left. \parallel \cdot \parallel \right.$ for the *spectral norm*, which coincides with the operator norm between Hilbert spaces. As before, we assume that ${\mathbf{Y}}_{0} = \mathbf{0}$, and we define the difference sequence $\{{\mathbf{X}}_{k}:{k = {1,2,3,\ldots}}\}$ via the relation A matrix-valued random process is a martingale if and only if we obtain a scalar martingale when we track each fixed coordinate in time.

### Freedman's Inequality for Matrices

In the elegant paper, Oliveira establishes that it is possible to extend Freedman's inequality to the matrix setting. He studies martingales that take self-adjoint matrix values, and he shows that the *maximum eigenvalue* of the martingale satisfies a result very similar to Freedman's inequality. The uniform bound $R$ and the predictable quadratic variation $\{ W_{k}\}$ are replaced by natural noncommutative extensions. As a consequence, these results have powerful applications in random matrix theory.

In this note, we establish a sharper version of Oliveira's theorem \[, Thm. 1.2\].

### Theorem 1.2 (Matrix Freedman)

Consider a matrix martingale $\{\mathbf{Y}_{k}:{k = {0,1,2,\ldots}}\}$ whose values are self-adjoint matrices with dimension $d$, and let $\{\mathbf{X}_{k}:{k = {1,2,3,\ldots}}\}$ be the difference sequence. Assume that the difference sequence is uniformly bounded in the sense that Define the predictable quadratic variation process of the martingale: Then, for all $t \geq 0$ and $\sigma^{2} > 0$, Here and elsewhere, $\lambda_{\max}$ denotes the algebraically largest eigenvalue of a self-adjoint matrix, and $\left. \parallel \cdot \parallel \right.$ denotes the spectral norm, which returns the largest singular value of a matrix.

Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") offers several concrete improvements over Oliveira's original work. His theorem \[, Thm. 1.2\] requires a stronger uniform bound of the form $\left\| {\mathbf{X}}_{k} \right\| \leq R$, and the constants in his inequality are somewhat larger (but still very reasonable).

We prove Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") in Section 3 as a consequence of a stronger probability inequality that follows from a general result for adapted sequences of matrices. These tail bounds cannot be sharpened without changing their structure; see \[, §4 and §6\] for a more detailed discussion.

As an immediate corollary of Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales"), we obtain a result for rectangular matrices.

### Corollary 1.3 (Rectangular Matrix Freedman)

Consider a matrix martingale $\{\mathbf{Y}_{k}:{k = {0,1,2,\ldots}}\}$ whose values are matrices with dimension $d_{1} \times d_{2}$, and let $\{\mathbf{X}_{k}:{k = {1,2,3,\ldots}}\}$ be the difference sequence. Assume that the difference sequence is uniformly bounded: Define two predictable quadratic variation processes for this martingale: Then, for all $t \geq 0$ and $\sigma^{2} > 0$,

### Proof Sketch

Define a self-adjoint matrix martingale $\{{\mathbf{Z}}_{k}\}$ with dimension $d = {d_{1} + d_{2}}$ via Apply Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") to this martingale. See \[, §2.6 and §4.2\] for some additional details about this type of argument. ∎

### Tools and Techniques

In his paper, Oliveira describes a way to transport Freedman's stopping-time argument to the matrix setting. The main technical obstacle is to control the evolution of the moment generating function (mgf) of the matrix martingale. Oliveira accomplishes this task using an insightful variation on a idea due to Ahlswede and Winter \[, App.\]. This method, however, does not result in the sharpest bounds on the matrix mgf.

This note demonstrates that the ideas allow us to obtain the sharp estimates for the mgf with minimal effort. Our main tool is a deep theorem \[, Thm. 6\] of Lieb.

### Theorem 1.4

Fix a self-adjoint matrix $\mathbf{H}$. The function is concave on the positive-definite cone.

See \[, §3.3\] and for some additional discussion of this result. We apply Theorem 1.4. ‣ 1.5. Tools and Techniques ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") through the following simple corollary \[, Cor. 3.2\]. We include a proof for completeness.

### Corollary 1.5

Let $\mathbf{H}$ be a fixed self-adjoint matrix, and let $\mathbf{X}$ be a random self-adjoint matrix. Then

### Proof

Define the random matrix ${\mathbf{Y}} = e^{\mathbf{X}}$, and calculate that The first identity follows because the logarithm can be defined as the functional inverse of the matrix exponential. Lieb's result, Theorem 1.4. ‣ 1.5. Tools and Techniques ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales"), establishes that the trace function is concave in $\mathbf{Y}$, so we may invoke Jensen's inequality to draw the expectation inside the logarithm. ∎ A significant advantage of our point of view is that the proof extends in a transparent way to yield other types of probability inequalities for adapted sequence of random matrices. We have dilated on this observation in a preliminary version of this work that is now available as a technical report. Here, for brevity, we focus on proving Freedman's inequality.

## Tail Bounds via Martingale Methods

In this section, we show that Freedman's techniques extend to the matrix setting with minor (but profound) changes. The key idea is to use Corollary 1.5. ‣ 1.5. Tools and Techniques ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") to control the evolution of a matrix version of the moment generating function. This argument culminates in a rather general theorem on the large deviation behavior of an adapted sequence of random matrices. In §3, we specialize this result to obtain Freedman's inequality.

### Additional Terminology

We say that a sequence $\{{\mathbf{X}}_{k}\}$ of random matrices is *adapted* to the filtration when each ${\mathbf{X}}_{k}$ is measurable with respect to $\mathcal{F}_{k}$. Loosely speaking, an adapted sequence is one where the present depends only upon the past. We say that a sequence $\{{\mathbf{V}}_{k}\}$ of random matrices is *previsible* when each ${\mathbf{V}}_{k}$ is measurable with respect to $\mathcal{F}_{k - 1}$. In particular, the sequence $\{{{\mathbb{E}}_{k - 1}{\mathbf{X}}_{k}}\}$ of conditional expectations of an adapted sequence $\{{\mathbf{X}}_{k}\}$ is previsible. A *stopping time* is a random variable $\kappa:{\Omega\rightarrow{{\mathbb{N}}_{0} \cup {\{\infty\}}}}$ that satisfies In words, we can determine if the stopping time has arrived from current and past experience.

### The Large Deviation Supermartingale

Consider an adapted random process $\{{\mathbf{X}}_{k}:{k = {1,2,3,\ldots}}\}$ and a previsible random process $\{{\mathbf{V}}_{k}:{k = {1,2,3,\ldots}}\}$ whose values are self-adjoing matrices with dimension $d$. Suppose that the two processes are connected through a relation of the form where the function $g:{{(0,\infty)}\rightarrow{\lbrack 0,\infty\rbrack}}$. The left-hand side should be interpreted as a conditional cumulant generating function (cgf); see \[, Sec. 3.1\]. It is convenient to introduce the partial sums of the original process and the partial sums of the conditional cgf bounds: The random matrix ${\mathbf{W}}_{k}$ can be viewed as a measure of the total variability of the process $\{{\mathbf{X}}_{k}\}$ up to time $k$. The partial sum ${\mathbf{Y}}_{k}$ is unlikely to be large unless ${\mathbf{W}}_{k}$ is also large.

To continue, we fix the function $g$ and a positive number $\theta$. Define a real-valued function with two self-adjoint matrix arguments: We use the function $G_{\theta}$ to construct a real-valued random process.

This process is an evolving measure of the discrepancy between the partial sum process $\{{\mathbf{Y}}_{k}\}$ and the cumulant sum process $\{{\mathbf{W}}_{k}\}$. The following lemma describes the key properties of this random sequence. In particular, the average discrepancy decreases with time.

### Lemma 2.1

For each fixed $\theta > 0$, the random process $\{{S_{k}{(\theta)}}:{k = {0,1,2,\ldots}}\}$ defined in (2.2) is a positive supermartingale whose initial value $S_{0} = d$.

### Proof

It is easily seen that $S_{k}$ is positive because the exponential of a self-adjoint matrix is positive definite, and the trace of a positive-definite matrix is positive. We obtain the initial value from a short calculation: To prove that the process is a supermartingale, we ascend a short chain of inequalities.

In the second line, we invoke Corollary 1.5. ‣ 1.5. Tools and Techniques ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales"), conditional on $\mathcal{F}_{k - 1}$. This act is legal because ${\mathbf{Y}}_{k - 1}$ and ${\mathbf{W}}_{k}$ are both measurable with respect to $\mathcal{F}_{k - 1}$. The next inequality depends on the assumption (2.1) together with the fact that the trace exponential is monotone with respect to the semidefinite order \[, §2.2\]. The last step follows because $\{{\mathbf{W}}_{k}\}$ is the sequence of partial sums of $\{{\mathbf{V}}_{k}\}$. ∎ Finally, we present a simple inequality for the function $G_{\theta}$ that holds when we have control on the eigenvalues of its arguments.

### Lemma 2.2

Suppose that ${\lambda_{\max}{(\mathbf{Y})}} \geq t$ and that ${\lambda_{\max}{(\mathbf{W})}} \leq w$. For each $\theta > 0$,

### Proof

Recall that ${g{(\theta)}} \geq 0$. The bound results from a straightforward calculation: The first inequality depends on the semidefinite relation ${\mathbf{W}} \preccurlyeq {w\mathbf{I}}$ and the monotonicity of the trace exponential with respect to the semidefinite order \[, §2.2\]. The second inequality relies on the fact that the trace of a psd matrix is at least as large as its maximum eigenvalue. The third identity follows from the spectral mapping theorem and elementary properties of the maximum eigenvalue map. ∎

### Tail Bound for Adapted Sequences

Our key theorem for adapted sequences provides a bound on the probability that the partial sum of a matrix-valued random process is large. In the next section, we apply this result to establish a stronger version of Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales"). This result also allows us to develop other types of probability inequalities for adapted sequences of random matrices; see the technical report for additional details.

### Theorem 2.3 (Master Tail Bound for Adapted Sequences)

Consider an adapted sequence $\{\mathbf{X}_{k}\}$ and a previsible sequence $\{\mathbf{V}_{k}\}$ of self-adjoint matrices with dimension $d$. Assume these sequences satisfy the relations where the function $g:{{(0,\infty)}\rightarrow{\lbrack 0,\infty\rbrack}}$. In particular, the hypothesis (2.3. ‣ 2.3. A Tail Bound for Adapted Sequences ‣ 2. Tail Bounds via Martingale Methods ‣ Freedman’s Inequality for Matrix Martingales")) holds when Define the partial sum processes Then, for all ${t,w} \in {\mathbb{R}}$,

### Proof

To begin, note that the cgf hypothesis (2.3. ‣ 2.3. A Tail Bound for Adapted Sequences ‣ 2. Tail Bounds via Martingale Methods ‣ Freedman’s Inequality for Matrix Martingales")) holds in the presence of (2.4. ‣ 2.3. A Tail Bound for Adapted Sequences ‣ 2. Tail Bounds via Martingale Methods ‣ Freedman’s Inequality for Matrix Martingales")) because the logarithm is an operator monotone function \[, Ch. V\].

The overall proof strategy is identical with the stopping-time technique used by Freedman. Fix a positive parameter $\theta$, which we will optimize later. Following the discussion in §2.2, we introduce the random process $S_{k}:={G_{\theta}{({\mathbf{Y}}_{k},{\mathbf{W}}_{k})}}$. Lemma 2.1 implies that $\{ S_{k}\}$ is a positive supermartingale with initial value $d$. These simple properties of the auxiliary random process distill all the essential information from the hypotheses of the theorem.

Define a stopping time $\kappa$ by finding the first time instant $k$ when the maximum eigenvalue of the partial sum process reaches the level $t$ even though the sum of cgf bounds has maximum eigenvalue no larger than $w$.

When the infimum is empty, the stopping time $\kappa = \infty$. Consider a system of exceptional events: Construct the event $E:={\bigcup_{k = 0}^{\infty}E_{k}}$ that one or more of these exceptional situations takes place. The intuition behind this definition is that the partial sum ${\mathbf{Y}}_{k}$ is typically not large unless the process $\{{\mathbf{X}}_{k}\}$ has varied substantially, a situation that the bound on ${\mathbf{W}}_{k}$ disallows. As a result, the event $E$ is rather unlikely.

We are prepared to estimate the probability of the exceptional event. First, note that $\kappa < \infty$ on the event $E$. Therefore, Lemma 2.2 provides a conditional lower bound for the process $\{ S_{k}\}$ at the stopping time $\kappa$: Since ${{\mathbb{E}}S_{k}} \leq d$ for each (finite) index $k$, We require the fact that $S_{\kappa}$ is positive to justify these inequalities. Rearrange the relation to obtain Minimize the right-hand side with respect to $\theta$ to complete the main part of the argument. ∎

## Proof of Freedman's Inequality

In this section, we use the general martingale deviation bound, Theorem 2.3. ‣ 2.3. A Tail Bound for Adapted Sequences ‣ 2. Tail Bounds via Martingale Methods ‣ Freedman’s Inequality for Matrix Martingales"), to prove a stronger version of Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales").

### Theorem 3.1

Consider an adapted sequence $\{\mathbf{X}_{k}\}$ of self-adjoint matrices with dimension $d$ that satisfy the relations Define the partial sums Then, for all $t \geq 0$ and $\sigma^{2} > 0$, The function ${h{(u)}}:={{{({1 + u})}{\log{({1 + u})}}} - u}$ for $u \geq 0$.

Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") follows easily from this result.

### Proof of Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") from Theorem 3.1

To derive Theorem 1.2. ‣ 1.4. Freedman’s Inequality for Matrices ‣ 1. An Introduction to Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales"), we note that the difference sequence of $\{{\mathbf{X}}_{k}\}$ a matrix martingale $\{{\mathbf{Y}}_{k}\}$ satisfies the conditions of Theorem 3.1 and the martingale can be expressed using partial sums of the difference sequence. Finally, we apply the numerical inequality which we obtain by comparing derivatives. ∎

### Demonstration of Theorem 3.1

We conclude with the proof of Theorem 3.1. The argument depends on the following estimate for the moment generating function of a zero-mean random matrix whose eigenvalues are uniformly bounded. See \[, Lem. 6.7\] for the proof.

### Lemma 3.2 (Freedman mgf)

Suppose that $\mathbf{X}$ is a random self-adjoint matrix that satisfies The main result follows quickly from this lemma.

### Proof of Theorem 3.1

We assume that $R = 1$; the general result follows by re-scaling since ${\mathbf{Y}}_{k}$ is 1-homogeneous and ${\mathbf{W}}_{k}$ is 2-homogeneous. Invoke Lemma 3.2. ‣ 3.1. Demonstration of Theorem 3.1 ‣ 3. Proof of Freedman’s Inequality ‣ Freedman’s Inequality for Matrix Martingales") conditionally to see that Theorem 2.3. ‣ 2.3. A Tail Bound for Adapted Sequences ‣ 2. Tail Bounds via Martingale Methods ‣ Freedman’s Inequality for Matrix Martingales") now implies that The infimum is achieved when $\theta = {\log{({1 + {t/\sigma^{2}}})}}$. Finally, note that the norm of a positive-semidefinite matrix, such as ${\mathbf{W}}_{k}$, equals its largest eigenvalue. ∎
