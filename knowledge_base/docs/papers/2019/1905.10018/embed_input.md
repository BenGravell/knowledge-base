<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Momentum-Based Variance Reduction in Non-Convex SGD

Topics include Convex optimization, Gradient descent, Stochastic gradients, Optimization, Learning, Variance reduction, Stochastic gradient descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Variance reduction has emerged in recent years as a strong competitor to stochastic gradient descent in non-convex problems, providing the first algorithms to improve upon the converge rate of stochastic gradient descent for finding first-order critical points. However, variance reduction techniques typically require carefully tuned learning rates and willingness to use excessively large "mega-batches" in order to achieve their improved results. We present a new algorithm, STORM, that does not require any batches and makes use of adaptive learning rates, enabling simpler implementation and less hyperparameter tuning. Our technique for removing the batches uses a variant of momentum to achieve variance reduction in non-convex optimization. On smooth losses F, STORM finds a point boldsymbolx with E[|nabla F(boldsymbolx)|] <= O(1/sqrt(T)+sigma^(1/3)/T^(1/3)) in T iterations with sigma^ variance in the gradients, matching the optimal rate but without requiring knowledge of sigma.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper addresses the classic stochastic optimization problem, in which we are given a function $F:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, and wish to find ${\mathbf{x}} \in {\mathbb{R}}^{d}$ such that $F{({\mathbf{x}})}$ is as small as possible. Unfortunately, our access to $F$ is limited to a stochastic function oracle: we can obtain sample functions $f{( \cdot,\xi)}$ where $\xi$ represents some sample variable (e.g. a minibatch index) such that ${{\mathbb{E}}{\lbrack{f{( \cdot,\xi)}}\rbrack}} = {F{( \cdot )}}$. Stochastic optimization problems are found throughout machine learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, in supervised learning, $\mathbf{x}$ represents the parameters of a model (say the weights of a neural network), $\xi$ represents an example, $f{({\mathbf{x}},\xi)}$ represents the loss on an example, and $F$ represents the training loss of the model.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We do not assume convexity, so in general the problem of finding a true minimum of $F$ may be NP-hard. Hence, we relax the problem to finding a critical point of $F$ -- that is a point such that ${{\nabla F}{({\mathbf{x}})}} = 0$. Also, we assume access only to stochastic gradients evaluated on arbitrary points, rather than Hessians or other information. In this setting, the standard algorithm is stochastic gradient descent (SGD).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, *variance reduction* has emerged as an improved technique for finding critical points in non-convex optimization problems. Stochastic variance-reduced gradient (SVRG) algorithms also produce iterates $x_{1},\ldots,x_{T}$ according to the update formula, but now ${\mathbf{g}}_{t}$ is a *variance reduced* estimate of ${\nabla F}{({\mathbf{x}}_{t})}$. Over the last few years, SVRG algorithms have improved the convergence rate to critical points of non-convex SGD from $O{({1/T^{1/4}})}$ to $O{({1/T^{3/10}})}$ to $O{({1/T^{1/3}})}$. Despite this improvement, SVRG has not seen as much success in practice in non-convex machine learning problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many reasons may contribute to this phenomenon, but two potential issues we address here are SVRG's use of *non-adaptive learning rates* and reliance on *giant batch sizes* to construct variance reduced gradients through the use of low-noise gradients calculated at a "checkpoint". In particular, for non-convex losses SVRG analyses typically involve carefully selecting learning rates, the number of samples to construct the gradient on the checkpoint points, and the frequency of update of the checkpoint points. The optimal settings balance various unknown problem parameters exactly in order to obtain improved performance, making it especially important, and especially difficult, to tune them.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we address both of these issues. We present a new algorithm called STOchastic Recursive Momentum (Storm) that achieves variance reduction through the use of a variant of the momentum term, similar to the popular RMSProp or Adam momentum heuristics. Hence, our algorithm does not require a gigantic batch to compute checkpoint gradients -- in fact, our algorithm does not require any batches at all because it *never needs to compute a checkpoint gradient*. Storm achieves the *optimal convergence rate* of $O{({1/T^{1/3}})}$, and it uses an *adaptive learning rate* schedule that will automatically adjust to the variance values of ${\nabla f}{({\mathbf{x}}_{t},\xi_{t})}$. Overall, we consider our algorithm a significant qualitative departure from the usual paradigm for variance reduction, and we hope our analysis may provide insight into the value of momentum in non-convex optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. The next section discusses the related work on variance reduction and adaptive learning rates in non-convex SGD. Section 3 formally introduces our notation and assumptions. We present our basic update rule and its connection to SGD with momentum in Section 4, and our algorithm in Section 5. Finally, we present some empirical results in Section 6 and concludes with a discussion in Section 7.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

