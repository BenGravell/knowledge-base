<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Ray: A Distributed Framework for Emerging AI Applications

Topics include Reinforcement learning, Distributed systems, Control, Learning, Ray.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The next generation of AI applications will continuously interact with the environment and learn from these interactions. These applications impose new and demanding systems requirements, both in terms of performance and flexibility. In this paper, we consider these requirements and present Ray - a distributed system to address them. Ray implements a unified interface that can express both task-parallel and actor-based computations, supported by a single dynamic execution engine. To meet the performance requirements, Ray employs a distributed scheduler and a distributed and fault-tolerant store to manage the system's control state. In our experiments, we demonstrate scaling beyond 1.8 million tasks per second and better performance than existing specialized systems for several challenging reinforcement learning applications.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the past two decades, many organizations have been collecting---and aiming to exploit---ever-growing quantities of data. This has led to the development of a plethora of frameworks for distributed data analysis, including batch, streaming, and graph processing systems. The success of these frameworks has made it possible for organizations to analyze large data sets as a core part of their business or scientific strategy, and has ushered in the age of "Big Data.​" More recently, the scope of data-focused applications has expanded to encompass more complex artificial intelligence (AI) or machine learning (ML) techniques. The paradigm case is that of *supervised learning*, where data points are accompanied by labels, and where the workhorse technology for mapping data points to labels is provided by deep neural networks. The complexity of these deep networks has led to another flurry of frameworks that focus on the training of deep neural networks and their use in prediction. These frameworks often leverage specialized hardware (e.g., GPUs and TPUs), with the goal of reducing training time in a batch setting. Examples include TensorFlow, MXNet, and PyTorch.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The promise of AI is, however, far broader than classical supervised learning. Emerging AI applications must increasingly operate in dynamic environments, react to changes in the environment, and take sequences of actions to accomplish long-term goals. They must aim not only to exploit the data gathered, but also to explore the space of possible actions. These broader requirements are naturally framed within the paradigm of *reinforcement learning* (RL). RL deals with learning to operate continuously within an uncertain environment based on delayed and limited feedback. RL-based systems have already yielded remarkable results, such as Google's AlphaGo beating a human world champion, and are beginning to find their way into dialogue systems, UAVs, and robotic manipulation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The central goal of an RL application is to learn a policy---a mapping from the state of the environment to a choice of action---that yields effective performance over time, e.g., winning a game or piloting a drone. Finding effective policies in large-scale applications requires three main capabilities. First, RL methods often rely on *simulation* to evaluate policies. Simulations make it possible to explore many different choices of action sequences and to learn about the long-term consequences of those choices. Second, like their supervised learning counterparts, RL algorithms need to perform *distributed training* to improve the policy based on data generated through simulations or interactions with the physical environment. Third, policies are intended to provide solutions to control problems, and thus it is necessary to *serve* the policy in interactive closed-loop and open-loop control scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These characteristics drive new systems requirements: a system for RL must support *fine-grained* computations (e.g., rendering actions in milliseconds when interacting with the real world, and performing vast numbers of simulations), must support *heterogeneity* both in time (e.g., a simulation may take milliseconds or hours) and in resource usage (e.g., GPUs for training and CPUs for simulations), and must support *dynamic* execution, as results of simulations or interactions with the environment can change future computations. Thus, we need a dynamic computation framework that handles millions of heterogeneous tasks per second at millisecond-level latencies.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing frameworks that have been developed for Big Data workloads or for supervised learning workloads fall short of satisfying these new requirements for RL. Bulk-synchronous parallel systems such as MapReduce, Apache Spark, and Dryad do not support fine-grained simulation or policy serving. Task-parallel systems such as CIEL and Dask provide little support for distributed training and serving. The same is true for streaming systems such as Naiad and Storm. Distributed deep-learning frameworks such as TensorFlow and MXNet do not naturally support simulation and serving. Finally, model-serving systems such as TensorFlow Serving and Clipper support neither training nor simulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While in principle one could develop an end-to-end solution by stitching together several existing systems (e.g., Horovod for distributed training, Clipper for serving, and CIEL for simulation), in practice this approach is untenable due to the tight coupling of these components within applications. As a result, researchers and practitioners today build one-off systems for specialized RL applications. This approach imposes a massive systems engineering burden on the development of distributed applications by essentially pushing standard systems challenges like scheduling, fault tolerance, and data movement onto each application.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose Ray, a general-purpose cluster-computing framework that enables simulation, training, and serving for RL applications. The requirements of these workloads range from lightweight and stateless computations, such as for simulation, to long-running and stateful computations, such as for training. To satisfy these requirements, Ray implements a unified interface that can express both *task-parallel* and *actor-based* computations. *Tasks* enable Ray to efficiently and dynamically load balance simulations, process large inputs and state spaces (e.g., images, video), and recover from failures. In contrast, *actors* enable Ray to efficiently support stateful computations, such as model training, and expose shared mutable state to clients, (e.g., a parameter server). Ray implements the actor and the task abstractions on top of a single dynamic execution engine that is highly scalable and fault tolerant.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To meet the performance requirements, Ray distributes two components that are typically centralized in existing frameworks: the task scheduler and a metadata store which maintains the computation lineage and a directory for data objects. This allows Ray to schedule millions of tasks per second with millisecond-level latencies. Furthermore, Ray provides lineage-based fault tolerance for tasks and actors, and replication-based fault tolerance for the metadata store.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

