<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AdaLoss: A Computationally-efficient and Provably Convergent Adaptive Gradient Method

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a computationally-friendly adaptive learning rate schedule, "AdaLoss", which directly uses the information of the loss function to adjust the stepsize in gradient descent methods. We prove that this schedule enjoys linear convergence in linear regression. Moreover, we provide a linear convergence guarantee over the non-convex regime, in the context of two-layer over-parameterized neural networks. If the width of the first-hidden layer in the two-layer networks is sufficiently large (polynomially), then AdaLoss converges robustly to the global minimum in polynomial time. We numerically verify the theoretical results and extend the scope of the numerical experiments by considering applications in LSTM models for text clarification and policy gradients for control problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient-based methods are widely used in optimizing neural networks. One crucial component in gradient methods is the learning rate (a.k.a. step size) hyper-parameter, which determines the convergence speed of the optimization procedure. An optimal learning rate can speed up the convergence but only up to a certain threshold value; once it exceeds this threshold value, the optimization algorithm may no longer converge. This is by now well-understood for convex problems; excellent works on this topic include Nesterov, Haykin et al., Bubeck et al., and the recent review for large-scale stochastic optimization to Bottou et al..

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While determining the optimal step size is theoretically important for identifying the optimal convergence rate, the optimal learning rate often depends on certain unknown parameters of the problem. For example, for a convex and $L$-smooth objective function, the optimal learning rate is $O{({1/L})}$ where $L$ is often unknown to practitioners. To solve this problem, adaptive methods Duchi et al.; McMahan and Streeter are proposed since they can change the learning rate on-the-fly according to gradient information received along the way. Though these methods often introduce additional hyper-parameters compared to gradient descent (GD) methods with well-tuned stepsizes, the adaptive methods are provably robust to their hyper-parameters in the sense that they still converge at suboptimal parameter specifications, but modulo (slightly) slower convergence rate Levy; Ward et al.. Hence, adaptive gradient methods are widely used by practitioners to save a large amount of human effort and computer power in manually tuning the hyper-parameters.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among many variants of adaptive gradient methods, one that requires a minimal amount of hyper-parameter tuning is *AdaGrad-Norm* Ward et al., which has the following update

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, computing the norm of the (sub)-gradient ${{\nabla f_{\xi}}{(\mathbf{w}_{j})}} \in {\mathbb{R}}^{d}$ in high dimensional space, particularly in settings which arise in training deep neural networks, is not at all practical.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\alpha > 0$ and $c$ are the tuning parameters. With this update, we theoretically show that AdaLoss converges with an upper bound that is tighter than AdaGrad-Norm under certain conditions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretical investigations into adaptive gradient methods for optimizing neural networks are scarce. Existing analyses only deal with general (non)-convex and smooth functions, and thus, only concern convergence to first-order stationary points Li and Orabona; Chen et al.. However, it is sensible to instead target global convergence guarantees for adaptive gradient methods in this setting in light of a series of recent breakthrough papers showing that (stochastic) GD can converge to the global minima of over-parameterized neural networks Du et al.; Li and Liang; Allen-Zhu et al.; Zou et al..

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*What is the iteration complexity of adaptive gradient methods in over-parameterized networks?*

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, we note that these papers require the step size to be sufficiently small to guarantee global convergence. In practice, these optimization algorithms can use a much larger learning rate while still converging to the global minimum. Thus, we make an effort to answer

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

*What is the optimal stepsize in optimizing neural networks?*

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

