## Introduction

Optimization provides a framework for solving problems described in a tractable mathematical manner. Optimization-based methods have been successfully applied across a broad range of applications involving decision making, ranging from electrical engineering to control and finance. The conventional approach to carry out decision making involves the introduction of mathematical models for the problem and the solver based on domain knowledge. Such model-based methods form the basis for many classical and fundamental optimization techniques. Many of these classical approaches rely on simplified descriptions of the problem that make decision making tractable, computationally feasible, and interpretable. While model-methods often work well, their simplified approximations can limit performance in some applications.

The unprecedented success of machine learning (ML), and particularly of deep learning, in areas such as computer vision and natural language processing gave rise to methodology geared towards data. It is becoming common practice to replace principled task-specific decision mappings with abstract purely data-driven pipelines, trained with massive data sets. Deep neural networks are trained end-to-end, often in a supervised manner, without relying on analytical approximations, and therefore, they can operate in scenarios where analytical models are unknown or highly complex. However, the abstractness and extreme parameterization of DNNs results in them often being treated as black-boxes; understanding how their predictions are obtained and how reliable they are tends to be quite challenging, and thus deep learning lacks the interpretability, flexibility, versatility, and reliability of model-based techniques.

Due to the limitations of model-based methods and data-driven pipelines, recent years have witnessed growing interest in decision mappings involving both principled mathematical optimization and data-centric deep learning. These include frameworks such as deep unfolding and learned optimization, as well as task-specific techniques augmenting optimizers with DNNs. While hybrid model-based deep learning methods are often designed and studied for specific tasks, their underlying methodology is relevant to a broad range of applications, motivating the systematic characterization of the interplay between existing approaches.

In this article we introduce a general framework for model-based deep learning schemes. While classic optimization and deep learning are typically considered to be distinct disciplines, we view them as edges of a continuum varying in specificity and parameterization. We build upon this characterization to provide a tutorial-style presentation of the main methodologies which lie in the middle ground of this spectrum, and combine model-based optimization with ML as a form of model-based deep learning. Our presentation is exemplified with running examples from super-resolution imaging and stochastic control.

We begin by providing a unified characterization for decision making algorithms, focusing on the main pillars of their design, which we identify as the decision rule type, the decision rule objective, and the evaluation procedure. Then, we show how classical model-based optimization as well as data-centric deep learning are obtained as special instances of this unified characterization. We identify the components dictating the distinction between the methodologies in the formulated objectives, the corresponding decision rule types, and their associated parameters. We next present a spectrum of decision making approaches which vary in specificity and parameterization, with model-based optimization and deep learning constituting its edges, and provide a systematic categorization of model-based deep learning techniques into concrete strategies positioned along this continuous spectrum. The proposed categorization captures the interplay between the different techniques and their pros and cons in comparison with both model-based optimization and conventional deep learning. We present extensive experimental results applying model-based deep learning methodologies in various application areas, including ultrasound image processing, microscopy imaging, digital communications, and tracking of dynamic systems. The results demonstrate the gains in performance and run-time of combining model-based optimization with deep learning over favouring one discipline over the other.

## Decision Making

We consider a generic setup where the goal is to design a decision rule $f:{\mathcal{X}\mapsto\mathcal{S}}$. The decision rule maps the context $x \in \mathcal{X}$, i.e., the available observations, into a decision $s \in \mathcal{S}$.

Examples: This generic formulation encompasses a multitude of settings involving classification, prediction, control, and many more. It thus corresponds to a broad range of applications. The task dictates the context space $\mathcal{X}$ and the possible decisions $\mathcal{S}$. A partial list of such applications includes:

Signal processing - The context $x$ includes samples from an observed signal or an image, which is mapped by $f$ into another signal (e.g., for denoising) or into some form of inference (e.g., anomaly detection).

Communications - The decision rule represents the operation of a digital receiver, which decodes the channel output $x$ into an estimate of the transmitted message $s$.

Vehicular control - The decision rule $f$ is the control algorithm. The context $x$ can include the traditional state variables, i.e., the vehicle sensory data, and commands. The decision $s$ is the control action.

Finance - The decision rule is the trading algorithm. The context $x$ includes quantities such as financial forecasts and current positions. The decision $s$ is the trade list, i.e., the list of assets to buy and to sell.

Figure 1: Super-resolution recovery illustration.

Figure 2: Stochastic control illustration.

To keep the presentation focused, we repeatedly use two concrete running examples:

### Example 1 (Super-Resolution)

Here, $s$ is a high-resolution image, while $x$ is a distorted low-resolution version of the image. Thus, $\mathcal{X}$ and $\mathcal{S}$ are the spaces of low-resolution and high-resolution images, respectively. Such decision rules, typically referred to as recovery methods, aim at reconstructing $s^{true}$ from its distorted version $x$, as illustrated in Fig. 1.

### Example 2 (Stochastic Control)

In our second example, we consider a dynamic system, where the decision rule is a control policy. At each time period $t$, the goal is to map the noisy state observations $x_{t}$, where $\mathcal{X}$ is the space of possible sensory measurements, into an action $s_{t}$ within an action space $\mathcal{S}$. The system is characterized by a latent state vector $z_{t}$ that evolves in a random fashion which is related to the previous state $z_{t - 1}$ and action $s_{t - 1}$, while being partially observable via the noisy $x_{t}$. This setup is illustrated in Fig. 2.

### II-A Decision Rule Types

The above generic formulation allows the decision rule $f$ to be any mapping from $\mathcal{X}$ into $\mathcal{S}$. In practice, decision rules are often carried out using a structured form. Some common types of decision rules are:

An affine rule, i.e., $s = {{Wx} + b}$ for some $(W,b)$.

A decision tree chooses $s$ from a finite set of possible decisions $\{ s_{k}\}$ by examining a set of nested conditions $\{{cond}_{k}\}$, e.g., if ${cond}_{1}{(x)}$ then $s = s_{1}$; else inspect ${cond}_{2}{(x)}$, and so on.

An optimization-based decision rule chooses $s$ as a solution or approximate solution of an optimization problem parametrized by the context $x$, i.e., ${\arg{\min_{s \in \mathcal{S}}\mathcal{L}}}{(s;x)}$, where $\mathcal{L}$ is an objective function.

An iterative algorithm finds its decision by executing a sequence of mappings $h_{k}:{{\mathcal{S} \times \mathcal{X}}\mapsto\mathcal{S}}$, repeating $s_{k + 1} = {h_{k}\left( s_{k};x \right)}$ from an initial guess $s_{0}$ until convergence, or a fixed number of steps $K$, i.e., $s = {h_{K}\left( {h_{K - 1}\left( {\cdotsh_{1}{(s_{0};x)}};x \right)};x \right)}$.

A neural network is a special case of an iterative algorithm, where ${h_{k}{(z)}} = {\sigma\left( {{W_{k}z} + b_{k}} \right)}$ with $\sigma{( \cdot )}$ being an activation function and $(W_{k},b_{k})$ are parameters of the affine transformation. These mappings are referred to as layers. We have $s = {h_{K}\left( {h_{K - 1}\left( {\cdotsh_{1}{(x)}} \right)} \right)}$.

