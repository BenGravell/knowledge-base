<!-- arxiv-full-text:v1 {"arxiv_id": "1910.00935", "source": "ar5iv"} -->

## Introduction

Figure 1: Left: Our language allows us to seamlessly integrate a neural network (NN) controller and a physical simulation module, and update the weights of the controller or the initial state parameterization (blue). Our simulations typically have 512 ∼ 2048 time steps, and each time step has up to one thousand parallel operations. Right: 10 differentiable simulators built with DiffTaichi.

Differentiable physical simulators are effective components in machine learning systems. For example, de Avila Belbute-Peres et al. and Hu et al. have shown that controller optimization with differentiable simulators converges one to four orders of magnitude faster than model-free reinforcement learning algorithms. The presence of differentiable physical simulators in the inner loop of these applications makes their performance vitally important. Unfortunately, using existing tools it is difficult to implement these simulators with high performance.

We present DiffTaichi, a new differentiable programming language for high performance physical simulations on both CPU and GPU. It is based on the Taichi programming language. The DiffTaichi automatic differentiation system is designed to suit key language features required by physical simulation, yet often missing in existing differentiable programming tools, as detailed below:

### Megakernels

Our language uses a "megakernel" approach, allowing the programmer to naturally fuse multiple stages of computation into a single kernel, which is later differentiated using source code transformations and just-in-time compilation. Compared to the linear algebra operators in TensorFlow and PyTorch, DiffTaichi kernels have higher arithmetic intensity and are therefore more efficient for physical simulation tasks.

### Imperative Parallel Programming

In contrast to functional array programming languages that are popular in modern deep learning, most traditional physical simulation programs are written in imperative languages such as Fortran and C++. DiffTaichi likewise adopts an imperative approach. The language provides parallel loops and control flows (such as "if" statements), which are widely used constructs in physical simulations: they simplify common tasks such as handling collisions, evaluating boundary conditions, and building iterative solvers. Using an imperative style makes it easier to port existing physical simulation code to DiffTaichi.

### Flexible Indexing

Existing parallel differentiable programming systems provide element-wise operations on arrays of the same shape, e.g. c\[i, j\] = a\[i, j\] + b\[i, j\]. However, many physical simulation operations, such as numerical stencils and particle-grid interactions are not element-wise. Common simulation patterns such as y\[p\[i\] \* 2, j\] = x\[q\[i + j\]\] can only be expressed with unintuitive scatter/gather operations in these existing systems, which are not only inefficient but also hard to develop and maintain. On the other hand, in DiffTaichi, the programmer directly manipulates array elements via arbitrary indexing, thus allowing partial updates of global arrays and making these common simulation patterns naturally expressible. The explicit indexing syntax also makes it easy for the compiler to perform access optimizations.

The three requirements motivated us to design a tailored two-scale automatic differentiation system, which makes DiffTaichi especially suitable for developing complex and high-performance differentiable physical simulators, possibly with neural network controllers (Fig. 1, left). Using our language, we are able to quickly implement and automatically differentiate 10 physical simulators^11^1Our language, compiler, and simulator code is open-source. All the results in this work can be reproduced by a single Python script. Visual results in this work are presented in the supplemental video., covering rigid bodies, deformable objects, and fluids (Fig. 1, right). A comprehensive comparison between DiffTaichiand other differentiable programming tools is in Appendix A.

## Background: The Taichi Programming Language

DiffTaichi is based on the Taichi programming language. Taichi is an imperative programming language embedded in C++14. It delivers both high performance and high productivity on modern hardware. The key design that distinguishes Taichi from other imperative programming languages such as C++/CUDA is the decoupling of computation from data structures. This allows programmers to easily switch between different data layouts and access data structures with indices (i.e. x\[i, j, k\]), as if they are normal dense arrays, regardless of the underlying layout. The Taichi compiler then takes both the data structure and algorithm information to apply performance optimizations. Taichi provides "parallel-for\" loops as a first-class construct. These designs make Taichi especially suitable for writing high-performance physical simulators. For more details, readers are referred to Hu et al..

The DiffTaichi language frontend is embedded in Python, and a Python AST transformer compiles DiffTaichi code to Taichi intermediate representation (IR). Unlike Python, the DiffTaichi language is compiled, statically-typed, parallel, and differentiable. We extend the Taichi compiler to further compile and automatically differentiate the generated Taichi IR into forward and backward executables.

