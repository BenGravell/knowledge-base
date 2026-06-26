## Introduction

It is recognized that algorithms for reinforcement learning such as TD- and Q-learning can be slow to converge. The poor performance of Watkins' Q-learning algorithm was first quantified , and since then many papers have appeared with proposed improvements, such as.

An emphasis in much of the literature is computation of finite-time PAC (probably almost correct) bounds as a metric for performance. Explicit bounds were obtained in for Watkins' algorithm, and in for the "speedy" Q-learning algorithm that was introduced by these authors. A general theory is presented in for stochastic approximation algorithms.

In each of the models considered in prior work, the update equation for the parameter estimates can be expressed in which $\{\alpha_{n}\}$ is a positive gain sequence, and $\{\Delta_{n}\}$ is a martingale difference sequence. This representation is critical in analysis, but unfortunately is not typical in reinforcement learning applications outside of these versions of Q-learning. For Markovian models, the usual transformation used to obtain a representation similar to results in an error sequence $\{\Delta_{n}\}$ that is the sum of a martingale difference sequence and a telescoping sequence. It is the telescoping sequence that prevents easy analysis of Markovian models.

This gap in the research literature carries over to the general theory of Markov chains. Examples of concentration bounds for i.i.d. sequences or martingale-difference sequences include the finite-time bounds of Hoeffding and Bennett. Extensions to Markovian models either offer very crude bounds, or restrictive assumptions; this remains an active area of research.

In contrast, asymptotic theory for stochastic approximation (as well as general state space Markov chains) is mature. Large Deviations or Central Limit Theorem (CLT) limits hold under very general assumptions.

The CLT will be a guide to algorithm design in the present paper. For a typical stochastic approximation algorithm, this takes the following form: denoting $\{{{{\overset{\sim}{\theta}}_{n}:=\theta_{n}} - \theta^{\ast}}:{n \geq 0}\}$ to be the error sequence, under general conditions the scaled sequence $\{{\sqrt{n}{\overset{\sim}{\theta}}_{n}}:{n \geq 1}\}$ converges in distribution to a Gaussian distribution, $\mathcal{N}{(0,\Sigma_{\theta})}$. Typically, the scaled covariance is also convergent: The limit is known as the asymptotic covariance.

An asymptotic bound such as may not be satisfying for practitioners of stochastic optimization or reinforcement learning, given the success of finite-$n$ performance bounds in prior research. There are however good reasons to apply this asymptotic theory in algorithm design: The asymptotic covariance $\Sigma_{\theta}$ has a simple representation as the solution to a Lyapunov equation. It is easily improved or optimized by design.

As shown in examples in this paper, the asymptotic covariance is often a good predictor of finite-time performance, since the CLT approximation is accurate for reasonable values of $n$.

Two approaches are known for optimizing the asymptotic covariance. First is the remarkable averaging technique of Polyak and Juditsky and Ruppert ( provides an accessible treatment in a simplified setting). Second is what we will call Stochastic Newton-Raphson, based on a special choice of matrix gain for the algorithm. The second approach underlies the analysis of the averaging approach.

We are not aware of theory that distinguishes the performance of Polyak-Ruppert averaging as compared to the Stochastic Newton-Raphson method. It is noted in that the averaging approach often leads to very large transients, so that the algorithm should be modified (such as through projection of parameter updates). This may explain why averaging is not very popular in practice. In our own numerical experiments it is observed that the rate of convergence of CLT in this case is slow when compared to matrix gain methods.

In addition to accelerating the convergence rate of standard algorithms for reinforcement learning, it is hoped that this paper will lead to entirely new algorithms. In particular, there is little theory to support Q-learning in non-ideal settings in which the optimal "$Q$-function" does not lie in the parameterized function class. Convergence results have been obtained for a class of optimal stopping problems, and for deterministic models. There is now intense practical interest, despite an incomplete theory. A stronger supporting theory will surely lead to more efficient algorithms.

### Contributions

A new class of algorithms is proposed, designed to more accurately mimic the classical Newton-Raphson algorithm. It is based on a two time-scale stochastic approximation algorithm, constructed so that the matrix gain tracks the gain that would be used in a deterministic Newton-Raphson method.

The application of this approach to reinforcement learning results in the new Zap Q-learning algorithms. A full analysis is presented for the special case of a complete parameterization (similar to the setting of Watkins' original algorithm). It is found that the associated ODE has a remarkable and simple representation, which implies consistency under suitable assumptions. Extensions to non-ideal parameterized settings are also proposed, and numerical experiments show dramatic variance reductions. Moreover, results obtained from finite-$n$ experiments show close solidarity with asymptotic theory.

The potential complexity introduced by the matrix gain is not of great concern in many cases, because of the dramatically acceleration in the rate of convergence. Moreover, the main contribution of this paper is not a single algorithm but a class of algorithms, wherein the computational complexity can be dealt with separately. For example, in a parameterized setting, the basis functions can be intelligently pruned via random projection.

The remainder of the paper is organized as follows. Background on computing and optimizing the asymptotic covariance is contained in Section 2. Application to Q-learning, and theory surrounding the new Zap Q-learning algorithm is developed in Section 3. Numerical results are surveyed in Section 4, and conclusions are contained in Section 5. The proofs of the main results are contained in the Appendix; the final page contains Table 2 containing a list of notation.

## Stochastic Newton Raphson and TD-Learning

This first section is largely a tutorial on reinforcement learning. It is shown that the LSTD($\lambda$) learning algorithm of is an instance of the "SNR algorithm", in which there is only one time-scale for the parameter and matrix-gain updates. The original motivation for the LSTD($\lambda$) algorithm had no connection with asymptotic variance. It was shown later in that the LSTD ($\lambda$) algorithm is the minimum asymptotic variance version of the TD ($\lambda$) algorithm of.

The focus is on fixed point equations associated with an uncontrolled Markov chain, denoted ${\mathbf{X}} = {\{ X_{n}:{n = {0,1,\ldots}}\}}$, on a measurable state space $(\mathsf{X},{\mathcal{B}{(\mathsf{X})}})$. It is assumed to be $\psi$-irreducible and aperiodic. In Section 3 we specialize to a finite state space.

In control applications and analysis of learning algorithms, it is necessary to construct a Markov chain $\mathbf{\Phi}$, of which $\mathbf{X}$ is a component. Other components may be an input process, or a sequence of "eligibility vectors" that arise in TD-learning. It will be assumed throughout that there is a unique stationary realization of $\mathbf{\Phi}$, with unique marginal distribution denoted $\varpi$.

### Motivation from SA & ODE fundamentals

The goal of stochastic approximation is to compute the solution ${\overline{f}{(\theta^{\ast})}} = 0$ for a function $\overline{f}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$. If the function is easily evaluated, then successive approximation can be used, and under stronger conditions the Newton-Raphson algorithm: Under general conditions the convergence rate of is quadratic (much faster than geometric), which is not generally true of successive approximation.

Stochastic approximation is itself an approximation of successive approximation. It is assumed that ${\overline{f}{(\theta)}} = {\mathsf{E}{\lbrack{f{(\theta,\Phi)}}\rbrack}}$, where $f:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{d}}$ and $\Phi$ is a random variable with distribution $\varpi$. The standard stochastic approximation algorithm is defined by For simplicity it is assumed that $\mathbf{\Phi}$ is the stationary realization of the Markov chain. It is always assumed that the scalar gain sequence $\{\alpha_{n}\}$ is non-negative, and satisfies: While convergent under general conditions, the rate of convergence of can often be improved dramatically through the introduction of a matrix gain. This is explained first in a simple linear setting.

### Optimal covariance for linear stochastic approximation

In many applications of reinforcement learning we arrive at a linear recursion of the form where $A_{n + 1} = {A{(\Phi_{n + 1})}}$ is a $d \times d$ matrix and $b_{n + 1} = {b{(\Phi_{n + 1})}}$ is a $d \times 1$ vector, $n \geq 0$. Let $A,b$ denote the respective steady-state means: It is assumed throughout this section that $A$ is Hurwitz: the real part of each eigenvalue is negative. Under this assumption, and subject to mild conditions on $\mathbf{\Phi}$, it is known that $\{\theta_{n}\}$ converges with probability one to $\theta^{\ast} = {A^{- 1}b}$.

Convergence of the recursion will be assumed henceforth. It is also assumed that the gain sequence is given by $\alpha_{n} = {1/n}$, $n \geq 1$.

Under general conditions, the asymptotic covariance $\Sigma_{\theta}$ defined in is the non-negative semi-definite solution to the Lyapunov equation: A solution is guaranteed only if each eigenvalue of $A$ has real part that is strictly less than $- {1/2}$. If there exists an eigenvalue which does not satisfy this property, then under general conditions the asymptotic covariance is infinity (see Thm. 2.1). Hence the Hurwitz assumption must be strengthened to ensure that the asymptotic covariance is finite.

The matrix $\Sigma_{\Delta}$ is obtained as follows: based, the error sequence $\{{{\overset{\sim}{\theta}}_{n} = {\theta_{n} - \theta^{\ast}}}\}$ evolves according to a deterministic linear system driven by "noise": in which $\mathbf{\Delta}$ is the sum of three terms: with ${\overset{\sim}{A}}_{n + 1} = {A_{n + 1} - A}$, ${\overset{\sim}{b}}_{n + 1} = {b_{n + 1} - b}$. The third term vanishes with probability one. The "noise covariance matrix" $\Sigma_{\Delta}$ has the following two equivalent forms: in which $S_{T} = {\sum_{n = 1}^{T}\Delta_{n}}$, and where the expectation is in steady-state. It is assumed that the CLT holds for sample-averages of the noise sequence: where the limit is in distribution. This is a mild requirement when $\mathbf{\Phi}$ is Markovian.

