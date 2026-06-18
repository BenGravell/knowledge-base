<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization

Topics include Convex optimization, Nonconvex optimization, Stochastic gradients, Deep learning, Probabilistic models, Datasets, Accuracy, Online algorithms, Optimization, Learning, PAGE, PL.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a novel stochastic gradient estimator - ProbAbilistic Gradient Estimator (PAGE) - for nonconvex optimization. PAGE is easy to implement as it is designed via a small adjustment to vanilla SGD: in each iteration, PAGE uses the vanilla minibatch SGD update with probability p_t or reuses the previous gradient with a small adjustment, at a much lower computational cost, with probability 1-p_t. We give a simple formula for the optimal choice of p_t. Moreover, we prove the first tight lower bound Omega(n+sqrt(n)/epsilon^) for nonconvex finite-sum problems, which also leads to a tight lower bound Omega(b+sqrt(b)/epsilon^) for nonconvex online problems, where b: = minsigma^/epsilon^, n. Then, we show that PAGE obtains the optimal convergence results O(n+sqrt(n)/epsilon^) (finite-sum) and O(b+sqrt(b)/epsilon^) (online) matching our lower bounds for both nonconvex finite-sum and online problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Besides, we also show that for nonconvex functions satisfying the Polyak-Łojasiewicz (PL) condition, PAGE can automatically switch to a faster linear convergence rate O(*log frac1epsilon). Finally, we conduct several deep learning experiments (e.g., LeNet, VGG, ResNet) on real datasets in PyTorch showing that PAGE not only converges much faster than SGD in training but also achieves the higher test accuracy, validating the optimal theoretical results and confirming the practical superiority of PAGE.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonconvex optimization is ubiquitous across many domains of machine learning, including robust regression, low rank matrix recovery, sparse recovery and supervised learning. Driven by the applied success of deep neural networks, and the critical place nonconvex optimization plays in training them, research in nonconvex optimization has been undergoing a renaissance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "The problem", "weight": 1.0} -->

Motivated by this development, we consider the general optimization problem

<!-- chunk {"id": "body-0006", "role": "body", "section": "The problem", "weight": 1.0} -->

where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is a differentiable and possibly nonconvex function. We are interested in functions having the *finite-sum* form

<!-- chunk {"id": "body-0007", "role": "body", "section": "The problem", "weight": 1.0} -->

where the functions $f_{i}$ are also differentiable and possibly nonconvex. Form captures the standard empirical risk minimization problems in machine learning. Moreover, if the number of data samples $n$ is very large or even infinite, e.g., in the online/streaming case, then $f{(x)}$ usually is modeled via the *online* form

<!-- chunk {"id": "body-0008", "role": "body", "section": "The problem", "weight": 1.0} -->

which we also consider in this work. For notational convenience, we adopt the notation of the finite-sum form in the descriptions and algorithms in the rest of this paper. However, our results apply to the online form as well by letting ${f_{i}{(x)}}:={F{(x,\zeta_{i})}}$ and treating $n$ as a very large value or even infinite.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Gradient complexity", "weight": 1.0} -->

To measure the efficiency of algorithms for solving the nonconvex optimization problem, it is standard to bound the number of stochastic gradient computations needed to find a solution of suitable characteristics. In this paper we use the standard term *gradient complexity* to describe such bounds. In particular, our goal will be to find a (possibly random) point $\hat{x} \in {\mathbb{R}}^{d}$ such that ${{\mathbb{E}}{\lbrack{\|{{\nabla f}{(\hat{x})}}\|}\rbrack}} \leq \epsilon$, where the expectation is with respect to the randomness inherent in the algorithm. We use the term $\epsilon$-approximate solution to refer to such a point $\hat{x}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Gradient complexity", "weight": 1.0} -->

