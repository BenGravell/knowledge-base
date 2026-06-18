<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Differentiable GPU-Parallelized Task and Motion Planning

Topics include Task and motion planning, Compute unified device architecture, Graphics processing unit, Parallelized, Differentiable optimization, Robot manipulation, Bilevel planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Exploits GPU parallelism to simultaneously evaluate thousands of candidate continuous parameter seeds for a given plan skeleton, then applies differentiable gradient-based optimization to each seed in parallel to satisfy the induced continuous constraint satisfaction problem. This combines the discrete search of classical TAMP with massively parallel differentiable optimization, significantly reducing solve times for long-horizon manipulation tasks in highly constrained settings.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning long-horizon robot manipulation requires making discrete decisions about which objects to interact with and continuous decisions about how to interact with them. A robot planner must select grasps, placements, and motions that are feasible and safe. This class of problems falls under Task and Motion Planning (TAMP) and poses significant computational challenges in terms of algorithm runtime and solution quality, particularly when the solution space is highly constrained. To address these challenges, we propose a new bilevel TAMP algorithm that leverages GPU parallelism to efficiently explore thousands of candidate continuous solutions simultaneously. Our approach uses GPU parallelism to sample an initial batch of solution seeds for a plan skeleton and to apply differentiable optimization on this batch to satisfy plan constraints and minimize solution cost with respect to soft objectives. We demonstrate that our algorithm can effectively solve highly constrained problems with non-convex constraints in just seconds, substantially outperforming serial TAMP approaches, and validate our approach on multiple real-world robots.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Task and Motion Planning (TAMP) enables robots to plan long-horizon manipulation through integrated reasoning about sequences of discrete action types, such as pick, place, or press, and continuous action parameter values, such as grasps, placements, and trajectories. TAMP planners have demonstrated remarkable generality in complex tasks including object rearrangement, multi-arm assembly, and cooking a meal. However, TAMP problems become increasingly challenging to solve efficiently as the horizon and action space increase, and the size of the set of solutions decreases due to tightly interacting constraints, e.g., kinematics and collisions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A popular family of TAMP algorithms solve problems by first searching over discrete action sequences, also known as plan skeletons, and then searching for continuous action parameter values that satisfy the collective action constraints that govern legal parameter values. Each candidate plan skeleton induces a continuous Constraint Satisfaction Problem (CSP), which TAMP algorithms typically solve using a mixture of compositional sampling and joint optimization techniques, with each having their own trade-offs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based approaches to TAMP disconnect the parameters by generating samples for each independently using hand-engineered, projection-based, or learned generators, and then combining them through composition and rejection. Because the parameters only interact through rejection sampling when evaluating constraints, many samples are often needed to satisfy problems where the constraints interact, such as tight packing problems (Figure LABEL:fig:teaser). Optimization-based TAMP approaches, on the other hand, represent constraints as analytic functions in a mathematical program and solve for the continuous parameters by applying first- or second-order gradient descent. However, these constrained mathematical programs are highly non-convex with many local optima, making it challenging to find even a feasible solution from random parameter initializations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present cuTAMP, the first GPU-parallelized TAMP planner. cuTAMP enables massively parallel exploration of TAMP solutions by combining ideas from sampling-based and optimization-based TAMP with GPU acceleration, going beyond prior serial algorithms. We treat TAMP constraint satisfaction as simultaneous differentiable optimization over a batch of particles, representing thousands of candidate solutions. This allows us to maintain the interdependence between continuous parameters by jointly optimizing them. To initialize the particles, we leverage parallelized samplers that solve constraint subgraphs, composing their generations to populate particles near the solution manifold while ensuring good coverage of parameter space. We demonstrate that when massively parallelized, cuTAMP can effectively solve highly constrained TAMP problems. Our approach inherits the locality of gradient descent and explores multiple basins through compositional sampling, increasing the likelihood of finding the global optima. Although we focus on GPU acceleration, our method applies to other forms of parallel computation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate cuTAMP on a diverse range of TAMP problems of varying difficulty and highlight the benefits of GPU parallelism. By scaling the number of particles, we achieve significant improvements in the number of satisfying solutions, algorithm runtime, and solution quality. For highly constrained problems that baselines fail to solve, cuTAMP finds solutions in just seconds. We deploy our algorithm on a real UR5 and Kinova arm and showcase its fast planning capabilities for long-horizon manipulation problems (Figures and ). Code and videos are available on our website: cutamp.github.io.
