<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RLlib: Abstractions for Distributed Reinforcement Learning

Topics include Reinforcement learning, Scalability, Distributed systems, Control, Learning, RLlib, Distributed reinforcement learning, Abstraction.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning (RL) algorithms involve the deep nesting of highly irregular computation patterns, each of which typically exhibits opportunities for distributed computation. We argue for distributing RL components in a composable way by adapting algorithms for top-down hierarchical control, thereby encapsulating parallelism and resource requirements within short-running compute tasks. We demonstrate the benefits of this principle through RLlib: a library that provides scalable software primitives for RL. These primitives enable a broad range of algorithms to be implemented with high performance, scalability, and substantial code reuse. RLlib is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in parallel computing and composition through symbolic differentiation have been fundamental to the recent success of deep learning. Today, there are a wide range of deep learning frameworks that enable rapid innovation in neural network design and facilitate training at the scale necessary for progress in the field.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, while the reinforcement learning community enjoys the advances in systems and abstractions for deep learning, there has been comparatively less progress in the design of systems and abstractions that directly target reinforcement learning. Nonetheless, many of the challenges in reinforcement learning stem from the need to scale learning and simulation while also integrating a rapidly increasing range of algorithms and models. As a consequence, there is a fundamental need for composable parallel primitives to support research in reinforcement learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the absence of a single dominant computational pattern (e.g., tensor algebra) or fundamental rules of composition (e.g., symbolic differentiation), the design and implementation of reinforcement learning algorithms can often be cumbersome, requiring RL researchers to directly reason about complex nested parallelism. Unlike typical operators in deep learning frameworks, individual components may require parallelism across a cluster (e.g., for rollouts), leverage neural networks implemented by deep learning frameworks, recursively invoke other components (e.g., model-based subtasks), or interface with black-box third-party simulators. In essence, the heterogeneous and distributed nature of many of these components poses a key challenge to reasoning about their parallel composition. Meanwhile, the main algorithms that connect these components are rapidly evolving and expose opportunities for parallelism at varying levels. Finally, RL algorithms manipulate substantial amounts of state (e.g., replay buffers and model parameters) that must be managed across multiple levels of parallelism and physical devices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The substantial recent progress in RL algorithms and applications has resulted in a large and growing number of RL libraries. While some of these are highly scalable, few enable the composition of components at scale. In large part, this is due to the fact that many of the frameworks used by these libraries rely on communication between long-running program replicas for distributed execution; e.g., MPI, Distributed TensorFlow, and parameter servers ). As this programming model ignores component boundaries, it does not naturally encapsulate parallelism and resource requirements within individual components.^22^2By encapsulation, we mean that individual components specify their own internal parallelism and resources requirements and can be used by other components that have no knowledge of these requirements. As a result, reusing these distributed components requires the insertion of appropriate control points in the program, a burdensome and error-prone process (Section 2). The absence of usable encapsulation hinders code reuse and leads to error prone reimplementation of mathematically complex and often highly stochastic algorithms. Even worse, in the distributed setting, often large parts of the distributed communication and execution must also be reimplemented with each new RL algorithm.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We believe that the ability to build scalable RL algorithms by composing and reusing existing components and implementations is essential for the rapid development and progress of the field.^33^3We note that composability without scalability can trivially be achieved with a single-threaded library and that all of the difficulty lies in achieving these two objectives simultaneously. Toward this end, we argue for structuring distributed RL components around the principles of logically centralized program control and parallelism encapsulation. We built RLlib using these principles, and as a result were not only able to implement a broad range of state-of-the-art RL algorithms, but also to pull out scalable primitives that can be used to easily compose new algorithms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Irregularity of RL training workloads", "weight": 1.0} -->

Modern RL algorithms are highly irregular in the computation patterns they create (Table 1), pushing the boundaries of computation models supported by popular distribution frameworks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Irregularity of RL training workloads", "weight": 1.0} -->

The duration and resource requirements of tasks differ by orders of magnitude depending on the algorithm; e.g., A3C updates may take milliseconds, but other algorithms like PPO batch rollouts into much larger granularities.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Irregularity of RL training workloads", "weight": 1.0} -->

