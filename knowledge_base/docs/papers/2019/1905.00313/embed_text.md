## Introduction

Scaleable optimization for machine learning is based entirely on first order gradient methods. Besides the age-old method of stochastic approximation, three accelerated methods have proved their practical and theoretical significance: Nesterov acceleration, variance reduction and adaptive learning-rate/regularization.

Adaptive choices of step sizes allow optimization algorithms to accelerate quickly according to the local curvature and smoothness of the optimization landscape. However, in theory, there are few parameter free algorithms, and, in practice, there are many search heuristics utilized.

Let us examine this question of parameter free, adaptive learning rates for one of the most standard algorithms, namely the gradient descent method: Although this class of algorithms is not optimal in all settings (i.e. the aforementioned accelerations can be applied), it is fundamental, and we may ask what are optimal known rates along with the optimal step size choices are for this particular algorithm. Here, Table 1 shows the best known rates for gradient descent in the standard regimes: general convex (non-smooth with bounded sub-gradients); $\beta$-smooth; $\alpha$-strongly-convex; and $\beta$-smooth&$\alpha$-strongly convex (see for more details).

From a practical perspective these step size settings are unfortunately disparate in various regimes: ranging from rapidly decaying at $\eta_{t} = {O{(\frac{1}{\alphat})}}$ to moderately decaying at $\eta_{t} = {O{(\frac{1}{\sqrt{t}})}}$ to a constant $\eta_{t} = \frac{1}{\beta}$ (see for more details).

This work: We show that a single (and simple) choice of a step size schedule gives, simultaneously, the optimal convergence (among the class of gradient descent algorithms) in all these regimes, without knowing these parameters in advance. Perhaps surprisingly, this choice is that prescribed, who argued that this choice was optimal for the non-smooth, convex case (marked as "convex" in Table 1, see also). $e^{- {\frac{\beta}{\alpha}T}}$ Table 1: Standard convergence rates of gradient descent in convex optimization problems. Error denotes f (xt) − f (x⋆) of a first order methods as a function of the number of iterations. Step Size is the standard learning rate schedule used to obtain this rate. Dependence on other parameters, namely the Lipchitz constant and initial distance to the objective, is omitted.

## Convexity Preliminaries

We consider the minimization of a continuous convex function over Euclidean space $f:{{\mathbb{R}}^{d}\mapsto{\mathbb{R}}}$ by an iterative gradient-based method. We say that $f$ is $\alpha$-strongly convex if and only if ${\forall\mathbf{x}},\mathbf{y}$: We say that $f$ is $\beta$ smooth if and only if ${\forall\mathbf{x}},\mathbf{y}$: The following notation is used throughout: $\mathbf{x}^{\star} = {{\arg\min}_{\mathbf{x} \in {\mathbb{R}}^{d}}\left\{ {f{(\mathbf{x})}} \right\}}$ - optimum ${h{(\mathbf{x}_{t})}} = h_{t} = {{f{(\mathbf{x}_{t})}} - {f{(\mathbf{x}^{\star})}}}$ - sub-optimality gap of the iterate $d_{t} = {\|{\mathbf{x}_{t} - \mathbf{x}^{\star}}\|}$ - Euclidean distance of the iterate. $\nabla_{t} = {{\nabla f}{(\mathbf{x}_{t})}}$ - gradient of the iterate. ${\|\nabla_{t}\|}^{2}$ denotes squared Euclidean norm.

The following are basic properties for $\alpha$-strongly-convex functions and/or $\beta$-smooth functions (proved for completeness in Lemma 4): The following standard lemma is at the heart of much of the analysis of first order convex optimization.

### Lemma 1

The sequence of iterates produced by projected gradient descent (equation 1) satisfies:

### Proof

By algorithm definition we have, where we have used properties of convexity in the last step. ∎

## Main Results

argued that, in a sense, the optimal step size choice of $\eta_{t}$ should decrease the upper bound on $d_{t + 1}^{2}$ as fast as possible. This choice is: which leads to a decrease of $d_{t}^{2}$: Note that this choice utilizes knowledge of $f{(\mathbf{x}^{\star})}$, since $h_{t} = {{f{(\mathbf{x}_{t})}} - {f{(\mathbf{x}^{\star})}}}$. showed that this choice was optimal for non-smooth convex optimization (i.e. for bounded gradients). Our first result shows that this step size schedule (which knows $f{(\mathbf{x}^{\star})}$) achieves the min of the best known bounds in all the standard parameter regimes (among the class of projected gradient descent algorithms). Assume ${\|\nabla_{t}\|} \leq G$, and define:

