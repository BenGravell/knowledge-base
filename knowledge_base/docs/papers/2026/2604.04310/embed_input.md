<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Frax: Fast Robot Kinematics and Dynamics in JAX

Topics include Robotics, Real-time systems, Optimization, Planning, Control, Learning, frax, Robot kinematics.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In robot control, planning, and learning, there is a need for rigid-body dynamics libraries that are highly performant, easy to use, and compatible with CPUs and accelerators. While existing libraries often excel at either low-latency CPU execution or high-throughput GPU workloads, few provide a unified framework that targets multiple architectures without compromising performance or ease-of-use. To address this, we introduce frax, a JAX-based library for robot kinematics and dynamics, providing a high-performance, pure-Python interface across CPU, GPU, and TPU. Via a fully-vectorized approach to robot dynamics, frax enables efficient real-time control and parallelization, while supporting automatic differentiation for optimization-based methods. On CPU, frax achieves low-microsecond computation times suitable for kilohertz control rates, outperforming common libraries in Python and approaching optimized C++ implementations. On GPU, the same code scales to thousands of instances, reaching upwards of 100 million dynamics evaluations per second.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate performance on a Franka Panda manipulator and a Unitree G1 humanoid, and release frax as an open-source library.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As robots move faster and out of purely kinematic, quasi-static settings, an understanding of dynamics is critical for computing or learning real-world-feasible planners, controllers, and safety filters. Many strong libraries exist for computing robot dynamics, with Pinocchio typically noted as the fastest, though closely followed by alternatives. Similarly, physics engines and simulators are often used in control and planning to extract dynamics properties, on CPU and GPU.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There have also been a number of fast libraries for motion planning and inverse kinematics, including those that use GPU acceleration, single instruction / multiple data (SIMD) operations, or native JAX implementations. Others focus on differential inverse kinematics, with Python interfaces to compiled libraries.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work has also focused extensively on analytical and accelerated computation of gradients of rigid body dynamics algorithms, with applications to nonlinear trajectory optimization, MPC, and optimal control more broadly.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most of the leading dynamics libraries are written in C++, and while they often provide Python bindings, this can lead to added development challenges and overhead when integrating into Python-based workflows. The best libraries on CPU cannot be directly run on GPU, and vice-versa. Likewise, even if large-scale parallelization on GPU is not needed, C++-based libraries often lead to difficulties when using automatic differentiation (AD) in Python, whether in machine learning, robot planning, or control. An ideal library would run across devices, be easy to prototype, deploy efficiently in high-performance settings, and be compatible with AD libraries in Python, such as JAX.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

To address this, we present frax, a pure-Python library for fast computation of robot kinematics and dynamics. Due to its vectorized JAX implementation of rigid-body dynamics algorithms, frax natively supports just-in-time (JIT) compilation, compatibility with CPU, GPU, and TPU, and automatic differentiation. In comparisons to common dynamics libraries with Python interfaces (Pinocchio, MuJoCo), frax is the fastest library for writing inverse-kinematic and inverse-dynamic controllers, coming close to matching the raw performance of optimized C++. The same code can then be deployed across thousands of parallel instances, meeting or exceeding the performance of libraries for GPU-based simulation (MJX, BRAX). frax's codebase can be found at

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

Fast dynamics and analytical derivatives on CPU

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

Fast simulation and dynamics on CPU

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

Simulation and controller prototyping on CPU

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

Fast controller design on CPU, GPU, and TPU

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

† Compatible with external AD libraries such as CppAD

<!-- chunk {"id": "body-0014", "role": "body", "section": "Kinematics and Dynamics Preliminaries", "weight": 1.0} -->

We consider a robot modeled as a kinematic tree with generalized coordinates $\mathbf{q}$. The forward kinematics $FK{(\mathbf{q})}$ defines the transformation $\mathbf{T}$ of a link, joint, or other reference frame $i$ with respect to the $0^{th}$ (root) frame, denoted as ${}_{}^{}{}_{}^{}$. Inverse kinematics (IK) seeks joint configurations or velocities that achieve a desired task-space pose or motion, either globally (solving for $\mathbf{q}$) or differentially (solving for $\overset{˙}{\mathbf{q}}$).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Kinematics and Dynamics Preliminaries", "weight": 1.0} -->

