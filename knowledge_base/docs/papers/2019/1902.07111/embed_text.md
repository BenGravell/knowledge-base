<!-- arxiv-full-text:v1 {"arxiv_id": "1902.07111", "source": "ar5iv"} -->

## Introduction

Gradient-based methods are widely used in optimizing neural networks. One crucial component in gradient methods is the learning rate (a.k.a. step size) hyper-parameter, which determines the convergence speed of the optimization procedure. A large learning rate can speed up the convergence but if it is larger than a threshold, the optimization algorithm cannot converge. This is by now well-understood for convex problems; excellent works on this topic include Nash and Nocedal, Bertsekas, Nesterov, Haykin et al., Bubeck et al., and the recent review for large-scale stochastic optimization to Bottou et al.. However, there is still limited work on the convergence analysis for nonsmooth and nonconvex problems, which includes over-parameterized neural networks.

Recently, a series of breakthrough papers showed that (stochastic) gradient descent can provably converge to the global minima for over-parameterized neural networks. However, these papers all require the step size to be sufficiently small to guarantee the global convergence. In practice, these optimization algorithms can use a much larger learning rate while still converging to the global minimum. This leads to the following question: *What is the optimal learning rate in optimizing neural networks?* While finding the optimal step size is important theoretically for identifying the optimal convergence rate, the optimal learning rate often depends on certain unknown parameters of the problem. For example, for a convex and $L$-smooth objective function, the optimal learning rate is $O{({1/L})}$ where $L$ is often unknown to practitioners. To solve this problem, adaptive methods are proposed so that they can change the learning rate on-the-fly according to gradient information received along the way. Though these methods often introduce additional hyper-parameters, compared to gradient descent methods with well-tuned stepsize, the adaptive methods are often robust to their hyper-parameters in the sense that these methods can still converge modulo (slightly) slower convergence rate. For this reason, adaptive gradient methods are widely used by practitioners in neural network optimization.

On the other hand, the theoretical investigation in adaptive methods in optimizing neural networks is limited. Existing analyses only deal with general (non)-convex and smooth functions, and thus, only concern convergence to first-order stationary points. However, a neural network is *neither smooth nor convex*. And yet, adaptive gradient methods are widely used in this setting as they converge without requiring a fine-tuned learning rate schedule. This leads to the following question: *What is the convergence rate of adaptive gradient methods in over-parameterized networks?* In this paper, we make progress on these two problems for the two-layer over-parameterized ReLU-activated neural networks setting.

### Our Results

First, we show the learning rate of gradient descent can be improved to $O{({1/{\|\mathbf{H}^{\infty}\|}})}$ where $\mathbf{H}^{\infty}$ is a Gram matrix that only depends on the data. Note that this upper bound is independent of the number of parameters. As a result, using this stepsize, we show gradient descent enjoys a faster convergence rate. This choice of stepsize directly leads to an improved convergence rate compared to Du et al..

We develop an adaptive gradient method, which can be viewed as a variant of the "norm" version of AdaGrad. We prove this adaptive gradient method converges to the global minimum in polynomial time and does so robustly, in the sense that for any choice of hyper-parameters used in this method, our method is guaranteed to converge to the global minimum in polynomial time. The choice of hyper-parameters only affect the rate but not the convergence. To our knowledge, this is the first polynomial time global convergence result for an adaptive gradient method in the non-convex setting.

### Challenges and Our Techniques

To verify the improved learning rate of gradient descent, we use a more subtle analysis of the dynamics of predictions considered in Du et al.. Our analysis shows that the dynamics are close to a linear one. This observation allows us to choose the improved learning rate.

For the adaptive method, there are two big challenges. First, because the learning rate (induced by the hyper-parameters and the dynamics) is changing at every iteration, we need to lower and upper bound the learning rate. The lower bound is required to guarantee the algorithm will converge in polynomial time and the upper bound is required to guarantee the algorithm will not diverge. The second challenge is that if at the beginning the learning rate is too large, the loss may increase at the beginning. The proof of Du et al. for gradient descent with well-tuned stepsize highly depends on the fact that the loss is decreasing geometrically at each iteration, so that proof cannot be adapted to our setting.

