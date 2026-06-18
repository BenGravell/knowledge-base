DiffTaichi: Differentiable Programming for Physical Simulation

We present DiffTaichi, a new differentiable programming language tailored for building high-performance differentiable physical simulators. Based on an imperative programming language, DiffTaichi generates gradients of simulation steps using source code transformations that preserve arithmetic intensity and parallelism. A light-weight tape is used to record the whole simulation program structure and replay the gradient kernels in a reversed order, for end-to-end backpropagation. We demonstrate the performance and productivity of our language in gradient-based learning and optimization tasks on 10 different physical simulators. For example, a differentiable elastic object simulator written in our language is 4.2x shorter than the hand-engineered CUDA version yet runs as fast, and is 188x faster than the TensorFlow implementation. Using our differentiable programs, neural network controllers are typically optimized within only tens of iterations.

## Introduction

Figure 1: Left: Our language allows us to seamlessly integrate a neural network (NN) controller and a physical simulation module, and update the weights of the controller or the initial state parameterization (blue). Our simulations typically have 512 ∼ 2048 time steps, and each time step has up to one thousand parallel operations. Right: 10 differentiable simulators built with DiffTaichi.

Differentiable physical simulators are effective components in machine learning systems. For example, de Avila Belbute-Peres et al. and Hu et al. have shown that controller optimization with differentiable simulators converges one to four orders of magnitude faster than model-free reinforcement learning algorithms. The presence of differentiable physical simulators in the inner loop of these applications makes their performance vitally important. Unfortunately, using existing tools it is difficult to implement these simulators with high performance.

## Conclusion

We have presented DiffTaichi, a new differentiable programming language designed specifically for building high-performance differentiable physical simulators. Motivated by the need for supporting megakernels, imperative programming, and flexible indexing, we developed a tailored two-scale automatic differentiation system. We used DiffTaichi to build 10 simulators and integrated them into deep neural networks, which proved the performance and productivity of DiffTaichi over existing systems....

### Eliminate Mutable Local Variables

The main goal of DiffTaichi's automatic differentiation (AD) system is to generate gradient simulators automatically with minimal code changes to the traditional forward simulators.

Sometimes the user may want to override the gradients provided by the compiler. For example, when differentiating a 3D singular value decomposition done with an iterative solver, it is better to use a manually engineered SVD derivative subroutine for better stability. We provide two more decorators ti.complex_kernel and ti.complex_kernel_grad to overwrite the default automatic differentiation, as detailed in Appendix C. Apart from custom gradients, complex kernels can also be used to implement checkpointing, as detailed in Appendix D.

We present DiffTaichi, a new differentiable programming language for high performance physical simulations on both CPU and GPU....
