<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bayesian Hyperparameter Optimization with BoTorch, GPyTorch and Ax

Topics include Gaussian processes, Deep learning, Autoencoders, Bayesian methods, Graphs, Optimization, Learning, Bayesian hyperparameter optimization, Bayesian optimization, Hyperparameter optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep learning models are full of hyperparameters, which are set manually before the learning process can start. To find the best configuration for these hyperparameters in such a high dimensional space, with time-consuming and expensive model training / validation, is not a trivial challenge. Bayesian optimization is a powerful tool for the joint optimization of hyperparameters, efficiently trading off exploration and exploitation of the hyperparameter space. In this paper, we discuss Bayesian hyperparameter optimization, including hyperparameter optimization, Bayesian optimization, and Gaussian processes. We also review BoTorch, GPyTorch and Ax, the new open-source frameworks that we use for Bayesian optimization, Gaussian process inference and adaptive experimentation, respectively. For experimentation, we apply Bayesian hyperparameter optimization, for optimizing group weights, to weighted group pooling, which couples unsupervised tiered graph autoencoders learning and supervised graph prediction learning for molecular graphs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We find that Ax, BoTorch and GPyTorch together provide a simple-to-use but powerful framework for Bayesian hyperparameter optimization, using Ax's high-level API that constructs and runs a full optimization loop and returns the best hyperparameter configuration.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep learning models are full of hyperparameters (e.g., learning rate, number of layers, number of units per layer), which are set manually before the learning process can start. To find the best configuration for these hyperparameters in such a high dimensional space, with time-consuming and expensive model training / validation, is not a trivial challenge. There are four common methods for hyperparameter optimization, in order of increasing efficiency: manual, grid search, random search, and Bayesian optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bayesian optimization, a sequential model-based optimization, is a powerful tool for the joint optimization of hyperparameters, efficiently trading off exploration and exploitation of the hyperparameter space. It is best-suited for optimization over continuous domains of less than 20 hyperparameters, and tolerates stochastic noise in function evaluations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we discuss Bayesian hyperparameter optimization, including hyperparameter optimization, Bayesian optimization, and Gaussian processes. Our focus is on providing a concise and consistent description, highlighting essential aspects and mathematical representations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also review BoTorch, GPyTorch and Ax, the new open-source frameworks, built on top of PyTorch, that we use for Bayesian optimization, Gaussian process inference and adaptive experimentation (e.g., Bayesian hyperparameter optimization), respectively. BoTorch supports seamless integration with GPyTorch, and is best used in tandem with Ax.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For experimentation, we apply Bayesian hyperparameter optimization to weighted group pooling for optimizing group weights. Tiered graph autoencoders and graph prediction together provide effective, efficient and interpretable deep learning for molecular graphs, with the former providing unsupervised, transferable learning and the latter providing supervised, task-optimized learning. Tiered graph autoencoders learning and graph prediction learning are essentially separated, coupled only through weighted group pooling, which are parameterized by group weights.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Notations and Symbols", "weight": 1.0} -->

Vectors are in bold type. Matrices are capitalized and in bold type.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Hyperparameter Optimization", "weight": 1.0} -->

Deep learning models are full of hyperparameters (e.g., learning rate, number of layers, number of units per layer), which are set manually before the learning process can start. To find the best configuration for these hyperparameters in such a high dimensional space, with time-consuming and expensive model training / validation, is not a trivial challenge.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Hyperparameter Optimization", "weight": 1.0} -->

Hyperparameter optimization is represented in mathematical form as: where x is the vector of hyperparameters, X is the feasible set (domain), and f(x) is the objective score to minimize, evaluated on the validation set. In simple terms, the goal is to find the hyperparameters that yield the best score on the validation set metric. The problem with hyperparameter optimization is that evaluating the objective function f to find the score is extremely time-consuming and costly with a large number of hyperparameters and complex models, such as deep learning models, that involve time-consuming and expensive train-predict-evaluate cycles.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Hyperparameter Optimization", "weight": 1.0} -->

There are four common methods for hyperparameter optimization, in order of increasing efficiency: The manual method does not scale. Grid search is infeasible with more than 4 hyperparameters. Random search (and grid search) has the downside that each new guess is independent of the previous iteration and, therefore, the search is incapable of leveraging learning for improvement.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Hyperparameter Optimization", "weight": 1.0} -->

