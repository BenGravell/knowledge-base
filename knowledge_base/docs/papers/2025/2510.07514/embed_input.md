<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse Kinematics (IK) is a core problem in robotics, in which joint configurations are found to achieve a desired end-effector pose. Although analytical solvers are fast and efficient, they are limited to systems with low degrees-of-freedom and specific topological structures. Numerical optimization-based approaches are more general, but suffer from high computational costs and frequent convergence to spurious local minima. Recent efforts have explored the use of GPUs to combine sampling and optimization to enhance both the accuracy and speed of IK solvers. We build on this recent literature and introduce HJCD-IK, a GPU-accelerated, sampling-based hybrid solver that combines an orientation-aware greedy coordinate descent initialization scheme with a Jacobian-based polishing routine. This design enables our solver to improve both convergence speed and overall accuracy as compared to the state-of-the-art, consistently finding solutions along the accuracy-latency Pareto frontier and often achieving order-of-magnitude gains. In addition, our method produces a broad distribution of high-quality samples, yielding the lowest maximum mean discrepancy. We release our code open-source for the benefit of the community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse Kinematics (IK) is fundamental robotics algorithm that finds joint configurations that achieve a desired end-effector position and orientation, arising in numerous long-standing applications. A robust IK solver must balance computational efficiency with precision and robustness, particularly in real-time and interactive environments. A key challenge for IK solvers is the inherent redundancy in many robotic systems, where multiple joint configurations can satisfy the same end-effector target. As such, unlike forward kinematics, which yields a unique end-effector pose given joint parameters, inverse kinematics often lacks a closed-form analytical solution. This renders popular and computationally efficient analytical solvers (e.g., IKFast, IKBT ) only applicable for low degree-of-freedom (DoF) systems with specific topological structures.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For general robotic systems, numerical approaches offer greater flexibility, particularly for high-DoF systems and systems with complex constraints, but come at the cost of increased computational complexity. Typically, numerical IK leverages the Jacobian of the manipulator kinematics at the current configuration to optimize for a solution using both first-order, as well as second-order methods. Many of these approaches can also incorporate additional constraints into the optimization problem. While generally effective, these methods are all *local methods*, and do not guarantee that a solution will be found given the initial seed configuration.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As such, there has been a line of work to develop "global" IK solvers, however these approaches are too computationally intensive for real-time use, or again limited to a fixed type of robotic system. There have also been many approaches that attempt to learn global solutions to the IK problem, often as a Neural Network (NN). While these approaches can learn general strategies that can be computed quickly due to the inherent parallelizability of NN inference, they often suffer from high final error, providing solutions that are centimeters of off the target pose.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given these challenges and opportunities, *parallel computing* provides promise to greatly improve the performance of numerical solvers through the parallel exploration of multiple candidate configurations that can escape local minima, particularly in cluttered or obstacle-rich environments. The computer graphics community has routinely leveraged iterative numerical IK algorithms like FABRIK and Cyclic Coordinate Descent (CCD) precisely because they are naively parallelizable and can return high quality solutions. However, these approaches lack support for orientation constraints which lessens their applicability for robotics tasks. Alternative GPU-accelerated IK approaches specifically aimed at robotics applications have instead been used to produce state-of-the-art results.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by these recent advances, in this work, we introduce HJCD-IK, a GPU-accelerated, hybrid, two-phase, sampling-based, IK solver. HJCD-IK combines a novel orientation-aware, greedy coordinate descent initialization scheme, that provides fast, diverse seeds, with a parallel Jacobian-based polishing routine. This design improves both convergence speed and accuracy over the state-of-the-art, consistently finding solutions along the accuracy-latency Pareto frontier and often achieving order-of-magnitude gains. In addition, our method produces a broad distribution of high-quality samples, yielding the lowest maximum mean discrepancy. We release our solver open-source:\

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Inverse Kinematics", "weight": 1.0} -->

Forward kinematics (FK) determines the pose of a robot manipulator's end-effector given a joint configurations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Inverse Kinematics", "weight": 1.0} -->

Numerical IK solvers generally turn the IK problem into a constrained optimization problem, minimizing the distance between the end-effector pose $\text{P}_{ee}$ and the target pose $\text{P}_{t}$, subject to joint limit constraints defined by ${\mathbf{θ}}_{min}$, ${\mathbf{θ}}_{max}$, and additional constraints, $g{({\mathbf{θ}})}$, which can account for e.g.,

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Inverse Kinematics", "weight": 1.0} -->