Inverse dynamics (ID) computes the torque required to achieve a joint acceleration $\overset{¨}{\mathbf{q}}$ given the joint state $\left\lbrack \mathbf{q},\overset{˙}{\mathbf{q}} \right\rbrack$ and any external contacts or applied forces,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Kinematics and Dynamics Preliminaries", "weight": 1.0} -->

Here, $\mathbf{\Gamma}$ is the vector of generalized joint torques, $\mathbf{M}{(\mathbf{q})}$ is the joint-space mass matrix, $\mathbf{c}{(\mathbf{q},\overset{˙}{\mathbf{q}})}$ is the vector of centrifugal and Coriolis forces, $\mathbf{g}{(\mathbf{q})}$ is the gravity vector, and $\mathbf{J}$ is the Jacobian for any constraints or external forces $\mathbf{f}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Kinematics and Dynamics Preliminaries", "weight": 1.0} -->

The corresponding forward dynamics (FD) computes the acceleration of the robot $\overset{¨}{\mathbf{q}}$ resulting from the applied joint torques and external forces, for a given joint state $\left\lbrack \mathbf{q},\overset{˙}{\mathbf{q}} \right\rbrack$,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Kinematics and Dynamics Preliminaries", "weight": 1.0} -->

Rigid body dynamics algorithms are commonly based on Featherstone's formulation, namely, the Composite Rigid Body Algorithm (CRBA), the Recursive Newton-Euler Algorithm (RNEA), and the Articulated Body Algorithm (ABA). CRBA computes the joint-space mass matrix $\mathbf{M}$; RNEA computes the inverse dynamics (Eq. 1) or individual terms such as $\mathbf{c}$ or $\mathbf{g}$; and ABA computes the forward dynamics as a lower-complexity alternative to Eq. 2. These methods rely on spatial algebra, expressing motion and force in 6-D vector spaces. Using the notation of spatial algebra, we can construct the spatial axes $\mathbf{S}$, inertias $\mathbf{I}$, velocities $\mathbf{V}$, accelerations $\mathbf{A}$, forces $\mathbf{F}$, and for CRBA, the composite inertias $\mathbf{C}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Vectorized Rigid-Body Dynamics", "weight": 1.0} -->

While most dynamics libraries implement these algorithms through a recursive traversal of the kinematic tree, frax instead adopts a fully-vectorized formulation that prioritizes fine-grained parallelism, simplified tracing for automatic differentiation, and fast JIT compilation. Algorithms 1 and 2 provide an overview of the primary vectorized dynamics methods used in frax. Notation is based on spatial algebra and array broadcasting; a full overview is available in the Appendix (Table III).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Vectorized Rigid-Body Dynamics", "weight": 1.0} -->

1:Precompute: U ⊳ Ancestor mask
Algorithm 2 Vectorized CRBA (q) → M

<!-- chunk {"id": "body-0021", "role": "body", "section": "Vectorized Rigid-Body Dynamics", "weight": 1.0} -->

The main difference between frax's vectorized approach and traditional recursive approaches comes from the use of an ancestor mask $\mathbf{U} \in {\{ 0,1\}}^{n \times n}$ to encode the tree structure. Specifically, $\mathbf{U}_{ij} = 1$ if $j \in {\text{Anc}{(i)}}$ (we consider $i \in {\text{Anc}{(i)}}$), and for a topological sort of the robot joints, $\mathbf{U}$ is lower triangular. This construction allows for summations up and down the tree to be performed with matrix multiplication, assuming spatial values are expressed in a common reference frame. For CRBA, $\mathbf{U}$ also allows for vectorized computation of the entries of $\mathbf{M}$, while masking out any terms corresponding to non-ancestral pairs. Similar operators have appeared in older work, such as, but are uncommon in modern libraries.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Complexity Tradeoffs", "weight": 1.0} -->