Bayesian optimization, on the other hand, efficiently trades off exploration and exploitation of the hyperparameter space to quickly guide the search into the configuration that best optimizes some overall evaluation criterion. Bayesian optimization is a sequential model-based optimization (SMBO), which has five key aspects: 1. A domain (input space) of hyperparameters. 2. An objective functi on which takes in hyperparameters and outputs a score that we want to minimize. 3. A surrogate model of the objective function. 4. A select function for evaluating which hyperparameters to select next from the surrogate model. 5. A history consisting of (hyperparameters, score) pairs used to update the surrogate model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

Bayesian optimization (BO) is a powerful tool for the joint optimization of hyperparameters, efficiently trading off exploration and exploitation of the hyperparameter space. It is best-suited for optimization over continuous domains of less than 20 hyperparameters, and tolerates stochastic noise in function evaluations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

BO focuses on solving the problem: where x is the input (e.g., hyperparameters), X is the feasible set (domain), and f is the objective function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

-  x ϵ R d for a value of d that is not too large. Typically d < 20. -  X is a simple set. Typically, X is a hyper-rectangle: a j <= xj <= bj. -  f is time-consuming and expensive to evaluate, a black-box, and derivative-free. -  f may be obscured by stochastic noise.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

BO consists of two main components: a probabilistic (surrogate) model for modeling the objective function, and an acquisition function that encodes a strategy for navigating the exploration vs. exploitation trade-off of the input space. We prescribe the Bayesian prior, p(f( x )), a prior belief (model) over the possible objective functions and then sequentially refine this model as data are observed via Bayesian posterior updating. The Bayesian posterior, p(f( x )| D ), represents our updated belief (model) -given data - on the likely objective functions we are optimizing. Given this probabilistic model, we can sequentially induce acquisition functions that leverage the uncertainty in the posterior to guide exploration. In short, BO builds a probabilistic model of the objective function and uses it to acquire the most promising input data to evaluate the true objective function. Our only recourse is to evaluate f at a sequence of inputs, with the hope of determining a near-optimal value after a small number of evaluations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Probabilistic (Surrogate) Models", "weight": 1.0} -->

For continuous objective functions, Bayesian optimization typically works by assuming the probabilistic model is a Gaussian process (prior) and maintains a posterior distribution as the results of evaluating objective functions are observed. Other choices for the probabilistic model include random forests and tree Parzen estimators (TPEs). Gaussian processes are flexible and powerful.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Probabilistic (Surrogate) Models", "weight": 1.0} -->

The Gaussian process (GP) is a convenient and powerful prior distribution on unknown functions of the form It is defined by the property that any finite set of N points induces a multivariate Gaussian distribution on R N. The i th of these points is taken to be the function value f(x i). We discuss Gaussian processes in Section 4 Gaussian Processes.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Acquisition Functions", "weight": 1.0} -->

We assume that the objective function f(x) is drawn from a surrogate Gaussian process prior, as discussed above, and that our observations (history) are of the form and σϵ 2 is the variance of noise introduced into the observations. This prior and these observations induce a posterior over functions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Acquisition Functions", "weight": 1.0} -->

We denote the acquisition function by It determines what point in X should be selected next via a proxy optimization: In general, acquisition functions depend on the previous observations, as well as the GP parameters θ (parameters of the GP kernel function, see 4 Gaussian Processes). We denote this dependence as Under the Gaussian process prior, acquisition functions depend on the model solely through its mean function and variance function Acquisition functions define a balance between exploring new areas in the objective function space and exploiting areas that are already known to have favorable values. A common strategy is to maximize the expected improvement (EI) over the current best result. This has closed form under the Gaussian process: Other strategies include probability improvement and GP upper confidence bound. EI is better-behaved than probability of improvement and, unlike GP upper confidence bound, it does not require its own tuning parameters.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gaussian Processes", "weight": 1.0} -->

The Gaussian process is a well-known non-parametric and interpretable Bayesian probabilistic model. A Gaussian process is a generalization of the Gaussian distribution. Whereas a probability distribution describes random variables which are scalars or vectors, a stochastic process governs the properties of functions. We can loosely think of a function as an infinite vector, each entry in the vector specifying the function value f(x i) at a particular input x i. A key aspect of this is that if we ask only for the properties of the function at a finite number of points, then GP inference will give us the same answer if we ignore the infinitely many other points.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Gaussian Processes", "weight": 1.0} -->

