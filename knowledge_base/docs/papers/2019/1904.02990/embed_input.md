<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Equivalence of Automatic and Symbolic Differentiation

Topics include Symbolic differentiation, Automatic differentiation, Reverse mode, Expression swell, Expression graphs, Symbolic computation, Machine learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Laue argues that reverse-mode automatic differentiation and symbolic differentiation are operationally equivalent when symbolic differentiation is represented with sharing rather than as fully expanded expressions. The paper is useful as a modern corrective to the common teaching contrast between AD and symbolic differentiation, especially around expression swell and control flow.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that reverse mode automatic differentiation and symbolic differentiation are equivalent in the sense that they both perform the same operations when computing derivatives. This is in stark contrast to the common claim that they are substantially different. The difference is often illustrated by claiming that symbolic differentiation suffers from "expression swell" whereas automatic differentiation does not. Here, we show that this statement is not true. "Expression swell" refers to the phenomenon of a much larger representation of the derivative as opposed to the representation of the original function.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computing derivatives is a fundamental task in computer science, especially in optimization and machine learning. Most optimization schemes rely on derivative information when minimizing a function. However, computing derivatives by hand is error prone and can be a time consuming task, especially when the function to be differentiated is more complex. Hence, methods for automatically computing derivatives have been designed. The two major approaches that can be found in the literature are automatic differentiation and symbolic differentiation. Symbolic differentiation is basically what one knows from high school. Automatic differentiation refers to the fact, that one can compute derivatives even for computer programs that compute functions. Automatic differentiation is often also referred to as algorithmic differentiation. The literature and tools on automatic differentiation is extensive, see, e.g.,. Its popularity increased significantly over the last few years, especially in the area of machine learning/deep learning where it is necessary to compute gradients of loss functions of deep nets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is often claimed in the literature that automatic differentiation is *not* symbolic differentiation. To tell them apart, the phenomenon of "expression swell" is used \[10, page 3\]. However, the difference is not really explained and stays in the dark. On the other hand it is sometimes hard to put one tool into its right category, i.e., either automatic differentiation or symbolic differentiation. For instance, the Theano framework that has been widely used in the machine learning community is sometimes said to use automatic differentiation and sometimes said to use symbolic differentiation. Here, we explain why it is hard to tell both approaches apart by showing that they are in fact equivalent. They both perform the same operations when computing derivatives. The only difference they have is the underlying data structure. Automatic differentiation operates on directed acyclic graphs (DAGs) whereas symbolic differentiation operates on expression trees or expression forests if one allows common subexpressions. However, when we allow common subexpressions in symbolic differentiation, then reverse mode automatic differentiation and symbolic differentiation compute the same result.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will also show that the phenomenon of "expression swell" does *not* originate from the differentiation process but from transforming a DAG into a tree when disallowing common subexpressions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Expression Representation", "weight": 1.0} -->

By expressions we understand mathematical expressions like ${\sin{({x_{1} + x_{2}})}}{\cos{({x_{1} + x_{2}})}}$. They can be represented by expression DAGs (also known as computational graphs or execution trace), expression trees, or expression forests with common subexpressions. Figure 1 illustrates the difference for the function ${f{(x)}} = {{\sin{({x_{1} + x_{2}})}}{\cos{({x_{1} + x_{2}})}}}$. Obviously, an expression tree is also an expression DAG. On the other hand, an expression DAG can be converted into a tree simply by unfolding. The execution of a computer program results in an expression DAG. For instance, the following Python code results in the above expression DAG.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Expression Representation", "weight": 1.0} -->

When unfolding an expression DAG into an expression tree without common subexpressions it can become exponentially large. An example is given in Figure 2. However, when allowing common subexpressions it can be converted one-to-one where the resulting forest has the same size as the DAG. The following Python code corresponds to this example.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Expression Representation", "weight": 1.0} -->