We demonstrate the language using a mass-spring simulator, with three springs and three mass points, as shown right. In this section we introduce the forward simulator using the DiffTaichi frontend of Taichi, which is an easier-to-use wrapper of the Taichi C++14 frontend.

### Allocating Global Variables

Firstly we allocate a set of global tensors to store the simulation state. These tensors include a scalar loss of type float32, 2D tensors x, v, force of size steps$\times$n_springs and type float32x2, and 1D arrays of size n_spring for spring properties: spring_anchor_a (int32), spring_anchor_b (int32), spring_length (float32).

### Defining Kernels

A mass-spring system is modeled by Hooke's law $\mathbf{F} = {k{({\left. \parallel{\mathbf{x}_{a} - \mathbf{x}_{b}}\parallel \right._{2} - l_{0}})}\frac{\mathbf{x}_{a} - \mathbf{x}_{b}}{\left. \parallel{\mathbf{x}_{a} - \mathbf{x}_{b}}\parallel \right._{2}}}$ where $k$ is the spring stiffness, $\mathbf{F}$ is spring force, $\mathbf{x}_{a}$ and $\mathbf{x}_{b}$ are the positions of two mass points, and $l_{0}$ is the rest length. The following kernel loops over all the springs and scatters forces to mass points: [⬇](data:text/plain;base64,QHRpLmtlcm5lbApkZWYgYXBwbHlfc3ByaW5nX2ZvcmNlKHQ6IHRpLmkzMik6CiAgIyBLZXJuZWxzIGNhbiBoYXZlIHBhcmFtZXRlcnMuIEhlcmUgdCBpcyBhIHBhcmFtZXRlciB3aXRoIHR5cGUgaW50MzIuCiAgZm9yIGkgaW4gcmFuZ2Uobl9zcHJpbmdzKTogIyBBIHBhcmFsbGVsIGZvciwgcHJlZmVyYWJseSBvbiBHUFUKICAgIGEsIGIgPSBzcHJpbmdfYW5jaG9yX2FbaV0sIHNwcmluZ19hbmNob3JfYltpXQogICAgeF9hLCB4X2IgPSB4W3QgLSAxLCBhXSwgeFt0IC0gMSwgYl0KICAgIGRpc3QgPSB4X2EgLSB4X2IKICAgIGxlbmd0aCA9IGRpc3Qubm9ybSgpICsgMWUtNAogICAgRiA9IChsZW5ndGggLSBzcHJpbmdfbGVuZ3RoW2ldKSAqIHNwcmluZ19zdGlmZm5lc3MgKiBkaXN0IC8gbGVuZ3RoCiAgICAjIEFwcGx5IHNwcmluZyBpbXB1bHNlcyB0byBtYXNzIHBvaW50cy4KICAgIGZvcmNlW3QsIGFdICs9IC1GICMgIis9IiBpcyBhdG9taWMgYnkgZGVmYXVsdAogICAgZm9yY2VbdCwgYl0gKz0gIEY=){download=""} def apply_spring_force(t: ti.i32): \# Kernels can have parameters. Here t is a parameter with type int32. for i in range(n_springs): \# A parallel, preferably on GPU a, b = spring_anchor_a\[i\], spring_anchor_b\[i\] length = dist.norm + 1e-4 F = (length - spring_length\[i\]) \* spring_stiffness \* dist / length \# Apply spring impulses to mass points. force\[t, a\] += -F \# \"+=\" is atomic by default For each particle $i$, we use semi-implicit Euler time integration with damping: ${{{\mathbf{v}}_{t,i} = {{e^{- {\Deltat\alpha}}{\mathbf{v}}_{{t - 1},i}} + {\frac{\Deltat}{m_{i}}\mathbf{F}_{t,i}}}},{\mathbf{x}_{t,i} = {\mathbf{x}_{{t - 1},i} + {\Deltat{\mathbf{v}}_{t,i}}}}},$ where ${\mathbf{v}}_{t,i},\mathbf{x}_{t,i},m_{i}$ are the velocity, position and mass of particle $i$ at time step $t$, respectively. $\alpha$ is a damping factor. The kernel is as follows: [⬇](data:text/plain;base64,QHRpLmtlcm5lbApkZWYgdGltZV9pbnRlZ3JhdGUodDogdGkuaTMyKToKICBmb3IgaSBpbiByYW5nZShuX29iamVjdHMpOgogICAgcyA9IG1hdGguZXhwKC1kdCAqIGRhbXBpbmcpICMgQ29tcGlsZS10aW1lIGV2YWx1YXRpb24gc2luY2UgZHQgYW5kIGRhbXBpbmcgYXJlIGNvbnN0YW50cwogICAgdlt0LCBpXSA9IHMgKiB2W3QgLSAxLCBpXSArIGR0ICogZm9yY2VbdCwgaV0gLyBtYXNzICMgbWFzcyA9IDEgaW4gdGhpcyBleGFtcGxlCiAgICB4W3QsIGldID0geFt0IC0gMSwgaV0gKyBkdCAqIHZbdCwgaV0=){download=""} def time_integrate(t: ti.i32): for i in range(n_objects): s = math.exp(-dt \* damping) \# Compile-time evaluation since dt and damping are constants v\[t, i\] = s \* v\[t - 1, i\] + dt \* force\[t, i\] / mass \# mass = 1 in this example

