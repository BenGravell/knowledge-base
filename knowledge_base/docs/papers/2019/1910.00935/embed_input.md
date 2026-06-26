<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DiffTaichi: Differentiable Programming for Physical Simulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present DiffTaichi, a new differentiable programming language tailored for building high-performance differentiable physical simulators. Based on an imperative programming language, DiffTaichi generates gradients of simulation steps using source code transformations that preserve arithmetic intensity and parallelism. A light-weight tape is used to record the whole simulation program structure and replay the gradient kernels in a reversed order, for end-to-end backpropagation. We demonstrate the performance and productivity of our language in gradient-based learning and optimization tasks on 10 different physical simulators. For example, a differentiable elastic object simulator written in our language is 4.2x shorter than the hand-engineered CUDA version yet runs as fast, and is 188x faster than the TensorFlow implementation. Using our differentiable programs, neural network controllers are typically optimized within only tens of iterations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Differentiable physical simulators are effective components in machine learning systems. For example, de Avila Belbute-Peres et al. and Hu et al. have shown that controller optimization with differentiable simulators converges one to four orders of magnitude faster than model-free reinforcement learning algorithms. The presence of differentiable physical simulators in the inner loop of these applications makes their performance vitally important. Unfortunately, using existing tools it is difficult to implement these simulators with high performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present DiffTaichi, a new differentiable programming language for high performance physical simulations on both CPU and GPU. It is based on the Taichi programming language.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Megakernels", "weight": 1.0} -->

Our language uses a "megakernel" approach, allowing the programmer to naturally fuse multiple stages of computation into a single kernel, which is later differentiated using source code transformations and just-in-time compilation. Compared to the linear algebra operators in TensorFlow and PyTorch, DiffTaichi kernels have higher arithmetic intensity and are therefore more efficient for physical simulation tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Imperative Parallel Programming", "weight": 1.0} -->

In contrast to functional array programming languages that are popular in modern deep learning, most traditional physical simulation programs are written in imperative languages such as Fortran and C++. DiffTaichi likewise adopts an imperative approach. The language provides parallel loops and control flows (such as "if" statements), which are widely used constructs in physical simulations: they simplify common tasks such as handling collisions, evaluating boundary conditions, and building iterative solvers. Using an imperative style makes it easier to port existing physical simulation code to DiffTaichi.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Flexible Indexing", "weight": 1.0} -->

Existing parallel differentiable programming systems provide element-wise operations on arrays of the same shape, e.g. c\[i, j\] = a\[i, j\] + b\[i, j\]. However, many physical simulation operations, such as numerical stencils and particle-grid interactions are not element-wise. Common simulation patterns such as y\[p\[i\] \* 2, j\] = x\[q\[i + j\]\] can only be expressed with unintuitive scatter/gather operations in these existing systems, which are not only inefficient but also hard to develop and maintain. On the other hand, in DiffTaichi, the programmer directly manipulates array elements via arbitrary indexing, thus allowing partial updates of global arrays and making these common simulation patterns naturally expressible. The explicit indexing syntax also makes it easy for the compiler to perform access optimizations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Flexible Indexing", "weight": 1.0} -->

The three requirements motivated us to design a tailored two-scale automatic differentiation system, which makes DiffTaichi especially suitable for developing complex and high-performance differentiable physical simulators, possibly with neural network controllers (Fig. 1, left). Using our language, we are able to quickly implement and automatically differentiate 10 physical simulators^11^1Our language, compiler, and simulator code is open-source. All the results in this work can be reproduced by a single Python script. Visual results in this work are presented in the supplemental video., covering rigid bodies, deformable objects, and fluids (Fig. 1, right). A comprehensive comparison between DiffTaichiand other differentiable programming tools is in Appendix A.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Allocating Global Variables", "weight": 1.0} -->

Firstly we allocate a set of global tensors to store the simulation state. These tensors include a scalar loss of type float32, 2D tensors x, v, force of size steps$\times$n_springs and type float32x2, and 1D arrays of size n_spring for spring properties: spring_anchor_a (int32), spring_anchor_b (int32), spring_length (float32).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Defining Kernels", "weight": 1.0} -->

