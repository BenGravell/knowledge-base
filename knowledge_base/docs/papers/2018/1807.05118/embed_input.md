<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tune: A Research Platform for Distributed Model Selection and Training

Topics include Distributed systems, Learning, Tune, Machine learning, Search algorithm.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modern machine learning algorithms are increasingly computationally demanding, requiring specialized hardware and distributed computation to achieve high performance in a reasonable time frame. Many hyperparameter search algorithms have been proposed for improving the efficiency of model selection, however their adaptation to the distributed compute environment is often ad-hoc. We propose Tune, a unified framework for model selection and training that provides a narrow-waist interface between training scripts and search algorithms. We show that this interface meets the requirements for a broad range of hyperparameter search algorithms, allows straightforward scaling of search to large clusters, and simplifies algorithm implementation. We demonstrate the implementation of several state-of-the-art hyperparameter search algorithms in Tune. Tune is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Machine learning pipelines are growing in complexity and cost. In particular, the model selection stage, which includes model training and hyperparameter tuning, can take the majority of a machine learning practitioner's time and consume vast amounts of computational resources. Take for example a researcher aiming to train ResNet-101, a convolutional neural-network model with millions of parameters. Training this model can take around 24 hours on a single GPU, and performing model selection sequentially will take weeks to complete. Naturally, one would be inclined to train the model on a cluster in a distributed fashion (Goyal et al. ) and utilize many machines to perform model selection in parallel.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, the research community has developed numerous techniques for accelerating model selection including those that are sequential (Snoek et al. ), parallel (Li et al. ), and both (Jaderberg et al. ). However, each technique is often implemented on its own, tied to a particular framework, is closed source, or perhaps not even reproducible without significant computational resources (Zoph and Le ). Further, often times these techniques require significant investment in software infrastructure for the execution of experiments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Tune, an open source framework for distributed model selection.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show how Tune's APIs enable the easy reproduction and integration of a wide variety of state-of-the-art hyperparameter search algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

We refer to a trial as a single training run with a fixed initial hyperparameter configuration. An experiment (similar to a "Study" in Vizier), is a collection of trials supervised by Tune using one of its trial scheduling algorithms (which implement model selection).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

A platform for model search and training blends both sequential and parallel computation. During search, many trials are evaluated in parallel. Hyperparameter search algorithms examine trial results in sequence and make decisions that affect the parallel computation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

Ability to handle irregular computations: Trials often vary in length and resource usage.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

Ability to handle resource requirements of arbitrary user code and third-party libraries. This includes parallelism and the use of hardware resources such as GPUs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

Ability to make search / scheduling decisions based on intermediate trial results. For example, genetic algorithms commonly clone or mutate model parameters in the middle of training. Algorithms that perform early stopping also use intermediate results to make stopping decisions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

The monitoring and visualization of trial progress and outcomes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

Simple integration and specification of the experiment to execute.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Requirements for API generality", "weight": 1.0} -->

To meet these requirements, we propose the Tune user-facing and scheduling APIs (Section 4) and implement it on the Ray distributed computing framework (Moritz et al. ). The Ray framework provides the underlying distributed execution and resource management. Its flexible task and actor abstractions allow Tune to schedule irregular computations and make decisions based on intermediate results.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tune API", "weight": 1.0} -->

Tune provides two development interfaces: a user API for users seeking to train models and a scheduling API for researchers interested in improving the model search process itself. As a consequence of this division, users of Tune have a choice of many search algorithms. Symmetrically, the scheduler API enables researchers to easily target a diverse range of workloads and provides a mechanism for making their algorithms available to users.

<!-- chunk {"id": "body-0016", "role": "body", "section": "User API", "weight": 1.0} -->

Model training scripts are commonly implemented as a loop over a model improvement step, with results periodically logged to the console (e.g., every training epoch). To support the full range of model search algorithms, Tune requires access to intermediate training results, the ability to snapshot training state, and also the ability to alter hyperparameters in the middle of training. These requirements can be met with minimal modifications to existing user code via a cooperative control model.

<!-- chunk {"id": "body-0017", "role": "body", "section": "User API", "weight": 1.0} -->

[Function-based API] {subfigure}[Class-based API]
Figure 2: Tune offers both a function-based cooperative control API and a class-based API that allows for direct control over trial execution. Either can be adopted by the user to enable control over model training via Tune’s trial schedulers.

<!-- chunk {"id": "body-0018", "role": "body", "section": "User API", "weight": 1.0} -->

Consider a typical model training script as shown in 2. A handle to Tune is passed into the function. To integrate with Tune, the model and optimizer hyperparameters are pulled from the tune.params map, checkpoints are created when tune.should_checkpoint returns positive, and the saved checkpoint file is passed to tune.record_checkpoint. Intermediate results are reported via tune.report. These cooperative calls enable Tune scheduling algorithms to monitor the training progress of each trial (via the reported metrics), save and clone promising parameters (via checkpoint and restore), and alter hyperparameters at runtime (by restoring a checkpoint with a changed hyperparameter map). Critically, these calls require minimal changes to existing user code.

<!-- chunk {"id": "body-0019", "role": "body", "section": "User API", "weight": 1.0} -->

Tune can also directly control trial execution if the user extends the trainable model class (Figure 2). Here, training steps, checkpointing, and restore are implemented as class methods which Tune schedulers call to incrementally train models. This mode of execution has some debuggability advantages over cooperative control; we offer both to users. Internally, Tune inserts adapters over the cooperative interface to provide a facade of direct control to trial schedulers.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