The boundaries between decision rule types are not always clear, and there is some overlap between the categories. For instance, an optimization-based decision rule with quadratic objective, where the context affects only the linear term in the objective, can be explicitly expressed as an affine decision rule. As another example, iterative decision rules often arise as iterations that solve an optimization problem. Moreover, an iterative algorithm with $K$ iterations can often be viewed as a neural network, as we further elaborate on in the sequel.

Each of these decision rule types include parameters. For example in an affine decision rule, the parameters are $W$ and $b$; in a decision tree, it is the values $s_{k}$ and parameters that specify the conditions. In an iterative algorithm the parameters are those appearing in the functions $h_{k}$; and in a neural network, the parameters are $W_{k}$ and $b_{k}$. In some cases the number of parameters is small, such as decision trees with a small number of conditions. In other cases, e.g., when $f$ is a DNN, decision rules can involve a massive number of parameters. These parameters capture the different mappings one can represent as decision rules.

For a decision rule type, we let $\mathcal{F}$ denote the set of possible decision rules, over all choices of parameters. In general, the more parameters there are, the broader the family of mappings captured by $\mathcal{F}$, which in turn results in the decision rule capable of accommodating more diverse and generic functions. Decision rules with fewer parameters are typically more specific, capturing a limited family of mappings. Let $\Theta$ denote the parameter space for a decision rule family $\mathcal{F}$, such that for each $\theta \in \Theta$, $f{( \cdot;\theta)}$ is a mapping in $\mathcal{F}$. We refer to the choosing of the decision rule parameters $\theta$ as tuning. In principle, tuning can be carried out based on understanding and modeling of the task. In practice, tuning typically involves simulation with either synthetic or real data; this procedure can be done manually when there are a few parameters, or by an automated algorithm for decision rules involving many parameters. In the latter case, tuning is also referred to as training or learning.

### II-B Evaluating a Decision Rule

The evaluation of a decision rule is comprised of two ingredients: $1)$ simulations where the decision rule is to be applied; and $2)$ an objective function for measuring its performance during the conducted simulations.

Figure 3: Decision rule selection procedure illustration.

Simulations represent the setting in which the decision rule is required to operate after its parameters are tuned. They can be as simple as applying $f$ on held out data, or involve complex mechanisms for emulating an overall system where the decision rule is to be applied and the expected environment. Various terminologies are used to describe simulators in different domains, including validation (in ML), closed-loop simulation (in control), and back-testing (in finance).

### Example 3