In the function-space view a Gaussian process defines a distribution over functions, and inference takes place directly in the space of functions. A Gaussian process is completely specified by its mean function (average of all functions) and kernel (covariance) function (how much individual functions can vary around the mean function): As such, we write the Gaussian process as Under the Gaussian process, the true objective is modeled by a GP prior with a mean and a kernel function. Given a set of (noisy) observations from initial evaluations, a Bayesian posterior update gives the GP posterior with an updated mean and kernel function. The mean function of the GP posterior gives the best predictions at any point conditional on the available observations, and the kernel function quantifies the uncertainty in the predictions. The GP prior is a multivariate Gaussian distribution: In the above, θ is GP parameters (parameters of the GP kernel function).

<!-- chunk {"id": "body-0024", "role": "body", "section": "BoTorch, GPyTorch and Ax", "weight": 1.0} -->

BoTorch, GPyTorch, and Ax are new open-source frameworks, built on top of PyTorch, for Bayesian optimization, Gaussian process inference, and adaptive experimentation (e.g., Bayesian hyperparameter optimization), respectively. BoTorch supports seamless integration with GPyTorch, and is best used in tandem with Ax.

<!-- chunk {"id": "body-0025", "role": "body", "section": "BoTorch", "weight": 1.0} -->

BoTorch is a scalable framework for Bayesian optimization, enabled by analytic and Monte-Carlo (MC) acquisition functions and auto-differentiation. Its modular design facilitates flexible specification and optimization of probabilistic models, and simplifies implementation of novel acquisition functions. BoTorch provides seamless integration with PyTorch modules, enabling joint training of GP and neural network modules and allowing end-to-end gradient-based optimization of acquisition functions operating on differentiable models.

<!-- chunk {"id": "body-0026", "role": "body", "section": "BoTorch", "weight": 1.0} -->

BoTorch provides abstractions for (combining) BO primitives, enabling BO with auto-differentiation, automatic parallelization, device-agnostic hardware acceleration, and generic neural network operators and modules.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model", "weight": 1.0} -->

The Model is an abstraction for a probabilistic (surrogate) model (see 3.1 Probabilistic (Surrogate) Models). A Model maps a set of inputs to a posterior distribution of its outputs. It requires only a single posterior method that returns a Posterior object describing the posterior distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model", "weight": 1.0} -->

BoTorch is model-agnostic - the only requirement for a model is that, given a set of inputs, it can produce posterior draws of one or more outputs. Explicit posteriors, such as those provided by a GP, can be used directly. BoTorch provides a simple Posterior API that only requires implementing an rsample method for sampling from the posterior. A Posterior can be any distribution (even an implicit one), so long as one can sample from that distribution.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model", "weight": 1.0} -->

BoTorch provides first-class support for state-of-the-art probabilistic models in GPyTorch (see 5.2 GPyTorch). This includes support for multi-task GPs, deep kernel learning, deep GPs, and approximate inference. BoTorch provides several GPyTorch models to cover most standard BO use cases. GPyTorchModel provides a base class for conveniently wrapping GPyTorch models. For these models, GPyTorchPosterior should be used.

<!-- chunk {"id": "body-0030", "role": "body", "section": "AcquisitionFunction", "weight": 1.0} -->

The AcquisitionFunction is an abstraction for the acquisition function (see 3.2 Acquisition Functions). It implements a forward pass that takes a candidate input x and computes their acquisition function α( x ). Analytic AcquisitionFunctions operate on the explicit posterior (e.g., GP), whereas MC-based AcquisitionFunctions operate on samples from the posterior evaluated under the Objective.

<!-- chunk {"id": "body-0031", "role": "body", "section": "AcquisitionFunction", "weight": 1.0} -->

The idea behind MC-based AcquisitionFunctions is simple: instead of computing an (intractable) expectation over the posterior, we sample from the posterior and use the sample average as an approximation. All MC-based AcquisitionFunctions are derived from MCAcquisitionFunction. Any Posterior object can be used with an MCAcquisitionFunction.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Objective", "weight": 1.0} -->

