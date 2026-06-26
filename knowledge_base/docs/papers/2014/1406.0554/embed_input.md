<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Universal Convexification via Risk-Aversion

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop a framework for convexifying a fairly general class of optimization problems. Under additional assumptions, we analyze the suboptimality of the solution to the convexified problem relative to the original nonconvex problem and prove additive approximation guarantees. We then develop algorithms based on stochastic gradient methods to solve the resulting optimization problems and show bounds on convergence rates. %We show a simple application of this framework to supervised learning, where one can perform integration explicitly and can use standard (non-stochastic) optimization algorithms with better convergence guarantees. We then extend this framework to apply to a general class of discrete-time dynamical systems. In this context, our convexification approach falls under the well-studied paradigm of risk-sensitive Markov Decision Processes. We derive the first known model-based and model-free policy gradient optimization algorithms with guaranteed convergence to the optimal solution. Finally, we present numerical results validating our formulation in different applications.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

It has been said that the "the great watershed in optimization isn't between linearity and nonlinearity, but convexity and nonconvexity". In this paper, we describe a framework for convexifying a fairly general class of optimization problems (section 3), turning them into problems that can be solved with efficient convergence guarantees. The convexification approach may change the problem drastically in some cases, which is not surprising since most nonconvex optimization problems are NP-hard and cannot be reduced to solving convex optimization problems. However, under additional assumptions, we can make guarantees that bound the suboptimality of the solution found by solving the convex surrogate relative to the optimum of the original nonconvex problem (section 3.2). We adapt stochastic gradient methods to solve the resulting problems (section 4) and prove convergence guarantees that bound the distance to optimality as a function of the number of iterations. In section 5, we extend the framework to arbitrary dynamical systems and derive the first known (to the best of our knowledge) policy optimization approach with guaranteed convergence to the global optimum.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The control problems we study fall under the classical framework of risk-sensitive control and the condition required for convexity is a natural one relating the control cost, risk factor and noise covariance. It is very similar to the condition used in path integral control and subsequent iterative algorithms (the ${PI}^{2}$ algorithm ). In section 6, we present numerical results illustrating the applications of our framework to various problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "GENERAL OPTIMIZATION PROBLEMS", "weight": 1.0} -->

We study optimization problems of the form: where $g$ is an arbitrary function and $\mathcal{C} \subset \mathbf{R}^{k}$ is a convex set. We do not assume that $g$ is convex so the above problem could be a nonconvex optimization problem. In this work, we convexify this problem by decomposing $g(\theta)$ as follows: ${g{(\theta)}} = {{f{(\theta)}} + {\frac{1}{2}\theta^{T}R\theta}}$ and perturbing $f$ with Gaussian noise. Optimization problems of this form are very common in machine learning (where $R$ corresponds to a regularizer) and control (where $R$ corresponds to a control cost). The convexified optimization problem is: where $R \succeq 0$ and This kind of objective is common in risk-averse optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "GENERAL OPTIMIZATION PROBLEMS", "weight": 1.0} -->

To a first order Taylor expansion in $\alpha$, the above objective is equal to ${E\left\lbrack {f\left({\theta + \omega} \right)} \right\rbrack} + {\alpha{\operatorname{Var}\left({f\left({\theta + \omega} \right)} \right)}}$, indicating that increasing $\alpha$ will make the solution more robust to Gaussian perturbations. $\alpha$ is called the risk-factor and is a measure of the risk-aversion of the decision maker. Larger values of $\alpha$ will reject solutions that are not robust to Gaussian perturbations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "GENERAL OPTIMIZATION PROBLEMS", "weight": 1.0} -->

In order that the expectation exists, we require that $f$ is bounded above: We implicitly make this assumption throughout this paper in all the stated results. Note that this is not a very restrictive assumption, since, given any function $g$ with a finite minimum, one can define a new objective $g' = {\min\left(g,\overline{m} \right)}$, where $\overline{m}$ is an upper bound on the minimum (say the value of the function at some point), without changing the minimum. Since the convex quadratic is non-negative, $f$ is also bounded above by $\overline{m}$ and hence $0 < {\exp\left({\alphaf\left({\theta + \omega} \right)} \right)} \leq {\exp\left({\alpha\overline{m}} \right)}$. This ensures that $f_{\alpha}(\theta)$ is finite.

