<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Convergence of Adam and Beyond

Topics include Convex optimization, Nonconvex optimization, Stochastic optimization, Optimization, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Several recently proposed stochastic optimization methods that have been successfully used in training deep networks such as RMSProp, Adam, Adadelta, Nadam are based on using gradient updates scaled by square roots of exponential moving averages of squared past gradients. In many applications, e.g. learning with large output spaces, it has been empirically observed that these algorithms fail to converge to an optimal solution (or a critical point in nonconvex settings). We show that one cause for such failures is the exponential moving average used in the algorithms. We provide an explicit example of a simple convex optimization setting where Adam does not converge to the optimal solution, and describe the precise problems with the previous analysis of Adam algorithm. Our analysis suggests that the convergence issues can be fixed by endowing such algorithms with `long-term memory' of past gradients, and propose new variants of the Adam algorithm which not only fix the convergence issues but often also lead to improved empirical performance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic gradient descent (Sgd) is the dominant method to train deep networks today. This method iteratively updates the parameters of a model by moving them in the direction of the negative gradient of the loss evaluated on a minibatch. In particular, variants of Sgd that scale coordinates of the gradient by square roots of some form of averaging of the squared coordinates in the past gradients have been particularly successful, because they automatically adjust the learning rate on a per-feature basis. The first popular algorithm in this line of research is Adagrad, which can achieve significantly better performance compared to vanilla Sgd when the gradients are sparse, or in general small.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although Adagrad works well for sparse settings, its performance has been observed to deteriorate in settings where the loss functions are nonconvex and gradients are dense due to rapid decay of the learning rate in these settings since it uses all the past gradients in the update. This problem is especially exacerbated in high dimensional problems arising in deep learning. To tackle this issue, several variants of Adagrad, such as RMSprop, Adam, Adadelta, Nadam, etc, have been proposed which mitigate the rapid decay of the learning rate using the exponential moving averages of squared past gradients, essentially limiting the reliance of the update to only the past few gradients. While these algorithms have been successfully employed in several practical applications, they have also been observed to not converge in some other settings. It has been typically observed that in these settings some minibatches provide large gradients but only quite rarely, and while these large gradients are quite informative, their influence dies out rather quickly due to the exponential averaging, thus leading to poor convergence.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we analyze this situation in detail. We rigorously prove that the intuition conveyed in the above paragraph is indeed correct; that limiting the reliance of the update on essentially only the past few gradients can indeed cause significant convergence issues.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We elucidate how the exponential moving average in the RMSprop and Adam algorithms can cause non-convergence by providing an example of simple convex optimization problem where RMSprop and Adam provably do not converge to an optimal solution. Our analysis easily extends to other algorithms using exponential moving averages such as Adadelta and Nadam as well, but we omit this for the sake of clarity. In fact, the analysis is flexible enough to extend to other algorithms that employ averaging squared gradients over essentially a fixed size window (for exponential moving averages, the influences of gradients beyond a fixed window size becomes negligibly small) in the immediate past. We omit the general analysis in this paper for the sake of clarity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above result indicates that in order to have guaranteed convergence the optimization algorithm must have "long-term memory" of past gradients. Specifically, we point out a problem with the proof of convergence of the Adam algorithm given by Kingma & Ba. To resolve this issue, we propose new variants of Adam which rely on long-term memory of past gradients, but can be implemented in the same time and space requirements as the original Adam algorithm. We provide a convergence analysis for the new variants in the convex setting, based on the analysis of Kingma & Ba, and show a data-dependent regret bound similar to the one in Adagrad.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a preliminary empirical study of one of the variants we proposed and show that it either performs similarly, or better, on some commonly used problems in machine learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Optimization setup", "weight": 1.0} -->

A flexible framework to analyze iterative optimization methods is the online optimization problem in the full information feedback setting. In this online setup, at each time step $t$, the optimization algorithm picks a point (i.e. the parameters of the model to be learned) $x_{t} \in \mathcal{F}$, where $\mathcal{F} \in {\mathbb{R}}^{d}$ is the feasible set of points. A loss function $f_{t}$ (to be interpreted as the loss of the model with the chosen parameters in the next minibatch) is then revealed, and the algorithm incurs loss $f_{t}{(x_{t})}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Optimization setup", "weight": 1.0} -->

Our aim to is to devise an algorithm that ensures $R_{T} = {o{(T)}}$, which implies that on average, the model's performance converges to the optimal one.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Optimization setup", "weight": 1.0} -->

$\alpha/\sqrt{t}$ for some constant $\alpha$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimization setup", "weight": 1.0} -->

The aforementioned online learning problem is closely related to the stochastic optimization problem: ${\min_{x \in \mathcal{F}}{\mathbb{E}}_{z}}{\lbrack{f{(x,z)}}\rbrack}$, popularly referred to as empirical risk minimization (ERM), where $z$ is a training example drawn training sample over which a model with parameters $x$ is to be learned, and $f{(x,z)}$ is the loss of the model with parameters $x$ on the sample $z$. In particular, an online optimization algorithm with vanishing average regret yields a stochastic optimization algorithm for the ERM problem. Thus, we use online gradient descent and stochastic gradient descent (Sgd) synonymously.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Generic adaptive methods setup", "weight": 1.0} -->

We now provide a framework of adaptive methods that gives us insights into the differences between different adaptive methods and is useful for understanding the flaws in a few popular adaptive methods. Algorithm 1 provides a generic adaptive framework that encapsulates many popular adaptive methods. Note the algorithm is still abstract because the "averaging" functions $\phi_{t}$ and $\psi_{t}$ have not been specified. Here $\phi_{t}:{\mathcal{F}^{t}\rightarrow{\mathbb{R}}^{d}}$ and $\psi_{t}:{\mathcal{F}^{t}\rightarrow\mathcal{S}_{+}^{d}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Generic adaptive methods setup", "weight": 1.0} -->

For ease of exposition, we refer to $\alpha_{t}$ as step size and $\alpha_{t}V_{t}^{- {1/2}}$ as learning rate of the algorithm and furthermore, restrict ourselves to diagonal variants of adaptive methods encapsulated by Algorithm 1 where $V_{t} = {\text{diag}{(v_{t})}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Generic adaptive methods setup", "weight": 1.0} -->

and $\alpha_{t} = {\alpha/\sqrt{t}}$ for all $t \in {\lbrack T\rbrack}$. While the decreasing step size is required for convergence, such an aggressive decay of learning rate typically translates into poor empirical performance. The key idea of adaptive methods is to choose averaging functions appropriately so as to entail good convergence.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Generic adaptive methods setup", "weight": 1.0} -->

and step size $\alpha_{t} = {\alpha/\sqrt{t}}$ for all $t \in {\lbrack T\rbrack}$. In contrast to a learning rate of $\alpha/\sqrt{t}$ in Sgd, such a setting effectively implies a modest learning rate decay of $\alpha/\sqrt{\sum_{i}g_{i,j}^{2}}$ for $j \in {\lbrack d\rbrack}$. When the gradients are sparse, this can potentially lead to huge gains in terms of convergence (see Duchi et al. ). These gains have also been observed in practice for even few non-sparse settings.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Adaptive methods based on Exponential Moving Averages", "weight": 1.0} -->

Exponential moving average variants of Adagrad are popular in the deep learning community. RMSprop, Adam, Nadam, and Adadelta are some prominent algorithms that fall in this category. The key difference is to use an exponential moving average as function $\psi_{t}$ instead of the simple average function used in Adagrad. Adam^11^1Here, for simplicity, we remove the debiasing step used in the version of Adam used in the original paper by Kingma & Ba. However, our arguments also apply to the debiased version as well.,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Adaptive methods based on Exponential Moving Averages", "weight": 1.0} -->

and $m_{0,i} = 0$ and $v_{0,i} = 0$ for all $i \in {\lbrack d\rbrack}$. and $t \in {\lbrack T\rbrack}$. A value of $\beta_{1} = 0.9$ and $\beta_{2} = 0.999$ is typically recommended in practice. We note the additional projection operation in Algorithm 1 in comparison to Adam. When $\mathcal{F} = {\mathbb{R}}^{d}$, the projection operation is an identity operation and this corresponds to the algorithm. For theoretical analysis, one requires $\alpha_{t} = {1/\sqrt{t}}$ for $t \in {\lbrack T\rbrack}$, although, a more aggressive choice of constant step size seems to work well in practice. RMSprop, which appeared in an earlier unpublished work is essentially a variant of Adam with $\beta_{1} = 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Adaptive methods based on Exponential Moving Averages", "weight": 1.0} -->

In practice, especially in deep learning applications, the momentum term arising due to non-zero $\beta_{1}$ appears to significantly boost the performance. We will mainly focus on Adam algorithm due to this generality but our arguments also apply to RMSprop and other algorithms such as Adadelta, Nadam.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Non-Convergence of Adam", "weight": 1.0} -->

With the problem setup in the previous section, we discuss fundamental flaw in the current exponential moving average methods like Adam. We show that Adam can fail to converge to an optimal solution even in simple one-dimensional convex settings.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Non-Convergence of Adam", "weight": 1.0} -->

This quantity essentially measures the change in the inverse of learning rate of the adaptive method with respect to time. One key observation is that for Sgd and Adagrad, $\Gamma_{t} \succeq 0$ for all $t \in {\lbrack T\rbrack}$. This simply follows from update rules of Sgd and Adagrad in the previous section. In particular, update rules for these algorithms lead to "non-increasing" learning rates. However, this is not necessarily the case for exponential moving average variants like Adam and RMSprop i.e., $\Gamma_{t}$ can potentially be indefinite for $t \in {\lbrack T\rbrack}$. We show that this violation of positive definiteness can lead to undesirable convergence behavior for Adam and RMSprop.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Non-Convergence of Adam", "weight": 1.0} -->

where $C > 2$. For this function sequence, it is easy to see that the point $x = {- 1}$ provides the minimum regret. Suppose $\beta_{1} = 0$ and $\beta_{2} = {1/{({1 + C^{2}})}}$. We show that Adam converges to a highly suboptimal solution of $x = {+ 1}$ for this setting. Intuitively, the reasoning is as follows. The algorithm obtains the large gradient $C$ once every 3 steps, and while the other 2 steps it observes the gradient $- 1$, which moves the algorithm in the wrong direction. The large gradient $C$ is unable to counteract this effect since it is scaled down by a factor of almost $C$ for the given value of $\beta_{2}$, and hence the algorithm converges to $1$ rather than $- 1$. We formalize this intuition in the result below.

<!-- chunk {"id": "body-0023", "role": "body", "section": "New Exponential Moving Average Variant: AMSGrad", "weight": 1.0} -->

In this section, we develop a new principled exponential moving average variant and provide its convergence analysis. Our aim is to devise a new strategy with guaranteed convergence while preserving the practical benefits of Adam and RMSprop. To understand the design of our algorithms, let us revisit the quantity $\Gamma_{t}$. For Adam and RMSprop, this quantity can potentially be negative. The proof in the original paper of Adam erroneously assumes that $\Gamma_{t}$ is positive semi-definite and is hence, incorrect (refer to Appendix D for more details). For the first part, we modify these algorithms to satisfy this additional constraint. Later, we also explore an alternative approach where $\Gamma_{t}$ can be made positive semi-definite by using values of $\beta_{1}$ and $\beta_{2}$ that change with $t$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "New Exponential Moving Average Variant: AMSGrad", "weight": 1.0} -->

AMSGrad uses a smaller learning rate in comparison to Adam and yet incorporates the intuition of slowly decaying the effect of past gradients on the learning rate as long as $\Gamma_{t}$ is positive semi-definite. Algorithm 2 presents the pseudocode for the algorithm. The key difference of AMSGrad with Adam is that it maintains the maximum of all $v_{t}$ until the present time step and uses this maximum value for normalizing the running average of the gradient instead of $v_{t}$ in Adam. By doing this, AMSGrad results in a non-increasing step size and avoids the pitfalls of Adam and RMSprop i.e., $\Gamma_{t} \succeq 0$ for all $t \in {\lbrack T\rbrack}$ even with constant $\beta_{2}$. Also, in Algorithm 2, one typically uses a constant $\beta_{1t}$ in practice (although, the proof requires a decreasing schedule for proving convergence of the algorithm).

<!-- chunk {"id": "body-0025", "role": "body", "section": "New Exponential Moving Average Variant: AMSGrad", "weight": 1.0} -->

To gain more intuition for the updates of AMSGrad, it is instructive to compare its update with Adam and Adagrad. Suppose at particular time step $t$ and coordinate $i \in {\lbrack d\rbrack}$, we have $v_{{t - 1},i} > g_{t,i}^{2} > 0$, then Adam aggressively increases the learning rate, however, as we have seen in the previous section, this can be detrimental to the overall performance of the algorithm. On the other hand, Adagrad slightly decreases the learning rate, which often leads to poor performance in practice since such an accumulation of gradients over a large time period can significantly decrease the learning rate. In contrast, AMSGrad neither increases nor decreases the learning rate and furthermore, decreases $v_{t}$ which can potentially lead to non-decreasing learning rate even if gradient is large in the future iterations.

<!-- chunk {"id": "body-0026", "role": "body", "section": "New Exponential Moving Average Variant: AMSGrad", "weight": 1.0} -->

For rest of the paper, we use $g_{1:t} = {\lbrack{g_{1}\ldotsg_{t}}\rbrack}$ to denote the matrix obtained by concatenating the gradient sequence. We prove the following key result for AMSGrad.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we present empirical results on both synthetic and real-world datasets. For our experiments, we study the problem of multiclass classification using logistic regression and neural networks, representing convex and nonconvex settings, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

with the constraint set $\mathcal{F} = {\lbrack{- 1},1\rbrack}$. We first observe that, similar to the examples of non-convergence we have considered, the optimal solution is $x = {- 1}$; thus, for convergence, we expect the algorithms to converge to $x = {- 1}$. For this sequence of functions, we investigate the regret and the value of the iterate $x_{t}$ for Adam and AMSGrad. To enable fair comparison, we set $\beta_{1} = 0.9$ and $\beta_{2} = 0.99$ for Adam and AMSGrad algorithm, which are typically the parameters settings used for Adam in practice. Figure 1 shows the average regret ($R_{t}/t$) and value of the iterate ($x_{t}$) for this problem. We first note that the average regret of Adam does not converge to $0$ with increasing $t$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

Furthermore, its iterates $x_{t}$ converge to $x = 1$, which unfortunately has the largest regret amongst all points in the domain. On the other hand, the average regret of AMSGrad converges to $0$ and its iterate converges to the optimal solution.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Similar to the aforementioned online setting, the optimal solution for this problem is $x = {- 1}$. Again, we see that the iterate $x_{t}$ of Adam converges to the highly suboptimal solution $x = 1$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Logistic Regression: To investigate the performance of the algorithm on convex problems, we compare AMSGrad with Adam on logistic regression problem. We use MNIST dataset for this experiment, the classification is based on 784 dimensional image vector to one of the 10 class labels. The step size parameter $\alpha_{t}$ is set to $\alpha/\sqrt{t}$ for both Adam and AMSGrad in for our experiments, consistent with the theory. We use a minibatch version of these algorithms with minibatch size set to $128$. We set $\beta_{1} = 0.9$ and $\beta_{2}$ is chosen from the set $\{ 0.99,0.999\}$, but they are fixed throughout the experiment. The parameters $\alpha$ and $\beta_{2}$ are chosen by grid search. We report the train and test loss with respect to iterations in Figure 2. We can see that AMSGrad performs better than Adam with respect to both train and test loss. We also observed that AMSGrad is relatively more robust to parameter changes in comparison to Adam.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Neural Networks: For our first experiment, we trained a simple 1-hidden fully connected layer neural network for the multiclass classification problem on MNIST. Similar to the previous experiment, we use $\beta_{1} = 0.9$ and $\beta_{2}$ is chosen from $\{ 0.99,0.999\}$. We use a fully connected 100 rectified linear units (ReLU) as the hidden layer for this experiment. Furthermore, we use constant $\alpha_{t} = \alpha$ throughout all our experiments on neural networks. Such a parameter setting choice of Adam is consistent with the ones typically used in the deep learning community for training neural networks. A grid search is used to determine parameters that provides the best performance for the algorithm.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Finally, we consider the multiclass classification problem on the standard CIFAR-10 dataset, which consists of 60,000 labeled examples of $32 \times 32$ images. We use Cifarnet, a convolutional neural network (CNN) with several layers of convolution, pooling and non-linear units, for training a multiclass classifer for this problem. In particular, this architecture has 2 convolutional layers with 64 channels and kernel size of $6 \times 6$ followed by 2 fully connected layers of size 384 and 192. The network uses $2 \times 2$ max pooling and layer response normalization between the convolutional layers. A dropout layer with keep probability of 0.5 is applied in between the fully connected layers. The minibatch size is also set to 128 similar to previous experiments. The results for this problem are reported in Figure 2. The parameters for Adam and AMSGrad are selected in a way similar to the previous experiments. We can see that AMSGrad performs considerably better than Adam on train loss and accuracy. Furthermore, this performance gain also translates into good performance on test loss.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Extension: AdamNc algorithm", "weight": 1.0} -->

An alternative approach is to use an increasing schedule of $\beta_{2}$ in Adam. This approach, unlike Algorithm 2 does not require changing the structure of Adam but rather uses a non-constant $\beta_{1}$ and $\beta_{2}$. The pseudocode for the algorithm, AdamNc, is provided in the appendix (Algorithm 3). We show that by appropriate selection of $\beta_{1t}$ and $\beta_{2t}$, we can achieve good convergence rates.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we study exponential moving variants of Adagrad and identify an important flaw in these algorithms which can lead to undesirable convergence behavior. We demonstrate these problems through carefully constructed examples where RMSprop and Adam converge to highly suboptimal solutions. In general, any algorithm that relies on an essentially fixed sized window of past gradients to scale the gradient updates will suffer from this problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

We proposed fixes to this problem by slightly modifying the algorithms, essentially endowing the algorithms with a long-term memory of past gradients. These fixes retain the good practical performance of the original algorithms, and in some cases actually show improvements.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

The primary goal of this paper is to highlight the problems with popular exponential moving average variants of Adagrad from a theoretical perspective. RMSprop and Adam have been immensely successful in development of several state-of-the-art solutions for a wide range of problems. Thus, it is important to understand their behavior in a rigorous manner and be aware of potential pitfalls while using them in practice. We believe this paper is a first step in this direction and suggests good design principles for faster and better stochastic optimization.