A simulation setup for super-resolution recovery (Example 1 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization")) can be comprised of a set of unseen images and a mapping that converts them into low-resolution data.

### Example 4

A simulation setup for stochastic control (Example 2 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization")) can be software which emulates how an action $s_{t - 1}$ is translated into a state $z_{t}$ and an observed context $x_{t}$.

Objective functions are measures used to evaluate a decision rule. In some cases, the objective is given by a cost or a loss function which one aims at minimizing, or it can be specified by an application utility or reward, which we wish to maximize. In many applications there are multiple objectives, which are scalarized into a single cost function, for example, by forming a weighted sum. The objective can be the average value of individual decisions, or a function of multiple decisions, e.g., a trajectory. In its most basic form, a loss function evaluates the decision rule for a given context as compared with some desired decision; such a loss function is formulated as a mapping

Broadly speaking, dictates the success criteria of a decision mapping for a given context-decision pair. For instance, in inference tasks, candidate losses include the error rate (zero-one) loss ${l_{Err}{(f,x,s^{true})}} = \mathbf{1}_{{f{(x)}} \neq s^{true}}$ (for classification) and the $\ell_{2}$ loss ${l_{Est}{(f,x,s^{true})}} = {\|{s^{true} - {f{(x)}}}\|}_{2}^{2}$ (for estimation).

In optimization-based decision rules, the objective used to formulate the optimization problem need not be the same as the evaluation objective function. The evaluation objective measures the performance of the decision rule in simulation; it may be complex and capture multiple utilities of the overall system. In some applications, e.g., medical imaging, it may involve inspecting the simulations outcome by human experts. The objective of the optimization-based decision rule, referred to as the decision rule objective, is used for tuning the decision rule; it is often a surrogate of the evaluation objective, including e.g., simplifications, approximations, and regularizations, introduced for tractability and to facilitate tuning.

The selection of a decision rule depends on how the mapping is judged during tuning and evaluation. This is a three-step procedure, whose first two steps are its design, involving $(i)$ selecting a type of decision rule $\mathcal{F}$ (e.g., linear model, decision tree, DNN, etc.); and $({ii})$ tuning its parameters $\theta$ based on the decision rule objective. Then $({iii})$, the tuned system is evaluated in simulations based on the evaluation objective. The evaluation is determined by the simulator, and is independent of the design steps. Fig. 3 illustrates the overall procedure. The traditional approaches to carry out the design procedure, referred to as model-based or classic methods, are based on modelling and knowledge; the data-centric approach uses ML, with deep learning being a leading family of ML techniques.

## Model-Based Methods

### III-A Decision Rule Objective

The classic model-based approach sets decision rules based on domain knowledge. Namely, knowledge of an underlying model which mathematically describes the setup is used along with the loss measure $l{( \cdot )}$ to formulate an analytical surrogate decision rule objective $\mathcal{L}:{\mathcal{F}\mapsto\mathcal{R}^{+}}$. Both the model imposed and the objective are typically simplified approximations of the evaluation simulator and objective, respectively, introduced for analytical tractability. The decision rule objective also often includes sensitivity and regularization terms, resulting in an inductive bias on $f$. The decision rule objective is applied to select the decision rule from $\mathcal{F}$, which can be a pre-defined type or the entire space of mappings from $\mathcal{X}$ to $\mathcal{S}$. Once a simplified objective $\mathcal{L}$ is set, one can often find the optimal decision rule in $\mathcal{F}$ with respect to $\mathcal{L}$.

For instance, for inference tasks, given knowledge of a distribution $\mathcal{P}$ defined over $\mathcal{X} \times \mathcal{S}$, one can formulate the risk ${\mathcal{L}{(f)}} = {{\mathbb{E}}_{{(x,s^{true})} \sim \mathcal{P}}{\{{l{(f,x,s^{true})}}\}}}$, and set $f$ to minimize the error rate risk among all mappings from $\mathcal{X}$ to $\mathcal{S}$ as the maximum a-posteriori probability (MAP) rule, given by:

The formulation of $\mathcal{L}{(f)}$ is dictated by the model imposed on the underlying relationship between $x$ and the desired $s^{true}$. This objective typically contains parameters of the model, which we denote by $\theta^{o}$, and henceforth write $\mathcal{L}_{\theta^{o}}{(f)}$.

### Example 5

A common approach to treat the super-resolution problem in Example 1 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization") is to assume the compression obeys a linear Gaussian model, i.e.,

The matrix $H$ in may represent the point-spread function of the system, a reduced measurement resolution, etc. The MAP rule in becomes

where ${\phi{(s)}}:={- {\log{\Pr{({s^{true} = s})}}}}$. The resulting decision rule objective requires imposing a prior on $\mathcal{S}$ encapsulated in $\phi{(s)}$. A popular selection is to impose sparsity in some known domain $\Psi$ (e.g., wavelet), such that $s = {\Psir}$, where $r$ is sparse. This boils down to an objective defined on $r$, given by

where the parameter $\rho$ encapsulates $\sigma^{2}$ and the expected sparsity level. The parameters of the objective in are

The above example shows how one can leverage domain knowledge to formulate an objective, which is dictated by the parameter vector $\theta^{o}$. It also demonstrates two key properties of model-based approaches: $(i)$ that surrogate models can be quite unfaithful to the true data, since, e.g., the Gaussianity of $w$ implies that $x$ in can take negative values, which is not the case for image data; and $({ii})$ that simplified models allow translating the task into a relatively simple closed-form objective, as in. Similar approaches can be used to tackle the stochastic control setting of Example 2 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization").

### Example 6

Traditional linear-quadratic-Gaussian (LQG) control considers dynamics that take the form of a linear Gaussian state-space model, where

Here, the noise sequences $v_{t},w_{t}$ are zero-mean Gaussian signals, i.i.d. in time, with covariance matrices $V,W$, respectively. The objective at each time instance $t$ is given by

The parameters of the objective function are thus

### Example 7

Model predictive control replaces the expectation based objective in with a deterministic optimization problem based on forecasting over some finite horizon $H$. Here, for the linear Gaussian state-space model of with a quadratic loss, the objective at each time period $t$ is given by

where ${s_{t},\ldots,s_{{t + H} - 1}} = {f{({\{ x_{\tau}\}}_{\tau \leq t})}}$ and $\{{\hat{z}}_{t + \tau}\}$ are computed via with $\{ v_{t + \tau}\}$ and $\{ w_{t + \tau}\}$ replaced with some predicted values. The parameters $\theta^{o}$ of the objective function thus include these predictive mapping, as well as the matrices $A,B,C,{\{ Q_{\tau},R_{\tau}\}}$.

The formulation of the decision rule objectives in Examples 5-7 relies on full domain knowledge, e.g., one has to know the prior $\phi{( \cdot )}$ or the covariances $V,W$ in order to express the objectives in and, respectively.

### III-B Decision Rule Type

Model-based methods determine the decision rule objective based on domain knowledge, obtained from measurements and from understanding of the underlying physics. Once the objective is fixed, evaluating the decision rule boils down to solving an optimization problem, typically resulting in highly-specific types of decision mappings whose structure follows from the optimization formulation. In particular, a decision rule is typically obtained as either an explicit solution of the problem, or in the form of an iterative solver.

Explicit solvers arise when the decision rule objective takes a relatively simplified form, such that one can characterize the optimal mapping. In such cases, the optimization-based decision rule of type T3 can specialize into an affine rule T1.

### Example 8

The mapping which minimizes the LQG loss in Example 6 is known to be obtained by first predicting the latent state $z_{t}$ using a Kalman filter, i.e.,

where $L_{t}$ is the Kalman gain matrix. The action is taken to be

with $K_{t}$ being the feedback gain matrix. Both $L_{t}$ and $K_{t}$ are determinstically determined by $\theta^{o}$ in, and are updated based on internally tracked statistical moments that are recursively updated.

Example 8 demonstrates how the modelling of a complex task using a simplified linear Gaussian model, combined with the usage of a simple surrogate quadratic objective, results in an explicit solution, which here takes a linear form. While this surrogate model and the objective are likely to differ from the operation of the system, one can tune the objective parameters $\theta^{o}$ (encapsulated in and in $K_{t}$) via simulations, thus modifying the decision rule to match the expected operation.

Iterative solvers follow mathematical steps which gradually lead to the decision that achieves the decision rule objective, yielding a mapping as in type T4. A large body of optimization techniques are iterative, with common schemes based on first-order methods (i.e., gradient iterative steps) \[13, Ch. 9\]. Iterative optimizers typically give rise to additional parameters which affect the speed and convergence rate of the algorithm, but not the actual objective being minimized. We refer to these parameters of the solver as hyperparameters, and denote them by $\theta^{h}$. As opposed to the objective parameters $\theta^{o}$ (as in, e.g., ), they often have no effect on the solution when the algorithm is allowed to run to convergence, and so are of secondary importance. But when the iterative algorithm is stopped after a predefined number of iterations, they affect the decisions, and therefore also the decision rule objective. Due to the surrogate nature of the objective, such stopping does not necessarily degrade the evaluation performance.

### Example 9

The super-resolution objective in can be tackled using the alternating direction method of multipliers (ADMM). This method summarized as Algorithm 1, where we merge $\sigma^{2}$ in into the prior $\phi{( \cdot )}$ for brevity, and the proximal mapping is defined as

Fix step size μ, and λ &gt; 0.
Update $v_{k + 1} = {{prox}_{\frac{1}{2\lambda}\phi}{({s_{k + 1} + u_{k}})}}$ (see ).

ADMM converges to a solution of when $\phi{( \cdot )}$ is convex, for any positive value of $\mu$. When $\phi{( \cdot )}$ is not convex, there are no convergence guarantees, but it has been observed in practice that good results are obtained, when $\mu$ is chosen appropriately. Since convergence of iterative optimizers to an optimal decision can be generally guaranteed for convex objectives, one often has to relax and modify the objective.

### Example 10

The non-convex super-resolution surrogate objective with sparse prior in can be relaxed into

where we set $\Psi$ to the identity matrix for simplicity. This successive relaxation of an already surrogate objective yields a convex cost in. It can be solved, e.g., using proximal gradient descent with step size $\mu$, which specializes here into the ISTA \[15, Ch. 7\]. Letting ${\mathcal{T}_{\beta}{( \cdot )}} \triangleq {{sign}{(x)}{\max{(0,{{|x|} - \beta})}}}$ be the element-wise soft-thresholding operation, the update equation is

In Example 9, illustrated in Fig. 5(a), the iterative solver introduces two hyperparameters, i.e., $\theta^{h} = {\lbrack\lambda,\mu\rbrack}$, which are used in the iterative minimization of. In Example 10, there is only one hyperparameter $\theta^{h} = \mu$. The hyperparameters $\theta^{h}$ are often set by manual hand tuning based on simulations.

### III-C Summary

Model-based methods rely on decision rules of type T3, where an analytically tractable optimization problem is formulated based domain knowledge. The optimization problems solved are typically surrogates for the real application problem. The decision rule objectives and constraints are often inspired by physical characteristics, understanding of the system operation, and existing models (of noise, disturbances, and other quantities). Yet, in practice, objectives are likely to differ from the system task, due to multiple reasons, including:

Simplifying approximations, e.g., modelling super-resolution as a linear Gaussian setup in Example 5.

Estimation inaccuracies, e.g., substituting estimated covariances $W,V$ to compute the LQG objective in Example 6 or an estimated $H$ in the MAP objective in Example 5.

Introducing regularization terms in the objective, e.g., $\rho{\| r\|}_{0}$ in Example 5.

Relaxations or approximations of the objective and constraints to render the optimization problem solvable.

Scaling of some of the quantities involved.

Model-based techniques are particularly suitable for the resulting optimization problem. Once a solvable (e.g., convex) formulation is determined, these methods are guaranteed to obtain its solution. Furthermore, their operation is interpretable, and tends to be highly flexible, as one can substitute different values of the objective parameters $\theta^{o}$.

In practice, accurate knowledge of the statistical model relating the context and the desired decision is often unavailable. Consequently, model-based techniques may require imposing assumptions on the underlying statistics, which in some cases reflect the actual behavior, but can also be a crude approximation. In the presence of inaccurate model knowledge, either as a result of estimation errors or due to enforcing a model which does not fully capture the environment, the performance of model-based techniques tends to degrade during evaluation. This limits the applicability of model-based schemes in scenarios where one cannot represent the task via a decision rule objective in a closed-form (and preferably simplified) expression, or alternatively, when the underlying model is costly to estimate accurately, or too complex to express analytically. Additional challenges stem from the fact that decision making can be slow, particularly using iterative solvers. Finally, setting the hyperparameters $\theta^{h}$ is often elusive, and may involve heuristics and cumbersome hand-crafted tunning.

## Deep Learning

### IV-A Decision Rule Objective

While in many applications coming up with accurate and tractable statistical modelling is difficult, we are often given access to data describing the setup. ML systems learn their mapping from data. In a supervised setting, data is comprised of a set of $n_{t}$ pairs of inputs and labels, denoted $\mathcal{D} = {\{ x_{i},s_{i}^{true}\}}_{i = 1}^{n_{t}}$. In reinforcement learning, data is obtained from a simulator, which on each decision produces a subsequent context. This data is referred to as the training set, and there is typically an additional data set used for evaluation and validation. Since no mathematical model relating the input and the desired decision is imposed, the decision rule objective is often the empirical risk. Focusing on a supervised setting, this objective is given by

Decision rule objectives that are based on data and do not rely on modeling are often a more faithful representation of the evaluation objective compared with model-based approaches. However, they are still surrogates. This follows not only from the difference between the training and validation data, but also from the frequent inclusions of regularizing terms and mechanisms such as dropout and batch normalization, whose operation differs between training and evaluation.

While we focus our description on supervised settings, ML systems can also learn in an unsupervised manner. In such cases, the data set $\mathcal{D}$ is comprised only of a set of examples ${\{ x_{i}\}}_{i = 1}^{n_{t}}$, and the loss measure $l$ is defined over $\mathcal{F} \times \mathcal{X}$, instead of over $\mathcal{F} \times \mathcal{X} \times \mathcal{S}$ as in. Unsupervised ML is often used to discover patterns in the data, with tasks including clustering, anomaly detection, generative modeling, and compression.

### IV-B Decision Rule Type

In contrast to the model-based case, where decision rules can sometimes be derived by directly solving the optimization problem without initially imposing structure on the system, setting a decision rule based on data necessitates restricting the domain of feasible mappings. This stems from the fact that one can usually form a decision rule which minimizes the empirical loss of by memorizing the data, i.e., overfit \[12, Ch. 2\]. A leading strategy in ML, upon which deep learning is based, is to assume a highly-expressive generic parametric model on the decision mapping, while incorporating optimization mechanisms and regularizing the empirical risk to avoid overfitting. In deep learning, $f$ is a DNN, i.e., type T5, with the parameters $\theta$ being the network parameters, e.g., the weights and biases of each layer. By the universal approximation theorem, DNNs can approach any Borel measurable mapping \[16, Ch. 6\].

Figure 4: Continuous spectrum of specificity and parameterization with model-based methods and deep learning constituting the extreme edges of the spectrum.

While model-based algorithms are specifically tailored to a given scenario, deep learning is model-agnostic. The unique characteristics of the scenario are encapsulated in the learned weights. The decision rule family $\mathcal{F}$, i.e., the possible DNN mappings, is generic and can be applied in a broad range of different problems. While standard DNN structures are model-agnostic and are commonly treated as black boxes, one can still incorporate some level of domain knowledge in the selection of the network architecture. For instance, when the input is known to exhibit temporal correlation, architectures based on recurrent neural networks \[16, Ch. 10\] or attention mechanisms are often preferred. Alternatively, in the presence of spatially local patterns, one may utilize convolutional layers. An additional method to incorporate domain knowledge into a black box DNN is by pre-processing of the input via, e.g., hand-crafted feature extraction.

### Example 11

The super-resolution task (Example 1 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization")) can be carried out by training a deep convolutional autoencoder.

### Example 12

Stochastic control (Example 2 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization")) can be carried by a DNN controller using deep reinforcement learning.

The fact that DNNs are comprised of a large number of parameters, and that massive data sets are often used for their training, makes it unlikely to recover $\theta$ that minimizes the empirical risk with affordable computational effort. Instead, the tuning of $\theta$ is typically carried out using first-order gradient-based algorithms, where gradients estimated from a small number of randomly chosen samples, e.g., by mini-batch stochastic gradient descent (SGD) iterations of the form

where $\mathcal{D}_{j}$ is a mini-batch sampled from $\mathcal{D}$, and $\eta_{j}$ is the learning rate. The gradients in are computed using backpropagation. Mini-batch SGD is the basis for DNN training, with common variants using momentum and adaptive learning rates. Such training methods operate in an automated manner, enabling tuning of DNNs from massive data sets.

### IV-C Summary

DNNs operate in a model-agnostic manner, and can be tuned to implement an immense family of mappings, making them widely adopted in areas where principled mathematical models are scarce, such as computer vision and natural language processing. Despite their success, existing deep learning approaches are subject to several challenges, which limit their applicability in some application domains. The computational burden of training and utilizing highly parametrized DNNs, as well as the fact that massive data sets are often required for their training, constitute major drawbacks in various signal-processing, communications and in control applications. This limitation is particularly relevant when operating on hardware-constrained devices, e.g., mobile systems, unmanned aerial vehicles, and sensors. Such systems are typically limited in their ability to utilize highly parametrized DNNs, and they should be flexible to adapt to variations in the environment. Furthermore, the fact that the decision mapping is learned solely from data often gives rise to generalization issues on unseen data. Finally, due to the complex and generic structure of DNNs, it is often extremely challenging to understand how they obtain their predictions, track the rationale leading to their decisions, and characterize confidence intervals. Consequently, deep learning does not offer the interpretability, flexibility, versatility, and reliability of model-based methods. This is a major limitation for tasks involving critical and even life-saving decision making, such as the control of vehicular and aerospace systems.

## Hybrid Model-Based Deep Learning Optimizers

Model-based methods and deep learning are often viewed as fundamentally different approaches for setting decision boxes. Nonetheless, both strategies typically use parametric mappings, i.e., the weights $\theta$ of DNNs and the parameters $(\theta^{o},\theta^{h})$ of model-based optimizers, whose setting is determined based on data and on principled mathematical models. The core difference thus lies in the specificity and the parameterization of the decision rule type: Model-based methods are knowledge-centric, using decision rules that are task-specific, and usually involve a limited number of parameters that can often be set manually. Deep learning is data-centric, and thus uses highly-parametrized model-agnostic task-generic mappings.

The identification of model-based methods and deep learning as two ends of a spectrum of specificity and parameterization indicates the presence of a continuum, as illustrated in Fig. 4. In fact, many techniques lie in the middle ground, designing decision rules with different levels of specificity and parameterization by combining some balance of deep learning with model-based optimization. In this section we review three systematic frameworks for designing decision mappings that are both knowledge- and data-centric as a form of hybrid model-based deep learning: The first strategy, coined learned optimizers, uses deep learning automated tuning machinery to tune parameters of model-based optimization conventionally tuned by hand. The second family of techniques, referred to as deep unfolding, converts iterative optimizers into DNNs. The third type of model-based deep learning schemes, which we call DNN-aided optimizers, augments model-based optimization with dedicated DNNs.

### V-A Learned Optimization

Learned optimizers use conventional model-based methods for decision making, while tuning the parameters and hyperparameters of classic solvers via automated deep learning training. This form of model-based deep learning leverages data to optimize the optimizer. While learned optimization bypasses the traditional daunting effort of manually fitting the decision rule parameters, it involves the introduction of new hyperparameters of the training procedure that must to be configured (typically by hand).

Learned optimization effectively converts an optimizer into an ML model. Since automated tuning of ML models typically uses gradient-based methods as in, a key requirement is for the optimizer to be differentiable, namely, that one can compute the gradient of its decision with respect to its parameters. Fortunately, convex optimization solvers are typically differentiable (under some regularity conditions). Alternatively, for non-convex optimization, one can differentiate numerically or, in some cases, implicitly.

Examples: Learned optimization focuses on optimizing parameters conventionally tuned manually; these are parameters whose value does not follow from prior knowledge of the problem being solved, and thus their modification affects only the solver, and not the problem being solved. For model-based optimizers based on explicit solutions, the parameters available are only those of the objective $\theta^{o}$. Nonetheless, some of these parameters stem from the fact the objective is inherently a surrogate for the actual problem being solved, and thus require tuning, as shown in the following example.

### Example 13

Consider a dynamic system characterized by a state-space model as in. In such settings, the linear mappings $A,B,C$ often arise from understanding the physics of the problem, while the objective parameters $Q$ and $R$ stem from the system requirements. Nonetheless, in practice, one typically does not have a concrete stochastic model for the noise signals, which are often introduced as a way to capture stochasticity, and thus $V$ and $W$ are often tuned by hand.

Given a data set of $n_{t}$ trajectories of $T$ observations with the corresponding states and actions $\mathcal{D} = {\{{\{ x_{t,i},s_{t,i},z_{t,i}\}}_{t = 1}^{T}\}}_{i = 1}^{n_{t}}$, one set the trainable parameters to be $\theta = {\lbrack V,W\rbrack}$, and optimize them via with $\mathcal{L}_{\mathcal{D}}$ being the empirical $\ell_{2}$ distance between the Kalman filter prediction and the true state. The gradients of $\mathcal{L}_{\mathcal{D}}$ are computed using backpropagation through time (BPTT), building upon the diffrentiability of the Kalman gain $L_{t}$ with respect to both $V$ and $W$.

When the optimizer being learned is an iterative solver, one can use data to tune the hyperparameters $\theta^{h}$, whose value does not affect the optimization objective. This can be specialized for the ADMM optimizer of Example 9, as shown next.

### Example 14

Consider the ADMM solver (Algorithm 1). Given a data set $\mathcal{D}$ of $n_{t}$ labeled samples, the hyperparameter vector $\theta^{h} = {\lbrack\lambda,\mu\rbrack}$ can be optimized by treating it as trainable parameters, as visualized in Fig. 5(b). Letting $f{( \cdot;\theta^{h})}$ be the ADMM mapping with hyperparameters $\theta^{h}$, this is given by

The problem in is as DNN training, e.g. where to compute each gradient of the objective with respect to $\theta^{h}$, Algorithm 1 must first run until it reaches convergence, after which the gradients are computed via BPTT.

Summary. Learned optimizers are ML decision rules which completely preserve the operation of conventional model-based methods. As such, they share the core gains of principled optimization. These include its suitability for the problem at hand; the interpretability that follows from the ability to relate each feature involved to an operation meaning; and flexibility, as one can control the objective for which the decision is configured using its non-learned parameters in $\theta^{o}$.

Compared with model-based optimization, learned optimizers facilitate the design procedure, avoiding the need to tune parameters by hand. Furthermore, the fact that tuning is carried out by observing the decision output and evaluating it based on data allows to improve performance when the surrogate objective differs from the (possibly analytically intractable) evaluation objective. Finally, when the decision box is an iterative solver, learned optimization can reduce the convergence speed compared with manually tuned $\theta^{h}$.

Figure 5: An illustration of the model-based deep learning strategies arising from the ADMM optimizer (Algorithm 1), where variables in red fonts represent trainable parameters: a) the model-based optimizer (Example 9); b) a learned ADMM optimizer (Example 14); c) plug-and-play ADMM (Example 20); and d) deep unfolded ADMM (Example 16).