Crucially, by avoiding a recursive loop-based structure, we intentionally increase the complexity of RNEA from $O{(n)}$ to $O{(n^{2})}$, and from $O{({nd})}$ to $O{(n^{2})}$ for CRBA. Here, $n$ is the number of degrees of freedom (DOFs) and $d$ is the maximum depth of the kinematic tree. However, the overhead of redundant $O{(n^{2})}$ computations is vastly outweighed by the performance gains from the XLA compiler's ability to make use of fine-grained parallelism within the CPU, GPU, or TPU.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Complexity Tradeoffs", "weight": 1.0} -->

In general, this aversion to loops typically leads to modest improvements to the compute time for a single evaluation on CPU, but significant improvements in JIT compilation, GPU performance, and automatic differentiation performance (on both CPU and GPU). While CPUs can efficiently handle tree traversals, GPUs favor operations with fewer sequential dependencies; thus, we take this approach to maintain strong performance across platforms. And, when applying automatic differentiation to the robot dynamics, the vectorized form avoids the cost of tracing gradients through long unrolled loops, for fast evaluation and compilation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Complexity Tradeoffs", "weight": 1.0} -->

Note that only one loop is strictly required in frax, to compute the forward kinematics. All dynamics terms are evaluated purely with array broadcasting, as seen in Algorithms 1 and 2. And, in the special case of a serial kinematic chain, such as the Franka Panda, the FK loop can even be replaced with an associative_scan. In this case, both the kinematics and dynamics can be evaluated fully loop-free, in the sense that no Python for loops are unrolled in the compiled graph.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Batched Performance", "weight": 1.0} -->

In Fig. 2, we explore the trends in throughput across CPU and increasing batch sizes on GPU. For a single robot instance, CPU is extremely fast -- much more so than on GPU, which experiences additional overhead cost, though it begins to match the total computations/second achievable once the batch size exceeds 4. As batch size increases, overhead is considerable up to approximately $N = 64$, after which the increased computational load begins to noticeably impact the total time for the batch. We also see strong performance even on very large batch sizes with throughput rates of upwards of 100 million computations per second. While this is not directly comparable with a GPU-accelerated simulator's "steps per second" metric, it does indicate that frax's dynamics methods can be used in a highly-parallelized context without impeding the performance of an underlying training environment.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Getting Started with FRAX", "weight": 1.0} -->

After installing either via pip or from source, frax supports any robot loaded via URDF, with specialized methods based on the kinematic structure (end-effector transforms, Jacobians, manipulability indices,...) available via the Manipulator and Humanoid classes. frax has native support for the Franka Panda and Unitree G1, including tuned spherized collision models and self-collision pairs for both robots.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Getting Started with FRAX", "weight": 1.0} -->

frax currently contains three examples, with more to be added: differential IK, operational space control, and safe operational space control with CBFs. Each is a minimal example of designing an IK or ID controller with JAX, and can be fully wrapped in jax.jit for high performance. Figure 1 gives a visual representation of the CBF demo, including the spherized collision model for the Franka, an obstacle, and the end-effector target shown in red.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Fast JVPs for Robot Control", "weight": 1.0} -->

As a unique benefit of using JAX, we can often replace a full set of Jacobian computations with an efficient, direct evaluation of a Jacobian-vector product (JVP). In general, a Jacobian computed via AD will be slower than an analytical form^11^1frax contains analytical Jacobians for many common functions of the robot kinematics, for this reason., unless the Jacobian does not need to be computed in the first place. As an example, in the CBF demo, we differentiate through the model of the Franka to form the safety constraints, which can be nontrivial functions of the kinematics and dynamics (e.g., the manipulability index). The Lie derivatives required to construct the CBF constraint, such as ${L_{f}h{(\mathbf{z})}} = {\frac{dh}{d\mathbf{z}}f{(\mathbf{z})}}$, is itself a JVP, and thus $\frac{dh}{d\mathbf{z}}$ does not need to be computed in full.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Fast JVPs for Robot Control", "weight": 1.0} -->

This can be particularly beneficial for high-DOF systems like the Unitree G1, while also being simple to derive and implement.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Comparison of Dynamics Libraries", "weight": 1.0} -->