Two of the most classical gradient complexity results for solving problem are those for gradient descent (GD) and stochastic gradient descent (SGD). In particular, the gradient complexity of GD is $O{({n/\epsilon^{2}})}$ in this nonconvex regime, and assuming that the stochastic gradient satisfies a (uniform) bounded variance assumption (Assumption 1 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")), the gradient complexity of SGD is $O{({1/\epsilon^{4}})}$. Note that although SGD has a worse dependence on $\epsilon$, it typically only needs to compute a constant minibatch of stochastic gradients in each iteration instead of the full batch (i.e., $n$ stochastic gradients) used in GD. Hence, SGD is better than GD if the number of data samples $n$ is very large or the error tolerance $\epsilon$ is not very small.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Gradient complexity", "weight": 1.0} -->

There has been extensive research in designing gradient-type methods with an improved dependence on $n$ and/or $\epsilon$. In particular, the SVRG method of Johnson & Zhang, the SAGA method of Defazio et al. and the SARAH method of Nguyen et al. are representatives of what is by now a large class of variance-reduced methods, which have played a particularly important role in this effort. However, the analyses in these papers focused on the convex regime. Furthermore, several accelerated (momentum) methods have been designed as well, with or without variance reduction. There are also some lower bounds given.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gradient complexity", "weight": 1.0} -->

Coming back to problem in the nonconvex regime studied in this paper, interesting recent development starts with the work of Reddi et al., and Allen-Zhu & Hazan, who have concurrently shown that if $f$ has the finite-sum form, a suitably designed minibatch version of SVRG enjoys the gradient complexity $O{({n + {n^{2/3}/\epsilon^{2}}})}$, which is an improvement on the $O{({n/\epsilon^{2}})}$ gradient complexity of GD. Subsequently, other variants of SVRG were shown to posses the same improved rate, including those developed. More recently, Fang et al. proposed the SPIDER method, and Zhou et al. proposed the SNVRG method, both of them further improve the gradient complexity to $O{({n + {\sqrt{n}/\epsilon^{2}}})}$. Further variants of the SARAH method which also achieve the same $O{({n + {\sqrt{n}/\epsilon^{2}}})}$ gradient complexity have been developed.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Gradient complexity", "weight": 1.0} -->

Also there are some lower bounds given. See Table 1 for an overview of results.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

As we show in through this work, despite enormous effort by the community to design efficient methods for solving in the nonconvex regime, there is still a considerable gap in our understanding. First, while optimal methods for in the finite-sum regime exist (e.g., SPIDER, SpiderBoost, SARAH, SSRGD ), the known lower bound $\Omega{({\sqrt{n}/\epsilon^{2}})}$ used to establish their optimality works only for $n \leq {O{({1/\epsilon^{4}})}}$, i.e., in the small data regime (see Table 1). Moreover, these methods are unnecessarily complicated, often with a double loop structure, and reliance on several hyperparameters. Besides, there is also no tight lower bound to show the optimality of optimal methods in the online regime.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Asp. 2 and 3 (PL setting)
PAGE (this paper)
$O\left( {\left( {n + {\sqrt{n}\kappa}} \right){\log\frac{1}{\epsilon}}} \right)$ 111Note that PAGE can switch to a faster linear convergence $O\left( \cdot \log\frac{1}{\epsilon} \right)$ instead of sublinear rate $O\left( \cdot \frac{1}{\epsilon^{2}} \right)$ by exploiting the local structure of the objective function via the PL condition (Assumption 3).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Online 222Note that we refer the online problem as the finite-sum problem with large or infinite n as discussed in the introduction Section 1.1. In this online case, the full gradient may not be available (e.g., if n is infinite), thus the bounded variance of stochastic gradient Assumption 1 is needed in this case.
$O\left( \frac{\sigma^{2}}{\epsilon^{4}} \right)$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Asp. 1, 2 and 3 (PL setting)
PAGE (this paper)
$O\left( {\left( {b + {\sqrt{b}\kappa}} \right){\log\frac{1}{\epsilon}}} \right)$

