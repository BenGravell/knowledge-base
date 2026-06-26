<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Overview of Gradient Descent Optimization Algorithms

Topics include Gradient descent, Distributed systems, Optimization, Optimization algorithm.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Gradient descent optimization algorithms, while increasingly popular, are often used as black-box optimizers, as practical explanations of their strengths and weaknesses are hard to come . This article aims to provide the reader with intuitions with regard to the behaviour of different algorithms that will allow her to put them to use. In the course of this overview, we look at different variants of gradient descent, summarize challenges, introduce the most common optimization algorithms, review architectures in a parallel and distributed setting, and investigate additional strategies for optimizing gradient descent.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient descent is one of the most popular algorithms to perform optimization and by far the most common way to optimize neural networks. At the same time, every state-of-the-art Deep Learning library contains implementations of various algorithms to optimize gradient descent. These algorithms, however, are often used as black-box optimizers, as practical explanations of their strengths and weaknesses are hard to come.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This article aims at providing the reader with intuitions with regard to the behaviour of different algorithms for optimizing gradient descent that will help her put them to use. In Section 2, we are first going to look at the different variants of gradient descent. We will then briefly summarize challenges during training in Section 3. Subsequently, in Section 4, we will introduce the most common optimization algorithms by showing their motivation to resolve these challenges and how this leads to the derivation of their update rules. Afterwards, in Section 5, we will take a short look at algorithms and architectures to optimize gradient descent in a parallel and distributed setting. Finally, we will consider additional strategies that are helpful for optimizing gradient descent in Section 6.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient descent is a way to minimize an objective function $J{(\theta)}$ parameterized by a model's parameters $\theta \in {\mathbb{R}}^{d}$ by updating the parameters in the opposite direction of the gradient of the objective function ${\nabla_{\theta}J}{(\theta)}$ w.r.t. to the parameters. The learning rate $\eta$ determines the size of the steps we take to reach a (local) minimum. In other words, we follow the direction of the slope of the surface created by the objective function downhill until we reach a valley.^44^4If you are unfamiliar with gradient descent, you can find a good introduction on optimizing neural networks at

<!-- chunk {"id": "body-0006", "role": "body", "section": "Gradient descent variants", "weight": 1.0} -->

There are three variants of gradient descent, which differ in how much data we use to compute the gradient of the objective function. Depending on the amount of data, we make a trade-off between the accuracy of the parameter update and the time it takes to perform an update.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Batch gradient descent", "weight": 1.0} -->

Vanilla gradient descent, aka batch gradient descent, computes the gradient of the cost function w.r.t. to the parameters $\theta$ for the entire training dataset: As we need to calculate the gradients for the whole dataset to perform just *one* update, batch gradient descent can be very slow and is intractable for datasets that do not fit in memory. Batch gradient descent also does not allow us to update our model *online*, i.e. with new examples on-the-fly.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Batch gradient descent", "weight": 1.0} -->

In code, batch gradient descent looks something like this: [⬇](data:text/plain;base64,Zm9yIGkgaW4gcmFuZ2UobmJfZXBvY2hzKToKICBwYXJhbXNfZ3JhZCA9IGV2YWx1YXRlX2dyYWRpZW50KGxvc3NfZnVuY3Rpb24sIGRhdGEsIHBhcmFtcykKICBwYXJhbXMgPSBwYXJhbXMgLSBsZWFybmluZ19yYXRlICogcGFyYW1zX2dyYWQ=){download=""} for i in range(nb_epochs): params_grad = evaluate_gradient(loss_function, data, params) params = params - learning_rate \* params_grad For a pre-defined number of epochs, we first compute the gradient vector params_grad of the loss function for the whole dataset w.r.t. our parameter vector params. Note that state-of-the-art deep learning libraries provide automatic differentiation that efficiently computes the gradient w.r.t. some parameters. If you derive the gradients yourself, then gradient checking is a good idea.^55^5Refer to for some great tips on how to check gradients properly.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Batch gradient descent", "weight": 1.0} -->

We then update our parameters in the direction of the gradients with the learning rate determining how big of an update we perform. Batch gradient descent is guaranteed to converge to the global minimum for convex error surfaces and to a local minimum for non-convex surfaces.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stochastic gradient descent", "weight": 1.0} -->

