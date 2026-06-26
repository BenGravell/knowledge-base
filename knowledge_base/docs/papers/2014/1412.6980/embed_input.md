<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Adam: A Method for Stochastic Optimization

Topics include Convex optimization, Stochastic optimization, Regret bounds, Online algorithms, Optimization, Adam.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments. The method is straightforward to implement, is computationally efficient, has little memory requirements, is invariant to diagonal rescaling of the gradients, and is well suited for problems that are large in terms of data and/or parameters. The method is also appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require little tuning. Some connections to related algorithms, on which Adam was inspired, are discussed. We also analyze the theoretical convergence properties of the algorithm and provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization framework. Empirical results demonstrate that Adam works well in practice and compares favorably to other stochastic optimization methods. Finally, we discuss AdaMax, a variant of Adam based on the infinity norm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Stochastic gradient-based optimization is of core practical importance in many fields of science and engineering. Many problems in these fields can be cast as the optimization of some scalar parameterized objective function requiring maximization or minimization with respect to its parameters. If the function is differentiable w.r.t. its parameters, gradient descent is a relatively efficient optimization method, since the computation of first-order partial derivatives w.r.t. all the parameters is of the same computational complexity as just evaluating the function. Often, objective functions are stochastic. For example, many objective functions are composed of a sum of subfunctions evaluated at different subsamples of data; in this case optimization can be made more efficient by taking gradient steps w.r.t. individual subfunctions, i.e. stochastic gradient descent (SGD) or ascent. SGD proved itself as an efficient and effective optimization method that was central in many machine learning success stories, such as recent advances in deep learning. Objectives may also have other sources of noise than data subsampling, such as dropout regularization. For all such noisy objectives, efficient stochastic optimization techniques are required.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The focus of this paper is on the optimization of stochastic objectives with high-dimensional parameters spaces. In these cases, higher-order optimization methods are ill-suited, and discussion in this paper will be restricted to first-order methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We propose Adam, a method for efficient stochastic optimization that only requires first-order gradients with little memory requirement. The method computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients; the name Adam is derived from adaptive moment estimation. Our method is designed to combine the advantages of two recently popular methods: AdaGrad, which works well with sparse gradients, and RMSProp, which works well in on-line and non-stationary settings; important connections to these and other stochastic optimization methods are clarified in section 5. Some of Adam's advantages are that the magnitudes of parameter updates are invariant to rescaling of the gradient, its stepsizes are approximately bounded by the stepsize hyperparameter, it does not require a stationary objective, it works with sparse gradients, and it naturally performs a form of step size annealing.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

∗ Equal contribution. Author ordering determined by coin flip over a Google Hangout.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Jimmy Lei Ba ∗ University of Toronto jimmy@psi.utoronto.ca Algorithm 1: Adam, our proposed algorithm for stochastic optimization. See section 2 for details, and for a slightly more efficient (but less clear) order of computation. g 2 t indicates the elementwise square g t ⊙ g t. Good default settings for the tested machine learning problems are α = 0. 001, β 1 = 0. 9, β 2 = 0. 999 and ϵ = 10 -8. All operations on vectors are element-wise. With β t 1 and β t 2 we denote β 1 and β 2 to the power t.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Require: α: Stepsize Require: β 1, β 2 ∈ [0, 1): Exponential decay rates for the moment estimates Require: f (θ): Stochastic objective function with parameters θ Require: θ 0: Initial parameter vector m 0 ← 0 (Initialize 1 st moment vector) v 0 ← 0 (Initialize 2 nd moment vector) t ← 0 (Initialize timestep) while θ t not converged do t ← t +1 g t ←∇ θ f t (θ t -1) (Get gradients w.r.t.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

stochastic objective at timestep t) m t ← β 1 · m t -1 +(1 -β 1) · g t (Update biased first moment estimate) v t ← β 2 · v t -1 +(1 -β 2) · g 2 t (Update biased second raw moment estimate) ̂ m t ← m t / (1 -β t 1) (Compute bias-corrected first moment estimate) ̂ v t ← v t / (1 -β t 2) (Compute bias-corrected second raw moment estimate) θ t ← θ t -1 -α · ̂ m t / (√ ̂ v t + ϵ) (Update parameters) end while return θ t (Resulting parameters) In section 2 we describe the algorithm and the properties of its update rule. Section 3 explains our initialization bias correction technique, and section 4 provides a theoretical analysis of Adam's convergence in online convex programming. Empirically, our method consistently outperforms other methods for a variety of models and datasets, as shown in section 6. Overall, we show that Adam is a versatile algorithm that scales to large-scale high-dimensional machine learning problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "ALGORITHM", "weight": 1.0} -->