### Assembling the Forward Simulator

With these components, we define the forward time integration: [⬇](data:text/plain;base64,ZGVmIGZvcndhcmQoKToKICBmb3IgdCBpbiByYW5nZSgxLCBzdGVwcyk6CiAgICBhcHBseV9zcHJpbmdfZm9yY2UodCkKICAgIHRpbWVfaW50ZWdyYXRlKHQp){download=""} for t in range(1, steps): apply_spring_force(t)

## Automatically Differentiating Physical Simulators in Taichi

The main goal of DiffTaichi's automatic differentiation (AD) system is to generate gradient simulators automatically with minimal code changes to the traditional forward simulators.

### Design Decision

Source Code Transformation (SCT) and Tracing are common choices when designing AD systems. In our setting, using SCT to differentiate a whole simulator with thousands of time steps, results in high performance yet poor flexibility and long compilation time. On the other hand, naively adopting tracing provides flexibility yet poor performance, since the "megakernel\" structure is not preserved during backpropagation. To get both performance and flexibility, we developed a two-scale automatic differentiation system (Figure 2): we use SCT for differentiating within kernels, and use a light-weight tape that only stores function pointers and arguments for end-to-end simulation differentiation. The global tensors are natural checkpoints for gradient evaluation.

Figure 2: Left: The DiffTaichi system. We reuse some infrastructure (white boxes) from Taichi, while the blue boxes are our extensions for differentiable programming. Right: The tape records kernel launches and replays the gradient kernels in reverse order during backpropagation.

### Assumption

Unlike functional programming languages where immutable output buffers are generated, imperative programming allows programmers to freely modify global tensors. To make automatic differentiation well-defined under this setting, we make the following assumption on imperative kernels: Global Data Access Rules: 1) If a global tensor element is written more than once, then starting from the second write, the write must come in the form of an atomic add ("accumulation"). 2) No read accesses happen to a global tensor element, until its accumulation is done.

In forward simulators, programmers may make subtle changes to satisfy the rules. For instance, in the mass-spring simulation example, we record the whole history of x and v, instead of keeping only the latest values. The memory consumption issues caused by this can be alleviated via checkpointing, as discussed later in Appendix D.

With these assumptions, kernels will not overwrite the outputs of each other, and the goal of AD is clear: given a primal kernel $f$ that takes as input $X_{1},X_{2},\ldots,X_{n}$ and outputs (or accumulates to) $Y_{1},Y_{2},\ldots,Y_{m}$, the generated gradient (adjoint) kernel $f^{\ast}$ should take as input $X_{1},X_{2},\ldots,X_{n}$ and $Y_{1}^{\ast},Y_{2}^{\ast},\ldots,Y_{m}^{\ast}$ and accumulate gradient contributions to $X_{1}^{\ast},X_{2}^{\ast},\ldots,X_{m}^{\ast}$, where each $X_{i}^{\ast}$ is an adjoint of $X_{i}$, i.e. $\partial{\text{(loss)}/{\partial X_{i}}}$.

### Storage Control of Adjoint Tensors

Users can specify the storage of adjoint tensors using the Taichi data structure description language, as if they are primal tensors. We also provide ti.root.lazy_grad to automatically place the adjoint tensors following the layout of their primals.