Communication patterns vary, from synchronous to asynchronous gradient-based optimization, to having several types of asynchronous tasks in high-throughput off-policy algorithms such as Ape-X and IMPALA.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Irregularity of RL training workloads", "weight": 1.0} -->

Nested computations are generated by model-based hybrid algorithms (Table 2), hyperparameter tuning in conjunction with RL or DL training, or the combination of derivative-free and gradient-based optimization within a single algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Irregularity of RL training workloads", "weight": 1.0} -->

RL algorithms often need to maintain and update substantial amounts of state including policy parameters, replay buffers, and even external simulators.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Irregularity of RL training workloads", "weight": 1.0} -->

As a consequence, the developers have no choice but to use a hodgepodge of frameworks to implement their algorithms, including parameter servers, collective communication primitives in MPI-like frameworks, task queues, etc. For more complex algorithms, it is common to build custom distributed systems in which processes independently compute and coordinate among themselves with no central control (Figure 2(a)). While this approach can achieve high performance, the cost to develop and evaluate is large, not only due to the need to implement and debug distributed programs, but because composing these algorithms further complicates their implementation (Figure 3). Moreover, today's computation frameworks (e.g., Spark, MPI) typically assume regular computation patterns and have difficulty when sub-tasks have varying durations, resource requirements, or nesting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

It is desirable for a single programming model to capture all the requirements of RL training. This can be done without eschewing high-level frameworks that structure the computation. Our key insight is that for each distributed RL algorithm, an equivalent algorithm can be written that exhibits logically centralized program control (Figure 2(b)). That is, instead of having independently executing processes (A, B, C, D in Figure 2(a)) coordinate among themselves (e.g., through RPCs, shared memory, parameter servers, or collective communication), a single driver program (D in Figure 2(b) and 2(c)) can delegate algorithm sub-tasks to other processes to execute in parallel.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

In this paradigm, the worker processes A, B, and C passively hold state (e.g., policy or simulator state) but execute no computations until called by D. To support nested computations, we propose extending the centralized control model with hierarchical delegation of control (Figure 2(c)), which allows the worker processes (e.g., B, C) to further delegate work (e.g., simulations, gradient computation) to sub-workers of their own when executing tasks.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

Building on such a logically centralized and hierarchical control model has several important advantages. First, the equivalent algorithm is often easier to implement in practice, since the distributed control logic is entirely encapsulated in a single process rather than multiple processes executing concurrently. Second, the separation of algorithm components into sub-routines (e.g., do rollouts, compute gradients with respect to some policy loss), enables code reuse across different execution patterns. Sub-tasks that have different resource requirements (e.g., CPUs vs GPUs) can be placed on different machines, reducing compute costs as we show in Section 5. Finally, distributed algorithms written in this model can be seamlessly nested within each other, satisfying the parallelism encapsulation principle.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

Logically centralized control models can be highly performant, our proposed hierarchical variant even more so. This is because the bulk of data transfer (blue arrows in Figure 2) between processes happens out of band of the driver, not passing through any central bottleneck. In fact many highly scalable distributed systems leverage centralized control in their design. Within a single differentiable tensor graph, frameworks like TensorFlow also implement logically centralized scheduling of tensor computations onto available physical devices. Our proposal extends this principle into the broader ML systems design space.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

The contributions of this paper are as follows.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

We propose a general and composable hierarchical programming model for RL training (Section 2).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

We describe RLlib, our highly scalable RL library, and how it builds on the proposed model to provide scalable abstractions for a broad range of RL algorithms, enabling rapid development (Section 3).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Logically centralized control for distributed RL", "weight": 1.0} -->

We discuss how performance is achieved within the proposed model (Section 4), and show that RLlib meets or exceeds state-of-the-art performance for a wide variety of RL workloads (Section 5).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hierarchical Parallel Task Model", "weight": 1.0} -->

