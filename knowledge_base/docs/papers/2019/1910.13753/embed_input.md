<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

acados: A Modular Open-source Framework for Fast Embedded Optimal Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents the acados software package, a collection of solvers for fast embedded optimization intended for fast embedded applications. Its interfaces to higher-level languages make it useful for quickly designing an optimization-based control algorithm by putting together different algorithmic components that can be readily connected and interchanged. Since the core of acados is written on top of a high-performance linear algebra library, we do not sacrifice computational performance. Thus, we aim to provide both flexibility and performance through modularity, without the need to rely on automatic code generation, which facilitates maintainability and extensibility. The main features of acados are: efficient optimal control algorithms targeting embedded devices implemented in C, linear algebra based on the high-performance BLASFEO library, user-friendly interfaces to Matlab and Python, and compatibility with the modeling language of CasADi. acados is free and open-source software released under the permissive BSD 2-Clause license.