### Local AD: Differentiating Taichi Kernels using Source Code Transforms

A typical Taichi kernel consists of multiple levels of for loops and a body block. To make later AD easier, we introduce two basic code transforms to simplify the loop body, as detailed below.

// eliminate mutable var Figure 3: Simple IR preprocessing before running the AD source code transform (left to right). Demonstrated in C++. The actual Taichi IR is often more complex. Containing loops are ignored.

### Flatten Branching

In physical simulation branches are common, e.g., when implementing boundary conditions and collisions. To simplify the reverse-mode AD pass, we first replace "if" statements with ternary operators select(cond, value_if_true, value_if_false), whose gradients are clearly defined (Fig. 3, middle). This is a common transformation in program vectorization (e.g. Karrenberg & Hack; Pharr & Mark ).

### Eliminate Mutable Local Variables

After removing branching, we end up with straight-line loop bodies. To further simplify the IR and make the procedure truly single-assignment, we apply a series of local variable store forwarding transforms, until the mutable local variables can be fully eliminated (Fig. 3, right).

After these two custom IR simplification transforms, DiffTaichi only has to differentiate the straight-line code without mutable variables, which it achieves with reverse-mode AD, using a standard source code transformation. More details on this transform are in Appendix B.

### Loops

Most loops in physical simulation are parallel loops, and during AD we preserve the parallel loop structures. For loops that are not explicitly marked as parallel, we reverse the loop order during AD transforms. We do not support loops that carry a mutating local variable since that would require a complex and costly run-time stack to maintain the history of local variables. Instead, users are instructed to employ global variables that satisfy the global data access rules.

### Parallelism and Thread Safety

For forward simulation, we inherit the "parallel-for\" construct from Taichi to map each loop iteration onto CPU/GPU threads. Programmers use atomic operations for thread safety. Our system can automatically differentiate these atomic operations. Gradient contributions in backward kernels are accumulated to the adjoint tensors via atomic adds.

### Global AD: End-to-end Backpropagation using A Light-Weight Tape

We construct a tape (Fig. 2, right) of the kernel execution so that gradient kernels can be replayed in a reversed order. The tape is very light-weight: since the intermediate results are stored in global tensors, during forward simulation the tape only records kernel names and the (scalar) input parameters, unlike other differentiable functional array systems where all the intermediate buffers have to be recorded by the tape. Whenever a DiffTaichi kernel is launched, we append the kernel function pointer and parameters to the tape. When evaluating gradients, we traverse the reversed tape, and invoke the gradient kernels with the recorded parameters. Note that DiffTaichi AD is evaluating gradients with respect to input global tensors instead of the input parameters.

### Learning/Optimization with Gradients

Now we revisit the mass-spring example and make it differentiable for optimization. Suppose the goal is to optimize the rest lengths of the springs so that the triangle area formed by the three springs becomes $0.2$ at the end of the simulation. We first define the loss function: def compute_loss(t: ti.i32):

## Triangle area from cross product

loss[None] = ti.sqr(area - target_area)

## Everything in Taichi is a tensor

## "loss" is a scalar (0-D tensor), thereby indexed with [None]

The programmer uses ti.Tape to memorize forward kernel launches. It automatically replays the gradients of these kernels in reverse for backpropagation. Initially the springs have lengths $\lbrack 0.1,0.1,0.14\rbrack$, and after optimization the rest lengths are $\lbrack 0.600,0.600,0.529\rbrack$. This means the springs will expand the triangle according to Hooke's law and form a larger triangle: \[Reproduce: mass_spring_simple.py\] for iter in range: with ti.Tape(loss): compute_loss(steps - 1) print(’Iter=’, iter) print(’Loss=’,loss[None])

## Gradient descent

for i in range(n_springs): lr * spring_length.grad[i]

### Complex Kernels

Sometimes the user may want to override the gradients provided by the compiler. For example, when differentiating a 3D singular value decomposition done with an iterative solver, it is better to use a manually engineered SVD derivative subroutine for better stability. We provide two more decorators ti.complex_kernel and ti.complex_kernel_grad to overwrite the default automatic differentiation, as detailed in Appendix C. Apart from custom gradients, complex kernels can also be used to implement checkpointing, as detailed in Appendix D.

## Evaluation

