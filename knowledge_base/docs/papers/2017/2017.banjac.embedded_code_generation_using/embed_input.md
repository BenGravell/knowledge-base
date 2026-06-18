<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Embedded Code Generation Using the OSQP Solver

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a code generation software package that accepts a parametric description of a quadratic program (QP) as input and generates tailored C code that compiles into a fast and reliable optimization solver for the QP that can run on embedded platforms. The generated code is based on OSQP, a novel open-source operator splitting solver for quadratic programming. Our software supports matrix factorization caching and warm starting, and allows updates of the problem parameters during runtime. The generated C code is library-free and has a very small compiled footprint. Examples arising in real-world applications show that the generated code outperforms state-of-the-art embedded and desktop QP solvers.