### V-B Deep Unfolding

A relatively common methodology for combining model-based methods and deep learning is that of deep unfolding, also referred to as deep unrolling. Originally proposed by Greger and LeCun for sparse recovery, deep unfolding converts iterative optimizers into trainable DNNs. As the name suggests, the method unfolds an iterative algorithm into a sequential procedure with a fixed number of iterations. Then, each iteration is treated as a layer, with its trainable parameters $\theta$ being either only the hyperparameters $\theta^{h}$, or also the decision rule objective parameters $\theta^{o}$.

Unfolding an iterative optimizer into a DNN facilitates tuning different parameters for each iteration, being converted into trainable parameters of different layers. This is achieved by training end-to-end, i.e., by evaluating the system output based on data. Letting $K$ be the number of unfolded iterations, deep unfolding can learn iteration-dependent hyperparameters ${\{\theta_{k}^{h}\}}_{k = 1}^{K}$ and even objective parameters ${\{\theta_{k}^{o}\}}_{k = 1}^{K}$. This increases the parameterization and abstractness compared with learned optimization of iterative solvers, which typically reuses the learned hyperparameters and runs until convergence (as in model-based optimizers). Nonetheless, for every setting of ${\{\theta_{k}^{o}\}}_{k = 1}^{K}$ and ${\{\theta_{k}^{h}\}}_{k = 1}^{K}$, a deep unfolded system effectively carries out its decision using $K$ iterations of some principled iterative solver known to be suitable for the problem.