A finite asymptotic covariance can be guaranteed by increasing the gain: choose $\alpha_{n} = {g/n}$, with $g > 0$ sufficiently large so that the eigenvalues of $gA$ satisfy the required bound. More generally, a matrix gain can be introduced: in which $G$ is a $d \times d$ matrix. Provided the matrix $GA$ satisfies the eigenvalue bound, the corresponding asymptotic covariance $\Sigma_{\theta}^{G}$ is finite and solves a modified Lyapunov equation: The choice $G^{\ast} = {- A^{- 1}}$ is analogous to the gain used in the Newton-Raphson algorithm. With this choice, the asymptotic covariance is finite and given by It is a remarkable fact that this choice is optimal in the strongest possible statistical sense: For any other gain $G$, the two asymptotic covariance matrices satisfy That is, the difference $\Sigma_{\theta}^{G} - \Sigma^{\ast}$ is positive semi-definite.

The following theorem summarizes the results on the asymptotic covariance for the matrix-gain recursion. The proof is contained in Section A.1 of the Appendix.

### Theorem 2.1

Suppose that the eigenvalues of $GA$ lie in the strict left half plane, and that the noise sequence satisfies the CLT with finite covariance $\Sigma_{\Delta}$. Then, the stochastic approximation recursion defined in is convergent, and the following also hold: Suppose that $(\lambda,v)$ is an eigenvalue-eigenvector pair satisfying where $v^{\dagger}$ denotes the conjugate transpose of the vector $v$. Then and consequently, the asymptotic covariance $\Sigma_{\theta}^{G}$ is not finite.

If all the eigenvalues of $GA$ satisfy ${\text{Re}{(\lambda)}} < {- {1/2}}$, then the corresponding asymptotic covariance $\Sigma_{\theta}^{G}$ is finite, and can be obtained as the solution to the Lyapunov equation For any matrix gain $G$ the asymptotic covariance admits the lower bound This lower bound is achieved using $G^{\ast}:= - A^{- 1}$. $\sqcap$$\sqcup$ Thm. 2.1 inspires improved algorithms in many settings. The first, which is essentially known, e.g. \[27, 14, p. 331\], will be called stochastic Newton-Raphson (SNR).

### Stochastic Newton-Raphson

This algorithm is obtained by estimating the mean $A$ simultaneously with the estimation of $\theta^{\ast}$: recursively define where $\theta_{0}$ and ${\hat{A}}_{1}$ are initial conditions.

If the steady-state mean $A$ (defined in ) is invertible, then ${\hat{A}}_{n}$ is invertible for all $n$ sufficiently large.

The sequence $\{{n{\hat{A}}_{n}\theta_{n}}:{n \geq 0}\}$ admits a simple recursive representation that implies the following alternative representation of the SNR parameter estimates:

### Proposition 2.2

Suppose ${\hat{A}}_{n}$ is invertible for each $n \geq 1$. Then, the sequence of estimates $\{\theta_{n}\}$ obtained using are identical to the direct estimates: Based on the proposition, it is obvious that the SNR algorithm is consistent whenever the Law of Large Numbers holds for the sequence $\{ A_{n},b_{n}\}$. Under the assumptions of Thm. 2.1, the resulting asymptotic covariance is identical to what would be obtained with the constant matrix gain $G^{\ast} = {- A^{- 1}}$.

Algorithm design in this linear setting is simplified in part because $\overline{f}$ is an affine function of $\theta$, so that the gain $G_{n}$ appearing in the standard Newton-Raphson algorithm does not depend upon the parameter estimates $\{\theta_{k}\}$. However, an ODE analysis of the SNR algorithm suggests that even in this linear setting, the dynamics are very different from its deterministic counterpart: | | $\frac{d}{dt}x_{t}$ | $= {- {\mathcal{A}_{t}^{- 1}\left\lbrack {{Ax_{t}} - b} \right\rbrack}}$ | | \(16\) | | | $\frac{d}{dt}\mathcal{A}_{t}$ | $= {{- \mathcal{A}_{t}} + A}$ | | | While evidently $\mathcal{A}_{t}$ converges to $A$ exponentially fast in the linear model, with a poor initial condition we might expect poor transient behavior.

In extending the SNR algorithm to a nonlinear stochastic approximation algorithm, an ODE approximation of the form will be possible under general conditions, but the matrix $A$ will depend on $\theta$. In addition to poor transient behavior, the coupled equations may be difficult to analyze. And, just as in the linear model, the continuous time system looks very different from the deterministic Newton-Raphson recursion.

The next class of algorithms are designed so that the associated ODE more closely matches the deterministic recursion.

### Zap Stochastic Newton-Raphson

This is a two time-scales algorithm with a higher step-size for the matrix recursion. In the linear setting of this section, it is defined by the variant of: | | ${\hat{A}}_{n + 1}$ | $= {{\hat{A}}_{n} + {\gamma_{n + 1}\left\lbrack {A_{n + 1} - {\hat{A}}_{n}} \right\rbrack}}$ | | | It is different from the original Stochastic Newton-Raphson algorithm because of the two time-scale construction: The second step-size sequence $\{\gamma_{n + 1}\}$ is non-negative, satisfies, and also We again take $\alpha_{n} = {1/n}$, $n \geq 1$.

The asymptotic covariance is again optimal. The ODE associated with the sequence $\{\theta_{n}\}$ is far simpler, and exactly matches the usual Newton-Raphson dynamics: This simplicity is also revealed in application to Q-learning, in which $A$ depends on the parameter.

A key point to note here is that the Zap version of the SNR algorithm plays a significant role in analysis as well as in performance improvement of general non-linear function approximation problems. We briefly discuss these in the following.

### Zap SNR for non-linear stochastic approximation

Consider a stochastic approximation algorithm of the form with ${\overline{f}{(\theta)}} = {\mathsf{E}{\lbrack{f{(\theta,\Phi)}}\rbrack}}$, a non-linear function of the parameter vector $\theta$. The ODE of the two algorithms: SNR and Zap-SNR look significantly different in this case; it is found that this difference is reflected in the rate of convergence of the stochastic recursion (as we will see in the case of Q-learning). The SNR algorithm is essentially the same as: Note that the function ${\nabla f}{(\theta_{n},\phi_{n + 1})}$ may or may not be readily accessible, and this is application specific. In the case of Q-learning with linear function approximation, though the function $f$ is iteslf non-linear in $\theta$, $\nabla f$ is readily computable.

The ODE for the pair of recursions once again will be similar to: | | $\frac{d}{dt}\mathcal{A}_{t}$ | $= {{- {{\nabla\overline{f}}{(\theta_{t})}}} + A}$ | | | The Zap-SNR algorithm is a generalization of: | | ${\hat{A}}_{n + 1}$ | $= {{\hat{A}}_{n} + {\gamma_{n + 1}\left\lbrack {{{\nabla f}{(\theta_{n},\phi_{n + 1})}} - {\hat{A}}_{n}} \right\rbrack}}$ | | | where once again the step-size sequence $\{\gamma_{n}\}$ satisfies, and. Similar to, the ODE of this algorithm is identical to the deterministic Newton-Raphson dynamics: The general convergence and stability analysis of both and is open. In Section 3 we show that when applied to Q-learning, the algorithms do converge under certain technical conditions. However, the assumptions under which the single time-scale algorithm converges is far more restrictive than the assumptions under which the the two-time-scale algorithm converges.

### Dealing with complexity: An $O$($d$) Zap-SNR algorithm

It is common to discard the idea of second order methods because of their computational complexity. Before we move on to the specific applications in Reinforcement Learning, we propose an enhancement of the SNR algorithms that will result in complexity that is comparable to first order methods.

We believe that we have convinced the readers that the two-timescale Zap-SNR algorithm is of more interest to us (we will make this more precise in Section 3), and hence restrict to extensions of this algorithm here.

It is assumed that there is no complexity in "calculating" the gradient function ${\nabla f}{( \cdot, \cdot )}$, and that it is readily available. This is not be true in all applications, but holds in the applications of interest in this paper. Under these assumptions, computational complexity arises from the operations that are performed in manipulating these quantities.

The per-iteration complexity of the first order algorithm is $O{(d)}$, since $\theta \in {\mathbb{R}}^{d}$. If the algorithm is run for $T$ iterations (assuming we have a data sequence of length $T$), the total complexity is $O{({dT})}$. The per iteration complexity in the case of the Zap-SNR algorithm is $O{(d^{2})}$, because it involves the product of a matrix inverse (of dimension $d \times d$) and a vector (of dimension $d \times 1$). The total complexity of the algorithm after running for $T$ iterations is $O{({Td^{2}})}$.

The essential idea behind the $O{(d)}$ Zap-SNR algorithm is to perform the $O{(d^{2})}$ complexity steps only once every $N \geq d$ iterations, so that the total computational complexity for a data sequence of length $T$ is $O{(\frac{Td^{2}}{N})}$; essentially resulting in the complexity of the first order method if $N = d$. This is done by "batching" the data sequence into mini-sequences of length $N$, and applying recursions for each batch as follows: For $i \geq 0$ | | ${\hat{A}}_{{({i + 1})}N}$ | ${= {{\hat{A}}_{iN} + {{\hat{\gamma}}_{i + 1}\left\lbrack {{{\nabla\hat{f}}{(\theta_{iN})}} - {\hat{A}}_{iN}} \right\rbrack}}},$ | | | The first two definitions in (25 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) are straightforward; the expression for ${\hat{\gamma}}_{{i + 1},N}$ is obtained in such a way that the recursions in (24 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) very closely resemble the recursions in ^11^1This deserves more explanation and we plan to provide one in a future version of the paper..

A remarkable (but almost obvious) property of the $O{(d)}$ Zap-SNR algorithm (24 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) is that it has the same asymptotic properties (specifically, the asymptotic covariance) as that of the original Zap-SNR algorithm. This once again is made more precise in a future version of the paper. The specific application of this algorithm to Q-learning is discussed in Section 3.7 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning").

### Application to temporal-difference algorithms

The general theory is illustrated here, through application to TD($\lambda$)-learning algorithms.

