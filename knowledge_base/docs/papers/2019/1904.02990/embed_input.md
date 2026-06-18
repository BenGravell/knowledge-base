On the Equivalence of Automatic and Symbolic Differentiation

Topics include Symbolic differentiation, Automatic differentiation, Reverse mode, Expression swell, Expression graphs, Symbolic computation, Machine learning.

Laue argues that reverse-mode automatic differentiation and symbolic differentiation are operationally equivalent when symbolic differentiation is represented with sharing rather than as fully expanded expressions. The paper is useful as a modern corrective to the common teaching contrast between AD and symbolic differentiation, especially around expression swell and control flow.

We show that reverse mode automatic differentiation and symbolic differentiation are equivalent in the sense that they both perform the same operations when computing derivatives. This is in stark contrast to the common claim that they are substantially different. The difference is often illustrated by claiming that symbolic differentiation suffers from "expression swell" whereas automatic differentiation does not. Here, we show that this statement is not true. "Expression swell" refers to the phenomenon of a much larger representation of the derivative as opposed to the representation of the original function.

## Introduction

Computing derivatives is a fundamental task in computer science, especially in optimization and machine learning. Most optimization schemes rely on derivative information when minimizing a function. However, computing derivatives by hand is error prone and can be a time consuming task, especially when the function to be differentiated is more complex. Hence, methods for automatically computing derivatives have been designed. The two major approaches that can be found in the literature are automatic differentiation and symbolic differentiation. Symbolic differentiation is basically what one knows from high school.

It is often claimed in the literature that automatic differentiation is *not* symbolic differentiation. To tell them apart, the phenomenon of "expression swell" is used \[10, page 3\]. However, the difference is not really explained and stays in the dark. On the other hand it is sometimes hard to put one tool into its right category, i.e., either automatic differentiation or symbolic differentiation. For instance, the Theano framework that has been widely used in the machine learning community is sometimes said to use automatic differentiation and sometimes said to use symbolic differentiation.

## Expression Representation

By expressions we understand mathematical expressions like ${\sin{({x_{1} + x_{2}})}}{\cos{({x_{1} + x_{2}})}}$. They can be represented by expression DAGs (also known as computational graphs or execution trace), expression trees, or expression forests with common subexpressions. Figure 1 illustrates the difference for the function ${f{(x)}} = {{\sin{({x_{1} + x_{2}})}}{\cos{({x_{1} + x_{2}})}}}$. Obviously, an expression tree is also an expression DAG. On the other hand, an expression DAG can be converted into a tree simply by unfolding. The execution of a computer program results in an expression DAG.

## Conclusion

We have shown in this note that reverse mode automatic differentiation and symbolic differentiation are algorithmically equivalent, i.e., they both perform the same set of operations when computing derivatives. The big contribution of automatic differentiation is rather of conceptual nature. It introduced the surprising idea that one can compute the derivative of any computer program. While this is a natural, yet very smart idea in hindsight, coming up with it for sure was not trivial.
