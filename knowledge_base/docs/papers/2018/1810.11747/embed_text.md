<!-- arxiv-full-text:v1 {"arxiv_id": "1810.11747", "source": "ar5iv"} -->

## Introduction

Nonlinear dynamical models possess the capacity to represent a variety of real-world systems and have been employed in different areas such as automatic control, robotics, autonomy and so . A most common approach to obtaining a nonlinear model is via the first principle, which requires a good understanding of the underlying physics. In many cases, this requirement is however not realistic. Therefore, a data-driven approach using generated data samples to build a nonlinear model is becoming more and more critical. This is known as the system identification problem in control theory.

Compared to that of linear systems, the system identification problems for nonlinear dynamics are considerably more difficult. There have been many works on this topic, and many algorithms have been proposed. Most of these works focus on the asymptotical performance of the algorithms, which copes with the situation when the amount of data available goes to infinity. A critical question pertains to the data efficiency hasn't been adequately addressed yet. How many data points do we need to recover a dynamical model to a certain precision?

It turns out that this question falls into the scope of sample complexity theory, which is a key mathematical tool in theoretical machine learning. This tool is used to analyze the performance guarantee of machine learning models. Many fundamental results have been established along this line in supervised learning. This attempt is not so successful in reinforcement learning, especially when the state space is continuous as in most control applications. Recently, as the first step in this direction, some sample complexity results for data-driven linear quadratic regulator problems.

The purpose of this work is to establish sample complexity results for nonlinear dynamics. To achieve this goal, we use a linear operator theoretic framework involving transfer Koopman and Perron-Frobenius (P-F) operators for linear representation and modeling of a nonlinear system. Linear operator theoretic framework has attracted lot of attention lately from the theoretical and applied dynamical system communities. One of the features that makes this approach attractive is its ability to approximate complicated and complex nonlinear dynamical system from time-series data. The basic idea behind the linear operator framework is to lift the nonlinear finite dimensional evolution of a dynamical system in the state space to linear albeit infinite dimensional evolution of functions in the functional space. Various algorithms are proposed for the finite dimensional approximation of these linear operators. However, to the best of authors knowledge, the problem of deriving sample complexity results for these operators has not been addressed yet. The linear nature of these operators allows us to carry out sample complexity analysis similar to the one developed for the case of a linear system but in the lifted functional space. We believe that sample complexity for a nonlinear system will play a fundamental role in our understanding of reinforcement learning algorithms, one of the fast-growing area of machine learning.

The paper is organized as follows. In Section II we introduce linear operator framework involving Koopman and P-F operators. The result on sample complexity is presented in Section III. We provide several examples in Section IV to illustrate our results. This follows by a short concluding remark in Section V.

## Preliminaries

In this section, we provide brief overview of the theory behind linear operator involving P-F and Koopman operator. For more details please refer to.

Consider a discrete-time dynamical system where $T:{X\rightarrow X \subset {\mathbb{R}}^{n}}$ with $X$ assumed to be compact. Associated with this dynamical system are two linear operators namely Koopman and Perron-Frobenius operator are are defined as follows.

### Definition 1 (P-F operator)

Let $L_{2}{(X)}$ be the space of square integrable functions. Under the assumption that the mapping $T$ is invertible, the P-F operator ${\mathbb{P}}_{T}:{{L_{2}{(X)}}\rightarrow{L_{2}{(X)}}}$ is defined as follows. where $| \cdot |$ stands for the matrix determinant.

### Remark 2

The P-F operator can also be defined without the restrictive invertibility assumption on the mapping $T$ on the space of measures. For more details on this please refer to.

### Definition 3 (Koopman Operator)

The Koopman operator ${\mathbb{U}}_{T}:{{L_{2}{(X)}}\rightarrow{L_{2}{(X)}}}$ is defined as The P-F and Koopman operators are dual to each other in the sense that The duality can be expressed compactly as These definitions extends to the setting of random dynamical systems. Consider the random dynamical system where $\xi_{0},\xi_{1},\ldots$ are assumed to independent identical distributed random vectors. One case of particular interest is which is a deterministic system perturbed by random noise $\xi$.

Next we provide definitions for the P-F and Koopman operators for the random dynamical system. We will use the same notation for the representing these operators for the deterministic and random dynamical systems.

### Definition 4 (P-F operator)

The P-F operator ${\mathbb{P}}_{F}:{{L_{2}{(X)}}\rightarrow{L_{2}{(X)}}}$ for the random dynamical system is defined as where $\rho{(\cdot)}$ is the probability density of $\xi$.

### Definition 5 (Koopman Operator)

The Koopman operator ${\mathbb{U}}_{F}:{{L_{2}{(X)}}\rightarrow{L_{2}{(X)}}}$ is defined as where the expectation is taken with respect to $\xi$.