<!-- chunk {"id": "body-0008", "role": "body", "section": "GENERAL OPTIMIZATION PROBLEMS", "weight": 1.0} -->

Some results will require differentiability, and we can preserve this by defining $g'$ using a soft-min: For example, ${g'(x)} = {\overline{m}{\tanh\left(\frac{g(x)}{\overline{m}} \right)}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTERPRETATION", "weight": 1.0} -->

Theorem 3.1. ‣ 3 GENERAL OPTIMIZATION PROBLEMS ‣ Universal Convexification via Risk-Aversion") is a surprising result, since the condition for convexity does not depend in any way on the properties of $f$ (except for the bounded growth assumption ), but only on the relationship between the quadratic objective $R$, the risk factor $\alpha$ and the noise level $\Sigma$. In this section, we give some intuition behind the result and describe why it is plausible that this is true.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTERPRETATION", "weight": 1.0} -->

In general, arbitrary nonconvex optimization problems can be very challenging to solve. As a worst case example, consider a convex quadratic function ${g{(x)}} = x^{2}$ that is perturbed slightly: At some point where the function value is very large (say $x = 100$), we modify the function so that it suddenly drops to a large negative value (lower than the global minimum 0 of the convex quadratic). By doing this perturbation over a small finite interval, one can preserve differentiability while introducing a new global minimum far away from the original global minimum. In this way, one can create difficult optimization problems that cannot be solved using gradient descent methods, unless initialized very carefully.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTERPRETATION", "weight": 1.0} -->

The work we present here does not solve this problem: In fact, it will not find a global minimum of the form created above. The risk-aversion introduced destroys this minimum, since small perturbations cause the function to increase rapidly, ie, ${g\left( {\theta^{\ast} + \omega} \right)} \gg {g\left( \theta^{\ast} \right)}$, so that the objective becomes large. Instead, it will find a "robust" minimum, in the sense that Gaussian perturbations around the minimum do not increase the value of the objective by much. This intuition is formalized by theorem 3.2. ‣ Definition 1 (Sensitivity Function). ‣ 3.2 ANALYSIS OF SUB-OPTIMALITY ‣ 3 GENERAL OPTIMIZATION PROBLEMS ‣ Universal Convexification via Risk-Aversion"), which bounds the suboptimality of the convexified solution relative to the optimal solution of the original problem in terms of the sensitivity of $f$ to Gaussian perturbations around the optimum.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTERPRETATION", "weight": 1.0} -->

In figure 1, we illustrate the effect of the convexification for a 1-dimensional optimization problem. The blue curve represents the original function $g(\theta)$. It has 4-local minima in the interval $({- 3},3)$. Two of the shallow minima are eliminated by smoothing with Gaussian noise to get $\overline{g}(\theta)$. However, there is a deep but narrow local minimum that remains even after smoothing. Making the problem convex using risk-aversion and theorem 3.1. ‣ 3 GENERAL OPTIMIZATION PROBLEMS ‣ Universal Convexification via Risk-Aversion") leads to the green curve that only preserves the robust minimum as the unique global optimum.

<!-- chunk {"id": "body-0013", "role": "body", "section": "ANALYSIS OF SUB-OPTIMALITY", "weight": 1.0} -->

We have derived a convex surrogate for a very general class of optimization problems. However, it is possible that the solution to the convexified problem is drastically different from that of the original problem and the convex surrogate we propose is a poor approximation. Given the hardness of general non-convex optimization, we do not expect the two problems to have close solutions without additional assumptions. In this section, we analyze the gap between the original and convexified problem, that is, we answer the question: Can we construct a reasonable approximation to the original (potentially nonconvex) problem based on the solution to the perturbed convex problem? In order to answer this, we first define the sensitivity function, which quantifies the gap between and.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Although we only prove suboptimality relative to the optimal solution of a smoothed version of $g$, we can extend the analysis to the optimal solution of $g$ itself. Define $\theta^{\ast} = {{\operatorname{\mathsf{a}\mathsf{r}\mathsf{g}\mathsf{m}\mathsf{i}\mathsf{n}}_{\theta \in \mathcal{C}}g}(\theta)}$. We can prove that Assuming that $g$ changes slowly around $\theta^{\ast}$ and $\theta_{\alpha}^{\ast}$ (indicative of the fact that $\theta^{\ast}$ is a "robust" minimum and $\theta_{\alpha}^{\ast}$ is the minimum of a robustified problem), we can bound the first term. We leave a precise analysis for future work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "BOUNDING THE SENSITIVITY FUNCTION", "weight": 1.0} -->