While Ray supports serving, training, and simulation in the context of RL applications, this does not mean that it should be viewed as a replacement for systems that provide solutions for these workloads in other contexts. In particular, Ray does not aim to substitute for serving systems like Clipper and TensorFlow Serving, as these systems address a broader set of challenges in deploying models, including model management, testing, and model composition. Similarly, despite its flexibility, Ray is not a substitute for generic data-parallel frameworks, such as Spark, as it currently lacks the rich functionality and APIs (e.g., straggler mitigation, query optimization) that these frameworks provide.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We make the following contributions: We design and build the first distributed framework that unifies training, simulation, and serving---necessary components of emerging RL applications.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

To support these workloads, we unify the actor and task-parallel abstractions on top of a dynamic task execution engine.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve scalability and fault tolerance, we propose a system design principle in which control state is stored in a sharded metadata store and all other system components are stateless.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve scalability, we propose a bottom-up distributed scheduling strategy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

We begin by considering the basic components of an RL system and fleshing out the key requirements for Ray. As shown in Figure 1, in an RL setting, an *agent* interacts repeatedly with the *environment*. The goal of the agent is to learn a policy that maximizes a *reward*. A *policy* is a mapping from the state of the environment to a choice of *action*. The precise definitions of environment, agent, state, action, and reward are application-specific.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

To learn a policy, an agent typically employs a two-step process: *policy evaluation* and policy improvement. To evaluate the policy, the agent interacts with the environment (e.g., with a simulation of the environment) to generate *trajectories*, where a trajectory consists of a sequence of (state, reward) tuples produced by the current policy. Then, the agent uses these trajectories to improve the policy; i.e., to update the policy in the direction of the gradient that maximizes the reward. Figure 2 shows an example of the pseudocode used by an agent to learn a policy. This pseudocode evaluates the policy by invoking rollout(environment, policy) to generate trajectories. ${\mathbf{t}\mathbf{r}\mathbf{a}\mathbf{i}\mathbf{n}}_{\mathbf{p}\mathbf{o}\mathbf{l}\mathbf{i}\mathbf{c}\mathbf{y}}{}$ then uses these trajectories to improve the current policy via policy.update(trajectories).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

This process repeats until the policy converges.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

Thus, a framework for RL applications must provide efficient support for training, serving, and *simulation* (Figure 1). Next, we briefly describe these workloads.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

*Training* typically involves running stochastic gradient descent (SGD), often in a distributed setting, to update the policy. Distributed SGD typically relies on an allreduce aggregation step or a parameter server.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

*Serving* uses the trained policy to render an action based on the current state of the environment. A serving system aims to minimize latency, and maximize the number of decisions per second. To scale, load is typically balanced across multiple nodes serving the policy.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

Finally, most existing RL applications use *simulations* to evaluate the policy---current RL algorithms are not sample-efficient enough to rely solely on data obtained from interactions with the physical world. These simulations vary widely in complexity. They might take a few ms (e.g., simulate a move in a chess game) to minutes (e.g., simulate a realistic environment for a self-driving car).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

In contrast with supervised learning, in which training and serving can be handled separately by different systems, in RL *all three of these workloads are tightly coupled in a single application*, with stringent latency requirements between them. Currently, no framework supports this coupling of workloads. In theory, multiple specialized frameworks could be stitched together to provide the overall capabilities, but in practice, the resulting data movement and latency between systems is prohibitive in the context of RL. As a result, researchers and practitioners have been building their own one-off systems.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

This state of affairs calls for the development of new distributed frameworks for RL that can efficiently support training, serving, and simulation. In particular, such a framework should satisfy the following requirements: Fine-grained, heterogeneous computations. The duration of a computation can range from milliseconds (e.g., taking an action) to hours (e.g., training a complex policy). Additionally, training often requires heterogeneous hardware (e.g., CPUs, GPUs, or TPUs).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

Flexible computation model. RL applications require both stateless and stateful computations. Stateless computations can be executed on any node in the system, which makes it easy to achieve load balancing and movement of computation to data, if needed. Thus stateless computations are a good fit for fine-grained simulation and data processing, such as extracting features from images or videos. In contrast stateful computations are a good fit for implementing parameter servers, performing repeated computation on GPU-backed data, or running third-party simulators that do not expose their state.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

Dynamic execution. Several components of RL applications require dynamic execution, as the order in which computations finish is not always known in advance (e.g., the order in which simulations finish), and the results of a computation can determine future computations (e.g., the results of a simulation will determine whether we need to perform more simulations). futures = f.remote (args) Execute function f remotely. f.remote can take objects or futures as inputs and returns one or more futures. This is non-blocking. objects = ray.get (futures) Return the values associated with one or more futures. This is blocking. ready _ futures = ray.wait (futures, k, timeout) Return the futures whose corresponding tasks have completed as soon as either k have completed or the timeout expires. actor = Class.remote (args) Instantiate class C l a s s as a remote actor, and return a handle to it. Call a method futures = actor.method.remote (args) on the remote actor and return one or more futures. Both are non-blocking.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Motivation and Requirements", "weight": 1.0} -->

We make two final comments. First, to achieve high utilization in large clusters, such a framework must handle millions of tasks per second.^\*\*^\*Assume 5ms single-core tasks and a cluster of 200 32-core nodes. This cluster can run ${{({{{1s}/5}ms})} \times 32 \times 200} = 1.28$M tasks/sec. Second, such a framework is not intended for implementing deep neural networks or complex simulators from scratch. Instead, it should enable seamless integration with existing simulators and deep learning frameworks.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Programming and Computation Model", "weight": 1.0} -->

