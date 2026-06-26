<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Convergence of Adaptive Gradient Methods for an Over-parameterized Neural Network

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Adaptive gradient methods like AdaGrad are widely used in optimizing neural networks. Yet, existing convergence guarantees for adaptive gradient methods require either convexity or smoothness, and, in the smooth setting, only guarantee convergence to a stationary point. We propose an adaptive gradient method and show that for two-layer over-parameterized neural networks - if the width is sufficiently large (polynomially) - then the proposed method converges to the global minimum in polynomial time, and convergence is robust, without the need to fine-tune hyper-parameters such as the step-size schedule and with the level of over-parametrization independent of the training error. Our analysis indicates in particular that over-parametrization is crucial for the harnessing the full potential of adaptive gradient methods in the setting of neural networks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient-based methods are widely used in optimizing neural networks. One crucial component in gradient methods is the learning rate (a.k.a. step size) hyper-parameter, which determines the convergence speed of the optimization procedure. A large learning rate can speed up the convergence but if it is larger than a threshold, the optimization algorithm cannot converge. This is by now well-understood for convex problems; excellent works on this topic include Nash and Nocedal, Bertsekas, Nesterov, Haykin et al., Bubeck et al., and the recent review for large-scale stochastic optimization to Bottou et al.. However, there is still limited work on the convergence analysis for nonsmooth and nonconvex problems, which includes over-parameterized neural networks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, a series of breakthrough papers showed that (stochastic) gradient descent can provably converge to the global minima for over-parameterized neural networks. However, these papers all require the step size to be sufficiently small to guarantee the global convergence. In practice, these optimization algorithms can use a much larger learning rate while still converging to the global minimum. This leads to the following question: *What is the optimal learning rate in optimizing neural networks?* While finding the optimal step size is important theoretically for identifying the optimal convergence rate, the optimal learning rate often depends on certain unknown parameters of the problem. For example, for a convex and $L$-smooth objective function, the optimal learning rate is $O{({1/L})}$ where $L$ is often unknown to practitioners. To solve this problem, adaptive methods are proposed so that they can change the learning rate on-the-fly according to gradient information received along the way. Though these methods often introduce additional hyper-parameters, compared to gradient descent methods with well-tuned stepsize, the adaptive methods are often robust to their hyper-parameters in the sense that these methods can still converge modulo (slightly) slower convergence rate.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For this reason, adaptive gradient methods are widely used by practitioners in neural network optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, the theoretical investigation in adaptive methods in optimizing neural networks is limited. Existing analyses only deal with general (non)-convex and smooth functions, and thus, only concern convergence to first-order stationary points. However, a neural network is *neither smooth nor convex*. And yet, adaptive gradient methods are widely used in this setting as they converge without requiring a fine-tuned learning rate schedule. This leads to the following question: *What is the convergence rate of adaptive gradient methods in over-parameterized networks?* In this paper, we make progress on these two problems for the two-layer over-parameterized ReLU-activated neural networks setting.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our Results", "weight": 1.0} -->

First, we show the learning rate of gradient descent can be improved to $O{({1/{\|\mathbf{H}^{\infty}\|}})}$ where $\mathbf{H}^{\infty}$ is a Gram matrix that only depends on the data. Note that this upper bound is independent of the number of parameters. As a result, using this stepsize, we show gradient descent enjoys a faster convergence rate. This choice of stepsize directly leads to an improved convergence rate compared to Du et al..

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Results", "weight": 1.0} -->

We develop an adaptive gradient method, which can be viewed as a variant of the "norm" version of AdaGrad. We prove this adaptive gradient method converges to the global minimum in polynomial time and does so robustly, in the sense that for any choice of hyper-parameters used in this method, our method is guaranteed to converge to the global minimum in polynomial time. The choice of hyper-parameters only affect the rate but not the convergence. To our knowledge, this is the first polynomial time global convergence result for an adaptive gradient method in the non-convex setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Challenges and Our Techniques", "weight": 1.0} -->

To verify the improved learning rate of gradient descent, we use a more subtle analysis of the dynamics of predictions considered in Du et al.. Our analysis shows that the dynamics are close to a linear one. This observation allows us to choose the improved learning rate.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Challenges and Our Techniques", "weight": 1.0} -->

For the adaptive method, there are two big challenges. First, because the learning rate (induced by the hyper-parameters and the dynamics) is changing at every iteration, we need to lower and upper bound the learning rate. The lower bound is required to guarantee the algorithm will converge in polynomial time and the upper bound is required to guarantee the algorithm will not diverge. The second challenge is that if at the beginning the learning rate is too large, the loss may increase at the beginning. The proof of Du et al. for gradient descent with well-tuned stepsize highly depends on the fact that the loss is decreasing geometrically at each iteration, so that proof cannot be adapted to our setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Challenges and Our Techniques", "weight": 1.0} -->

