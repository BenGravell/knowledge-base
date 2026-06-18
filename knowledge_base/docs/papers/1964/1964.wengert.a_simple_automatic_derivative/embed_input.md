<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Simple Automatic Derivative Evaluation Program

Topics include Automatic differentiation, Symbolic differentiation, Wengert list, Forward mode, Intermediate variables, Derivatives, Scientific computing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Wengert introduces the intermediate-variable representation now called a Wengert list, avoiding expression-level derivative expansion while still applying exact chain-rule transformations. Although usually classified as automatic differentiation, the paper is central to symbolic differentiation's history because it sharpens the distinction between generating derivative expressions and evaluating derivative programs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A procedure for automatic evaluation of total/partial derivatives of arbitrary algebraic functions is presented. The technique permits computation of numerical values of derivatives without developing analytical expressions for the derivatives. The key to the method is the decomposition of the given function, by introduction of intermediate variables, into a series of elementary functional steps. A library of elementary function subroutines is provided for the automatic evaluation and differentiation of these new variables. The final step in this process produces the desired function's derivative. The main feature of this approach is its simplicity. It can be used as a quick-reaction tool where the derivation of analytical derivatives is laborious and also as a debugging tool for programs which contain derivatives.