@ray.remotedef create_policy: # Initialize the policy randomly. return policy@ray.remote(num_gpus=1)class Simulator(object): def __init__(self): # Initialize the environment. self.env = Environment def rollout(self, policy, num_steps): observations = observation = self.env.current_state for _ in range(num_steps): action = policy(observation) observation = self.env.step(action) observations.append(observation) return observations@ray.remote(num_gpus=2)def update_policy(policy, *rollouts): # Update the policy. return policy@ray.remotedef train_policy: # Create a policy. policy_id = create_policy.remote # Create 10 actors. simulators = [Simulator.remote for _ in range] # Do 100 steps of training. for _ in range: # Perform one rollout on each actor. rollout_ids = [s.rollout.remote(policy_id) for s in simulators] # Update the policy with the rollouts.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Programming and Computation Model", "weight": 1.0} -->

policy_id = update_policy.remote(policy_id, *rollout_ids) return ray.get(policy_id) Figure 3: Python code implementing the example in Figure 2 in Ray. Note that @ray.remote indicates remote functions and actors. Invocations of remote functions and actor methods return futures, which can be passed to subsequent remote functions or actor methods to encode task dependencies. Each actor has an environment object self.env shared between all of its methods.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Programming and Computation Model", "weight": 1.0} -->

Ray implements a dynamic task graph computation model, i.e., it models an application as a graph of dependent tasks that evolves during execution. On top of this model, Ray provides both an actor and a task-parallel programming abstraction. This unification differentiates Ray from related systems like CIEL, which only provides a task-parallel abstraction, and from Orleans or Akka, which primarily provide an actor abstraction.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Programming Model", "weight": 1.0} -->

Tasks. A *task* represents the execution of a remote function on a stateless worker. When a remote function is invoked, a *future* representing the result of the task is returned immediately. Futures can be retrieved using ${\mathbf{r}\mathbf{a}\mathbf{y}}.{{\mathbf{g}\mathbf{e}\mathbf{t}}{}}$ and passed as arguments into other remote functions without waiting for their result. This allows the user to express parallelism while capturing data dependencies. Table 1 shows Ray's API.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Programming Model", "weight": 1.0} -->

Remote functions operate on immutable objects and are expected to be *stateless* and side-effect free: their outputs are determined solely by their inputs. This implies idempotence, which simplifies fault tolerance through function re-execution on failure.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Programming Model", "weight": 1.0} -->

Actors. An *actor* represents a stateful computation. Each actor exposes methods that can be invoked remotely and are executed serially. A method execution is similar to a task, in that it executes remotely and returns a future, but differs in that it executes on a stateful worker. A handle to an actor can be passed to other actors or tasks, making it possible for them to invoke methods on that actor.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Programming Model", "weight": 1.0} -->

Table 2 summarizes the properties of tasks and actors. Tasks enable fine-grained load balancing through leveraging load-aware scheduling at task granularity, input data locality, as each task can be scheduled on the node storing its inputs, and low recovery overhead, as there is no need to checkpoint and recover intermediate state. In contrast, actors provide much more efficient fine-grained updates, as these updates are performed on internal rather than external state, which typically requires serialization and deserialization. For example, actors can be used to implement parameter servers and GPU-based iterative computations (e.g., training). In addition, actors can be used to wrap third-party simulators and other opaque handles that are hard to serialize.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Programming Model", "weight": 1.0} -->

To satisfy the requirements for heterogeneity and flexibility (Section 2), we augment the API in three ways. First, to handle concurrent tasks with heterogeneous durations, we introduce ${\mathbf{r}\mathbf{a}\mathbf{y}}.{{\mathbf{w}\mathbf{a}\mathbf{i}\mathbf{t}}{}}$, which waits for the first $k$ available results, instead of waiting for all results like ${\mathbf{r}\mathbf{a}\mathbf{y}}.{{\mathbf{g}\mathbf{e}\mathbf{t}}{}}$. Second, to handle resource-heterogeneous tasks, we enable developers to specify resource requirements so that the Ray scheduler can efficiently manage resources. Third, to improve flexibility, we enable nested remote functions, meaning that remote functions can invoke other remote functions. This is also critical for achieving high scalability (Section 4), as it enables multiple processes to invoke remote functions in a distributed fashion.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Computation Model", "weight": 1.0} -->

Ray employs a dynamic task graph computation model, in which the execution of both remote functions and actor methods is automatically triggered by the system when their inputs become available. In this section, we describe how the computation graph (Figure 4) is constructed from a user program (Figure 3). This program uses the API in Table 1 to implement the pseudocode from Figure 2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Computation Model", "weight": 1.0} -->

Ignoring actors first, there are two types of nodes in a computation graph: data objects and remote function invocations, or tasks. There are also two types of edges: data edges and control edges. Data edges capture the dependencies between data objects and tasks. More precisely, if data object $D$ is an output of task $T$, we add a data edge from $T$ to $D$. Similarly, if $D$ is an input to $T$, we add a data edge from $D$ to $T$. Control edges capture the computation dependencies that result from nested remote functions (Section 3.1): if task $T_{1}$ invokes task $T_{2}$, then we add a control edge from $T_{1}$ to $T_{2}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Computation Model", "weight": 1.0} -->

