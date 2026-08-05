<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Complexity for Nonlinear Dynamics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the identification problems for nonlinear dynamical systems. An explicit sample complexity bound in terms of the number of data points required to recover the models accurately is derived. Our results extend recent sample complexity results for linear dynamics. Our approach for obtaining sample complexity bounds for nonlinear dynamics relies on a linear, albeit infinite dimensional, representation of nonlinear dynamics provided by Koopman and Perron-Frobenius operator. We exploit the linear property of these operators to derive the sample complexity bounds. Such complexity bounds will play a significant role in data-driven learning and control of nonlinear dynamics. Several numerical examples are provided to highlight our theory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonlinear dynamical models possess the capacity to represent a variety of real-world systems and have been employed in different areas such as automatic control, robotics, autonomy and so. A most common approach to obtaining a nonlinear model is via the first principle, which requires a good understanding of the underlying physics. In many cases, this requirement is however not realistic. Therefore, a data-driven approach using generated data samples to build a nonlinear model is becoming more and more critical. This is known as the system identification problem in control theory.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Compared to that of linear systems, the system identification problems for nonlinear dynamics are considerably more difficult. There have been many works on this topic, and many algorithms have been proposed. Most of these works focus on the asymptotical performance of the algorithms, which copes with the situation when the amount of data available goes to infinity. A critical question pertains to the data efficiency hasn't been adequately addressed yet. How many data points do we need to recover a dynamical model to a certain precision?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

It turns out that this question falls into the scope of sample complexity theory, which is a key mathematical tool in theoretical machine learning. This tool is used to analyze the performance guarantee of machine learning models. Many fundamental results have been established along this line in supervised learning. This attempt is not so successful in reinforcement learning, especially when the state space is continuous as in most control applications. Recently, as the first step in this direction, some sample complexity results for data-driven linear quadratic regulator problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The purpose of this work is to establish sample complexity results for nonlinear dynamics. To achieve this goal, we use a linear operator theoretic framework involving transfer Koopman and Perron-Frobenius (P-F) operators for linear representation and modeling of a nonlinear system. Linear operator theoretic framework has attracted lot of attention lately from the theoretical and applied dynamical system communities. One of the features that makes this approach attractive is its ability to approximate complicated and complex nonlinear dynamical system from time-series data. The basic idea behind the linear operator framework is to lift the nonlinear finite dimensional evolution of a dynamical system in the state space to linear albeit infinite dimensional evolution of functions in the functional space. Various algorithms are proposed for the finite dimensional approximation of these linear operators. However, to the best of authors knowledge, the problem of deriving sample complexity results for these operators has not been addressed yet. The linear nature of these operators allows us to carry out sample complexity analysis similar to the one developed for the case of a linear system but in the lifted functional space. We believe that sample complexity for a nonlinear system will play a fundamental role in our understanding of reinforcement learning algorithms, one of the fast-growing area of machine learning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. In Section II we introduce linear operator framework involving Koopman and P-F operators. The result on sample complexity is presented in Section III. We provide several examples in Section IV to illustrate our results. This follows by a short concluding remark in Section V.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The P-F operator can also be defined without the restrictive invertibility assumption on the mapping $T$ on the space of measures. For more details on this please refer to.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Sample Complexity of Koopman and Perron-Frobenius Operators", "weight": 1.0} -->

Linear operator theoretic framework involving P-F and Koopman operator provides a powerful tool for the representation, analysis, and design of nonlinear dynamical systems. Our objective in this section is to derive sample complexity results for the finite dimensional approximation of these linear operators. Although several algorithms are proposed for the finite dimensional approximation of the Koopman operators from time series data, the fundamental principle behind these different algorithms remains the same. Hence, the sample complexity results that we derive, using extended dynamic mode decomposition (EDMD) algorithm and its modification for the approximation of P-F operator, should apply to other algorithms as well.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sample Complexity of Koopman and Perron-Frobenius Operators", "weight": 1.0} -->

For the finite dimensional approximation, let be data points generated by random dynamical system through experiments or simulations. Note that here $y_{k} = {F{(x_{k},\xi_{k})}}$. These data samples could be from a single trajectory, in which case $y_{k} = x_{k + 1}$, or different trajectories.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sample Complexity of Koopman and Perron-Frobenius Operators", "weight": 1.0} -->

To establish a finite dimensional approximation of a Koopman operator we first choose a set of finite many basis functions A corresponding approximation of a Koopman operator is nothing but its projection on this basis. More specifically, if for some matrix $\mathbf{K}$ with $r_{k}{(\cdot)}$ being almost perpendicular to the linear span of $\Psi$ for each $k$, then we say $K$ is the approximation of the Koopman operator ${\mathbb{U}}_{F}$ on the basis $\Psi$. When the basis functions are properly chosen, the error functions $r_{k}$ are usually small. Consequently, the matrix $\mathbf{K}$ is a relatively accurate representation of the Koopman operator and therefore the underlying nonlinear dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sample Complexity of Koopman and Perron-Frobenius Operators", "weight": 1.0} -->