<!-- chunk {"id": "body-0018", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

In this paper, we resolve the above issues by designing a simple ProbAbilistic Gradient Estimator (PAGE) described in Algorithm 1 for achieving optimal convergence results in nonconvex optimization. Moreover, PAGE is very simple and easy to implement. In each iteration, PAGE uses minibatch SGD update with probability $p_{t}$, or reuses the previous gradient with a small adjustment (at a low computational cost) with probability $1 - p_{t}$ (see Line 4 of Algorithm 1).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

$\bullet$We provide tight lower bounds to close the gap for both nonconvex finite-sum problem and online problem (see Theorem 2 ‣ 4.1 Convergence for nonconvex finite-sum problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization") and Corollary 5 ‣ 4.2 Convergence for nonconvex online problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")). Our lower bounds are based and inspired by recent work.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Then we show the optimality of PAGE by proving that PAGE achieves the optimal convergence results matching our lower bounds for both nonconvex finite-sum problem and online problem (see Corollaries 2) ‣ 4.1 Convergence for nonconvex finite-sum problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization") and 4) ‣ 4.2 Convergence for nonconvex online problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")). See Table 1 for a detailed comparison.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

$\bullet$ Moreover, we show that PAGE can automatically switch to a faster *linear convergence* $O{( \cdot \log\frac{1}{\epsilon})}$ by exploiting the local structure of the objective function, via the PL condition (Assumption 3 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")), although the objective function $f$ is globally nonconvex. See the middle and the last row of Table 1 (highlighted with green color). For example, PAGE automatically switches from the sublinear rate $O{({n + {\sqrt{n}/\epsilon^{2}}})}$ to the faster linear rate $O{({{({n + {\sqrt{n}\kappa}})}{\log\frac{1}{\epsilon}}})}$ for nonconvex finite-sum problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

$\bullet$ PAGE is simple and easy to implement via a small adjustment to vanilla minibatch SGD, and takes a lower computational cost than SGD (i.e., $p_{t} = 1$ in Algorithm 1) since $b^{\prime} < b$. We conduct several deep learning experiments (e.g., LeNet, VGG, ResNet) on real datasets in PyTorch showing that PAGE indeed not only converges much faster than SGD in training but also achieves higher test accuracy. This validates our theoretical results and confirms the practical superiority of PAGE.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The PAGE gradient estimator", "weight": 1.0} -->

In this section, we describe PAGE, an SGD variant employing a new, simple and optimal gradient estimator (see Algorithm 1). In particular, PAGE was inspired by algorithmic design elements coming from methods such as SARAH, SPIDER, SSRGD (usage of a recursive estimator), and L-SVRG and SAGD (probabilistic switching between two estimators to avoid a double loop structure).

<!-- chunk {"id": "body-0024", "role": "body", "section": "The PAGE gradient estimator", "weight": 1.0} -->

In each iteration, the gradient estimator $g^{t + 1}$ of PAGE is defined in Line 4 of Algorithm 1, which indicates that PAGE uses the vanilla minibatch SGD update with probability $p_{t}$, and reuses the previous gradient $g^{t}$ with a small adjustment (which lowers the computational cost since $b^{\prime} \ll b$) with probability $1 - p_{t}$. In particular, the $p_{t} \equiv 1$ case reduces to vanilla minibatch SGD, and to GD if we further set the minibatch size to $b = n$. We give a simple formula for the optimal choice of $p_{t}$, i.e., $p_{t} \equiv \frac{b^{\prime}}{b + b^{\prime}}$ is enough for PAGE to obtain the optimal convergence rates. More details can be found in the convergence results of Section 4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The PAGE gradient estimator", "weight": 1.0} -->

Note that PAGE with constant probability $p_{t} \equiv p$ can be reduced to an equivalent form of the double loop algorithm with geometric distribution Geom-SARAH, but our single-loop PAGE is more flexible and also leads to simpler and better analysis. Similar to L-SVRG which switches between GD and SVRG probabilistically, L2S switches between GD and SARAH and uses a fixed probability $p$ (i.e., equivalent to Geom-SARAH ). However, PAGE is more general which switches between minibatch SGD and minibatch SARAH and also allows a flexible probability $p_{t}$. More importantly, the minibatch SGD update instead of GD can allow PAGE to solve both nonconvex finite-sum and online problems, while L2S can only deal with the finite-sum case. Besides, our convergence analysis of PAGE is simple and clean, which is totally different from L2S. Concretely, our analysis of PAGE directly shows the decrease for each iteration (see or ), i.e., *truly loopless analysis*.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The PAGE gradient estimator", "weight": 1.0} -->

However, L2S still uses a *double loop analysis* where they transform the probabilistic switch steps to an equivalent double loop structure and upper bound the variance term by considering all inner loop iterations together not just one iteration as ours (see Lemma 5 of L2S vs. our Lemma 3).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1 (Bounded variance)", "weight": 1.0} -->

The stochastic gradient has bounded variance if ${\exists\sigma} > 0$, such that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2 (Average $L$-smoothness)", "weight": 1.0} -->

Moreover, we also prove faster linear convergence rates for nonconvex functions under the Polyak-Łojasiewicz (PL) condition.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3 (PL condition)", "weight": 1.0} -->

A function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ satisfies PL condition ^44^4It is worth noting that the PL condition does not imply convexity of $f$. For example, ${f{(x)}} = {x^{2} + {3{\sin^{2}x}}}$ is a nonconvex function but it satisfies PL condition with $\mu = {1/32}$. if ${\exists\mu} > 0$, such that

<!-- chunk {"id": "body-0030", "role": "body", "section": "General Convergence Results", "weight": 1.0} -->

In this section, we present two main convergence theorems for PAGE (Algorithm 1): i) for nonconvex finite-sum problem (Section 4.1), and ii) for nonconvex online problem (Section 4.2). Subsequently, we formulate several corollaries which lead to the optimal convergence results. Finally, we provide tight lower bounds for both types of nonconvex problems to close the gap and validate the optimality of PAGE. See Table 1 for an overview.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergence for nonconvex finite-sum problems", "weight": 1.0} -->