Let $\{ P^{n}\}$ denote the transition semigroup for the Markov chain $\mathbf{X}$: For each $n \geq 0$, $x \in \mathsf{X}$, and $A \in {\mathcal{B}{(\mathsf{X})}}$, The standard operator-theoretic notation is used for conditional expectation: for any measurable function $f:{\mathsf{X}\rightarrow{\mathbb{R}}}$, In a finite state space setting, $P^{n}$ is the $n$-step transition probability matrix of the Markov chain, and the conditional expectation appears as matrix-vector multiplication: Let $c:{\mathsf{X}\rightarrow{\mathbb{R}}_{+}}$ denote a cost function, and $\beta \in {}$ a discount factor. The discounted-cost value function is defined as $h = {\sum_{n = 0}^{\infty}{\beta^{n}P^{n}c}}$, which is the unique solution to the Bellman equation TD-learning algorithms are designed to obtain approximations of $h$ within a finite-dimensional parameterized class.

Consider the case of a $d$-dimensional linear parameterization. A function $\psi:{\mathsf{X}\rightarrow{\mathbb{R}}^{d}}$ is chosen, which is viewed as a collection of $d$ basis functions. Each vector $\theta \in {\mathbb{R}}^{d}$ is associated with the approximate value function $h^{\theta} = {\sum_{i}{\theta_{i}\psi_{i}}}$. There are two standard criteria for defining optimality of the parameter. Most natural is the minimum norm approach: in which the choice of norm is part of the design of the algorithm. Most common is where the expectation is in steady-state.

In the Galerkin approach, a $d$-dimensional stationary stochastic process $\mathbf{ζ}$ is constructed that is adapted to a stationary realization of $\mathbf{X}$. An algorithm is designed to obtain the vector $\theta^{\ast} \in {\mathbb{R}}^{d}$ that satisfies in which the expectation is again in steady state. The $d$-dimensional stochastic process $\mathbf{ζ}$ is called the sequence of eligibility vectors.

The motivation for the first criterion is clear, but algorithms that solve this problem often suffer from high variance. The Galerkin approach is used because it is simple and generally applicable. Also, if the basis functions are chosen such that $h = h^{\theta^{\bullet}}$ for some $\theta^{\bullet} \in {\mathbb{R}}^{d}$, and if the solution to is unique, then the Galerkin approach will yield the exact solution $h$.

The goal of the TD($\lambda$) learning algorithm is to solve the Galerkin relaxation in which the eligibility vectors are obtained by passing $\{{\psi{(X_{n})}}\}$ through the corresponding first-order low-pass filter: $\zeta_{n + 1} = {{\lambda\beta\zeta_{n}} + {\psi{(X_{n + 1})}}}$, $n \geq 0$. It is always assumed that $\lambda \in {\lbrack 0,1\rbrack}$. It is shown in that the solutions to the Galerkin fixed point equation and the minimum norm problem coincide if $\lambda = 1$, with the norm defined .

### TD($\lambda$) algorithm

For initialization ${\theta_{0},\zeta_{0}} \in {\mathbb{R}}^{d}$, the sequence of estimates are defined recursively: | | $d_{n + 1}$ | $= {{c{(X_{n})}} + {\left\lbrack {{\beta\psi{(X_{n + 1})}} - {\psi{(X_{n})}}} \right\rbrack^{\text{T}}\theta_{n}}}$ | | | The recursion (30 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) can be placed in the form in which $\Phi_{n} = {(X_{n},X_{n - 1},\zeta_{n - 1})}$, and Based on this representation, it can be shown that the TD($\lambda$) algorithm is consistent provided the basis vectors are linearly independent, in the sense that ${\mathsf{E}_{\varpi}{\lbrack{\psi{(X_{n})}\psi{(X_{n})}^{\text{T}}}\rbrack}} > 0$.

It is also easy to construct an example for which the asymptotic covariance is infinite: Take any consistent example, and scale the basis vectors by a small constant $\varepsilon$. Using the basis $\varepsilon\psi$, the resulting matrix $A$ is scaled by $\varepsilon^{2}$. Hence, for sufficiently small $\varepsilon > 0$, each eigenvalue of $A$ will have real part that is strictly greater than $- {1/2}$.

An application of the SNR matrix gain algorithm results in an algorithm with optimal asymptotic covariance. This results in the coupled recursions: where $\alpha_{n} \equiv {1/n}$, for $n \geq 1$.

The following proposition follows directly from Prop. 2.2:

### Proposition 2.3

Suppose that ${\hat{A}}_{n}$ is invertible for all $n \geq 1$. Then, the sequence of parameters obtained using the SNR-TD($\lambda$) algorithm (32 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning"),33 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) coincides with the direct estimates: | | $\theta_{n}$ | ${= {{\hat{A}}_{n}^{- 1}{\hat{b}}_{n}}},$ | | \(34\) | | | ${\hat{A}}_{n} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}{\zeta_{i - 1}\left\lbrack {{\beta\psi{(X_{i})}} - {\psi{(X_{i - 1})}}} \right\rbrack^{\text{T}}}}}$ | ${{{+ {\frac{1}{n}\mathcal{E}_{1}}},{\hat{b}}_{n}} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}{\zeta_{i - 1}c{(X_{i - 1})}}}}},$ | | | where $\mathcal{E}_{1} = {{\hat{A}}_{\text{IC}} - A_{1}}$, ${\hat{A}}_{\text{IC}}$ denoting the matrix ${\hat{A}}_{1}$ in (32 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning"),33 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")), and the sequence of vectors $\{\zeta_{n}\}$ are again defined by $\zeta_{n + 1} = {{\lambda\beta\zeta_{n}} + {\psi{(X_{n + 1})}}}$. $\sqcap$$\sqcup$ It is a remarkable fact that this algorithm is essentially equivalent to the LSTD($\lambda$) algorithm of: The LSTD($\lambda$) algorithm is defined to be (34 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) with $\mathcal{E}_{1} = 0$.

## Q-Learning

The class of algorithms considered next is designed for a controlled Markov model, whose input process is denoted $\mathbf{U}$. It is assumed that the state space $\mathsf{X}$ and the action space $\mathsf{U}$ on which $\mathbf{U}$ evolves are both finite. Denote $\ell = {|\mathsf{X}|}$ and $\ell_{u} = {|\mathsf{U}|}$.

### Notation and assumptions

It is convenient to maintain the operator-theoretic notation used in the uncontrolled setting. There is now a controlled transition matrix that acts on functions $h:{\mathsf{X}\rightarrow{\mathbb{R}}}$ via For any non-anticipative input sequence $\mathbf{U}$ we have ${P_{u}h{(x)}} = {\mathsf{E}{\lbrack{{h{(X_{t + 1})}} \mid {X_{0}^{t},U_{0}^{t}}}\rbrack}}$ on the event $X_{t} = x$ and $U_{t} = u$.

There is a finite number of deterministic stationary policies that are enumerated as $\{\phi^{(i)}:{1 \leq i \leq \ell_{\phi}}\}$, with $\ell_{\phi} = {(\ell_{u})}^{\ell}$. A randomized stationary policy is defined by a pmf $\mu$ on the integers $\{{1 \leq i \leq \ell_{\phi}}\}$ and such that for each $t$, where $\{{\iota{(t)}}\}$ is an i.i.d. sequence on ${\{ 0,1\}}^{\ell_{\phi}}$ satisfying ${\sum_{k}{\iota_{k}{(t)}}} = 1$, and ${\mathsf{P}{\{{{\iota_{k}{(t)}} = 1}\mid X_{0}^{t}\}}} = {\mu{(k)}}$ for all $k$ and $t$.

For any deterministic stationary policy $\phi$, let $S_{\phi}$ denote the substitution operator, defined for any function $q:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{R}}}$ by ${S_{\phi}q{(x)}} = {q{(x,{\phi{(x)}})}}$. If the policy $\phi$ is randomized, of the form, then we denote With $P$ viewed as a single matrix with $\ell \cdot \ell_{u}$ rows and $\ell$ columns, and $S_{\phi}$ viewed as a matrix with $\ell$ rows and $\ell \cdot \ell_{u}$ columns, the following interpretations hold:

### Lemma 3.1

Suppose that $\mathbf{U}$ is defined using a stationary policy $\phi$ (possibly randomized). Then, both $\mathbf{X}$ and the pair process $(\mathbf{X},\mathbf{U})$ are Markovian, and ${P_{\phi}:=S_{\phi}}P$ is the transition matrix for $\mathbf{X}$. $PS_{\phi}$ is the transition matrix for $({\mathbf{X}},{\mathbf{U}})$. $\sqcap$$\sqcup$ A cost function $c:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{R}}}$ is given together with a discount factor $\beta \in {}$. For any (possibly randomized) stationary policy $\phi$, the resulting value function is denoted The minimal value function is denoted $h^{\ast}$, which is the unique solution to the discounted-cost optimality equation (DCOE): The minimizer defines a stationary policy $\phi^{\ast}:{\mathsf{X}\rightarrow\mathsf{U}}$ that is optimal over all input sequences.

The associated "Q-function" is defined to be the term within the brackets, ${{{Q^{\ast}{(x,u)}}:=c}{(x,u)}} + {\betaP_{u}h^{\ast}{(x)}}$. The DCOE implies a similar fixed point equation for the Q-function: in which ${{\underset{¯}{Q}{(x)}}:={\min_{u}Q}}{(x,u)}$ for any function $Q:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{R}}}$.