Actor method invocations are also represented as nodes in the computation graph. They are identical to tasks with one key difference. To capture the state dependency across subsequent method invocations on the same actor, we add a third type of edge: a stateful edge. If method $M_{j}$ is called right after method $M_{i}$ on the same actor, then we add a stateful edge from $M_{i}$ to $M_{j}$. Thus, all methods invoked on the same actor object form a chain that is connected by stateful edges (Figure 4). This chain captures the order in which these methods were invoked.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computation Model", "weight": 1.0} -->

Stateful edges help us embed actors in an otherwise stateless task graph, as they capture the implicit data dependency between successive method invocations sharing the internal state of an actor. Stateful edges also enable us to maintain lineage. As in other dataflow systems, we track data lineage to enable reconstruction. By explicitly including stateful edges in the lineage graph, we can easily reconstruct lost data, whether produced by remote functions or actor methods (Section 4.2.3).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Architecture", "weight": 1.0} -->

Ray's architecture comprises an application layer implementing the API, and a system layer providing high scalability and fault tolerance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Application Layer", "weight": 1.0} -->

The application layer consists of three types of processes: Driver: A process executing the user program.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Application Layer", "weight": 1.0} -->

Worker: A stateless process that executes tasks (remote functions) invoked by a driver or another worker. Workers are started automatically and assigned tasks by the system layer. When a remote function is declared, the function is automatically published to all workers. A worker executes tasks serially, with no local state maintained across tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Application Layer", "weight": 1.0} -->

Actor: A stateful process that executes, when invoked, only the methods it exposes. Unlike a worker, an actor is explicitly instantiated by a worker or a driver. Like workers, actors execute methods serially, except that each method depends on the state resulting from the previous method execution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "System Layer", "weight": 1.0} -->

The system layer consists of three major components: a global control store, a distributed scheduler, and a distributed object store. All components are horizontally scalable and fault-tolerant.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Global Control Store (GCS)", "weight": 1.0} -->

The global control store (GCS) maintains the entire control state of the system, and it is a unique feature of our design. At its core, GCS is a key-value store with pub-sub functionality. We use sharding to achieve scale, and per-shard chain replication to provide fault tolerance. The primary reason for the GCS and its design is to maintain fault tolerance and low latency for a system that can dynamically spawn millions of tasks per second.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Global Control Store (GCS)", "weight": 1.0} -->

Fault tolerance in case of node failure requires a solution to maintain lineage information. Existing lineage-based solutions focus on coarse-grained parallelism and can therefore use a single node (e.g., master, driver) to store the lineage without impacting performance. However, this design is not scalable for a fine-grained and dynamic workload like simulation. Therefore, we decouple the durable lineage storage from the other system components, allowing each to scale independently.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Global Control Store (GCS)", "weight": 1.0} -->

Maintaining low latency requires minimizing overheads in task scheduling, which involves choosing where to execute, and subsequently task dispatch, which involves retrieving remote inputs from other nodes. Many existing dataflow systems couple these by storing object locations and sizes in a centralized scheduler, a natural design when the scheduler is not a bottleneck. However, the scale and granularity that Ray targets requires keeping the centralized scheduler off the critical path. Involving the scheduler in each object transfer is prohibitively expensive for primitives important to distributed training like allreduce, which is both communication-intensive and latency-sensitive. Therefore, we store the object metadata in the GCS rather than in the scheduler, fully decoupling task dispatch from task scheduling.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Global Control Store (GCS)", "weight": 1.0} -->

In summary, the GCS significantly simplifies Ray's overall design, as it *enables every component in the system to be stateless*. This not only simplifies support for fault tolerance (i.e., on failure, components simply restart and read the lineage from the GCS), but also makes it easy to scale the distributed object store and scheduler independently, as all components share the needed state via the GCS. An added benefit is the easy development of debugging, profiling, and visualization tools.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Bottom-Up Distributed Scheduler", "weight": 1.0} -->

As discussed in Section 2, Ray needs to dynamically schedule millions of tasks per second, tasks which may take as little as a few milliseconds. None of the cluster schedulers we are aware of meet these requirements. Most cluster computing frameworks, such as Spark, CIEL, and Dryad implement a centralized scheduler, which can provide locality but at latencies in the tens of ms. Distributed schedulers such as work stealing, Sparrow and Canary can achieve high scale, but they either don't consider data locality, or assume tasks belong to independent jobs, or assume the computation graph is known.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Bottom-Up Distributed Scheduler", "weight": 1.0} -->

To satisfy the above requirements, we design a two-level hierarchical scheduler consisting of a global scheduler and per-node local schedulers. To avoid overloading the global scheduler, the tasks created at a node are submitted first to the node's local scheduler. A local scheduler schedules tasks locally unless the node is overloaded (i.e., its local task queue exceeds a predefined threshold), or it cannot satisfy a task's requirements (e.g., lacks a GPU). If a local scheduler decides not to schedule a task locally, it forwards it to the global scheduler. Since this scheduler attempts to schedule tasks locally first (i.e., at the leaves of the scheduling hierarchy), we call it a bottom-up scheduler.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Bottom-Up Distributed Scheduler", "weight": 1.0} -->