See algorithm 1 for pseudo-code of our proposed algorithm Adam. Let f ( θ ) be a noisy objective function: a stochastic scalar function that is differentiable w.r.t. parameters θ. We are interested in minimizing the expected value of this function, E [ f ( θ )] w.r.t. its parameters θ. With f 1 ( θ ),... f T ( θ ) we denote the realisations of the stochastic function at subsequent timesteps 1,..., T. The stochasticity might come from the evaluation at random subsamples (minibatches) of datapoints, or arise from inherent function noise. With g t = ∇ θ f t ( θ ) we denote the gradient, i.e. the vector of partial derivatives of f t, w.r.t θ evaluated at timestep t.

<!-- chunk {"id": "body-0011", "role": "body", "section": "ALGORITHM", "weight": 1.0} -->

The algorithm updates exponential moving averages of the gradient ( m t ) and the squared gradient ( v t ) where the hyper-parameters β 1, β 2 ∈ [0, 1) control the exponential decay rates of these moving averages. The moving averages themselves are estimates of the 1 st moment (the mean) and the 2 nd raw moment (the uncentered variance) of the gradient. However, these moving averages are initialized as (vectors of) 0's, leading to moment estimates that are biased towards zero, especially during the initial timesteps, and especially when the decay rates are small (i.e. the β s are close to 1). The good news is that this initialization bias can be easily counteracted, resulting in bias-corrected estimates m t and v t. See section 3 for more details.

<!-- chunk {"id": "body-0012", "role": "body", "section": "ALGORITHM", "weight": 1.0} -->

̂ ̂ Note that the efficiency of algorithm 1 can, at the expense of clarity, be improved upon by changing the order of computation, e.g.

<!-- chunk {"id": "body-0013", "role": "body", "section": "ADAM'S UPDATE RULE", "weight": 1.0} -->

An important property of Adam's update rule is its careful choice of stepsizes. Assuming ϵ = 0, the effective step taken in parameter space at timestep t is ∆ t = α · ̂ m t / √ ̂ v t. The effective stepsize has two upper bounds: | ∆ t | ≤ α · (1 -β 1) / √ 1 -β 2 in the case (1 -β 1) > √ 1 -β 2, and | ∆ t | ≤ α otherwise. The first case only happens in the most severe case of sparsity: when a gradient has been zero at all timesteps except at the current timestep. For less sparse cases, the effective stepsize will be smaller. When (1 -β 1) = √ 1 -β 2 we have that | ̂ m t / √ ̂ v t | < 1 therefore | ∆ t | < α. In more common scenarios, we will have that ̂ m t / √ ̂ v t ≈ ± 1 since | E [g] / √ E [g 2] | ≤ 1. The effective magnitude of the steps taken in parameter space at each timestep are approximately bounded by the stepsize setting α, i.e., | ∆ t | ⪅ α.

<!-- chunk {"id": "body-0014", "role": "body", "section": "ADAM'S UPDATE RULE", "weight": 1.0} -->

This can be understood as establishing a trust region around the current parameter value, beyond which the current gradient estimate does not provide sufficient information. This typically makes it relatively easy to know the right scale of α in advance. For many machine learning models, for instance, we often know in advance that good optima are with high probability within some set region in parameter space; it is not uncommon, for example, to have a prior distribution over the parameters. Since α sets (an upper bound of) the magnitude of steps in parameter space, we can often deduce the right order of magnitude of α such that optima can be reached from θ 0 within some number of iterations. With a slight abuse of terminology, we will call the ratio ̂ m t / √ ̂ v t the signal-to-noise ratio (SNR). With a smaller SNR the effective stepsize ∆ t will be closer to zero. This is a desirable property, since a smaller SNR means that there is greater uncertainty about whether the direction of ̂ m t corresponds to the direction of the true gradient. For example, the SNR value typically becomes closer to 0 towards an optimum, leading to smaller effective steps in parameter space: a form of automatic annealing.

<!-- chunk {"id": "body-0015", "role": "body", "section": "ADAM'S UPDATE RULE", "weight": 1.0} -->