Stochastic gradient descent (SGD) in contrast performs a parameter update for *each* training example $x^{(i)}$ and label $y^{(i)}$: Batch gradient descent performs redundant computations for large datasets, as it recomputes gradients for similar examples before each parameter update. SGD does away with this redundancy by performing one update at a time. It is therefore usually much faster and can also be used to learn online. SGD performs frequent updates with a high variance that cause the objective function to fluctuate heavily as in Figure 1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Mini-batch gradient descent", "weight": 1.0} -->

Mini-batch gradient descent finally takes the best of both worlds and performs an update for every mini-batch of $n$ training examples: This way, it a) reduces the variance of the parameter updates, which can lead to more stable convergence; and b) can make use of highly optimized matrix optimizations common to state-of-the-art deep learning libraries that make computing the gradient w.r.t. a mini-batch very efficient. Common mini-batch sizes range between $50$ and $256$, but can vary for different applications. Mini-batch gradient descent is typically the algorithm of choice when training a neural network and the term SGD usually is employed also when mini-batches are used. Note: In modifications of SGD in the rest of this post, we leave out the parameters $x^{({i:{i + n}})};y^{({i:{i + n}})}$ for simplicity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Mini-batch gradient descent", "weight": 1.0} -->

In code, instead of iterating over examples, we now iterate over mini-batches of size $50$: [⬇](data:text/plain;base64,Zm9yIGkgaW4gcmFuZ2UobmJfZXBvY2hzKToKICBucC5yYW5kb20uc2h1ZmZsZShkYXRhKQogIGZvciBiYXRjaCBpbiBnZXRfYmF0Y2hlcyhkYXRhLCBiYXRjaF9zaXplPTUwKToKICAgIHBhcmFtc19ncmFkID0gZXZhbHVhdGVfZ3JhZGllbnQobG9zc19mdW5jdGlvbiwgYmF0Y2gsIHBhcmFtcykKICAgIHBhcmFtcyA9IHBhcmFtcyAtIGxlYXJuaW5nX3JhdGUgKiBwYXJhbXNfZ3JhZA==){download=""} for i in range(nb_epochs): np.random.shuffle(data) for batch in get_batches(data, batch_size=50): params_grad = evaluate_gradient(loss_function, batch, params) params = params - learning_rate \* params_grad

<!-- chunk {"id": "body-0013", "role": "body", "section": "Challenges", "weight": 1.0} -->

Vanilla mini-batch gradient descent, however, does not guarantee good convergence, but offers a few challenges that need to be addressed: Choosing a proper learning rate can be difficult. A learning rate that is too small leads to painfully slow convergence, while a learning rate that is too large can hinder convergence and cause the loss function to fluctuate around the minimum or even to diverge.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Challenges", "weight": 1.0} -->

Learning rate schedules try to adjust the learning rate during training by e.g. annealing, i.e. reducing the learning rate according to a pre-defined schedule or when the change in objective between epochs falls below a threshold. These schedules and thresholds, however, have to be defined in advance and are thus unable to adapt to a dataset's characteristics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Challenges", "weight": 1.0} -->

Additionally, the same learning rate applies to all parameter updates. If our data is sparse and our features have very different frequencies, we might not want to update all of them to the same extent, but perform a larger update for rarely occurring features.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Challenges", "weight": 1.0} -->

Another key challenge of minimizing highly non-convex error functions common for neural networks is avoiding getting trapped in their numerous suboptimal local minima. Dauphin et al. argue that the difficulty arises in fact not from local minima but from saddle points, i.e. points where one dimension slopes up and another slopes down. These saddle points are usually surrounded by a plateau of the same error, which makes it notoriously hard for SGD to escape, as the gradient is close to zero in all dimensions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gradient descent optimization algorithms", "weight": 1.0} -->

In the following, we will outline some algorithms that are widely used by the Deep Learning community to deal with the aforementioned challenges. We will not discuss algorithms that are infeasible to compute in practice for high-dimensional data sets, e.g. second-order methods such as Newton's method^66^6

<!-- chunk {"id": "body-0018", "role": "body", "section": "Momentum", "weight": 1.0} -->

SGD has trouble navigating ravines, i.e. areas where the surface curves much more steeply in one dimension than in another, which are common around local optima. In these scenarios, SGD oscillates across the slopes of the ravine while only making hesitant progress along the bottom towards the local optimum as in Figure 2(a).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Momentum", "weight": 1.0} -->