For any function $q:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{R}}}$, let $\phi^{q}:{\mathsf{X}\rightarrow\mathsf{U}}$ denote an associated policy satisfying for each $x \in \mathsf{X}$. It is assumed to be specified *uniquely* as follows: The fixed point equation becomes In the analysis that follows it is necessary to consider the Q-function associated with all possible cost functions simultaneously: given any function $\varsigma:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{R}}}$, let $\mathcal{Q}{(\varsigma)}$ denote the corresponding solution to the fixed point equation, with $c$ replaced by $\varsigma$. That is, the function $q = {\mathcal{Q}{(\varsigma)}}$ is the solution to the fixed point equation, For a pmf $\mu$ defined on the set of policy indices $\{{1 \leq i \leq \ell_{\phi}}\}$, denote so that $\partial{\mathcal{Q}_{\mu}\varsigma}$ is the "$Q$-function" obtained with the cost function $\varsigma$, and the randomized stationary policy defined by $\mu$ (see also discussion of the SARSA algorithm following the proof of Lemma 3.6). It follows that the functional $\mathcal{Q}$ can be expressed as the minimum over all pmfs $\mu$: There is a single degenerate pmf that attains the minimum for each $(x,u)$ (the optimal stationary policy is deterministic).

### Lemma 3.2

The mapping $\mathcal{Q}$ is a bijection on the set of real-valued functions on $\mathsf{X} \times \mathsf{U}$. It is also piecewise linear, concave and monotone.

### Proof

The fixed point equation defines the Q-function with respect to the cost function $\varsigma$. Concavity and monotonicity hold because $q = {\mathcal{Q}{(\varsigma)}}$ as defined in is the minimum of linear, monotone functions. The existence of an inverse $q\mapsto\varsigma$ follows. $\sqcap$$\sqcup$ A Galerkin approach to approximating $Q^{\ast}$ is formulated as follows: Consider a linear parameterization ${Q^{\theta}{(x,u)}} = {\theta^{\text{T}}\psi{(x,u)}}$, with $\theta \in {\mathbb{R}}^{d}$ and $\psi:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{R}}^{d}}$, and denote ${{\underset{¯}{Q}}^{\theta}{(x)}} = {{\min_{u}Q^{\theta}}{(x,u)}}$. Obtain a $d$-dimensional stationary stochastic process $\mathbf{ζ}$ that is adapted to $({\mathbf{X}},{\mathbf{U}})$, and define $\theta^{\ast}$ to be a solution to where the expectation is in steady-state.

Similar to TD($\lambda$)-learning, a possible approach to estimate $\theta^{\ast}$ is the following:

### Q($\lambda$) algorithm

For initialization ${\theta_{0},\zeta_{0}} \in {\mathbb{R}}^{d}$, the sequence of estimates are defined recursively: The success of this approach has been demonstrated in a few restricted settings, such as optimal stopping problems, deterministic models, and variations of Watkins algorithm that are discussed next.

### Watkins algorithm

The basic Q-learning algorithm of is a particular instance of the Galerkin approach with $\lambda = 0$ in (46 algorithm: ‣ 3.1 Notation and assumptions ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")). The basis functions are taken to be indicator functions: where $\{{(x^{k},u^{k})}:{1 \leq k \leq d}\}$ is an enumeration of all state-input pairs. The goal of this approach is to compute the function $Q^{\ast}$ exactly.

The parameter $\theta$ is identified with the estimate $Q^{\theta}$, and hence $\theta \in {\mathbb{R}}^{d}$ with $d = {\ell \cdot \ell_{u}}$. The basic stochastic approximation algorithm to solve coincides with Watkins algorithm: Only one entry of the approximation is updated at each time point, corresponding to the previous state-input pair $(X_{n},U_{n})$ observed.

Assumption Q1: The input is defined by a randomized stationary policy of the form. The joint process $({\mathbf{X}},{\mathbf{U}})$ is an irreducible Markov chain. That is, it has a unique invariant pmf $\varpi$ satisfying ${\varpi{(x,u)}} > 0$ for each $x,u$. $\sqcap$$\sqcup$ Assumption Q2: The optimal policy $\phi^{\ast}$ is unique. $\sqcap$$\sqcup$ The ODE for stability analysis takes on the following simple form: in which ${{\underset{¯}{q}}_{t}{(x)}} = {{\min_{u}q_{t}}{(x,u)}}$ as defined below. This ODE is stable under Assumption Q1, which then implies that the parameter estimates converge to $Q^{\ast}$ a.s..

Under Assumption Q2 there exists $\varepsilon > 0$ such that This justifies a linearization of the ODE, in which ${\underset{¯}{q}}_{t}$ is replaced by $S_{\phi^{\ast}}q_{t}$.

Although the algorithm is consistent, it should be clear that the asymptotic covariance of this algorithm is typically infinite.

### Theorem 3.3

Suppose that Assumptions Q1 and Q2 hold. Then, the sequence of parameters $\{\theta_{n}\}$ obtained using the Q-learning algorithm converges to $Q^{\ast}$ a.s.. Suppose moreover that the conditional variance of $h^{\ast}{(X_{t})}$ is positive: and ${{({1 - \beta})}{\max_{x,u}\varpi}{(x,u)}} \leq \frac{1}{2}$. Then, in the case $\alpha_{n} \equiv {1/n}$, The assumption ${{({1 - \beta})}{\max_{x,u}\varpi}{(x,u)}} \leq \frac{1}{2}$ is satisfied whenever $\beta \geq \frac{1}{2}$.

The proof of convergence can be found. The proof of infinite asymptotic covariance is given in Section A.2 of the Appendix. An eigenvector for $A$ is constructed with strictly positive entries, and with real eigenvalue satisfying $\lambda \geq {- {1/2}}$. Interpreted as a function $v:{{\mathsf{X} \times \mathsf{U}}\rightarrow{\mathbb{C}}}$, this eigenvector satisfies Assumption ensures that the right hand side is strictly positive, as required in Thm. 2.1 (i).

The recursion for the Q-learning algorithm can be written in the form in which This motivates the introduction of stochastic Newton-Raphson algorithms that are considered next.

### SNR and Zap Q-Learning

For a sequence of $d \times d$ matrices ${\mathbf{G}} = {\{ G_{n}\}}$ and $\lambda \in {\lbrack 0,1\rbrack}$, the matrix-gain Q($\lambda$) algorithm is described as follows:

### $\mathbf{G}$-Q($\lambda$) algorithm

For initialization ${\theta_{0},\zeta_{0}} \in {\mathbb{R}}^{d}$, the sequence of estimates are defined recursively: The special case based on stochastic Newton-Raphson is called the Zap-Q($\lambda$) algorithm: 3: ϕnXn + 1:= arg min uQθn (Xn + 1, u); 4: dn + 1:= c (Xn, Un) + β Qθn (Xn + 1, ϕnXn + 1) − Qθn (Xn, Un);⊳ Temporal difference term 6: Ân + 1 = Ân + γn + 1 [An + 1 − Ân];⊳ Matrix gain update rule 7: θn + 1 = θn − αn + 1 Ân + 1−1 ζn dn + 1;⊳ Zap-Q update rule 8: ζn + 1:= λ β ζn + ψ (Xn + 1, Un + 1);⊳ Eligibility vector update rule Algorithm 1 Zap-Q(λ) algorithm It is assumed that a projection is employed to ensure that $\{{\hat{A}}_{n}^{- 1}\}$ is a bounded sequence --- this is most easily achieved using the Matrix Inversion Lemma.

The analysis that follows is specialized to $\lambda = 0$ and the basis that is used in Watkins' algorithm. The resulting Zap-Q algorithm is defined as follows, after identifying $Q^{\theta}$ and $\theta$: where ${\hat{G}}_{n}^{\ast} = {- {\lbrack{\hat{A}}_{n}\rbrack}^{- 1}}$, and $\lbrack \cdot \rbrack$ denotes a projection, chosen so that $\{{\hat{G}}_{n}^{\ast}\}$ is a bounded sequence. In Thm. 3.4 it is established that the projection is required only for a finite number of iterations: $\{{\hat{A}}_{n}^{- 1}:{n \geq n_{\bullet}}\}$ is a bounded sequence, where $n_{\bullet} < \infty$ a.s..

An equivalent representation for the parameter recursion (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) is in which $c$ and $\theta_{n}$ are treated as $d$-dimensional vectors rather than functions on $\mathsf{X} \times \mathsf{U}$, and It would seem that the analysis is complicated by the fact that the sequence $\{ A_{n}\}$ depends upon $\{\theta_{n}\}$ through the policy sequence $\{\phi_{n}\}$. Part of the analysis is simplified by obtaining a recursion for the following $d$-dimensional sequence: where $\Pi$ is the $d \times d$ diagonal matrix with entries ${{\Pi{(k,k)}}:=\varpi}{(x^{k},u^{k})}$. This admits a very simple recursion in the special case ${\mathbf{γ}} \equiv {\mathbf{α}}$. In the other case considered, wherein the step-size sequence $\mathbf{γ}$ satisfies, the recursion for $\hat{\mathbf{C}}$ is more complex, but the ODE analysis is simplified.

### Main results

Conditions for convergence of the Zap-Q algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) are summarized in Thm. 3.4. The following assumption is used to address the discontinuity in the recursion for $\{{\hat{A}}_{n}\}$ resulting from the dependence of $A_{n + 1}$ on $\phi_{n}$.

Assumption Q3: The sequence of policies $\{\phi_{n}\}$ satisfies:

### Theorem 3.4

Suppose that Assumptions Q1--Q3 hold, with the gain sequences $\mathbf{α}$ and $\mathbf{γ}$ satisfying for some fixed $\rho \in {(\frac{1}{2},1)}$. Then, The parameter sequence $\{\theta_{n}\}$ obtained using the Zap-Q algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) converges to $Q^{\ast}$ a.s..

The asymptotic covariance is minimized over all $\mathbf{G}$-Q($0$) matrix gain versions of Watkins' Q-learning algorithm.

An ODE approximation holds for the sequence $\{\theta_{n},{\hat{C}}_{n}\}$, by continuous functions $({\mathbf{q}},{\mathbf{c}})$ satisfying This ODE approximation is exponentially asymptotically stable, with ${\lim\limits_{t\rightarrow\infty}q_{t}} = Q^{\ast}$. $\sqcap$$\sqcup$ See Section 3.6.2 and standard references such as for the precise meaning of the ODE approximation.