We evaluate DiffTaichi on 10 different physical simulators covering large-scale continuum and small-scale rigid body simulations. All results can be reproduced with the provided script. The dynamic/optimization processes are visualized in the supplemental video. In this section we focus our discussions on three simulators. More details on the simulators are in Appendix E.

### Differentiable Continuum Mechanics for Elastic Objects \[diffmpm\]

First, we build a differentiable continuum simulation for soft robotics applications. The physical system is governed by momentum and mass conservation, i.e. ${{{\rho\frac{D\mathbf{v}}{Dt}} = {{\nabla \cdot \sigma} + {\rho\mathbf{g}}}},{{\frac{D\rho}{Dt} + {{\rho\nabla} \cdot \mathbf{v}}} = 0}}.$ We follow ChainQueen's implementation and use the moving least squares material point method to simulate the system. We were able to easily translate the original CUDA simulator into DiffTaichi syntax. Using this simulator and an open-loop controller, we can easily train a soft robot to move forward (Fig. 1, diffmpm).

### Performance and Productivity

Compared with manual gradient implementations , getting gradients in DiffTaichi is effortless. As a result, the DiffTaichi implementation is $4.2 \times$ shorter in terms of lines of code, and runs almost as fast; compared with TensorFlow, DiffTaichi code is $1.7 \times$ shorter and $188 \times$ faster (Table 1). The Tensorflow implementation is verbose due to the heavy use of tf.gather_nd/scatter_nd and array transposing and broadcasting.

## Lines of Code

Table 1: diffmpm performance comparison on an NVIDIA GTX 1080 Ti GPU. We benchmark in 2D using 6.4K particles. For the lines of code, we only include the essential implementation, excluding boilerplate code. [Reproduce: python3 diffmpm_benchmark.py]

### Differentiable Incompressible Fluid Simulator \[smoke\]

We implemented a smoke simulator (Fig. 1, smoke) with semi-Lagrangian advection and implicit pressure projection, following the example in Autograd. Using gradient descent optimization on the initial velocity field, we are able to find a velocity field that changes the pattern of the fluid to a target image (Fig. 7a in Appendix). We compare the performance of our system against PyTorch, Autograd, and JAX in Table 2. Note that as an example from the Autograd library, this grid-based simulator is intentionally simplified to suit traditional array-based programs. For example, a periodic boundary condition is used so that Autograd can represent it using numpy.roll, without any branching. Still, Taichi delivers higher performance than these array-based systems. The whole program takes 10 seconds to run in DiffTaichi on a GPU, and 2 seconds are spent on JIT. JAX JIT compilation takes 2 minutes.

## Essential LoC

Table 2: smoke benchmark against Autograd, PyTorch, and JAX. We used a 110 × 110 grid and 100 time steps, each with 6 Jacobi pressure projections. [Reproduce: python3 smoke_[autograd/pytorch/jax/taichi_cpu/taichi_gpu].py]. Note that the Autograd program uses float64 precision, which approximately doubles the run time.

### Differentiable rigid body simulators \[rigid_body\]

We built an impulse-based differentiable rigid body simulator (Fig. 1, rigid_body) for optimizing robot controllers. This simulator supports rigid body collision and friction, spring forces, joints, and actuation. The simulation is end-to-end differentiable except for a countable number of discontinuities. Interestingly, although the forward simulator works well, naively differentiating it with DiffTaichi leads to completely misleading gradients, due to the rigid body collisions. We discuss the cause and solution of this issue below.

### Improving collision gradients

Consider the rigid ball example in Fig. 4 (left), where a rigid ball collides with a friction-less ground. Gravity is ignored, and due to conservation of kinetic energy the ball keeps a constant speed even after this elastic collision.

In the forward simulation, using a small $\Deltat$ often leads to a reasonable result, as done in many physics simulators. Lowering the initial ball height will increase the final ball height, since there is less distance to travel before the ball hits the ground and more after (see the loss curves in Fig.4, middle right). However, using a naive time integrator, no matter how small $\Deltat$ is, the evaluated gradient of final height w.r.t. initial height will be $1$ instead of $- 1$. This counter-intuitive behavior is due to the fact that time discretization itself is not differentiated by the compiler. Fig. 4 explains this effect in greater detail.