The following kernel loops over all the springs and scatters forces to mass points: [⬇](data:text/plain;base64,QHRpLmtlcm5lbApkZWYgYXBwbHlfc3ByaW5nX2ZvcmNlKHQ6IHRpLmkzMik6CiAgIyBLZXJuZWxzIGNhbiBoYXZlIHBhcmFtZXRlcnMuIEhlcmUgdCBpcyBhIHBhcmFtZXRlciB3aXRoIHR5cGUgaW50MzIuCiAgZm9yIGkgaW4gcmFuZ2Uobl9zcHJpbmdzKTogIyBBIHBhcmFsbGVsIGZvciwgcHJlZmVyYWJseSBvbiBHUFUKICAgIGEsIGIgPSBzcHJpbmdfYW5jaG9yX2FbaV0sIHNwcmluZ19hbmNob3JfYltpXQogICAgeF9hLCB4X2IgPSB4W3QgLSAxLCBhXSwgeFt0IC0gMSwgYl0KICAgIGRpc3QgPSB4X2EgLSB4X2IKICAgIGxlbmd0aCA9IGRpc3Qubm9ybSgpICsgMWUtNAogICAgRiA9IChsZW5ndGggLSBzcHJpbmdfbGVuZ3RoW2ldKSAqIHNwcmluZ19zdGlmZm5lc3MgKiBkaXN0IC8gbGVuZ3RoCiAgICAjIEFwcGx5IHNwcmluZyBpbXB1bHNlcyB0byBtYXNzIHBvaW50cy4KICAgIGZvcmNlW3QsIGFdICs9IC1GICMgIis9IiBpcyBhdG9taWMgYnkgZGVmYXVsdAogICAgZm9yY2VbdCwgYl0gKz0gIEY=){download=""} def apply_spring_force(t: ti.i32): \# Kernels can have parameters. Here t is a parameter with type int32. for i in range(n_springs): \# A parallel, preferably on GPU a, b = spring_anchor_a\[i\], spring_anchor_b\[i\] length = dist.norm + 1e-4 F = (length - spring_length\[i\]) \* spring_stiffness \* dist / length \# Apply spring impulses to mass points.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Defining Kernels", "weight": 1.0} -->

The kernel is as follows: [⬇](data:text/plain;base64,QHRpLmtlcm5lbApkZWYgdGltZV9pbnRlZ3JhdGUodDogdGkuaTMyKToKICBmb3IgaSBpbiByYW5nZShuX29iamVjdHMpOgogICAgcyA9IG1hdGguZXhwKC1kdCAqIGRhbXBpbmcpICMgQ29tcGlsZS10aW1lIGV2YWx1YXRpb24gc2luY2UgZHQgYW5kIGRhbXBpbmcgYXJlIGNvbnN0YW50cwogICAgdlt0LCBpXSA9IHMgKiB2W3QgLSAxLCBpXSArIGR0ICogZm9yY2VbdCwgaV0gLyBtYXNzICMgbWFzcyA9IDEgaW4gdGhpcyBleGFtcGxlCiAgICB4W3QsIGldID0geFt0IC0gMSwgaV0gKyBkdCAqIHZbdCwgaV0=){download=""} def time_integrate(t: ti.i32): for i in range(n_objects): s = math.exp(-dt \* damping) \# Compile-time evaluation since dt and damping are constants v\[t, i\] = s \* v\[t - 1, i\] + dt \* force\[t, i\] / mass \# mass = 1 in this example

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assembling the Forward Simulator", "weight": 1.0} -->

With these components, we define the forward time integration: [⬇](data:text/plain;base64,ZGVmIGZvcndhcmQoKToKICBmb3IgdCBpbiByYW5nZSgxLCBzdGVwcyk6CiAgICBhcHBseV9zcHJpbmdfZm9yY2UodCkKICAgIHRpbWVfaW50ZWdyYXRlKHQp){download=""} for t in range(1, steps): apply_spring_force(t)

<!-- chunk {"id": "body-0013", "role": "body", "section": "Automatically Differentiating Physical Simulators in Taichi", "weight": 1.0} -->

The main goal of DiffTaichi's automatic differentiation (AD) system is to generate gradient simulators automatically with minimal code changes to the traditional forward simulators.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Design Decision", "weight": 1.0} -->

