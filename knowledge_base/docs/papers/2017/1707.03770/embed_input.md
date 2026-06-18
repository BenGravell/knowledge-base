<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fastest Convergence for Q-learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Zap Q-learning algorithm introduced in this paper is an improvement of Watkins' original algorithm and recent competitors in several respects. It is a matrix-gain algorithm designed so that its asymptotic variance is optimal. Moreover, an ODE analysis suggests that the transient behavior is a close match to a deterministic Newton-Raphson implementation. This is made possible by a two time-scale update equation for the matrix gain sequence. The analysis suggests that the approach will lead to stable and efficient computation even for non-ideal parameterized settings. Numerical experiments confirm the quick convergence, even in such non-ideal cases. A secondary goal of this paper is tutorial. The first half of the paper contains a survey on reinforcement learning algorithms, with a focus on minimum variance algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is recognized that algorithms for reinforcement learning such as TD- and Q-learning can be slow to converge. The poor performance of Watkins' Q-learning algorithm was first quantified, and since then many papers have appeared with proposed improvements, such as.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

An emphasis in much of the literature is computation of finite-time PAC (probably almost correct) bounds as a metric for performance. Explicit bounds were obtained in for Watkins' algorithm, and in for the "speedy" Q-learning algorithm that was introduced by these authors. A general theory is presented in for stochastic approximation algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In each of the models considered in prior work, the update equation for the parameter estimates can be expressed

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

in which $\{\alpha_{n}\}$ is a positive gain sequence, and $\{\Delta_{n}\}$ is a martingale difference sequence. This representation is critical in analysis, but unfortunately is not typical in reinforcement learning applications outside of these versions of Q-learning. For Markovian models, the usual transformation used to obtain a representation similar to results in an error sequence $\{\Delta_{n}\}$ that is the sum of a martingale difference sequence and a telescoping sequence. It is the telescoping sequence that prevents easy analysis of Markovian models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This gap in the research literature carries over to the general theory of Markov chains. Examples of concentration bounds for i.i.d. sequences or martingale-difference sequences include the finite-time bounds of Hoeffding and Bennett. Extensions to Markovian models either offer very crude bounds, or restrictive assumptions; this remains an active area of research.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, asymptotic theory for stochastic approximation (as well as general state space Markov chains) is mature. Large Deviations or Central Limit Theorem (CLT) limits hold under very general assumptions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The CLT will be a guide to algorithm design in the present paper. For a typical stochastic approximation algorithm, this takes the following form: denoting $\{{{{\overset{\sim}{\theta}}_{n}:=\theta_{n}} - \theta^{\ast}}:{n \geq 0}\}$ to be the error sequence, under general conditions the scaled sequence $\{{\sqrt{n}{\overset{\sim}{\theta}}_{n}}:{n \geq 1}\}$ converges in distribution to a Gaussian distribution, $\mathcal{N}{(0,\Sigma_{\theta})}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The limit is known as the asymptotic covariance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

An asymptotic bound such as may not be satisfying for practitioners of stochastic optimization or reinforcement learning, given the success of finite-$n$ performance bounds in prior research.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The asymptotic covariance $\Sigma_{\theta}$ has a simple representation as the solution to a Lyapunov equation. It is easily improved or optimized by design.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

As shown in examples in this paper, the asymptotic covariance is often a good predictor of finite-time performance, since the CLT approximation is accurate for reasonable values of $n$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two approaches are known for optimizing the asymptotic covariance. First is the remarkable averaging technique of Polyak and Juditsky and Ruppert ( provides an accessible treatment in a simplified setting). Second is what we will call Stochastic Newton-Raphson, based on a special choice of matrix gain for the algorithm. The second approach underlies the analysis of the averaging approach.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are not aware of theory that distinguishes the performance of Polyak-Ruppert averaging as compared to the Stochastic Newton-Raphson method. It is noted in that the averaging approach often leads to very large transients, so that the algorithm should be modified (such as through projection of parameter updates). This may explain why averaging is not very popular in practice. In our own numerical experiments it is observed that the rate of convergence of CLT in this case is slow when compared to matrix gain methods.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition to accelerating the convergence rate of standard algorithms for reinforcement learning, it is hoped that this paper will lead to entirely new algorithms. In particular, there is little theory to support Q-learning in non-ideal settings in which the optimal "$Q$-function" does not lie in the parameterized function class. Convergence results have been obtained for a class of optimal stopping problems, and for deterministic models. There is now intense practical interest, despite an incomplete theory. A stronger supporting theory will surely lead to more efficient algorithms.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

A new class of algorithms is proposed, designed to more accurately mimic the classical Newton-Raphson algorithm. It is based on a two time-scale stochastic approximation algorithm, constructed so that the matrix gain tracks the gain that would be used in a deterministic Newton-Raphson method.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions", "weight": 1.0} -->

The application of this approach to reinforcement learning results in the new Zap Q-learning algorithms. A full analysis is presented for the special case of a complete parameterization (similar to the setting of Watkins' original algorithm). It is found that the associated ODE has a remarkable and simple representation, which implies consistency under suitable assumptions. Extensions to non-ideal parameterized settings are also proposed, and numerical experiments show dramatic variance reductions. Moreover, results obtained from finite-$n$ experiments show close solidarity with asymptotic theory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions", "weight": 1.0} -->

The potential complexity introduced by the matrix gain is not of great concern in many cases, because of the dramatically acceleration in the rate of convergence. Moreover, the main contribution of this paper is not a single algorithm but a class of algorithms, wherein the computational complexity can be dealt with separately. For example, in a parameterized setting, the basis functions can be intelligently pruned via random projection.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions", "weight": 1.0} -->

The remainder of the paper is organized as follows. Background on computing and optimizing the asymptotic covariance is contained in Section 2. Application to Q-learning, and theory surrounding the new Zap Q-learning algorithm is developed in Section 3. Numerical results are surveyed in Section 4, and conclusions are contained in Section 5. The proofs of the main results are contained in the Appendix; the final page contains Table 2 containing a list of notation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stochastic Newton Raphson and TD-Learning", "weight": 1.0} -->

This first section is largely a tutorial on reinforcement learning. It is shown that the LSTD($\lambda$) learning algorithm of is an instance of the "SNR algorithm", in which there is only one time-scale for the parameter and matrix-gain updates. The original motivation for the LSTD($\lambda$) algorithm had no connection with asymptotic variance. It was shown later in that the LSTD ($\lambda$) algorithm is the minimum asymptotic variance version of the TD ($\lambda$) algorithm of.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stochastic Newton Raphson and TD-Learning", "weight": 1.0} -->

The focus is on fixed point equations associated with an uncontrolled Markov chain, denoted ${\mathbf{X}} = {\{ X_{n}:{n = {0,1,\ldots}}\}}$, on a measurable state space $(\mathsf{X},{\mathcal{B}{(\mathsf{X})}})$. It is assumed to be $\psi$-irreducible and aperiodic. In Section 3 we specialize to a finite state space.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stochastic Newton Raphson and TD-Learning", "weight": 1.0} -->

In control applications and analysis of learning algorithms, it is necessary to construct a Markov chain $\mathbf{\Phi}$, of which $\mathbf{X}$ is a component. Other components may be an input process, or a sequence of "eligibility vectors" that arise in TD-learning. It will be assumed throughout that there is a unique stationary realization of $\mathbf{\Phi}$, with unique marginal distribution denoted $\varpi$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Motivation from SA & ODE fundamentals", "weight": 1.0} -->

Under general conditions the convergence rate of is quadratic (much faster than geometric), which is not generally true of successive approximation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Motivation from SA & ODE fundamentals", "weight": 1.0} -->

Stochastic approximation is itself an approximation of successive approximation. It is assumed that ${\overline{f}{(\theta)}} = {\mathsf{E}{\lbrack{f{(\theta,\Phi)}}\rbrack}}$, where $f:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{d}}$ and $\Phi$ is a random variable with distribution $\varpi$. The standard stochastic approximation algorithm is defined by