The sensitivity function is exactly the moment generating function of the $0$-mean random variable ${\overset{\sim}{f}}_{\omega}(\theta)$. Several techniques have been developed for bounding moment generation functions in the field of concentration inequalities. Using these techniques, we can bound the moment generating function (i.e. the sensitivity function) under the assumption that $f$ is Lipschitz-continuous.

<!-- chunk {"id": "body-0016", "role": "body", "section": "ALGORITHMS AND CONVERGENCE GUARANTEES", "weight": 1.0} -->

In general, the expectations involved in cannot be computed analytically. Thus, we need to resort to sampling based approaches in order to solve these problems. This has been studied extensively in recent years in the context of machine learning, where stochastic gradient methods and variants have been shown to be efficient, particularly in the context training machine learning algorithms with huge amounts of data. We now describe stochastic gradient methods for solving and adapt the convergence guarantees of stochastic gradient methods to our setting.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stochastic Gradient Methods with Convergence Guarantees", "weight": 1.0} -->

In this section, we will derive gradients of the convex objective function. We will assume that the function $f$ is differentiable at all $\theta \in \mathbf{R}^{k}$. In order to get unbiased gradient estimates, we exponentiate the objective to get: Since $f(\theta)$ is differentiable for all $\theta$, so is $\exp\left({{\alphaf\left({\theta + \omega} \right)} + {\frac{1}{2}\theta^{T}\left({\alphaR} \right)\theta}} \right)$. Further, suppose that exists and is finite for each $\theta$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stochastic Gradient Methods with Convergence Guarantees", "weight": 1.0} -->

Then, if we differentiate $\mathbf{G}(\theta)$ with respect to $\theta$, we can interchange the expectation and differentiation to get Thus, we can sample $\omega \sim {\mathcal{N}(0,\Sigma)}$ and get an unbiased estimate of the gradient which we denote by $\hat{\nabla}\mathbf{G}(\theta,\omega)$. As in standard stochastic gradient methods, one saves on the complexity of a single iteration by using a single (or a small number of) samples to get a gradient estimate while still converging to the global optimum with high probability and in expectation, because over multiple iterations one moves along the negative gradient "on average".

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The convergence guarantees are in terms of the exponentiated objective $\mathbf{G}(\theta)$. We can convert these into bounds on $\log\left({\mathbf{G}(\theta)} \right)$ as follows: where the first inequality follows from concavity of the $\log$ function. Subtracting $\log\left(\mathbf{G}^{\ast} \right)$, we get

<!-- chunk {"id": "body-0020", "role": "body", "section": "CONTROL PROBLEMS", "weight": 1.0} -->

In this section, we extend the above approach to the control of discrete-time dynamical systems. Stochastic optimal control of nonlinear systems in general is a hard problem and the only known general approach is based on dynamic programming, which scales exponentially with the dimension of the state space. Algorithms that approximate the solution of the dynamic program directly (approximate dynamic programming) have been successful in various domains, but scaling these approaches to high dimensional continuous state control problems has been challenging. In this section, we pursue the alternate approach of policy search or policy gradient methods. These algorithms have the advantage that they are directly optimizing the performance of a control policy as opposed to a surrogate measure like the error in the solution to the Bellman equation. They have been used successfully for various applications and are closely related to path integral control. However, in all of these approaches, there were no guarantees made regarding the optimality of the policy that the algorithm converges to (even in the limit of infinite sampling) or the rate of convergence.

<!-- chunk {"id": "body-0021", "role": "body", "section": "CONTROL PROBLEMS", "weight": 1.0} -->

In this work, we develop the *first* policy gradient algorithms that achieve the *globally* optimal solutions to a class of *risk-averse* policy optimization problems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