As highlighted in Figure 3, parallelization of entire programs using frameworks like MPI and Distributed Tensorflow typically require explicit algorithm modifications to insert points of coordination when trying to compose two programs or components together. This limits the ability to rapidly prototype novel distributed RL applications. Though the example in Figure 3 is simple, new hyperparameter tuning algorithms for long-running training tasks; e.g., HyperBand, Population Based Training (PBT) increasingly demand fine-grained control over training.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Hierarchical Parallel Task Model", "weight": 1.0} -->

We propose building RL libraries with hierarchical and logically centralized control on top of flexible task-based programming models like Ray. Task-based systems allow subroutines to be scheduled and executed asynchronously on worker processes, on a fine-grained basis, and for results to be retrieved or passed between processes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Relation to existing distributed ML abstractions", "weight": 1.0} -->

Though typically formulated for distributed control, abstractions such as parameter servers and collective communication operations can also be used within a logically centralized control model. As an example, RLlib uses allreduce and parameter-servers in some of its policy optimizers (Figure 4), and we evaluate their performance in Section 5.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Ray implementation of hierarchical control", "weight": 1.0} -->

We note that, within a single machine, the proposed programming model can be implemented simply with thread-pools and shared memory, though it is desirable for the underlying framework to scale to larger clusters if needed.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Ray implementation of hierarchical control", "weight": 1.0} -->

We chose to build RLlib on top of the Ray framework, which allows Python tasks to be distributed across large clusters. Ray's distributed scheduler is a natural fit for the hierarchical control model, as nested computation can be implemented in Ray with no central task scheduling bottleneck.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Ray implementation of hierarchical control", "weight": 1.0} -->

To implement a logically centralized control model, it is first necessary to have a mechanism to launch new processes and schedule tasks on them. Ray meets this requirement with Ray actors, which are Python classes that may be created in the cluster and accept remote method calls (i.e., tasks). Ray permits these actors to in turn launch more actors and schedule tasks on those actors as part of a method call, satisfying our need for hierarchical delegation as well.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Ray implementation of hierarchical control", "weight": 1.0} -->

For performance, Ray provides standard communication primitives such as aggregate and broadcast, and critically enables the zero-copy sharing of large data objects through a shared memory object store. As shown in Section 5, this enables the performance of RLlib algorithms. We further discuss framework performance in Section 4.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Abstractions for Reinforcement Learning", "weight": 1.0} -->

To leverage RLlib for distributed execution, algorithms must declare their policy $\pi$, experience postprocessor $\rho$, and loss $L$. These can be specified in any deep learning framework, including TensorFlow and PyTorch. RLlib provides policy evaluators and policy optimizers that implement strategies for distributed policy evaluation and training.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

RLlib's abstractions are as follows. The developer specifies a policy model $\pi$ that maps the current observation $o_{t}$ and (optional) RNN hidden state $h_{t}$ to an action $a_{t}$ and the next RNN state $h_{t + 1}$. Any number of user-defined values $y_{t}^{i}$ (e.g.,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

Most algorithms will also specify a trajectory postprocessor $\rho$ that transforms a batch $X_{t,K}$ of $K$ $\{{(o_{t},h_{t},a_{t},h_{t + 1},{y_{t}^{1}\ldotsy_{t}^{N}},r_{t},o_{t + 1})}\}$ tuples starting at $t$. Here $r_{t}$ and $o_{t + 1}$ are the reward and new observation after taking an action. Example uses include advantage estimation and goal relabeling.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

Finally, the developer can also specify any number of utility functions $u^{i}$ to be called as needed during training to, e.g.,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

[⬇](data:text/plain;base64,YWJzdHJhY3QgY2xhc3MgcmxsaWIuUG9saWN5R3JhcGg6CglkZWYgYWN0KHNlbGYsIG9icywgaCk6IGFjdGlvbiwgaCwgeSoKCWRlZiBwb3N0cHJvY2VzcyhzZWxmLCBiYXRjaCwgYiopOiBiYXRjaAoJZGVmIGdyYWRpZW50cyhzZWxmLCBiYXRjaCk6IGdyYWRzCglkZWYgZ2V0X3dlaWdodHM7IGRlZiBzZXRfd2VpZ2h0czsKCWRlZiB1KihzZWxmLCBhcmdzKik=){download=""}