In this paper, we use induction with a carefully constructed hypothesis which implies both the upper and the lower bounds of the learning rate. Furthermore, utilizing the particular property induced by our proposed adaptive algorithm, the learning rate learns from feedback from previous iterations and thus perseveres the distance of the updated weight matrix and its initialization (Lemma 4.2) while does not vanishes to zero (Lemma 4.1). This property, together with the effect of over-parameterization, we show that the loss may only increase by a bounded amount and then decreases to zero eventually. Resolving these issues, we are able to prove the first global convergence result for an adaptive gradient method in optimizing neural networks.

### Related Work

### Global Convergence of Neural Networks

Recently, a series of papers showed that gradient based methods can provably reduce the training error to $0$ for over-parameterized neural networks. In this paper we study the same setting considered in Du et al. which showed that for learning rate $\eta = {O{({{\lambda_{\min}{(\mathbf{H}^{\infty})}}/n^{2}})}}$, gradient descent finds an $\varepsilon$-suboptimal global minimum in $O\left( {\frac{1}{\eta\lambda_{\min}{(\mathbf{H}^{\infty})}}{\log{(\frac{1}{\epsilon})}}} \right)$ iterations for the two-layer over-parameterized ReLU-activated neural network. As a by-product of the analysis in this paper, we show that the learning rate can be improved to $\eta = {O{({1/{\|\mathbf{H}^{\infty}\|}})}}$ which results in faster convergence. We believe that the proof techniques developed in this paper can be extended to deep neural networks, following the recent works.

### Adaptive Gradient Methods

Adaptive Gradient (AdaGrad) Methods, first introduced independently by Duchi et al. and McMahan and Streeter, are now widely used in practice for online learning due in part to their robustness to the choice of stepsize. The first convergence guarantees, proved in Duchi et al., were for the setting of online convex optimization where the loss function may change from iteration to iteration. Later convergence results for the variants of AdaGrad were proved in Levy and Mukkamala and Hein for offline convex and strongly convex settings. In the general non-convex and smooth setting, Ward et al. and Li and Orabona prove that the same "norm" version of AdaGrad converges to a stationary point at rate $O\left( {1/\varepsilon^{2}} \right)$ for stochastic gradient descent and at rate $O\left( {1/\varepsilon} \right)$ for batch gradient descent.

Many modifications to AdaGrad have been proposed, namely, RMSprop, AdaDelta, Adam, AdaFTRL, SGD-BB, AdaBatch, signSGD, SC-Adagrad, WNGrad, AcceleGrad, Yogi, Padam, to name a few. More recently, acccelerated adaptive gradient methods have also been proved to converge to stationary points.

Our work is inspired by the analysis of Ward et al. and Wu et al. which quantifies the auto-tuning property in the learning rate in AdaGrad. We propose a new adaptive algorithm for the stepsize in the setting of over-parameterized neural networks and show global polynomial convergence guarantee.

## Problem Setup

### Notations

Throughout, $\parallel \cdot \parallel$ denotes the Euclidean norm if it applies to a vector and the maximum eigenvalue if it applies to a matrix. We use $N{(\mathbf{0},\mathbf{I})}$ to denote a standard Gaussian distribution where $\mathbf{I}$ denotes the identity matrix and $U{(S)}$ to denote the uniform distribution over a set $S$. We use the notation ${\lbrack n\rbrack}:={\{ 0,1,2,\ldots,n\}}$.

### Problem Setup

In this paper we consider the same setup as Du et al.. We are given $n$ data points, ${\{\mathbf{x}_{i},y_{i}\}}_{i = 1}^{n}$. Following Du et al., to simplify the analysis, we make the following assumption on the training data.

### Assumption 2.1

For $i \in {\lbrack n\rbrack}$, ${\|\mathbf{x}_{i}\|} = 1$ and $\left| y_{i} \right| = {O{}}$.

The assumption on the input is only for the ease of presentation and analysis. See discussions in Du et al.. The second assumption on labels is satisfied in most real world datasets.