This results in a least-squares update to $\mathbf{θ}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Inverse Kinematics", "weight": 1.0} -->

where $\lambda > 0$ is a damping factor, $D$ is a positive diagonal matrix that scales joint updates to stabilize the step, and $J{({\mathbf{θ}})}$ is the manipulator Jacobian at the current joint configuration.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Inverse Kinematics", "weight": 1.0} -->

Finally, we note that since multiple solutions often exist for a given target pose at higher DOFs, it would be ideal to find the *global* optimal solution to maximize performance. While this is often computationally infeasible in practice, by leveraging the return of *multiple local* optima, we can enhance overall IK solver performance for real-time robotic systems. This strategy has led to the current state-of-the-art GPU-accelerated solvers. For ease of notation later, we refer to such a batch of $M$ solutions $\lbrack{{\mathbf{θ}}_{0}\ldots{\mathbf{θ}}_{M}}\rbrack$ as ${\lbrack\Theta\rbrack}_{M}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Inverse Kinematics", "weight": 1.0} -->

1:for iteration k in max_iters do
2: for joint j in J from n: 1 do
3: Compute ${\overset{\rightarrow}{u}}_{proj},{\overset{\rightarrow}{v}}_{proj}$ by Eq.˜8
Algorithm 1 CCD (θ, ϵ, max_iters → θ*)

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Cyclic Coordinate Descent (CCD)", "weight": 1.0} -->

The CCD algorithm, as typically employed, is an iterative heuristic search technique designed for solving the position-only IK problem, that is, solving for the joint angles $\mathbf{θ}$ that produce the desired $x,y,z$ position of the end effector.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Cyclic Coordinate Descent (CCD)", "weight": 1.0} -->

In CCD, joints are numbered $i = {1\text{~to~}n}$ starting at the base. As shown in Fig.˜1, at each step of the algorithm a joint, $j$ is selected from $j = {n\text{~to~}1}$ (aka from the tip to the root of the kinematic tree).

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Cyclic Coordinate Descent (CCD)", "weight": 1.0} -->

After each iteration, once all $n$ joints have been updated, the algorithm measures the distance between the end-effector and target position, often through the $L_{2}$ norm, ${\|{{\text{P}_{ee}{({\mathbf{θ}})}} - \text{P}_{t}}\|}_{2}^{2}$, and exits upon $\epsilon$-convergence. However, if the target is out of reach or CCD becomes locked in a singularity, the algorithm will continue until it reaches a preset iteration limit. The complete CCD algorithm is outlined in Alg.˜1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Orientation-Aware CCD", "weight": 1.0} -->

In this section, we develop an orientation-aware CCD scheme leveraging screw theory and manifold optimization to project not only in position space but also in orientation space. To the best of the authors' knowledge, this is the first time that orientation-based projections have been integrated into a CCD framework for robotics (e.g., derived custom update steps specifically for protein loop closure).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Orientation-Aware CCD", "weight": 1.0} -->

Given the end-effector quaternion $q_{ee}{({\mathbf{θ}})}$ and the target quaternion $q_{t}$, the orientation error $q_{err}{({\mathbf{θ}})}$ is defined as the quaternion difference Eq.˜5. We decompose the resulting quaternion error $q_{err} = {\lbrack w,{\mathbf{v}}\rbrack}$ into angle-axis form.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Orientation-Aware CCD", "weight": 1.0} -->

The angle-axis pair $(\phi,\hat{a})$ defines the orientation update.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Orientation-Aware CCD", "weight": 1.0} -->

By considering this orientation update with the standard positional CCD step, our method performs greedy joint selection in both position and orientation space, enabling rapid convergence with respect to euclidean and angular error. As such, this scheme enables a CCD-style algorithm to solve the full IK problem as shown in Eq.˜2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The HJCD-IK Algorithm", "weight": 1.0} -->

In this section we present HJCD-IK (Fig.˜2 ‣ II Background ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent"), Alg.˜2), a GPU-accelerated, sampling-based hybrid solver that couples an orientation-aware greedy coordinate-descent (PO-CCD) initializer with a parallel Jacobian-based polishing stage (PJ-IK). We present the full algorithm in Alg.˜2 and detail its sub-components in later sections and algorithms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The HJCD-IK Algorithm", "weight": 1.0} -->