Source Code Transformation (SCT) and Tracing are common choices when designing AD systems. In our setting, using SCT to differentiate a whole simulator with thousands of time steps, results in high performance yet poor flexibility and long compilation time. On the other hand, naively adopting tracing provides flexibility yet poor performance, since the "megakernel\" structure is not preserved during backpropagation. To get both performance and flexibility, we developed a two-scale automatic differentiation system (Figure 2): we use SCT for differentiating within kernels, and use a light-weight tape that only stores function pointers and arguments for end-to-end simulation differentiation. The global tensors are natural checkpoints for gradient evaluation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption", "weight": 1.0} -->

Unlike functional programming languages where immutable output buffers are generated, imperative programming allows programmers to freely modify global tensors. To make automatic differentiation well-defined under this setting, we make the following assumption on imperative kernels: Global Data Access Rules: 1) If a global tensor element is written more than once, then starting from the second write, the write must come in the form of an atomic add ("accumulation"). 2) No read accesses happen to a global tensor element, until its accumulation is done.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption", "weight": 1.0} -->

In forward simulators, programmers may make subtle changes to satisfy the rules. For instance, in the mass-spring simulation example, we record the whole history of x and v, instead of keeping only the latest values. The memory consumption issues caused by this can be alleviated via checkpointing, as discussed later in Appendix D.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Storage Control of Adjoint Tensors", "weight": 1.0} -->

Users can specify the storage of adjoint tensors using the Taichi data structure description language, as if they are primal tensors. We also provide ti.root.lazy_grad to automatically place the adjoint tensors following the layout of their primals.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Local AD: Differentiating Taichi Kernels using Source Code Transforms", "weight": 1.0} -->

A typical Taichi kernel consists of multiple levels of for loops and a body block. To make later AD easier, we introduce two basic code transforms to simplify the loop body, as detailed below.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Local AD: Differentiating Taichi Kernels using Source Code Transforms", "weight": 1.0} -->

// eliminate mutable var Figure 3: Simple IR preprocessing before running the AD source code transform (left to right). Demonstrated in C++. The actual Taichi IR is often more complex. Containing loops are ignored.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Flatten Branching", "weight": 1.0} -->

In physical simulation branches are common, e.g., when implementing boundary conditions and collisions. To simplify the reverse-mode AD pass, we first replace "if" statements with ternary operators select(cond, value_if_true, value_if_false), whose gradients are clearly defined (Fig. 3, middle). This is a common transformation in program vectorization (e.g. Karrenberg & Hack; Pharr & Mark ).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Eliminate Mutable Local Variables", "weight": 1.0} -->

After removing branching, we end up with straight-line loop bodies. To further simplify the IR and make the procedure truly single-assignment, we apply a series of local variable store forwarding transforms, until the mutable local variables can be fully eliminated (Fig. 3, right).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Eliminate Mutable Local Variables", "weight": 1.0} -->

After these two custom IR simplification transforms, DiffTaichi only has to differentiate the straight-line code without mutable variables, which it achieves with reverse-mode AD, using a standard source code transformation. More details on this transform are in Appendix B.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Loops", "weight": 1.0} -->

Most loops in physical simulation are parallel loops, and during AD we preserve the parallel loop structures. For loops that are not explicitly marked as parallel, we reverse the loop order during AD transforms. We do not support loops that carry a mutating local variable since that would require a complex and costly run-time stack to maintain the history of local variables. Instead, users are instructed to employ global variables that satisfy the global data access rules.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Parallelism and Thread Safety", "weight": 1.0} -->

For forward simulation, we inherit the "parallel-for\" construct from Taichi to map each loop iteration onto CPU/GPU threads. Programmers use atomic operations for thread safety. Our system can automatically differentiate these atomic operations. Gradient contributions in backward kernels are accumulated to the adjoint tensors via atomic adds.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Global AD: End-to-end Backpropagation using A Light-Weight Tape", "weight": 1.0} -->

We construct a tape (Fig. 2, right) of the kernel execution so that gradient kernels can be replayed in a reversed order. The tape is very light-weight: since the intermediate results are stored in global tensors, during forward simulation the tape only records kernel names and the (scalar) input parameters, unlike other differentiable functional array systems where all the intermediate buffers have to be recorded by the tape. Whenever a DiffTaichi kernel is launched, we append the kernel function pointer and parameters to the tape. When evaluating gradients, we traverse the reversed tape, and invoke the gradient kernels with the recorded parameters. Note that DiffTaichi AD is evaluating gradients with respect to input global tensors instead of the input parameters.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Learning/Optimization with Gradients", "weight": 1.0} -->