### Proof of Thm. 3.4

Boundedness of the sequences $\{{\theta_{n},{\hat{A}}_{n}}:{n \geq 0}\}$ and $\{{\hat{A}}_{n}^{- 1}:{n \geq n_{\bullet}}\}$ is established in Lemmas A.3 and A.6, where $n_{\bullet} < \infty$ a.s.. The ODE approximation is established in Prop. A.7. These two results combined with standard arguments establishes (i).

Result (ii) follows from convergence of the algorithm, just as in the case of TD-learning. Uniqueness of the optimal policy is needed so that the recursion for $\{\theta_{n}\}$ admits a linearization around $Q^{\ast}$. $\sqcap$$\sqcup$ In the case ${\mathbf{γ}} \equiv {\mathbf{α}}$, the three consequences hold under a stronger assumption than Q3:

### Proposition 3.5

Suppose that Assumptions Q1--Q2 hold, ${\mathbf{γ}} \equiv {\mathbf{α}}$, and the sequence of policies $\{\phi_{n}\}$ is convergent. Then, the parameter sequence $\{\theta_{n}\}$ obtained using the Zap-Q algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) converges to $Q^{\ast}$ a.s..

The convergence assumption in Prop. 3.5 is far stronger than Q3: Recall that the policies $\{\phi_{n}\}$ evolve in a finite set $\{\phi^{(i)}:{1 \leq i \leq \ell_{\phi}}\}$. Convergence means that $\phi_{n} = \phi^{(\overset{\sim}{k})}$ for some integer-valued random variable $\overset{\sim}{k}$, and all $n$ sufficiently large.

The proof of Prop. 3.5 is based on a simple inverse dynamic programming argument: it is easily shown that ${\hat{C}}_{n}$ is convergent to $c$ in the case ${\mathbf{γ}} \equiv {\mathbf{α}}$, and it is also easily established that ${{\lim_{n\rightarrow\infty}\theta_{n}} - {\mathcal{Q}{({\hat{C}}_{n})}}} = 0$ in this case. The proof of Thm. 3.4 is more delicate, and is based on extensions of ODE arguments .

The simplicity of the proof of Prop. 3.5 suggests that this case would be preferred. However, when $\gamma_{n} \equiv \alpha_{n} = {1/n}$ we do not know how to relax the assumption that $\{\phi_{n}\}$ is convergent. Analysis is complicated by the fact that ${\hat{A}}_{n}$ is obtained as a uniform average of $\{ A_{n}\}$.

The ODE analysis in the proof of Thm. 3.4 suggests that the dynamics of the two time-scale algorithm closely matches the Newton-Raphson ideal. Moreover, the two time-scale algorithm has the best performance in all of the numerical experiments surveyed in Section 4.

### ODE and Policy Iteration

Recall the definition of $\partial\mathcal{Q}_{\mu}$. The ODE approximation can be expressed where $\mu_{t}$ is any pmf satisfying ${\partial{\mathcal{Q}_{\mu_{t}}c_{t}}} = q_{t}$, and the derivative exists for a.e. $t$ (see Lemma A.10 for full justification). This has an interesting geometric interpretation. Without loss of generality, assume that the cost function is non-negative, so that $\mathbf{q}$ evolves in the positive orthant ${\mathbb{R}}_{+}^{d}$ whenever its initial condition lies in this domain.

Figure 1: ODE for SNR2 Q-Learning. The light arrows show typical vectors in the vector field that defines the ODE. The solution starting at q0 ∈ Θ3 initially moves in a straight line towards Q3.

A typical solution to the ODE is shown in Fig. 1: the trajectory is piecewise linear, with changes in direction corresponding to changes in the policy $\phi^{q_{t}}$. Each set $\Theta^{k}$ shown in the figure corresponds to a deterministic policy:

### Lemma 3.6

For each $k$ the set $\Theta^{k}$ is a convex polyhedron, and also a positive cone. When $q_{t} \in {\text{interior}{(\Theta^{k})}}$ then

### Proof

The power series expansion holds: For each $n \geq 1$ we have ${\lbrack{PS_{\phi}}\rbrack}^{n} = {PP_{\phi}^{n - 1}S_{\phi}}$, which together with implies the desired result. $\sqcap$$\sqcup$ The function $Q^{k}$ is the fixed-policy Q-function considered in the SARSA algorithm. While $q_{t}$ evolves in the interior of the set $\Theta^{k}$, it moves in a straight line towards the function $Q^{k}$. On reaching the boundary, it then moves in a straight line to the next Q-function. This is something like a policy iteration recursion, since the policy $\phi^{q_{t}}$ is obtained as the argmin over $u$ of $q_{t}{(\cdot,u)}$.

Of course, it is far easier to establish stability of the equivalent ODE.

### Overview of proofs

This final subsection is dedicated to the proof of Prop. 3.5, and the main ideas in the proof of Thm. 3.4. It is assumed throughout the remainder of this section that Assumptions Q1--Q3 hold. Proofs of technical lemmas are contained in Appendix A.3.

We require the usual probabilistic foundations: There is a probability space $(\Omega,\mathcal{F},\mathsf{P})$ that supports all random variables under consideration. The probability measure $\mathsf{P}$ may depend on an initialization of the Markov chain. All stochastic processes under consideration are assumed adapted to a filtration denoted $\{\mathcal{F}_{n}:{n \geq 0}\}$.

We begin with the proof of the simpler Prop. 3.5.

### Inverse Dynamic Programming Analysis

Prop. 3.5 is a quick consequence of the following extension of Prop. 2.2:

### Proposition 3.7

