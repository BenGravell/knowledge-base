<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Code Generation for Embedded Second-Order Cone Programming

Topics include Second-order cone programming, Code generation, Embedded optimization, Convex optimization, Disciplined convex programming.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows how high-level convex models can be compiled into lightweight parameter-mapping code for embedded SOCPs. The main idea is to separate easy-to-verify generated code from a reusable conic solver, making embedded convex optimization more practical.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes a framework for generating easily verifiable code to solve convex optimization problems in embedded applications by transforming them into equivalent second-order cone programs. In embedded applications, it is critical to be able to verify code correctness, but it is also desirable to be able to rapidly prototype and deploy high-performance solvers for different problems. To balance these two requirements, we propose a code generation system that takes high-level descriptions of convex optimization problems and generates code that maps the parameters in the original problem to data in an equivalent second-order cone program, which is then solved by a single, external solver that can be verified once and for all. A novel aspect is that we restrict the parameters in the original problem to only appear in affine functions, which lets us map the parameters to problem data without performing any floating point operations. As a result, the generated code is lightweight, fast, and trivial to verify. The approach thus marries the benefits of high-level parser/solvers with custom, high-performance, high-reliability solvers for embedded applications.