Before describing our algorithm in details, we briefly explore the connection between SGD with momentum and variance reduction.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

The stochastic gradient descent with momentum algorithm is typically implemented as where $a$ is small, i.e. $a = 0.1$. In words, instead of using the current gradient ${\nabla F}{({\mathbf{x}}_{t})}$ in the update of ${\mathbf{x}}_{t}$, we use an exponential average of the past observed gradients.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

While SGD with momentum and its variants have been successfully used in many machine learning applications, it is well known that the presence of noise in the stochastic gradients can nullify the theoretical gain of the momentum term \e.g.. As a result, it is unclear how and why using momentum can be better than plain SGD. Although recent works have proved that a variant of SGD with momentum improves the non-dominant terms in the convergence rate on convex stochastic least square problems, it is still unclear if the actual convergence rate can be improved.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

Here, we take a different route. Instead of showing that momentum in SGD works in the same way as in the noiseless case, i.e. giving accelerated rates, we show that *a variant of momentum can provably reduce the variance of the gradients*. In its simplest form, the variant we propose is: The only difference is the that we add the term ${({1 - a})}{({{{\nabla f}{({\mathbf{x}}_{t},\xi_{t})}} - {{\nabla f}{({\mathbf{x}}_{t - 1},\xi_{t})}}})}$ to the update. As in standard variance-reduced methods, we use two gradients in each step. However, we do not need to use the gradient calculated at any checkpoint points. Note that if ${\mathbf{x}}_{t} \approx {\mathbf{x}}_{t - 1}$, then our update becomes approximately the momentum one.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

These two terms will be similar as long as the algorithm is actually converging to some point, and so we can expect the algorithm to behave exactly like the classic momentum SGD towards the end of the optimization process.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

So, if ${\mathbb{E}}{\lbrack{\|\mathbf{\epsilon}_{t}\|}^{2}\rbrack}$ decreases over time, we have realized a variance reduction effect. Our technical result that we use to show this decrease is provided in Lemma 2, but let us take a moment here to appreciate why this should be expected intuitively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