(a) SGD without momentum (b) SGD with momentum Figure 2: Source: Genevieve B. Orr Momentum is a method that helps accelerate SGD in the relevant direction and dampens oscillations as can be seen in Figure 2(b). It does this by adding a fraction $\gamma$ of the update vector of the past time step to the current update vector^77^7Some implementations exchange the signs in the equations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Momentum", "weight": 1.0} -->

The momentum term $\gamma$ is usually set to $0.9$ or a similar value.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Momentum", "weight": 1.0} -->

Essentially, when using momentum, we push a ball down a hill. The ball accumulates momentum as it rolls downhill, becoming faster and faster on the way (until it reaches its terminal velocity, if there is air resistance, i.e. $\gamma < 1$). The same thing happens to our parameter updates: The momentum term increases for dimensions whose gradients point in the same directions and reduces updates for dimensions whose gradients change directions. As a result, we gain faster convergence and reduced oscillation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Nesterov accelerated gradient", "weight": 1.0} -->

However, a ball that rolls down a hill, blindly following the slope, is highly unsatisfactory. We would like to have a smarter ball, a ball that has a notion of where it is going so that it knows to slow down before the hill slopes up again.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Nesterov accelerated gradient", "weight": 1.0} -->

Nesterov accelerated gradient (NAG) is a way to give our momentum term this kind of prescience. We know that we will use our momentum term $\gammav_{t - 1}$ to move the parameters $\theta$. Computing $\theta - {\gammav_{t - 1}}$ thus gives us an approximation of the next position of the parameters (the gradient is missing for the full update), a rough idea where our parameters are going to be. We can now effectively look ahead by calculating the gradient not w.r.t. to our current parameters $\theta$ but w.r.t. the approximate future position of our parameters: Again, we set the momentum term $\gamma$ to a value of around $0.9$. While Momentum first computes the current gradient (small blue vector in Figure 3) and then takes a big jump in the direction of the updated accumulated gradient (big blue vector), NAG first makes a big jump in the direction of the previous accumulated gradient (brown vector), measures the gradient and then makes a correction (green vector).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Nesterov accelerated gradient", "weight": 1.0} -->

This anticipatory update prevents us from going too fast and results in increased responsiveness, which has significantly increased the performance of RNNs on a number of tasks.^88^8Refer to for another explanation of the intuitions behind NAG, while Ilya Sutskever gives a more detailed overview in his PhD thesis.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Nesterov accelerated gradient", "weight": 1.0} -->

Now that we are able to adapt our updates to the slope of our error function and speed up SGD in turn, we would also like to adapt our updates to each individual parameter to perform larger or smaller updates depending on their importance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Adagrad", "weight": 1.0} -->

Adagrad is an algorithm for gradient-based optimization that does just this: It adapts the learning rate to the parameters, performing larger updates for infrequent and smaller updates for frequent parameters. For this reason, it is well-suited for dealing with sparse data. Dean et al. have found that Adagrad greatly improved the robustness of SGD and used it for training large-scale neural nets at Google, which -- among other things -- learned to recognize cats in Youtube videos^99^9 Moreover, Pennington et al. used Adagrad to train GloVe word embeddings, as infrequent words require much larger updates than frequent ones.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Adagrad", "weight": 1.0} -->

Previously, we performed an update for all parameters $\theta$ at once as every parameter $\theta_{i}$ used the same learning rate $\eta$. As Adagrad uses a different learning rate for every parameter $\theta_{i}$ at every time step $t$, we first show Adagrad's per-parameter update, which we then vectorize. For brevity, we set $g_{t,i}$ to be the gradient of the objective function w.r.t.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Adagrad", "weight": 1.0} -->

to the parameter $\theta_{i}$ at time step $t$: The SGD update for every parameter $\theta_{i}$ at each time step $t$ then becomes: In its update rule, Adagrad modifies the general learning rate $\eta$ at each time step $t$ for every parameter $\theta_{i}$ based on the past gradients that have been computed for $\theta_{i}$: $G_{t} \in {\mathbb{R}}^{d \times d}$ here is a diagonal matrix where each diagonal element $i,i$ is the sum of the squares of the gradients w.r.t. $\theta_{i}$ up to time step $t$^1010^10Duchi et al. give this matrix as an alternative to the *full* matrix containing the outer products of all previous gradients, as the computation of the matrix square root is infeasible even for a moderate number of parameters $d$., while $\epsilon$ is a smoothing term that avoids division by zero (usually on the order of ${1e} - 8$).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Adagrad", "weight": 1.0} -->