First, we study AdaGrad-Norm (Ward et al. ) in the linear regression setting and significantly improve the constants in the convergence bounds -- $\mathcal{O}\left( {L^{2}/\epsilon} \right)$ (Ward et al.,Xie et al. )^11^1The rate is for Case of Theorem 3 in Xie et al. and of Theorem 2.2 in Ward et al.. $L$ is ${\overline{\lambda}}_{1}$ in Theorem 3.1. in the deterministic gradient descent setting-- to a near-constant dependence $\mathcal{O}\left( {\log{({L/\epsilon})}} \right)$ (Theorem 3.1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

Second, we develop an adaptive gradient method called *AdaLoss* that can be viewed as a variant of the "norm\" version of AdaGrad but with better computational efficiency and easier implementation. We provide theoretical evidence that AdaLoss converges at the same rate as AdaGrad-Norm *but with a better convergence constant* in the setting of linear regression (Corollary 3.1).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

Third, for an overparameterized two-layer neural network, we show the learning rate of GD can be improved to the rate of $\mathcal{O}{({1/{\|\mathbf{H}^{\infty}\|}})}$ (Theorem 4.1) where $\mathbf{H}^{\infty}$ is a Gram matrix which only depends on the data.^22^2Note that this upper bound is independent of the number of parameters. As a result, using this stepsize, we show GD enjoys a faster convergence rate. This choice of stepsize directly leads to an improved convergence rate compared to Du et al.. We further prove AdaLoss converges to the global minimum in polynomial time and does so robustly, in the sense that *for any choice of hyper-parameters* used, our method is guaranteed to converge to the global minimum in polynomial time (Theorem 4.2). The choice of hyper-parameters only affects the rate but not the convergence.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

In particular, we provide explicit expressions for the polynomial dependencies in the parameters required to achieve global convergence.^33^3Note that this section has greatly subsumes Wu et al.. However, Theorem 4.2 is a much improved version compared to Theorem 4.1 in Wu et al.. This is due to our new inspiration from Theorem 3.1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

We numerically verify our theorems in both linear regression and a two-layer neural network (Figure 3, 3 and 3). To demonstrate the easy implementation and extension of our algorithm for practical purposes, we perform experiments in a text classification example using LSTM models, as well as for a control problem using policy gradient methods (Section 5).

<!-- chunk {"id": "body-0017", "role": "body", "section": "AdaLoss Stepsize", "weight": 1.0} -->

Let $\{ Z_{1},\ldots,Z_{n}\}$ be empirical samples drawn uniformly from an unknown underlying distribution $\mathcal{S}$. Define ${{f_{i}{(\mathbf{w})}} = {f{(\mathbf{w},Z_{i})}}}:{{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}},{i = {1,2,\ldots,n}}}$. Consider minimizing the empirical risk defined as finite sum of $f_{i}{(\mathbf{w})}$ over $i \in {\lbrack n\rbrack}$. The standard algorithm is stochastic gradient descent (SGD) with an appropriate step-size Bottou et al.. Stepsize tuning for optimization problems, including training neural networks, is generally challenging because the convergence of the algorithm is very sensitive to the stepsize: too small values of the stepsize mean slow progress while too large values lead to the divergence of the algorithm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "AdaLoss Stepsize", "weight": 1.0} -->

To find a suitable learning rate schedule, one could use the information on past and present gradient norms as described in equation, and the convergence rate for SGD is $\mathcal{O}\left( {1/\varepsilon^{2}} \right)$, the same order as for well-tuned stepsize Levy; Li and Orabona; Ward et al.. However, in high dimensional statistics, particularly in the widespread application of deep neural networks, computing the norm of the (sub)-gradient ${{\nabla f_{i}}{(\mathbf{w}_{j})}} \in {\mathbb{R}}^{d}$ for $i \in {\lbrack n\rbrack}$ at every iteration $j$ is impractical. To tackle the problem, we recall the popular setting of linear regression and two-layer network regression Du et al. where assuming at optimal ${\nabla f_{i}^{\ast}} = 0$,

<!-- chunk {"id": "body-0019", "role": "body", "section": "AdaLoss Stepsize", "weight": 1.0} -->

The norm of the gradient is bounded by the difference between $f_{i}{(\mathbf{w}_{j})}$ and $f_{i}^{\ast}$. The optimal value $f_{i}^{\ast}$ is a fixed number, which could possibly be known as prior or estimated under some conditions. For instance, for an over-determined linear regression problem or over-parameterized neural networks, we know that $f_{i}^{\ast} = 0$. For the sake of the generality of our proposed algorithm, we replace $f^{\ast}$ with a constant $c$. Based on the above observation, we propose the update in Algorithm 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "AdaLoss Stepsize", "weight": 1.0} -->

Our focus is $b_{k + 1}$, a parameter that is changing at every iteration according to the loss value of previous computational outputs. There are four positive hyper-parameters, $b_{0},\eta,\alpha,c$, in the algorithm. $\eta$ is for ensuring homogeneity and that the units match. $b_{0}$ is the initialization of a monotonically increasing sequence ${\{ b_{k}\}}_{k = 1}^{\infty}$. The parameter $\alpha$ is to control the rate of updating ${\{ b_{k}\}}_{k = 1}^{\infty}$ and the constant $c$ is a surrogate for the ground truth value $f^{\ast}$ ($c = 0$ if $f^{\ast} = 0$).

<!-- chunk {"id": "body-0021", "role": "body", "section": "AdaLoss Stepsize", "weight": 1.0} -->