The global scheduler considers each node's load and task's constraints to make scheduling decisions. More precisely, the global scheduler identifies the set of nodes that have enough resources of the type requested by the task, and of these nodes selects the node which provides the lowest *estimated waiting time*. At a given node, this time is the sum of (i) the estimated time the task will be queued at that node (i.e., task queue size times average task execution), and (ii) the estimated transfer time of task's remote inputs (i.e., total size of remote inputs divided by average bandwidth). The global scheduler gets the queue size at each node and the node resource availability via heartbeats, and the location of the task's inputs and their sizes from GCS. Furthermore, the global scheduler computes the average task execution and the average transfer bandwidth using simple exponential averaging. If the global scheduler becomes a bottleneck, we can instantiate more replicas all sharing the same information via GCS. This makes our scheduler architecture highly scalable.

<!-- chunk {"id": "body-0052", "role": "body", "section": "In-Memory Distributed Object Store", "weight": 1.0} -->

To minimize task latency, we implement an in-memory distributed storage system to store the inputs and outputs of every task, or stateless computation. On each node, we implement the object store via shared memory. This allows zero-copy data sharing between tasks running on the same node. As a data format, we use Apache Arrow.

<!-- chunk {"id": "body-0053", "role": "body", "section": "In-Memory Distributed Object Store", "weight": 1.0} -->

If a task's inputs are not local, the inputs are replicated to the local object store before execution. Also, a task writes its outputs to the local object store. Replication eliminates the potential bottleneck due to hot data objects and minimizes task execution time as a task only reads/writes data from/to the local memory. This increases throughput for computation-bound workloads, a profile shared by many AI applications. For low latency, we keep objects entirely in memory and evict them as needed to disk using an LRU policy.

<!-- chunk {"id": "body-0054", "role": "body", "section": "In-Memory Distributed Object Store", "weight": 1.0} -->

As with existing cluster computing frameworks, such as Spark, and Dryad, the object store is limited to immutable data. This obviates the need for complex consistency protocols (as objects are not updated), and simplifies support for fault tolerance. In the case of node failure, Ray recovers any needed objects through lineage re-execution. The lineage stored in the GCS tracks both stateless tasks and stateful actors during initial execution; we use the former to reconstruct objects in the store.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Implementation", "weight": 1.0} -->

Ray is an active open source project^††^† developed at the University of California, Berkeley. Ray fully integrates with the Python environment and is easy to install by simply running pip install ray. The implementation comprises $\approx 40$K lines of code (LoC), 72% in C++ for the system layer, 28% in Python for the application layer. The GCS uses one Redis key-value store per shard, with entirely single-key operations. GCS tables are sharded by object and task IDs to scale, and every shard is chain-replicated for fault tolerance. We implement both the local and global schedulers as event-driven, single-threaded processes. Internally, local schedulers maintain cached state for local object metadata, tasks waiting for inputs, and tasks ready for dispatch to a worker. To transfer large objects between different object stores, we stripe the object across multiple TCP connections.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Implementation", "weight": 1.0} -->

(a) Executing a task remotely (b) Returning the result of a remote task Figure 7: An end-to-end example that adds a and b and returns c. Solid lines are data plane operations and dotted lines are control plane operations. (a) The function add is registered with the GCS by node 1 (N 1), invoked on N 1, and executed on N 2. (b) N 1 gets add’s result using ray.get. The Object Table entry for c is created in step 4 and updated in step 6 after c is copied to N 1.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Putting Everything Together", "weight": 1.0} -->

While this example involves a large number of RPCs, in many cases this number is much smaller, as most tasks are scheduled locally, and the GCS replies are cached by the global and local schedulers.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In our evaluation, we study the following questions: How well does Ray meet the latency, scalability, and fault tolerance requirements listed in Section 2? (Section 5.1) What overheads are imposed on distributed primitives (e.g., allreduce) written using Ray's API? (Section 5.1) In the context of RL workloads, how does Ray compare against specialized systems for training, serving, and simulation? (Section 5.2) What advantages does Ray provide for RL applications, compared to custom systems? (Section 5.3) All experiments were run on Amazon Web Services. Unless otherwise stated, we use m4.16xlarge CPU instances and p3.16xlarge GPU instances.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluation", "weight": 1.0} -->

(a) Ray locality scheduling Figure 8: (a) Tasks leverage locality-aware placement. 1000 tasks with a random object dependency are scheduled onto one of two nodes. With locality-aware policy, task latency remains independent of the size of task inputs instead of growing by 1-2 orders of magnitude. (b) Near-linear scalability leveraging the GCS and bottom-up distributed scheduler. Ray reaches 1 million tasks per second throughput with 60 nodes. x ∈ {70, 80, 90} omitted due to cost.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

Locality-aware task placement. Fine-grain load balancing and locality-aware placement are primary benefits of tasks in Ray. Actors, once placed, are unable to move their computation to large remote objects, while tasks can. In Figure 8(a) ‣ Figure 8 ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications"), tasks placed without data locality awareness (as is the case for actor methods), suffer 1-2 orders of magnitude latency increase at 10-100MB input data sizes. Ray unifies tasks and actors through the shared object store, allowing developers to use tasks for e.g., expensive postprocessing on output produced by simulation actors.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