Now we revisit the mass-spring example and make it differentiable for optimization. Suppose the goal is to optimize the rest lengths of the springs so that the triangle area formed by the three springs becomes $0.2$ at the end of the simulation. We first define the loss function: def compute_loss(t: ti.i32):

<!-- chunk {"id": "body-0027", "role": "body", "section": "Triangle area from cross product", "weight": 1.0} -->

loss[None] = ti.sqr(area - target_area)

<!-- chunk {"id": "body-0028", "role": "body", "section": "\"loss\" is a scalar (0-D tensor), thereby indexed with [None]", "weight": 1.0} -->

The programmer uses ti.Tape to memorize forward kernel launches. It automatically replays the gradients of these kernels in reverse for backpropagation. Initially the springs have lengths $\lbrack 0.1,0.1,0.14\rbrack$, and after optimization the rest lengths are $\lbrack 0.600,0.600,0.529\rbrack$. This means the springs will expand the triangle according to Hooke's law and form a larger triangle: \[Reproduce: mass_spring_simple.py\] for iter in range: with ti.Tape(loss): compute_loss(steps - 1) print(’Iter=’, iter) print(’Loss=’,loss[None])

<!-- chunk {"id": "body-0029", "role": "body", "section": "Gradient descent", "weight": 1.0} -->

for i in range(n_springs): lr * spring_length.grad[i]

<!-- chunk {"id": "body-0030", "role": "body", "section": "Complex Kernels", "weight": 1.0} -->

Sometimes the user may want to override the gradients provided by the compiler. For example, when differentiating a 3D singular value decomposition done with an iterative solver, it is better to use a manually engineered SVD derivative subroutine for better stability. We provide two more decorators ti.complex_kernel and ti.complex_kernel_grad to overwrite the default automatic differentiation, as detailed in Appendix C. Apart from custom gradients, complex kernels can also be used to implement checkpointing, as detailed in Appendix D.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We evaluate DiffTaichi on 10 different physical simulators covering large-scale continuum and small-scale rigid body simulations. All results can be reproduced with the provided script. The dynamic/optimization processes are visualized in the supplemental video. In this section we focus our discussions on three simulators. More details on the simulators are in Appendix E.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Differentiable Continuum Mechanics for Elastic Objects \\[diffmpm\\]", "weight": 1.0} -->

First, we build a differentiable continuum simulation for soft robotics applications. The physical system is governed by momentum and mass conservation, i.e. ${{{\rho\frac{D\mathbf{v}}{Dt}} = {{\nabla \cdot \sigma} + {\rho\mathbf{g}}}},{{\frac{D\rho}{Dt} + {{\rho\nabla} \cdot \mathbf{v}}} = 0}}.$ We follow ChainQueen's implementation and use the moving least squares material point method to simulate the system. We were able to easily translate the original CUDA simulator into DiffTaichi syntax. Using this simulator and an open-loop controller, we can easily train a soft robot to move forward (Fig. 1, diffmpm).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Performance and Productivity", "weight": 1.0} -->

Compared with manual gradient implementations, getting gradients in DiffTaichi is effortless. As a result, the DiffTaichi implementation is $4.2 \times$ shorter in terms of lines of code, and runs almost as fast; compared with TensorFlow, DiffTaichi code is $1.7 \times$ shorter and $188 \times$ faster (Table 1). The Tensorflow implementation is verbose due to the heavy use of tf.gather_nd/scatter_nd and array transposing and broadcasting.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Differentiable Incompressible Fluid Simulator \\[smoke\\]", "weight": 1.0} -->

We implemented a smoke simulator (Fig. 1, smoke) with semi-Lagrangian advection and implicit pressure projection, following the example in Autograd. Using gradient descent optimization on the initial velocity field, we are able to find a velocity field that changes the pattern of the fluid to a target image (Fig. 7a in Appendix). We compare the performance of our system against PyTorch, Autograd, and JAX in Table 2. Note that as an example from the Autograd library, this grid-based simulator is intentionally simplified to suit traditional array-based programs. For example, a periodic boundary condition is used so that Autograd can represent it using numpy.roll, without any branching. Still, Taichi delivers higher performance than these array-based systems. The whole program takes 10 seconds to run in DiffTaichi on a GPU, and 2 seconds are spent on JIT. JAX JIT compilation takes 2 minutes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Differentiable rigid body simulators \\[rigid_body\\]", "weight": 1.0} -->