To evaluate frax's performance, we consider the application of writing robot controllers, including IK-based (differential IK) and ID-based (operational space control) methods. For comparison, we include compiled C++ libraries (Pinocchio, MuJoCo), their Python APIs (with NumPy for intermediate computations), and JIT-compiled JAX libraries (MJX, BRAX). These tests reflect a typical workflow, where we need multiple kinematic and dynamic terms ($\mathbf{M}$, $\mathbf{c}$, $\mathbf{g}$, $\mathbf{J}$,...).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Comparison of Dynamics Libraries", "weight": 1.0} -->

From Figure 3, we observe that existing JAX libraries for robot dynamics (MJX, BRAX) tend to optimize for GPU performance, leading to limited applicability for single-robot control and planning on CPU. This is especially noticeable for inverse dynamics methods on the G1, which can lead to significant spikes in controller compute times (on the order of 1 $ms$ as opposed to 25 $\mus$ with frax).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Comparison of Dynamics Libraries", "weight": 1.0} -->

In comparison to the Python APIs for Pinocchio and MuJoCo, frax fares very well, with around a 2-5x speedup, due to JAX's JIT compilation leading to reduced overhead, compiler fusions, and multithreaded linear algebra operations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Comparison of Dynamics Libraries", "weight": 1.0} -->

For the best possible performance on CPU, a controller written in C++ and compiled directly with the C++ interfaces to Pinocchio and MuJoCo will beat out frax, but this gap can be quite close, as seen in the G1 OSC timings (Fig. 3). This C++ approach also loses the flexibility of Python, the easy automatic differentiation enabled via JAX, and the ability to run on GPU or TPU (see Table I). A brief summary of frax's CPU performance on common IK and ID controllers is also available in Table II, and further discussion on performance is included in the Appendix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Comparison of Dynamics Libraries", "weight": 1.0} -->

On GPU, frax is on par (or slightly faster) than MJX or BRAX. All three were designed for good GPU compatibility with JAX as the backend, so this is to be expected. However, frax has the additional benefit of significantly reduced JIT compilation times --- while JIT times are of much lower importance than "hot" calls in the control loop, for these tests, frax compiles in 1-2 seconds versus 6-12 for MJX/BRAX. For iterative development and tuning, this speedup can significantly reduce friction for designers.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we presented frax, a high-performance JAX-based library for robot kinematics and dynamics. Through a vectorized form of rigid-body dynamics, frax is fast enough for real-time, single-robot control on CPU, and scales to thousands of parallel instances on GPU or TPU. Integration with JAX allows users to automatically differentiate through complex functions of the robot kinematics and dynamics, and easily prototype in Python, without sacrificing on performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A Limitations and Future Work", "weight": 1.0} -->

frax is more minimal than other libraries like Pinocchio and MJX, but this is by design, resulting in high performance on a restricted setting. While C++ can lead to moderately faster control rates (and potentially further improved speed with code generation ), frax provides a much more flexible Python-based AD-compatible interface that is sufficiently fast for kilohertz-rate control on hardware. And, while MJX can provide a full simulation environment for training RL policies, frax can complement these environments (e.g. a low-level controller for an end-effector action space), and is more flexible for other parallelized applications such as planning. Additionally, frax does not currently focus on solving global IK problems, which is best handled by other libraries.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A Limitations and Future Work", "weight": 1.0} -->

Future directions for the library include (as an inexhaustive list) support for collision geometries beyond just spheres and planes, especially capsules, boxes, and ellipsoids; implementations of ABA, analytical derivatives of RNEA, and direct inversion of the mass matrix ^22^2Initial experiments indicate that these methods are not well suited to vectorization, and often, it seems to be more practical and faster to just call a Cholesky-based inversion or solve method on the mass matrix.; and improved support for more classes of robots (e.g. quadrupeds) and more built-in collision models for common robots. And, while we have mainly focused on frax's application to robot control, the dynamics and automatic differentiation support will be beneficial for a wide range of future planners and nonlinear optimization methods in robotics.
