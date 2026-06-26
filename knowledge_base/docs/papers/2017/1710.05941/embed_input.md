<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Searching for Activation Functions

Topics include Activation functions, Swish, Neural architecture search, Reinforcement learning, ImageNet, ReLU alternatives, Deep learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This paper uses search over activation-function expressions to discover Swish, a smooth self-gated nonlinearity of the form x times a sigmoid. The empirical result is important less because every searched function transfers, and more because a simple ReLU-like smooth gate became a strong activation baseline for deep vision networks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The choice of activation functions in deep networks has a significant effect on the training dynamics and task performance. Currently, the most successful and widely-used activation function is the Rectified Linear Unit (ReLU). Although various hand-designed alternatives to ReLU have been proposed, none have managed to replace it due to inconsistent gains. In this work, we propose to leverage automatic search techniques to discover new activation functions. Using a combination of exhaustive and reinforcement learning-based search, we discover multiple novel activation functions. We verify the effectiveness of the searches by conducting an empirical evaluation with the best discovered activation function. Our experiments show that the best discovered activation function, f(x) = x * sigmoid(beta x), which we name Swish, tends to work better than ReLU on deeper models across a number of challenging datasets. For example, simply replacing ReLUs with Swish units improves top-1 classification accuracy on ImageNet by 0.9\% for Mobile NASNet-A and 0.6\% for Inception-ResNet-v2. The simplicity of Swish and its similarity to ReLU make it easy for practitioners to replace ReLUs with Swish units in any neural network.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the heart of every deep network lies a linear transformation followed by an activation function $f{( \cdot )}$. The activation function plays a major role in the success of training deep neural networks. Currently, the most successful and widely-used activation function is the Rectified Linear Unit (ReLU), defined as ${f{(x)}} = {\max{(x,0)}}$. The use of ReLUs was a breakthrough that enabled the fully supervised training of state-of-the-art deep networks. Deep networks with ReLUs are more easily optimized than networks with sigmoid or tanh units, because gradients are able to flow when the input to the ReLU function is positive. Thanks to its simplicity and effectiveness, ReLU has become the default activation function used across the deep learning community.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While numerous activation functions have been proposed to replace ReLU, none have managed to gain the widespread adoption that ReLU enjoys. Many practitioners have favored the simplicity and reliability of ReLU because the performance improvements of the other activation functions tend to be inconsistent across different models and datasets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The activation functions proposed to replace ReLU were hand-designed to fit properties deemed to be important. However, the use of search techniques to automate the discovery of traditionally human-designed components has recently shown to be extremely effective. For example, Zoph et al. used reinforcement learning-based search to find a replicable convolutional cell that outperforms human-designed architectures on ImageNet.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we use automated search techniques to discover novel activation functions. We focus on finding new scalar activation functions, which take in as input a scalar and output a scalar, because scalar activation functions can be used to replace the ReLU function without changing the network architecture. Using a combination of exhaustive and reinforcement learning-based search, we find a number of novel activation functions that show promising performance. To further validate the effectiveness of using searches to discover scalar activation functions, we empirically evaluate the best discovered activation function. The best discovered activation function, which we call *Swish*, is ${f{(x)}} = {{x \cdot \text{sigmoid}}{({\betax})}}$, where $\beta$ is a constant or trainable parameter. Our extensive experiments show that Swish consistently matches or outperforms ReLU on deep networks applied to a variety of challenging domains such as image classification and machine translation. On ImageNet, replacing ReLUs with Swish units improves top-1 classification accuracy by 0.9% on Mobile NASNet-A and 0.6% on Inception-ResNet-v2.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

These accuracy gains are significant given that one year of architectural tuning and enlarging yielded 1.3% accuracy improvement going from Inception V3 to Inception-ResNet-v2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Methods", "weight": 1.0} -->

In order to utilize search techniques, a search space that contains promising candidate activation functions must be designed. An important challenge in designing search spaces is balancing the size and expressivity of the search space. An overly constrained search space will not contain novel activation functions, whereas a search space that is too large will be difficult to effectively search. To balance the two criteria, we design a simple search space inspired by the optimizer search space of Bello et al. that composes unary and binary functions to construct the activation function.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methods", "weight": 1.0} -->