In this paper, we use induction with a carefully constructed hypothesis which implies both the upper and the lower bounds of the learning rate. Furthermore, utilizing the particular property induced by our proposed adaptive algorithm, the learning rate learns from feedback from previous iterations and thus perseveres the distance of the updated weight matrix and its initialization (Lemma 4.2) while does not vanishes to zero (Lemma 4.1). This property, together with the effect of over-parameterization, we show that the loss may only increase by a bounded amount and then decreases to zero eventually. Resolving these issues, we are able to prove the first global convergence result for an adaptive gradient method in optimizing neural networks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Global Convergence of Neural Networks", "weight": 1.0} -->

Recently, a series of papers showed that gradient based methods can provably reduce the training error to $0$ for over-parameterized neural networks. In this paper we study the same setting considered in Du et al. which showed that for learning rate $\eta = {O{({{\lambda_{\min}{(\mathbf{H}^{\infty})}}/n^{2}})}}$, gradient descent finds an $\varepsilon$-suboptimal global minimum in $O\left( {\frac{1}{\eta\lambda_{\min}{(\mathbf{H}^{\infty})}}{\log{(\frac{1}{\epsilon})}}} \right)$ iterations for the two-layer over-parameterized ReLU-activated neural network.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Global Convergence of Neural Networks", "weight": 1.0} -->

As a by-product of the analysis in this paper, we show that the learning rate can be improved to $\eta = {O{({1/{\|\mathbf{H}^{\infty}\|}})}}$ which results in faster convergence. We believe that the proof techniques developed in this paper can be extended to deep neural networks, following the recent works.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Adaptive Gradient Methods", "weight": 1.0} -->

Adaptive Gradient (AdaGrad) Methods, first introduced independently by Duchi et al. and McMahan and Streeter, are now widely used in practice for online learning due in part to their robustness to the choice of stepsize. The first convergence guarantees, proved in Duchi et al., were for the setting of online convex optimization where the loss function may change from iteration to iteration. Later convergence results for the variants of AdaGrad were proved in Levy and Mukkamala and Hein for offline convex and strongly convex settings. In the general non-convex and smooth setting, Ward et al. and Li and Orabona prove that the same "norm" version of AdaGrad converges to a stationary point at rate $O\left( {1/\varepsilon^{2}} \right)$ for stochastic gradient descent and at rate $O\left( {1/\varepsilon} \right)$ for batch gradient descent.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Adaptive Gradient Methods", "weight": 1.0} -->

Many modifications to AdaGrad have been proposed, namely, RMSprop, AdaDelta, Adam, AdaFTRL, SGD-BB, AdaBatch, signSGD, SC-Adagrad, WNGrad, AcceleGrad, Yogi, Padam, to name a few. More recently, acccelerated adaptive gradient methods have also been proved to converge to stationary points.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Adaptive Gradient Methods", "weight": 1.0} -->

Our work is inspired by the analysis of Ward et al. and Wu et al. which quantifies the auto-tuning property in the learning rate in AdaGrad. We propose a new adaptive algorithm for the stepsize in the setting of over-parameterized neural networks and show global polynomial convergence guarantee.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations", "weight": 1.0} -->