We predict labels using a two-layer neural network of the following form where $\mathbf{x} \in {\mathbb{R}}^{d}$ is the input, for $r \in {\lbrack m\rbrack}$, $\mathbf{w}_{r} \in {\mathbb{R}}^{d}$ the weight vector of the first layer and $a_{r} \in {\mathbb{R}}$ is the output weight and $\sigma{(\cdot)}$ is ReLU activation function. For $r \in {\lbrack m\rbrack}$, we initialize the first layer vector ${\mathbf{w}_{r}{}} \sim {N{(\mathbf{0},\mathbf{I})}}$ and output weight $a_{r} \sim {U{(\left\{ {- 1},{+ 1} \right\})}}$. We fix the second layer and train the first layer with the quadratic loss We will use iterative gradient-based algorithms to train $\mathbf{W}$. The gradient of each weight vector has the following form: We use $\mathbf{W}{(k)}$ to denote the parameters at the $k$-th iteration.

The training algorithm will be specified in Section 3 and 4. Define $u_{i} = {f{(\mathbf{W},\mathbf{a},\mathbf{x}_{i})}}$, the prediction of the $i$-th example and $\mathbf{u} = \left(u_{1},\ldots,u_{n} \right)^{\top} \in {\mathbb{R}}^{n}$. We also let $\mathbf{y} = \left(y_{1},\ldots,y_{n} \right)^{\top} \in {\mathbb{R}}^{n}$. Then we can write the loss function as In this paper, we will study the dynamics of $\mathbf{u}{(k)}$. Here we use $k$ for indexing because $\mathbf{u}{(k)}$ is induced by $\mathbf{W}{(k)}$. According to Du et al., the matrix below determines the convergence rate of the randomly initialized gradient descent.

### Definition 2.1

The matrix $\mathbf{H}^{\infty} \in {\mathbb{R}}^{n \times n}$ is defined as follows. For ${(i,j)} \in {{\lbrack n\rbrack} \times {\lbrack n\rbrack}}$.

This matrix represents the kernel matrix induced by Gaussian initialization and ReLU activation function. We make the following assumption on $\mathbf{H}^{\infty}$.

### Assumption 2.2

The matrix $\mathbf{H}^{\infty} \in {\mathbb{R}}^{n \times n}$ in Definition 2.1 satisfies ${\lambda_{\min}{(\mathbf{H}^{\infty})}} \triangleq \lambda_{0} > 0$.

Du et al. showed that this condition holds as long as the training data is not degenerate. We also define the following empirical version of this Gram matrix, which will be used in our analysis. For ${(i,j)} \in {{\lbrack n\rbrack} \times {\lbrack n\rbrack}}$:

## Warm up: Improved Learning Rate for Gradient Descent

Before presenting our adaptive method, we first revisit the gradient descent algorithm. At each iteration $k = {0,1,\ldots}$, we update the weight matrix according to where $\eta > 0$ is the learning rate. Du et al. showed if $\eta = {O{({\lambda_{0}/n^{2}})}}$, then gradient descent achieves $0$ training loss at a linear rate. We improve the upper bound of learning rate used in Du et al.. This improved analysis also gives tighter bound for the adaptive method we will discuss in the next section. Our main result for gradient descent is the following theorem.

### Theorem 3.1 (Convergence Rate of Gradient Descent with Improved Learning Rate)

Under Assumption 2.1 and 2.2, if the number of hidden nodes $m = {\Omega\left(\frac{n^{6}}{\lambda_{0}^{4}\delta^{3}} \right)}$ and we set the stepsize to be then with probability at least $1 - \delta$ over the random initialization, after^11^1 $\overset{\sim}{O}$ and $\overset{\sim}{\Omega}$ hide ${\log{(n)}},{\log{({1/\lambda_{0}})}},{\log{({1/\delta})}}$ terms. iterations, we have ${L{({\mathbf{W}{(T)}})}} \leq \varepsilon$.

Comparing with Du et al., we improve the maximum allowable learning rate from $O{({\lambda_{0}/n^{2}})}$ to $O{({1/{\|\mathbf{H}^{\infty}\|}})}$. Note since ${\|\mathbf{H}^{\infty}\|} \leq n$, Theorem 3.1. ‣ 3 Warm up: Improved Learning Rate for Gradient Descent ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network") gives an $O{({\lambda_{0}/n})}$ improvement. The improved learning also gives a tighter iteration complexity bound $O\left( {\frac{\|\mathbf{H}^{\infty}\|}{\lambda_{0}}{\log\left( \frac{n}{\varepsilon\delta} \right)}} \right)$ comparing to the $O\left( {\frac{n^{2}}{\lambda_{0}^{2}}{\log\left( \frac{n}{\varepsilon\delta} \right)}} \right)$ bound in Du et al.. Empirically, we found that if the data matrix is approximately orthogonal, then ${\|\mathbf{H}^{\infty}\|} = {O}$ (see Figure 1 in Appendix E). Therefore, in certain scenarios, the iteration complexity of gradient descent is independent of $n$.