As shown in Figure 1, the activation function is constructed by repeatedly composing the the "core unit", which is defined as $b{({u_{1}{(x_{1})}},{u_{2}{(x_{2})}})}$. The core unit takes in two scalar inputs, passes each input independently through an unary function, and combines the two unary outputs with a binary function that outputs a scalar. Since our aim is to find scalar activation functions which transform a single scalar input into a single scalar output, the inputs of the unary functions are restricted to the layer preactivation $x$ and the binary function outputs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Methods", "weight": 1.0} -->

Given the search space, the goal of the search algorithm is to find effective choices for the unary and binary functions. The choice of the search algorithm depends on the size of the search space. If the search space is small, such as when using a single core unit, it is possible to exhaustively enumerate the entire search space. If the core unit is repeated multiple times, the search space will be extremely large (i.e., on the order of $10^{12}$ possibilities), making exhaustive search infeasible.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Methods", "weight": 1.0} -->

For large search spaces, we use an RNN controller, which is visualized in Figure 2. At each timestep, the controller predicts a single component of the activation function. The prediction is fed back to the controller in the next timestep, and this process is repeated until every component of the activation function is predicted. The predicted string is then used to construct the activation function.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Methods", "weight": 1.0} -->

Once a candidate activation function has been generated by the search algorithm, a "child network" with the candidate activation function is trained on some task, such as image classification on CIFAR-10. After training, the validation accuracy of the child network is recorded and used to update the search algorithm. In the case of exhaustive search, a list of the top performing activation functions ordered by validation accuracy is maintained. In the case of the RNN controller, the controller is trained with reinforcement learning to maximize the validation accuracy, where the validation accuracy serves as the reward. This training pushes the controller to generate activation functions that have high validation accuracies.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Methods", "weight": 1.0} -->

Since evaluating a single activation function requires training a child network, the search is computationally expensive. To decrease the wall clock time required to conduct the search, a distributed training scheme is used to parallelize the training of each child network. In this scheme, the search algorithm proposes a batch of candidate activation functions which are added to a queue. Worker machines pull activation functions off the queue, train a child network, and report back the final validation accuracy of the corresponding activation function. The validation accuracies are aggregated and used to update the search algorithm.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Search Findings", "weight": 1.0} -->

We conduct all our searches with the ResNet-20 as the child network architecture, and train on CIFAR-10 for 10K steps. This constrained environment could potentially skew the results because the top performing activation functions might only perform well for small networks. However, we show in the experiments section that many of the discovered functions generalize to larger models. Exhaustive search is used for small search spaces, while an RNN controller is used for larger search spaces. The RNN controller is trained with Policy Proximal Optimization, using the exponential moving average of rewards as a baseline to reduce variance. The full list unary and binary functions considered are as follows: where $\beta$ indicates a per-channel trainable parameter and ${\sigma{(x)}} = {({1 + {\exp{({- x})}}})}^{- 1}$ is the sigmoid function. Different search spaces are created by varying the number of core units used to construct the activation function and varying the unary and binary functions available to the search algorithm.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Search Findings", "weight": 1.0} -->

A common structure shared by the top activation functions is the use of the raw preactivation $x$ as input to the final binary function: $b{(x,{g{(x)}})}$. The ReLU function also follows this structure, where ${b{(x_{1},x_{2})}} = {\max{(x_{1},x_{2})}}$ and ${g{(x)}} = 0$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Search Findings", "weight": 1.0} -->

The searches discovered activation functions that utilize periodic functions, such as $\sin$ and $\cos$. The most common use of periodic functions is through addition or subtraction with the raw preactivation $x$ (or a linearly scaled $x$). The use of periodic functions in activation functions has only been briefly explored in prior work, so these discovered functions suggest a fruitful route for further research.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Search Findings", "weight": 1.0} -->

Functions that use division tend to perform poorly because the output explodes when the denominator is near $0$. Division is successful only when functions in the denominator are either bounded away from $0$, such as $\cosh{(x)}$, or approach $0$ only when the numerator also approaches $0$, producing an output of $1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Search Findings", "weight": 1.0} -->