1: Input: Initialize w0 ∈ ℝd, b0 &gt; 0, c &gt; 0, j ← 0, and the total iterations T.
3: Generate a random index ξj
5: $\mathbf{w}_{j + 1}\leftarrow{\mathbf{w}_{j} - {\frac{\eta}{b_{j + 1}}{\nabla f_{\xi_{j}}}{(\mathbf{w}_{j})}}}$
Algorithm 1 AdaLoss Algorithm

<!-- chunk {"id": "body-0022", "role": "body", "section": "AdaLoss Stepsize", "weight": 1.0} -->

The algorithm makes a significant improvement in *computational efficiency* by using the direct feedback of the (stochastic) loss. For the above algorithm, $\xi_{j} \sim {\text{Unif}{\{ 1,2,\ldots,n\}}}$ satisfies the conditional equality ${{\mathbb{E}}_{\xi_{j}}{\lbrack\left. {{\nabla f_{\xi_{j}}}{(\mathbf{w}_{j})}} \middle| \mathbf{w}_{j} \right.\rbrack}} = {{\nabla F}{(\mathbf{w}_{j})}}$. As a nod to the use of the information of the stochastic loss for the stepsize schedule, we call this method adaptive loss (AdaLoss). In the following sections, we present our analysis of this algorithm on linear regression and two-layer over-parameterized neural networks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "AdaLoss in Linear Regression", "weight": 1.0} -->

Suppose the data matrix $\mathbf{X}^{\top}\mathbf{X}$ a positive definite matrix with the smallest singular value ${\overline{\lambda}}_{0} > 0$ and the largest singular value ${\overline{\lambda}}_{1} > 0$. Denote $\mathbf{V}$ the unitary matrix from the singular value decomposition of ${\mathbf{X}^{\top}\mathbf{X}} = {\mathbf{V}\Sigma\mathbf{V}^{T}}$. Suppose we have the optimal solution ${\mathbf{X}\mathbf{w}}^{\ast} = \mathbf{y}$. The recent work of Xie et al. implies that the convergence rate using the adaptive stepsize update in enjoys linear convergence.

<!-- chunk {"id": "body-0024", "role": "body", "section": "AdaLoss in Linear Regression", "weight": 1.0} -->

However, the linear convergence is under the condition that the effective learning rate ${2\eta}/b_{0}$ is less than the critical threshold $1/{\overline{\lambda}}_{1}$ (i.e.,$b_{0} \geq {{\overline{\eta\lambda}}_{1}/2}$). If we initialize the effective learning rate larger than the threshold, the algorithm falls back to a sub-linear convergence rate with an order $\mathcal{O}\left( {{\overline{\lambda}}_{1}/\varepsilon} \right)$. Suspecting that this might be due to an artifact of the proof, we here tighten the bound that admits the linear convergence $\mathcal{O}\left( {\log\left( {1/\varepsilon} \right)} \right)$ for any $b_{0}$ (Theorem 3.1).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To verify the convergence results in linear regression, we compare four algorithms: (a) AdaLoss with $1/b_{t}$, (b) AdaGrad-Norm with $1/b_{t}$ (c) SGD-Constant with $1/b_{0}$, (d) SGD-DecaySqrt with $1/{({b_{0} + {c_{s}\sqrt{t}}})}$ ($c_{s}$ is a constant). See Appendix D for experimental details. Figure 3 implies that AdaGrad-Norm and AdaLoss behave similarly in the deterministic setting, while AdaLoss performs much better in the stochastic setting, particularly when $b_{0} \leq L =:\sup_{i} \parallel \mathbf{x}_{i} \parallel$. Figure 3 implies that stochastic AdaLoss and AdaGrad-Norm are robust to a wide range of initialization of $b_{0}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Comparing AdaLoss with AdaGrad-Norm, we find that when $b_{0} \leq 1$, AdaLoss is not better than AdaGrad-Norm at the beginning (at least before 1000 iterations, see the first two figures at the top row), albeit the effective learning rate is much larger than AdaGrad-Norm. However, after 5000 iterations (3rd figure, 1st row), AdaLoss outperforms AdaGrad-Norm in general.

<!-- chunk {"id": "body-0027", "role": "body", "section": "AdaLoss in Two-Layer Networks", "weight": 1.0} -->

We consider the same setup as in Du et al. where they assume that the data points, ${\{\mathbf{x}_{i},y_{i}\}}_{i = 1}^{n}$, satisfy

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The assumption on the input is only for the ease of presentation and analysis. The second assumption on labels is satisfied in most real-world datasets. We predict labels using a two-layer neural network

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