Throughout, $\parallel \cdot \parallel$ denotes the Euclidean norm if it applies to a vector and the maximum eigenvalue if it applies to a matrix. We use $N{(\mathbf{0},\mathbf{I})}$ to denote a standard Gaussian distribution where $\mathbf{I}$ denotes the identity matrix and $U{(S)}$ to denote the uniform distribution over a set $S$. We use the notation ${\lbrack n\rbrack}:={\{ 0,1,2,\ldots,n\}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

In this paper we consider the same setup as Du et al.. We are given $n$ data points, ${\{\mathbf{x}_{i},y_{i}\}}_{i = 1}^{n}$. Following Du et al., to simplify the analysis, we make the following assumption on the training data.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The assumption on the input is only for the ease of presentation and analysis. See discussions in Du et al.. The second assumption on labels is satisfied in most real world datasets.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

We predict labels using a two-layer neural network of the following form where $\mathbf{x} \in {\mathbb{R}}^{d}$ is the input, for $r \in {\lbrack m\rbrack}$, $\mathbf{w}_{r} \in {\mathbb{R}}^{d}$ the weight vector of the first layer and $a_{r} \in {\mathbb{R}}$ is the output weight and $\sigma{(\cdot)}$ is ReLU activation function. For $r \in {\lbrack m\rbrack}$, we initialize the first layer vector ${\mathbf{w}_{r}{}} \sim {N{(\mathbf{0},\mathbf{I})}}$ and output weight $a_{r} \sim {U{(\left\{ {- 1},{+ 1} \right\})}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

We fix the second layer and train the first layer with the quadratic loss We will use iterative gradient-based algorithms to train $\mathbf{W}$. The gradient of each weight vector has the following form: We use $\mathbf{W}{(k)}$ to denote the parameters at the $k$-th iteration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The training algorithm will be specified in Section 3 and 4. Define $u_{i} = {f{(\mathbf{W},\mathbf{a},\mathbf{x}_{i})}}$, the prediction of the $i$-th example and $\mathbf{u} = \left(u_{1},\ldots,u_{n} \right)^{\top} \in {\mathbb{R}}^{n}$. We also let $\mathbf{y} = \left(y_{1},\ldots,y_{n} \right)^{\top} \in {\mathbb{R}}^{n}$. Then we can write the loss function as In this paper, we will study the dynamics of $\mathbf{u}{(k)}$. Here we use $k$ for indexing because $\mathbf{u}{(k)}$ is induced by $\mathbf{W}{(k)}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

According to Du et al., the matrix below determines the convergence rate of the randomly initialized gradient descent.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

Du et al. showed that this condition holds as long as the training data is not degenerate. We also define the following empirical version of this Gram matrix, which will be used in our analysis.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Warm up: Improved Learning Rate for Gradient Descent", "weight": 1.0} -->

Before presenting our adaptive method, we first revisit the gradient descent algorithm. At each iteration $k = {0,1,\ldots}$, we update the weight matrix according to where $\eta > 0$ is the learning rate. Du et al. showed if $\eta = {O{({\lambda_{0}/n^{2}})}}$, then gradient descent achieves $0$ training loss at a linear rate. We improve the upper bound of learning rate used in Du et al.. This improved analysis also gives tighter bound for the adaptive method we will discuss in the next section. Our main result for gradient descent is the following theorem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "An Adaptive Method for Over-parameterized Neural Networks", "weight": 1.0} -->

In this section we present our new adaptive gradient algorithm for optimizing over-parameterized neural networks. At the high level, we use the same paradigm as existing adaptive methods. There are three positive hyper-parameters, $b_{0},\eta,\alpha$ in the algorithm. $\eta$ is to ensure the homogeneity and that the units match. $b_{0}$ is the initialization of a monotonically increasing sequence ${\{ b_{k}\}}_{k = 1}^{\infty}$ such that $b_{k}$ is updated at $k$-th iteration. To control the rate of this update, we use the parameter $\alpha$. Note $\alpha$ is not the learning rate to update the parameter $\mathbf{W}$. At $k$-th iteration, we first use $\alpha$ and the information received to obtain $b_{k + 1}$, then use $\eta/b_{k + 1}$ to update the parameters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "An Adaptive Method for Over-parameterized Neural Networks", "weight": 1.0} -->

Here $\eta/b_{k + 1}$ is the effective learning rate at the $k$-th iteration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An Adaptive Method for Over-parameterized Neural Networks", "weight": 1.0} -->

In practice, we would like an adaptive method that is robust to the choices of hyper-parameters. That is, we want this method guaranteed to converge in polynomial time for any choice of hyper-parameters.^22^2 The convergence rate will, of course, depend on the choices of the hyper-parameters. The convergence of the ideal adaptive algorithm only depends polynomially on the these hyper-parameters. The key challenge for the adaptive method is how to design an appropriate update rule for $\{ b_{k}\}$ to achieve the goal. Our algorithm uses the following update rule: Here one can just view $\alpha$ and $n$ together as one constant. Using $\alpha^{2}$ is for matching the scale of $\eta$ and using $\sqrt{n}$ is for the ease of comparison with other adaptive gradient methods that we further discuss in Section 5. The key for this update is $\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|$ instead of its square.

<!-- chunk {"id": "body-0029", "role": "body", "section": "An Adaptive Method for Over-parameterized Neural Networks", "weight": 1.0} -->

Note this is sharp contrast to Duchi et al. where the scheme to update the effective learning rate can be equivalently written as ${\|{\mathbf{y} - {\mathbf{u}{(k)}}}\|}^{2}$. The main reason is that our convergence analysis requires analyzing both over-parameterization and the dynamics of the adaptive stepsize at the same time. See Section 5 for more discussions. We list pseudo codes in Algorithm 1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

