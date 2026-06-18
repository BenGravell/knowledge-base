<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Compiling Machine Learning Programs via High-Level Tracing

Topics include JAX, Automatic differentiation, JIT compilation, Tracing, XLA, Machine learning systems, Python, Accelerators.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces JAX as a high-level tracing compiler that combines NumPy-style Python, Autograd-compatible transformations, and XLA code generation. Its central contribution is making automatic differentiation, JIT compilation, and accelerator execution composable enough for research workflows.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe JAX, a domain-specific tracing JIT compiler for generating high-performance accelerator code from pure Python and Numpy machine learning programs. JAX uses the XLA compiler infrastructure to generate optimized code for the program subroutines that are most favorable for acceleration, and these optimized subroutines can be called and orchestrated by arbitrary Python. Because the system is fully compatible with Autograd, it allows forward- and reverse-mode automatic differentiation of Python functions to arbitrary order. Because JAX supports structured control flow, it can generate code for sophisticated machine learning algorithms while maintaining high performance. We show that by combining JAX with Autograd and Numpy we get an easily programmable and highly performant ML system that targets CPUs, GPUs, and TPUs, capable of scaling to multi-core Cloud TPUs.