Examples: Deep unfolded networks can be designed to improve upon model-based optimization in convergence speed and model abstractness. The former is achieved since the resulting system operates with a fixed number of iterations, which can be much smaller compared with that usually required to converge. This is combined with the natural ability of deep unfolding to learn iteration-dependent hyperparameters to enable accurate decisions to be achieved within this predefined number of iterations, as exemplified next:

### Example 15

Let us consider again the ADMM optimizer of Algorithm 1. A deep unfolded ADMM is obtained by setting the decision to be $s = s_{K}$ for some fixed $K$, and allowing each iteration to use hyperparameters $\lbrack\lambda_{k},\mu_{k}\rbrack$, that are stacked into the trainable parameters vector $\theta$. Similarly to, these hyperparameters are learned from data via

Example 15 implements $K$ ADMM iterations, as only the hyperparameters are learned. One can also transform iterative solvers into more abstract DNNs by also tuning the objective of each iteration. Continuing along the line of Examples 14-15, we show how this is can be achieved following:

### Example 16

An alternative approach to unfold the ADMM optimizer into a DNN is by repeating the procedure in Example 15, where algorithm is unfolded into $K$ iterations with each assigned hypereparameters $\lbrack\lambda_{k},\mu_{k}\rbrack$. Furthermore, the first update step of Algorithm 1 is now replaced with