<!-- chunk {"id": "body-0026", "role": "body", "section": "Motivation from SA & ODE fundamentals", "weight": 1.0} -->

While convergent under general conditions, the rate of convergence of can often be improved dramatically through the introduction of a matrix gain. This is explained first in a simple linear setting.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

In many applications of reinforcement learning we arrive at a linear recursion of the form

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

It is assumed throughout this section that $A$ is Hurwitz: the real part of each eigenvalue is negative. Under this assumption, and subject to mild conditions on $\mathbf{\Phi}$, it is known that $\{\theta_{n}\}$ converges with probability one to $\theta^{\ast} = {A^{- 1}b}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

Convergence of the recursion will be assumed henceforth. It is also assumed that the gain sequence is given by $\alpha_{n} = {1/n}$, $n \geq 1$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

A solution is guaranteed only if each eigenvalue of $A$ has real part that is strictly less than $- {1/2}$. If there exists an eigenvalue which does not satisfy this property, then under general conditions the asymptotic covariance is infinity (see Thm. 2.1). Hence the Hurwitz assumption must be strengthened to ensure that the asymptotic covariance is finite.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

where the limit is in distribution. This is a mild requirement when $\mathbf{\Phi}$ is Markovian.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

A finite asymptotic covariance can be guaranteed by increasing the gain: choose $\alpha_{n} = {g/n}$, with $g > 0$ sufficiently large so that the eigenvalues of $gA$ satisfy the required bound.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

The choice $G^{\ast} = {- A^{- 1}}$ is analogous to the gain used in the Newton-Raphson algorithm. With this choice, the asymptotic covariance is finite and given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

It is a remarkable fact that this choice is optimal in the strongest possible statistical sense: For any other gain $G$, the two asymptotic covariance matrices satisfy