End-to-end scalability. One of the key benefits of the Global Control Store (GCS) and the bottom-up distributed scheduler is the ability to horizontally scale the system to support a high throughput of fine-grained tasks, while maintaining fault tolerance and low-latency task scheduling. In Figure 8(b) ‣ Figure 8 ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications"), we evaluate this ability on an embarrassingly parallel workload of empty tasks, increasing the cluster size on the x-axis. We observe near-perfect linearity in progressively increasing task throughput. Ray exceeds 1 million tasks per second throughput at 60 nodes and continues to scale linearly beyond 1.8 million tasks per second at 100 nodes. The rightmost datapoint shows that Ray can process 100 million tasks in less than a minute (54s), with minimum variability. As expected, increasing task duration reduces throughput proportionally to mean task duration, but the overall scalability remains linear. While many realistic workloads may exhibit more limited scalability due to object dependencies and inherent limits to application parallelism, this demonstrates the scalability of our overall architecture under high load.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

Object store performance. To evaluate the performance of the object store (Section 4.2.3), we track two metrics: IOPS (for small objects) and write throughput (for large objects). In Figure 9, the write throughput from a single client exceeds 15GB/s as object size increases. For larger objects, memcpy dominates object creation time. For smaller objects, the main overheads are in serialization and IPC between the client and object store.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

(a) A timeline for GCS read and write latencies as viewed from a client submitting tasks. The chain starts with 2 replicas. We manually trigger reconfiguration as follows. At t ≈ 4.2s, a chain member is killed; immediately after, a new chain member joins, initiates state transfer, and restores the chain to 2-way replication. The maximum client-observed latency is under 30ms despite reconfigurations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

(b) The Ray GCS maintains a constant memory footprint with GCS flushing. Without GCS flushing, the memory footprint reaches a maximum capacity and the workload fails to complete within a predetermined duration (indicated by the red cross).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

GCS fault tolerance. To maintain low latency while providing strong consistency and fault tolerance, we build a lightweight chain replication layer on top of Redis. Figure 10(a) ‣ Figure 10 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications") simulates recording Ray tasks to and reading tasks from the GCS, where keys are 25 bytes and values are 512 bytes. The client sends requests as fast as it can, having at most one in-flight request at a time. Failures are reported to the chain master either from the client (having received explicit errors, or timeouts despite retries) or from any server in the chain (having received explicit errors). Overall, reconfigurations caused a maximum *client-observed* delay of under 30ms (this includes both failure detection and recovery delays).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

GCS flushing. Ray is equipped to periodically flush the contents of GCS to disk. In Figure 10(b) ‣ Figure 10 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications") we submit 50 million empty tasks sequentially and monitor GCS memory consumption. As expected, it grows linearly with the number of tasks tracked and eventually reaches the memory capacity of the system. At that point, the system becomes stalled and the workload fails to finish within a reasonable amount of time. With periodic GCS flushing, we achieve two goals. First, the memory footprint is capped at a user-configurable level (in the microbenchmark we employ an aggressive strategy where consumed memory is kept as low as possible). Second, the flushing mechanism provides a natural way to snapshot lineage to disk for long-running Ray applications.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

Recovering from task failures. In Figure 11(a) ‣ Figure 11 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications"), we demonstrate Ray's ability to transparently recover from worker node failures and elastically scale, using the durable GCS lineage storage. The workload, run on m4.xlarge instances, consists of linear chains of 100ms tasks submitted by the driver. As nodes are removed (at 25s, 50s, 100s), the local schedulers reconstruct previous results in the chain in order to continue execution. Overall per-node throughput remains stable throughout.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

Recovering from actor failures. By encoding actor method calls as stateful edges directly in the dependency graph, we can reuse the same object reconstruction mechanism as in Figure 11(a) ‣ Figure 11 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications") to provide transparent fault tolerance for *stateful computation*. Ray additionally leverages user-defined checkpoint functions to bound the reconstruction time for actors (Figure 11(b) ‣ Figure 11 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications")). With minimal overhead, checkpointing enables only 500 methods to be re-executed, versus 10k re-executions without checkpointing. In the future, we hope to further reduce actor reconstruction time, e.g., by allowing users to annotate methods that do not mutate state.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

(b) Ray scheduler ablation Figure 12: (a) Mean execution time of allreduce on 16 m4.16xl nodes. Each worker runs on a distinct node. Ray* restricts Ray to 1 thread for sending and 1 thread for receiving. (b) Ray’s low-latency scheduling is critical for allreduce.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

Allreduce. Allreduce is a distributed communication primitive important to many machine learning workloads. Here, we evaluate whether Ray can natively support a ring allreduce implementation with low enough overhead to match existing implementations. We find that Ray completes allreduce across 16 nodes on 100MB in $\sim$`<!-- -->`{=html}200ms and 1GB in $\sim$`<!-- -->`{=html}1200ms, surprisingly outperforming OpenMPI (v1.10), a popular MPI implementation, by 1.5$\times$ and 2$\times$ respectively (Figure 12(a) ‣ Figure 12 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications")). We attribute Ray's performance to its use of multiple threads for network transfers, taking full advantage of the 25Gbps connection between nodes on AWS, whereas OpenMPI sequentially sends and receives data on a single thread. For smaller objects, OpenMPI outperforms Ray by switching to a lower overhead algorithm, an optimization we plan to implement in the future.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Microbenchmarks", "weight": 1.0} -->

Ray's scheduler performance is critical to implementing primitives such as allreduce. In Figure 12(b) ‣ Figure 12 ‣ 5.1 Microbenchmarks ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications"), we inject artificial task execution delays and show that performance drops nearly 2$\times$ with just a few ms of extra latency. Systems with centralized schedulers like Spark and CIEL typically have scheduler overheads in the tens of milliseconds, making such workloads impractical. Scheduler throughput also becomes a bottleneck since the number of tasks required by ring reduce scales quadratically with the number of participants.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Building blocks", "weight": 1.0} -->