Again the duality between the P-F and Koopman operator follows in the random setting and equality is true for P-F and Koopman operator as defined in Eqs. (6 ‣ II Preliminaries ‣ Sample Complexity for Nonlinear Dynamics"))-(7 ‣ II Preliminaries ‣ Sample Complexity for Nonlinear Dynamics")). This duality between the Koopman and P-F operator is exploited to propose finite dimensional approximation of the P-F operator using numerical algorithm developed for the approximation of Koopman operator.

## Sample Complexity of Koopman and Perron-Frobenius Operators

Linear operator theoretic framework involving P-F and Koopman operator provides a powerful tool for the representation, analysis, and design of nonlinear dynamical systems. Our objective in this section is to derive sample complexity results for the finite dimensional approximation of these linear operators. Although several algorithms are proposed for the finite dimensional approximation of the Koopman operators from time series data, the fundamental principle behind these different algorithms remains the same. Hence, the sample complexity results that we derive, using extended dynamic mode decomposition (EDMD) algorithm and its modification for the approximation of P-F operator, should apply to other algorithms as well.

For the finite dimensional approximation, let be data points generated by random dynamical system through experiments or simulations. Note that here $y_{k} = {F{(x_{k},\xi_{k})}}$. These data samples could be from a single trajectory, in which case $y_{k} = x_{k + 1}$, or different trajectories.

To establish a finite dimensional approximation of a Koopman operator we first choose a set of finite many basis functions A corresponding approximation of a Koopman operator is nothing but its projection on this basis. More specifically, if for some matrix $\mathbf{K}$ with $r_{k}{(\cdot)}$ being almost perpendicular to the linear span of $\Psi$ for each $k$, then we say $K$ is the approximation of the Koopman operator ${\mathbb{U}}_{F}$ on the basis $\Psi$. When the basis functions are properly chosen, the error functions $r_{k}$ are usually small. Consequently, the matrix $\mathbf{K}$ is a relatively accurate representation of the Koopman operator and therefore the underlying nonlinear dynamics.

There are two sources of error in the approximation of the infinite dimensional linear operators. The first source of error is due to finite choice of the basis function used in the projection. Apart from the cardinality, choice of the basis function itself should to be rich enough to accurately capture the dynamics. In particular, the choice could be directed by the fact the unknown eigenfunctions of the operator lies in the span of the basis functions. The physics of the problem such as continuity property or the non-locality or locality of the phenomena to be captured can be used in determining the choice and number of basis function. The second source of error arise due to finite length of data used in the approximation of the operator. In this paper we are interested in characterizing the error due to the finite data length. Since our focus in the present paper is the estimation error induced by limited data points, we shall make the following assumption.

### Assumption 6

The action of the Koopman operator on the basis functions, $\Psi$, is closed, i.e., for some constant coefficients $\mathbf{K}_{jk}$.

Let $\varphi$ be any function in the span of $\Psi$, namely, for some vector $\alpha \in {\mathbb{R}}^{N}$. By definition, the function $\varphi$ will evolve under the action of Koopman operator as where $y = {F{(x,\xi)}}$. It follows that which says that the coordinate of ${\mathbb{U}}_{F}\varphi$ in the space spanned by $\Psi$ is $\mathbf{K}\alpha$. This implies that applying Koopman operator ${\mathbb{U}}_{F}$ on a function $\varphi$ is nothing but multiplying its coordinate $\alpha$ by $\mathbf{K}$ on the left.

To estimate the approximation $\mathbf{K}$, we multiply the equation by $\Psi{(x)}$ Since $x$ is fixed, this is same as Now taking expectation with respect to the initial condition $x$, we obtain then $\Sigma_{1} = {\Sigma_{0}\mathbf{K}}$ and consequently $\mathbf{K} = {\Sigma_{1}\Sigma_{0}^{- 1}}$.

When only generated data samples $X,Y$ are available, we have where $\delta_{t}:={{\Psi{(y_{t})}} - {{\mathbb{E}}{\{{\Psi{({F{(x_{t},\xi_{t})}})}}\}}}}$ satisfies We assume that ${{\mathbb{E}}{\{\delta_{t,j}^{2}\}}} \leq \Delta$. This is clearly true when the dynamics is of the form with $\xi$ having bounded variance.

Multiplying (the transpose of) all terms of with $\Psi{(x_{t})}$ on the left and sum up them over $t$ gives Clearly, ${\hat{\Sigma}}_{0}$ is an unbiased estimation of $\Sigma_{0}$ and ${\hat{\Sigma}}_{0}\rightarrow\Sigma_{0}$ when $T\rightarrow\infty$. The same argument holds for ${\hat{\Sigma}}_{1},\Sigma_{1}$. The error term $R$ has zero expectation, i.e., ${{\mathbb{E}}{\{ R\}}} = 0$. Hence, a least square estimator of $\mathbf{K}$ is given by This estimator is widely used in the Koopman operator literatures.