Now, we see an expression swell when converting a DAG into a tree. However, this is totally independent of computing derivatives. When allowing common subexpressions, we do not see an expression swell. This expression swell is often put forward as an argument for distinguishing between automatic and symbolic differentiation. Here, we see that it is *not* connected to computing derivatives. Rather, it is a matter of the expression representation. Note, that when allowing common subexpressions such an expression swell does not occur.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Equivalence of Reverse Mode Automatic Differentiation and Symbolic Differentiation", "weight": 1.0} -->

In this section we will first review reverse mode automatic differentiation and symbolic differentiation, and then we will show their equivalence.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reverse Mode Automatic Differentiation", "weight": 1.0} -->

Given an expression DAG $D = {(V,E)}$, reverse mode automatic differentiation proceeds as follows when computing the derivative of the output function $f$. Each internal node $v_{i}$ will eventually store the derivative $\frac{\partial f}{\partial v_{i}}$ that is commonly denoted as ${\overline{v}}_{i}$. Reverse mode proceeds from output to input nodes. At the nodes representing the output function $f$, the derivative $\frac{\partial f}{\partial f}$ is stored. Then, the derivatives that are stored at the remaining nodes, here called $v_{i}$, are iteratively computed by summing over all their outgoing edges using the following equation: where the $\overline{v} = \frac{\partial f}{\partial v}$ are the partial derivatives that have been computed before and are stored at the nodes $v$. Finally, the derivative of the function $f$ with respect to all variables is stored at the corresponding input nodes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Symbolic Differentiation", "weight": 1.0} -->

Symbolic differentiation applies the following two rules iteratively to a given function in order to compute its derivative.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Symbolic Differentiation", "weight": 1.0} -->

If the function is unary, e.g., sine, cosine, etc., it applies the following rule In case of binary functions, e.g, addition, multiplication, etc., symbolic differentiation applies All rules from Calculus 101 can be reduced to these two rules. For instance, the multiplication rule is commonly known as $\frac{\partial{({uv})}}{\partial x} = {{u\frac{\partial v}{\partial x}} + {v\frac{\partial u}{\partial x}}}$. The following sequence shows that this follows from Equation. We have where the binary function $f{(.,.)}$ is the multiplication operation, $g_{1} = u$, and $g_{2} = v$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Symbolic Differentiation", "weight": 1.0} -->

Please note, that the input expression is usually stored in an expression tree or expression forest with common subexpressions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Question 1", "weight": 1.0} -->

How does symbolic differentiation proceed when encountering common subexpressions?

<!-- chunk {"id": "body-0016", "role": "body", "section": "Question 1", "weight": 1.0} -->

We illustrate this problem by the following example: Suppose we are differentiating a multiplication node $f = {uv}$. The derivative would be $\frac{\partial f}{\partial x} = {{u\frac{\partial v}{\partial x}} + {v\frac{\partial u}{\partial x}}}$. Note, that $u$ (and also $v$) appear in the original function as well as in the derivative. There are three possibilities to store the result.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Question 1", "weight": 1.0} -->

Copy the whole subtree representing $u$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Question 1", "weight": 1.0} -->

Store a pointer to the subtree representing $u$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Question 1", "weight": 1.0} -->

All three options are valid possibilities. Option 1 will result in a tree as the output, Option 2 will result in a DAG, and Option 3 in a forest where each tree represents a common subexpression. Conceptually, Option 2 and Option 3 are identical. And this is also how one would implement symbolic differentiation. It is much easier to just store a pointer to the subtree $u$ instead of copying the whole subtree $u$. And since common subexpressions are allowed, turning this into a forest with common subexpressions is also trivial.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Question 2", "weight": 1.0} -->

Consider for instance the expression $f = {u + u}$. Blindly computing the derivative would require to compute the derivative of $u$ twice. Whenever there is the need for computing the derivative of a subtree $u$, then one can simply check, if it has been done before. In this case, one does not compute it again but can reuse the old result.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Equivalence", "weight": 1.0} -->