Suppose that Assumptions Q1--Q3 hold. Suppose moreover that each of the matrices $\{{\hat{A}}_{n}:{n \geq n_{\bullet}}\}$ is invertible for some $n_{\bullet} \geq 1$ that is a.s. finite. Then, the following recursion holds for $n \geq n_{\bullet}$: where $\Psi_{n}$ is defined in (56 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")). $\sqcap$$\sqcup$

### Proof of Prop. 3.5

The assumption that the sequence of policies $\{\phi_{n}\}$ converges to a (possibly random) limit $\phi_{\infty}$ has the following consequences: First, this implies that ${\hat{A}}_{n}$ defined in (54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) converges: Second, for all $n$ sufficiently large the following identities hold, by applying the definitions of $\phi_{n}$ and $\mathcal{Q}^{- 1}$: From, since the limit on the right hand side is invertible and the set of all invertible matrices is open, it follows that there is an integer $n_{\bullet}$ that is finite a.s., and such that ${\hat{A}}_{n}$ is invertible for $n \geq n_{\bullet}$.

Now applying Prop. 3.7, the recursion is reduced to the following in the case that ${\mathbf{γ}} \equiv {\mathbf{α}}$: This is essentially a Monte-Carlo average of $\{{\Pi^{- 1}\Psi_{n}c}:{n \geq 0}\}$. Since the steady state expectation of $\Psi_{n}$ is equal to $\Pi$, convergence follows from the Law of Large Numbers: Combining equations and implies Lemma 3.2 completes the proof: ${\lim\limits_{n\rightarrow\infty}\theta_{n}} = {\mathcal{Q}{(c)}} = Q^{\ast}$. $\sqcap$$\sqcup$

### ODE Analysis

The remainder of this section is devoted to a high-level view of the proof of the ODE approximation for the two time-scale algorithm, with $\mathbf{α}$ and $\mathbf{γ}$ defined .

The construction of an approximating ODE involves first defining a continuous time process. Denote and define ${\overline{q}}_{t_{n}} = \theta_{n}$ for these values, with the definition extended to ${\mathbb{R}}_{+}$ via linear interpolation. We say that the ODE approximation ${\frac{d}{dt}q} = {f{(q)}}$ holds if we have the approximation, where the error process satisfies, for each $T > 0$, Such approximations will be represented using the more compact notation: An ODE approximation holds for Watkins algorithm, with $f{(q_{t})}$ defined by the right hand side of, or in more compact notation: The significance of this representation is that $q_{t}$ is the Q-function associated with the "cost function" $c_{t}$: $q_{t} = {\mathcal{Q}{(c_{t})}}$.

The same notation will be used in the following treatment of Zap Q-learning. Along with the piecewise linear continuous-time process $\{{\overline{q}}_{t}:{t \geq 0}\}$, denote by $\{{\overline{\mathcal{A}}}_{t}:{t \geq 0}\}$ the piecewise linear continuous-time process defined similarly, with ${\overline{\mathcal{A}}}_{t_{n}} = {\hat{A}}_{n}$, $n \geq 1$, and ${\overline{c}}_{t} = {\mathcal{Q}^{- 1}{({\overline{q}}_{t})}}$ for $t \geq 0$.

To construct an ODE, it is convenient first to obtain an alternative and suggestive representation for the pair of equations (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")). A vector-valued sequence of random variables $\{\mathcal{E}_{k}\}$ will be called ODE-friendly if it admits the decomposition, in which $\{\Delta_{k}:{k \geq 1}\}$ is a martingale-difference sequence satisfying ${\mathsf{E}{\lbrack{{\|\Delta_{k + 1}\|}^{2} \mid \mathcal{F}_{k}}\rbrack}} \leq {\overline{\sigma}}_{\Delta}^{2}$ a.s. for some finite ${\overline{\sigma}}_{\Delta}^{2}$ and all $k$, $\{\mathcal{T}_{k}:{k \geq 1}\}$ is a bounded sequence, and the final sequence is bounded and satisfies

### Lemma 3.8

The pair of equations (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) can be expressed, | | $\theta_{n + 1}$ | $= {\theta_{n} + {\alpha_{n + 1}{\hat{G}}_{n + 1}^{\ast}\left\lbrack {{- {\Pi{\lbrack{I - {\betaPS_{\phi^{\theta_{n}}}}}\rbrack}\theta_{n}}} + {\Pic} + {\mathcal{E}_{n + 1}^{A}\theta_{n}} + \mathcal{E}_{n + 1}^{q}} \right\rbrack}}$ | | \(71\) | | | ${\hat{A}}_{n + 1}$ | $= {{\hat{A}}_{n} + {\gamma_{n + 1}\left\lbrack {{{- {\Pi{\lbrack{I - {\betaPS_{\phi^{\theta_{n}}}}}\rbrack}}} - {\hat{A}}_{n}} + \mathcal{E}_{n + 1}^{A}} \right\rbrack}}$ | | | in which the sequence $\{\mathcal{E}_{n}^{q}:{n \geq 1}\}$ is ODE-friendly. The sequence $\{\mathcal{E}_{n}^{A}\}$ is ODE-friendly provided Assumption Q3 holds. $\sqcap$$\sqcup$ The assertion that $\{\mathcal{E}_{n}^{q},\mathcal{E}_{n}^{A}\}$ are ODE-friendly follows from standard arguments based on solutions to Poisson's equation for zero-mean functions of the Markov chain $({\mathbf{X}},{\mathbf{U}})$. The proof of Lemma 3.9 is based on an extension of this technique to the present setting.

### Lemma 3.9

For each $n \geq 0$, where $\{\Delta_{k}^{\Psi}\}$ is a martingale difference sequence with uniformly bounded second moment, and the sequences $\{{\mathcal{T}_{k},\varepsilon_{k}}:{k \geq 0}\}$ are also bounded. If Assumption Q3 holds then $\{\varepsilon_{k}\}$ satisfies. $\sqcap$$\sqcup$ The representation in Lemma 3.8 appears similar to an Euler approximation of the solution to an ODE: It is discontinuity of the function $f_{A}$ that presents the most significant challenge in analysis of the algorithm --- this violates standard conditions for existence and uniqueness of solutions to the ODE without disturbance.

Fortunately there is special structure that will allow the construction of an ODE approximation. Some of this structure is highlighted in the lemma that follows. These approximations are taken from Lemmas A.3 and A.6.

### Lemma 3.10

For each ${t,T_{0}} \geq 0$, where ${g_{t}:=\gamma_{n}}/\alpha_{n}$ when $t = t_{n}$ for some $n$, and extended to all $t \in {\mathbb{R}}_{+}$ by linear interpolation. $\sqcap$$\sqcup$ The "gain" $g_{t}$ appearing in converges to infinity rapidly as $t\rightarrow\infty$: Based on the definitions, it follows from that $t_{n} \approx {\log{(n)}}$ for large $n$, and consequently $g_{t} \approx {\exp{({{({1 - \rho})}t})}}$ for large $t$. This suggests that the integrand ${\Pi{\lbrack{I - {\betaPS_{\phi^{{\overline{q}}_{t}}}}}\rbrack}} + {\overline{\mathcal{A}}}_{t}$ should converge to zero rapidly with $t$. This intuition is made precise in the Appendix. Through several subsequent transformations, these integral equations are shown to imply the ODE approximation in Thm. 3.4.

### An $O{(d)}$ Zap-Q learning algorithm

In this subsection, we introduce an $O{(d)}$ Zap-Q learning algorithm, which is basically the $O{(d)}$ Zap-SNR algorithm described in Section 2.3.2 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning") specialized to Q-learning.

Based on the equations (24 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")), (25 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")), (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")), and (54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")), the algorithm is defined as follows: Fix $N = d$, and for $i \geq 0$, | | ${\hat{A}}_{{({i + 1})}N}$ | $= {{\hat{A}}_{iN} + {{\hat{\gamma}}_{i + 1}\left\lbrack {{{\nabla\hat{f}}{(\theta_{iN})}} - {\hat{A}}_{n}} \right\rbrack}}$ | | | | | ${\nabla\hat{f}}{(\theta_{iN})}$ | ${= {N^{- 1}{\sum\limits_{j = {{iN} + 1}}^{{({i + 1})}N}{\psi{(X_{j},U_{j})}\left\lbrack {{\beta\psi{(X_{j + 1},{\phi^{\theta_{iN}}{(X_{j + 1})}})}} - {\psi{(X_{j},U_{j})}}} \right\rbrack^{\text{T}}}}}},$ | | | ${\hat{G}}_{{({i + 1})}N}^{\ast} = {- {\lbrack{\hat{A}}_{{({i + 1})}N}\rbrack}^{- 1}}$, with $\lbrack \cdot \rbrack$ denoting a projection, chosen so that $\{{\hat{G}}_{{({i + 1})}N}^{\ast}\}$ is a bounded sequence. For a given parameter vector $\theta$, the policy $\phi^{\theta}$ is defined.

Once again, we claim that the asymptotic properties of the above defined $O{(d)}$ Zap-Q learning algorithm is the same as that of the Zap-Q learning algorithm defined in (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) and (54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")), with justification postponed to a future version of the paper.

## Numerical Results

Results from numerical experiments are surveyed here to illustrate the performance of the Zap Q-learning algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")). Comparisons are made with several existing algorithms, including Watkins Q-learning, Watkins Q-learning with Ruppert-Polyak-Juditsky (RPJ) averaging, Watkins Q-learning with a "polynomial learning rate", and the more recent *Speedy Q-learning* algorithm.

In addition, the Watkins algorithm with a scalar gain $g$ is considered, with $g$ chosen so that the algorithm has finite asymptotic covariance. When the value of $g$ is optimized and numerical conditions are favorable (e.g., the condition number of $A$ is not too large) it is found that the performance is nearly as good as the Zap-Q algorithm. However, there is no free lunch: Design of the scalar gain $g$ depends on approximation of $A$, and hence $\theta^{\ast}$. While it is possible to estimate $A$ via Monte-Carlo in Zap Q-learning, it is not known how to efficiently update approximations for an optimal scalar gain.

A reasonable asymptotic covariance required a large value of $g$. Consequently, the scalar gain algorithm had massive transients, resulting in a poor performance in practice.

Transient behavior could be tamed through projection to a bounded set. However, this again requires prior knowledge of the region in the parameter space to which $\theta^{\ast}$ belongs.

Projection of parameters was also necessary for RPJ averaging.

The following batch mean method was used to estimate the asymptotic covariance.

### Batch Mean Method

At stage $n$ of the algorithm we will be interested in the distribution of a vector-valued random variable of the form $f_{n}{(\theta_{n})}$, where $f_{n}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{m}}$ is possibly dependent on $n$. The batch mean method is used to estimate its statistics: For each algorithm, $N$ parallel simulations are run with $\theta_{0}$ initialized i.i.d. according to some distribution. Denoting $\theta_{n}^{i}$ to be the vector $\theta_{n}$ corresponding to the $i^{th}$ simulation, the distribution of the random variable $f_{n}{(\theta_{n})}$ is estimated based on the histogram of the independent samples $\{{f_{n}{(\theta_{n}^{i})}}:{1 \leq i \leq N}\}$.

An important special case in this paper is ${f_{n}{(\theta_{n})}} = {{W_{n}:=\sqrt{n}}{({\theta^{n} - \theta^{\ast}})}}$. However, since the limit $\theta^{\ast}$ is not available, the empirical mean is substituted: The estimate of the covariance of $f_{n}{(\theta_{n})}$ is then obtained as the sample covariance of $\{{{W_{n}^{i},\, 1} \leq i \leq N}\}$. This corresponds to the estimate of the asymptotic covariance $\Sigma_{\theta}$ defined.

The value $N = 10^{3}$ is used in all of the experiments surveyed here.

Figure 2: Graph for MDP

### Finite state-action MDP