For $W_{k}^{1} = {{({{H^{T}H} + {2\lambdaI}})}^{- 1}H^{T}}$ and $W_{k}^{2} = {2\lambda{({{H^{T}H} + {2\lambdaI}})}^{- 1}}$, coincides with the corresponding step in Algorithm 1. The trainable parameters $\theta = {\{ W_{k}^{1},W_{k}^{2},\lambda_{k},\mu_{k}\}}_{k = 1}^{K}$ are learned from data by jointly minimizing

The resulting decision mapping of Example 16 is illustrated in Fig. 5(d). Unlike Example 15 which only learns the hyperparameters, the unfolded ADMM in Example 16 jointly learns the hyperparameters and the objective parameters $\theta^{o}$ per each iteration. This can be viewed as if each iteration follows a different objective, such that the output after $K$ iterations most accurately matches the desired value. While each layer in Example 16 has different parameters, one can enforce identical parameters across layers. The DNN can realize a larger family of mappings compared with the original model-based optimizer, which serves as a principled initialization for the system, rather than its fixed structure as in Example 15.

A popular application of deep unfolding, which follows the rationale of Example 16 with both $\theta^{o}$ and $\theta^{h}$ learned end-to-end, is the unfolding of ISTA into learned (LISTA).

### Example 17

The ISTA optimizer in Example 10 can be unfolded into the LISTA DNN architecture by fixing $K$ iterations and replacing the update step in with

For $W_{k}^{1} = {\muH^{T}}$, $W_{k}^{2} = {I - {\muH^{T}H}}$, $\mu_{k} = 1$ and $\lambda_{k} = {\mu\rho}$, coincides with model-based ISTA. The trainable parameters $\theta = \left\lbrack {\{ W_{k}^{1},W_{k}^{2},\mu_{k}\}}_{k = 1}^{K} \right\rbrack$ are learned from data via end-to-end training as in.

Summary: Deep unfolding designs dedicated DNNs whose architecture follows iterative optimization algorithms. Compared with conventional DNNs applied to similar tasks, deep unfolded networks are more task-specific and less parameterized, as the setting of their trainable parameters and their interconnection is based on a iterative solver suitable for such problems. As a result, deep unfolded networks tend to require less data for training compared with standard DNNs, and often achieve improved performance and generalization. Furthermore, deep unfolded networks offer improved interpretability, as one can identify the meaning of some of its internal features, a task which is rarely achievable in conventional DNNs. In deep unfolded networks, the features exchanged between its layers represent the output of each iteration as in type T4, and can thus be associated with an estimate of the decision which is gradually refined as in iterative optimization.

Compared with model-based optimization, converting an iterative solver (T4) into a DNN with $K$ layers (T5) typically results in faster inference. The fact that iteration-specific parameters are learned end-to-end allows deep unfolded networks to operate with much fewer layers compared with the number of iterations required by the model-based optimizer to achieve similar performance. Furthermore, the increased parameterization improves the abstractness of the decision rule, particularly when both the hyperparameters $\theta^{h}$ and the objective parameters $\theta^{o}$ are jointly learned as in Examples 16 and 17. Such unfolded networks depart from the iterative algorithm from which they originates, allowing them to overcome mismatches and approximation errors associated with the need to specify a mathematically tractable surrogate objective for decision making. In particular, training an unfolded network designed with a mismatched model using data corresponding to the true underlying scenario typically yields improved performance compared to the model-based iterative algorithm with the same model-mismatch, as the unfolded network can learn to compensate for this mismatch.

### V-C DNN-Aided Optimization

The third model-based deep learning strategy combines conventional DNN architectures with model-based optimization to enable the latter to operate reliably in complex domains. The rationale here is to preserve the objective and structure of a model-based decision mapping suitable for the problem at hand based on the available domain knowledge, while augmenting computations that rely on approximations and missing domain knowledge with model-agnostic DNNs. DNN-aided optimizers thus aim at benefiting from the best of both worlds by accounting in principled manner for the available domain knowledge while using deep learning to cope with the elusive aspects of the problem description.

Unlike the aforementioned strategies of learned optimizers and deep unfolding, which are relatively systematic and can be viewed as recipe-style methodologies, DNN-aided optimization accommodates a broad family of different techniques for augmenting model-based optimizers with DNNs. We next discuss some representative DNN-aided optimization approaches.

Examples: The straight-forward application of DNN-aided optimization replaces an internal computation of a model-based solver with a dedicated DNN, converting it into a trainable model-based deep learning system. An example of how this is done, based on, is detailed next.

### Example 18

Consider again the setting of Example 13, where a Kalman filter is designed without knowing the distribution of the noise signals in. Since the dependency on the noise statistics in the Kalman filter is encapsulated in the Kalman gain $L_{t}$, its computation can be replaced with a trainable DNN, and thus is replaced with

where $h_{\theta}$ is a DNN with parameters $\theta$. Particularly, since $L_{t}$ is updated recursively, its learned computation is carried out with an RNN. By letting $f{( \cdot;\theta)}$ be the latent state estimate computed using with parameters $\theta$, the overall system is trained end-to-end via

Example 18 was shown in to overcome non-linearities and mismatches in the state-space model, outperforming the classical Kalman filter while retaining its data efficiency and interpretability. It is emphasized though that Example 18 represents one approach to combine Kalman filtering with DNN-aided optimization methodology. Additional techniques include the usage of an external DNN operating in parallel with the filter and providing correction terms, as proposed in, and the application of the Kalman filter to learned features extracted by a DNN as in, exemplified next.