Note even though gradient descent gives fast convergence, one needs to set the learning rate $\eta$ appropriately to achieve the fast convergence rate. In practice, $\|\mathbf{H}^{\infty}\|$ is unknown to users so it would be better if the learning rate can be automatically adjusted. We address this problem in the next section.

### Proof Sketch of Theorem 3.1. ‣ 3 Warm up: Improved Learning Rate for Gradient Descent ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network")

Our main observation is the following recursion formula.

The first approximation we used over-parameterization ($m$ is large enough) for which the width $m$ becomes larger the approximation becomes more accurate. In Section B, we will give precise perturbation analysis. The first inequality we used the fact that $\eta = {O\left( {1/{\|\mathbf{H}^{\infty}\|}} \right)}$ and the two symmetric matrices $\left( {\mathbf{I} - {\eta\mathbf{H}^{\infty}}} \right)$ and $\mathbf{H}^{\infty}$ share same eigenvectors. The second inequality we used $\eta = {O\left( {1/{\|\mathbf{H}^{\infty}\|}} \right)}$ again. Note this recursion formula shows the loss converges to $0$ at a linear rate and if we plug in $\eta = {\Theta\left( {1/{\|\mathbf{H}^{\infty}\|}} \right)}$ we prove theorem. The details are in Section B.

## An Adaptive Method for Over-parameterized Neural Networks

In this section we present our new adaptive gradient algorithm for optimizing over-parameterized neural networks. At the high level, we use the same paradigm as existing adaptive methods. There are three positive hyper-parameters, $b_{0},\eta,\alpha$ in the algorithm. $\eta$ is to ensure the homogeneity and that the units match. $b_{0}$ is the initialization of a monotonically increasing sequence ${\{ b_{k}\}}_{k = 1}^{\infty}$ such that $b_{k}$ is updated at $k$-th iteration. To control the rate of this update, we use the parameter $\alpha$. Note $\alpha$ is not the learning rate to update the parameter $\mathbf{W}$. At $k$-th iteration, we first use $\alpha$ and the information received to obtain $b_{k + 1}$, then use $\eta/b_{k + 1}$ to update the parameters. Here $\eta/b_{k + 1}$ is the effective learning rate at the $k$-th iteration.

In practice, we would like an adaptive method that is robust to the choices of hyper-parameters. That is, we want this method guaranteed to converge in polynomial time for any choice of hyper-parameters.^22^2 The convergence rate will, of course, depend on the choices of the hyper-parameters. The convergence of the ideal adaptive algorithm only depends polynomially on the these hyper-parameters. The key challenge for the adaptive method is how to design an appropriate update rule for $\{ b_{k}\}$ to achieve the goal. Our algorithm uses the following update rule: Here one can just view $\alpha$ and $n$ together as one constant. Using $\alpha^{2}$ is for matching the scale of $\eta$ and using $\sqrt{n}$ is for the ease of comparison with other adaptive gradient methods that we further discuss in Section 5. The key for this update is $\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|$ instead of its square. Note this is sharp contrast to Duchi et al. where the scheme to update the effective learning rate can be equivalently written as ${\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|}^{2}$. The main reason is that our convergence analysis requires analyzing both over-parameterization and the dynamics of the adaptive stepsize at the same time. See Section 5 for more discussions. We list pseudo codes in Algorithm 1.

Input: Tolerance ε > 0, initialization W, a, positive constants b0, η and α > 0. $b_{k + 1}^{2}\leftarrow{b_{k}^{2} + {\alpha^{2}\sqrt{n}{\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|}}}$ ${\mathbf{W}{({k + 1})}} = {{\mathbf{W}{(k)}} - {\frac{\eta}{b_{k + 1}}\frac{\partial{L{({\mathbf{W}{(k)}})}}}{\partial\mathbf{W}}}}$ Algorithm 1 Adaptive Loss (AdaLoss) The following theorem characterizes the convergence rate of our proposed algorithm.