End-to-end applications (e.g., AlphaGo ) require a tight coupling of training, serving, and simulation. In this section, we isolate each of these workloads to a setting that illustrates a typical RL application's requirements. Due to a flexible programming model targeted to RL, and a system designed to support this programming model, Ray matches and sometimes exceeds the performance of dedicated systems for these individual workloads.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Distributed Training", "weight": 1.0} -->

We implement data-parallel synchronous SGD leveraging the Ray actor abstraction to represent model replicas. Model weights are synchronized via allreduce (5.1) or parameter server, both implemented on top of the Ray API.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Distributed Training", "weight": 1.0} -->

In Figure 13, we evaluate the performance of the Ray (synchronous) parameter-server SGD implementation against state-of-the-art implementations, using the same TensorFlow model and synthetic data generator for each experiment. We compare only against TensorFlow-based systems to accurately measure the overhead imposed by Ray, rather than differences between the deep learning frameworks themselves. In each iteration, model replica actors compute gradients in parallel, send the gradients to a sharded parameter server, then read the summed gradients from the parameter server for the next iteration.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Serving", "weight": 1.0} -->

Model serving is an important component of end-to-end applications. Ray focuses primarily on the embedded serving of models to simulators running within the same dynamic task graph (e.g., within an RL application on Ray). In contrast, systems like Clipper focus on serving predictions to external clients.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Serving", "weight": 1.0} -->

In this setting, low latency is critical for achieving high utilization. To show this, in Table 3 we compare the server throughput achieved using a Ray actor to serve a policy versus using the open source Clipper system over REST. Here, both client and server processes are co-located on the same machine (a p3.8xlarge instance). This is often the case for RL applications but not for the general web serving workloads addressed by systems like Clipper. Due to its low-overhead serialization and shared memory abstractions, Ray achieves an order of magnitude higher throughput for a small fully connected policy model that takes in a large input and is also faster on a more expensive residual network policy model, similar to one used in AlphaGo Zero, that takes smaller input.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Simulation", "weight": 1.0} -->

Simulators used in RL produce results with variable lengths ("timesteps") that, due to the tight loop with training, must be used as soon as they are available. The task heterogeneity and timeliness requirements make simulations hard to support efficiently in BSP-style systems. To demonstrate, we compare an MPI implementation that submits $3n$ parallel simulation runs on $n$ cores in 3 rounds, with a global barrier between rounds^§§^§Note that experts *can* use MPI's asynchronous primitives to get around barriers---at the expense of increased program complexity ---we nonetheless chose such an implementation to simulate BSP., to a Ray program that issues the same $3n$ tasks while concurrently gathering simulation results back to the driver. Table 4 shows that both systems scale well, yet Ray achieves up to 1.8$\times$ throughput. This motivates a programming model that can dynamically spawn and collect the results of fine-grained simulation tasks.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Simulation", "weight": 1.0} -->

System, programming model MPI, bulk synchronous Ray, asynchronous tasks Table 4: Timesteps per second for the Pendulum-v0 simulator in OpenAI Gym. Ray allows for better utilization when running heterogeneous simulations at scale.

<!-- chunk {"id": "body-0079", "role": "body", "section": "RL Applications", "weight": 1.0} -->

Without a system that can tightly couple the training, simulation, and serving steps, reinforcement learning algorithms today are implemented as one-off solutions that make it difficult to incorporate optimizations that, for example, require a different computation structure or that utilize different architectures. Consequently, with implementations of two representative reinforcement learning applications in Ray, we are able to match and even outperform custom systems built specifically for these algorithms. The primary reason is the flexibility of Ray's programming model, which can express application-level optimizations that would require substantial engineering effort to port to custom-built systems, but are transparently supported by Ray's dynamic task graph execution engine.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Evolution Strategies", "weight": 1.0} -->

To evaluate Ray on large-scale RL workloads, we implement the evolution strategies (ES) algorithm and compare to the reference implementation ---a system specially built for this algorithm that relies on Redis for messaging and low-level multiprocessing libraries for data-sharing. The algorithm periodically broadcasts a new policy to a pool of workers and aggregates the results of roughly 10000 tasks (each performing 10 to 1000 simulation steps).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Evolution Strategies", "weight": 1.0} -->

As shown in Figure 14(a) ‣ Figure 14 ‣ 5.3.1 Evolution Strategies ‣ 5.3 RL Applications ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications"), an implementation on Ray scales to 8192 cores. Doubling the cores available yields an average completion time speedup of 1.6$\times$. Conversely, the special-purpose system fails to complete at 2048 cores, where the work in the system exceeds the processing capacity of the application driver. To avoid this issue, the Ray implementation uses an aggregation tree of actors, reaching a median time of 3.7 minutes, more than twice as fast as the best published result (10 minutes).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Evolution Strategies", "weight": 1.0} -->

Initial parallelization of a serial implementation using Ray required modifying only 7 lines of code. Performance improvement through hierarchical aggregation was easy to realize with Ray's support for nested tasks and actors. In contrast, the reference implementation had several hundred lines of code dedicated to a protocol for communicating tasks and data between workers, and would require further engineering to support optimizations like hierarchical aggregation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