The effective stepsize ∆ t is also invariant to the scale of the gradients; rescaling the gradients g with factor c will scale ̂ m t with a factor c and ̂ v t with a factor c 2, which cancel out: (c · ̂ m t) / (√ c 2 · ̂ v t) = ̂ m t / √ ̂ v t.

<!-- chunk {"id": "body-0016", "role": "body", "section": "INITIALIZATION BIAS CORRECTION", "weight": 1.0} -->

As explained in section 2, Adam utilizes initialization bias correction terms. We will here derive the term for the second moment estimate; the derivation for the first moment estimate is completely analogous. Let g be the gradient of the stochastic objective f, and we wish to estimate its second raw moment (uncentered variance) using an exponential moving average of the squared gradient, with decay rate β 2. Let g 1,..., g T be the gradients at subsequent timesteps, each a draw from an underlying gradient distribution g t ∼ p (g t). Let us initialize the exponential moving average as v 0 = 0 (a vector of zeros).

<!-- chunk {"id": "body-0017", "role": "body", "section": "INITIALIZATION BIAS CORRECTION", "weight": 1.0} -->

First note that the update at timestep t of the exponential moving average v t = β 2 · v t -1 +(1 -β 2) · g 2 t (where g 2 t indicates the elementwise square g t ⊙ g t) can be written as a function of the gradients at all previous timesteps: We wish to know how E [v t], the expected value of the exponential moving average at timestep t, relates to the true second moment E [g 2 t], so we can correct for the discrepancy between the two. Taking expectations of the left-hand and right-hand sides of eq.: where ζ = 0 if the true second moment E [g 2 i] is stationary; otherwise ζ can be kept small since the exponential decay rate β 1 can (and should) be chosen such that the exponential moving average assigns small weights to gradients too far in the past. What is left is the term (1 -β t 2) which is caused by initializing the running average with zeros. In algorithm 1 we therefore divide by this term to correct the initialization bias.

<!-- chunk {"id": "body-0018", "role": "body", "section": "INITIALIZATION BIAS CORRECTION", "weight": 1.0} -->

In case of sparse gradients, for a reliable estimate of the second moment one needs to average over many gradients by chosing a small value of β 2; however it is exactly this case of small β 2 where a lack of initialisation bias correction would lead to initial steps that are much larger.