Interestingly, without the square root operation, the algorithm performs much worse.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Adagrad", "weight": 1.0} -->

As $G_{t}$ contains the sum of the squares of the past gradients w.r.t. to all parameters $\theta$ along its diagonal, we can now vectorize our implementation by performing an element-wise matrix-vector multiplication $\odot$ between $G_{t}$ and $g_{t}$: One of Adagrad's main benefits is that it eliminates the need to manually tune the learning rate. Most implementations use a default value of $0.01$ and leave it at that.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Adagrad", "weight": 1.0} -->

Adagrad's main weakness is its accumulation of the squared gradients in the denominator: Since every added term is positive, the accumulated sum keeps growing during training. This in turn causes the learning rate to shrink and eventually become infinitesimally small, at which point the algorithm is no longer able to acquire additional knowledge. The following algorithms aim to resolve this flaw.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Adadelta", "weight": 1.0} -->

Adadelta is an extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing learning rate. Instead of accumulating all past squared gradients, Adadelta restricts the window of accumulated past gradients to some fixed size $w$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Adadelta", "weight": 1.0} -->

Instead of inefficiently storing $w$ previous squared gradients, the sum of gradients is recursively defined as a decaying average of all past squared gradients. The running average $E{\lbrack g^{2}\rbrack}_{t}$ at time step $t$ then depends (as a fraction $\gamma$ similarly to the Momentum term) only on the previous average and the current gradient: We set $\gamma$ to a similar value as the momentum term, around $0.9$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Adadelta", "weight": 1.0} -->

For clarity, we now rewrite our vanilla SGD update in terms of the parameter update vector $\Delta\theta_{t}$: | | {\Delta\theta_{t}} & {= {- {\eta \cdot g_{t,i}}}} \\ | | | | | \theta_{t + 1} & {= {\theta_{t} + {\Delta\theta_{t}}}} | | | The parameter update vector of Adagrad that we derived previously thus takes the form: We now simply replace the diagonal matrix $G_{t}$ with the decaying average over past squared gradients $E{\lbrack g^{2}\rbrack}_{t}$: As the denominator is just the root mean squared (RMS) error criterion of the gradient, we can replace it with the criterion short-hand: The authors note that the units in this update (as well as in SGD, Momentum, or Adagrad) do not match, i.e. the update should have the same hypothetical units as the parameter.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Adadelta", "weight": 1.0} -->

To realize this, they first define another exponentially decaying average, this time not of squared gradients but of squared parameter updates: The root mean squared error of parameter updates is thus: Since $RMS{\lbrack{\Delta\theta}\rbrack}_{t}$ is unknown, we approximate it with the RMS of parameter updates until the previous time step.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Adadelta", "weight": 1.0} -->

Replacing the learning rate $\eta$ in the previous update rule with $RMS{\lbrack{\Delta\theta}\rbrack}_{t - 1}$ finally yields the Adadelta update rule: | | {\Delta\theta_{t}} & {= {- {\frac{RMS{\lbrack{\Delta\theta}\rbrack}_{t - 1}}{RMS{\lbrack g\rbrack}_{t}}g_{t}}}} \\ | | | | | \theta_{t + 1} & {= {\theta_{t} + {\Delta\theta_{t}}}} | | | With Adadelta, we do not even need to set a default learning rate, as it has been eliminated from the update rule.

<!-- chunk {"id": "body-0037", "role": "body", "section": "RMSprop", "weight": 1.0} -->

RMSprop is an unpublished, adaptive learning rate method proposed by Geoff Hinton in Lecture 6e of his Coursera Class^1111^11 RMSprop and Adadelta have both been developed independently around the same time stemming from the need to resolve Adagrad's radically diminishing learning rates. RMSprop in fact is identical to the first update vector of Adadelta that we derived above: | | \theta_{t + 1} & {= {\theta_{t} - {\frac{\eta}{\sqrt{{E{\lbrack g^{2}\rbrack}_{t}} + \epsilon}}g_{t}}}} | | | RMSprop as well divides the learning rate by an exponentially decaying average of squared gradients. Hinton suggests $\gamma$ to be set to $0.9$, while a good default value for the learning rate $\eta$ is $0.001$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Adam", "weight": 1.0} -->