Consider first a simple stochastic-shortest-path problem. The state space $\mathsf{X} = {\{ 1,\ldots,6\}}$ coincides with the six nodes on the un-directed graph shown in Fig. 2. The action space $\mathsf{U} = {\{ e_{x,x'}\}}$, ${x,x'} \in \mathsf{X}$, consists of all feasible edges along which an agent can travel, including each "self-loop", $u = e_{x,x}$. The number of state-action pairs for this example coincides with the number of nodes plus twice the number of edges: $d = 18$.

The controlled transition matrix is defined as follows: If $X_{n} = x \in \mathsf{X}$, and $U_{n} = e_{x,x'} \in \mathsf{U}$, then $X_{n + 1} = x'$ with probability $0.8$, and with probability $0.2$, the next state is randomly chosen between all neighboring nodes. The goal is to reach the state $x^{\ast} = 6$ and maximize the time spent there. This is modeled through a discounted-reward optimality criterion with discount factor $\beta \in {}$. The one-step reward is defined as follows: The solution to the discounted-cost optimal control problem can be computed numerically for this model; the optimal policy is unique and independent of $\beta$.

Six different variants of Q-learning were tested: Watkins' algorithm with scalar gain $g$, so that $\alpha_{n} \equiv {g/n}$ Watkins' algorithm using RPJ averaging, with $\gamma_{n} \equiv {(\alpha_{n})}^{0.6} \equiv n^{- 0.6}$ Watkins' algorithm with the polynomial learning rate $\alpha_{n} \equiv n^{- 0.6}$ Zap Q-learning with ${\mathbf{α}} \equiv {\mathbf{γ}}$ Zap Q-learning with $\gamma_{n} \equiv {(\alpha_{n})}^{0.85} \equiv n^{- 0.85}$ The basis was taken to be the same as in Watkins Q-learning algorithm. In each case, the randomized policy was taken to be uniform: feasible transitions were sampled uniformly at each time.

Discount factors $\beta = 0.8$ and $\beta = 0.99$ were considered. In each case, the unique optimal parameter $\theta^{\ast} = Q^{\ast}$ was obtained numerically.

### Asymptotic Covariance

Speedy Q-learning cannot be represented as a standard stochastic approximation, so standard theory cannot be applied to obtain its asymptotic covariance. The Watkins' algorithm with polynomial learning rate has infinite asymptotic covariance.

For the other four algorithms, the asymptotic covariance $\Sigma_{\theta}$ was computed by solving the Lyapunov equation based on the matrix gain $G$ that is particular to each algorithm. Recall that $G = {- A^{- 1}}$ in the case of either of the Zap-Q algorithms.

The matrices $A$ and $\Sigma_{\Delta}$ appearing in are defined with respect to Watkins' Q-learning algorithm with $\alpha_{n} = {1/n}$. The first matrix is $A = {- {\Pi{\lbrack{I - {\betaPS_{\phi^{\ast}}}}\rbrack}}}$ under the standing assumption that the optimal policy is unique. The proof that this is a linearization comes first from the representation of the ODE approximation in vector form: Uniqueness of the optimal policy implies that $\overline{f}$ is locally linear: there exists $\varepsilon > 0$ such that The matrix $\Sigma_{\Delta}$ was also obtained numerically, without resorting to simulation.

Figure 3: Eigenvalues of the matrix A for the 6-state example The eigenvalues of the $18 \times 18$ matrix $A$ are real in this example, as shown in Fig. 3 for both values of $\beta$. To ensure that the eigenvalues of $gA$ are all strictly less than $- {1/2}$ in a scalar gain algorithm requires the (approximate) lower bounds $g > 45$ for $\beta = 0.8$, and $g > 900$ for $\beta = 0.99$. Thm. 2.1 implies that the asymptotic covariance $\Sigma_{\theta}{(g)}$ is finite for this range of $g$ in the Watkins algorithm with $\alpha_{n} \equiv {g/n}$. Fig. 4 shows the normalized trace of the asymptotic covariance as a function of $g > 0$, and the significance of $g \approx 45$ and $g \approx 900$.

Figure 4: The normalized trace of the asymptotic covariance for the scaled Watkins algorithm with different scalar gains g, for the 6-state example: σ2 (g) = trace (Σθ (g)) and σ2 (G*) = trace (Σ*).

Based on this analysis or on Thm. 3.3, it follows that the asymptotic covariance is not finite for the standard Watkins' algorithm with $\alpha_{n} \equiv {1/n}$. In simulations it was found that the parameter estimates are not close to $\theta^{\ast}$ even after many millions of samples. This is illustrated for the case $\beta = 0.8$ in Fig. 5, which shows a histogram of $10^{3}$ estimates of $\theta_{n}{}$ with $n = 10^{6}$ (other entries showed similar behavior).

Figure 5: Histogram of 103 estimates of θn, with n = 106 for the Watkins algorithm applied to the 6-state example with discount factor β = 0.8 It was found that the algorithm performed very poorly in practice for any scalar gain algorithm. For example, more than half of the $10^{3}$ experiments using $\beta = 0.8$ and $g = 70$ resulted in values of $\theta_{n}{}$ exceeding $\theta^{\ast}{}$ by $10^{4}$ (with ${\theta^{\ast}{}} \approx 500$), even with $n = 10^{6}$. The algorithm performed well with the introduction of projection in the case $\beta = 0.8$. With $\beta = 0.99$, the performance was unacceptable for any scalar gain, even with projection.

The results presented next used a gain of $g = 70$ in the case $\beta = 0.8$, and projection of each entry of the estimates to the interval $({- \infty},1000\rbrack$. Fig. 6 shows normalized histograms of $\{{W_{n}^{i}{(k)}}:{1 \leq i \leq N}\}$, as defined , with $k = {10,18}$.

The Central Limit Theorem holds: $W_{n}$ is expected to be approximately normally distributed: $\mathcal{N}{(0,{\Sigma_{\theta}{(g)}})}$, when $n$ is large. Of the $d = 18$ entries of the vector $W_{n}$, with $n \geq 10^{4}$, it was found that the asymptotic variance matched the histogram nearly perfectly for $k = 10$, while $k = 18$ showed the worst fit.

Figure 6: Comparison of theoretical and empirical asymptotic variance for the scaled Watkins’ algorithm, with gain g = 70, applied to the 6-state example with discount factor β = 0.8 These experiments were repeated for each of the Zap-Q algorithms, for which the asymptotic variance $\Sigma^{\ast}$ is obtained using the formula. Plots are shown only for Case 2: the two time-scale algorithm, with $\gamma_{n} = {(\alpha_{n})}^{0.85}$. Histograms in the case of $\beta = 0.8$ are shown in Fig. 7, and Fig. 8 for $\beta = 0.99$. The covariance estimates and the Gaussian approximations match the theoretical predictions remarkably well for $n \geq 10^{4}$.

Figure 7: Comparison of theoretical and empirical asymptotic variance of the two time-scale Zap-Q algorithm applied to the 6-state example; β = 0.8 Figure 8: Comparison of theoretical and empirical asymptotic variance of the Zap-Q-learning algorithm applied to the 6-state example; β = 0.99 Figure 9: Maximum Bellman error $\{{\overline{\mathcal{B}}}_{n}:{n \geq 0}\}$ for the six Q-learning algorithms

### Bellman Error

The Bellman error at iteration $n$ is denoted: This is identically zero if and only if $\theta_{n} = Q^{\ast}$. If $\{\theta_{n}\}$ converges to $Q^{\ast}$ then $\mathcal{B}_{n} = {{\overset{\sim}{\theta}}_{n} - {\betaPS_{\phi^{\ast}}{\overset{\sim}{\theta}}_{n}}}$ for all sufficiently large $n$, and the CLT holds for $\{\mathcal{B}_{n}\}$ whenever it holds for $\{\theta_{n}\}$. Moreover, on denoting the maximal error the sequence $\{{\sqrt{n}{\overline{\mathcal{B}}}_{n}}\}$ also converges in distribution as $n\rightarrow\infty$. Fig. 9 contains plots of $\{{\overline{\mathcal{B}}}_{n}\}$ for the six different Q-learning algorithms.

For large $n$, the two versions of Zap Q-learning exhibit similar behavior since ${\hat{A}}_{n}$ converges to $A$ in both algorithms. Though all six algorithms perform reasonably well when $\beta = 0.8$, Zap Q-learning is the only one that achieves near zero Bellman error within $n = 10^{6}$ iterations in the case $\beta = 0.99$. Moreover, the performance of the two time-scale algorithm is clearly superior to the one time-scale algorithm.

Figure 10: Simulation-based 2 σ confidence intervals for the six Q-learning algorithms with discount factor β = 0.8.

Figure 11: Simulation-based 2 σ confidence intervals for the six Q-learning algorithms with discount factor β = 0.99.

Fig. 9 shows only the typical behavior --- repeated trails were run to investigate the range of possible outcomes. For each algorithm, the outcomes of $N = 1000$ independent simulations resulted in samples $\{{{{\overline{\mathcal{B}}}_{n}^{i},\, 1} \leq i \leq N}\}$, with $\theta_{0}$ uniformly distributed on the interval $\lbrack{- 10^{3}},10^{3}\rbrack$ for $\beta = 0.8$ and $\lbrack{- 10^{4}},10^{4}\rbrack$ for $\beta = 0.99$.

The batch means method was used to obtain estimates of the mean and variance of ${\overline{\mathcal{B}}}_{n}$ for a range of values of $n$. Plots of the mean and $2\sigma$ confidence intervals are shown in Fig. 10 for the case $\beta = 0.8$, and plots for $\beta = 0.99$ are shown in Fig. 11.

Fig. 12 and Fig. 13 shows histograms of $\{{{{\overline{\mathcal{B}}}_{n}^{i},\, 1} \leq i \leq N}\}$, ${n = 10^{6}},$ for all the six algorithms; this corresponds to the data shown in Fig. 10 and Fig. 11 at $n = 10^{6}$.

Figure 12: Histogram of the maximal Bellman error when discount factor β = 0.8 and number of iterations n = 106.

Figure 13: Histogram of the maximal Bellman error when discount factor β = 0.99 and number of iterations n = 106.

### Performance of the $O{(d)}$ Zap-Q learning algorithm

In this subsection, we test the performance of the $O{(d)}$ Zap-Q learning algorithm that was defined in equations (74 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) and (75 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) of Section 3.7 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning") by applying it to the stochastic shortest path problem. We restrict to the comparison of the Bellman errors (defined in ) of the different algorithms, and we consider the case $\beta = 0.99$.

Fig. 14 Zap-Q learning algorithm ‣ 4.1 Finite state-action MDP ‣ 4 Numerical Results ‣ Fastest Convergence for Q-Learning") contains plots of $\{{\overline{\mathcal{B}}}_{n}\}$ for the different Q-learning algorithms. For the $O{(d)}$ Zap-Q learning algorithms, the batch size was set to $N = 100$ ($d = 18$ in this problem). We notice in the figure that the $O{(d)}$ algorithm performs nearly as well as the $O{(d^{2})}$ algorithm when the step-sizes (${\hat{\gamma}}_{i}$) are chosen appropriately. Furthermore, the naive batching technique applied to a single-time-scale Stochastic Newton-Raphson algorithm ($\gamma_{n} \equiv \alpha_{n}$ and therefore ${\hat{\gamma}}_{i} \approx \alpha_{i}$) performs extremely poorly.

Figure 14: Maximum Bellman error $\{{\overline{\mathcal{B}}}_{n}:{n \geq 0}\}$ for different Q-learning algorithms

### Finance model

The next example is taken . The reader is referred to these references for complete details of the problem set-up and the reinforcement learning architecture used in this prior work. The example is of interest because it shows how the Zap Q-learning algorithm can be used with a more general basis, and also how the technique can be extended to optimal stopping time problems.

The Markovian state process considered in is the vector of ratios: in which $\{{\overset{\sim}{p}}_{t}:{t \in {\mathbb{R}}}\}$ is a geometric Brownian motion (derived from an exogenous price-process). This uncontrolled Markov chain is positive Harris recurrent on the state space $\mathsf{X} \equiv {\mathbb{R}}^{100}$.

The "time to exercise" is modeled as a stopping time $\tau \in {\mathbf{Z}}^{+}$. The associated expected reward is defined as $\mathsf{E}{\lbrack{\beta^{\tau}r{(X_{\tau})}}\rbrack}$, with ${{{r{(X_{n})}}:=X_{n}}{}} = {{\overset{\sim}{p}}_{n}/{\overset{\sim}{p}}_{n - 100}}$ and $\beta \in {}$ fixed. The objective of finding a policy that maximizes the expected reward is modeled as an optimal stopping time problem.

The value function is defined to be the supremum over all stopping times: This solves the Bellman equation: The associated Q-function is denoted ${{Q^{\ast}{(x)}}:=\beta}\mathsf{E}{\lbrack{{{h^{\ast}{(X_{n + 1})}} \mid X_{n}} = x}\rbrack}$, which solves a similar fixed point equation: A stationary policy $\phi:{\mathsf{X}\rightarrow{\{ 0,1\}}}$ assigns an action for each state $x \in \mathsf{X}$ as Each policy $\phi$ defines a stopping time and associated average reward, denoted The optimal policy is expressed as The corresponding optimal stopping time that solves the supremum in is achieved using this policy: $\tau^{\ast} = {\min{\{{n:{{\phi^{\ast}{(X_{n})}} = 1}}\}}}$.

The objective here is to find an approximation for $Q^{\ast}$ in a parameterized class $\{{{Q^{\theta}:=\theta^{\text{T}}}\psi}:{\theta \in {\mathbb{R}}^{d}}\}$, where $\psi:{\mathsf{X}\rightarrow{\mathbb{R}}^{d}}$ is a vector of basis functions. For a fixed parameter vector $\theta$, the associated value function is denoted | | $h_{\phi^{\theta}}{(x)}$ | ${= {\mathsf{E}{\lbrack{{{\beta^{\tau_{\theta}}r{(X_{\tau_{\theta}})}} \mid x_{0}} = x}\rbrack}}},$ | | \(81\) | | | $\text{where}\qquad\tau_{\theta} = \min{\{ n:}$ | $\phi^{\theta}{(X_{n})} = 1\},\phi^{\theta}(x) = {\mathbb{I}}\{ r{(x)} \geq Q^{\theta}{(x)}\}.$ | | | The function $h_{\phi^{\theta}}$ was estimated using Monte-Carlo in the numerical experiments surveyed below.

### Approximations to the Optimal Stopping Time Problem

To obtain the optimal parameter vector $\theta^{\ast}$, in the authors apply the Q($0$)-learning algorithm: This is one of the few parameterized Q-learning settings for which convergence is guaranteed.

In the authors attempt to improve the performance of the Q($0$) algorithm through the use of the sequence of matrix gains and a special choice for the $\{\alpha_{n}\}$: where $g$ and $b$ are positive constants. The resulting recursion is the $\mathbf{G}$-Q($0$) algorithm: Through trial and error the authors find that $g = 10^{2}$, $b = 10^{4}$ gives good performance. These values were also used in the experiments described in the following.

The limiting matrix gain is given by where the expectation is in steady-state. The asymptotic covariance $\Sigma_{\theta}^{G}$ is the unique positive semi-definite solution to the Lyapunov equation, provided all eigenvalues of $GA$ satisfy ${\text{Re}{(\lambda)}} < {- \frac{1}{2}}$.

The Zap Q-learning algorithm for this example is defined by the following recursion: It is conjectured that the asymptotic covariance $\Sigma^{\ast}$ is obtained using, where the matrix $A$ is the limit of ${\hat{A}}_{n}$: Figure 15: Eigenvalues of A and G A for the finance example

### Experimental Results

The experimental setting of is used to define the set of basis functions and other parameters. The dimension of the parameter vector $d$ was chosen to be $10$, with the basis functions defined . The objective here is to compare the performances of $\mathbf{G}$-Q($0$) and the Zap-Q algorithms in terms of both parameter convergence, and with respect to the resulting average reward.

The asymptotic covariance matrices $\Sigma^{\ast}$ and $\Sigma_{\theta}^{G}$ were estimated through the following steps: The matrices $A$ and $G$ were estimated via Monte-Carlo. Estimation of $A$ requires an estimate of $\theta^{\ast}$; this was taken to be $\theta_{n}$, with $n = {2 \times 10^{6}}$, obtained using the Zap-Q two timescale algorithm with $\alpha_{n} \equiv {1/n}$ and $\gamma_{n} \equiv \alpha_{n}^{0.85}$. This estimate of $\theta^{\ast}$ was also used to estimate the covariance matrix $\Sigma_{\Delta}$ defined in using the batch means method. The matrices $\Sigma_{\theta}^{G}$ and $\Sigma^{\ast}$ were then obtained using and, respectively.

It was found that the trace of $\Sigma_{\theta}^{G}$ was about $15$ times greater than that of $\Sigma^{\ast}$.

### High performance despite ill-conditioned matrix gain

The real part of the eigenvalues of $A$ are shown on a logarithmic scale on the left-hand side of Fig. 15. The eigenvalues of the matrix $A$ have a wide spread: The condition-number is of the order $10^{4}$. This presents a challenge in applying any method. In particular, it was found that the performance of any scalar-gain algorithm was extremely poor, even with projection of parameter estimates.

This is a consequence of the fact that the basis functions $\{\psi_{i}\}$ are nearly linearly dependent. A better basis should be considered in future work, but the main objective here is to test the new methods in a challenging setting, and to compare with prior approaches.

Figure 16: Theoretical and empirical variance for the finance example In applying the Zap Q-learning algorithm it was found that the estimates $\{{\hat{A}}_{n}\}$ in are nearly singular. Despite the unfavorable setting for this approach, the performance of the algorithm was much better than any alternative that was tested. The upper row of Fig. 16 contains normalized histograms of $\{{{W_{n}^{i}{(k)}} = {\sqrt{n}{({{\theta_{n}^{i}{(k)}} - {{\overline{\theta}}_{n}{(k)}}})}}}:{1 \leq i \leq N}\}$ for the Zap-Q algorithm. The variance for finite $n$ is close to the theoretical predictions based on the asymptotic covariance $\Sigma^{\ast}$. The histograms were generated for two values of $n$, and $k = {1,7}$. Of the $d = 10$ possibilities, the histogram for $k = 1$ had the worst match with theoretical predictions, and $k = 7$ was the closest.

The eigenvalues corresponding to the matrix $GA$ are shown on the right hand side of Fig. 15. It is found that one of these eigenvalues is very close to $- 0.5$, and the sufficient condition for ${\text{trace~}{(\Sigma_{\theta}^{G})}} < \infty$ is barely satisfied. It is worth stressing that the finite asymptotic covariance was not a design goal in this prior work. It is only now on revisiting this paper that we find that the sufficient condition $\lambda < {- \frac{1}{2}}$ is satisfied.

The lower row of Fig. 16 contains the normalized histograms of $\{{{W_{n}^{i}{(k)}} = {\sqrt{n}{({{\theta_{n}^{i}{(k)}} - {{\overline{\theta}}_{n}{(k)}}})}}}:{1 \leq i \leq N}\}$ for the $\mathbf{G}$-Q($0$) algorithm for $n = {2 \times 10^{4}}$ and $2 \times 10^{6}$, and $k = {1,7}$, along with the theoretical predictions based on the asymptotic covariance $\Sigma_{\theta}^{G}$.

Figure 17: Histograms of the average reward obtained using the G-Q learning and the Zap-Q-learning, γn ≡ αn−ρ ≡ n − ρ

### Asymptotic variance of the discounted reward

Denote $h_{n} = h_{\phi}$, with $\phi = \phi^{\theta_{n}}$. Histograms of the average reward $h_{n}{(x)}$ were obtained for ${x{(i)}} = 1$, $1 \leq i \leq 100$, and various values of $n$, based on $N = 1000$ independent simulations. The plots shown in Fig. 17 are based on $n = {2 \times 10^{k}}$, for $k = {4,5,6}$. Omitted in this figure are outliers: values of the reward in the interval $\lbrack 0,1)$. Table 1 lists the number of outliers for each $n$ and each algorithm.

Recall that the asymptotic covariance of the $\mathbf{G}$-Q($0$) algorithm was not far from optimal (its trace was about 15 times larger than obtained using Zap Q-learning). However, it is observed that this algorithm suffers from much larger outliers. It can also be seen that doubling the scalar gain $g$ (causing the largest eigenvalue of $GA$ to be $\approx {- 1}$) results in slightly better performance.

Table 1: Outliers observed in N = 1000 runs. Each table represents the number of runs which resulted in an average reward below a certain value

## Conclusions

Watkins' Q-learning algorithm is elegant, but subject to two common and valid constraints: it can be very slow to converge, and it is not obvious how to extend this approach to obtain a stable algorithm in non-trivial parameterized settings. This paper addresses both concerns with the new Zap Q($\lambda$) algorithms that are motivated by asymptotic theory of stochastic approximation.

There are many avenues for future research. It would be valuable to find an alternative to Assumption Q3 that is readily verified. Based on the ODE analysis, it seems likely that the conclusions of Thm. 3.4 hold without this additional assumption. No theory has been presented here for non-ideal parameterized settings. It is conjectured that conditions for stability of Zap Q($\lambda$)-learning will hold under general conditions. Consistency is a more challenging problem and is a focus of current research.

In terms of algorithm design, it is remarkable to see how well the scalar-gain algorithms perform, provided projection is employed and the condition number of $A$ is not too large. It is possible to estimate the optimal scalar gain based on estimates of the matrix $A$ that is central to this paper. How to do so without introducing high complexity is an open question.

On the other hand, the performance of RPJ averaging is unpredictable. In many experiments it is found that the asymptotic covariance is a poor indicator of finite-$n$ performance when using this approach. There are many suggestions in the literature for improving this technique (see discussion after Theorem 3 of ).

The results in this paper suggest new approaches that we hope will simultaneously Reduce complexity and potential numerical instability of matrix inversion, Improve transient performance, and Maintain optimality of the asymptotic covariance