Given the ability to create trials and control their execution, the next question is how trials should be scheduled. Tune's trial schedulers operate over a set of possible trials to run, prioritizing trial execution given available cluster resources. In addition, they can add to the list of trials to execute (e.g., based on suggestions from HyperOpt).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

The simplest trial scheduler executes trials sequentially, running each until a stopping condition is met. Trials are launched in parallel when sufficient resources are available in the cluster. However, this is not all trial schedulers can do.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

Early stop a trial that is not performing well based on its intermediate results.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

Adjust the annealing of hyperparameters such as learning rate.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

Clone the parameters of a promising trial and launch additional trials that explore the nearby hyperparameter space.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

Query a shared database of trial results to choose promising hyperparameters.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

Prioritize resource allocation between a large number of trials, more than can run concurrently given available resources.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y2xhc3MgVHJpYWxTY2hlZHVsZXI6CiAgICBkZWYgb25fcmVzdWx0KHNlbGYsIHRyaWFsLCByZXN1bHQpOiAuLi4KICAgIGRlZiBjaG9vc2VfdHJpYWxfdG9fcnVuKHNlbGYpOiAuLi4=){download=""}

<!-- chunk {"id": "body-0028", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

def on_result(self, trial, result): \.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

def choose_trial_to_run(self): \.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

The interface is event based. When Tune has resources available, it calls scheduler.choose_trial_to_run to get a trial to launch on the cluster. As results for the trial become available, the scheduler.on_result callback is invoked and the scheduler returns an flag indicating whether to continue, checkpoint, stop, or restart a trial with an updated hyperparameter configuration. This interface is sufficient to provide a broad range of hyperparameter tuning algorithms including Median Stopping Rule (Golovin et al. ), Bayesian Optimization approaches (Bergstra et al. ), HyperBand (Li et al. ), and Population-based Training (Jaderberg et al. ).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scheduler API", "weight": 1.0} -->

We note that Tune keeps the metadata for active trials in memory and relies on checkpoints for fault tolerance. This drastically simplifies the design of trial schedulers and is not a limitation in practice. Trial scheduler implementations are free to leverage external storage if necessary.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Putting it together", "weight": 1.0} -->

To launch an experiment, the user must specify their model training function or class (Figures 1 and 2), an initial set of trials, and a trial scheduler.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Putting it together", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZGVmIG15X2Z1bmMoKTogLi4uCnR1bmUucnVuX2V4cGVyaW1lbnRzKG15X2Z1bmMsIHsKICAgICJsciI6IHR1bmUuZ3JpZF9zZWFyY2goWzAuMDEsIDAuMDAxLCAwLjAwMDFdKSwKICAgICJhY3RpdmF0aW9uIjogdHVuZS5ncmlkX3NlYXJjaChbInJlbHUiLCAidGFuaCJdKSwKfSwgc2NoZWR1bGVyPUh5cGVyQmFuZCk=){download=""}

<!-- chunk {"id": "body-0034", "role": "body", "section": "Putting it together", "weight": 1.0} -->

\"activation\": tune.grid_search(\[\"relu\", \"tanh\"\]),

<!-- chunk {"id": "body-0035", "role": "body", "section": "Putting it together", "weight": 1.0} -->

Here, we use Tune's built-in DSL to specify a small $3 \times 2$ grid search over two hyperparameters. These serve as the initial set of trials input to the scheduler. Tune's parameter DSL offers features similar to those provided by HyperOpt (Bergstra et al. ). Alternatively, users can generate the list of initial trial configurations with the mechanism of their choice. Once an experiment is launched, the progress of trials is periodically reported in the console and can also be viewed through integrations such as TensorBoard.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Scaling computation", "weight": 1.0} -->

Each trial in Tune runs in its own Python process, and can be allocated given number of CPU and GPU resources through Ray. Individual trials can themselves leverage distributed computation by launching further subprocesses using Ray APIs. These child processes can coordinate with each other using Ray to e.g., perform SGD, or use collective communication primitives provided by libraries such as torch.distributed and Nvidia NCCL.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data input", "weight": 1.0} -->

Since each trial in Tune runs as a Ray task or actor, they can use Ray APIs to handle data ingest. For example, weights can be broadcast to all workers using ray.put(obj) to the Ray object store, and retrieved via ray.get(obj_id) during trial initialization.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation", "weight": 1.0} -->

We list in Table 1 currently implemented algorithms in Tune. Line counts include lines used for logging and debugging functionality. We implemented Tune using the Ray (Moritz et al. ) framework, which as noted earlier provides the actor abstraction used to run trials in Tune. In contrast to popular distributed frameworks such as Spark (Zaharia et al. ), or MPI (Gabriel et al. ), Ray offers a more flexible programming model. This flexibility enables Tune's trial schedulers to centrally control the many types of stateful distributed computations created by hyperparameter optimization algorithms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation", "weight": 1.0} -->

The Ray framework is also uniquely suited for executing nested computations (i.e., hyperparameter optimization) since it has a two-level distributed scheduler. In Ray, task scheduling decisions are typically made on the local machine when possible, only "spilling over" to other machines on the cluster when local resources are exhausted. This avoids any central bottleneck when distributing trial executions that may themselves leverage parallel computations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we explored the design of a general framework for hyperparameter tuning. We proposed the Tune API and System which supports extensible distributed hyperparameter search algorithms while also being easy for end-user model developers to incorporate into their model design processes. We are actively developing new functionality to help not only in the tuning process but also in analyzing and debugging the intermediate results.