In this section, we focus on the nonconvex finite-sum problems defined via. In this case, we do not need the bounded variance assumption (Assumption 1 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergence for nonconvex online problems", "weight": 1.0} -->

In this section, we focus on the nonconvex online problems, i.e.,. Recall that we refer this online problem as the finite-sum problem with large or infinite $n$. Also, we need the bounded variance assumption (Assumption 1 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")) in this online case. Similarly, we first present the main theorem in this online case and then provide corollaries with the optimal convergence results. Finally, we provide tight lower bound for validating the optimality of PAGE.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Better Convergence under PL Condition", "weight": 1.0} -->

In this section, we show that better convergence can be achieved if the loss function $f$ satisfies the PL condition (Assumption 3 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")). Note that under the PL condition, one can obtain a faster linear convergence $O{( \cdot \log\frac{1}{\epsilon})}$ (see Corollary 6) rather than the sublinear convergence $O{( \cdot \frac{1}{\epsilon^{2}})}$ (see Corollary 2) ‣ 4.1 Convergence for nonconvex finite-sum problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")). In many cases, although the loss function $f$ is globally nonconvex, some local regions (e.g., large gradient regions) may satisfy the PL condition. We prove that PAGE can *automatically* switch to the faster convergence rate in these regions where $f$ satisfies PL condition locally.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Better Convergence under PL Condition", "weight": 1.0} -->

As in Section 4, here we also establish two main theorems and the deduce corollaries for both finite-sum and online regimes. The convergence results are also listed in Table 1 (i.e., the middle row and last row).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we conduct several deep learning experiments for multi-class image classification. Concretely, we compare our PAGE algorithm with vanilla SGD by running standard LeNet, VGG and ResNet models on MNIST and CIFAR-10 datasets. We implement the algorithms in PyTorch and run the experiments on several NVIDIA Tesla V100 GPUs.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