As $T\rightarrow\infty$, ${{\hat{\Sigma}}_{0}\rightarrow\Sigma_{0}},{{\hat{\Sigma}}_{1}\rightarrow\Sigma_{1}}$, and therefore $\hat{\mathbf{K}}\rightarrow\mathbf{K}$. In addition, there estimation error can be analyzed as follows. We first invoke Cauchy-Schwarz inequality, which gives In the above, $\parallel \cdot \parallel_{F}$ denotes Frobenius norm. To attain an upper bound on ${\mathbb{E}}{\{{\| R\|}_{F}^{2}\}}$, we observe that each element $R_{kj}$ of $R$ satisfies The second equality follows from the fact that $\delta_{t}$ is conditionally independent of $x_{s}$ for all $s \leq t$. The last inequality follows from the boundedness assumption ${{\mathbb{E}}{\{\delta_{t,j}^{2}\}}} \leq \Delta$. Summing up the above over all $k,j$ we obtain

### Theorem 7

Let $\epsilon > 0$ and $T > {{2N} + 2}$, then with probability at least $1 - \epsilon$, the least square estimator $\hat{\mathbf{K}}$ in reconstructs $\mathbf{K}$ within a Frobenius norm error bounded by

### Proof

The assumption $T > {{2N} + 2}$ guarantees that the least square estimator $\hat{\mathbf{K}}$ in is well defined. The rest follows by applying Markov's inequality to the nonnegative random variable ${\|{\hat{\mathbf{K}} - \mathbf{K}}\|}_{F}$. ∎ In, the duality between the P-F and Koopman operator is exploited to provide algorithm for the finite dimensional approximation of the P-F operator. Following and under the assumption that $g$ and $h$ lie in the span of $\Psi$ i.e., $g = {\Psi^{\top}a}$ and $h = {\Psi^{\top}b}$ for some constant vectors $a$ and $b$, we can write where ${\lbrack\Lambda\rbrack}_{ij} = \left\langle \psi_{i},\psi_{j} \right\rangle$ for $i = {2,\ldots,N}$ is a symmetric matrix. Using Assumption 6, we have Let $\mathbf{P}$ be the finite dimensional approximation of the P-F operator on the basis function, $\Psi$. Then using, we obtain Since the above is true for all $g$ and $h$ in the span of $\Psi$, we obtain following finite dimensional approximation of the P-F operator in terms of the Koopman operator

### Corollary 8

Let $\epsilon > 0$ and $T > {{2N} + 2}$, then with probability at least $1 - \epsilon$, the least square estimator $\hat{\mathbf{P}}$ in reconstructs $\mathbf{P}$ within a Frobenius norm error bounded by

### Proof

It follows directly from Theorem 7 and the definition of induced 2-norm $\parallel \cdot \parallel_{2}$. ∎

## Numerical Examples

We provide two examples to illustrate our results. In the first one, the Assumption 6 is valid. The second one is a standard Van der Pol oscillator which doesn't satisfy this assumption.

Example 1: Consider the following discrete time dynamical system where $\xi_{1},\xi_{2}$ are standard unit variance Gaussian noise, and ${\rho < 1},{{\mu < 1},{c > 0}}$ are parameters.

It is easy to see that the action of the Koopman operator is closed for the basis functions, Figure 1 and Fig. 2 showcase the estimation errors ${err} = \frac{{\|{\hat{\mathbf{K}} - \mathbf{K}}\|}_{F}}{{\|\mathbf{K}\|}_{F}}$ as a function of time step $T$, which match with our results pretty well. Note that we used a single trajectory to estimate $\mathbf{K}$ but the estimation errors are averaged over $50$ realizations.

Example 2: The second example that we consider is the discretized version of Van der Pol oscillator. The discretized equation for the Van der Pol oscillator is given by where $\Delta$ is the time step of discretization and is chosen to be equal to $\Delta = 0.0001$. Monomial with largest degree two is used as the choice of basis functions. Hence there are total of six functions in the basis. As can be seen from Fig. 3, even though the system is not closed with respect to Koopman operator, the convergent result matches the theory pretty well.

Figure 3: Example 2: Van der Pol Oscillator

## Conclusion

We derived sample complexity results for the identification of nonlinear dynamical systems. The results make use of linear operator theoretic framework involving Koopman operator which lifts nonlinear systems to infinite dimensional linear systems. The results are derived for discrete-time dynamical systems but can be extended to continuous-time setting.