Each internal node in an expression DAG can have either one or two incoming edges. In case a node has one incoming edge, the differentiation Rule for reverse mode automatic differentiation is equivalent to the differentiation Rule for symbolic differentiation. In case of two incoming edges, it is equivalent to rule in symbolic differentiation. So obviously, both approaches perform the same operations.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Equivalence", "weight": 1.0} -->

In symbolic differentiation, if one stores only a pointer to common subtrees, or introduces a common subexpression (Option 2 and Option 3 in Question 1) then this is exactly how automatic differentiation proceeds.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Equivalence", "weight": 1.0} -->

Furthermore, if one stores intermediate results and reuses them (Question 2) then symbolic differentiation and reverse mode automatic differentiation are identical.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Demystifying the Common Myths", "weight": 1.0} -->

It should be obvious now, that the myths that are commonly encountered when talking about automatic and symbolic differentiation are not true. The distinction between them is rather artificial. Especially, the claim of the "expression swell", i.e., careless symbolic differentiation can easily produce exponentially large expressions is not true. Instead, it will lead to the same result as reverse mode automatic differentiation when intermediate results are stored as common subexpressions. This can be done easily. Hence, also the claim that common subexpressions need to be carefully determined *after* the differentiation process is not true. They can be simply collected during the differentiation process.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Demystifying the Common Myths", "weight": 1.0} -->

When the input is a tree of size $n$, then the resulting tree of the derivative will be of size at most $O{(n)}$ when storing only pointers to common subtrees and at most $O{(n^{2})}$ when copying every subtree during the symbolic differentiation process. There is *no* exponential growth here. This misconception can be explained maybe by the following fact. When turning a DAG into a tree, one might see an exponential growth. But this is unrelated to differentiation. And if one turns a DAG into a forest with common subexpression then the size of the output stays the same (Myth 1).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Speelpenning's Example", "weight": 1.0} -->

Often, Speelpenning's example is brought forward to illustrate that symbolic differentiation is inefficient. Speelpenning's example is the following. Consider the function ${f{(x_{1},x_{2},\ldots,x_{n})}} = {x_{1}x_{2}\ldotsx_{n}}$. When computing the gradient with respect to $x = {(x_{1},x_{2},\ldots,x_{n})}$, symbolic differentiation would output It is argued that the output is unnecessary large and there are quite a number of common subexpressions that now need to be identified. This is not true. What is displayed is the final output. However, this is the final output *after* expression simplification and the removal of common subexpressions. In between, they have already been computed in the same way as in reverse mode automatic differentiation. If one looks at the individual steps when computing the derivatives symbolically, one can see that the result is exactly the same as reverse mode automatic differentiation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Speelpenning's Example", "weight": 1.0} -->

Hence, symbolic differentiation is as efficient as reverse mode automatic differentiation (Myth 4).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Speelpenning's Example", "weight": 1.0} -->

Summing up, Speelpenning's example rather serves as an example why reverse mode automatic differentiation is more efficient in case of many input variables and one output function. But the same holds true for standard symbolic differentiation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Control Structures", "weight": 1.0} -->

When using operator overloading in automatic differentiation, control structures are easily circumvented since they do not appear in the computational graph, also known as the execution trace. That is, even when the code contains control structures, the computational graph/expression DAG will not. The same reasoning also applies to symbolic differentiation (Myth 2 and 3).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have shown in this note that reverse mode automatic differentiation and symbolic differentiation are algorithmically equivalent, i.e., they both perform the same set of operations when computing derivatives. The big contribution of automatic differentiation is rather of conceptual nature. It introduced the surprising idea that one can compute the derivative of any computer program. While this is a natural, yet very smart idea in hindsight, coming up with it for sure was not trivial. It has also led to many insights and algorithmic approaches like cross-country mode, edge elimination, etc., and to automatic differentiation tools that compute derivatives of even very complex computer programs.