### Theorem 4.1 (Convergence Rate of AdaLoss)

Under Assumption 2.1 and 2.2, if the width satisfies Then Algorithm 1 admits the following convergence results.

If the hyper-parameter satisfies $\frac{b_{0}}{\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$, ^33^3The notation $C$ is well-defined, please check Table 1 in Appendix E then with probability $1 - \delta$ over the random initialization ${\min_{t \in {\lbrack T\rbrack}}{\|{\mathbf{y} - {\mathbf{u}{(t)}}}\|}^{2}} \leq \varepsilon$ after If the hyper-parameter satisfies $0 < \frac{b_{0}}{\eta} \leq {C{\|\mathbf{H}^{\infty}\|}}$, then with probability $1 - \delta$ over the random initialization ${\min_{t \in {\lbrack T\rbrack}}{\|{\mathbf{y} - {\mathbf{u}{(t)}}}\|}^{2}} \leq \varepsilon$ after To our knowledge, this is first global convergence guarantee for the adaptive gradient method. Now we unpack the statements of Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network"). Our theorem applies to two cases. In the first case, the effective learning rate at the beginning $\eta/b_{0}$ is smaller than the threshold $1/{({C{\|\mathbf{H}^{\infty}\|}})}$ that guarantees the global convergence of gradient descent (c.f. Theorem 3.1. ‣ 3 Warm up: Improved Learning Rate for Gradient Descent ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network")). In this case, the convergence has two terms, the first term $\frac{b_{0}}{\eta\lambda_{0}}{\log\left(\frac{1}{\epsilon} \right)}$ is standard gradient descent rate if we use $\eta/b_{0}$ as the learning rate. Note this term is the same as Theorem 3.1. ‣ 3 Warm up: Improved Learning Rate for Gradient Descent ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network") if ${\eta/b_{0}} = {\Theta{({1/{\|\mathbf{H}^{\infty}\|}})}}$. The second term comes from the upper bound of $b_{T}$ in the effective learning rate $\eta/b_{T}$ (c.f. Lemma 4.1). This case shows that if $\alpha$ is relatively small that the second term is smaller than the first term, then we have the same rate as gradient descent. See Remark 4.1 for more discussion.

In the second case, the initial effective learning $\eta/b_{0}$ is greater than the threshold that guarantees the convergence of gradient descent. Our algorithm will guarantee either of the followings happens after $T$ iterations. The loss is already small, so we can stop training. This corresponds the first term $\frac{\left( {\eta{\|\mathbf{H}^{\infty}\|}} \right)^{2} - b_{0}^{2}}{\alpha^{2}\sqrt{n\varepsilon}}$. The loss is still large, which will make the effective stepsize $\eta/b_{k}$ decrease with a good rate. That is, if keeps happening, the stepsize will decrease till ${\eta/b_{k}} \leq {1/{({C{\|\mathbf{H}^{\infty}\|}})}}$ and we are in the first case. Note the first term is the same as the second term of the first case. The third term $\left( \frac{\|\mathbf{H}^{\infty}\|}{\lambda_{0}} \right)^{2}{\log\left( \frac{1}{\epsilon} \right)}$ is slightly worse than the rate in the gradient descent. The reason is the loss may increase due to the large learning rate at the beginning. (c.f. Lemma C.1).

To summarize, these two cases together show that our algorithm is robust to hyper-parameter choices. The bad choices of hyper-parameters will only hurt the constant in the convergence rate but the global polynomial time convergence is still guaranteed.

### Remark 4.1

It is difficult to set the parameters with optimal values due to the fact that the maximum and minimum eigenvalues of the matrix $\mathbf{H}^{\infty}$ are computational costly and so generally unknown. According to Theorem 3.1. ‣ 3 Warm up: Improved Learning Rate for Gradient Descent ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network"), since $n$ is an upper bound of $\|\mathbf{H}^{\infty}\|$, one may use gradient descent by setting $\eta = {\Theta\left( \frac{1}{n} \right)}$ and have the convergence rate of $T_{1} = {\overset{\sim}{O}\left( {\left( \frac{n}{\lambda_{0}} \right){\log\left( \frac{1}{\varepsilon} \right)}} \right)}$.