At the highest level, the first stage evaluates hundreds to low-thousands of orientation-aware CCD seeds in parallel (Sec.˜IV-A ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent")) and returns $M$ seeds (Alg.˜2 Line 1). These are collected and ranked by their residuals, of which the top $K$ candidates are then duplicated with small perturbations to reduce the risk of converging to local minima, producing a batch of $B$ seeds (Alg.˜2 Lines 3-8). These are further refined by a batched Jacobian solver (Sec.˜IV-B) to return the final optimal ${\mathbf{θ}}^{\ast}$ (Alg.˜2 Line 9).

<!-- chunk {"id": "body-0023", "role": "body", "section": "The HJCD-IK Algorithm", "weight": 1.0} -->

We note that alone, orientation-aware CCD cannot converge quickly to high-precision solutions, and batched Jacobian solvers are prone to getting trapped in spurious local minima. However, when combined, orientation-aware CCD generates a diverse set of coarse solutions from many randomized initializations, providing excellent seeds for the Jacobian-based polishing stage. We also note that HJCD-IK is explicitly co-designed for GPUs, with kernels that exploit block-, warp-, and thread-level parallelism to maximize throughput while minimizing synchronization. This algorithm-hardware-software co-design approach enables real-time performance and, as shown in Sec.˜V, produces IK solutions that are both faster and more accurate than state-of-the-art alternatives.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

Our co-designed, orientation-aware, greedy CCD stage (Alg.˜3 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent")) efficiently harnesses GPU parallelism by distributing orientation-aware CCD computations across blocks, warps, and threads, enabling the simultaneous processing of hundreds to low thousands of sampled configuration seeds. At the highest level this is done by launching $M$ parallel blocks that run asynchronously, one for each sample. Within these samples synchronizations are kept to a minimum, and all underlying linear algebra is parallelized across threads for maximal efficiency.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

As shown in Alg.˜3 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Lines 2-4, the algorithm begins with uniform sampling of $M$ initial joint configuration seeds within the joint limits of each joint.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

We then enter the main orientation-aware CCD loop (Alg.˜3 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Lines 5-14) where each block uses two warps of threads for each joint. This ensures that each pair of warps is responsible for performing an update for a single joint of a single IK problem, one for orientation and one for position. At every iteration, these warps calculate coordinate descent updates while holding all other values constant, producing for each joint, in parallel, the orientation and position task residual (Alg.˜3 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Lines 6-8).

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

To determine the best update for each step, these residuals are stored in shared memory, allowing for fast, low-overhead comparisons across each block in which we greedily select both the best orientation and position update and apply it (Alg.˜3 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Lines 9-10). If both updates target the same joint, we chose the larger of the two. To reduce the chance of this process jumping to a local minima, we require a minimum threshold for improvement, $\gamma$, along either the position or orientation task space. If this update fails, we instead randomly perturb the joint configuration. This greedy joint selection process allows us to skip joint updates that will result in no progress (e.g., when the normal axis of the rotation plane is close to that of the vector made between the joint and the target position) and reduce total computation time (Alg.˜2 Lines 11-13).

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

Finally, once a seed satisfies the position and orientation error thresholds (Alg.˜2 Lines 14), the parallel loop is broken and all samples are returned.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

Because this initializer is very fast at finding reasonably good solutions but can struggle to satisfy extremely tight tolerances, it terminates at a coarse tolerance with only a modest number of iterations, deferring fine accuracy to the downstream Jacobian-based refinement. Each computation is lightweight, which allows us to scale to hundreds or even thousands of seeds and rapidly assemble a high-quality batch for subsequent refinement.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Massively-Parallel Orientation-Aware CCD (PO-CCD)", "weight": 1.0} -->

1:for iteration k in max_iters do
2: for sample b = 0 … B do in parallel blocks
3: for joint j in b do in parallel warps

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Parallel Jacobian-IK", "weight": 1.0} -->

Stage 2 of our algorithm polishes the returned high-quality batch of refined seeds $B$ into the final returned IK solution through parallel Jacobian-IK (PJ-IK) as shown in Alg.˜4 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent"). Here, each block handles one seed and parallelizes all underlying linear algebra across the warps of threads within that block. As Jacobian calculations are more expensive than CCD calculations, this reduced batch size of tens to low-hundreds of refined seeds $B$ also scales well on modern GPU hardware. To ensure that these calculations are done maximally efficiently, we leverage the GRiD library for all Jacobian calculations which is also designed for overall block-level parallelism and underlying thread-level linear algebra parallelism.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Parallel Jacobian-IK", "weight": 1.0} -->

For each candidate $b$, we solve Eq.˜2 by first minimizing a weighted task residual, where $W{({\mathbf{θ}})}$ is a diagonal weighting matrix that normalizes the rows of the Jacobian and adaptively scales the translational and rotational components of the residual. Adapting this to the LM formulation, Eq.˜6,

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Parallel Jacobian-IK", "weight": 1.0} -->

where $D = {\text{diag}{({J^{\intercal}J})}}$. The interpolation between the gradient and Gauss-Newton step via the $\lambdaD$ damping term provides additional robustness near singularities and joint limits. To further stabilize convergence, each update $\Delta{\mathbf{θ}}$ is constrained by a trust region of radius $R$, preventing aggressive steps far from the solution. Candidate steps are also validated through a backtracking line-search for the scaling factor $\alpha$, accepting the first iterate that reduces the task residual. This LM step is shown in Alg.˜4 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Lines 3-9.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Parallel Jacobian-IK", "weight": 1.0} -->

If no scaled LM step can be found, we resort to two fallback strategies. The first, a dogleg method, shown in Alg.˜4

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Parallel Jacobian-IK", "weight": 1.0} -->

If the dogleg also fails to improve the cost, a single-coordinate line search, shown in Alg.˜4

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Parallel Jacobian-IK", "weight": 1.0} -->

If all of these fail a random perturbation is made to avoid local minima (Alg.˜4 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Line 17). This is repeated until convergence is reached (Alg.˜4 ‣ IV The HJCD-IK Algorithm ‣ HJCD-IK: GPU-Accelerated Inverse Kinematics through Batched Hybrid Jacobian Coordinate Descent") Line 18). These combined refinement stages are able to consistently return precise, feasible solutions from the coarse candidates, achieving sub-millimeter positional and sub-degree rotational accuracy.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

We benchmark HJCD-IK against three other parallel IK solvers-CuRobo, IKFlow, and PyRoki. These solvers represent different state-of-the-art approaches for solving IK problems based: GPU-accelerated optimization, generative modeling with normalizing flows, and differentiable JAX-based computation, respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

Ori. Err. (rad)
Ori. Err. (rad)
Ori. Err. (rad)
Ori. Err. (rad)

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results", "weight": 1.0} -->

Ori. Err. (rad)
Ori. Err. (rad)
Ori. Err. (rad)

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

All results were collected using a workstation with an Intel Core i7-14700HX CPU (20 core, 2.1 GHz base), an NVIDIA GeForce RTX 4060 (Laptop), Windows 11 (WSL - Ubuntu 24.04), and CUDA 12.5. We sample joint configurations from a Halton Sequence to obtain 100 feasible target poses. We compare timing results across batch sizes using two robot models with 7-DoF: Franka Panda and Fetch arm. We also expand the configuration space to increase redundancy of the Franka Panda robot by adding replicated revolute joints and links to test the system scalability of our approach.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Batch-size Scalability", "weight": 1.0} -->

We first demonstrate the power of our approach through a scalability study using the 7-DoF Panda and Fetch robot arms across batch sizes of $M \in {\{ 1,10,100,1000,2000\}}$ as shown in Fig.˜3 and Table˜I. Across both robots, HJCD-IK benefits from increased batch size, yielding rapid error reductions with only modest per-target latency increases. On Panda, position/orientation error drops from $2.07 \times 10^{- 2}$mm/$1.66 \times 10^{- 3}$ at $B = 1$ to $9.21 \times 10^{- 6}$mm/$7.99 \times 10^{- 8}$rad at $B = 2000$ demonstrating reductions by $\sim {2.2 \times 10^{3}}$x and $\sim {2.1 \times 10^{4}}$x across position and orientation error, resulting in order-of-magnitude combined error improvements over baselines at larger batch sizes.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Batch-size Scalability", "weight": 1.0} -->

Fetch showcases a smaller but similar trend in improvement as batch size increases of $\sim 5$x and $\sim 1.7$x, again surpassing the state of the art at larger batch sizes. HJCD-IK also occurs minimal latency penalties by increasing batch size. On the Panda Arm as $B = 1\rightarrow 2000$, solve time increases from 5.18ms to 8.58ms and on the Fetch Arm, solve time increases from 4.70ms to 8.72ms. This results in order of magnitude speedups over IKFLow, and more than 1.5x speedups over PyROki and cuRobo at larger batch sizes. Overall, we find that across all batch sizes, our approach (shown in orange), is able to outperform state-of-the-art baselines in terms of latency, while also generally surpassing all baselines in accuracy, remaining on or near the accuracy-latency Pareto frontier.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C DoF Scalability", "weight": 1.0} -->

We also assess scalability with respect to manipulator complexity by fixing the batch size to $B = 1000$ and evaluating the 7-, 12-, 18-, and 24-DoF Panda Arm variants using HJCD-IK, CuRobo, and PyRoki. As shown in Fig.˜4 and Table˜II, HJCD-IK maintains the lowest pose error at every DoF, with position confined to $1.10 - {1.67 \times 10^{- 6}}$mm and orientation error to $3.0 - {5.4 \times 10^{- 8}}$rad, indicating added redundancy does not inflate error. We note that as DoF increases, this error improvement grows to multiple orders-of-magnitude over baselines. Latency also remains competitive and performs at or better than baselines along all DoFs. Against PyRoki, HJCD-IK is consistently faster while maintaining better accuracy, presenting speedups ranging from 1.06x to 1.93x.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C DoF Scalability", "weight": 1.0} -->

Against CuRobo, HJCD-IK is faster through 18-DoFs, presenting speedups between 1.03x and 1.17x, and a slight slowdown for the 24-DoF system (albeit with the multiple-orders-of-magnitude accuracy improvement). Overall, HJCD-IK remains on or near the accuracy-latency Pareto frontier across all DoFs, showcasing competitive IK solve times while converging to lower errors.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-D Solution Space Distribution", "weight": 1.0} -->

Returning batches of diverse solutions indicates that a batched local solver is doing a good job at sampling across the space of local optima to find good globalizing solutions. As such, to evaluate the diversity of solutions and extent of solution space coverage, we computed the Maximum Mean Discrepancy (MMD) score between solver joint configurations and a ground truth reference distribution. For each of the 100 randomly sampled target poses, solvers were initialized with a batch size of 2000 and the best 50 joint configurations with the smallest pose error were retained. These samples were compared against 50 ground truth samples generated by TRAC-IK, which were seeded with random initial joint configurations to create a diverse distribution over the feasible solution space.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-D Solution Space Distribution", "weight": 1.0} -->

Table˜III showcases the MMD scores across solvers. Smaller MMD values indicate the solver's solution space distribution better approximate the ground truth coverage. HJCD-IK achieves the lowest MMD (0.02983), suggesting that it better represents the solution space by returning a diverse set of joint configurations despite the minimized return batch size. IKFlow demonstrates a competitive MMD score (0.03670), however, PyRoki (0.04514) and CuRobo (0.05348) exhibit noticeably higher values, indicating less diversity and coverage in returned solutions.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Solution Space Distribution", "weight": 1.0} -->

In addition to MMD, we also report the squared MMD ($\text{MMD}^{2}$) which provides additional information about the variance of the distribution as it is more sensitive to small discrepancies in coverage. HJCD-IK maintains the smallest squared MMD (0.00089), demonstrating its ability to consistently generate a diverse set of solutions per target pose. With a minimized return batch, HJCD-IK is still able to preserve redundancy in the solution manifold, ensuring robustness in a feasible solution. In contrast, IKFlow, PyRoki, and CuRobo all present high squared MMD scores indicating reduced variability in their batch of returned solutions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

HJCD-IK provides fast, accurate IK solutions for any kinematically redundant manipulator operating in SE by combining a massively parallel, orientation-aware greedy coordinate descent initialization, with a parallel Jacobian-based polishing scheme. Our experiments show that HJCD-IK outperforms the state-of-the-art methods, remaining on or near the accuracy-latency Pareto frontier across batch sizes and robot DoFs, resulting in either order-of-magnitude increases in latency or accuracy. HJCD-IK also provides lower MMD and MMD^2^ scores for batches of solutions, indicating greater solution diversity and coverage.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Looking ahead, there are several promising directions for future work. One of particular note is the integration of parallel collision-checking. This would enable the solver to directly return only collision-free solutions, increasing its practicality for real-world deployment. A second direction of note is that while our empirical results demonstrate HJCD-IK's strong performance, formal analysis of its convergence and optimality remains an important open area of research.