Since the activation functions were found using a relatively small child network, their performance may not generalize when applied to bigger models. To test the robustness of the top performing novel activation functions to different architectures, we run additional experiments using the preactivation ResNet-164 (RN), Wide ResNet 28-10 (WRN), and DenseNet 100-12 (DN) models. We implement the 3 models in TensorFlow and replace the ReLU function with each of the top novel activation functions discovered by the searches. We use the same hyperparameters described in each work, such as optimizing using SGD with momentum, and follow previous works by reporting the median of 5 different runs.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Search Findings", "weight": 1.0} -->

The results are shown in Tables 2 and 2. Despite the changes in model architecture, six of the eight activation functions successfully generalize. Of these six activation functions, all match or outperform ReLU on ResNet-164. Furthermore, two of the discovered activation functions, ${x \cdot \sigma}{({\betax})}$ and $\max{(x,{\sigma{(x)}})}$, consistently match or outperform ReLU on all three models.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Search Findings", "weight": 1.0} -->

While these results are promising, it is still unclear whether the discovered activation functions can successfully replace ReLU on challenging real world datasets. In order to validate the effectiveness of the searches, in the rest of this work we focus on empirically evaluating the activation function ${f{(x)}} = {{x \cdot \sigma}{({\betax})}}$, which we call *Swish*. We choose to extensively evaluate Swish instead of $\max{(x,{\sigma{(x)}})}$ because early experimentation showed better generalization for Swish. In the following sections, we analyze the properties of Swish and then conduct a thorough empirical evaluation comparing Swish, ReLU, and other candidate baseline activation functions on number of large models across a variety of tasks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Swish", "weight": 1.0} -->

To recap, Swish is defined as ${x \cdot \sigma}{({\betax})}$, where ${\sigma{(z)}} = {({1 + {\exp{({- z})}}})}^{- 1}$ is the sigmoid function and $\beta$ is either a constant or a trainable parameter. Figure 5 plots the graph of Swish for different values of $\beta$. If $\beta = 1$, Swish is equivalent to the Sigmoid-weighted Linear Unit (SiL) of Elfwing et al. that was proposed for reinforcement learning. If $\beta = 0$, Swish becomes the scaled linear function ${f{(x)}} = \frac{x}{2}$. As $\beta\rightarrow\infty$, the sigmoid component approaches a $0$-$1$ function, so Swish becomes like the ReLU function. This suggests that Swish can be loosely viewed as a smooth function which nonlinearly interpolates between the linear function and the ReLU function.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Swish", "weight": 1.0} -->

The degree of interpolation can be controlled by the model if $\beta$ is set as a trainable parameter.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Swish", "weight": 1.0} -->

Like ReLU, Swish is unbounded above and bounded below. Unlike ReLU, Swish is smooth and non-monotonic. In fact, the non-monotonicity property of Swish distinguishes itself from most common activation functions. The derivative of Swish is The first derivative of Swish is shown in Figure 5 for different values of $\beta$. The scale of $\beta$ controls how fast the first derivative asymptotes to $0$ and $1$. When $\beta = 1$, the derivative has magnitude less than $1$ for inputs that are less than around $1.25$. Thus, the success of Swish with $\beta = 1$ implies that the gradient preserving property of ReLU (i.e., having a derivative of 1 when $x > 0$) may no longer be a distinct advantage in modern architectures.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Swish", "weight": 1.0} -->

The most striking difference between Swish and ReLU is the non-monotonic "bump" of Swish when $x < 0$. As shown in Figure 7, a large percentage of preactivations fall inside the domain of the bump ($- 5 \leq x \leq 0)$, which indicates that the non-monotonic bump is an important aspect of Swish. The shape of the bump can be controlled by changing the $\beta$ parameter. While fixing $\beta = 1$ is effective in practice, the experiments section shows that training $\beta$ can further improve performance on some models. Figure 7 plots distribution of trained $\beta$ values from a Mobile NASNet-A model. The trained $\beta$ values are spread out between $0$ and $1.5$ and have a peak at $\beta \approx 1$, suggesting that the model takes advantage of the additional flexibility of trainable $\beta$ parameters.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Swish", "weight": 1.0} -->