However, this choice of step size is not optimal when $\|\mathbf{H}^{\infty}\|$ is much smaller than $n$. Using adaptive gradient algorithm with the small initialization on the effective learning rate would results in better complexity. Indeed, for instance, let the target training error be $\varepsilon = \frac{1}{\sqrt{n}}$, the typical statistical target error and set $b_{0} = \eta$, $\alpha = \frac{1}{\sqrt{n}}$. Now in the scenario that ${\|\mathbf{H}^{\infty}\|} = {\Theta{}}$ and $\frac{1}{\lambda_{0}} = {\Theta\left( n^{9/8} \right)}$, the convergence rate of our adaptive method is $T_{2} = {\overset{\sim}{O}{(n^{9/4})}}$ comparing to the convergence rate of gradient descent which is $T_{1} = {\overset{\sim}{O}{(n^{5/2})}}$.

### Proof Sketch of Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network")

We prove by induction. Our induction hypothesis is the following.

### Condition 4.1

At the $k'$-th iteration,^44^4 For the convenience of induction proof, we define ${{\|{\mathbf{y} - {\mathbf{u}{({- 1})}}}\|}^{2} = {{\|{\mathbf{y} - {\mathbf{u}{}}}\|}^{2}/\left({1 - {\frac{\eta\lambda_{0}C_{1}}{b_{0}}\left({1 - \frac{\etaC{\|{\mathbf{H}{}}\|}}{b_{0}}} \right)}} \right)}}.$ there exists a constant $C_{1}$ such that ^55^5See Table 1 in Appendeix E for the expressions Recall the key Gram matrix $\mathbf{H}{(k')}$ at $k'$-th iteration We prove two cases ${b_{0}/\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$ and ${b_{0}/\eta} \leq {C{\|\mathbf{H}^{\infty}\|}}$ separately.

### Case: ${b_{0}/\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$

The base case $k' = 0$ holds by the definition. Now suppose for $k' = {0,\ldots,k}$, Condition 4.1 holds and we want to show Condition 4.1 holds for $k' = {k + 1}$. Because ${b_{0}/\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$, by Lemma 4.1 we have Next, plugging in $m = {\Omega\left(\frac{n^{6}}{\lambda_{0}^{4}\delta^{3}} \right)}$, we have ${\|{{\mathbf{w}_{r}{(k)}} - {\mathbf{w}_{r}{}}}\|} \leq \frac{c\lambda_{0}\delta}{n^{2}}$. Then by Lemma B.1 andB.3, the matrix $\mathbf{H}{(k)}$ is positive such that the smallest eigenvalue of $\mathbf{H}{(k)}$ is greater than $\frac{\lambda_{0}}{2}$. Consequently, we have Condition 4.1 holds for $k' = {k + 1}$.

Now we have proved the induction part. Using Condition 4.1, for any $T \in {\mathbb{Z}}^{+}$, we have where $b_{\infty} = {b_{0} + {\frac{4\alpha^{2}\sqrt{n}}{\eta\lambda_{0}C_{1}}{\|{\mathbf{y} - {\mathbf{u}{}}}\|}}} = {O{({b_{0} + \frac{\alpha^{2}n}{\eta^{2}\lambda_{0}\sqrt{\delta}}})}}$ (c.f. Lemma 4.1). This implies the convergence rate of Case.

### Case: ${b_{0}/\eta} \leq {C{\|\mathbf{H}^{\infty}\|}}$

Note this represents the number of iterations to make Case reduce to Case. We first give an upper bound $T_{0}$ of $\hat{T}$. If applying Lemma E.1 with parameters $\gamma = {\alpha^{2}\sqrt{n}}$, $a_{j} = {\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|}$ and $L = \left({\etaC{\|\mathbf{H}^{\infty}\|}} \right)^{2}$ we have after $T_{0}$ step, If ${\min_{k \in {\lbrack T_{0}\rbrack}}{\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|}^{2}} \leq \varepsilon$, we are done. Note this bound $T_{0}$ incurs the first term of iteration complexity of the Case in Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network").