According to the update form in PAGE (see Line 4 of Algorithm 1), PAGE enjoys a lower computational cost than vanilla minibatch SGD (i.e., $p_{t} \equiv 1$ in PAGE) since $b^{\prime} < b$. Thus, in the experiments we want to show how the performance of PAGE compares with vanilla minibatch SGD under different minibatch sizes $b$ (i.e., $b = {64,256,512}$).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Note that we do not tune the parameters for PAGE, i.e., we set $b^{\prime} = \sqrt{b}$ and $p_{t} \equiv \frac{b^{\prime}}{b + b^{\prime}} = \frac{\sqrt{b}}{b + \sqrt{b}}$ according to our theoretical results (see e.g., Corollary 2) ‣ 4.1 Convergence for nonconvex finite-sum problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization") and 4) ‣ 4.2 Convergence for nonconvex online problems ‣ 4 General Convergence Results ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization")). For the stepsize/learning rate $\eta$, we choose the same one for both PAGE and minibatch SGD according to the theoretical results.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

(2a) Different minibatch size b
(2b) Different minibatch size b
(2c) Different neural networks
Figure 2: and on CIFAR-10 dataset

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Concretely, in Figure 1, we choose standard minibatch $b = 64$ and $b = 256$ for both PAGE and vanilla minibatch SGD for MNIST experiments. In Figure 2, we choose $b = 256$ and $b = 512$ for CIFAR-10 experiments. The first row of Figures 1 and 2 denotes the training loss with respect to the gradient computations, and the second row denotes the test accuracy with respect to the gradient computations. Both Figures 1 and 2 demonstrate that PAGE not only converges much faster than SGD in training but also achieves higher test accuracy (which is typically very important in practice, e.g., lead to a better model). Moreover, the performance gap between PAGE and SGD is larger when the minibatch size $b$ is larger (i.e, gap between solid lines in Figures 1a, 1b, 2a, 2b), which is consistent with the update form of PAGE, i.e, it reuses the previous gradient with a small adjustment (lower computational cost $b^{\prime} = \sqrt{b}$ instead of $b$) with probability $1 - p_{t}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

The experimental results validate our theoretical results and confirm the practical superiority of PAGE.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

(3a) Training/test loss (3b) Training/test accuracy
Figure 3: on MNIST dataset

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

In the following, we conduct extra experiments for comparing the training loss and test loss (Figure 3a, 4a), and training accuracy and test accuracy (Figure 3b, 4b) between PAGE and SGD. Note that Figure 3 (i.e., 3a, 3b) uses MNIST dataset and Figure 4 (i.e., 4a, 4b) uses CIFAR-10 dataset. Figures (3a) and (4a) also demonstrate that PAGE converges much faster than SGD both in training loss and test loss. Moreover, Figures (3b) and (4b) demonstrate that PAGE achieves the higher test accuracy than SGD and converges faster in training accuracy. Thus, our PAGE is not only converging faster than SGD in training but also achieves the higher test accuracy (which is typically very important in practice, e.g., lead to a better model). Again, the experimental results validate our theoretical results and confirm the practical superiority of PAGE.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

(4a) Training/test loss (4b) Training/test accuracy
Figure 4: on CIFAR-10 dataset

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose a simple and optimal PAGE algorithm for both nonconvex finite-sum and online optimization. We prove tight lower bounds and show that PAGE achieves the optimal convergence results matching our lower bounds for both nonconvex finite-sum problems and online problems. We also show that for nonconvex functions satisfying the PL condition, PAGE can automatically switch to a faster linear convergence rate. Besides, PAGE is easy to implement and we conduct several deep learning experiments (e.g., LeNet, VGG, ResNet) in PyTorch which confirm the practical superiority of PAGE. More importantly, the novel convergence analysis of PAGE is very simple and clean. Thus PAGE and its analysis can be easily adopted and generalized to other works. In fact, it already leads to some further breakthroughs in communication-efficient distributed learning.
