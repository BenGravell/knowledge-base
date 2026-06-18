<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Numba

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dynamic, interpreted languages, like Python, are attractive for domain-experts and scientists experimenting with new ideas. However, the performance of the interpreter is often a barrier when scaling to larger data sets. This paper presents a just-in-time compiler for Python that focuses in scientific and array-oriented computing. Starting with the simple syntax of Python, Numba compiles a subset of the language into efficient machine code that is comparable in performance to a traditional compiled language. In addition, we share our experience in building a JIT compiler using LLVM.