<!-- chunk {"id": "body-0034", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

def act(self, obs, h): action, h, y\*

<!-- chunk {"id": "body-0035", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

def postprocess(self, batch, b\*): batch

<!-- chunk {"id": "body-0036", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

def gradients(self, batch): grads

<!-- chunk {"id": "body-0037", "role": "body", "section": "Defining the Policy Graph", "weight": 1.0} -->

def get_weights; def set_weights;

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

For collecting experiences, RLlib provides a PolicyEvaluator class that wraps a policy graph and environment to add a method to sample experience batches. Policy evaluator instances can be created as Ray remote actors and replicated across a cluster for parallelism. To make their usage concrete, consider a minimal TensorFlow policy gradients implementation that extends the rllib.TFPolicyGraph

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

[⬇](data:text/plain;base64,Y2xhc3MgUG9saWN5R3JhZGllbnQoVEZQb2xpY3lHcmFwaCk6CiAgZGVmIF9faW5pdF9fKHNlbGYsIG9ic19zcGFjZSwgYWN0X3NwYWNlKToKICAgIHNlbGYub2JzLCBzZWxmLmFkdmFudGFnZXMgPSAuLi4KICAgIHBpID0gRnVsbHlDb25uZWN0ZWROZXR3b3JrKHNlbGYub2JzKQogICAgZGlzdCA9IHJsbGliLmFjdGlvbl9kaXN0KGFjdF9zcGFjZSwgcGkpCiAgICBzZWxmLmFjdCA9IGRpc3Quc2FtcGxlKCkKICAgIHNlbGYubG9zcyA9IC10Zi5yZWR1Y2VfbWVhbigKICAgICAgZGlzdC5sb2dwKHNlbGYuYWN0KSAqIHNlbGYuYWR2YW50YWdlcykKICBkZWYgcG9zdHByb2Nlc3Moc2VsZiwgYmF0Y2gpOgogICAgcmV0dXJuIHJsbGliLmNvbXB1dGVfYWR2YW50YWdlcyhiYXRjaCk=){download=""}

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

dist = rllib.action_dist(act_space, pi)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

dist.logp(self.act) \* self.advantages)

<!-- chunk {"id": "body-0042", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

return rllib.compute_advantages(batch)

<!-- chunk {"id": "body-0043", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

From this policy graph definition, the developer can create a number of policy evaluator replicas ev and call ev.sample.remote on each to collect experiences in parallel from environments.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

[⬇](data:text/plain;base64,ZXZhbHVhdG9ycyA9IFtybGxpYi5Qb2xpY3lFdmFsdWF0b3IucmVtb3RlKAogICAgZW52PVNvbWVFbnYsIGdyYXBoPVBvbGljeUdyYWRpZW50KQogIGZvciBfIGluIHJhbmdlKDEwKV0KcHJpbnQocmF5LmdldChbCiAgICBldi5zYW1wbGUucmVtb3RlKCkgZm9yIGV2IGluIGV2YWx1YXRvcnNdKSk=){download=""}

<!-- chunk {"id": "body-0045", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

RLlib separates the implementation of algorithms into the declaration of the algorithm-specific policy graph and the choice of an algorithm-independent policy optimizer. The policy optimizer is responsible for the performance-critical tasks of distributed sampling, parameter updates, and managing replay buffers. To distribute the computation, the optimizer operates over a set of policy evaluator replicas.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

To complete the example, the developer chooses a policy optimizer and creates it with references to existing evaluators. The async optimizer uses the evaluator actors to compute gradients in parallel on many CPUs (Figure 4(c)). Each optimizer.step runs a round of remote tasks to improve the model. Between steps, policy graph replicas can be queried directly, e.g.,

<!-- chunk {"id": "body-0047", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

[⬇](data:text/plain;base64,b3B0aW1pemVyID0gcmxsaWIuQXN5bmNQb2xpY3lPcHRpbWl6ZXIoCiAgICBncmFwaD1Qb2xpY3lHcmFkaWVudCwgd29ya2Vycz1ldmFsdWF0b3JzKQp3aGlsZSBUcnVlOgogICAgb3B0aW1pemVyLnN0ZXAoKQogICAgcHJpbnQob3B0aW1pemVyLmZvcmVhY2hfcG9saWN5KAogICAgICAgIGxhbWJkYSBwOiBwLmdldF90cmFpbl9zdGF0cygpKSk=){download=""}

<!-- chunk {"id": "body-0048", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

Policy optimizers extend the well-known gradient-descent optimizer abstraction to the RL domain. A typical gradient-descent optimizer implements ${step{({L{(\theta)}},X,\theta)}}\Rightarrow\theta_{opt}$. RLlib's policy optimizers instead operate over the local policy graph $G$ and a set of remote evaluator replicas, i.e., ${step{(G,{ev_{1}\ldotsev_{n}},\theta)}}\Rightarrow\theta_{opt}$, capturing the sampling phase of RL as part of optimization (i.e., calling sample on policy evaluators to produce new simulation data).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

The policy optimizer abstraction has the following advantages. By separating execution strategy from policy and loss definitions, specialized optimizers can be swapped in to take advantage of available hardware or algorithm features without needing to change the rest of the algorithm. The policy graph class encapsulates interaction with the deep learning framework, allowing algorithm authors to avoid mixing distributed systems code with numerical computations, and enabling optimizer implementations to be improved and reused across different deep learning frameworks.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

As shown in Figure 4, by leveraging centralized control, policy optimizers succinctly capture a broad range of choices in RL optimization: synchronous vs asynchronous, allreduce vs parameter server, and use of GPUs vs CPUs. RLlib's policy optimizers provide performance comparable to optimized parameter server (Figure 5(a)) and MPI-based implementations (Section 5). Pulling out this optimizer abstraction is easy in a logically centralized control model since each policy optimizer has full control over the distributed computation it implements.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

We demonstrate the completeness of RLlib's abstractions by formulating the algorithm families listed in Table 2 within the API.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

DQNs: DQNs use $y^{1}$ for storing TD error, implement n-step return calculation in $\rho_{\theta}$, and the Q loss in $L$. Target updates are implemented in $u^{1}$, and setting the exploration $\epsilon$ in $u^{2}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

DQN implementation: To support experience replay, RLlib's DQN uses a policy optimizer that saves collected samples in an embedded replay buffer. The user can alternatively use an asynchronous optimizer (Figure 4(c)). The target network is updated by calls to $u^{1}$ between optimizer steps.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Ape-X implementation: Ape-X is a variation of DQN that leverages distributed experience prioritization to scale to many hundreds of cores. To adapt our DQN implementation, we created policy evaluators with a distribution of $\epsilon$ values, and wrote a new high-throughput policy optimizer ($\sim$`<!-- -->`{=html}200 lines) that pipelines the sampling and transfer of data between replay buffer actors using Ray primitives. Our implementation scales nearly linearly up to 160k environment frames per second with 256 workers (Figure 5(b)), and the optimizer can compute gradients for $\sim$`<!-- -->`{=html}8.5k 80$\times$`<!-- -->`{=html}80$\times$`<!-- -->`{=html}4 observations/s on a V100 GPU.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Policy Gradient / Off-policy PG: These algorithms store value predictions in $y^{1}$, implement advantage estimation using $\rho_{\theta}$, and combine actor and critic losses in $L$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

PPO implementation: Since PPO's loss function permits multiple SGD passes over sample data, when there is sufficient GPU memory RLlib chooses a GPU-optimized policy optimizer (Figure 4(b)) that pins data into local GPU memory. In each iteration, the optimizer collects samples from evaluator replicas, performs multi-GPU optimization locally, and then broadcasts the new model weights.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

A3C implementation: RLlib's A3C can use either the asynchronous (Figure 4(c)) or sharded parameter server policy optimizer (4(d)). These optimizers collect gradients from the policy evaluators to update the canonical copy of $\theta$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

DDPG implementation: RLlib's DDPG uses the same replay policy optimizer as DQN. $L$ includes both actor and critic losses. The user can also choose to use the Ape-X policy optimizer with DDPG.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Model-based / Hybrid: Model-based RL algorithms extend $\pi_{\theta}{(o_{t},h_{t})}$ to make decisions based on model rollouts, which can be parallelized using Ray. To update their environment models, the model loss can either be bundled with $L$, or the model trained separately (i.e., in parallel using Ray primitives) and its weights periodically updated via $u^{1}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Multi-Agent: Policy evaluators can run multiple policies at once in the same environment, producing batches of experience for each agent. Many multi-agent algorithms use a centralized critic or value function, which we support by allowing $\rho_{\theta}$ to collate experiences from multiple agents.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Evolutionary Methods: Derivative-free methods can be supported through non-gradient-based policy optimizers.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Evolution Strategies (ES) implementation: ES is a derivative-free optimization algorithm that scales well to clusters with thousands of CPUs. We were able to port a single-threaded implementation of ES to RLlib with only a few changes, and further scale it with an aggregation tree of actors (Figure 8(a)), suggesting that the hierarchical control model is both flexible and easy to adapt algorithms.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

PPO-ES experiment: We studied a hybrid algorithm that runs PPO updates in the inner loop of an ES optimization step that randomly perturbs the PPO models. The implementation took only $\sim$`<!-- -->`{=html}50 lines of code and did not require changes to PPO, showing the value of encapsulating parallelism. In our experiments, PPO-ES converged faster and to a higher reward than PPO on the Walker2d-v1 task. A similarly modified A3C-ES implementation solved PongDeterministic-v4 in 30% less time.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

AlphaGo: We sketch how to scalably implement the AlphaGo Zero algorithm using a combination of Ray and RLlib abstractions. Pseudocode for the $\sim$`<!-- -->`{=html}70 line main algorithm loop is provided in the Supplementary Material.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Logically centralized control of multiple distributed components: AlphaGo Zero uses multiple distributed components: model optimizers, self-play evaluators, candidate model evaluators, and the shared replay buffer. These components are manageable as Ray actors under a top-level AlphaGo policy optimizer. Each optimizer step loops over actor statuses to process new results, routing data between actors and launching new actor instances.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Shared replay buffer: AlphaGo Zero stores the experiences from self-play evaluator instances in a shared replay buffer. This requires routing game results to the shared buffer, which is easily done by passing the result object references from actor to actor.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Best player: AlphaGo Zero tracks the current best model and only populates its replay buffer with self-play from that model. Candidate models must achieve a $\geq {55\%}$ victory margin to replace the best model. Implementing this amounts to adding an if block in the main control loop.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

Monte-Carlo tree search: MCTS (i.e., model-based planning) can be handled as a subroutine of the policy graph, and optionally parallelized as well using Ray.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Completeness and Generality of Abstractions", "weight": 1.0} -->

HyperBand and Population Based Training: Ray includes distributed implementations of hyperparameter search algorithms such as HyperBand and PBT. We were able to use these to evaluate RLlib algorithms, which are themselves distributed, with the addition of $\sim$`<!-- -->`{=html}15 lines of code per algorithm. We note that these algorithms are non-trivial to integrate when using distributed control models due to the need to modify existing code to insert points of coordination (Figure 3). RLlib's use of short-running tasks avoids this problem, since control decisions can be easily made between tasks.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Framework Performance", "weight": 1.0} -->

In this section, we discuss properties of Ray and other optimizations critical to RLlib.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Single-node performance", "weight": 1.0} -->

Stateful computation: Tasks can share mutable state with other tasks through Ray actors. This is critical for tasks that operate on and mutate stateful objects like third-party simulators or neural network weights.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Single-node performance", "weight": 1.0} -->

Shared memory object store: RL workloads involve sharing large quantities of data (e.g., rollouts and neural network weights). Ray supports this by allowing data objects to be passed directly between workers without any central bottleneck. In Ray, workers on the same machine can also read data objects through shared memory without copies.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Single-node performance", "weight": 1.0} -->

Vectorization: RLlib can batch policy evaluation to improve hardware utilization (Figure 7), supports batched environments, and passes experience data between actors efficiently in columnar array format.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Distributed performance", "weight": 1.0} -->

Lightweight tasks: Remote call overheads in Ray are on the order of $\sim$`<!-- -->`{=html}200$\mu$s when scheduled on the same machine. When machine resources are saturated, tasks spill over to other nodes, increasing latencies to around $\sim$`<!-- -->`{=html}1ms. This enables parallel algorithms to scale seamlessly to multiple machines while preserving high single-node throughput.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Distributed performance", "weight": 1.0} -->

Nested parallelism: Building RL algorithms by composing distributed components creates multiple levels of nested parallel calls (Figure 1). Since components make decisions that may affect downstream calls, the call graph is also inherently dynamic. Ray supports this by allowing any Python function or class method to be invoked remotely as a lightweight task. For example, func.remote executes func remotely and immediately returns a placeholder result which can later be retrieved or passed to other tasks.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Distributed performance", "weight": 1.0} -->

Resource awareness: Ray allows remote calls to specify resource requirements and utilizes a resource-aware scheduler to preserve component performance. Without this, distributed components can improperly allocate resources, causing algorithms to run inefficiently or fail.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Distributed performance", "weight": 1.0} -->

Fault tolerance and straggler mitigation: Failure events become significant at scale. RLlib leverages Ray's built-in fault tolerance mechanisms, reducing costs with preemptible cloud compute instances. Similarly, stragglers can significantly impact the performance of distributed algorithms at scale. RLlib supports straggler mitigation in a generic way via the ray.wait primitive. For example, in PPO we use this to drop the slowest evaluator tasks, at the cost of some bias.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Distributed performance", "weight": 1.0} -->

Data compression: RLlib uses the LZ4 algorithm to compress experience batches. For image observations, LZ4 reduces network traffic and memory usage by more than an order of magnitude, at a compression rate of $\sim$`<!-- -->`{=html}1 GB/s/core.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Sampling efficiency: Policy evaluation is an important building block for all RL algorithms. In Figure 7 we benchmark the scalability of gathering samples from policy evaluator actors. To avoid bottlenecks, we use four intermediate actors for aggregation. Pendulum-CPU reaches over 1.5 million actions/s running a small 64$\times$`<!-- -->`{=html}64 fully connected network as the policy. Pong-GPU nears 200k actions/s on the DQN convolutional architecture.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Large-scale tests: We evaluate the performance of RLlib on Evolution Strategies (ES), Proximal Policy Optimization (PPO), and A3C, comparing against specialized systems built specifically for those algorithms using Redis, OpenMPI, and Distributed TensorFlow. The same hyperparameters were used in all experiments. We used TensorFlow to define neural networks for the RLlib algorithms evaluated.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Evaluation", "weight": 1.0} -->

RLlib's ES implementation scales well on the Humanoid-v1 task to 8192 cores using AWS m4.16xl CPU instances. With 8192 cores, we achieve a reward of 6000 in a median time of 3.7 minutes, which is over twice as fast as the best published result. For PPO we evaluate on the same Humanoid-v1 task, starting with one p2.16xl GPU instance and adding m4.16xl instances to scale. This cost-efficient local policy optimizer (Table 3) outperformed the reference MPI implementation that required multiple expensive GPU instances to scale.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We ran RLlib's A3C on an x1.16xl machine and solved the PongDeterministic-v4 environment in 12 minutes using an asynchronous policy optimizer and 9 minutes using a sharded param-server optimizer, which matches the performance of a well-tuned baseline.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Multi-GPU: To better understand RLlib's advantage in the PPO experiment, we ran benchmarks on a p2.16xl instance comparing RLlib's local multi-GPU policy optimizer with one using an allreduce in Table 3. The fact that different strategies perform better under different conditions suggests that policy optimizers are a useful abstraction.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusion", "weight": 1.5} -->

RLlib is an open source library for reinforcement learning that leverages fine-grained nested parallelism to achieve state-of-the-art performance across a broad range of RL workloads. It offers both a collection of reference algorithms and scalable abstractions for easily composing new ones.