Adaptive Moment Estimation (Adam) is another method that computes adaptive learning rates for each parameter. In addition to storing an exponentially decaying average of past squared gradients $v_{t}$ like Adadelta and RMSprop, Adam also keeps an exponentially decaying average of past gradients $m_{t}$, similar to momentum: $m_{t}$ and $v_{t}$ are estimates of the first moment (the mean) and the second moment (the uncentered variance) of the gradients respectively, hence the name of the method. As $m_{t}$ and $v_{t}$ are initialized as vectors of $0$'s, the authors of Adam observe that they are biased towards zero, especially during the initial time steps, and especially when the decay rates are small (i.e. $\beta_{1}$ and $\beta_{2}$ are close to $1$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Adam", "weight": 1.0} -->

They counteract these biases by computing bias-corrected first and second moment estimates: | | {\hat{m}}_{t} & {= \frac{m_{t}}{1 - \beta_{1}^{t}}} \\ | | | | | {\hat{v}}_{t} & {= \frac{v_{t}}{1 - \beta_{2}^{t}}} | | | They then use these to update the parameters just as we have seen in Adadelta and RMSprop, which yields the Adam update rule: The authors propose default values of $0.9$ for $\beta_{1}$, $0.999$ for $\beta_{2}$, and $10^{- 8}$ for $\epsilon$. They show empirically that Adam works well in practice and compares favorably to other adaptive learning-method algorithms.

<!-- chunk {"id": "body-0040", "role": "body", "section": "AdaMax", "weight": 1.0} -->

The $v_{t}$ factor in the Adam update rule scales the gradient inversely proportionally to the $\ell_{2}$ norm of the past gradients (via the $v_{t - 1}$ term) and current gradient ${|g_{t}|}^{2}$: We can generalize this update to the $\ell_{p}$ norm. Note that Kingma and Ba also parameterize $\beta_{2}$ as $\beta_{2}^{p}$: Norms for large $p$ values generally become numerically unstable, which is why $\ell_{1}$ and $\ell_{2}$ norms are most common in practice. However, $\ell_{\infty}$ also generally exhibits stable behavior. For this reason, the authors propose AdaMax and show that $v_{t}$ with $\ell_{\infty}$ converges to the following more stable value.

<!-- chunk {"id": "body-0041", "role": "body", "section": "AdaMax", "weight": 1.0} -->

To avoid confusion with Adam, we use $u_{t}$ to denote the infinity norm-constrained $v_{t}$: | | & {= {\max{({\beta_{2} \cdot v_{t - 1}},{|g_{t}|})}}} | | | We can now plug this into the Adam update equation by replacing $\sqrt{{\hat{v}}_{t}} + \epsilon$ with $u_{t}$ to obtain the AdaMax update rule: Note that as $u_{t}$ relies on the $\max$ operation, it is not as suggestible to bias towards zero as $m_{t}$ and $v_{t}$ in Adam, which is why we do not need to compute a bias correction for $u_{t}$. Good default values are again $\eta = 0.002$, $\beta_{1} = 0.9$, and $\beta_{2} = 0.999$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Nadam", "weight": 1.0} -->

As we have seen before, Adam can be viewed as a combination of RMSprop and momentum: RMSprop contributes the exponentially decaying average of past squared gradients $v_{t}$, while momentum accounts for the exponentially decaying average of past gradients $m_{t}$. We have also seen that Nesterov accelerated gradient (NAG) is superior to vanilla momentum.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nadam", "weight": 1.0} -->

Nadam (Nesterov-accelerated Adaptive Moment Estimation) thus combines Adam and NAG. In order to incorporate NAG into Adam, we need to modify its momentum term $m_{t}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nadam", "weight": 1.0} -->

First, let us recall the momentum update rule using our current notation: | | g_{t} & {= {{\nabla_{\theta_{t}}J}{(\theta_{t})}}} \\ | | | where $J$ is our objective function, $\gamma$ is the momentum decay term, and $\eta$ is our step size. Expanding the third equation above yields: This demonstrates again that momentum involves taking a step in the direction of the previous momentum vector and a step in the direction of the current gradient.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nadam", "weight": 1.0} -->

NAG then allows us to perform a more accurate step in the gradient direction by updating the parameters with the momentum step *before* computing the gradient.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nadam", "weight": 1.0} -->