### Example 19

Consider a state-space model as in where the observations $x_{t}$ are complex and non-linear, i.e., (7b) does not hold. One can still apply a Kalman filter designed for a linear Gaussian setting by applying a DNN $h_{\theta}{( \cdot )}$ to transform $x_{t}$ into features that follow the state-space model assumed by the model-based filter. Here, becomes

and the tuning is done via end-to-end training as in.

The latter approach, of applying a model-based optimizer to features extracted by a DNN as in Example 19, can also be used to enforce decisions made by a DNN to comply to some underlying physical requirements, see, e.g.,.

The above examples build upon the differentiability of the model-based solver to train the DNN augmented into the method end-to-end. Nonetheless, DNN-aided optimization can also augment model-based methods with DNNs that are pre-trained, possibly even in an unsupervised manner thus alleviating the dependence on the availability of labeled data. One such family of DNN-aided optimization techniques, referred to as plug-and-play networks, is exemplified next.

### Example 20

Consider the application of ADMM (Algorithm 1) to solving. Computing the proximal mapping in the second update step is often challenging, as the ability to evaluate the prior $\phi{( \cdot )}$ is required, which in practice may be unavailable or involve exhaustive computations. Nonetheless, the proximal mapping is invariant of the task, and can be viewed as a denoiser for samples in $\mathcal{S}$, e.g., high-resolution images for the setting in Example 1 ‣ II Decision Making ‣ Model-Based Deep Learning: On the Intersection of Deep Learning and Optimization"). Denoisers are common DNN models, which can be trained in an unsupervised manner, and can reliably operate on signals with intractable priors (e.g., natural images). By letting $h_{\theta}{( \cdot;\alpha)}$ be a DNN trained to denoise data in $\mathcal{S}$ with noise level $\alpha$, one can thus implement Algorithm 1 without specifying the prior $\phi{( \cdot )}$ by replacing the proximal mapping with

The term plug-and-play is used to describe decision mappings as in Example 20 where pre-trained models are plugged into model-based optimizers without further tuning, as illustrated in Fig. 5(c). Nonetheless, this methodology can also incorporate deep learning into the optimization procedure by, e.g., unfolding the iterative optimization steps into a large DNN whose trainable parameters are those of the smaller networks augmenting each iteration, as in. This approach allows to benefit from both the ability of deep learning to implicitly represent complex domains, as well as the inference speed reduction of deep unfolding along with its robustness to uncertainty and errors in the model parameters assumed to be known. Nonetheless, the fact that the iterative optimization must be learned from data in addition to the prior on $\mathcal{S}$ implies that larger amounts of labeled data are required to train the system, compared to using the model-based optimizer.

An alternative approach to augment model-based solvers with pre-trained DNNs is the usage of deep priors. As opposed to plug-and-play networks, which augment the solver with a DNN in order to cope with complex modelling, deep priors use DNNs to directly compute the (possibly intractable) decision rule objective, as shown in the next example.

### Example 21

Consider again the setting in Example 20, where one aims at solving while the prior $\phi{( \cdot )}$ is unavailable and possibly intractable. However, now let us assume that we have access to some bijective mapping from some latent space $\mathcal{Z}$ to the signal space $\mathcal{S}$, denoted $g:{\mathcal{Z}\mapsto\mathcal{S}}$, such that the prior term $\phi{(s)}$ can be written in terms of $z$ as ${\phi{(s)}} = {{\overset{\sim}{\phi}{(z)}}|}_{z = {G^{- 1}{(s)}}}$. In this case, the MAP rule in becomes

Deep generative priors use a pre-trained DNN-based prior $h_{\theta}{( \cdot )}$, typically a generative network trained to map Gaussian vectors to $\mathcal{S}$. The resulting objective becomes:

Even though the exact formulation of $h_{\theta}{( \cdot )}$ may be highly complex, one can tackle via first-order optimization, building upon the fact that DNNs allow simple computation of gradients via backpropagation. These gradients are taken not with respect to the weights (as done in conventional DNN training), but with respect to the input of the network.

Summary: DNN-aided optimizers implement decision boxes via an interleaving of model-based principled mathematical procedures and trained DNNs. The approach is particularly suitable for enabling decision making in complex environments with partial domain knowledge, where the latter is used to determine the suitable model-based optimizer, whose complex computations are replaced with DNNs. Such augmentations facilitate the model-based optimizer in coping with mismatches in its objective model and its parameters, and makes it applicable in complex domains.

Compared with the direct application of deep learning for the decision mappings, DNN-aided optimizers are less generic and more task-specific due to the fact that they preserve the structure of a model-based optimizer. This property does not only facilitate their training procedure, which can sometimes be done unsupervised as in Examples 20-21, but also yields decision rules that are interpretable and suitable for their task. This interpretability can be exploited to extract additional measures of interest, e.g., uncertainty, as shown in for the DNN-aided Kalman filter in Example 18; such measures, which are naturally obtained in model-based methods while being challenging to characterize for black-box DNNs, are often of importance in some applications.

Figure 6: Experimental results (reproduced from ) for recovering ultrasound contrast agents from cluttered maximum intensity projection images: a) the observed image; b) the ground-truth sparse contrast agents; c) image recovered by deep unfolding; d) MSE versus iterations/layers of deep unfolded network (CORONA) compared to fast ISTA.

## Results

In this section we experimentally exemplify model-based deep learning methodology in a broad range of diverse application areas, including ultrasound imaging, optics, digital communications, and tracking of dynamic systems.

### VI-A Ultrasound Imaging

We first demonstrate the ability of deep unfolding, and particularly of LISTA-like architectures as detailed in Example 17, to facilitate the processing of ultrasound images. Our first example is taken from, which trained a deep unfolded decision box for clutter removal in contrast-enhanced ultrasound. Here the data was modeled as comprising a low-rank clutter background and a sparse blood flow image depicting the contrast agents. A generalization of ISTA was then applied to robust principled component analysis (RPCA) optimization leading to an unfolded network referred to as CORONA: Convolutional rObust pRincipal cOmpoNent Analysis. Here, both the context $x$ and the decision $s$ are maximum intensity projection ultrasound images; the decision rule type type is $K = 10$ iterations of a generalized ISTA, i.e., type T4, whose objective parameters $\theta^{o}$ and hyperparameters $\theta^{h}$ are tuned per-iteration from data via end-to-end training using the empirical risk with the $\ell_{2}$ loss $l_{Est}{( \cdot )}$, computed over a set of $n_{t} = 4800$ images.