### Theorem 1

(GD with the Polyak Step Size) Algorithm 1 attains the following regret bound after $T$ steps: 1: Input: time horizon T, x0 3: Set $\eta_{t} = \frac{h_{t}}{{\|\nabla_{t}\|}^{2}}$ 6: Return $\overline{\mathbf{x}} = \mathbf{x}_{t^{\star}}$ where t⋆ = arg min t < T{f (xt)}. Algorithm 1 GD with the Polyak stepsize Without knowledge of the optimal function value $f{(\mathbf{x}^{\star})}$, our second main result shows that all we need is a lower bound ${\overset{\sim}{f}}_{0} \leq {f{(\mathbf{x}^{\star})}}$, and we can do nearly as well as the exact Polyak step size method (up to a $\log$ factor in ${f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{0}$). Note that it is often the case that ${\overset{\sim}{f}}_{0} = 0$ is a valid lower bound (e.g. in empirical risk minimization settings).

### Theorem 2

(The Adaptive Polyak Step Size) Assume a lower bound ${\overset{\sim}{f}}_{0} \leq {f{(\mathbf{x}^{\star})}}$; that $K = {1 + {\lceil{2{\log\frac{{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{0}}{B_{T}}}}\rceil}}$. Algorithm 3 returns an $\overline{\mathbf{x}}$ such that: Furthermore, the number of gradient descent updates made by the algorithm is at most $T \cdot {({1 + {\lceil{2{\log\frac{{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{0}}{B_{T}}}}\rceil}})}$.

In other words, this algorithms makes at most $O{({T \cdot {\log\frac{{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{0}}{B_{T}}}})}$ gradient updates to get $B_{T}$ error, while the exact Polyak stepsize uses $T$ updates (to obtain $B_{T}$ error). The subtlety in the construction is that even with a initial lower bound on ${\overset{\sim}{f}}_{0}$, the values $f{(\mathbf{x}_{t})}$ are only upper bounds. However, Algorithm 3 and its proof shows how either the lower bound can be refined or, if not, the algorithm will succeed. Note that Algorithm 3 always call the subroutine Algorithm 2 starting at the same $x_{0}$.

### Analysis: the exact case

1: Input: time horizon T, x0, lower bound $\overset{\sim}{f} \leq {f{(\mathbf{x}^{\star})}}$. 3: Set $\eta_{t} = \frac{{f{(\mathbf{x}_{t})}} - \overset{\sim}{f}}{2{\|\nabla_{t}\|}^{2}}$ 6: Return $\overline{\mathbf{x}} = \mathbf{x}_{t^{\star}}$ where t⋆ = arg min t < T{f (xt)}. Algorithm 2 GD with a lower bound 1: Input: time horizon T, number of epochs K, x0, value ${\overset{\sim}{f}}_{0} \leq {f{(\mathbf{x}^{\star})}}$. 3: Let ${\overline{\mathbf{x}}}_{k}$ be the output of Algorithm 2 using input $\mathbf{x}_{0},T,{\overset{\sim}{f}}_{k}$. 4: Update ${\overset{\sim}{f}}_{k + 1}\leftarrow\frac{{f{({\overline{\mathbf{x}}}_{k})}} + \overset{\sim}{f_{k}}}{2}$ 6: Return ${\overline{\mathbf{x}}}_{k^{\star}}$ where $k^{\star} = {{\arg\min}_{k < K}{\{{f{({\overline{\mathbf{x}}}_{k})}}\}}}$. Algorithm 3 Adaptive Polyak Theorem 1 directly follows from the following lemma. It is helpful for us to state this lemma in a more general form, where, for $0 \leq \gamma \leq 1$, we define $R_{T,\gamma}$ as follows:

### Lemma 2

For $0 \leq \gamma \leq 1$, suppose that a sequence $\mathbf{x}_{0},{\ldots\mathbf{x}_{t}}$ satisfies: then for $\overline{\mathbf{x}} = \mathbf{x}_{t^{\star}}$, where $t^{\star} = {{\arg\min}_{t < T}{\{{f{(\mathbf{x}_{t})}}\}}}$,

### Proof

The proof analyzes different cases: For convex functions with gradient bound $G$, Summing up over $T$ iterations, and using Cauchy-Schwartz, we have For smooth functions, equation implies: For strongly convex functions, equation implies: In other words, ${d_{t + 1}^{2} \leq {d_{t}^{2}{({1 - {\gamma\frac{\alpha^{2}d_{t}^{2}}{4G^{2}}}})}}}.$ Defining $a_{t}:={\gamma\frac{4\alpha^{2}d_{t}^{2}}{G^{2}}}$, we have: This implies that $a_{t} \leq \frac{1}{t + 1}$, which can be seen by induction^11^1That $a_{0} \leq 1$ follows from equation. For $t = 1$, $a_{1} \leq \frac{1}{2}$ since $a_{1} \leq {a_{0}{({1 - a_{0}})}}$ and $0 \leq a_{0} \leq 1$. For the induction step, $a_{t} \leq {a_{t - 1}{({1 - a_{t - 1}})}} \leq {\frac{1}{t}{({1 - \frac{1}{t}})}} = \frac{t - 1}{t^{2}} = {\frac{1}{t + 1}{(\frac{t^{2} - 1}{t^{2}})}} \leq \frac{1}{t + 1}$.. The proof is completed as follows^22^2This assumes $T$ is even. $T$ odd leads to the same constants.: Thus, there exists a $t$ for which $h_{t}^{2} \leq \frac{G^{4}}{\gamma^{2}\alpha^{2}T^{2}}$. Taking the square root completes the claim.

For both strongly convex and smooth: This completes the proof of all cases. ∎

### Analysis: the adaptive case

The proof of Theorem 2 rests on the following lemma which shows that, given a lower bound on the objective, the subroutine in Algorithm 3 either returns a near-optimal point with desired precision or a tighter lower bound.

### Lemma 3

Assume ${\|\nabla_{t}\|} \leq G$. With input $T$, $\mathbf{x}_{0}$, and $\overset{\sim}{f}$ where $\overset{\sim}{f} \leq {f{(\mathbf{x}^{\star})}}$, Algorithm 2 returns a point $\overline{\mathbf{x}}$ such that one of the following holds: ${h{(\overline{\mathbf{x}})}} \leq R_{T,\frac{1}{2}}$ For ${\overset{\sim}{f}}_{+}:=\frac{{f{(\overline{\mathbf{x}})}} + \overset{\sim}{f}}{2}$,

### Proof

Due to that $\overset{\sim}{f}$ is a lower bound, we have that We will consider two cases. First, suppose that held for $T$ steps. For this case, by Lemma 1, using the assumed upper bound on $\eta_{t}$ in the second step and the lower bound in the last step. By Lemma 2, we can take $\gamma = {1/2}$ and we have that ${\min_{t < T}h_{t}} \leq R_{T,\frac{1}{2}}$.

Now suppose there exists a time $t^{\ast}$ where Equation 5 fails to hold. Hence, for some iteration, After rearranging, we have using the definition of $\overline{\mathbf{x}}$ and the definition of ${\overset{\sim}{f}}_{+}$. Hence, ${{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{+}} \geq 0$. In addition, we have which completes the proof. ∎ Now the proof Theorem 2 follows.

### Proof

(of Theorem 2) Note $R_{T,\frac{1}{2}} \leq {2B_{T}}$. Suppose that ${{f{({\overline{\mathbf{x}}}_{k})}} - {f{(\mathbf{x}^{\star})}}} \geq R_{T,\frac{1}{2}}$ for all $k \leq {K - 1}$, else the proof would be complete. By Lemma 3, we have that ${{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{k}} \leq {{({1/2})}^{k}{({{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{0}})}}$ and that $0 \leq {{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{k}}$, for all $k \in {\{ 1,\ldots,K\}}$. Hence, for $k = {K - 1} = {\lceil{2{\log\frac{{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{0}}{B_{T}}}}\rceil}$, we have ${{f{(\mathbf{x}^{\star})}} - {\overset{\sim}{f}}_{K - 1}} \leq B_{T}$. By construction ${\overset{\sim}{f}}_{K} = \frac{{f{({\overline{\mathbf{x}}}_{K - 1})}} + {\overset{\sim}{f}}_{K - 1}}{2}$, which implies: which completes the proof. ∎