Figure 4: How gradients can go wrong with naive time integrators. For clarity we use a large Δ t here. Left: Since collision detection only happens at multiples of Δ t (2 Δ t in this case), lowering the initial position of the ball (light blue) leads to a lowered final position. Middle Left: By improving the time integrator to support continuous time of impact (TOI), collisions can be detected at any time, e.g. 1.9 Δ t (light red). Now the blue ball ends up higher than the green one. Middle Right: Although the two time integration techniques lead to almost identical forward results (in practice Δ t is small), the naive time integrator gives an incorrect gradient of 1, but adding TOI yields the correct gradient. Please see our supplemental video for a better demonstration. [Reproduce: python3 rigid_body_toi.py] Right: When zooming, the loss of the naive integrator is decreasing, and the saw-tooth pattern explains the positive gradients. [Reproduce: python3 rigid_body_toi.py zoom] We propose a simple solution of adding continuous collision resolution (see, for example, Redon et al.), which considers precise time of impact (TOI), to the forward program (Fig. 4, middle left). Although it barely improves the forward simulation (Fig. 4, middle right), the gradient will be corrected effectively (Fig. 4, right). The details of continuous collision detection are in Appendix F. In real-world simulators, we find the TOI technique leads to significant improvement in gradient quality in controller optimization tasks (Fig. 5). Having TOI or not barely affects forward simulation: in the supplemental video, we show that a robot controller optimized in a simulator with TOI, actually works well in a simulator without TOI.

Figure 5: Adding TOI greatly improves gradient and optimization quality. Each experiment is repeated five times. [Reproduce: python3 [mass_spring/rigid_body.py] [1/2] plot && python3 plot_losses.py] The takeaway is, differentiating physical simulators does not always yield useful gradients of the physical system being simulated, even if the simulator does forward simulation well. In Appendix G, we discuss some additional gradient issues we have encountered.

## Related Work

### Differentiable programming

The recent rise of deep learning has motivated the development of differentiable programming libraries for deep NNs, most notably auto-differentiation frameworks such as Theano, TensorFlow and PyTorch. However, physical simulation requires complex and customizable operations due to the intrinsic computational irregularity. Using the aforementioned frameworks, programmers have to compose these coarse-grained basic operations into desired complex operations. Doing so often leads to unsatisfactory performance.

Earlier work on automatic differentiation focuses on transforming existing scalar code to obtain derivatives (e.g. Utke et al., Hascoet & Pascual, Pearlmutter & Siskind ). A recent trend has emerged for modern programming languages to support differentiable function transformations through annotation (e.g. Innes et al., Wei et al. ). These frameworks enable differentiating general programming languages, yet they provide limited parallelism.

Differentiable array programming languages such as Halide, Autograd, JAX, and Enoki operate on arrays instead of scalars to utilize parallelism. Instead of operating on arrays that are immutable, DiffTaichi uses an imperative style with flexible indexing to make porting existing physical simulation algorithms easier.

### Differentiable Physical Simulators

Building differentiable simulators for robotics and machine learning has recently increased in popularity. Without differentiable programming, Battaglia et al., Chang et al. and Mrowca et al. used NNs to approximate the physical process and used the NN gradients as the approximate simulation gradients. Degrave et al. and de Avila Belbute-Peres et al. used Theano and PyTorch respectively to build differentiable rigid body simulators. Schenck & Fox differentiates position-based fluid using custom CUDA kernels. Popović et al. used a differentiable rigid body simulator for manipulating physically based animations. The ChainQueen differentiable elastic object simulator implements forward and gradient versions of continuum mechanics in hand-written CUDA kernels, leading to performance that is two orders of magnitude higher than a pure TensorFlow implementation. Liang et al. built a differentiable cloth simulator for material estimation and motion control. The deep learning community also often incorporates differentiable rendering operations (OpenDR, N3MR, redner, Mitsuba 2 ) to learn from 3D scenes.

## Conclusion

We have presented DiffTaichi, a new differentiable programming language designed specifically for building high-performance differentiable physical simulators. Motivated by the need for supporting megakernels, imperative programming, and flexible indexing, we developed a tailored two-scale automatic differentiation system. We used DiffTaichi to build 10 simulators and integrated them into deep neural networks, which proved the performance and productivity of DiffTaichi over existing systems. We hope our programming language can greatly lower the barrier of future research on differentiable physical simulation in the machine learning and robotics communities.