<!-- chunk {"id": "body-0035", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

That is, the difference $\Sigma_{\theta}^{G} - \Sigma^{\ast}$ is positive semi-definite.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Optimal covariance for linear stochastic approximation", "weight": 1.0} -->

The following theorem summarizes the results on the asymptotic covariance for the matrix-gain recursion. The proof is contained in Section A.1 of the Appendix.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Stochastic Newton-Raphson", "weight": 1.0} -->

This algorithm is obtained by estimating the mean $A$ simultaneously with the estimation of $\theta^{\ast}$: recursively define

<!-- chunk {"id": "body-0038", "role": "body", "section": "Stochastic Newton-Raphson", "weight": 1.0} -->

If the steady-state mean $A$ (defined in ) is invertible, then ${\hat{A}}_{n}$ is invertible for all $n$ sufficiently large.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Zap Stochastic Newton-Raphson", "weight": 1.0} -->

This is a two time-scales algorithm with a higher step-size for the matrix recursion.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Zap Stochastic Newton-Raphson", "weight": 1.0} -->

It is different from the original Stochastic Newton-Raphson algorithm because of the two time-scale construction: The second step-size sequence $\{\gamma_{n + 1}\}$ is non-negative, satisfies, and also

<!-- chunk {"id": "body-0041", "role": "body", "section": "Zap Stochastic Newton-Raphson", "weight": 1.0} -->

The asymptotic covariance is again optimal.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Zap Stochastic Newton-Raphson", "weight": 1.0} -->

This simplicity is also revealed in application to Q-learning, in which $A$ depends on the parameter.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Zap Stochastic Newton-Raphson", "weight": 1.0} -->

A key point to note here is that the Zap version of the SNR algorithm plays a significant role in analysis as well as in performance improvement of general non-linear function approximation problems. We briefly discuss these in the following.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Zap SNR for non-linear stochastic approximation", "weight": 1.0} -->

Consider a stochastic approximation algorithm of the form with ${\overline{f}{(\theta)}} = {\mathsf{E}{\lbrack{f{(\theta,\Phi)}}\rbrack}}$, a non-linear function of the parameter vector $\theta$. The ODE of the two algorithms: SNR and Zap-SNR look significantly different in this case; it is found that this difference is reflected in the rate of convergence of the stochastic recursion (as we will see in the case of Q-learning).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Zap SNR for non-linear stochastic approximation", "weight": 1.0} -->

Note that the function ${\nabla f}{(\theta_{n},\phi_{n + 1})}$ may or may not be readily accessible, and this is application specific. In the case of Q-learning with linear function approximation, though the function $f$ is iteslf non-linear in $\theta$, $\nabla f$ is readily computable.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Zap SNR for non-linear stochastic approximation", "weight": 1.0} -->

where once again the step-size sequence $\{\gamma_{n}\}$ satisfies, and.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Zap SNR for non-linear stochastic approximation", "weight": 1.0} -->

The general convergence and stability analysis of both and is open. In Section 3 we show that when applied to Q-learning, the algorithms do converge under certain technical conditions. However, the assumptions under which the single time-scale algorithm converges is far more restrictive than the assumptions under which the the two-time-scale algorithm converges.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

It is common to discard the idea of second order methods because of their computational complexity. Before we move on to the specific applications in Reinforcement Learning, we propose an enhancement of the SNR algorithms that will result in complexity that is comparable to first order methods.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

We believe that we have convinced the readers that the two-timescale Zap-SNR algorithm is of more interest to us (we will make this more precise in Section 3), and hence restrict to extensions of this algorithm here.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

It is assumed that there is no complexity in "calculating" the gradient function ${\nabla f}{( \cdot, \cdot )}$, and that it is readily available. This is not be true in all applications, but holds in the applications of interest in this paper. Under these assumptions, computational complexity arises from the operations that are performed in manipulating these quantities.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

The per-iteration complexity of the first order algorithm is $O{(d)}$, since $\theta \in {\mathbb{R}}^{d}$. If the algorithm is run for $T$ iterations (assuming we have a data sequence of length $T$), the total complexity is $O{({dT})}$. The per iteration complexity in the case of the Zap-SNR algorithm is $O{(d^{2})}$, because it involves the product of a matrix inverse (of dimension $d \times d$) and a vector (of dimension $d \times 1$). The total complexity of the algorithm after running for $T$ iterations is $O{({Td^{2}})}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

The essential idea behind the $O{(d)}$ Zap-SNR algorithm is to perform the $O{(d^{2})}$ complexity steps only once every $N \geq d$ iterations, so that the total computational complexity for a data sequence of length $T$ is $O{(\frac{Td^{2}}{N})}$; essentially resulting in the complexity of the first order method if $N = d$. This is done by "batching" the data sequence into mini-sequences of length $N$, and applying recursions for each batch as follows: For $i \geq 0$

<!-- chunk {"id": "body-0053", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

The first two definitions in (25 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) are straightforward; the expression for ${\hat{\gamma}}_{{i + 1},N}$ is obtained in such a way that the recursions in (24 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) very closely resemble the recursions in ^11^1This deserves more explanation and we plan to provide one in a future version of the paper..

<!-- chunk {"id": "body-0054", "role": "body", "section": "Dealing with complexity: An $O$($d$) Zap-SNR algorithm", "weight": 1.0} -->

A remarkable (but almost obvious) property of the $O{(d)}$ Zap-SNR algorithm (24 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) is that it has the same asymptotic properties (specifically, the asymptotic covariance) as that of the original Zap-SNR algorithm. This once again is made more precise in a future version of the paper. The specific application of this algorithm to Q-learning is discussed in Section 3.7 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning").

<!-- chunk {"id": "body-0055", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

The general theory is illustrated here, through application to TD($\lambda$)-learning algorithms.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

The standard operator-theoretic notation is used for conditional expectation: for any measurable function $f:{\mathsf{X}\rightarrow{\mathbb{R}}}$,

<!-- chunk {"id": "body-0057", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

Let $c:{\mathsf{X}\rightarrow{\mathbb{R}}_{+}}$ denote a cost function, and $\beta \in {}$ a discount factor. The discounted-cost value function is defined as $h = {\sum_{n = 0}^{\infty}{\beta^{n}P^{n}c}}$, which is the unique solution to the Bellman equation

<!-- chunk {"id": "body-0058", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

TD-learning algorithms are designed to obtain approximations of $h$ within a finite-dimensional parameterized class.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

Consider the case of a $d$-dimensional linear parameterization. A function $\psi:{\mathsf{X}\rightarrow{\mathbb{R}}^{d}}$ is chosen, which is viewed as a collection of $d$ basis functions. Each vector $\theta \in {\mathbb{R}}^{d}$ is associated with the approximate value function $h^{\theta} = {\sum_{i}{\theta_{i}\psi_{i}}}$. There are two standard criteria for defining optimality of the parameter.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

in which the choice of norm is part of the design of the algorithm. Most common is

<!-- chunk {"id": "body-0061", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

In the Galerkin approach, a $d$-dimensional stationary stochastic process $\mathbf{ζ}$ is constructed that is adapted to a stationary realization of $\mathbf{X}$. An algorithm is designed to obtain the vector $\theta^{\ast} \in {\mathbb{R}}^{d}$ that satisfies

<!-- chunk {"id": "body-0062", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

in which the expectation is again in steady state. The $d$-dimensional stochastic process $\mathbf{ζ}$ is called the sequence of eligibility vectors.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

The motivation for the first criterion is clear, but algorithms that solve this problem often suffer from high variance. The Galerkin approach is used because it is simple and generally applicable. Also, if the basis functions are chosen such that $h = h^{\theta^{\bullet}}$ for some $\theta^{\bullet} \in {\mathbb{R}}^{d}$, and if the solution to is unique, then the Galerkin approach will yield the exact solution $h$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Application to temporal-difference algorithms", "weight": 1.0} -->

The goal of the TD($\lambda$) learning algorithm is to solve the Galerkin relaxation in which the eligibility vectors are obtained by passing $\{{\psi{(X_{n})}}\}$ through the corresponding first-order low-pass filter: $\zeta_{n + 1} = {{\lambda\beta\zeta_{n}} + {\psi{(X_{n + 1})}}}$, $n \geq 0$. It is always assumed that $\lambda \in {\lbrack 0,1\rbrack}$. It is shown in that the solutions to the Galerkin fixed point equation and the minimum norm problem coincide if $\lambda = 1$, with the norm defined.

<!-- chunk {"id": "body-0065", "role": "body", "section": "TD($\\lambda$) algorithm", "weight": 1.0} -->

The recursion (30 algorithm: ‣ 2.4 Application to temporal-difference algorithms ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")) can be placed in the form in which $\Phi_{n} = {(X_{n},X_{n - 1},\zeta_{n - 1})}$, and

<!-- chunk {"id": "body-0066", "role": "body", "section": "TD($\\lambda$) algorithm", "weight": 1.0} -->

Based on this representation, it can be shown that the TD($\lambda$) algorithm is consistent provided the basis vectors are linearly independent, in the sense that ${\mathsf{E}_{\varpi}{\lbrack{\psi{(X_{n})}\psi{(X_{n})}^{\text{T}}}\rbrack}} > 0$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "TD($\\lambda$) algorithm", "weight": 1.0} -->

It is also easy to construct an example for which the asymptotic covariance is infinite: Take any consistent example, and scale the basis vectors by a small constant $\varepsilon$. Using the basis $\varepsilon\psi$, the resulting matrix $A$ is scaled by $\varepsilon^{2}$. Hence, for sufficiently small $\varepsilon > 0$, each eigenvalue of $A$ will have real part that is strictly greater than $- {1/2}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "TD($\\lambda$) algorithm", "weight": 1.0} -->

An application of the SNR matrix gain algorithm results in an algorithm with optimal asymptotic covariance.

<!-- chunk {"id": "body-0069", "role": "body", "section": "TD($\\lambda$) algorithm", "weight": 1.0} -->

The following proposition follows directly from Prop. 2.2:

<!-- chunk {"id": "body-0070", "role": "body", "section": "Q-Learning", "weight": 1.0} -->

The class of algorithms considered next is designed for a controlled Markov model, whose input process is denoted $\mathbf{U}$. It is assumed that the state space $\mathsf{X}$ and the action space $\mathsf{U}$ on which $\mathbf{U}$ evolves are both finite. Denote $\ell = {|\mathsf{X}|}$ and $\ell_{u} = {|\mathsf{U}|}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Q($\\lambda$) algorithm", "weight": 1.0} -->

The success of this approach has been demonstrated in a few restricted settings, such as optimal stopping problems, deterministic models, and variations of Watkins algorithm that are discussed next.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

The basic Q-learning algorithm of is a particular instance of the Galerkin approach with $\lambda = 0$ in (46 algorithm: ‣ 3.1 Notation and assumptions ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

where $\{{(x^{k},u^{k})}:{1 \leq k \leq d}\}$ is an enumeration of all state-input pairs. The goal of this approach is to compute the function $Q^{\ast}$ exactly.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

Only one entry of the approximation is updated at each time point, corresponding to the previous state-input pair $(X_{n},U_{n})$ observed.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

Assumption Q1: The input is defined by a randomized stationary policy of the form. The joint process $({\mathbf{X}},{\mathbf{U}})$ is an irreducible Markov chain. That is, it has a unique invariant pmf $\varpi$ satisfying ${\varpi{(x,u)}} > 0$ for each $x,u$. $\sqcap$$\sqcup$

<!-- chunk {"id": "body-0076", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

Assumption Q2: The optimal policy $\phi^{\ast}$ is unique. $\sqcap$$\sqcup$

<!-- chunk {"id": "body-0077", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

in which ${{\underset{¯}{q}}_{t}{(x)}} = {{\min_{u}q_{t}}{(x,u)}}$ as defined below. This ODE is stable under Assumption Q1, which then implies that the parameter estimates converge to $Q^{\ast}$ a.s..

<!-- chunk {"id": "body-0078", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

Under Assumption Q2 there exists $\varepsilon > 0$ such that

<!-- chunk {"id": "body-0079", "role": "body", "section": "Watkins algorithm", "weight": 1.0} -->

Although the algorithm is consistent, it should be clear that the asymptotic covariance of this algorithm is typically infinite.

<!-- chunk {"id": "body-0080", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

3: ϕnXn + 1:= arg min uQθn (Xn + 1,u);
4: dn + 1:= c (Xn,Un) + β Qθn (Xn + 1,ϕnXn + 1) − Qθn (Xn,Un);⊳ Temporal difference term
6: Ân + 1 = Ân + γn + 1 [An + 1−Ân];⊳ Matrix gain update rule
7: θn + 1 = θn − αn + 1 Ân + 1−1 ζn dn + 1;⊳ Zap-Q update rule
8: ζn + 1:= λ β ζn + ψ (Xn + 1,Un + 1);⊳ Eligibility vector update rule
Algorithm 1 Zap-Q(λ) algorithm

<!-- chunk {"id": "body-0081", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

It is assumed that a projection is employed to ensure that $\{{\hat{A}}_{n}^{- 1}\}$ is a bounded sequence --- this is most easily achieved using the Matrix Inversion Lemma.

<!-- chunk {"id": "body-0082", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

The analysis that follows is specialized to $\lambda = 0$ and the basis that is used in Watkins' algorithm.

<!-- chunk {"id": "body-0083", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

An equivalent representation for the parameter recursion (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) is

<!-- chunk {"id": "body-0084", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

in which $c$ and $\theta_{n}$ are treated as $d$-dimensional vectors rather than functions on $\mathsf{X} \times \mathsf{U}$, and

<!-- chunk {"id": "body-0085", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

It would seem that the analysis is complicated by the fact that the sequence $\{ A_{n}\}$ depends upon $\{\theta_{n}\}$ through the policy sequence $\{\phi_{n}\}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "$\\mathbf{G}$-Q($\\lambda$) algorithm", "weight": 1.0} -->

where $\Pi$ is the $d \times d$ diagonal matrix with entries ${{\Pi{(k,k)}}:=\varpi}{(x^{k},u^{k})}$. This admits a very simple recursion in the special case ${\mathbf{γ}} \equiv {\mathbf{α}}$. In the other case considered, wherein the step-size sequence $\mathbf{γ}$ satisfies, the recursion for $\hat{\mathbf{C}}$ is more complex, but the ODE analysis is simplified.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Main results", "weight": 1.0} -->

Conditions for convergence of the Zap-Q algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) are summarized in Thm. 3.4. The following assumption is used to address the discontinuity in the recursion for $\{{\hat{A}}_{n}\}$ resulting from the dependence of $A_{n + 1}$ on $\phi_{n}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "ODE and Policy Iteration", "weight": 1.0} -->

Recall the definition of $\partial\mathcal{Q}_{\mu}$. The ODE approximation can be expressed

<!-- chunk {"id": "body-0089", "role": "body", "section": "ODE and Policy Iteration", "weight": 1.0} -->

where $\mu_{t}$ is any pmf satisfying ${\partial{\mathcal{Q}_{\mu_{t}}c_{t}}} = q_{t}$, and the derivative exists for a.e. $t$ (see Lemma A.10 for full justification). This has an interesting geometric interpretation. Without loss of generality, assume that the cost function is non-negative, so that $\mathbf{q}$ evolves in the positive orthant ${\mathbb{R}}_{+}^{d}$ whenever its initial condition lies in this domain.

<!-- chunk {"id": "body-0090", "role": "body", "section": "ODE and Policy Iteration", "weight": 1.0} -->

A typical solution to the ODE is shown in Fig. 1: the trajectory is piecewise linear, with changes in direction corresponding to changes in the policy $\phi^{q_{t}}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Overview of proofs", "weight": 1.0} -->

This final subsection is dedicated to the proof of Prop. 3.5, and the main ideas in the proof of Thm. 3.4. It is assumed throughout the remainder of this section that Assumptions Q1--Q3 hold. Proofs of technical lemmas are contained in Appendix A.3.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Overview of proofs", "weight": 1.0} -->

We require the usual probabilistic foundations: There is a probability space $(\Omega,\mathcal{F},\mathsf{P})$ that supports all random variables under consideration. The probability measure $\mathsf{P}$ may depend on an initialization of the Markov chain. All stochastic processes under consideration are assumed adapted to a filtration denoted $\{\mathcal{F}_{n}:{n \geq 0}\}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Overview of proofs", "weight": 1.0} -->

We begin with the proof of the simpler Prop. 3.5.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Inverse Dynamic Programming Analysis", "weight": 1.0} -->

Prop. 3.5 is a quick consequence of the following extension of Prop. 2.2:

<!-- chunk {"id": "body-0095", "role": "body", "section": "ODE Analysis", "weight": 1.0} -->

The remainder of this section is devoted to a high-level view of the proof of the ODE approximation for the two time-scale algorithm, with $\mathbf{α}$ and $\mathbf{γ}$ defined.

<!-- chunk {"id": "body-0096", "role": "body", "section": "ODE Analysis", "weight": 1.0} -->

The construction of an approximating ODE involves first defining a continuous time process. Denote

<!-- chunk {"id": "body-0097", "role": "body", "section": "ODE Analysis", "weight": 1.0} -->

and define ${\overline{q}}_{t_{n}} = \theta_{n}$ for these values, with the definition extended to ${\mathbb{R}}_{+}$ via linear interpolation. We say that the ODE approximation ${\frac{d}{dt}q} = {f{(q)}}$ holds if we have the approximation,

<!-- chunk {"id": "body-0098", "role": "body", "section": "ODE Analysis", "weight": 1.0} -->

where the error process satisfies, for each $T > 0$,

<!-- chunk {"id": "body-0099", "role": "body", "section": "ODE Analysis", "weight": 1.0} -->

The significance of this representation is that $q_{t}$ is the Q-function associated with the "cost function" $c_{t}$: $q_{t} = {\mathcal{Q}{(c_{t})}}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "ODE Analysis", "weight": 1.0} -->

To construct an ODE, it is convenient first to obtain an alternative and suggestive representation for the pair of equations (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")). A vector-valued sequence of random variables $\{\mathcal{E}_{k}\}$ will be called ODE-friendly if it admits the decomposition,

<!-- chunk {"id": "body-0101", "role": "body", "section": "An $O{(d)}$ Zap-Q learning algorithm", "weight": 1.0} -->

In this subsection, we introduce an $O{(d)}$ Zap-Q learning algorithm, which is basically the $O{(d)}$ Zap-SNR algorithm described in Section 2.3.2 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning") specialized to Q-learning.

<!-- chunk {"id": "body-0102", "role": "body", "section": "An $O{(d)}$ Zap-Q learning algorithm", "weight": 1.0} -->

Based on the equations (24 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")), (25 Zap-SNR algorithm ‣ 2.3 Zap Stochastic Newton-Raphson ‣ 2 Stochastic Newton Raphson and TD-Learning ‣ Fastest Convergence for Q-Learning")), (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")), and (54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")), the algorithm is defined as follows: Fix $N = d$, and for $i \geq 0$,

<!-- chunk {"id": "body-0103", "role": "body", "section": "An $O{(d)}$ Zap-Q learning algorithm", "weight": 1.0} -->

Once again, we claim that the asymptotic properties of the above defined $O{(d)}$ Zap-Q learning algorithm is the same as that of the Zap-Q learning algorithm defined in (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) and (54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")), with justification postponed to a future version of the paper.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Results from numerical experiments are surveyed here to illustrate the performance of the Zap Q-learning algorithm (53 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning"),54 algorithm: ‣ 3.3 SNR and Zap Q-Learning ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")). Comparisons are made with several existing algorithms, including Watkins Q-learning, Watkins Q-learning with Ruppert-Polyak-Juditsky (RPJ) averaging, Watkins Q-learning with a "polynomial learning rate", and the more recent *Speedy Q-learning* algorithm.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

In addition, the Watkins algorithm with a scalar gain $g$ is considered, with $g$ chosen so that the algorithm has finite asymptotic covariance. When the value of $g$ is optimized and numerical conditions are favorable (e.g., the condition number of $A$ is not too large) it is found that the performance is nearly as good as the Zap-Q algorithm.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Design of the scalar gain $g$ depends on approximation of $A$, and hence $\theta^{\ast}$. While it is possible to estimate $A$ via Monte-Carlo in Zap Q-learning, it is not known how to efficiently update approximations for an optimal scalar gain.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

A reasonable asymptotic covariance required a large value of $g$. Consequently, the scalar gain algorithm had massive transients, resulting in a poor performance in practice.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Transient behavior could be tamed through projection to a bounded set. However, this again requires prior knowledge of the region in the parameter space to which $\theta^{\ast}$ belongs.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Projection of parameters was also necessary for RPJ averaging.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

The following batch mean method was used to estimate the asymptotic covariance.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Batch Mean Method", "weight": 1.0} -->

At stage $n$ of the algorithm we will be interested in the distribution of a vector-valued random variable of the form $f_{n}{(\theta_{n})}$, where $f_{n}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{m}}$ is possibly dependent on $n$. The batch mean method is used to estimate its statistics: For each algorithm, $N$ parallel simulations are run with $\theta_{0}$ initialized i.i.d. according to some distribution. Denoting $\theta_{n}^{i}$ to be the vector $\theta_{n}$ corresponding to the $i^{th}$ simulation, the distribution of the random variable $f_{n}{(\theta_{n})}$ is estimated based on the histogram of the independent samples $\{{f_{n}{(\theta_{n}^{i})}}:{1 \leq i \leq N}\}$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Batch Mean Method", "weight": 1.0} -->

The estimate of the covariance of $f_{n}{(\theta_{n})}$ is then obtained as the sample covariance of $\{{{W_{n}^{i},\, 1} \leq i \leq N}\}$. This corresponds to the estimate of the asymptotic covariance $\Sigma_{\theta}$ defined.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Batch Mean Method", "weight": 1.0} -->

The value $N = 10^{3}$ is used in all of the experiments surveyed here.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

Consider first a simple stochastic-shortest-path problem. The state space $\mathsf{X} = {\{ 1,\ldots,6\}}$ coincides with the six nodes on the un-directed graph shown in Fig. 2. The action space $\mathsf{U} = {\{ e_{x,x^{\prime}}\}}$, ${x,x^{\prime}} \in \mathsf{X}$, consists of all feasible edges along which an agent can travel, including each "self-loop", $u = e_{x,x}$. The number of state-action pairs for this example coincides with the number of nodes plus twice the number of edges: $d = 18$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

The controlled transition matrix is defined as follows: If $X_{n} = x \in \mathsf{X}$, and $U_{n} = e_{x,x^{\prime}} \in \mathsf{U}$, then $X_{n + 1} = x^{\prime}$ with probability $0.8$, and with probability $0.2$, the next state is randomly chosen between all neighboring nodes. The goal is to reach the state $x^{\ast} = 6$ and maximize the time spent there. This is modeled through a discounted-reward optimality criterion with discount factor $\beta \in {}$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

The solution to the discounted-cost optimal control problem can be computed numerically for this model; the optimal policy is unique and independent of $\beta$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

Watkins' algorithm with scalar gain $g$, so that $\alpha_{n} \equiv {g/n}$

<!-- chunk {"id": "body-0118", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

Watkins' algorithm using RPJ averaging, with $\gamma_{n} \equiv {(\alpha_{n})}^{0.6} \equiv n^{- 0.6}$

<!-- chunk {"id": "body-0119", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

Watkins' algorithm with the polynomial learning rate $\alpha_{n} \equiv n^{- 0.6}$

<!-- chunk {"id": "body-0120", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

The basis was taken to be the same as in Watkins Q-learning algorithm. In each case, the randomized policy was taken to be uniform: feasible transitions were sampled uniformly at each time.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Finite state-action MDP", "weight": 1.0} -->

Discount factors $\beta = 0.8$ and $\beta = 0.99$ were considered. In each case, the unique optimal parameter $\theta^{\ast} = Q^{\ast}$ was obtained numerically.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

Speedy Q-learning cannot be represented as a standard stochastic approximation, so standard theory cannot be applied to obtain its asymptotic covariance. The Watkins' algorithm with polynomial learning rate has infinite asymptotic covariance.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

For the other four algorithms, the asymptotic covariance $\Sigma_{\theta}$ was computed by solving the Lyapunov equation based on the matrix gain $G$ that is particular to each algorithm. Recall that $G = {- A^{- 1}}$ in the case of either of the Zap-Q algorithms.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

The matrices $A$ and $\Sigma_{\Delta}$ appearing in are defined with respect to Watkins' Q-learning algorithm with $\alpha_{n} = {1/n}$. The first matrix is $A = {- {\Pi{\lbrack{I - {\betaPS_{\phi^{\ast}}}}\rbrack}}}$ under the standing assumption that the optimal policy is unique.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

Uniqueness of the optimal policy implies that $\overline{f}$ is locally linear: there exists $\varepsilon > 0$ such that

<!-- chunk {"id": "body-0126", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

The matrix $\Sigma_{\Delta}$ was also obtained numerically, without resorting to simulation.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

The eigenvalues of the $18 \times 18$ matrix $A$ are real in this example, as shown in Fig. 3 for both values of $\beta$. To ensure that the eigenvalues of $gA$ are all strictly less than $- {1/2}$ in a scalar gain algorithm requires the (approximate) lower bounds $g > 45$ for $\beta = 0.8$, and $g > 900$ for $\beta = 0.99$. Thm. 2.1 implies that the asymptotic covariance $\Sigma_{\theta}{(g)}$ is finite for this range of $g$ in the Watkins algorithm with $\alpha_{n} \equiv {g/n}$. Fig. 4 shows the normalized trace of the asymptotic covariance as a function of $g > 0$, and the significance of $g \approx 45$ and $g \approx 900$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

Based on this analysis or on Thm. 3.3, it follows that the asymptotic covariance is not finite for the standard Watkins' algorithm with $\alpha_{n} \equiv {1/n}$. In simulations it was found that the parameter estimates are not close to $\theta^{\ast}$ even after many millions of samples. This is illustrated for the case $\beta = 0.8$ in Fig. 5, which shows a histogram of $10^{3}$ estimates of $\theta_{n}{}$ with $n = 10^{6}$ (other entries showed similar behavior).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

It was found that the algorithm performed very poorly in practice for any scalar gain algorithm. For example, more than half of the $10^{3}$ experiments using $\beta = 0.8$ and $g = 70$ resulted in values of $\theta_{n}{}$ exceeding $\theta^{\ast}{}$ by $10^{4}$ (with ${\theta^{\ast}{}} \approx 500$), even with $n = 10^{6}$. The algorithm performed well with the introduction of projection in the case $\beta = 0.8$. With $\beta = 0.99$, the performance was unacceptable for any scalar gain, even with projection.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

The results presented next used a gain of $g = 70$ in the case $\beta = 0.8$, and projection of each entry of the estimates to the interval $({- \infty},1000\rbrack$. Fig. 6 shows normalized histograms of $\{{W_{n}^{i}{(k)}}:{1 \leq i \leq N}\}$, as defined, with $k = {10,18}$.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

The Central Limit Theorem holds: $W_{n}$ is expected to be approximately normally distributed: $\mathcal{N}{(0,{\Sigma_{\theta}{(g)}})}$, when $n$ is large. Of the $d = 18$ entries of the vector $W_{n}$, with $n \geq 10^{4}$, it was found that the asymptotic variance matched the histogram nearly perfectly for $k = 10$, while $k = 18$ showed the worst fit.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Asymptotic Covariance", "weight": 1.0} -->

These experiments were repeated for each of the Zap-Q algorithms, for which the asymptotic variance $\Sigma^{\ast}$ is obtained using the formula. Plots are shown only for Case 2: the two time-scale algorithm, with $\gamma_{n} = {(\alpha_{n})}^{0.85}$. Histograms in the case of $\beta = 0.8$ are shown in Fig. 7, and Fig. 8 for $\beta = 0.99$. The covariance estimates and the Gaussian approximations match the theoretical predictions remarkably well for $n \geq 10^{4}$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Bellman Error", "weight": 1.0} -->

the sequence $\{{\sqrt{n}{\overline{\mathcal{B}}}_{n}}\}$ also converges in distribution as $n\rightarrow\infty$. Fig. 9 contains plots of $\{{\overline{\mathcal{B}}}_{n}\}$ for the six different Q-learning algorithms.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Bellman Error", "weight": 1.0} -->

For large $n$, the two versions of Zap Q-learning exhibit similar behavior since ${\hat{A}}_{n}$ converges to $A$ in both algorithms. Though all six algorithms perform reasonably well when $\beta = 0.8$, Zap Q-learning is the only one that achieves near zero Bellman error within $n = 10^{6}$ iterations in the case $\beta = 0.99$. Moreover, the performance of the two time-scale algorithm is clearly superior to the one time-scale algorithm.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Bellman Error", "weight": 1.0} -->

Fig. 9 shows only the typical behavior --- repeated trails were run to investigate the range of possible outcomes. For each algorithm, the outcomes of $N = 1000$ independent simulations resulted in samples $\{{{{\overline{\mathcal{B}}}_{n}^{i},\, 1} \leq i \leq N}\}$, with $\theta_{0}$ uniformly distributed on the interval $\lbrack{- 10^{3}},10^{3}\rbrack$ for $\beta = 0.8$ and $\lbrack{- 10^{4}},10^{4}\rbrack$ for $\beta = 0.99$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Bellman Error", "weight": 1.0} -->

The batch means method was used to obtain estimates of the mean and variance of ${\overline{\mathcal{B}}}_{n}$ for a range of values of $n$. Plots of the mean and $2\sigma$ confidence intervals are shown in Fig. 10 for the case $\beta = 0.8$, and plots for $\beta = 0.99$ are shown in Fig. 11.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Bellman Error", "weight": 1.0} -->

Fig. 12 and Fig. 13 shows histograms of $\{{{{\overline{\mathcal{B}}}_{n}^{i},\, 1} \leq i \leq N}\}$, ${n = 10^{6}},$ for all the six algorithms; this corresponds to the data shown in Fig. 10 and Fig. 11 at $n = 10^{6}$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Performance of the $O{(d)}$ Zap-Q learning algorithm", "weight": 1.0} -->

In this subsection, we test the performance of the $O{(d)}$ Zap-Q learning algorithm that was defined in equations (74 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) and (75 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning")) of Section 3.7 Zap-Q learning algorithm ‣ 3 Q-Learning ‣ Fastest Convergence for Q-Learning") by applying it to the stochastic shortest path problem. We restrict to the comparison of the Bellman errors (defined in ) of the different algorithms, and we consider the case $\beta = 0.99$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Performance of the $O{(d)}$ Zap-Q learning algorithm", "weight": 1.0} -->

Fig. 14 Zap-Q learning algorithm ‣ 4.1 Finite state-action MDP ‣ 4 Numerical Results ‣ Fastest Convergence for Q-Learning") contains plots of $\{{\overline{\mathcal{B}}}_{n}\}$ for the different Q-learning algorithms. For the $O{(d)}$ Zap-Q learning algorithms, the batch size was set to $N = 100$ ($d = 18$ in this problem). We notice in the figure that the $O{(d)}$ algorithm performs nearly as well as the $O{(d^{2})}$ algorithm when the step-sizes (${\hat{\gamma}}_{i}$) are chosen appropriately. Furthermore, the naive batching technique applied to a single-time-scale Stochastic Newton-Raphson algorithm ($\gamma_{n} \equiv \alpha_{n}$ and therefore ${\hat{\gamma}}_{i} \approx \alpha_{i}$) performs extremely poorly.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Finance model", "weight": 1.0} -->

The next example is taken. The reader is referred to these references for complete details of the problem set-up and the reinforcement learning architecture used in this prior work. The example is of interest because it shows how the Zap Q-learning algorithm can be used with a more general basis, and also how the technique can be extended to optimal stopping time problems.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Finance model", "weight": 1.0} -->

in which $\{{\overset{\sim}{p}}_{t}:{t \in {\mathbb{R}}}\}$ is a geometric Brownian motion (derived from an exogenous price-process). This uncontrolled Markov chain is positive Harris recurrent on the state space $\mathsf{X} \equiv {\mathbb{R}}^{100}$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Finance model", "weight": 1.0} -->

A stationary policy $\phi:{\mathsf{X}\rightarrow{\{ 0,1\}}}$ assigns an action for each state $x \in \mathsf{X}$ as

<!-- chunk {"id": "body-0143", "role": "body", "section": "Finance model", "weight": 1.0} -->

Each policy $\phi$ defines a stopping time and associated average reward, denoted

<!-- chunk {"id": "body-0144", "role": "body", "section": "Finance model", "weight": 1.0} -->

The objective here is to find an approximation for $Q^{\ast}$ in a parameterized class $\{{{Q^{\theta}:=\theta^{\text{T}}}\psi}:{\theta \in {\mathbb{R}}^{d}}\}$, where $\psi:{\mathsf{X}\rightarrow{\mathbb{R}}^{d}}$ is a vector of basis functions. For a fixed parameter vector $\theta$, the associated value function is denoted

<!-- chunk {"id": "body-0145", "role": "body", "section": "Finance model", "weight": 1.0} -->

The function $h_{\phi^{\theta}}$ was estimated using Monte-Carlo in the numerical experiments surveyed below.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Approximations to the Optimal Stopping Time Problem", "weight": 1.0} -->

This is one of the few parameterized Q-learning settings for which convergence is guaranteed.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Approximations to the Optimal Stopping Time Problem", "weight": 1.0} -->

where $g$ and $b$ are positive constants.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Approximations to the Optimal Stopping Time Problem", "weight": 1.0} -->

Through trial and error the authors find that $g = 10^{2}$, $b = 10^{4}$ gives good performance. These values were also used in the experiments described in the following.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Approximations to the Optimal Stopping Time Problem", "weight": 1.0} -->

The limiting matrix gain is given by

<!-- chunk {"id": "body-0150", "role": "body", "section": "Approximations to the Optimal Stopping Time Problem", "weight": 1.0} -->

where the expectation is in steady-state. The asymptotic covariance $\Sigma_{\theta}^{G}$ is the unique positive semi-definite solution to the Lyapunov equation, provided all eigenvalues of $GA$ satisfy ${\text{Re}{(\lambda)}} < {- \frac{1}{2}}$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The experimental setting of is used to define the set of basis functions and other parameters. The dimension of the parameter vector $d$ was chosen to be $10$, with the basis functions defined. The objective here is to compare the performances of $\mathbf{G}$-Q($0$) and the Zap-Q algorithms in terms of both parameter convergence, and with respect to the resulting average reward.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The asymptotic covariance matrices $\Sigma^{\ast}$ and $\Sigma_{\theta}^{G}$ were estimated through the following steps: The matrices $A$ and $G$ were estimated via Monte-Carlo. Estimation of $A$ requires an estimate of $\theta^{\ast}$; this was taken to be $\theta_{n}$, with $n = {2 \times 10^{6}}$, obtained using the Zap-Q two timescale algorithm with $\alpha_{n} \equiv {1/n}$ and $\gamma_{n} \equiv \alpha_{n}^{0.85}$. This estimate of $\theta^{\ast}$ was also used to estimate the covariance matrix $\Sigma_{\Delta}$ defined in using the batch means method. The matrices $\Sigma_{\theta}^{G}$ and $\Sigma^{\ast}$ were then obtained using and, respectively.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

It was found that the trace of $\Sigma_{\theta}^{G}$ was about $15$ times greater than that of $\Sigma^{\ast}$.

<!-- chunk {"id": "body-0154", "role": "body", "section": "High performance despite ill-conditioned matrix gain", "weight": 1.0} -->

The real part of the eigenvalues of $A$ are shown on a logarithmic scale on the left-hand side of Fig. 15. The eigenvalues of the matrix $A$ have a wide spread: The condition-number is of the order $10^{4}$. This presents a challenge in applying any method. In particular, it was found that the performance of any scalar-gain algorithm was extremely poor, even with projection of parameter estimates.

<!-- chunk {"id": "body-0155", "role": "body", "section": "High performance despite ill-conditioned matrix gain", "weight": 1.0} -->

This is a consequence of the fact that the basis functions $\{\psi_{i}\}$ are nearly linearly dependent. A better basis should be considered in future work, but the main objective here is to test the new methods in a challenging setting, and to compare with prior approaches.

<!-- chunk {"id": "body-0156", "role": "body", "section": "High performance despite ill-conditioned matrix gain", "weight": 1.0} -->

In applying the Zap Q-learning algorithm it was found that the estimates $\{{\hat{A}}_{n}\}$ in are nearly singular. Despite the unfavorable setting for this approach, the performance of the algorithm was much better than any alternative that was tested. The upper row of Fig. 16 contains normalized histograms of $\{{{W_{n}^{i}{(k)}} = {\sqrt{n}{({{\theta_{n}^{i}{(k)}} - {{\overline{\theta}}_{n}{(k)}}})}}}:{1 \leq i \leq N}\}$ for the Zap-Q algorithm. The variance for finite $n$ is close to the theoretical predictions based on the asymptotic covariance $\Sigma^{\ast}$. The histograms were generated for two values of $n$, and $k = {1,7}$.

<!-- chunk {"id": "body-0157", "role": "body", "section": "High performance despite ill-conditioned matrix gain", "weight": 1.0} -->

Of the $d = 10$ possibilities, the histogram for $k = 1$ had the worst match with theoretical predictions, and $k = 7$ was the closest.

<!-- chunk {"id": "body-0158", "role": "body", "section": "High performance despite ill-conditioned matrix gain", "weight": 1.0} -->

The eigenvalues corresponding to the matrix $GA$ are shown on the right hand side of Fig. 15. It is found that one of these eigenvalues is very close to $- 0.5$, and the sufficient condition for ${\text{trace~}{(\Sigma_{\theta}^{G})}} < \infty$ is barely satisfied. It is worth stressing that the finite asymptotic covariance was not a design goal in this prior work. It is only now on revisiting this paper that we find that the sufficient condition $\lambda < {- \frac{1}{2}}$ is satisfied.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Asymptotic variance of the discounted reward", "weight": 1.0} -->

Denote $h_{n} = h_{\phi}$, with $\phi = \phi^{\theta_{n}}$. Histograms of the average reward $h_{n}{(x)}$ were obtained for ${x{(i)}} = 1$, $1 \leq i \leq 100$, and various values of $n$, based on $N = 1000$ independent simulations. The plots shown in Fig. 17 are based on $n = {2 \times 10^{k}}$, for $k = {4,5,6}$. Omitted in this figure are outliers: values of the reward in the interval $\lbrack 0,1)$. Table 1 lists the number of outliers for each $n$ and each algorithm.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Asymptotic variance of the discounted reward", "weight": 1.0} -->

Recall that the asymptotic covariance of the $\mathbf{G}$-Q($0$) algorithm was not far from optimal (its trace was about 15 times larger than obtained using Zap Q-learning). However, it is observed that this algorithm suffers from much larger outliers. It can also be seen that doubling the scalar gain $g$ (causing the largest eigenvalue of $GA$ to be $\approx {- 1}$) results in slightly better performance.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Watkins' Q-learning algorithm is elegant, but subject to two common and valid constraints: it can be very slow to converge, and it is not obvious how to extend this approach to obtain a stable algorithm in non-trivial parameterized settings. This paper addresses both concerns with the new Zap Q($\lambda$) algorithms that are motivated by asymptotic theory of stochastic approximation.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Conclusions", "weight": 1.0} -->

There are many avenues for future research. It would be valuable to find an alternative to Assumption Q3 that is readily verified. Based on the ODE analysis, it seems likely that the conclusions of Thm. 3.4 hold without this additional assumption. No theory has been presented here for non-ideal parameterized settings. It is conjectured that conditions for stability of Zap Q($\lambda$)-learning will hold under general conditions. Consistency is a more challenging problem and is a focus of current research.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In terms of algorithm design, it is remarkable to see how well the scalar-gain algorithms perform, provided projection is employed and the condition number of $A$ is not too large. It is possible to estimate the optimal scalar gain based on estimates of the matrix $A$ that is central to this paper. How to do so without introducing high complexity is an open question.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Conclusions", "weight": 1.0} -->

On the other hand, the performance of RPJ averaging is unpredictable. In many experiments it is found that the asymptotic covariance is a poor indicator of finite-$n$ performance when using this approach. There are many suggestions in the literature for improving this technique (see discussion after Theorem 3 of ).

<!-- chunk {"id": "body-0165", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The results in this paper suggest new approaches that we hope will simultaneously

<!-- chunk {"id": "body-0166", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Reduce complexity and potential numerical instability of matrix inversion,

<!-- chunk {"id": "body-0167", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Maintain optimality of the asymptotic covariance