Similar to Case, we use induction for the proof. Again the base case $k' = 0$ holds by the definition. Now suppose for $k' = {0,\ldots,k}$, Condition 4.1 holds and we will show it also holds for $k' = {k + 1}$. There are two scenarios.

For $k \leq {T_{0} - 1}$, Lemma 4.2 implies that $\|{{\mathbf{w}_{r}{(k)}} - {\mathbf{w}_{r}{}}}\|$ is upper bounded. Now plugging in our choice on $m$ and using Lemma B.1 and B.3, we know ${\lambda_{\min}\left( {\mathbf{H}{(k)}} \right)} \geq {\lambda_{0}/2}$ and ${\|{\mathbf{H}{(k)}}\|} \leq {C{\|\mathbf{H}^{\infty}\|}}$. These two bounds on $\mathbf{H}{(k)}$ imply Condition 4.1.

When $k \geq T_{0}$, we have contraction bound as in Case and then same argument follows but with the different initial values $\mathbf{W}{({T_{0} - 1})}$ and $\|{\mathbf{y} - {\mathbf{u}{({T_{0} - 1})}}}\|$. We first analyze $\mathbf{W}{({T_{0} - 1})}$ and $\|{\mathbf{y} - {\mathbf{u}{({T_{0} - 1})}}}\|$. By Lemma C.1, we know $\|{\mathbf{y} - {\mathbf{u}{({T_{0} - 1})}}}\|$ only increases an additive $O\left(\left({\etaC{\|\mathbf{H}^{\infty}\|}} \right)^{3/2} \right)$ factor from $\|{\mathbf{y} - {\mathbf{u}{}}}\|$. Furthermore, by Lemma 4.2, we know for $r \in {\lbrack m\rbrack}$ Now we consider $k$-th iteration. Applying Lemma 4.1, we have where the last inequality we have used our choice of $m$. Using Lemma B.1 and B.3 again, we can show ${\lambda_{\min}\left({\mathbf{H}{(k)}} \right)} \geq {\lambda_{0}/2}$ and ${\|{\mathbf{H}{(k)}}\|} \leq {C{\|\mathbf{H}^{\infty}\|}}$. These two bounds on $\mathbf{H}{(k)}$ imply Condition 4.1.

Now we have proved the induction. The last step is to use Condition 4.1 to prove the convergence rate. Observe that for any $T \geq T_{0}$, we have where we have used Lemma 4.1 and Lemma C.1 to derive With some algebra, one can show this bound corresponds to the second and the third term of iteration complexity of the Case in Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network").

### Ingredients of Proof

As we have seen in the proof sketch. Lemma 4.1 and Lemma 4.2 are most important lemmas in the proof of Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network"). Here we state and prove these two lemmas.

### Lemma 4.1

Suppose Condition 4.1 holds for $k' = {0,\ldots,k}$ and $b_{k}$ is updated by Algorithm 1. Let $T_{0} \geq 1$ be the first index such that $b_{T_{0}} \geq {\etaC{\|\mathbf{H}^{\infty}\|}}$. Then for every $r \in {\lbrack m\rbrack}$ and $k = {0,1,\cdots}$, Proof of Lemma 4.1 When ${b_{T_{0}}/\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$ at some $T_{0} \geq 1$, thanks to the key fact that Condition 4.1 holds $k' = {0,\ldots,k}$, we have Thus, the upper bound for $b_{k}$, As for the upper bound of ${\|{{\mathbf{w}_{r}{({k + T_{0}})}} - {\mathbf{w}_{r}{({T_{0} - 1})}}}\|},$

### Lemma 4.2

Let $T_{0} \geq 1$ be the first index such that $b_{T_{0}} \geq {\etaC{\|\mathbf{H}^{\infty}\|}}$. Then for every $r \in {\lbrack m\rbrack}$, we have for $k = {0,1,\ldots,{T_{0} - 1}}$, Proof of Lemma 4.2 For the upper bound of $\|{{\mathbf{w}_{r}{({k + 1})}} - {\mathbf{w}_{r}{}}}\|$ when ${b_{t}/\eta} < {C{\|\mathbf{H}^{\infty}\|}}$, $t = {0,1,\cdots,k}$ and $k \leq {T_{0} - 2}$, we first observe that where the second inequality use Lemma E.2 and the third inequality is due to the fact that $b_{k} \leq b_{T_{0} - 1} \leq {\etaC{\|\mathbf{H}^{\infty}\|}}$ for all $k \leq {T_{0} - 2}$. Thus,