We thus only need to modify the gradient $g_{t}$ to arrive at NAG: Dozat proposes to modify NAG the following way: Rather than applying the momentum step twice -- one time for updating the gradient $g_{t}$ and a second time for updating the parameters $\theta_{t + 1}$ -- we now apply the look-ahead momentum vector directly to update the current parameters: | | g_{t} & {= {{\nabla_{\theta_{t}}J}{(\theta_{t})}}} \\ | | | | | \theta_{t + 1} & {= {\theta_{t} - {({{\gammam_{t}} + {\etag_{t}}})}}} | | | Notice that rather than utilizing the previous momentum vector $m_{t - 1}$ as in Equation 27, we now use the current momentum vector $m_{t}$ to look ahead. In order to add Nesterov momentum to Adam, we can thus similarly replace the previous momentum vector with the current momentum vector.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Nadam", "weight": 1.0} -->

We can thus replace it with ${\hat{m}}_{t - 1}$: This equation looks very similar to our expanded momentum term in Equation 27.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Visualization of algorithms", "weight": 1.0} -->

The following two figures provide some intuitions towards the optimization behaviour of the presented optimization algorithms.^1212^12Also have a look at for a description of the same images by Karpathy and another concise overview of the algorithms discussed.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Visualization of algorithms", "weight": 1.0} -->

In Figure 4(a), we see the path they took on the contours of a loss surface (the Beale function). All started at the same point and took different paths to reach the minimum. Note that Adagrad, Adadelta, and RMSprop headed off immediately in the right direction and converged similarly fast, while Momentum and NAG were led off-track, evoking the image of a ball rolling down the hill. NAG, however, was able to correct its course sooner due to its increased responsiveness by looking ahead and headed to the minimum.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Visualization of algorithms", "weight": 1.0} -->

(a) SGD optimization on loss surface contours (b) SGD optimization on saddle point Figure 4: Source and full animations: Alec Radford As we can see, the adaptive learning-rate methods, i.e. Adagrad, Adadelta, RMSprop, and Adam are most suitable and provide the best convergence for these scenarios.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Which optimizer to use?", "weight": 1.0} -->

So, which optimizer should you use? If your input data is sparse, then you likely achieve the best results using one of the adaptive learning-rate methods. An additional benefit is that you will not need to tune the learning rate but will likely achieve the best results with the default value.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Which optimizer to use?", "weight": 1.0} -->

In summary, RMSprop is an extension of Adagrad that deals with its radically diminishing learning rates. It is identical to Adadelta, except that Adadelta uses the RMS of parameter updates in the numerator update rule. Adam, finally, adds bias-correction and momentum to RMSprop. Insofar, RMSprop, Adadelta, and Adam are very similar algorithms that do well in similar circumstances. Kingma et al. show that its bias-correction helps Adam slightly outperform RMSprop towards the end of optimization as gradients become sparser. Insofar, Adam might be the best overall choice.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Which optimizer to use?", "weight": 1.0} -->

Interestingly, many recent papers use vanilla SGD without momentum and a simple learning rate annealing schedule. As has been shown, SGD usually achieves to find a minimum, but it might take significantly longer than with some of the optimizers, is much more reliant on a robust initialization and annealing schedule, and may get stuck in saddle points rather than local minima. Consequently, if you care about fast convergence and train a deep or complex neural network, you should choose one of the adaptive learning rate methods.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Parallelizing and distributing SGD", "weight": 1.0} -->

Given the ubiquity of large-scale data solutions and the availability of low-commodity clusters, distributing SGD to speed it up further is an obvious choice. SGD by itself is inherently sequential: Step-by-step, we progress further towards the minimum. Running it provides good convergence but can be slow particularly on large datasets. In contrast, running SGD asynchronously is faster, but suboptimal communication between workers can lead to poor convergence. Additionally, we can also parallelize SGD on one machine without the need for a large computing cluster. The following are algorithms and architectures that have been proposed to optimize parallelized and distributed SGD.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Hogwild!", "weight": 1.0} -->

Niu et al. introduce an update scheme called Hogwild! that allows performing SGD updates in parallel on CPUs. Processors are allowed to access shared memory without locking the parameters. This only works if the input data is sparse, as each update will only modify a fraction of all parameters. They show that in this case, the update scheme achieves almost an optimal rate of convergence, as it is unlikely that processors will overwrite useful information.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Downpour SGD", "weight": 1.0} -->