The Objective allows for convenient Objectives are derived from transformation MCAcquisitionObjective of Model outputs into a scalar function to be optimized. All. BoTorch implements several MC-based Objectives, including LinearMCObjective for linear combinations of model outputs, and ConstrainedMCObjective for constrained objectives.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimizer", "weight": 1.0} -->

The optimizer finds in order to proceed with the next iteration of BO. Auto-differentiation makes it straightforward to use gradient-based optimization, which typically performs better than derivative-free approaches.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimizer", "weight": 1.0} -->

Optimization over N inputs in a d-dimensional hyperparameter space results in Nd scalar hyperparameters. Both N and d are often small compared to deep learning inputs and model parameters, respectively. As such, BoTorch provides a custom interface that wraps the optimizers from the scipy.optimize module, since these can be used but are not in the torch.optim module.

<!-- chunk {"id": "body-0035", "role": "body", "section": "GPyTorch", "weight": 1.0} -->

GPyTorch is a framework for scalable GP inference and Bayesian deep learning. GPyTorch uses Blackbox Matrix-Matrix multiplication (BBMM) for GP inference. BBMM reduces the asymptotic complexity of GP inference from O (n 3 ) to O (n 2 ). In addition, BBMM effectively uses GPU hardware to accelerate both GP inference and scalable approximations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "GPyTorch", "weight": 1.0} -->

GPytorch supports both exact GP inference and variational GP inference. Exact GP inference is supported via the ExactGP model; variational GP inference is supported via the ApproximateGP model. The easiest way to use the BoTorch GPyTorchModel, discussed earlier, is to subclass a model from it and a GPyTorch model (e.g. an ExactGP). Such is the case for the BoTorch SingleTaskGP model, which works with independent output(s) and all outputs using the same training data, as well as the BoTorch Fixed NoiseGP model, a single-task exact GP that uses fixed observation noise levels.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Ax", "weight": 1.0} -->

Ax is a framework for adaptive experimentation that automates the process of sequential optimization (e.g., Bayesian optimization ). It provides an easy-to-use interface for defining, managing and running sequential experiments, while handling metadata management, transformations, and systems integration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Components", "weight": 1.0} -->

In Ax, an Experiment keeps track of the whole optimization process. It contains a search space, optimization configuration, metadata, information on what metrics to track, and how to run iterations, etc.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Components", "weight": 1.0} -->

A SearchSpace is composed of a set of Parameters to be optimized in the Experiment, and optionally a set of parameter constraints. Each Parameter has a name, a type (int, float, bool, or string), and a domain. There are three kinds of Parameter: RangeParameter, ChoiceParameter and FixedParameter.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Components", "weight": 1.0} -->

An Arm is a set of Parameters and their values with a name attached to it. In the case of hyperparameter optimization, an Arm corresponds to a hyperparameter configuration explored in the course of a given optimization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Components", "weight": 1.0} -->

An experiment consists of a sequence of Trials, each of which evaluates one or more Arms. Based on the evaluation results, the optimization algorithm suggests one or more Arms to evaluate. A Trial is added to the Experiment when a new Arm (or Arms) is proposed by the optimization algorithm. A Trial goes through multiple phases during the experimentation cycle, tracked by its TrialStatus field.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Components", "weight": 1.0} -->

An OptimizationConfig is composed of an Objective with Metric to be minimized or maximized, and optionally a set of outcome constraints. The Metric provides an interface for fetching data for a Trial. All Metric classes must implement the method fetch\_trial\_data, which accepts a Trial and returns an instance of Data. Each row of the final Data object represents the evaluation of an Arm on a Metric.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Models", "weight": 1.0} -->

The Model represents a probabilistic (surrogate) model and predicts the outcomes of Metrics evaluated at an Arm. All Models share a common API with predict to make predictions at new Arms and gen to generate candidate Arms to be evaluated. Models are created using factory functions from the ax.modelbridge.factory. In particular, the get\_botorch function instantiates a BotorchModel, to be discussed later.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Models", "weight": 1.0} -->

All Models can be used with the built-in plotting utilities, which can produce plots of model predictions on 1-d or 2-d slices of the parameter space. Ax also includes utilities for cross validation to assess model predictive performance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Models", "weight": 1.0} -->