There are two sources of error in the approximation of the infinite dimensional linear operators. The first source of error is due to finite choice of the basis function used in the projection. Apart from the cardinality, choice of the basis function itself should to be rich enough to accurately capture the dynamics. In particular, the choice could be directed by the fact the unknown eigenfunctions of the operator lies in the span of the basis functions. The physics of the problem such as continuity property or the non-locality or locality of the phenomena to be captured can be used in determining the choice and number of basis function. The second source of error arise due to finite length of data used in the approximation of the operator. In this paper we are interested in characterizing the error due to the finite data length. Since our focus in the present paper is the estimation error induced by limited data points, we shall make the following assumption.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

The action of the Koopman operator on the basis functions, $\Psi$, is closed, i.e., for some constant coefficients $\mathbf{K}_{jk}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

Let $\varphi$ be any function in the span of $\Psi$, namely, for some vector $\alpha \in {\mathbb{R}}^{N}$. By definition, the function $\varphi$ will evolve under the action of Koopman operator as where $y = {F{(x,\xi)}}$. It follows that which says that the coordinate of ${\mathbb{U}}_{F}\varphi$ in the space spanned by $\Psi$ is $\mathbf{K}\alpha$. This implies that applying Koopman operator ${\mathbb{U}}_{F}$ on a function $\varphi$ is nothing but multiplying its coordinate $\alpha$ by $\mathbf{K}$ on the left.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

To estimate the approximation $\mathbf{K}$, we multiply the equation by $\Psi{(x)}$ Since $x$ is fixed, this is same as Now taking expectation with respect to the initial condition $x$, we obtain then $\Sigma_{1} = {\Sigma_{0}\mathbf{K}}$ and consequently $\mathbf{K} = {\Sigma_{1}\Sigma_{0}^{- 1}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

Multiplying (the transpose of) all terms of with $\Psi{(x_{t})}$ on the left and sum up them over $t$ gives Clearly, ${\hat{\Sigma}}_{0}$ is an unbiased estimation of $\Sigma_{0}$ and ${\hat{\Sigma}}_{0}\rightarrow\Sigma_{0}$ when $T\rightarrow\infty$. The same argument holds for ${\hat{\Sigma}}_{1},\Sigma_{1}$. The error term $R$ has zero expectation, i.e., ${{\mathbb{E}}{\{ R\}}} = 0$. Hence, a least square estimator of $\mathbf{K}$ is given by This estimator is widely used in the Koopman operator literatures.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

As $T\rightarrow\infty$, ${{\hat{\Sigma}}_{0}\rightarrow\Sigma_{0}},{{\hat{\Sigma}}_{1}\rightarrow\Sigma_{1}}$, and therefore $\hat{\mathbf{K}}\rightarrow\mathbf{K}$. In addition, there estimation error can be analyzed as follows. We first invoke Cauchy-Schwarz inequality, which gives In the above, $\parallel \cdot \parallel_{F}$ denotes Frobenius norm. To attain an upper bound on ${\mathbb{E}}{\{{\| R\|}_{F}^{2}\}}$, we observe that each element $R_{kj}$ of $R$ satisfies The second equality follows from the fact that $\delta_{t}$ is conditionally independent of $x_{s}$ for all $s \leq t$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

The last inequality follows from the boundedness assumption ${{\mathbb{E}}{\{\delta_{t,j}^{2}\}}} \leq \Delta$. Summing up the above over all $k,j$ we obtain

<!-- chunk {"id": "body-0019", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We provide two examples to illustrate our results. In the first one, the Assumption 6 is valid. The second one is a standard Van der Pol oscillator which doesn't satisfy this assumption.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Example 1: Consider the following discrete time dynamical system where $\xi_{1},\xi_{2}$ are standard unit variance Gaussian noise, and ${\rho < 1},{{\mu < 1},{c > 0}}$ are parameters.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

It is easy to see that the action of the Koopman operator is closed for the basis functions, Figure 1 and Fig. 2 showcase the estimation errors ${err} = \frac{{\|{\hat{\mathbf{K}} - \mathbf{K}}\|}_{F}}{{\|\mathbf{K}\|}_{F}}$ as a function of time step $T$, which match with our results pretty well. Note that we used a single trajectory to estimate $\mathbf{K}$ but the estimation errors are averaged over $50$ realizations.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Example 2: The second example that we consider is the discretized version of Van der Pol oscillator. The discretized equation for the Van der Pol oscillator is given by where $\Delta$ is the time step of discretization and is chosen to be equal to $\Delta = 0.0001$. Monomial with largest degree two is used as the choice of basis functions. Hence there are total of six functions in the basis. As can be seen from Fig. 3, even though the system is not closed with respect to Koopman operator, the convergent result matches the theory pretty well.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We derived sample complexity results for the identification of nonlinear dynamical systems. The results make use of linear operator theoretic framework involving Koopman operator which lifts nonlinear systems to infinite dimensional linear systems. The results are derived for discrete-time dynamical systems but can be extended to continuous-time setting.