Considering the update written, we can obtain a recursive expression for $\mathbf{\epsilon}_{t}$ by subtracting ${\nabla F}{({\mathbf{x}}_{t})}$ from both sides: Now, notice that there is good reason to expect the second and third terms of the RHS above to be small: we can control $a{({{{\nabla f}{({\mathbf{x}}_{t},\xi_{t})}} - {{\nabla F}{({\mathbf{x}}_{t})}}})}$ simply by choosing small enough values $a$, and from smoothness we expect $(\nabla f{({\mathbf{x}}_{t},\xi_{t})} - \nabla f{({\mathbf{x}}_{t - 1},\xi_{t})} - {(\nabla F{({\mathbf{x}}_{t})} - \nabla

<!-- chunk {"id": "body-0017", "role": "body", "section": "Momentum and Variance Reduction", "weight": 1.0} -->

Therefore, by choosing small enough $\eta$ and $a$, we obtain ${\|\mathbf{\epsilon}_{t}\|} = {{{({1 - a})}{\|\mathbf{\epsilon}_{t - 1}\|}} + Z}$ where $Z$ is some small value. Thus, intuitively $\|\mathbf{\epsilon}_{t}\|$ will decrease until it reaches $Z/a$. This highlights a trade-off in setting $\eta$ and $a$ in order to decrease the numerator of $Z/a$ while keeping the denominator sufficiently large. Our central challenge is showing that it is possible to achieve a favorable trade-off in which $Z/a$ is very small, resulting in small error $\mathbf{\epsilon}_{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Storm: STOchastic Recursive Momentum", "weight": 1.0} -->

1: Input: Parameters k, w, c, initial point x1 5: $\eta_{0}\leftarrow\frac{k}{w^{1/3}}$ 7: $\eta_{t}\leftarrow\frac{k}{{({w + {\sum_{i = 1}^{t}G_{t}^{2}}})}^{1/3}}$ 14: Choose $\hat{\mathbf{x}}$ uniformly at random from x1, …, xT. (In practice, set $\hat{\mathbf{x}} = {\mathbf{x}}_{T}$). 15: return $\hat{\mathbf{x}}$ Algorithm 1 Storm: STOchastic Recursive Momentum We now describe our stochastic optimization algorithm, which we call STOchastic Recursive Momentum (Storm). The pseudocode is in Algorithm 1. As described in the previous section, its basic update is of the form of and.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Storm: STOchastic Recursive Momentum", "weight": 1.0} -->

However, in order to achieve adaptivity to the noise in the gradients, both the stepsize and the momentum term will depend on the past gradients, à la AdaGrad.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Storm: STOchastic Recursive Momentum", "weight": 1.0} -->

The convergence guarantee of Storm is presented in Theorem 1 below.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Empirical Validation", "weight": 1.0} -->

(a) Train Loss vs Iterations (b) Train Accuracy vs Iterations (c) Test Accuracy vs Iterations Figure 1: Experiments on CIFAR-10 with ResNet-32 Network.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Empirical Validation", "weight": 1.0} -->

In order to confirm that our advances do indeed yield an algorithm that performs well and requires little tuning, we implemented Storm in TensorFlow and tested its performance on the CIFAR-10 image recognition benchmark using a ResNet model, as implemented by the Tensor2Tensor package ^11^1 We compare Storm to AdaGrad and Adam, which are both very popular and successful optimization algorithms. The learning rates for AdaGrad and Adam were swept over a logarithmically spaced grid. For Storm, we set $w = k = 0.1$ as a default^22^2We picked these defaults by tuning over a logarithmic grid on the much-simpler MNIST dataset. $w$ and $k$ were not tuned. and swept $c$ over a logarithmically spaced grid, so that all algorithms involved only one parameter to tune. No regularization was employed. We record train loss (cross-entropy), and accuracy on both the train and test sets (see Figure 1).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Empirical Validation", "weight": 1.0} -->

These results show that, while Storm is only marginally better than AdaGrad on test accuracy, on both training loss and accuracy Storm appears to be somewhat faster in terms of number of iterations. We note that the convergence proof we provide actually only applies to the training loss (since we are making multiple passes over the dataset). We leave for the future whether appropriate regularization can trade-off Storm's better training loss performance to obtain better test performance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced a new variance-reduction-based algorithm, Storm, that finds critical points in stochastic, smooth, non-convex problems. Our algorithm improves upon prior algorithms by virtue of removing the need for checkpoint gradients, and incorporating adaptive learning rates. These improvements mean that Storm is substantially easier to tune: it does not require choosing the size of the checkpoints, nor how often to compute the checkpoints (because there are no checkpoints), and by using adaptive learning rates the algorithm enjoys the same robustness to learning rate tuning as popular algorithms like AdaGrad or Adam. Storm obtains the optimal convergence guarantee, adapting to the level of noise in the problem without knowledge of this parameter. We verified that on CIFAR-10 with a ResNet architecture, Storm indeed seems to be optimizing the objective in fewer iterations than baseline algorithms.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Additionally, we point out that Storm's update formula is strikingly similar to the standard SGD with momentum heuristic employed in practice. To our knowledge, no theoretical result actually establishes an advantage of adding momentum to SGD in stochastic problems, creating an intriguing mystery. While our algorithm is not precisely the same as the SGD with momentum, we feel that it provides strong intuitive evidence that momentum is performing some kind of variance reduction. We therefore hope that some of the analysis techniques used in this paper may provide a path towards explaining the advantages of momentum.