Ax uses a bridge design to provide a unified interface for models. The modeling stack consists of two layers: the ModelBridge and the Model. The ModelBridge is the object that is directly used in Ax: model factories return ModelBridge objects, and plotting and cross validation tools operate on a ModelBridge. Model objects are only used via a ModelBridge. The primary role of the ModelBridge is to act as a transformation layer. This includes transformations to the data, search space, and optimization configuration, as well as the final transform from Ax objects into the objects consumed by the Model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ax with BoTorch", "weight": 1.0} -->

Ax relies on BoTorch for implementing Bayesian optimization algorithms. It provides a BotorchModel that is a default for modeling and optimization, which can be customized by specifying and passing in model constructors, acquisition functions, and optimization strategies. This TorchModelBridge, for BotorchModel, utilizes a number of built-in transformations, such as normalizing inputs and outputs to ensure reasonable fitting of GPs. GPs are used for Bayesian optimization in Ax. The get\_GPEI function constructs a model that fits a GP to the data, and uses the BoTorch ExpectedImprovement acquisition function to generate new points.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The optimize Function", "weight": 1.0} -->

Ax provides a simple-to-use but powerful API for Bayesian hyperparameter optimization, optimize, which constructs and runs a full OptimizationLoop, given hyperparameters and an evaluation function, and returns the best hyperparameter configuration. The OptimizationLoop creates a SimpleExperiment with the evaluation function and an associated SearchSpace with the hyperparameters. By default, the OptimizationLoop uses 20 Trials per SimpleExperiment and 1 Arm per Trial.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The optimize Function", "weight": 1.0} -->

When a SimpleExperiment is constructed, it creates an OptimizationConfig with an Objective and a Metric. To run a trial, a SimpleExperiment first fetches the trial data (an instance of Data ) for the previous existing Trial, and creates a new Trial with the trial data and pending observations. The generation strategy uses Sobol for the first 5 Arms and GPEI for subsequent Arms. Iterations after 5 will take longer to generate due to model-fitting.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The optimize Function", "weight": 1.0} -->

In addition to the best hyperparameter configuration, the optimize function also returns the TorchModelBridge used, with its associated BotorchModel. By default, this model uses a noisy ExpectedImprovement acquisition function on top of a model made up of separate GPs, one for each outcome.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Bayesian Hyperparameter Optimization Applied to Weighted Group Pooling 6.1 Tiered Graph Autoencoders with Graph Prediction", "weight": 1.0} -->

Tiered graph autoencoders provide the most direct and effective architecture and mechanisms for generating hierarchical representations (embeddings) of molecular graphs since they are based on the direct representation and utilization of groups. With tiered graph autoencoders, we use tiered graph embeddings for molecular graph prediction, as shown below: In the diagram, M is the graph membership matrix. Based on DiffGroupPool, we have where Z is the group embeddings and X is the initial graph embeddings. wg, i is the group weight for group i in the graph membership matrix M.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Weighted Group Pooling", "weight": 1.0} -->

To use tiered graph autoencoders with graph prediction we introduce the group weight wg, i to represent and account for the different importance of group i for predicting different target molecular property / activity.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Weighted Group Pooling", "weight": 1.0} -->

-  wg, i = wFG if i is a FG (functional group), -  wg, i = wRG if i is a RG (ring group), -  wg, i = wCCG if i is a CCG (connected-component group).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Weighted Group Pooling", "weight": 1.0} -->

Using (variable) group weights wg, i in the graph membership matrix M amounts to weighted group pooling. Weighted group pooling thus serves as the link / coupling between (unsupervised) tiered graph autoencoders and (supervised) graph prediction, enabling task-independent node and group embeddings, generated using tiered graph autoencoders, to be used to build task-optimized graph embeddings, generated using graph prediction for specific target molecular properties / activities.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Hyperparameter Optimization for Group Weights", "weight": 1.0} -->

To optimize group weights based on the results of graph prediction learning, we treat group weights as hyperparameters and use hyperparameter optimization to accomplish it. Optimization of group weights is separate from learning of graph prediction, but depends on the latter's results.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Hyperparameter Optimization for Group Weights", "weight": 1.0} -->