Practically, Swish can be implemented with a single line code change in most deep learning libraries, such as TensorFlow (e.g., x \* tf.sigmoid(beta \* x) or tf.nn.swish(x) if using a version of TensorFlow released after the submission of this work). As a cautionary note, if BatchNorm is used, the scale parameter should be set. Some high level libraries turn off the scale parameter by default due to the ReLU function being piecewise linear, but this setting is incorrect for Swish. For training Swish networks, we found that slightly lowering the learning rate used to train ReLU networks works well.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments with Swish", "weight": 1.0} -->

We benchmark Swish against ReLU and a number of recently proposed activation functions on challenging datasets, and find that Swish matches or exceeds the baselines on nearly all tasks. The following sections will describe our experimental settings and results in greater detail. As a summary, Table 3 shows Swish in comparison to each baseline activation function we considered (which are defined in the next section). The results in Table 3 are aggregated by comparing the performance of Swish to the performance of different activation functions applied to a variety of models, such as Inception ResNet-v2 and Transformer, across multiple datasets, such as CIFAR, ImageNet, and English$\rightarrow$German translation.^11^1To avoid skewing the comparison, each model type is compared just once. A model with multiple results is represented by the median of its results.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments with Swish", "weight": 1.0} -->

Specifically, the models with aggregated results are (a) ResNet-164, Wide ResNet 28-10, and DenseNet 100-12 across the CIFAR-10 and CIFAR-100 results, (b) Mobile NASNet-A and Inception-ResNet-v2 across the 3 runs, and (c) WMT Transformer model across the 4 newstest results. The improvement of Swish over other activation functions is statistically significant under a one-sided paired sign test.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Set Up", "weight": 1.0} -->

We compare Swish against several additional baseline activation functions on a variety of models and datasets. Since many activation functions have been proposed, we choose the most common activation functions to compare against, and follow the guidelines laid out in each work: Leaky ReLU (*LReLU*): where $\alpha = 0.01$. LReLU enables a small amount of information to flow when $x < 0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Set Up", "weight": 1.0} -->

Parametric ReLU (*PReLU*): The same form as LReLU but $\alpha$ is a learnable parameter. Each channel has a shared $\alpha$ which is initialized to $0.25$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Set Up", "weight": 1.0} -->

Softplus: ${f{(x)}} = {\log{({1 + {\exp{(x)}}})}}$. Softplus is a smooth function with properties similar to Swish, but is strictly positive and monotonic. It can be viewed as a smooth version of ReLU.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Set Up", "weight": 1.0} -->

Exponential Linear Unit (*ELU*): Scaled Exponential Linear Unit (*SELU*): with $\alpha \approx 1.6733$ and $\lambda \approx 1.0507$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Set Up", "weight": 1.0} -->

Gaussian Error Linear Unit (*GELU*): ${f{(x)}} = {{x \cdot \Phi}{(x)}}$, where $\Phi{(x)}$ is the cumulative distribution function of the standard normal distribution. GELU is a nonmonotonic function that has a shape similar to Swish with $\beta = 1.4$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Set Up", "weight": 1.0} -->

We evaluate both Swish with a trainable $\beta$ and Swish with a fixed $\beta = 1$ (which for simplicity we call Swish-1, but it is equivalent to the Sigmoid-weighted Linear Unit of Elfwing et al. ). Note that our results may not be directly comparable to the results in the corresponding works due to differences in our training setup.

<!-- chunk {"id": "body-0035", "role": "body", "section": "CIFAR", "weight": 1.0} -->

We first compare Swish to all the baseline activation functions on the CIFAR-10 and CIFAR-100 datasets. We follow the same set up used when comparing the activation functions discovered by the search techniques, and compare the median of 5 runs with the preactivation ResNet-164, Wide ResNet 28-10 (WRN), and DenseNet 100-12 models.

<!-- chunk {"id": "body-0036", "role": "body", "section": "CIFAR", "weight": 1.0} -->