In this section, we will use boldface to denote quantities stacked over time (like $\mathbf{\epsilon}$). Equation can model any noisy discrete-time dynamical system, since $\mathcal{F}$ can be any function of the current state, control input and external disturbance (noise). However, we require that all the control dimensions are affected by Gaussian noise as. This can be thought of either as real actuator noise or artificial exploration noise. The choice of zero initial state $x_{1} = 0$ is arbitrary - our results even extend to an arbitrary distribution over the initial state.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We will work with costs that are a combination of arbitrary state costs and quadratic control costs: where $\ell_{t}\left(x_{t} \right)$ is the stage-wise state cost at time $t$. $\ell_{t}$ can be any bounded function of the state-vector $x_{t}$. Further, we will assume that the control-noise is non-degenerate, that is $\Sigma_{t}$ is full rank for all $0 \leq t \leq {N - 1}$. We denote $S_{t} = \Sigma_{t}^{- 1}$. We seek to design feedback policies to minimize the accumulated cost. We will assume that the features $\phi$ are fixed and we seek to optimize the policy parameters $\mathbf{K} = {\{ K_{t}:{t = {1,2,\ldots,{N - 1}}}\}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The stochastic optimal control problem we consider is defined as follows: This is exactly the same as the formulation in Risk Sensitive Markov Decision Processes, the only change being that we have explicitly separated the noise appearing in the controls from the noise in the dynamical system overall. In this formulation, the objective depends not only on the average behavior of the control policy but also on variance and higher moments (the tails of the distribution of costs). This has been studied for linear systems under the name of LEQG control. $\alpha$ is called the risk factor: Large positive values of $\alpha$ result in strongly risk-averse policies while large negative values result in risk-seeking policies. In our formulation, we will need a certain minimum degree of risk-aversion for the resulting policy optimization problem to be convex.

<!-- chunk {"id": "body-0025", "role": "body", "section": "NUMERICAL RESULTS", "weight": 1.0} -->

In this section, we present preliminary numerical results illustrating applications of the framework to various problems with comparisons to a simple baseline approach. These are not meant to be thorough numerical comparisons but simple illustrations of the power and applications of our framework.

<!-- chunk {"id": "body-0026", "role": "body", "section": "BINARY CLASSIFICATION", "weight": 1.0} -->

We look at a problem of binary classification. Let $y$ denote the actual label and $\hat{y}$ denote the predicted label. We use the loss function This is a non-convex loss function (the logarithm of the standard $0$-$1$ loss). We convexify this in the prediction $\hat{y}$ using our approach: Plugging in $\hat{y} = {\theta^{T}x}$ where $x$ is the feature vector, we get Plugging in the expression for $\ell$ gives where $erfc$ is the Gaussian error function. Given a dataset $\{\left(x_{i},y_{u} \right)\}$, we can form the empirical risk-minimization problem with this convexified objective: We can drop the $\alpha$ since it only scales the objective (this is a consequence of the fact that $\exp(\ell)$ is 0-1 valued and does not change on raising it to a positive power).

<!-- chunk {"id": "body-0027", "role": "body", "section": "BINARY CLASSIFICATION", "weight": 1.0} -->

Thus, we finally end up with The first term is a data-fit term (a smoothed version of the 0-1 loss) and the second term is a regularizer. although we penalize the prediction $\theta^{T}x$ rather than $\theta$ itself. If $x$ are normalized and span all directions, by summing over the entire dataset we get something close to the standard Tikhonov regularization.

<!-- chunk {"id": "body-0028", "role": "body", "section": "BINARY CLASSIFICATION", "weight": 1.0} -->

We compare the performance of our convexification-based approach with a standard implementation of a Support Vector Machine (SVM). We use the breast cancer dataset. We compare the two algorithms on various train-test splits of the dataset (without using cross-validation or parameter tuning). For each split, we create a noisy version of the dataset by adding Gaussian noise to the labels and truncating to $+ 1/ - 1$:${{\hat{y}}^{i} = {{sign}\left( {y^{i} + \omega} \right)}},{\omega \sim {\mathcal{N}\left( 0,\sigma^{2} \right)}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "BINARY CLASSIFICATION", "weight": 1.0} -->

The accuracy of the learned classifiers on withheld test-data, averaged over $50$ random train-test splits with label corruption as described above, are plotted as function of the noise level $\sigma$ in figure 1. This is not a completely fair comparison since our approach explicitly optimizes for the worst case under Gaussian perturbations to the prediction (which can also be seen as a Gaussian perturbation to the label). However, as mentioned earlier, the purpose of these numerical experiments is to illustrate the applicability of our convexification approach to various problems so we do not do a careful comparison to robust variants of SVMs, which would be better suited to the setting described here.

<!-- chunk {"id": "body-0030", "role": "body", "section": "CLASSIFICATION WITH NEURAL NETWORKS", "weight": 1.0} -->

We present an algorithm that does neural network training using the results of section 5. Each layer of the neural network is a time-step in a dynamical system, and the neural network weights correspond to the time-varying policy parameters. Let $h$ denote a component-wise nonlinearity applied to its vector-input (a transfer function). The deterministic dynamics is where $x_{t}$ is the vector of activations at the $t$-th layer, $K_{t}$ is the weight matrix and $x$ is the input to the neural network. The output is $x_{N}$, where $N$ is the number of layers in the network. The cost function is simply the loss function between the output of the neural network $x_{N}$ and a desired output $y$: $\ell\left(y,x_{N} \right)$. To put this into our framework, we add noise to the input of the transfer function at each layer: Additionally, we define the objective to be where the expectation is with respect to the Gaussian noise added at each layer in the network.

<!-- chunk {"id": "body-0031", "role": "body", "section": "CLASSIFICATION WITH NEURAL NETWORKS", "weight": 1.0} -->

Note that the above objective is a function of $\mathbf{K},x,y$. The quadratic penalty on $K_{t}x_{t}$ can again be thought of as a particular type of regularization which encourages learning networks with small internal activations. We add this objective over the entire dataset $\{ x^{i},y^{i}\}$ to get our overall training objective.

<!-- chunk {"id": "body-0032", "role": "body", "section": "CLASSIFICATION WITH NEURAL NETWORKS", "weight": 1.0} -->

We evaluate this approach on a small randomly selected subset of the MNIST dataset. We use the version available at along with the MATLAB code provided for training neural networks. We use a 2-layer neural network with 20 units in the hidden layer and tanh-transfer functions in both layers. We use a randomly chosen collection of 900 data points for training and another 100 data points for validation. We compare training using our approach with simple backprop based training. Both of the approaches use a stochastic gradient - in our approach the stochasticity is both in selection of the data point $i$ and the realization of the Gaussian noise $\omega$ while in standard backprop the stochasticity is only in the selection of $i$. We plot learning curves (in terms of generalization or test error) for both approaches, as a function of the number of neural network evaluations (forward+back prop) performed by the algorithm in figure 3(a). The nonconvex approach based on standard backprop-gradient descent gets stuck in a local minimum and does not improve test accuracy much. On the other hand, the convexified approach is able to learn a classifier that generalizes better.

<!-- chunk {"id": "body-0033", "role": "body", "section": "CLASSIFICATION WITH NEURAL NETWORKS", "weight": 1.0} -->

We also compared backprop with training a neural network on a 1-dimensional regression problem where the red curve represents the original function with data-points indicated by squares, the blue curve the reconstruction learned by our convexified training approach and the black curve the reconstruction obtained by using backprop (figure 3(b)). Again, backprop gets stuck in a bad local minimum while our approach is able to find a fairly accurate reconstruction.

<!-- chunk {"id": "body-0034", "role": "body", "section": "CONCLUSION AND FUTURE WORK", "weight": 1.5} -->

We have developed a general framework for convexifying a broad class of optimization problems, analysis that relates the solution of the convexified problem to the original one and given algorithms with convergence rate guarantees to solve the convexified problems. Extending the framework to dynamical systems, we derive the first approach to policy optimization with optimality and convergence rate guarantees. We validated our approach numerically on problems of binary classification and training neural networks. In future work, we will refine the suboptimality analysis for our convexification approach. Algorithmically, stochastic gradient methods could be slow if the variance in the gradient estimates is high, which is the case when using the exponentiated objective (as in section 4). We will study the applicability of recent work on using better sampling algorithms with stochastic gradient to our convexified problems.