<!-- chunk {"id": "body-0019", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

We analyze the convergence of Adam using the online learning framework proposed. Given an arbitrary, unknown sequence of convex cost functions f 1 (θ), f 2 (θ),..., f T (θ). At each time t, our goal is to predict the parameter θ t and evaluate it on a previously unknown cost function f t. Since the nature of the sequence is unknown in advance, we evaluate our algorithm using the regret, that is the sum of all the previous difference between the online prediction f t (θ t) and the best fixed point parameter f t (θ ∗) from a feasible set X for all the previous steps.

<!-- chunk {"id": "body-0020", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

Concretely, the regret is defined as: Theorem 4.1. Assume that the function f t has bounded gradients, ‖∇ f t (θ) ‖ 2 ≤ G, ‖∇ f t (θ) ‖ ∞ ≤ G ∞ for all θ ∈ R d and distance between any θ t generated by Adam is bounded, ‖ θ n -θ m ‖ 2 ≤ D, ‖ θ m -θ n ‖ ∞ ≤ D ∞ for any m,n ∈ { 1,..., T }, and β 1, β 2 ∈ [0, 1) satisfy β 2 1 √ β 2 < 1. Let α t = α √ t and β 1,t = β 1 λ t -1, λ ∈. Adam achieves the following guarantee, for all T ≥ 1. where θ ∗ = arg min θ ∈X ∑ T t =1 f t (θ). We show Adam has O (√ T) regret bound and a proof is given in the appendix. Our result is comparable to the best known bound for this general convex online learning problem. We also use some definitions simplify our notation, where g t ≜ ∇ f t (θ t) and g t,i as the i th element.

<!-- chunk {"id": "body-0021", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

We define g 1: t,i ∈ R t as a vector that contains the i th dimension of the gradients over all iterations till t, g 1: t,i = [g 1,i, g 2,i, · · ·, g t,i]. Also, we define γ ≜ β 2 1 √ β 2. Our following theorem holds when the learning rate α t is decaying at a rate of t -1 2 and first moment running average coefficient β 1,t decay exponentially with λ, that is typically close to 1, e.g. 1 -10 -8.

<!-- chunk {"id": "body-0022", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

Our Theorem 4.1 implies when the data features are sparse and bounded gradients, the summation term can be much smaller than its upper bound ∑ d i =1 ‖ g 1: T,i ‖ 2 << dG ∞ √ T and ∑ d i =1 √ T ̂ v T,i << dG ∞ √ T, in particular if the class of function and data features are in the form of section 1.2. Their results for the expected value E [ ∑ d i =1 ‖ g 1: T,i ‖ 2 ] also apply to Adam. In particular, the adaptive method, such as Adam and Adagrad, can achieve O (log d √ T ), an improvement over O ( √ dT ) for the non-adaptive method. Decaying β 1,t towards zero is important in our theoretical analysis and also matches previous empirical findings, e.g. suggests reducing the momentum coefficient in the end of training can improve convergence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

Finally, we can show the average regret of Adam converges, Corollary 4.2. Assume that the function f t has bounded gradients, ‖∇ f t (θ) ‖ 2 ≤ G, ‖∇ f t (θ) ‖ ∞ ≤ G ∞ for all θ ∈ R d and distance between any θ t generated by Adam is bounded, ‖ θ n -θ m ‖ 2 ≤ D, ‖ θ m -θ n ‖ ∞ ≤ D ∞ for any m,n ∈ { 1,..., T }. Adam achieves the following guarantee, for all T ≥ 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

This result can be obtained by using Theorem 4.1 and ∑ d i =1 ‖ g 1: T,i ‖ 2 ≤ dG ∞ √ T. Thus, lim T →∞ R ( T ) T = 0.

<!-- chunk {"id": "body-0025", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

To empirically evaluate the proposed method, we investigated different popular machine learning models, including logistic regression, multilayer fully connected neural networks and deep convolutional neural networks. Using large models and datasets, we demonstrate Adam can efficiently solve practical deep learning problems.

<!-- chunk {"id": "body-0026", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We use the same parameter initialization when comparing different optimization algorithms. The hyper-parameters, such as learning rate and momentum, are searched over a dense grid and the results are reported using the best hyper-parameter setting.

<!-- chunk {"id": "body-0027", "role": "body", "section": "EXPERIMENT: LOGISTIC REGRESSION", "weight": 1.0} -->

Weevaluate our proposed method on L2-regularized multi-class logistic regression using the MNIST dataset. Logistic regression has a well-studied convex objective, making it suitable for comparison of different optimizers without worrying about local minimum issues. The stepsize α in our logistic regression experiments is adjusted by 1 / √ t decay, namely α t = α √ t that matches with our theoratical prediction from section 4. The logistic regression classifies the class label directly on the 784 dimension image vectors. We compare Adam to accelerated SGD with Nesterov momentum and Adagrad using minibatch size of 128. According to Figure 1, we found that the Adam yields similar convergence as SGD with momentum and both converge faster than Adagrad.

<!-- chunk {"id": "body-0028", "role": "body", "section": "EXPERIMENT: LOGISTIC REGRESSION", "weight": 1.0} -->

As discussed, Adagrad can efficiently deal with sparse features and gradients as one of its main theoretical results whereas SGD is low at learning rare features. Adam with 1 / √ t decay on its stepsize should theoratically match the performance of Adagrad. We examine the sparse feature problem using IMDB movie review dataset. We pre-process the IMDB movie reviews into bag-of-words (BoW) feature vectors including the first 10,000 most frequent words. The 10,000 dimension BoW feature vector for each review is highly sparse. As suggested, 50% dropout noise can be applied to the BoW features during training to prevent over-fitting. In figure 1, Adagrad outperforms SGD with Nesterov momentum by a large margin both with and without dropout noise. Adam converges as fast as Adagrad. The empirical performance of Adam is consistent with our theoretical findings in sections 2 and 4. Similar to Adagrad, Adam can take advantage of sparse features and obtain faster convergence rate than normal SGD with momentum.

<!-- chunk {"id": "body-0029", "role": "body", "section": "EXPERIMENT: MULTI-LAYER NEURAL NETWORKS", "weight": 1.0} -->

Multi-layer neural network are powerful models with non-convex objective functions. Although our convergence analysis does not apply to non-convex problems, we empirically found that Adam often outperforms other methods in such cases. In our experiments, we made model choices that are consistent with previous publications in the area; a neural network model with two fully connected hidden layers with 1000 hidden units each and ReLU activation are used for this experiment with minibatch size of 128.

<!-- chunk {"id": "body-0030", "role": "body", "section": "EXPERIMENT: MULTI-LAYER NEURAL NETWORKS", "weight": 1.0} -->

First, we study different optimizers using the standard deterministic cross-entropy objective function with L 2 weight decay on the parameters to prevent over-fitting. The sum-of-functions (SFO) method is a recently proposed quasi-Newton method that works with minibatches of data and has shown good performance on optimization of multi-layer neural networks. We used their implementation and compared with Adam to train such models. Figure 2 shows that Adam makes faster progress in terms of both the number of iterations and wall-clock time. Due to the cost of updating curvature information, SFO is 5-10x slower per iteration compared to Adam, and has a memory requirement that is linear in the number minibatches.

<!-- chunk {"id": "body-0031", "role": "body", "section": "EXPERIMENT: MULTI-LAYER NEURAL NETWORKS", "weight": 1.0} -->

Stochastic regularization methods, such as dropout, are an effective way to prevent over-fitting and often used in practice due to their simplicity. SFO assumes deterministic subfunctions, and indeed failed to converge on cost functions with stochastic regularization. We compare the effectiveness of Adam to other stochastic first order methods on multi-layer neural networks trained with dropout noise. Figure 2 shows our results; Adam shows better convergence than other methods.

<!-- chunk {"id": "body-0032", "role": "body", "section": "EXPERIMENT: CONVOLUTIONAL NEURAL NETWORKS", "weight": 1.0} -->

Convolutional neural networks (CNNs) with several layers of convolution, pooling and non-linear units have shown considerable success in computer vision tasks. Unlike most fully connected neural nets, weight sharing in CNNs results in vastly different gradients in different layers. A smaller learning rate for the convolution layers is often used in practice when applying SGD. We show the effectiveness of Adam in deep CNNs. Our CNN architecture has three alternating stages of 5x5 convolution filters and 3x3 max pooling with stride of 2 that are followed by a fully connected layer of 1000 rectified linear hidden units (ReLU's). The input image are pre-processed by whitening, and Figure 2: Training of multilayer neural networks on MNIST images. (a) Neural networks using dropout stochastic regularization. (b) Neural networks with deterministic cost function. We compare with the sum-of-functions (SFO) optimizer Figure 3: Convolutional neural networks training cost. (left) Training cost for the first three epochs. (right) Training cost over 45 epochs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "EXPERIMENT: CONVOLUTIONAL NEURAL NETWORKS", "weight": 1.0} -->

CIFAR-10 with c64-c64-c128-1000 architecture. dropout noise is applied to the input layer and fully connected layer. The minibatch size is also set to 128 similar to previous experiments.

<!-- chunk {"id": "body-0034", "role": "body", "section": "EXPERIMENT: CONVOLUTIONAL NEURAL NETWORKS", "weight": 1.0} -->

Interestingly, although both Adam and Adagrad make rapid progress lowering the cost in the initial stage of the training, shown in Figure 3 (left), Adam and SGD eventually converge considerably faster than Adagrad for CNNs shown in Figure 3 (right). We notice the second moment estimate ̂ v t vanishes to zeros after a few epochs and is dominated by the ϵ in algorithm 1. The second moment estimate is therefore a poor approximation to the geometry of the cost function in CNNs comparing to fully connected network from Section 6.2. Whereas, reducing the minibatch variance through the first moment is more important in CNNs and contributes to the speed-up. As a result, Adagrad converges much slower than others in this particular experiment. Though Adam shows marginal improvement over SGD with momentum, it adapts learning rate scale for different layers instead of hand picking manually as in SGD.

<!-- chunk {"id": "body-0035", "role": "body", "section": "EXPERIMENT: BIAS-CORRECTION TERM", "weight": 1.0} -->

We also empirically evaluate the effect of the bias correction terms explained in sections 2 and 3. Discussed in section 5, removal of the bias correction terms results in a version of RMSProp with momentum. We vary the β 1 and β 2 when training a variational autoencoder (VAE) with the same architecture as in with a single hidden layer with 500 hidden units with softplus nonlinearities and a 50-dimensional spherical Gaussian latent variable. We iterated over a broad range of hyper-parameter choices, i.e. β 1 ∈ [0, 0. 9] and β 2 ∈ [0. 99, 0. 999, 0. 9999], and log 10 ( α ) ∈ [ -5,..., -1]. Values of β 2 close to 1, required for robustness to sparse gradients, results in larger initialization bias; therefore we expect the bias correction term is important in such cases of slow decay, preventing an adverse effect on optimization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "EXPERIMENT: BIAS-CORRECTION TERM", "weight": 1.0} -->

In Figure 4, values β 2 close to 1 indeed lead to instabilities in training when no bias correction term was present, especially at first few epochs of the training. The best results were achieved with small values of (1 -β 2 ) and bias correction; this was more apparent towards the end of optimization when gradients tends to become sparser as hidden units specialize to specific patterns. In summary, Adam performed equal or better than RMSProp, regardless of hyper-parameter setting.

<!-- chunk {"id": "body-0037", "role": "body", "section": "ADAMAX", "weight": 1.0} -->

In Adam, the update rule for individual weights is to scale their gradients inversely proportional to a (scaled) L 2 norm of their individual current and past gradients. We can generalize the L 2 norm based update rule to a L p norm based update rule. Such variants become numerically unstable for large p. However, in the special case where we let p → ∞, a surprisingly simple and stable algorithm emerges; see algorithm 2. We'll now derive the algorithm. Let, in case of the L p norm, the stepsize at time t be inversely proportional to v 1 /p t, where: Algorithm 2: AdaMax, a variant of Adam based on the infinity norm. See section 7.1 for details. Good default settings for the tested machine learning problems are α = 0. 002, β 1 = 0. 9 and β 2 = 0. 999. With β t 1 we denote β 1 to the power t. Here, (α/ (1 -β t 1)) is the learning rate with the bias-correction term for the first moment. All operations on vectors are element-wise.

<!-- chunk {"id": "body-0038", "role": "body", "section": "ADAMAX", "weight": 1.0} -->

Require: f (θ): Stochastic objective function with parameters θ Require: β 1, β 2 ∈ [0, 1): Exponential decay rates Require: θ 0: Initial parameter vector u 0 ← 0 (Initialize the exponentially weighted infinity norm) m 0 ← 0 (Initialize 1 st moment vector) while θ t not converged do g t ←∇ θ f t (θ t -1) (Get gradients w.r.t. stochastic objective at timestep t) u t ← max(β 2 · u t -1, | g t |) (Update the exponentially weighted infinity norm) m t ← β 1 · m t -1 +(1 -β 1) · g t (Update biased first moment estimate) return θ t (Resulting parameters)

<!-- chunk {"id": "body-0039", "role": "body", "section": "end while", "weight": 1.0} -->

Note that the decay term is here equivalently parameterised as β p 2 instead of β 2. Now let p → ∞, and define u t = lim p →∞ (v t) 1 /p, then: Which corresponds to the remarkably simple recursive formula: with initial value u 0 = 0. Note that, conveniently enough, we don't need to correct for initialization bias in this case. Also note that the magnitude of parameter updates has a simpler bound with AdaMax than Adam, namely: | ∆ t | ≤ α.

<!-- chunk {"id": "body-0040", "role": "body", "section": "TEMPORAL AVERAGING", "weight": 1.0} -->

Since the last iterate is noisy due to stochastic approximation, better generalization performance is often achieved by averaging. Previously in Moulines & Bach, Polyak-Ruppert averaging has been shown to improve the convergence of standard SGD, where ¯ θ t = 1 t ∑ n k =1 θ k. Alternatively, an exponential moving average over the parameters can be used, giving higher weight to more recent parameter values. This can be trivially implemented by adding one line to the inner loop of algorithms 1 and 2: ¯ θ t ← β 2 · ¯ θ t -1 +(1 -β 2 ) θ t, with ¯ θ 0 = 0. Initalization bias can again be corrected by the estimator ̂ θ t = ¯ θ t / (1 -β t 2 ).

<!-- chunk {"id": "body-0041", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have introduced a simple and computationally efficient algorithm for gradient-based optimization of stochastic objective functions. Our method is aimed towards machine learning problems with large datasets and/or high-dimensional parameter spaces. The method combines the advantages of two recently popular optimization methods: the ability of AdaGrad to deal with sparse gradients, and the ability of RMSProp to deal with non-stationary objectives. The method is straightforward to implement and requires little memory. The experiments confirm the analysis on the rate of convergence in convex problems. Overall, we found Adam to be robust and well-suited to a wide range of non-convex optimization problems in the field machine learning.
