## Introduction

Machine learning pipelines are growing in complexity and cost. In particular, the model selection stage, which includes model training and hyperparameter tuning, can take the majority of a machine learning practitioner's time and consume vast amounts of computational resources. Take for example a researcher aiming to train ResNet-101, a convolutional neural-network model with millions of parameters. Training this model can take around 24 hours on a single GPU, and performing model selection sequentially will take weeks to complete. Naturally, one would be inclined to train the model on a cluster in a distributed fashion (Goyal et al. ) and utilize many machines to perform model selection in parallel.

To this end, the research community has developed numerous techniques for accelerating model selection including those that are sequential (Snoek et al. ), parallel (Li et al. ), and both (Jaderberg et al. ). However, each technique is often implemented on its own, tied to a particular framework, is closed source, or perhaps not even reproducible without significant computational resources (Zoph and Le ). Further, often times these techniques require significant investment in software infrastructure for the execution of experiments.

Figure 1: Tune provides narrow-waist interfaces that training scripts can implement with a few lines of code changes. Once done, this enables the use of Tune for experiment management, result visualization, and a choice of trial scheduling strategies. This narrow interface also enables AutoML researchers to easily swap out different search algorithms for comparison, or release distributed implementations of new algorithms without needing to worry about distributed scaffolding.

The contributions of this paper are as follows:

We introduce Tune, an open source framework for distributed model selection.

We show how Tune's APIs enable the easy reproduction and integration of a wide variety of state-of-the-art hyperparameter search algorithms.

## Related work

There are multiple open source systems for model selection.

HyperOpt, Spearmint, and HPOLib (Snoek et al.; Eggensperger et al. ) are distributed model selection tools that manage both the search and evaluation of the model, implementing search techniques such as random search and tree of parzen estimators (TPE). However, both frameworks are tightly coupled to the search algorithm structure and requires manual management of computational resources across a cluster. Further, systems such as Spearmint, HyperOpt, and TuPAQ (MLBase) (Sparks et al. ) treat a full trial execution as an atomic unit, which does not allow for intermediate control of trial execution. This inhibits efficient usage of cluster resources and also does not provide the expressivity needed to support algorithms such as HyperBand.

Google Vizier (Golovin et al. ) is a Google-internal service that provides model selection capabilities. Similar to Tune, Vizier provides parallel evaluation of trials, hosts many state-of-the-art optimization algorithms, provides functionality for performance analysis. However, it is first and foremost a service and is tied to closed-source infrastructure.

Mistique (Vartak et al. ) is also a system that addresses model selection. However, rather than focusing on the execution of the selection process, Mistique focuses on model debugging, emphasizing iterative procedures and memory footprint minimization.

Finally, Auto-SKLearn (Feurer et al. ) and Auto-WEKA (Thornton et al. ) are systems for automating model selection, integrating meta learning and ensembling into a single system. The focus of these systems is at the execution layer rather than the algorithmic level. This implies that in principle, it would be possible to implement Auto-WEKA and Auto-SKLearn on top of Tune, providing distributed execution of these AutoML components. Further, both Auto-SKLearn and Auto-WEKA are tied to Scikit-Learn and WEKA respectively as the only machine learning frameworks supported.

## Requirements for API generality

We refer to a trial as a single training run with a fixed initial hyperparameter configuration. An experiment (similar to a "Study" in Vizier), is a collection of trials supervised by Tune using one of its trial scheduling algorithms (which implement model selection).

A platform for model search and training blends both sequential and parallel computation. During search, many trials are evaluated in parallel. Hyperparameter search algorithms examine trial results in sequence and make decisions that affect the parallel computation. In order to support both a broad range of training workloads and selection algorithms, a framework for model search needs to meet the following requirements:

Ability to handle irregular computations: Trials often vary in length and resource usage.

Ability to handle resource requirements of arbitrary user code and third-party libraries. This includes parallelism and the use of hardware resources such as GPUs.

Ability to make search / scheduling decisions based on intermediate trial results. For example, genetic algorithms commonly clone or mutate model parameters in the middle of training. Algorithms that perform early stopping also use intermediate results to make stopping decisions.