We use $k$ for indexing since $\mathbf{u}{(k)}$ is induced by $\mathbf{W}{(k)}$. According to, the matrix below determines the convergence rate of GD.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 4.2", "weight": 1.0} -->

We first consider GD with a constant learning rate ($\eta$) ${{\mathbf{W}{({k + 1})}} = {{\mathbf{W}{(k)}} - {\eta\frac{\partial{L{({\mathbf{W}{(k)}})}}}{\partial\mathbf{W}}}}}.$ showed gradient descent achieves zero training loss with learning rate $\eta = {O{({\lambda_{0}/n^{2}})}}$. Based on the approach of eigenvalue decomposition in Arora et al. (c.f. Lemma B.7), we show that the maximum allowable learning rate can be improved from $O{({\lambda_{0}/n^{2}})}$ to $O{({1/{\|\mathbf{H}^{\infty}\|}})}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Apply AdaLoss to Adam", "weight": 1.0} -->

In this section, we consider the application of AdaLoss in the practical domain. Adam Kingma and Ba has been successfully applied to many machine learning problems. However, it still requires fine-tuning the stepsize $\eta$ in Algorithm 2. Although the default value is $\eta = 0.001$, one might wonder if this is the optimal value. Therefore, we apply AdaLoss to make the value $\eta$ robust to any initialization (see the blue part in Algorithm 2) and name it AdamLoss. We take two tasks to test the robustness of AdamLoss and compare it with the default Adam as well as AdamSqrt, where we literally let $\eta = {1/\sqrt{b_{0} + t}}$. Note that for simplicity, we set $\alpha = 1$. More experiments are provided in the appendix for different $\alpha$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Apply AdaLoss to Adam", "weight": 1.0} -->

The first task is two-class (Fake/True News) text classification using one-layer LSTM (see Section D for details). The left plot in Figure 5 implies that the training loss is very robust to any initialization of the AdamLoss algorithm and subsequently achieves relatively better test accuracy. The right plot in Figure 5 captures the dynamics of $1/b_{t}$ for the first 200 iterations at the beginning of the training. We see that when $b_{0} = 0.1$ (red) or $b_{0} = 1$ (blue), the stochastic loss (bottom right) is very high such that after $25$ iterations, it reaches ${1/b_{t}} \approx 0.01$ and then stabilizes. When $b_{0} = 400$, the stochastic loss shows a decreasing trend at the beginning, which means it is around the critical threshold.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Apply AdaLoss to Adam", "weight": 1.0} -->

The second task is to solve the classical control problem: inverted pendulum swing-up. One popular algorithm is the actor-critic algorithm Konda and Tsitsiklis, where the actor algorithm is optimized by proximal policy gradient methods Zoph et al., and the critic algorithm is optimized by function approximation methods Fujimoto et al.. The actor-network and critic-network are fully connected layers with different depths. We use Adam and AdamLoss to optimize the actor-critic algorithm independently for four times and average the rewards. The code source is provided in the supplementary material. The left plot of Figure 5 implies that AdaLoss is very robust to different initialization, while the standard Adam is extremely sensitive to $\eta = \frac{1}{b_{0}}$. Interestingly, AdamLoss does better when starting with $\eta_{0} = \frac{1}{200}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Apply AdaLoss to Adam", "weight": 1.0} -->

We plot the corresponding $1/b_{t}$ on the right-hand side in Figure 5. We see that regardless of the initialization of $b_{0}$, the final value ${1/b_{t}} \approx 0.01$ reaches a value between $0.002$ and $0.001$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Apply AdaLoss to Adam", "weight": 1.0} -->

Overall, AdamLoss is shown numerically robust to any initialization $b_{0}$ for the two-class text classification and the inverted pendulum swing-up problems. See appendix for more experiments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Our theoretical results make a step forward in explaining the linear convergence rate and zero training error using adaptive gradient methods as observed in neural network training in practice. Our new technique for developing a linear convergence proof (Theorem 3.1 and Theorem 4.2) might be used to improve the recent sub-linear convergence results of Adam-type methods. Based on a theoretical understanding of the complexity bound of adaptive gradient methods and the relationship between loss and gradient, we proposed a provably convergent adaptive gradient method (Adaloss). It is computationally-efficient and could potentially be a useful optimization method for large-scale data training. In particular, it can be applied in natural language processing and reinforcement learning domains where tuning hyper-parameters is very expensive, and thus making a potentially positive impact on society.