We implement Proximal Policy Optimization (PPO) in Ray and compare to a highly-optimized reference implementation that uses OpenMPI communication primitives. The algorithm is an asynchronous scatter-gather, where new tasks are assigned to simulation actors as they return rollouts to the driver. Tasks are submitted until 320000 simulation steps are collected (each task produces between 10 and 1000 steps). The policy update performs 20 steps of SGD with a batch size of 32768. The model parameters in this example are roughly 350KB. These experiments were run using p2.16xlarge (GPU) and m4.16xlarge (high CPU) instances.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

As shown in Figure 14(b) ‣ Figure 14 ‣ 5.3.1 Evolution Strategies ‣ 5.3 RL Applications ‣ 5 Evaluation ‣ Ray: A Distributed Framework for Emerging AI Applications"), the Ray implementation outperforms the optimized MPI implementation in all experiments, while using a fraction of the GPUs. The reason is that Ray is heterogeneity-aware and allows the user to utilize asymmetric architectures by expressing resource requirements at the granularity of a task or actor. The Ray implementation can then leverage TensorFlow's single-process multi-GPU support and can pin objects in GPU memory when possible. This optimization cannot be easily ported to MPI due to the need to asynchronously gather rollouts to a single GPU process. Indeed, includes two custom implementations of PPO, one using MPI for large clusters and one that is optimized for GPUs but that is restricted to a single node. Ray allows for an implementation suitable for both scenarios.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

Ray's ability to handle resource heterogeneity also decreased PPO's cost by a factor of 4.5, since CPU-only tasks can be scheduled on cheaper high-CPU instances. In contrast, MPI applications often exhibit symmetric architectures, in which all processes run the same code and require identical resources, in this case preventing the use of CPU-only machines for scale-out. Furthermore, the MPI implementation requires on-demand instances since it does not transparently handle failure. Assuming 4$\times$ cheaper spot instances, Ray's fault tolerance and resource-aware scheduling together cut costs by 18$\times$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion and Experiences", "weight": 1.5} -->

Building Ray has been a long journey. It started two years ago with a Spark library to perform distributed training and simulations. However, the relative inflexibility of the BSP model, the high per-task overhead, and the lack of an actor abstraction led us to develop a new system. Since we released Ray roughly one year ago, several hundreds of people have used it and several companies are running it in production. Here we discuss our experience developing and using Ray, and some early user feedback.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion and Experiences", "weight": 1.5} -->

API. In designing the API, we have emphasized minimalism. Initially we started with a basic *task* abstraction. Later, we added the wait primitive to accommodate rollouts with heterogeneous durations and the *actor* abstraction to accommodate third-party simulators and amortize the overhead of expensive initializations. While the resulting API is relatively low-level, it has proven both powerful and simple to use. We have already used this API to implement many state-of-the-art RL algorithms on top of Ray, including A3C, PPO, DQN, ES, DDPG, and Ape-X. In most cases it took us just a few tens of lines of code to port these algorithms to Ray. Based on early user feedback, we are considering enhancing the API to include higher level primitives and libraries, which could also inform scheduling decisions.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion and Experiences", "weight": 1.5} -->

Limitations. Given the workload generality, specialized optimizations are hard. For example, we must make scheduling decisions without full knowledge of the computation graph. Scheduling optimizations in Ray might require more complex runtime profiling. In addition, storing lineage for each task requires the implementation of garbage collection policies to bound storage costs in the GCS, a feature we are actively developing.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion and Experiences", "weight": 1.5} -->

Fault tolerance. We are often asked if fault tolerance is really needed for AI applications. After all, due to the statistical nature of many AI algorithms, one could simply ignore failed rollouts. Based on our experience, our answer is "yes". First, the ability to ignore failures makes applications much easier to write and reason about. Second, our particular implementation of fault tolerance via deterministic replay dramatically simplifies debugging as it allows us to easily reproduce most errors. This is particularly important since, due to their stochasticity, AI algorithms are notoriously hard to debug. Third, fault tolerance helps save money since it allows us to run on cheap resources like spot instances on AWS. Of course, this comes at the price of some overhead. However, we found this overhead to be minimal for our target workloads.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion and Experiences", "weight": 1.5} -->

GCS and Horizontal Scalability. The GCS dramatically simplified Ray development and debugging. It enabled us to query the entire system state while debugging Ray itself, instead of having to manually expose internal component state. In addition, the GCS is also the backend for our timeline visualization tool, used for application-level debugging.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion and Experiences", "weight": 1.5} -->

The GCS was also instrumental to Ray's horizontal scalability. In Section 5, we were able to scale by adding more shards whenever the GCS became a bottleneck. The GCS also enabled the global scheduler to scale by simply adding more replicas. Due to these advantages, we believe that centralizing control state will be a key design component of future distributed systems.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

No general-purpose system today can efficiently support the tight loop of training, serving, and simulation. To express these core building blocks and meet the demands of emerging AI applications, Ray unifies task-parallel and actor programming models in a single dynamic task graph and employs a scalable architecture enabled by the global control store and a bottom-up distributed scheduler. The programming flexibility, high throughput, and low latencies simultaneously achieved by this architecture is particularly important for emerging artificial intelligence workloads, which produce tasks diverse in their resource requirements, duration, and functionality. Our evaluation demonstrates linear scalability up to 1.8 million tasks per second, transparent fault tolerance, and substantial performance improvements on several contemporary RL workloads. Thus, Ray provides a powerful combination of flexibility, performance, and ease of use for the development of future AI applications.