For a good user experience, the following features are also necessary:

The monitoring and visualization of trial progress and outcomes.

Simple integration and specification of the experiment to execute.

To meet these requirements, we propose the Tune user-facing and scheduling APIs (Section 4) and implement it on the Ray distributed computing framework (Moritz et al. ). The Ray framework provides the underlying distributed execution and resource management. Its flexible task and actor abstractions allow Tune to schedule irregular computations and make decisions based on intermediate results.

## Tune API

Tune provides two development interfaces: a user API for users seeking to train models and a scheduling API for researchers interested in improving the model search process itself. As a consequence of this division, users of Tune have a choice of many search algorithms. Symmetrically, the scheduler API enables researchers to easily target a diverse range of workloads and provides a mechanism for making their algorithms available to users.

### User API

Model training scripts are commonly implemented as a loop over a model improvement step, with results periodically logged to the console (e.g., every training epoch). To support the full range of model search algorithms, Tune requires access to intermediate training results, the ability to snapshot training state, and also the ability to alter hyperparameters in the middle of training. These requirements can be met with minimal modifications to existing user code via a cooperative control model.

[Function-based API] {subfigure}[Class-based API]
Figure 2: Tune offers both a function-based cooperative control API and a class-based API that allows for direct control over trial execution. Either can be adopted by the user to enable control over model training via Tune’s trial schedulers.

Consider a typical model training script as shown in 2. A handle to Tune is passed into the function. To integrate with Tune, the model and optimizer hyperparameters are pulled from the tune.params map, checkpoints are created when tune.should_checkpoint() returns positive, and the saved checkpoint file is passed to tune.record_checkpoint(). Intermediate results are reported via tune.report(). These cooperative calls enable Tune scheduling algorithms to monitor the training progress of each trial (via the reported metrics), save and clone promising parameters (via checkpoint and restore), and alter hyperparameters at runtime (by restoring a checkpoint with a changed hyperparameter map). Critically, these calls require minimal changes to existing user code.

Tune can also directly control trial execution if the user extends the trainable model class (Figure 2). Here, training steps, checkpointing, and restore are implemented as class methods which Tune schedulers call to incrementally train models. This mode of execution has some debuggability advantages over cooperative control; we offer both to users. Internally, Tune inserts adapters over the cooperative interface to provide a facade of direct control to trial schedulers.

### Scheduler API

Given the ability to create trials and control their execution, the next question is how trials should be scheduled. Tune's trial schedulers operate over a set of possible trials to run, prioritizing trial execution given available cluster resources. In addition, they can add to the list of trials to execute (e.g., based on suggestions from HyperOpt).

The simplest trial scheduler executes trials sequentially, running each until a stopping condition is met. Trials are launched in parallel when sufficient resources are available in the cluster. However, this is not all trial schedulers can do. They can:

Early stop a trial that is not performing well based on its intermediate results.

Adjust the annealing of hyperparameters such as learning rate.

Clone the parameters of a promising trial and launch additional trials that explore the nearby hyperparameter space.

Query a shared database of trial results to choose promising hyperparameters.

Prioritize resource allocation between a large number of trials, more than can run concurrently given available resources.

The primary interface for a trial scheduler is as follows:

[⬇](data:text/plain;base64,Y2xhc3MgVHJpYWxTY2hlZHVsZXI6CiAgICBkZWYgb25fcmVzdWx0KHNlbGYsIHRyaWFsLCByZXN1bHQpOiAuLi4KICAgIGRlZiBjaG9vc2VfdHJpYWxfdG9fcnVuKHNlbGYpOiAuLi4=){download=""}

def on_result(self, trial, result): \...

def choose_trial_to_run(self): \...

The interface is event based. When Tune has resources available, it calls scheduler.choose_trial_to_run() to get a trial to launch on the cluster. As results for the trial become available, the scheduler.on_result() callback is invoked and the scheduler returns an flag indicating whether to continue, checkpoint, stop, or restart a trial with an updated hyperparameter configuration. This interface is sufficient to provide a broad range of hyperparameter tuning algorithms including Median Stopping Rule (Golovin et al. ), Bayesian Optimization approaches (Bergstra et al. ), HyperBand (Li et al. ), and Population-based Training (Jaderberg et al. ).