Downpour SGD is an asynchronous variant of SGD that was used by Dean et al. in their DistBelief framework (the predecessor to TensorFlow) at Google. It runs multiple replicas of a model in parallel on subsets of the training data. These models send their updates to a parameter server, which is split across many machines. Each machine is responsible for storing and updating a fraction of the model's parameters. However, as replicas don't communicate with each other e.g. by sharing weights or updates, their parameters are continuously at risk of diverging, hindering convergence.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Delay-tolerant Algorithms for SGD", "weight": 1.0} -->

McMahan and Streeter extend AdaGrad to the parallel setting by developing delay-tolerant algorithms that not only adapt to past gradients, but also to the update delays. This has been shown to work well in practice.

<!-- chunk {"id": "body-0058", "role": "body", "section": "TensorFlow", "weight": 1.0} -->

TensorFlow^1313^13 is Google's recently open-sourced framework for the implementation and deployment of large-scale machine learning models. It is based on their experience with DistBelief and is already used internally to perform computations on a large range of mobile devices as well as on large-scale distributed systems. The distributed version, which was released in April 2016 ^1414^14 relies on a computation graph that is split into a subgraph for every device, while communication takes place using Send/Receive node pairs.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Elastic Averaging SGD", "weight": 1.0} -->

Zhang et al. propose Elastic Averaging SGD (EASGD), which links the parameters of the workers of asynchronous SGD with an elastic force, i.e. a center variable stored by the parameter server. This allows the local variables to fluctuate further from the center variable, which in theory allows for more exploration of the parameter space. They show empirically that this increased capacity for exploration leads to improved performance by finding new local optima.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Additional strategies for optimizing SGD", "weight": 1.0} -->

Finally, we introduce additional strategies that can be used alongside any of the previously mentioned algorithms to further improve the performance of SGD. For a great overview of some other common tricks, refer to.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Shuffling and Curriculum Learning", "weight": 1.0} -->

Generally, we want to avoid providing the training examples in a meaningful order to our model as this may bias the optimization algorithm. Consequently, it is often a good idea to shuffle the training data after every epoch.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Shuffling and Curriculum Learning", "weight": 1.0} -->

On the other hand, for some cases where we aim to solve progressively harder problems, supplying the training examples in a meaningful order may actually lead to improved performance and better convergence. The method for establishing this meaningful order is called Curriculum Learning.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Shuffling and Curriculum Learning", "weight": 1.0} -->

Zaremba and Sutskever were only able to train LSTMs to evaluate simple programs using Curriculum Learning and show that a combined or mixed strategy is better than the naive one, which sorts examples by increasing difficulty.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Batch normalization", "weight": 1.0} -->

To facilitate learning, we typically normalize the initial values of our parameters by initializing them with zero mean and unit variance. As training progresses and we update parameters to different extents, we lose this normalization, which slows down training and amplifies changes as the network becomes deeper.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Batch normalization", "weight": 1.0} -->

Batch normalization reestablishes these normalizations for every mini-batch and changes are back-propagated through the operation as well. By making normalization part of the model architecture, we are able to use higher learning rates and pay less attention to the initialization parameters. Batch normalization additionally acts as a regularizer, reducing (and sometimes even eliminating) the need for Dropout.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Early stopping", "weight": 1.0} -->

According to Geoff Hinton: "Early stopping (is) beautiful free lunch"^1515^15NIPS 2015 Tutorial slides, slide 63, You should thus always monitor error on a validation set during training and stop (with some patience) if your validation error does not improve enough.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Gradient noise", "weight": 1.0} -->

Neelakantan et al. add noise that follows a Gaussian distribution $N{(0,\sigma_{t}^{2})}$ to each gradient update: They anneal the variance according to the following schedule: They show that adding this noise makes networks more robust to poor initialization and helps training particularly deep and complex networks. They suspect that the added noise gives the model more chances to escape and find new local minima, which are more frequent for deeper models.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this article, we have initially looked at the three variants of gradient descent, among which mini-batch gradient descent is the most popular. We have then investigated algorithms that are most commonly used for optimizing SGD: Momentum, Nesterov accelerated gradient, Adagrad, Adadelta, RMSprop, Adam, AdaMax, Nadam, as well as different algorithms to optimize asynchronous SGD. Finally, we've considered other strategies to improve SGD such as shuffling and curriculum learning, batch normalization, and early stopping.