We built an impulse-based differentiable rigid body simulator (Fig. 1, rigid_body) for optimizing robot controllers. This simulator supports rigid body collision and friction, spring forces, joints, and actuation. The simulation is end-to-end differentiable except for a countable number of discontinuities. Interestingly, although the forward simulator works well, naively differentiating it with DiffTaichi leads to completely misleading gradients, due to the rigid body collisions. We discuss the cause and solution of this issue below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Improving collision gradients", "weight": 1.0} -->

Consider the rigid ball example in Fig. 4 (left), where a rigid ball collides with a friction-less ground. Gravity is ignored, and due to conservation of kinetic energy the ball keeps a constant speed even after this elastic collision.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Improving collision gradients", "weight": 1.0} -->

In the forward simulation, using a small $\Deltat$ often leads to a reasonable result, as done in many physics simulators. Lowering the initial ball height will increase the final ball height, since there is less distance to travel before the ball hits the ground and more after (see the loss curves in Fig.4, middle right). However, using a naive time integrator, no matter how small $\Deltat$ is, the evaluated gradient of final height w.r.t. initial height will be $1$ instead of $- 1$. This counter-intuitive behavior is due to the fact that time discretization itself is not differentiated by the compiler. Fig. 4 explains this effect in greater detail.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Differentiable programming", "weight": 1.0} -->

The recent rise of deep learning has motivated the development of differentiable programming libraries for deep NNs, most notably auto-differentiation frameworks such as Theano, TensorFlow and PyTorch. However, physical simulation requires complex and customizable operations due to the intrinsic computational irregularity. Using the aforementioned frameworks, programmers have to compose these coarse-grained basic operations into desired complex operations. Doing so often leads to unsatisfactory performance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Differentiable programming", "weight": 1.0} -->

Earlier work on automatic differentiation focuses on transforming existing scalar code to obtain derivatives (e.g. Utke et al., Hascoet & Pascual, Pearlmutter & Siskind ). A recent trend has emerged for modern programming languages to support differentiable function transformations through annotation (e.g. Innes et al., Wei et al. ). These frameworks enable differentiating general programming languages, yet they provide limited parallelism.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Differentiable programming", "weight": 1.0} -->

Differentiable array programming languages such as Halide, Autograd, JAX, and Enoki operate on arrays instead of scalars to utilize parallelism. Instead of operating on arrays that are immutable, DiffTaichi uses an imperative style with flexible indexing to make porting existing physical simulation algorithms easier.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Differentiable Physical Simulators", "weight": 1.0} -->

Building differentiable simulators for robotics and machine learning has recently increased in popularity. Without differentiable programming, Battaglia et al., Chang et al. and Mrowca et al. used NNs to approximate the physical process and used the NN gradients as the approximate simulation gradients. Degrave et al. and de Avila Belbute-Peres et al. used Theano and PyTorch respectively to build differentiable rigid body simulators. Schenck & Fox differentiates position-based fluid using custom CUDA kernels. Popović et al. used a differentiable rigid body simulator for manipulating physically based animations. The ChainQueen differentiable elastic object simulator implements forward and gradient versions of continuum mechanics in hand-written CUDA kernels, leading to performance that is two orders of magnitude higher than a pure TensorFlow implementation. Liang et al. built a differentiable cloth simulator for material estimation and motion control. The deep learning community also often incorporates differentiable rendering operations (OpenDR, N3MR, redner, Mitsuba 2 ) to learn from 3D scenes.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented DiffTaichi, a new differentiable programming language designed specifically for building high-performance differentiable physical simulators. Motivated by the need for supporting megakernels, imperative programming, and flexible indexing, we developed a tailored two-scale automatic differentiation system. We used DiffTaichi to build 10 simulators and integrated them into deep neural networks, which proved the performance and productivity of DiffTaichi over existing systems. We hope our programming language can greatly lower the barrier of future research on differentiable physical simulation in the machine learning and robotics communities.