## Discussion on Variants of AdaGrad

In this section we compare our proposed algorithm AdaLoss with existing adaptive methods. Algorithm 1 can be viewed as a variant of the standard AdaGrad algorithm proposed by Duchi et al., where the norm version of the update is Our algorithm AdaLoss is similar to AdaGrad, but is distinctly different from AdaGrad: we update $b_{k + 1}^{2}$ using the *norm* of the *loss* instead of the *squared norm* of the *gradient*. We considered the AdaLoss update instead of AdaGrad because, in the setting considered here, the modifications allowed for dramatically better theoretical convergence rate.

### Why the Loss instead of the Gradient?

Indeed, our update of $b_{k + 1}^{2}$ is not too different from the following update rule using the gradient The AdaLoss update can be upper and lower bounded by $b_{k}^{2}$ and the norm of the gradient, i.e., where the first and second inequalities are respectively due to Proposition E.1 and Proposition 5.1.

### Proposition 5.1

If ${\lambda_{min}{(\mathbf{H})}} \geq \frac{\lambda_{0}}{2}$, then ${{\|{\mathbf{y} - \mathbf{u}}\|} \leq {\frac{\sqrt{2m}}{\sqrt{\lambda_{0}}}{\max_{r \in {\lbrack m\rbrack}}{\|\frac{\partial{L{(\mathbf{W})}}}{\partial\mathbf{w}_{r}}\|}}}}.$ ^66^6Proof is given in Appendix D However, we use $\sqrt{n}{\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|}$ instead of using the gradient to update $b_{k}$ because our convergence analysis requires lower and upper bounding the dynamics $b_{1},\ldots,b_{k}$, in terms of $\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|$. If $b_{k}$ were instead updated using, then The above lower bound of $b_{k}$ results in a larger $T$ in Case by a factor of $\sqrt{n/\lambda_{0}}$. Using the loss instead of the gradient to update $b_{k}$ is independently useful as reusing the already computed loss information for each iteration can save some computation cost and thus make the update more efficient.

### Why the norm and not the squared-norm?

For ease of comparison with Algorithm 1, we switch from gradient information to loss and compare with two close variants: Equation using the "square" rule update is the standarad AdaGrad proposed by Duchi et al. and has been widely recognized as important optimizer in deep learning -- especially for training sparse datasets. For our over-parameterized models, this update rule does give a better convergence result in Case 1 when ${b_{0}/\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$ ^77^7The convergence proof is straightforward and similar to the first case in Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network"). However, when the initialization ${b_{0}/\eta} \leq {C{\|\mathbf{H}^{\infty}\|}}$, we were only able to prove convergence in case the level of over-parameterization (i.e., $m$) depends on the training error $1/\varepsilon$, the bottleneck resulting from the attempting to prove the analog of Lemma 4.2 (see Proposition 5.2 below).

### Proposition 5.2

Let $T_{0} \geq 1$ be the first index such that $b_{T_{0}} \geq {\etaC{\|\mathbf{H}^{\infty}\|}}$. Consider the update of $b_{k}$. Then for every $r \in {\lbrack m\rbrack}$, we have for $k = {0,1,\ldots,{T_{0} - 1}}$, On the other hand, the update rule in can resolve the problem because the growth of $b_{k}$ is larger than such that the upper bound of ${\|{{\mathbf{w}_{r}{(k)}} - {\mathbf{w}_{r}{}}}\|}_{2}$ $k = {0,{1\ldots},{T_{0} - 1}}$, is better than that in Proposition 5.2 and even Lemma 4.2 if $c{<{b_{0}{<{\etaC}\parallel}\mathbf{H}^{\infty}}\parallel}$ for some small $c$. However, the growth of $b_{k}$ remains too fast once the critical value of $\etaC{\|\mathbf{H}^{\infty}\|}$ has been reached -- the upper bound $b_{\infty}$ we were able to show is exponential in $1/\lambda_{0}$ and also in the hyper-parameters $b_{0}$,$\eta$, $\alpha$ and $n$, resulting in an extremely large $T$ compared to Case in Thoeorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network").
