DiffTaichi: Differentiable Programming for Physical Simulation

We present DiffTaichi, a new differentiable programming language tailored for building high-performance differentiable physical simulators. Based on an imperative programming language, DiffTaichi generates gradients of simulation steps using source code transformations that preserve arithmetic intensity and parallelism. A light-weight tape is used to record the whole simulation program structure and replay the gradient kernels in a reversed order, for end-to-end backpropagation. We demonstrate the performance and productivity of our language in gradient-based learning and optimization tasks on 10 different physical simulators. For example, a differentiable elastic object simulator written in our language is 4.2x shorter than the hand-engineered CUDA version yet runs as fast, and is 188x faster than the TensorFlow implementation. Using our differentiable programs, neural network controllers are typically optimized within only tens of iterations.

## Introduction

Differentiable physical simulators are effective components in machine learning systems. For example, de Avila Belbute-Peres et al. and Hu et al. have shown that controller optimization with differentiable simulators converges one to four orders of magnitude faster than model-free reinforcement learning algorithms. The presence of differentiable physical simulators in the inner loop of these applications makes their performance vitally important. Unfortunately, using existing tools it is difficult to implement these simulators with high performance.

We present DiffTaichi, a new differentiable programming language for high performance physical simulations on both CPU and GPU. It is based on the Taichi programming language.

## Megakernels

Our language uses a "megakernel" approach, allowing the programmer to naturally fuse multiple stages of computation into a single kernel, which is later differentiated using source code transformations and just-in-time compilation. Compared to the linear algebra operators in TensorFlow and PyTorch, DiffTaichi kernels have higher arithmetic intensity and are therefore more efficient for physical simulation tasks.

## Imperative Parallel Programming

In contrast to functional array programming languages that are popular in modern deep learning, most traditional physical simulation programs are written in imperative languages such as Fortran and C++. DiffTaichi likewise adopts an imperative approach. The language provides parallel loops and control flows (such as "if" statements), which are widely used constructs in physical simulations: they simplify common tasks such as handling collisions, evaluating boundary conditions, and building iterative solvers. Using an imperative style makes it easier to port existing physical simulation code to DiffTaichi.

## Conclusion

We have presented DiffTaichi, a new differentiable programming language designed specifically for building high-performance differentiable physical simulators. Motivated by the need for supporting megakernels, imperative programming, and flexible indexing, we developed a tailored two-scale automatic differentiation system. We used DiffTaichi to build 10 simulators and integrated them into deep neural networks, which proved the performance and productivity of DiffTaichi over existing systems.