We note that Tune keeps the metadata for active trials in memory and relies on checkpoints for fault tolerance. This drastically simplifies the design of trial schedulers and is not a limitation in practice. Trial scheduler implementations are free to leverage external storage if necessary.

### Putting it together

To launch an experiment, the user must specify their model training function or class (Figures 1 and 2), an initial set of trials, and a trial scheduler. The following is a minimal example:

[⬇](data:text/plain;base64,ZGVmIG15X2Z1bmMoKTogLi4uCnR1bmUucnVuX2V4cGVyaW1lbnRzKG15X2Z1bmMsIHsKICAgICJsciI6IHR1bmUuZ3JpZF9zZWFyY2goWzAuMDEsIDAuMDAxLCAwLjAwMDFdKSwKICAgICJhY3RpdmF0aW9uIjogdHVuZS5ncmlkX3NlYXJjaChbInJlbHUiLCAidGFuaCJdKSwKfSwgc2NoZWR1bGVyPUh5cGVyQmFuZCk=){download=""}

tune.run_experiments(my_func, {

\"lr\": tune.grid_search(\[0.01, 0.001, 0.0001\]),

\"activation\": tune.grid_search(\[\"relu\", \"tanh\"\]),

Here, we use Tune's built-in DSL to specify a small $3 \times 2$ grid search over two hyperparameters. These serve as the initial set of trials input to the scheduler. Tune's parameter DSL offers features similar to those provided by HyperOpt (Bergstra et al. ). Alternatively, users can generate the list of initial trial configurations with the mechanism of their choice. Once an experiment is launched, the progress of trials is periodically reported in the console and can also be viewed through integrations such as TensorBoard.

### Scaling computation

Each trial in Tune runs in its own Python process, and can be allocated given number of CPU and GPU resources through Ray. Individual trials can themselves leverage distributed computation by launching further subprocesses using Ray APIs. These child processes can coordinate with each other using Ray to e.g., perform SGD, or use collective communication primitives provided by libraries such as torch.distributed and Nvidia NCCL.

### Data input

Since each trial in Tune runs as a Ray task or actor, they can use Ray APIs to handle data ingest. For example, weights can be broadcast to all workers using ray.put(obj) to the Ray object store, and retrieved via ray.get(obj_id) during trial initialization.

## Implementation

FIFO (trivial scheduler)

Median Stopping Rule

Population-Based Training (Jaderberg et al. )

Table 1: Model selection algorithms implemented (or integrated) in Tune. Two versions of HyperBand are implemented: the original formulation and the asynchronous variation which is simpler to implement in the distributed setting.

We list in Table 1 currently implemented algorithms in Tune. Line counts include lines used for logging and debugging functionality. We implemented Tune using the Ray (Moritz et al. ) framework, which as noted earlier provides the actor abstraction used to run trials in Tune. In contrast to popular distributed frameworks such as Spark (Zaharia et al. ), or MPI (Gabriel et al. ), Ray offers a more flexible programming model. This flexibility enables Tune's trial schedulers to centrally control the many types of stateful distributed computations created by hyperparameter optimization algorithms.

The Ray framework is also uniquely suited for executing nested computations (i.e., hyperparameter optimization) since it has a two-level distributed scheduler. In Ray, task scheduling decisions are typically made on the local machine when possible, only "spilling over" to other machines on the cluster when local resources are exhausted. This avoids any central bottleneck when distributing trial executions that may themselves leverage parallel computations.

## Conclusion and Future Work

In this work, we explored the design of a general framework for hyperparameter tuning. We proposed the Tune API and System which supports extensible distributed hyperparameter search algorithms while also being easy for end-user model developers to incorporate into their model design processes. We are actively developing new functionality to help not only in the tuning process but also in analyzing and debugging the intermediate results.