In this approach, we use graph embeddings, generated using tiered graph autoencoders at Tier 3, as input for graph prediction (see 6.1 Tiered Graph Autoencoders with Graph Prediction). Note that graph embeddings depend on M and therefore on group weights. They need to be regenerated whenever a new configuration of group weights is selected in the hyperparameter optimization process. Group embeddings (and node embedding) are used in the generation of graph embeddings, but need to be generated only once for a dataset, independent of graph prediction and hyperparameter optimization, greatly reducing their computational cost and execution time.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Hyperparameter Optimization for Group Weights", "weight": 1.0} -->

For group weights optimization, we need to select a strategy (e.g., Bayesian Optimization) for group weights (hyperparameters) search, based on the strategy, design a set, or sets, of group weights to use, generate graph embeddings for the designed set(s) of group weights, perform a target-specific graph prediction learning for each generated graph embedding, determine the optimal set of group weights that produce the best graph prediction results for the target, and repeat from step 2, if the strategy calls, until a termination condition is reached.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Group Weights Optimization Using Ax, BoTorch and GPyTorch", "weight": 1.0} -->

Based on earlier discussions on hyperparameter optimization, we select Bayesian optimization with Gaussian processes for group weights (hyperparameters) optimization. In particular, we select Ax, BoTorch and GPyTorch as the unified framework to use for Bayesian hyperparameter optimization.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Group Weights Optimization Using Ax, BoTorch and GPyTorch", "weight": 1.0} -->

Ax provides the optimize function to construct and run a full OptimizationLoop, and to return the best hyperparameter configuration.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Group Weights Optimization Using Ax, BoTorch and GPyTorch", "weight": 1.0} -->

-  hyperparameters: wFG, wRG, wCCG -  evaluation function: train\_evaluate -  total trials (default: 20) The evaluation function evaluates the objective function f(x) given a hyperparameter configuration x.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Group Weights Optimization Using Ax, BoTorch and GPyTorch", "weight": 1.0} -->

The evaluation function, train\_evaluate(parametrization) 2. train(training dataset) 3. evaluate(validation dataset) The hyperparameter configuration Given a hyperparameter configuration, the (parametrization) is automatically generated by Ax for each Trial during a full run of the function generates graph embeddings graph autoencoders and pre-generated / saved group embeddings, as discussed previously. The graph prediction MLP, given the training dataset that contains graph embeddings. The validation dataset given the trained graph prediction MLP, and returns the For the feasibility study we use the QM9 dataset which has 133K drug-like organic molecules and 12 target molecular properties. Initially, we used (80% training, 10% validation, 10% test) and For each target molecular property, we did two runs and the best hyperparameter configurations obtained are shown as the first two results in the table that follows. We then increased the sample size to obtained is shown as the third result. We finally also increased the number of configuration obtained is shown as the. The best hyperparameter configuration. The best hyperparameter.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Group Weights Optimization Using Ax, BoTorch and GPyTorch", "weight": 1.0} -->

For each target molecular property, it corresponds to the hyperparameter configuration (in bold) obtained by the feasibility study. function trains the function evaluates the which serves as the objective, that we provide has three components: | Target Molecular Property | w FG | w RG | w CCG | As an aside, we observe that different types of groups (FG, RG, and CCG) have different significance in predicting different molecular properties. Therefore, it is important to explicitly represent and utilize groups and group weights in deep learning for molecular graphs.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Summary and Conclusion", "weight": 1.0} -->

In this paper, we discussed Bayesian hyperparameter optimization, including hyperparameter optimization, Bayesian optimization, and Gaussian processes. We also reviewed BoTorch, GPyTorch and Ax, the new open-source frameworks that we used for Bayesian optimization, Gaussian process inference and adaptive experimentation, respectively.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Summary and Conclusion", "weight": 1.0} -->

For experimentation, we applied Bayesian hyperparameter optimization, for optimizing group weights, to weighted group pooling, which couples unsupervised tiered graph autoencoders learning and supervised graph prediction learning for molecular graphs.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Summary and Conclusion", "weight": 1.0} -->

We find that Ax, BoTorch and GPyTorch together provide a simple-to-use but powerful framework for Bayesian hyperparameter optimization, using Ax's high-level API that constructs and runs a full optimization loop and returns the best hyperparameter configuration.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Summary and Conclusion", "weight": 1.0} -->

As an aside, we find that different types of groups have different significance in predicting different molecular properties. Therefore, it is important to explicitly represent and utilize groups and group weights in deep learning for molecular graphs.