An experimental study of this application, showing that deep unfolding can infer both quickly and reliably, is presented in Fig. 6. Fig. 6(c) shows the recovered ultrasound (contrast agents) image from a cluttered image (Fig. 6(a)) achieved using deep unfolding of RPCA. Comparing the recovered image to the ground-truth in Fig. 6(b) demonstrates the accuracy in using a DNN to imitate the operations of the generalized ISTA algorithm in a learned fashion. Furthermore, the fact that the unfolded network learns its parameters from data for each layer allows it to infer with a notably reduced number of layers compared to the corresponding number of iterations required by the model-based algorithm, which utilizes its full domain knowledge in applying the hard-coded iterative procedure. This is illustrated in Fig. 6(d) which demonstrates that the trained unfolded network can achieve with only a few layers a mean-squared error (MSE) accuracy which the model-based fast ISTA of does not approach even in $50$ iterations.

Deep unfolding can also be applied for super-resolution in ultrasound using micro bubbles. For instance, the work applied LISTA for ultrasound-based breast lesion characterization. Here, the input $x$ is a low-resolution ultrasound image, while the decision $s$ is a high-resolution image. The decision rule is again an unfolded iterative algorithm, i.e., T4, with $\theta^{o}$ and $\theta^{h}$ jointly learned end-to-end as in Example 17.

The ability of LISTA to increase ultrasound resolution and facilitate diagnosis is demonstrated in Fig. 7. Here, a super-resolved recovery of a fibroadenoma (Fig. 7, top) shows an oval, well circumscribed mass with homogeneous high vascularization; a cyst (Fig. 7, middle) is visualized as a round structure with high concentration of blood vessels at the periphery of lesion; while an invasive ductal carcinoma (Fig. 7, bottom) shows an irregular mass with ill-defined margins, high concentration of blood vessels at the periphery of the mass, and a low concentrations of blood vessels at the center. These resolved features are not visually identifiable in the low-resolution.

Figure 7: Experimental results (reproduced from ) for applying LISTA for super-resolution in human scans of three lesions in breasts of three patients. Left: B-mode images; Right: super-resolution recoveries; Top: fibroadenoma (benign); Middle: cyst (benign); Bottom: invasive ductal carcinoma (malignant).

### VI-B Microscopy Imaging

Next, we demonstrate the application of model-based deep learning techniques in optics, considering again the usage of LISTA (applied in the correlation domain) for super-resolution. The context $x$ is a low resolution microscopy image, and $s^{true}$ is a high resolution image, with the decision rule being $K = 10$ iterations of ISTA (T4) where the parameters $\theta^{o}$ and $\theta^{h}$ are jointly learned from data to minimize the empirical risk with the $\ell_{2}$ loss as its design objective.

Experimental results of applying the deep unfolded mapping trained for super-resolution in microscopy imaging are depicted in Fig. 8, which is reproduced from based on the method from. Here, a super-resolved image is reconstructed from a simulated tubulins data set, composed of $350$ high-density frames, where the deep unfolded network (Fig. 8(c)) is compared with $100$ iterations of the model-based iterative sparse recovery algorithm from which it originates (Fig. 8(b)). These results demonstrate the ability of deep unfolding, where both the objective parameters $\theta^{o}$ and the hyperparameters $\theta^{h}$ are jointly learned end-to-end, to yield more abstract models that can overcome mismatches due to the surrogate objectives of model-based optimization with complex data, where mathematical descriptions are rarely accurate.

Figure 8: Sample results (reproduced from ) for applying deep unfolding for recovery of high resolution image. a) simulated ground truth tubulin structure; b) model-based recovery with hyperparameter θh = 0.25; c) deep unfolded resolved image.

### VI-C Digital Communications

The experimental evaluations so far focused on deep unfolding methodology and on tasks where the context $x$ is an image. We proceed to a different family of tasks, arising in the operation of digital receivers, and present a a numerical example for DNN-aided optimization. We consider a scenario of symbol detection over causal stationary communication channels with finite memory, reproduced from. Here, the input $x$ is a real valued vector representing samples from an observed channel output, and $s^{true}$ is a vector of the transmitted symbols, whose entries take value in a discrete binary phase shift keying constellation. The decision mapping which minimizes the error is the MAP rule which in such scenarios can be implemented with reduced complexity using the sum-product (SP) algorithm. This mapping relies on accurate knowledge of the underlying channel which is captured using a factor graph. The parameters of the decision rule are the weights of an internal DNN used for evaluating the function nodes of the graph, and these parameters are tuned by minimizing the empirical cross entropy loss on a data set comprised of observations and their corresponding symbols.

Figure 9: Experimental results from of learned factor graphs compared to the model-based SP and the sliding bidirectional RNN (SBRNN) of. Perfect CSI implies that the system is trained and tested using samples from the same channel, while in CSI uncertainty they are trained using samples from a set of different channels.

Fig. 9 depicts the numerically evaluated symbol error rate achieved by applying a DNN-aided SP algorithm where deep learning is used to learn to compute the function nodes of the factor graph from $n_{t} = 5000$ labeled samples. The results are compared to the performance of the model-based SP, that requires complete knowledge of the underlying statistical model, as well as the sliding bidirectional RNN detector proposed in for such setups, which utilizes a conventional DNN architecture. Fig. 9 demonstrates the ability of learned factor graphs to enable accurate message passing inference in a data-driven manner, as the performance achieved using learned factor graphs approaches that of the SP algorithm, which operates with full knowledge of the underlying statistical model. The numerical results also demonstrate that combining model-agnostic DNNs with model-aware optimization notably improves robustness to model uncertainty compared to applying the SP algorithm with the inaccurate model. Furthermore, it also observed that the principled incorporation of DNNs and SP inference allows to achieve improved performance compared to utilizing black-box DNN architectures such as the sliding bidirectional RNN detector, with limited training data.

### VI-D Tracking of Dynamic Systems

We conclude our experimental results with the application of DNN-aided optimization for tracking of dynamic systems. Here, we use the DNN-aided Kalman filter of Example 18 to track the Lorentz attractor non-linear chaotic system. Both the context and the decision are three-dimensional vectors, representing $3000$ noisy observations and the trajectory of the Lorenz attractor, respectively. The decision rule is a combination of a DNN (T5) and an affine mapping (T1) trained end-to-end from supervised data, as detailed in Example 18. We compare this model-based deep learning mapping with several model-based tracking algorithms designed for such settings -- the extended Kalman filter (EKF); unscented Kalman filter (UKF); and particle filter (PF) -- as well as to a black-box RNN trained end-to-end.

TABLE I: MSE performance and run-time of the DNN-aided KalmanNet, end-to-end RNN, and the model-based EKF, UKF, and PF.

The results, reproduced from are summarized in Table I, and a representative reconstruction is visualized in Fig. 10. It is observed in Table I that the gains of DNN-aided optimization here are two-fold: first, it achieves the best MSE results due to its incorporation of the state-space model as domain knowledge along with a DNN which learns to handle the complex dynamics and overcome the mismatches induced by the surrogate objective. Furthermore, the integration of deep learning allows DNN-aided optimization to operate more quickly than its model-based counterparts, as some of the internal exhaustive computations of the algorithms are replaced with a DNN inferring at fixed complexity.

Figure 10: Tracking a single trajectory of the Lorentz attractor chaotic system using the DNN-aided KalmanNet compared with the model-based EKF (reproduced from ).