The results in Tables 5 and 5 show how Swish and Swish-1 consistently matches or outperforms ReLU on every model for both CIFAR-10 and CIFAR-100. Swish also matches or exceeds the best baseline performance on almost every model. Importantly, the "best baseline" changes between different models, which demonstrates the stability of Swish to match these varying baselines. Softplus, which is smooth and approaches zero on one side, similar to Swish, also has strong performance.

<!-- chunk {"id": "body-0037", "role": "body", "section": "ImageNet", "weight": 1.0} -->

Next, we benchmark Swish against the baseline activation functions on the ImageNet 2012 classification dataset. ImageNet is widely considered one of most important image classification datasets, consisting of a 1,000 classes and 1.28 million training images. We evaluate on the validation dataset, which has 50,000 images.

<!-- chunk {"id": "body-0038", "role": "body", "section": "ImageNet", "weight": 1.0} -->

We compare all the activation functions on a variety of architectures designed for ImageNet: Inception-ResNet-v2, Inception-v4, Inception-v3, MobileNet, and Mobile NASNet-A. All these architectures were designed with ReLUs. We again replace the ReLU activation function with different activation functions and train for a fixed number of steps, determined by the convergence of the ReLU baseline. For each activation function, we try 3 different learning rates with RMSProp and pick the best.^22^2For some of the models with ELU, SELU, and PReLU, we train with an additional 3 learning rates (so a total of 6 learning rates) because the original 3 learning rates did not converge. All networks are initialized with He initialization.^33^3For SELU, we tried both He initialization and the initialization recommended in Klambauer et al., and choose the best result for each model separately. To verify that the performance differences are reproducible, we run the Inception-ResNet-v2 and Mobile NASNet-A experiments 3 times with the best learning rate from the first experiment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "ImageNet", "weight": 1.0} -->

We plot the learning curves for Mobile NASNet-A in Figure 8.

<!-- chunk {"id": "body-0040", "role": "body", "section": "ImageNet", "weight": 1.0} -->

The results in Tables 6-10 show strong performance for Swish. On Inception-ResNet-v2, Swish outperforms ReLU by a nontrivial $0.5\%$. Swish performs especially well on mobile sized models, with a $1.4\%$ boost on Mobile NASNet-A and a $2.2\%$ boost on MobileNet over ReLU. Swish also matches or exceeds the best performing baseline on most models, where again, the best performing baseline differs depending on the model. Softplus achieves accuracies comparable to Swish on the larger models, but performs worse on both mobile sized models. For Inception-v4, the gains from switching between activation functions is more limited, and Swish slightly underperforms Softplus and ELU. In general, the results suggest that switching to Swish improves performance with little additional tuning.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Machine Translation", "weight": 1.0} -->

We additionally benchmark Swish on the domain of machine translation. We train machine translation models on the standard WMT 2014 English$\rightarrow$German dataset, which has 4.5 million training sentences, and evaluate on 4 different newstest sets using the standard BLEU metric. We use the attention based Transformer model, which utilizes ReLUs in a 2-layered feedforward network between each attention layer. We train a 12 layer "Base Transformer" model with 2 different learning rates^44^4We tried an additional learning rate for Softplus, but found it did not work well across all learning rates. for 300K steps, but otherwise use the same hyperparameters as in the original work, such as using Adam to optimize.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Machine Translation", "weight": 1.0} -->

Table 11 shows that Swish outperforms or matches the other baselines on machine translation. Swish-1 does especially well on newstest2016, exceeding the next best performing baseline by $0.6$ BLEU points. The worst performing baseline function is Softplus, demonstrating inconsistency in performance across differing domains. In contrast, Swish consistently performs well across multiple domains.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we utilized automatic search techniques to discover novel activation functions that have strong empirical performance. We then empirically validated the best discovered activation function, which we call Swish and is defined as ${f{(x)}} = {{x \cdot \text{sigmoid}}{({\betax})}}$. Our experiments used models and hyperparameters that were designed for ReLU and just replaced the ReLU activation function with Swish; even this simple, suboptimal procedure resulted in Swish consistently outperforming ReLU and other activation functions. We expect additional gains to be made when these models and hyperparameters are specifically designed with Swish in mind. The simplicity of Swish and its similarity to ReLU means that replacing ReLUs in any network is just a simple one line code change.