It is difficult to set the parameters with optimal values due to the fact that the maximum and minimum eigenvalues of the matrix $\mathbf{H}^{\infty}$ are computational costly and so generally unknown. According to Theorem 3.1. ‣ 3 Warm up: Improved Learning Rate for Gradient Descent ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network"), since $n$ is an upper bound of $\|\mathbf{H}^{\infty}\|$, one may use gradient descent by setting $\eta = {\Theta\left( \frac{1}{n} \right)}$ and have the convergence rate of $T_{1} = {\overset{\sim}{O}\left( {\left( \frac{n}{\lambda_{0}} \right){\log\left( \frac{1}{\varepsilon} \right)}} \right)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

However, this choice of step size is not optimal when $\|\mathbf{H}^{\infty}\|$ is much smaller than $n$. Using adaptive gradient algorithm with the small initialization on the effective learning rate would results in better complexity. Indeed, for instance, let the target training error be $\varepsilon = \frac{1}{\sqrt{n}}$, the typical statistical target error and set $b_{0} = \eta$, $\alpha = \frac{1}{\sqrt{n}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Case: ${b_{0}/\\eta} \\leq {C{\\|\\mathbf{H}^{\\infty}\\|}}$", "weight": 1.0} -->

‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network").

<!-- chunk {"id": "body-0033", "role": "body", "section": "Case: ${b_{0}/\\eta} \\leq {C{\\|\\mathbf{H}^{\\infty}\\|}}$", "weight": 1.0} -->

Similar to Case, we use induction for the proof. Again the base case $k' = 0$ holds by the definition. Now suppose for $k' = {0,\ldots,k}$, Condition 4.1 holds and we will show it also holds for $k' = {k + 1}$. There are two scenarios.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Case: ${b_{0}/\\eta} \\leq {C{\\|\\mathbf{H}^{\\infty}\\|}}$", "weight": 1.0} -->

Now we have proved the induction. The last step is to use Condition 4.1 to prove the convergence rate. Observe that for any $T \geq T_{0}$, we have where we have used Lemma 4.1 and Lemma C.1 to derive With some algebra, one can show this bound corresponds to the second and the third term of iteration complexity of the Case in Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network").

<!-- chunk {"id": "body-0035", "role": "body", "section": "Ingredients of Proof", "weight": 1.0} -->

As we have seen in the proof sketch. Lemma 4.1 and Lemma 4.2 are most important lemmas in the proof of Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network"). Here we state and prove these two lemmas.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion on Variants of AdaGrad", "weight": 1.5} -->

In this section we compare our proposed algorithm AdaLoss with existing adaptive methods. Algorithm 1 can be viewed as a variant of the standard AdaGrad algorithm proposed by Duchi et al., where the norm version of the update is Our algorithm AdaLoss is similar to AdaGrad, but is distinctly different from AdaGrad: we update $b_{k + 1}^{2}$ using the *norm* of the *loss* instead of the *squared norm* of the *gradient*. We considered the AdaLoss update instead of AdaGrad because, in the setting considered here, the modifications allowed for dramatically better theoretical convergence rate.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Why the Loss instead of the Gradient?", "weight": 1.0} -->

Indeed, our update of $b_{k + 1}^{2}$ is not too different from the following update rule using the gradient The AdaLoss update can be upper and lower bounded by $b_{k}^{2}$ and the norm of the gradient, i.e., where the first and second inequalities are respectively due to Proposition E.1 and Proposition 5.1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Why the norm and not the squared-norm?", "weight": 1.0} -->

For ease of comparison with Algorithm 1, we switch from gradient information to loss and compare with two close variants: Equation using the "square" rule update is the standarad AdaGrad proposed by Duchi et al. and has been widely recognized as important optimizer in deep learning -- especially for training sparse datasets. For our over-parameterized models, this update rule does give a better convergence result in Case 1 when ${b_{0}/\eta} \geq {C{\|\mathbf{H}^{\infty}\|}}$ ^77^7The convergence proof is straightforward and similar to the first case in Theorem 4.1. ‣ 4 An Adaptive Method for Over-parameterized Neural Networks ‣ Global Convergence of Adaptive Gradient Methods for An Over-parameterized Neural Network").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Why the norm and not the squared-norm?", "weight": 1.0} -->

However, when the initialization ${b_{0}/\eta} \leq {C{\|\mathbf{H}^{\infty}\|}}$, we were only able to prove convergence in case the level of over-parameterization (i.e., $m$) depends on the training error $1/\varepsilon$, the bottleneck resulting from the attempting to prove the analog of Lemma 4.2 (see Proposition 5.2 below).
