<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scalable Semidefinite Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Semidefinite programming (SDP) is a powerful framework from convex optimization that has striking potential for data science applications. This paper develops a provably correct randomized algorithm for solving large, weakly constrained SDP problems by economizing on the storage and arithmetic costs. Numerical evidence shows that the method is effective for a range of applications, including relaxations of MaxCut, abstract phase retrieval, and quadratic assignment. Running on a laptop equivalent, the algorithm can handle SDP instances where the matrix variable has over 10^ entries.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

Semidefinite programming (SDP) is a powerful framework from convex optimization that has striking potential for data science applications. This paper develops a provably correct randomized algorithm for solving large, weakly constrained SDP problems by economizing on the storage and arithmetic costs. Numerical evidence shows that the method is effective for a range of applications, including relaxations of MaxCut, abstract phase retrieval, and quadratic assignment. Running on a laptop equivalent, the algorithm can handle SDP instances where the matrix variable has over $10^{14}$ entries.

<!-- chunk {"id": "body-0004", "role": "body", "section": "keywords", "weight": 1.0} -->

Augmented Lagrangian, conditional gradient method, convex optimization, dimension reduction, first-order method, randomized linear algebra, semidefinite programming, sketching.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

For a spectrum of challenges in data science, methodologies based on semidefinite programming offer remarkable performance both in theory and for small problem instances. Even so, practitioners often critique this approach by asserting that it is impossible to solve semidefinite programs (SDPs) at the scale demanded by real-world applications. We would like to argue against this article of conventional wisdom.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

This paper proposes a new algorithm, called SketchyCGAL, that can solve very large SDPs to moderate accuracy. The algorithm marries a primal--dual optimization technique to a randomized sketch for low-rank matrix approximation. In each iteration, the primary expense is one low-precision randomized eigenvector calculation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

For every standard-form SDP that satisfies strong duality, SketchyCGAL provably converges to a near-optimal low-rank approximation of a solution. The algorithm uses limited arithmetic and minimal storage. It is most effective for weakly constrained problems whose solutions are nearly low-rank. In contrast, given the same computational resources, other methods for this class of problems may fail. In particular, SketchyCGAL needs far less storage than the Burer--Monteiro factorization heuristic for certain problem instances.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

In addition to the theoretical guarantees, we offer evidence that SketchyCGAL is a practical optimization algorithm. For example, on a laptop equivalent, we can solve the MaxCut SDP for a sparse graph with over 20 million vertices, where the matrix variable has over $10^{14}$ entries. We also tackle large phase retrieval problems arising from Fourier ptychography, as well as relaxations of the quadratic assignment problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Example: The maximum cut in a graph", "weight": 1.0} -->

To begin, we derive a fundamental SDP that arises in combinatorial optimization. This example highlights why large SDPs are hard to solve, and it illustrates the potential of our approach.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MaxCut", "weight": 1.0} -->

Consider an undirected graph $\mathsf{G} = {(\mathsf{V},\mathsf{E})}$ comprising a vertex set $\mathsf{V} = {\{ 1,\ldots,n\}}$ and a set $\mathsf{E}$ of $m$ edges. The combinatorial Laplacian of the graph is the real positive-semidefinite (psd) matrix where $\mathbf{e}_{i} \in {\mathbb{R}}^{n}$ denotes the $i$th standard basis vector and ^∗^ refers to the (conjugate) transpose of a matrix or vector.

<!-- chunk {"id": "body-0011", "role": "body", "section": "MaxCut", "weight": 1.0} -->

We can search for a maximum-weight cut in the graph by solving Unfortunately, the formulation Eq. 1.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is NP-hard. One remedy is to relax it to an SDP.

<!-- chunk {"id": "body-0012", "role": "body", "section": "MaxCut", "weight": 1.0} -->

Consider the matrix ${\mathbf{X}} = {{\mathbf{χ}}{\mathbf{χ}}^{\ast}}$ where ${\mathbf{χ}} \in {\{{\pm 1}\}}^{n}$. The matrix $\mathbf{X}$ is psd; its diagonal entries equal one; and it has rank one. We can express the MaxCut problem Eq. 1.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0013", "role": "body", "section": "MaxCut", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") in terms of the matrix $\mathbf{X}$ by rewriting the objective as a trace. Bringing forward the implicit constraints on $\mathbf{X}$ and dropping the rank constraint, we arrive at the MaxCut SDP: As usual, $diag$ extracts the diagonal of a matrix as a vector, and $\mathbf{1} \in {\mathbb{R}}^{n}$ is the vector of ones.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MaxCut", "weight": 1.0} -->

The matrix solution ${\mathbf{X}}_{\star}$ of Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") does not immediately yield a cut.

<!-- chunk {"id": "body-0015", "role": "body", "section": "MaxCut", "weight": 1.0} -->

In many cases, the cut ${\mathbf{χ}}_{\star}$ yields an excellent solution to the discrete MaxCut problem Eq. 1.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0016", "role": "body", "section": "MaxCut", "weight": 1.0} -->

We can also use ${\mathbf{X}}_{\star}$ to compute a cut that is provably near-optimal via a more involved randomized rounding procedure.

<!-- chunk {"id": "body-0017", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

We specify an instance of the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") by means of the Laplacian $\mathbf{L}$ of the graph, which has $\mathcal{O}{({m + n})}$ nonzero entries.

<!-- chunk {"id": "body-0018", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

Our goal is to compute a best rank-one approximation of a solution to the SDP, which has $\mathcal{O}{(n)}$ degrees of freedom. In other words, the total cost of representing the input and output of the problem is $\mathcal{O}{({m + n})}$. Sadly, the matrix variable in Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0019", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") seems to require storage $\mathcal{O}{(n^{2})}$. For example, a graph $\mathsf{G}$ with one million vertices leads to an SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0020", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") with a trillion real variables.

<!-- chunk {"id": "body-0021", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

Storage is one of the main reasons that it has been challenging to solve large instances of the MaxCut SDP reliably. Undeterred, we raise a question: > *Can we provably find a best rank-one approximation of a solution to the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0022", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") with storage $\mathcal{O}{({m + n})}$? Can we achieve working storage $\mathcal{O}{(n)}$?* We are not aware of any correct algorithm that can solve an arbitrary instance of Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0023", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") with a working storage guarantee better than $\Theta{({\min{\{ m,n^{3/2}\}}})}$; see Section 8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0024", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0025", "role": "body", "section": "What's the issue?", "weight": 1.0} -->

In addition to the limit on storage, a good algorithm should interact with the Laplacian $\mathbf{L}$ only through noninvasive, low-cost operations, such as matrix--vector multiplication.

<!-- chunk {"id": "body-0026", "role": "body", "section": "A storage-optimal algorithm for the MaxCut SDP", "weight": 1.0} -->

Surprisingly, it is possible to achieve all the goals announced in the last subsection.

<!-- chunk {"id": "body-0027", "role": "body", "section": "A model problem", "weight": 1.0} -->

SketchyCGAL can solve all standard-form SDPs that satisfy strong duality. To simplify parts of the presentation, we focus on a model problem that includes an extra trace constraint. Appendix D under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") extends SketchyCGAL to a more expressive problem template that includes standard-form SDPs with additional (conic) inequality constraints.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The trace-constrained SDP", "weight": 1.0} -->

We always assume that Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") satisfies strong duality with its standard-form dual problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The trace-constrained SDP", "weight": 1.0} -->

To solve a general standard-form SDP, we replace the inclusion ${\mathbf{X}} \in {\alpha\mathbf{\Delta}_{n}}$ with the constraints that $\mathbf{X}$ is psd and ${{tr}{({\mathbf{X}})}} \leq \alpha$ for a large enough parameter $\alpha$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Applications", "weight": 1.0} -->

The model problem Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") has diverse applications in statistics, signal processing, quantum information theory, combinatorics, and beyond.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Applications", "weight": 1.0} -->

Evidently, the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is a special case.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Applications", "weight": 1.0} -->

The template Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") includes problems in computer vision, in microscopy, and in robotics. It also supports contemporary machine learning tasks, such as certifying robustness of neural networks. There is a galaxy of other examples.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Complexity of SDP formulations and solutions", "weight": 1.0} -->

This section describes some special features that commonly appear in large, real-world SDPs. Our algorithm will take advantage of these features, even as it provides guarantees for every instance of Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0034", "role": "body", "section": "Structure of the problem data", "weight": 1.0} -->

The matrices $\mathbf{C}$ and ${\mathbf{A}}_{i}$ that appear in Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") are often highly structured, or sparse, or have low-rank. As such, we can specify the SDP using a small amount of information.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Structure of the problem data", "weight": 1.0} -->

In our work, we exploit this property by treating the problem data for the SDP Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") as a collection of black boxes that support specific linear algebraic operations. The algorithm for solving the SDP only needs to access the data via these black boxes, and we can insist that these subroutines are implemented efficiently.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Low-rank solutions of SDPs", "weight": 1.0} -->

We will also capitalize on the fact that SDPs frequently have low-rank solutions, or the solutions are approximated well by low-rank matrices. There are several reasons why we can make this surmise.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Weakly-constrained SDPs", "weight": 1.0} -->

First, many SDPs have low-rank solutions just because they are weakly constrained. That is, the number $d$ of linear equalities in Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is much smaller than the number $n^{2}$ of components in the matrix variable.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Weakly-constrained SDPs", "weight": 1.0} -->

This situation often occurs in signal processing and statistics problems, where $d$ reflects the amount of measured data. SketchyCGAL is designed for weakly constrained SDPs, but it does not require this property.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Weakly-constrained SDPs", "weight": 1.0} -->

A weakly constrained SDP has at least one low-rank solution because of the geometry of the set of psd matrices; see \[18, Prop. II(13.4) and Prob. II.14.5\] and.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Fact 1 (Barvinok--Pataki)", "weight": 1.0} -->

When ${\mathbb{F}} = {\mathbb{R}}$, the SDP Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") has a solution with rank $r \leq \sqrt{2{({d + 1})}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Fact 1 (Barvinok--Pataki)", "weight": 1.0} -->

For example, the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") admits a solution with rank $\sqrt{2{({n + 1})}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Fact 1 (Barvinok--Pataki)", "weight": 1.0} -->

Although a weakly-constrained SDP can have solutions with high rank, a *generic* weakly-constrained SDP has a unique solution, which must be low-rank.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Fact 2 (Alizadeh et al.)", "weight": 1.0} -->

Let ${\mathbb{F}} = {\mathbb{R}}$. Except for a set of matrices $\{\mathbf{C},\mathbf{A}_{1},\ldots,\mathbf{A}_{d}\}$ with measure zero, the solution set of the SDP Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Fact 2 (Alizadeh et al.)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is a unique matrix with rank $r \leq \sqrt{2{({d + 1})}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Matrix rank minimization", "weight": 1.0} -->

Second, some SDPs are *designed* to produce a low-rank matrix that satisfies a system of linear matrix equations. This idea can be traced to the control theory literature, and it was explored thoroughly in Fazel's thesis. Early applications include Euclidean distance matrix completion and collaborative filtering. Extensive empirical work indicates that these SDPs often produce low-rank solutions.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Structural properties", "weight": 1.0} -->

There are other reasons that an SDP must have a low-rank solution. For instance, consider the optimal power flow SDPs developed by Lavaei and Low, where the rank of the solution is controlled by the geometry of the power grid.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithms?", "weight": 1.0} -->

To summarize, many realistic SDPs have structured data, and they admit solutions that are (close to) low rank. Are there algorithms that can exploit these features? Although there are a number of methods that attempt to do so, none can provably solve every SDP with limited arithmetic and minimal storage. See Section 8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for related work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithms?", "weight": 1.0} -->

Why has it been so difficult to develop provably correct algorithms for finding low-rank solutions to structured SDPs? Most approaches that try to control the rank run headlong into a computational complexity barrier: For any fixed rank parameter $r$, it is NP-hard to solve the model problem Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithms?", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") if the variable $\mathbf{X}$ is also constrained to be a rank-$r$ matrix \[40, p. 7\].

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithms?", "weight": 1.0} -->

To escape this sticky fact, we revise the computational goal, following. The key insight is to seek a rank-$r$ matrix that *approximates a solution* to Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithms?", "weight": 1.0} -->

See Section 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for a detailed explanation. This shift in perspective opens up new algorithmic prospects.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Contributions", "weight": 1.0} -->

Inspired, we derive an algorithm that harnesses the favorable properties common in large SDPs. The SketchyCGAL algorithm solves the SDP Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") using a primal--dual optimization method developed by a subset of the authors.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Contributions", "weight": 1.0} -->

Each iteration requires one coarse eigenvector computation and leads to a rank-one update of the psd matrix variable. Instead of storing this matrix, we maintain a compressed representation by means of a matrix sketching technique. After the optimization algorithm terminates, we extract from the sketch a low-rank approximation of a solution of the SDP. This idea leads to a practical, provably correct SDP solver that economizes on storage and arithmetic.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Section 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") presents an abstract framework for studying SDPs that exposes the challenges associated with large problems.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Section 3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Roadmap", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") outlines a primal--dual algorithm, called CGAL, for the model problem Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0057", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Sections 4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Roadmap", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and 5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") introduce methods from randomized linear algebra that we use to control storage and arithmetic costs.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Section 6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") develops the SketchyCGAL algorithm, its convergence theory, and its resource usage guarantees.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Section 7 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Roadmap", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") contains a numerical study of SketchyCGAL, and Section 8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") covers related work.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Scalable semidefinite programming", "weight": 1.0} -->

To solve the model problem Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") efficiently, we need to exploit structure inherent in the problem data. This section outlines an abstract approach that directs our attention to the core computational difficulties.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Abstract form of the model problem", "weight": 1.5} -->

Let us instate compact notation for the linear constraints in the model problem Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0064", "role": "body", "section": "Abstract form of the model problem", "weight": 1.5} -->

Form the vector ${\mathbf{b}}:={(b_{1},\ldots,b_{d})} \in {\mathbb{R}}^{d}$ of constraint values. In this notation, Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Abstract form of the model problem", "weight": 1.5} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") becomes Problem instances are parameterized by the tuple $({\mathbf{C}},\mathcal{A},{\mathbf{b}},\alpha)$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

Let ${\mathbf{X}}_{\star}$ be a solution to the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0067", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

For $\varepsilon \geq 0$, we say that a matrix ${\mathbf{X}}_{\varepsilon}$ is *$\varepsilon$-optimal* for Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") when Many optimization algorithms aim to produce such $\varepsilon$-optimal points; cf. Section 8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0069", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

As we saw in Section 1.3.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), there are many situations where the solutions to Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") have low rank or they admit accurate low-rank approximations. The $\varepsilon$-optimal points inherit these properties for sufficiently small $\varepsilon$. This insight suggests a new computational goal.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

For a rank parameter $r$, we will seek a rank-$r$ matrix $\hat{\mathbf{X}}$ that approximates an $\varepsilon$-optimal point ${\mathbf{X}}_{\varepsilon}$. More precisely, for a fixed suboptimality parameter $\zeta > 0$, we want Given Eq. 2.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Approximate solutions", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), if the $\varepsilon$-optimal point ${\mathbf{X}}_{\varepsilon}$ is close to *any* rank-$r$ matrix, then the rank-$r$ approximate solution $\hat{\mathbf{X}}$ is also close to the $\varepsilon$-optimal point ${\mathbf{X}}_{\varepsilon}$. This formulation is advantageous because it is easier to compute and to store the low-rank matrix $\hat{\mathbf{X}}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Black-box presentation of problem data", "weight": 1.0} -->

To develop scalable algorithms for Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), it is productive to hide the internal complexity of the problem instance from the algorithm.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Black-box presentation of problem data", "weight": 1.0} -->

To do so, we treat $\mathbf{C}$ and $\mathcal{A}$ as black boxes that support three primitive computations: The vectors ${\mathbf{u}} \in {\mathbb{R}}^{n}$ and ${\mathbf{z}} \in {\mathbb{R}}^{d}$ are arbitrary. Although these functions may seem abstract, they are often quite natural and easy to implement well. For example, see Section 2.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Black-box presentation of problem data", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0077", "role": "body", "section": "Black-box presentation of problem data", "weight": 1.0} -->

We will formulate algorithms for Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Black-box presentation of problem data", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") that interact with the problem data only through the operations Eq. 2.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0079", "role": "body", "section": "Black-box presentation of problem data", "weight": 1.0} -->

We tacitly assume that the primitives require minimal storage and arithmetic; otherwise, it may be impossible to develop a truly efficient algorithm.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Example: The MaxCut SDP", "weight": 1.0} -->

To provide a concrete example, let us summarize the meaning of the primitives and the desired storage costs for solving the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0081", "role": "body", "section": "Example: The MaxCut SDP", "weight": 1.0} -->

The primitive $\text{➊}:{{\mathbf{u}}\mapsto{- {{\mathbf{L}}{\mathbf{u}}}}}$. In the typical case that the Laplacian $\mathbf{L}$ is sparse, this amounts to a sparse matrix--vector multiply.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Example: The MaxCut SDP", "weight": 1.0} -->

The MaxCut SDP has $n$ linear constraints, and we seek a rank-one approximation of the solution. Thus, we desire an algorithm that operates with $\Theta{(n)}$ working storage.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Example: The MaxCut SDP", "weight": 1.0} -->

Note that we still need $\Theta{(m)}$ numbers to store the Laplacian $\mathbf{L}$ of a generic graph with $m$ edges. But we do not charge the optimization algorithm for this storage because the algorithm only interacts with $\mathbf{L}$ through the primitives Eq. 2.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Example: The MaxCut SDP", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0085", "role": "body", "section": "An algorithm for the model problem", "weight": 1.0} -->

We will develop a scalable method for the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") by enhancing an existing algorithm, called CGAL, developed by a subset of the authors. This method works well, but it is not as scalable as we would like because it lacks storage and arithmetic guarantees. This section summarizes the CGAL method and its convergence properties.

<!-- chunk {"id": "body-0086", "role": "body", "section": "An algorithm for the model problem", "weight": 1.0} -->

Subsequent sections introduce additional ideas that we need to control resource usage, culminating with the SketchyCGAL algorithm in Section 6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0087", "role": "body", "section": "The augmented problem", "weight": 1.0} -->

For a parameter $\beta > 0$, we revise the problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0088", "role": "body", "section": "The augmented problem", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") by introducing an extra term in the objective: The original problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0089", "role": "body", "section": "The augmented problem", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and the augmented problem Eq. 3.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") share the same optimal value and optimal set.

<!-- chunk {"id": "body-0090", "role": "body", "section": "The augmented problem", "weight": 1.0} -->

But the new formulation has several benefits: the augmented objective cooperates with the affine constraint to penalize infeasible points, and the dual of the augmented problem is smooth, whereas the dual of the original problem is not. See \[20, Ch. 2\] for background.

<!-- chunk {"id": "body-0091", "role": "body", "section": "The augmented Lagrangian", "weight": 1.0} -->

We construct the Lagrangian $L_{\beta}$ of the augmented problem Eq. 3.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0092", "role": "body", "section": "The augmented Lagrangian", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") by introducing a dual variable ${\mathbf{y}} \in {\mathbb{R}}^{d}$ and promoting the affine constraint: For reference, note that the partial derivatives of the augmented Lagrangian $L_{\beta}$ satisfy We attempt to minimize the augmented Lagrangian $L_{\beta}$ with respect to the primal variable $\mathbf{X}$, while we attempt to maximize with respect to the dual variable $\mathbf{y}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "The augmented Lagrangian strategy", "weight": 1.0} -->

The form of the augmented Lagrangian suggests an algorithm. We generate a sequence $\{{({\mathbf{X}}_{t};{\mathbf{y}}_{t})}\}$ of primal--dual pairs by alternately minimizing over the primal variable $\mathbf{X}$ and taking a gradient step in the dual variable $\mathbf{y}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "The augmented Lagrangian strategy", "weight": 1.0} -->

As we proceed, we can also increase the smoothing parameter $\beta$ to make violations of the affine constraint in Eq. 3.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") more and more intolerable.

<!-- chunk {"id": "body-0095", "role": "body", "section": "The augmented Lagrangian strategy", "weight": 1.0} -->

The augmented Lagrangian strategy is powerful, but it is hard to apply in this setting because of the cost of implementing the primal step, even approximately.

<!-- chunk {"id": "body-0096", "role": "body", "section": "The CGAL iteration", "weight": 1.0} -->

The CGAL iteration is related to the augmented Lagrangian paradigm, but the primal steps are inspired by the conditional gradient method. CGAL identifies an update direction for the primal variable by minimizing a linear proxy for the augmented Lagrangian. We take a small primal step in the update direction, and we improve the dual variable by taking a small gradient step. At each iteration, the smoothing parameter increases according to a fixed schedule.

<!-- chunk {"id": "body-0097", "role": "body", "section": "The CGAL iteration", "weight": 1.0} -->

This subsection outlines the steps in the CGAL iteration. Afterward, we give *a priori* guarantees on the convergence rate. Pseudocode for CGAL appears as Algorithm 1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0098", "role": "body", "section": "The CGAL iteration", "weight": 1.0} -->

1:Problem data for Eq. 2.2 implemented via the primitives Eq. 2.4; number T of iterations 4: Scale problem data (Section 7.1.1) ⊳ [opt] Recommended! 5: β0 ← 1 and K ← +∞ ⊳ Default parameters 8: $\beta\leftarrow{\beta_{0}\sqrt{t + 1}}$ and η ← 2/(t + 1) 9: (ξ, v) ← ApproxMinEvec (C + 𝒜* (y + β (𝒜 X − b)); qt) ⊳ Algorithm 2 with qt = t1/4 log n 10:⊳ Implement with primitives Eq. 2.4➊➋! 12: y ← y + γ (𝒜 X − b) ⊳ Step size γ satisfies Eq. 3.8 Algorithm 1 CGAL for the model problem Eq. 2.2

<!-- chunk {"id": "body-0099", "role": "body", "section": "Initialization", "weight": 1.0} -->

Let $\beta_{0} > 0$ be an initial smoothing parameter, and fix a (large) bound $K > 0$ on the maximum allowable size of the dual variable. We also assume that we have access to the norm $\|\mathcal{A}\|$ of the constraint matrix, or---failing that---a *lower* bound. Begin with an arbitrary choice ${\mathbf{X}}_{1} \in {\mathbb{S}}_{n}$ for the primal variable; set the initial dual variable ${\mathbf{y}}_{1} = \mathbf{0}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Primal updates via linear minimization", "weight": 1.0} -->

At iteration $t = {1,2,3,\ldots}$, we increase the smoothing parameter to $\beta_{t}:={\beta_{0}\sqrt{t + 1}}$, and we form the partial derivative of the augmented Lagrangian with respect to the primal variable at the current pair of iterates: Then we compute an update ${\mathbf{H}}_{t} \in {\alpha\mathbf{\Delta}_{t}}$ by finding the feasible point that is most correlated with the negative gradient $- {\mathbf{D}}_{t}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Primal updates via linear minimization", "weight": 1.0} -->

Next, update the matrix primal variable by taking a small step in the direction ${\mathbf{H}}_{t}$: The appeal of this approach is that it only requires a single eigenvector computation Eq. 3.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0102", "role": "body", "section": "Primal updates via linear minimization", "weight": 1.0} -->

Moreover, we need not compute the eigenvector accurately; see Section 3.4.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for details.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Dual updates via gradient ascent", "weight": 1.0} -->

Next, we update the dual variable by taking a small gradient step on the dual variable in the augmented Lagrangian: The dual step size $\gamma_{t}$ is the largest number that satisfies the conditions We omit the dual step if it makes the dual variable too large. More precisely, if Eqs. 3.7 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Dual updates via gradient ascent", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and 3.8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Dual updates via gradient ascent", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") result in ${\|{\mathbf{y}}_{t + 1}\|} > K$, then we set ${\mathbf{y}}_{t + 1} = {\mathbf{y}}_{t}$ instead. This is the CGAL iteration.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

Given a primal--dual pair $({\mathbf{X}}_{t};{\mathbf{y}}_{t})$, we can assess the quality of the primal solution to the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0107", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

First, note that we can simply compute the infeasibility: ${\mathcal{A}{\mathbf{X}}_{t}} - {\mathbf{b}}$. Second, we can bound the suboptimality of the primal objective value. To do so, define the *surrogate duality gap* The latter expression follows from Eqs. 3.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and 3.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). As usual, $\lambda_{\min}$ is the minimum eigenvalue.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

The suboptimality of ${\mathbf{X}}_{t}$ is bounded as where ${\mathbf{X}}_{\star}$ is a primal optimal point. See Section A.7 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for the derivation of Eq. 3.10 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0111", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

For CGAL, the surrogate duality gap Eq. 3.9 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is analogous to the Frank--Wolfe duality gap. It offers a practical tool for detecting early convergence.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

Unfortunately, we have not been able to prove that the CGAL error bound Eq. 3.10 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") converges to zero as the algorithm converges.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Approximate eigenvector computations", "weight": 1.0} -->

A crucial fact is that the CGAL strategy provably works if we replace Eq. 3.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") with an approximate minimum eigenvector computation.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Approximate eigenvector computations", "weight": 1.0} -->

At step $t$, suppose that we find an update direction for a unit vector ${\mathbf{v}}_{t} \in {\mathbb{F}}^{n}$. The matrix ${\mathbf{H}}_{t}$ defined in Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Approximate eigenvector computations", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") serves in place of a solution to Eq. 3.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") throughout the algorithm.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Approximate eigenvector computations", "weight": 1.0} -->

We discuss solvers for the subproblem Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Approximate eigenvector computations", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") in Section 4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0118", "role": "body", "section": "Convergence guarantees for CGAL", "weight": 1.0} -->

The following result describes the convergence of the CGAL iteration. The analysis is adapted from \[112, Thm. 3.1\]; see Appendix A under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for details and a recapitulation of the proof.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

Assume problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") satisfies strong duality.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

The CGAL iteration (Section 3.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")) with approximate eigenvector computations Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") yields a sequence ${\{\mathbf{X}_{t}:{t = {1,2,3,\ldots}}\}} \subset {\alpha\mathbf{\Delta}_{n}}$ that satisfies The matrix $\mathbf{X}_{\star}$ solves Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of

<!-- chunk {"id": "body-0123", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). The constant depends on the problem data $(\mathbf{C},\mathcal{A},\mathbf{b},\alpha)$, the minimum Euclidean norm of a dual solution, and the algorithm parameters $\beta_{0}$ and $K$.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

In view of Eq. 3.12. ‣ 3.5 Convergence guarantees for CGAL ‣ 3 An algorithm for the model problem ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020. \fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), CGAL produces a primal iterate ${\mathbf{X}}_{T}$ that is $\varepsilon$-optimal after $T = {\mathcal{O}{(\varepsilon^{- 2})}}$ iterations. The numerical work in \[112, Sec. 5\] shows that CGAL finds an $\varepsilon$-optimal point after $T = {\mathcal{O}{(\varepsilon^{- 1})}}$ iterations for realistic problem instances.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

See also Section E.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0127", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

The analysis behind Fact 3. ‣ 3.5 Convergence guarantees for CGAL ‣ 3 An algorithm for the model problem ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020. \fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") indicates that CGAL converges more quickly if we pre-condition the problem data by rescaling; see Section 7.1.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Fact 3 (CGAL: Convergence)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). This step is critical in practice.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Approximate eigenvectors", "weight": 1.0} -->

Most of the computation in CGAL occurs in the approximate eigenvector step Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). This section describes our approach to this subproblem.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Krylov methods", "weight": 1.0} -->

The approximate minimum eigenvector computation Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") involves a matrix of the form ${\mathbf{D}}_{t} = {{\mathbf{C}} + {\mathcal{A}^{\ast}{\mathbf{w}}_{t}}}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Krylov methods", "weight": 1.0} -->

We can multiply the matrix ${\mathbf{D}}_{t}$ by a vector using the primitives Eq. 2.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")➊➋.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Krylov methods", "weight": 1.0} -->

Krylov methods compute eigenvectors of ${\mathbf{D}}_{t}$ by repeated matrix--vector multiplication with ${\mathbf{D}}_{t}$, so they are obvious tools for the subproblem Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0134", "role": "body", "section": "Krylov methods", "weight": 1.0} -->

Unfortunately, CGAL tends to generate matrices ${\mathbf{D}}_{t}$ that have clustered eigenvalues. These matrices challenge standard eigenvector software, such as ARPACK, the engine behind the Matlab command eigs. Instead, we retreat to a more classical technique.

<!-- chunk {"id": "body-0135", "role": "body", "section": "A storage-optimal randomized Lanczos method", "weight": 1.0} -->

We use a nonstandard implementation of the randomized Lanczos method to find an approximate eigenvector with minimal storage. This hinges on two ideas. First, we run the Lanczos iteration with a random initial vector, which supports convergence guarantees. Second, we do not store the Lanczos vectors, but rather regenerate them to construct the approximate eigenvector. See Algorithm 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0136", "role": "body", "section": "A storage-optimal randomized Lanczos method", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for pseudocode. Kuczyński & Woźniakowski \[61, Thm. 4.2(a)\] have obtained error bounds.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Fact 4 (Randomized Lanczos method)", "weight": 1.0} -->

Let $\mathbf{M} \in {\mathbb{S}}_{n}$. For $\varepsilon \in {(0,1\rbrack}$ and $\delta \in {(0,0.5\rbrack}$, the randomized Lanczos method, Algorithm 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Fact 4 (Randomized Lanczos method)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), computes a unit vector $\mathbf{u} \in {\mathbb{F}}^{n}$ that satisfies after $q \geq {\frac{1}{2} + {\varepsilon^{- {1/2}}{\log{({n/\delta^{2}})}}}}$ iterations. The arithmetic cost is at most $q$ matrix--vector multiplies with $\mathbf{M}$ and $\mathcal{O}{({qn})}$ extra operations. The working storage is $\mathcal{O}{({n + q})}$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Fact 4 (Randomized Lanczos method)", "weight": 1.0} -->

With constant probability, we solve the eigenvector problem Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Fact 4 (Randomized Lanczos method)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") successfully in every iteration $t$ of CGAL if we use $q_{t} = {\mathcal{O}{({t^{1/4}{\log{({tn})}}})}}$ iterations of Algorithm 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Fact 4 (Randomized Lanczos method)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). In practice, we implement CGAL with $q_{t} = {t^{1/4}{\log n}}$. Although the Lanczos method has complicated numerical behavior in finite-precision arithmetic, it serves well as a subroutine within CGAL.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Remark 4.1 (Time--storage tradeoff)", "weight": 1.0} -->

We can retain the vectors $\mathbf{v}_{i}$ in Algorithm 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") to reduce the flop count by approximately a factor two, but the storage increases to $\mathcal{O}{({qn})}$.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Remark 4.1 (Time--storage tradeoff)", "weight": 1.0} -->

1:Input matrix M ∈ 𝕊n and maximum number q of iterations 2:Approximate minimum eigenpair (ξ, v) ∈ ℝ × 𝔽n of the matrix M 5: v1 ← v1/∥v1∥ ⊳ Store v1 for reuse 6: for i ← 1, 2, 3, …, min {q, n − 1} do ⊳ During loop, store only vi and vi + 1 8: vi + 1 ← M vi − ωi vi − ρi − 1 vi − 1 ⊳ Three-term Lanczos recurrence; ρ0 v0 = 0 10: if ρi = 0 then break ⊳ Found an invariant subspace! 12: T ← tridiag (ρ1: (i − 1), ω1: i, ρ1: (i − 1)) ⊳ Form tridiagonal matrix 13: [ξ, u] ← MinEvec (T) ⊳ Exploit tridiagonal form [83, Ch.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Remark 4.1 (Time--storage tradeoff)", "weight": 1.0} -->

7], or just use eig 14: ${\mathbf{v}}\leftarrow{\sum_{j = 1}^{i}{u_{j}{\mathbf{v}}_{j}}}$ ⊳ Modify lines 4–9 to regenerate v2, …, vi and form sum Algorithm 2 ApproxMinEvec via storage-optimal randomized Lanczos (Section 4.2).

<!-- chunk {"id": "body-0145", "role": "body", "section": "Sketching and reconstruction of a psd matrix", "weight": 1.0} -->

The CGAL iteration generates a psd matrix that solves the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Sketching and reconstruction of a psd matrix", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") via a sequence Eq. 3.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") of rank-one linear updates.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Sketching and reconstruction of a psd matrix", "weight": 1.0} -->

To control storage costs, SketchyCGAL retains only a compressed version of the psd matrix variable ${\mathbf{X}}_{t}$. This section outlines the *Nyström sketch*, an established method that can track the evolving psd matrix and then report a provably accurate low-rank approximation.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Sketching and reconstruction of a psd matrix", "weight": 1.0} -->

For more information about the implementation and behavior of low-rank matrix approximation from streaming data, see Appendix B under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and our papers.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Sketching and updates", "weight": 1.0} -->

Consider a psd input matrix ${\mathbf{X}} \in {\mathbb{S}}_{n}$. Let $R$ be a parameter that modulates the storage cost of the sketch and the quality of the matrix approximation.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Sketching and updates", "weight": 1.0} -->

To construct the Nyström sketch, we draw and fix a standard normal^11^1Each entry of the matrix is an independent Gaussian random variable with mean zero and variance one. In the complex setting, the real and imaginary parts of each entry are independent standard normal variables. test matrix $\mathbf{\Omega} \in {\mathbb{F}}^{n \times R}$. Our summary, or *sketch*, of the matrix $\mathbf{X}$ takes the form The sketch $\mathbf{S}$ supports linear rank-one updates to $\mathbf{X}$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Sketching and updates", "weight": 1.0} -->

and the sketch $\mathbf{S}$ require storage of $2Rn$ numbers in $\mathbb{F}$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Sketching and updates", "weight": 1.0} -->

The arithmetic cost of the linear update Eq. 5.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") to the sketch is $\Theta{({Rn})}$ numerical operations.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Remark 5.1 (Structured random matrices)", "weight": 1.0} -->

We can reduce storage costs by a factor of two by using a structured random matrix in place of $\mathbf{\Omega}$. For example, see \[104, Sec. 3\] or.

<!-- chunk {"id": "body-0154", "role": "body", "section": "The reconstruction process", "weight": 1.0} -->

Given the test matrix $\mathbf{\Omega}$ and the sketch ${\mathbf{S}} = {{\mathbf{X}}\mathbf{\Omega}}$, we form a rank-$R$ approximation $\hat{\mathbf{X}}$ of the sketched matrix $\mathbf{X}$. The approximation is defined by where ^†^ is the pseudoinverse. This reconstruction is called a *Nyström approximation*. We often truncate $\hat{\mathbf{X}}$ by replacing it with its best rank-$r$ approximation ${⟦\hat{\mathbf{X}}⟧}_{r}$ for some $r \leq R$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "The reconstruction process", "weight": 1.0} -->

See Algorithm 3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0156", "role": "body", "section": "The reconstruction process", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for a numerically stable implementation of the Nyström approximation Eq. 5.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0157", "role": "body", "section": "The reconstruction process", "weight": 1.0} -->

The algorithm takes $\Theta{({R^{2}n})}$ numerical operations and $\Theta{({Rn})}$ storage.

<!-- chunk {"id": "body-0158", "role": "body", "section": "The reconstruction process", "weight": 1.0} -->

1:Dimension n of input matrix, size R of sketch 2:Rank-R approximation $\hat{\mathbf{X}}$ of sketched matrix in factored form $\hat{\mathbf{X}} = {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}$, where U ∈ 𝔽n × R has orthonormal columns and Λ ∈ ℝR × R is nonnegative diagonal 3:function NystromSketch.Init(n, R) 4: Ω ← randn (n, R) ⊳ Draw and fix random test matrix 5: S ← zeros (n, R) ⊳ Form sketch of zero matrix 6:function NystromSketch.RankOneUpdate(v, η) ⊳ Implements Eq. 5.2 7: S ← (1 − η) S + η v (v* Ω) ⊳ Update sketch of matrix 8:function NystromSketch.Reconstruct

<!-- chunk {"id": "body-0159", "role": "body", "section": "The reconstruction process", "weight": 1.0} -->

$\sigma\leftarrow{\sqrt{n}\text{eps}\left({\text{norm}({\mathbf{S}})} \right)}$ ⊳ Compute a shift parameter 10: Sσ ← S + σ Ω ⊳ Implicitly form sketch of X + σ I 12: [U, Σ, ∼] ← svd (Sσ/L) ⊳ Dense SVD 13: Λ ← max {0, Σ2 − σ I} ⊳ Remove shift Algorithm 3 NystromSketch implementation (see Section 5)

<!-- chunk {"id": "body-0160", "role": "body", "section": "A priori error bounds", "weight": 1.0} -->

The Nyström approximation $\hat{\mathbf{X}}$ yields a provably good estimate for the matrix $\mathbf{X}$ contained in the sketch \[102, Thm. 4.1\].

<!-- chunk {"id": "body-0161", "role": "body", "section": "Fact 5 (Nyström sketch: Error bound)", "weight": 1.0} -->

Fix a psd matrix $\mathbf{X} \in {\mathbb{S}}_{n}$. Let $\mathbf{S} = {\mathbf{X}\mathbf{\Omega}}$ where $\mathbf{\Omega} \in {\mathbb{F}}^{n \times R}$ is standard normal. For each $r < {R - 1}$, the Nyström approximation Eq. 5.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Fact 5 (Nyström sketch: Error bound)", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") satisfies where ${\mathbb{E}}_{\mathbf{\Omega}}$ is the expectation with respect to $\mathbf{\Omega}$. If we replace $\hat{\mathbf{X}}$ with its rank-$r$ truncation ${⟦\hat{\mathbf{X}}⟧}_{r}$, the error bound Eq. 5.4. ‣ 5.3 A priori error bounds ‣ 5 Sketching and reconstruction of a psd matrix ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Fact 5 (Nyström sketch: Error bound)", "weight": 1.0} -->

\fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") remains valid. Similar results hold with high probability.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Scalable semidefinite programming via SketchyCGAL", "weight": 1.0} -->

We may now present an extension of CGAL that solves the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") with controlled storage and computation.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Scalable semidefinite programming via SketchyCGAL", "weight": 1.0} -->

Our new algorithm, SketchyCGAL, enhances the CGAL iteration from Section 3.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0166", "role": "body", "section": "Scalable semidefinite programming via SketchyCGAL", "weight": 1.0} -->

Instead of storing the matrix ${\mathbf{X}}_{t}$ in the CGAL iteration, We drive the iteration with the $d$-dimensional primal state variable ${\mathbf{z}}_{t}:={\mathcal{A}{\mathbf{X}}_{t}}$.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Scalable semidefinite programming via SketchyCGAL", "weight": 1.0} -->

We maintain a Nyström sketch of the primal iterate ${\mathbf{X}}_{t}$ using storage $\Theta{({Rn})}$.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Scalable semidefinite programming via SketchyCGAL", "weight": 1.0} -->

When the iteration is halted, say at time $T$, we use the sketch to construct a rank-$R$ approximation ${\hat{\mathbf{X}}}_{T}$ of the implicitly computed solution ${\mathbf{X}}_{T}$ of the model problem.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Scalable semidefinite programming via SketchyCGAL", "weight": 1.0} -->

As we will see, the resulting method exhibits almost the same convergence behavior as the CGAL algorithm, but it also enjoys a strong storage guarantee (when $d \ll n^{2}$ and $R \ll n$).

<!-- chunk {"id": "body-0170", "role": "body", "section": "The SketchyCGAL iteration", "weight": 1.0} -->

To develop the SketchyCGAL iteration, we start with the CGAL iteration. Then we make the substitutions ${\mathbf{z}}_{t} = {\mathcal{A}{\mathbf{X}}_{t}}$ and ${\mathbf{h}}_{t} = {\mathcal{A}{\mathbf{H}}_{t}}$ to eliminate the matrix variables. Let us summarize what happens; see Section 6.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0171", "role": "body", "section": "The SketchyCGAL iteration", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for additional explanation. Algorithm 4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") contains pseudocode with implementation recommendations.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Primal updates", "weight": 1.0} -->

At iteration $t = {1,2,3,\ldots}$, we compute a unit-norm vector ${\mathbf{v}}_{t}$ that is an approximate minimum eigenvector of the gradient ${\mathbf{D}}_{t}$ of the smoothed objective: This calculation corresponds with Eq. 3.11 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Primal updates", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0174", "role": "body", "section": "Primal updates", "weight": 1.0} -->

Form the primal update direction ${\mathbf{h}}_{t} = {\mathcal{A}{({\alpha{\mathbf{v}}_{t}{\mathbf{v}}_{t}^{\ast}})}}$, and then update the primal state variable ${\mathbf{z}}_{t}$ and the sketch ${\mathbf{S}}_{t}$: We obtain the update rule for the primal state variable ${\mathbf{z}}_{t}$ by applying the linear map $\mathcal{A}$ to the primal update rule Eq. 3.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA

<!-- chunk {"id": "body-0175", "role": "body", "section": "Primal updates", "weight": 1.0} -->

Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Primal updates", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). The update rule for the sketch ${\mathbf{S}}_{t}$ follows from Eq. 5.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Primal updates", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0178", "role": "body", "section": "Dual updates", "weight": 1.0} -->

The update to the dual variable takes the form where we choose the largest $\gamma_{t}$ that satisfies the conditions If needed, we set $\gamma_{t} = 0$ to prevent ${\|{\mathbf{y}}_{t + 1}\|} > K$. This is the SketchyCGAL iteration.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Dual updates", "weight": 1.0} -->

1:Problem data for Eq. 2.2 implemented via the primitives Eq. 2.4, sketch size R, number T of iterations 2:Rank-R approximate solution to Eq. 2.2 in factored form ${\hat{\mathbf{X}}}_{T} = {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}$, where U ∈ 𝔽n × R has orthonormal columns and Λ ∈ ℝR × R is nonnegative diagonal 4: Scale problem data (Section 7.1.1) ⊳ [opt] Recommended! 5: β0 ← 1 and K ← +∞ ⊳ Default parameters 9: $\beta\leftarrow{\beta_{0}\sqrt{t + 1}}$ and η ← 2/(t + 1) 10: [ξ, v] ← ApproxMinEvec (C + 𝒜* (y + β (z − b)); qt) ⊳ Algorithm 2 with qt = t1/4 log n 11:⊳ Implement with primitives Eq. 2.4➊➋!

<!-- chunk {"id": "body-0180", "role": "body", "section": "Dual updates", "weight": 1.0} -->

13: y ← y + γ (z − b) ⊳ γ is the largest solution to Eq. 6.4 14: NystromSketch.RankOneUpdate($\sqrt{\alpha}{\mathbf{v}}$, η) 16: Λ ← Λ + (α − tr(Λ)) IR/R ⊳ [opt] Enforce trace constraint in Eq. 2.2 Algorithm 4 SketchyCGAL for the model problem Eq. 2.2

<!-- chunk {"id": "body-0181", "role": "body", "section": "Connection with CGAL", "weight": 1.0} -->

There is a tight connection between the iterates of SketchyCGAL and CGAL. Let ${\mathbf{X}}_{1}:=\mathbf{0}$. Using the vectors ${\mathbf{v}}_{t}$ computed in Eq. 6.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Connection with CGAL", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), define matrices With these definitions, the following loop invariants are in force: By comparing Sections 6.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Connection with CGAL", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and 3.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Connection with CGAL", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we see that the trajectory $\{{({\mathbf{X}}_{t},{\mathbf{H}}_{t},{\mathbf{y}}_{t})}:{t = {1,2,3,\ldots}}\}$ could also have been generated by running the CGAL iteration. In other words, the variables in SketchyCGAL track the variables of some invocation of CGAL and inherit their behavior. We refer to the matrices ${\mathbf{X}}_{t}$ as the *implicit* CGAL iterates.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Approximating the CGAL iterates", "weight": 1.0} -->

We do not have access to the implicit CGAL iterates described above. Nevertheless, the sketch permits us to approximate them! After iteration $t$ of SketchyCGAL, we can form a rank-$R$ approximation ${\hat{\mathbf{X}}}_{t}$ of the implicit iterate ${\mathbf{X}}_{t}$ by invoking the formula Eq. 5.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Approximating the CGAL iterates", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") with ${\mathbf{S}} = {\mathbf{S}}_{t}$. According to Fact 5. ‣ 5.3 A priori error bounds ‣ 5 Sketching and reconstruction of a psd matrix ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Approximating the CGAL iterates", "weight": 1.0} -->

\fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Approximating the CGAL iterates", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), for each $r < {R - 1}$, In other words, the computed approximation ${\hat{\mathbf{X}}}_{t}$ is a good proxy for the implicit iterate ${\mathbf{X}}_{t}$ whenever the latter matrix is well-approximated by a low-rank matrix.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Approximating the CGAL iterates", "weight": 1.0} -->

The same bound Eq. 6.7 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") holds if we replace ${\hat{\mathbf{X}}}_{t}$ by the truncated rank-$r$ matrix ${⟦{\hat{\mathbf{X}}}_{t}⟧}_{r}$.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Remark 6.1 (Trace correction)", "weight": 1.0} -->

The model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") requires the matrix variable to have trace $\alpha$, but the computed solution ${\hat{\mathbf{X}}}_{t}$ rarely satisfies this constraint.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Remark 6.1 (Trace correction)", "weight": 1.0} -->

Algorithm 4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") includes an optional projection step (line 13) that corrects the trace.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Remark 6.1 (Trace correction)", "weight": 1.0} -->

This step never increases the error in the Nyström approximation by more than a factor of two (Section B.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")). Our analysis of SketchyCGAL *does not* include the projection, but it is valuable in practice.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

Given quantities computed by SketchyCGAL, we can assess how well the implicit iterate ${\mathbf{X}}_{t}$ solves the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0194", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

The surrogate duality gap Eq. 3.9 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") takes the form In practice, we use Eq. 6.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") to approximate the minimum eigenvalue: ${\lambda_{\min}{({\mathbf{D}}_{t})}} \approx \xi_{t}$. In light of Eq. 3.10 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we can bound the suboptimality of ${\mathbf{X}}_{t}$ via the expression where ${\mathbf{X}}_{\star}$ is a primal optimal point. See Section C.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Assessing solution quality", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for more details.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Convergence of SketchyCGAL", "weight": 1.0} -->

The implicit iterates ${\mathbf{X}}_{t}$ converge to a solution of the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") at the same rate as the iterates of CGAL would.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Convergence of SketchyCGAL", "weight": 1.0} -->

On average, the rank-$R$ iterates ${\hat{\mathbf{X}}}_{t}$ track the implicit iterates. The discrepancy between them depends on how well the implicit iterates are approximated by low-rank matrices. Here is a simple convergence result that reflects this intuition; see Section C.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Convergence of SketchyCGAL", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for the easy proof and further results.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Resource usage", "weight": 1.0} -->

The arithmetic bottleneck in SketchyCGAL comes from the approximate eigenvector computation Eq. 6.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Resource usage", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."); see Section 4.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for resource requirements. The remaining computation takes place in the variable updates.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Resource usage", "weight": 1.0} -->

To form the primal update direction ${\mathbf{h}}_{t}$, we invoke the primitive Eq. 2.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")➌.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Resource usage", "weight": 1.0} -->

To update the primal state variable ${\mathbf{z}}_{t}$ and the sketch ${\mathbf{S}}_{t}$ in Eq. 6.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we need $\mathcal{O}{({d + {Rn}})}$ arithmetic operations.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Resource usage", "weight": 1.0} -->

No further storage is required at this stage.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Resource usage", "weight": 1.0} -->

Table 1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") documents the cost of performing $T$ iterations of the SketchyCGAL method. The first column summarizes the resources consumed in the outer iteration.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Resource usage", "weight": 1.0} -->

The second column tabulates the total resources spent to solve the eigenvalue problem Eq. 6.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Resource usage", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") via the randomized Lanczos method (Algorithm 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")).

<!-- chunk {"id": "body-0210", "role": "body", "section": "Resource usage", "weight": 1.0} -->

In light of Facts 3. ‣ 3.5 Convergence guarantees for CGAL ‣ 3 An algorithm for the model problem ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020. \fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Resource usage", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") and 6.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Resource usage", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we can be confident that the implicit iterate ${\mathbf{X}}_{T}$ is $\varepsilon$-optimal within $T = {\mathcal{O}{(\varepsilon^{- 2})}}$ iterations. The formula Eq. 6.7 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Resource usage", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") gives *a priori* guarantees on the quality of the approximation ${\hat{\mathbf{X}}}_{T}$.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Theoretical performance of SketchyCGAL", "weight": 1.0} -->

We can package up this discussion in a theorem that describes the theoretical performance of the SketchyCGAL method.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

This section showcases computational experiments that establish that SketchyCGAL is a practical method for solving large SDPs. We show that the algorithm is flexible by applying it to several classes of SDPs, and we show it is reliable by solving a large number of instances of each type. We give empirical evidence that the (implicit) iterates converge to optimality much faster than Theorem 6.3. ‣ 6.5 Theoretical performance of SketchyCGAL ‣ 6 Scalable semidefinite programming via SketchyCGAL ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

\fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") suggests. Comparisons with other general-purpose SDP solvers demonstrate that SketchyCGAL is competitive for small SDPs, while it scales to problems that standard methods cannot handle.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Setup", "weight": 1.0} -->

All experiments are performed in Matlab_R2018a with double-precision arithmetic. Source code is included with the supplementary material. To simulate the processing power of a personal laptop computer, we use a single Intel Xeon CPU E5-2630 v3, clocked at 2.40 GHz, with RAM usage capped at 16 GB.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Setup", "weight": 1.0} -->

Arithmetic costs are measured in terms of actual run time. Matlab does not currently offer a memory profiler, so we externally monitor the total memory allocated. We approximate the storage cost by reporting the peak value minus the storage at Matlab's idle state.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Problem scaling", "weight": 1.0} -->

The bounds in the convergence theorem Fact 3. ‣ 3.5 Convergence guarantees for CGAL ‣ 3 An algorithm for the model problem ‣ Scalable Semidefinite ProgrammingSubmitted to the editors 6 December 2019. Revised on 18 January 2020, 24 July 2020 and 12 November 2020. \fundingVC and AY have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Problem scaling", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for the implicit iterates of SketchyCGAL depend on problem scaling. Our analysis motivates us to set In our experiments, we enforce the scalings Eq. 7.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Problem scaling", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), except where noted.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Implementation", "weight": 1.0} -->

Our experiments require a variant of SketchyCGAL that can handle inequality constraints; see Appendix D under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). We implement the algorithm with the default parameters ($\beta_{0} = 1$ and $K = {+ \infty}$). The sketch uses a Gaussian test matrix.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Implementation", "weight": 1.0} -->

The eigenvalue subproblem is solved via randomized Lanczos (Algorithm 2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")).

<!-- chunk {"id": "body-0224", "role": "body", "section": "Implementation", "weight": 1.0} -->

We include the optional trace normalization (line 13 in Algorithm 4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")) whenever appropriate. No other tuning is done.

<!-- chunk {"id": "body-0225", "role": "body", "section": "The MaxCut SDP", "weight": 1.0} -->

We begin with MaxCut SDPs Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). Our goal is to assess the storage and arithmetic costs of SketchyCGAL for a standard testbed. We compare with provable solvers for general SDPs: SEDUMI, SDPT3, MOSEK, and SDPNAL+.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Rounding", "weight": 1.0} -->

To extract a cut from an approximate solution to Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we apply a simple rounding procedure.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Rounding", "weight": 1.0} -->

SketchyCGAL returns a matrix $\hat{\mathbf{X}} = {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}$, where ${\mathbf{U}} \in {\mathbb{R}}^{n \times R}$ has orthonormal columns. The columns of the entrywise signum, ${sgn}{({\mathbf{U}})}$, are the signed indicators of $R$ cuts. We compute the weights of all $R$ cuts and select the largest. The other solvers return a full-dimensional solution $\hat{\mathbf{X}}$; we compute the top $R$ eigenvectors of $\hat{\mathbf{X}}$ using the Matlab command eigs and invoke the same rounding procedure.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Datasets", "weight": 1.0} -->

We consider datasets from two different benchmark groups: Gset: 67 binary-valued matrices generated by an autonomous random graph generator and published online. The dimension $n$ varies from $800$ to $10\, 000$.: This benchmark consists of 150 symmetric matrices (with $n$ varying from $39$ to $50\, 912\, 018$) chosen for the $10$th Dimacs Implementation Challenge. We consider 148 datasets with dimension $n \leq 24\, 000\, 000$. Two problems (rgg_n_2_24_s0 and Europe_osm) exceeded the 16 GB storage limit.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Storage and arithmetic comparisons", "weight": 1.0} -->

We run each solver for each dataset and measure the storage cost and the runtime. We invoke SketchyCGAL with rank parameter $R = 10$, and we stop the algorithm when the error bound Eq. 6.8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Storage and arithmetic comparisons", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") guarantees that the implicit iterates have both relative suboptimality and infeasibility below $10^{- 1}$. For other solvers, we set the relative error tolerance to $10^{- 1}$. See Appendix E under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Storage and arithmetic comparisons", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for implementation details.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Empirical convergence rates", "weight": 1.0} -->

Next, we investigate the empirical convergence of SketchyCGAL and the effect of the sketch size parameter $R$. We consider the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for the G67 dataset ($n = 10\, 000$), the largest instance in Gset.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Empirical convergence rates", "weight": 1.0} -->

We run $10^{6}$ iterations of SketchyCGAL for each $R \in {\{ 10,25,100\}}$.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Empirical convergence rates", "weight": 1.0} -->

We use a high-accuracy solution from SDPT3 to approximate an optimal point ${\mathbf{X}}_{\star}$ of Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0235", "role": "body", "section": "Empirical convergence rates", "weight": 1.0} -->

Given a prospective solution $\mathbf{X}$, we compute its relative suboptimality and feasibility as It is standard to increment the denominator by one to handle small values gracefully. These quantities are evaluated with respect to the original (not rescaled) problem data.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Empirical convergence rates", "weight": 1.0} -->

Fig. 7.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") also displays the weight of the cut obtained after rounding, compared with the weight of the cut obtained from the SDPT3 solution. Observe that sketch size $R = 10$ is sufficient, and the SketchyCGAL solutions yield excellent cuts after a few hundred iterations.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Primal--dual convergence", "weight": 1.0} -->

We have observed empirically that convergence occurs for the implicit primal sequence $({\mathbf{X}}_{t})$, the dual sequence $({\mathbf{y}}_{t})$, and the posterior error bound Eq. 6.8 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") generated by SketchyCGAL.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Primal--dual convergence", "weight": 1.0} -->

See Section E.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for numerical evidence.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Hard MaxCut instances", "weight": 1.0} -->

Waldspurger & Waters construct instances of the MaxCut SDP Eq. 1.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Hard MaxCut instances", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") that are challenging for algorithms based on the Burer--Monteiro factorization heuristic (Section 8.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")).

<!-- chunk {"id": "body-0241", "role": "body", "section": "Hard MaxCut instances", "weight": 1.0} -->

Each instance has a unique solution and the solution has rank $1$, but Burer--Monteiro methods require factorization rank $R = {\Theta{(\sqrt{n})}}$, resulting in storage cost $\Theta{(n^{3/2})}$. In Section E.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Hard MaxCut instances", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we give numerical evidence that SketchyCGAL can solve these instances with sketch size $R = 2$, achieving the optimal storage $\Theta{(n)}$. We confirm that Burer--Monteiro usually fails in the optimal-storage regime.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Abstract phase retrieval", "weight": 1.5} -->

Phase retrieval is the problem of reconstructing a complex-valued signal from intensity-only measurements. It arises in interferometry, speech processing, array imaging, microscopy, and many other applications. We will outline a standard method for performing phase retrieval by means of an SDP.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Abstract phase retrieval", "weight": 1.5} -->

This section uses synthetic instances of a phase retrieval SDP to compare the scaling behavior of SketchyCGAL and CGAL. We also consider a third algorithm ThinCGAL, inspired, that maintains a thin SVD of the matrix variable via rank-one updates.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Phase retrieval SDPs", "weight": 1.0} -->

Let ${\mathbf{χ}}_{\natural} \in {\mathbb{C}}^{n}$ be an unknown (discrete) signal. For known vectors ${\mathbf{a}}_{i} \in {\mathbb{C}}^{n}$, we acquire measurements of the form Abstract phase retrieval is the challenging problem of recovering ${\mathbf{χ}}_{\natural}$ from $\mathbf{b}$.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Phase retrieval SDPs", "weight": 1.0} -->

Let us summarize a lifting approach introduced by Balan et al.. The key idea is to replace the signal vector ${\mathbf{x}}_{\natural}$ by the matrix ${\mathbf{X}}_{\natural} = {{\mathbf{χ}}_{\natural}{\mathbf{χ}}_{\natural}^{\ast}}$. Then rewrite Eq. 7.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Phase retrieval SDPs", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") as Promoting the implicit constraints on ${\mathbf{X}}_{\natural}$ and forming the ${\mathbf{A}}_{i}$ into a linear map $\mathcal{A}$, we can express the problem of finding ${\mathbf{X}}_{\natural}$ as a feasibility problem with a matrix variable: To reach a tractable convex formulation, we pass to a trace minimization SDP: The parameter $\alpha$ is an upper bound on the signal energy ${\|{\mathbf{χ}}_{\natural}\|}^{2}$, which can be estimated from the observed data $\mathbf{b}$; see for the details.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Phase retrieval SDPs", "weight": 1.0} -->

We can solve the SDP Eq. 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") via SketchyCGAL.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Rounding", "weight": 1.0} -->

Suppose that we have obtained an approximate solution $\mathbf{X}$ to Eq. 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0250", "role": "body", "section": "Rounding", "weight": 1.0} -->

To estimate the signal ${\mathbf{χ}}_{\natural}$, we form the vector ${\mathbf{χ}} = {\sqrt{\lambda}{\mathbf{u}}}$ where $(\lambda,{\mathbf{u}})$ is a maximum eigenpair of $\mathbf{X}$. Both SketchyCGAL and ThinCGAL return eigenvalue decompositions, so this step is trivial. For CGAL, we use the Matlab function eigs to perform this computation.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

We consider synthetic phase retrieval instances. For each $n \in {\{ 10^{2},10^{3},\ldots,10^{6}\}}$, we generate $20$ independent datasets as follows. First, draw ${\mathbf{χ}}_{\natural} \in {\mathbb{C}}^{n}$ from the complex standard normal distribution. Then acquire $d = {12n}$ phaseless measurements Eq. 7.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") using the coded diffraction pattern model; see Section F.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0253", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

The induced linear maps $\mathcal{A}$ and $\mathcal{A}^{\ast}$ can be applied via the fast Fourier transform (FFT).

<!-- chunk {"id": "body-0254", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

The relative error in a signal reconstruction $\mathbf{χ}$ is given by $\min_{\phi \in {\mathbb{R}}}{{\|{{e^{i\phi}{\mathbf{χ}}} - {\mathbf{χ}}_{\natural}}\|}/{\|{\mathbf{χ}}_{\natural}\|}}$. In the SDP Eq. 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we set $\alpha = {3n}$ to demonstrate insensitivity of the algorithm to the choice of $\alpha$.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Storage and arithmetic comparisons", "weight": 1.0} -->

For each algorithm, we report the storage cost and runtime required to produce a signal estimate $\mathbf{χ}$ with (exact) relative error below $10^{- 2}$. We invoke SketchyCGAL with sketch size parameter $R = 5$.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Phase retrieval in microscopy", "weight": 1.0} -->

Next, we study a more realistic phase retrieval problem that arises from a type of microscopy system called Fourier ptychography (FP). Phase retrieval SDPs offer a potential approach to FP imaging. This section shows that SketchyCGAL can successfully solve the difficult phase retrieval SDPs that arise from FP.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Fourier ptychography", "weight": 1.0} -->

FP microscopes circumvent the physical limits of a simple lens to achieve high-resolution and wide field-of-view simultaneously. To do so, an FP microscope illuminates a sample from many angles and uses a simple lens to collect low-resolution intensity-only images. The measurements are low-pass filters, whose transfer functions depend on the lens and the angle of illumination. From the data, we form a high-resolution image by solving a phase retrieval problem; e.g., via the SDP Eq. 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Fourier ptychography", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0260", "role": "body", "section": "Fourier ptychography", "weight": 1.0} -->

The high-resolution image of the sample is represented by a Fourier-domain vector ${\mathbf{χ}}_{\natural} \in {\mathbb{C}}^{n}$. We acquire $d$ intensity-only measurements of the form Eq. 7.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Fourier ptychography", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), where $d$ is the total number of pixels in the low-resolution illuminations. The low-pass measurements are encoded in vectors ${\mathbf{a}}_{i}$. The operators $\mathcal{A}$ and $\mathcal{A}^{\ast}$, built from the matrices ${\mathbf{A}}_{i} = {{\mathbf{a}}_{i}{\mathbf{a}}_{i}^{\ast}}$, can be applied via the FFT.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

The authors of provided transmission matrices ${\mathbf{A}}_{i}$ of a working FP system. We simulate this system in the computer environment to acquire noiseless intensity-only measurements of a high-resolution target image. In this setup, ${\mathbf{χ}}_{\natural} \in {\mathbb{C}}^{n}$ corresponds to the Fourier transform of an $n = 320^{2} = 102\, 400$ pixel grayscale image. We normalize ${\mathbf{χ}}_{\natural}$ so that ${\|{\mathbf{χ}}_{\natural}\|} = 1$. We acquire $225$ low-resolution illuminations of the original image, each with $64^{2} = 4\, 096$ pixels. The total number of measurements is $d = 921\, 600$.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

We evaluate the error of an estimate $\mathbf{χ}$ as in Section 7.3.3 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0264", "role": "body", "section": "Dataset and evaluation", "weight": 1.0} -->

Although we know that the signal energy equals $1$, it is more realistic to approximate the signal energy by setting $\alpha = 1.5$ in the SDP Eq. 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0265", "role": "body", "section": "FP imaging", "weight": 1.0} -->

We solve the phase retrieval SDP Eq. 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") by performing $10\, 000$ iterations of SketchyCGAL with rank parameter $R = 5$.

<!-- chunk {"id": "body-0266", "role": "body", "section": "FP imaging", "weight": 1.0} -->

The top eigenvector of the output gives an approximation ${\mathbf{χ}} \in {\mathbb{C}}^{n}$ of the signal. The inverse Fourier transform of $\mathbf{χ}$ is the desired image.

<!-- chunk {"id": "body-0267", "role": "body", "section": "The quadratic assignment problem", "weight": 1.0} -->

The quadratic assignment problem (QAP) is a very difficult combinatorial optimization problem that includes the traveling salesman, max-clique, bandwidth problems, and many others as special cases. SDP relaxations offer a powerful approach for obtaining good solutions to large QAP problems. In this section, we demonstrate that SketchyCGAL can solve these challenging SDPs.

<!-- chunk {"id": "body-0268", "role": "body", "section": "QAP", "weight": 1.0} -->

We begin with the simplest form of the QAP. Fix symmetric $\mathtt{n} \times \mathtt{n}$ matrices ${{\mathbf{A}},{\mathbf{B}}} \in {\mathbb{S}}_{\mathtt{n}}$ where $\mathtt{n}$ is a natural number. We wish to "align" the matrices by solving Recall that a permutation matrix $\mathbf{\Pi}$ has precisely one nonzero entry in each row and column, and that nonzero entry equals one. A brute force search over the $\mathtt{n}!$ permutation matrices of size $\mathtt{n}$ quickly becomes intractable as $\mathtt{n}$ grows.

<!-- chunk {"id": "body-0269", "role": "body", "section": "QAP", "weight": 1.0} -->

Unsurprisingly, the QAP problem Eq. 7.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is NP-hard. Instances with $\mathtt{n} > 30$ usually cannot be solved in reasonable time.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Relaxations", "weight": 1.0} -->

The constraint ${\mathcal{G}{(\mathsf{Y})}} \geq \mathsf{0}$ enforces nonnegativity of a subset of the entries in $\mathsf{Y}$. In the Zhao et al. relaxation, $\mathcal{G}$ is the identity map, so it yields $\mathcal{O}{(\mathtt{n}^{4})}$ constraints. We reduce the complexity by choosing $\mathcal{G}$ more carefully. In our formulation, $\mathcal{G}$ extracts precisely the nonzero entries of the matrix ${\mathbf{B}} \otimes \mathbf{1}\mathbf{1}^{\ast}$. This is beneficial because $\mathbf{B}$ is sparse in many applications.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Relaxations", "weight": 1.0} -->

For example, in traveling salesman and bandwidth problems, $\mathbf{B}$ has $\mathcal{O}{(\mathtt{n})}$ nonzero entries, so the map $\mathcal{G}$ produces only $\mathcal{O}{(\mathtt{n}^{3})}$ constraints.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Relaxations", "weight": 1.0} -->

The main variable $\mathsf{Y}$ in Eq. 7.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") has dimension $\mathtt{n}^{2} \times \mathtt{n}^{2}$.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Relaxations", "weight": 1.0} -->

As a consequence, the problem has $\mathcal{O}{(\mathtt{n}^{4})}$ degrees of freedom, together with $\mathcal{O}{(\mathtt{n}^{3})}$ to $\mathcal{O}{(\mathtt{n}^{4})}$ constraints (depending on $\mathcal{G}$). The explosive growth of this relaxation scuttles most algorithms by the time $\mathtt{n} > 50$. To solve larger instances, many researchers resort to even weaker relaxations.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Relaxations", "weight": 1.0} -->

In contrast, we can solve the relaxation Eq. 7.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") directly using SketchyCGAL, up to $\mathtt{n} = 150$. By limiting the number of inequality constraints, via the operator $\mathcal{G}$, we achieve substantial reductions in resource usage.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Relaxations", "weight": 1.0} -->

We validate our algorithm on QAPs where the exact solution is known, and we compare the performance with algorithms for other relaxations.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Rounding", "weight": 1.0} -->

Given an approximate solution to Eq. 7.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we use a rounding method to construct a permutation.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Rounding", "weight": 1.0} -->

SketchyCGAL returns a matrix $\hat{\mathbf{X}} = {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\ast}}$ where $\mathbf{U}$ has dimension ${({\mathtt{n}^{2} + 1})} \times R$. We extract the first column of $\mathbf{U}$, discard its first entry and reshape the remaining part into an $\mathtt{n} \times \mathtt{n}$ matrix. Then we project this matrix onto the set of permutation matrices via the Hungarian method.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Rounding", "weight": 1.0} -->

This yields a feasible point $\mathbf{\Pi}$ for the problem Eq. 7.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0279", "role": "body", "section": "Rounding", "weight": 1.0} -->

We repeat this procedure for all $R$ columns of $\mathbf{U}$, and we pick the one that minimizes ${tr}{({{\mathbf{A}}\mathbf{\Pi}{\mathbf{B}}\mathbf{\Pi}^{\ast}})}$. This permutation gives an upper bound on the optimal value of Eq. 7.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Rounding", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0281", "role": "body", "section": "Datasets and evaluation", "weight": 1.0} -->

We consider instances from QAPLIB and TSPLIB that are used. The optimal values are known, and the permutation size $\mathtt{n}$ varies between $12$ and $150$. (Recall that the SDP matrix dimension $n = {\mathtt{n}^{2} + 1}$.) We report

<!-- chunk {"id": "body-0282", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

To solve Eq. 7.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."), we cannot use the scaling Eq. 7.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") because $\|\mathcal{A}\|$ is not available; see the source code for our approach. We apply SketchyCGAL with sketch size $R = \mathtt{n}$, so the sketch uses storage $\Theta{(\mathtt{n}^{3})}$.

<!-- chunk {"id": "body-0285", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

After rounding, a low- or medium-accuracy solution of Eq. 7.6 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") often provides a better permutation than a high-accuracy solution. Therefore, we applied the rounding step at iterations $2,4,8,16,\ldots$ and tracked the quality of the best permutation attained on the solution path.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

We stopped after (the first of) $10^{6}$ iterations or $72$ hours.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

The results of this experiment appear in Figure 7.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). We compare against the best value reported by Bravo Ferreira et al. in \[26, Tables 4 and 6\] for their CSDP method with clique size $k \in {\{ 2,3,4\}}$.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

We also include the results that lists for the PATH method.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Solving QAPs", "weight": 1.0} -->

SketchyCGAL allows us to solve a tighter SDP relaxation of QAP than the other methods (CSDP, PATH). As a consequence, we obtain significantly smaller gaps for most instances.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Standard methodologies", "weight": 1.0} -->

First, we outline the approaches that drive most of the reliable, general-purpose SDP software packages that are currently available.

<!-- chunk {"id": "body-0291", "role": "body", "section": "Standard methodologies", "weight": 1.0} -->

Interior-point methods (IPMs) reformulate the SDP as an unconstrained problem and take an (approximate) Newton step at each iteration. In exchange, they deliver quadratic convergence. Hence IPMs are widely used to solve SDPs to high precision. Software packages include SeDuMi, MoSeK, and SDPT3. Alas, IPMs do not scale to large problems: to solve the Newton system we must store and factor large, dense matrices. A typical IPM for the SDP Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Standard methodologies", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") requires $\Theta{({n^{3} + {d^{2}n^{2}} + d^{3}})}$ arithmetic operations per iteration and $\Theta{({n^{2} + {dn} + d^{2}})}$ memory.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Standard methodologies", "weight": 1.0} -->

Several effective SDP solvers are based on the augmented Lagrangian (AL) paradigm. In particular, Zhao et al. employ a semi-smooth Newton method and the conjugate gradient method to solve the subproblems. Their method is enhanced and implemented in the software package SDPNAL+. AL methods for SDPs typically require storage $\Omega{(n^{2})}$.

<!-- chunk {"id": "body-0294", "role": "body", "section": "First-order methods", "weight": 1.0} -->

First-order methods use only gradient information to solve the SDP to reduce runtime and storage requirements. We focus on *projection-free* algorithms, suitable large SDPs, that do not require full SVD computations. Major first-order methods for SDP include approaches based on the conditional gradient method (CGM) and extensions that handle more complex constraints, primal--dual subgradient algorithms, and the matrix multiplicative weight (MMW) method, or equivalently, the mirror-prox algorithm with the quantum entropy mirror map.

<!-- chunk {"id": "body-0295", "role": "body", "section": "First-order methods", "weight": 1.0} -->

The standard CGM algorithm does not apply to the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") because of the affine constraint ${\mathcal{A}{\mathbf{X}}} = {\mathbf{b}}$. Several variants of CGM can handle affine constraints.

<!-- chunk {"id": "body-0296", "role": "body", "section": "First-order methods", "weight": 1.0} -->

In particular, CGAL does so by applying CGM to an AL formulation. We have chosen to extend CGAL because of its strong empirical performance and its robustness to inexact eigenvector computations; see \[112, Sec. 4-5\].

<!-- chunk {"id": "body-0297", "role": "body", "section": "First-order methods", "weight": 1.0} -->

Primal--dual subgradient methods perform subgradient ascent on the dual problem; the cost of each iteration is dominated by an eigenvector computation. Nesterov constructs primal iterates by proximal mapping. The algorithm in Yurtsever et al. constructs primal iterates by an averaging technique, similar to the updates in CGM; this method involves a line search, so it requires very accurate eigenvector calculations.

<!-- chunk {"id": "body-0298", "role": "body", "section": "First-order methods", "weight": 1.0} -->

The MMW method is derived by reducing the SDP to a sequence of feasibility problems. These are reformulated as a primal--dual game whose dual is an eigenvalue optimization problem. The resulting MMW algorithm can be interpreted as performing gradient descent in a dual space and using the matrix exponential map to transfer information back to the primal space. To scale this approach to larger problems, researchers have proposed linearization, random projection, sparsification techniques, and stochastic Lanczos quadrature to approximate the matrix exponential. Even so, the reduction to a sequence of feasibility problems makes this technique impractical for general SDPs. We are aware of only one computational evaluation of the MMW idea.

<!-- chunk {"id": "body-0299", "role": "body", "section": "Storage considerations", "weight": 1.0} -->

Almost all provably correct SDP algorithms store and operate on a full-dimensional matrix variable, so they are not suitable for very large SDPs.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Storage considerations", "weight": 1.0} -->

Some primal--dual subgradient methods and CGM variants build an approximate solution as a convex combination of rank-one updates, so the rank of the solution does not exceed the number of iterations. This fact has led researchers to call these methods "storage-efficient," but this claim is misleading because the algorithms require many iterations to converge.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Storage considerations", "weight": 1.0} -->

In the conference paper, written by a subset of the authors, we observed that certain types of optimization algorithms can be combined with sketching to control storage costs. As a first example, we augmented CGM with sketching to obtain a new algorithm called SketchyCGM. This method solves a special class of low-rank matrix optimization problems that arise in statistics and machine learning. We believe that SketchyCGM is the first algorithm for this class of problems that provably succeeds with optimal storage.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Storage considerations", "weight": 1.0} -->

To develop SketchyCGAL, we changed the base optimization algorithm (to CGAL) so that we can solve standard-form SDPs. We switched to a simpler sketching technique (the Nyström sketch) that has better empirical performance. We also analyzed how accurately to solve the eigenvalue problems to ensure that SketchyCGAL succeeds (Appendix A under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Storage considerations", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.")), and we deployed an approximate eigenvalue computation method (randomized Lanczos) that meets our needs. Altogether, this effort leads to a storage-optimal algorithm that works for all standard-form SDPs with a minimum of tuning. Reducing the storage has the ancillary benefit of reducing arithmetic and communication costs, which also improves scalability.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Storage considerations", "weight": 1.0} -->

In concurrent work with Ding, a subset of the authors developed a new *approximate complementarity principle* that also yields a storage-optimal algorithm for standard-form SDPs. This approach uses a suboptimal dual point to approximate the range of the primal solution to the SDP. By compressing the primal problem to this subspace, we can solve the primal SDP with limited storage. This method, however, has more limited guarantees than SketchyCGAL. A numerical evaluation is in progress.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

The most famous approach to low-storage semidefinite programming is the factorization heuristic proposed by Homer and Peinado and refined by Burer and Monteiro (BM). The main idea is to reformulate the model problem Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") by expressing the psd matrix variable ${\mathbf{X}} = {{\mathbf{F}}{\mathbf{F}}^{\ast}}$ in terms of a factor ${\mathbf{F}} \in {\mathbb{R}}^{n \times R}$, where the rank parameter $R \ll n$. That is, This approach controls storage by sacrificing convexity and the associated guarantees.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

Many nonlinear programming methods have been applied to optimize Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). AL methods are commonly used. The most popular research software based on BM factorization is Manopt, which implements manifold optimization algorithms including Riemannian gradient and Riemannian trust region methods.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

Consequently, Manopt is limited to problems where the factorized formulation Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") defines a smooth manifold.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

There has been an intense effort to establish theoretical results for the BM factorization approach. It is clear that every solution to the SDP Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0310", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") of rank $R$ or less is also a solution to the factorized problem Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.").

<!-- chunk {"id": "body-0311", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

On the other hand, Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0312", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") may admit local minima that are not global minima of Eq. 2.2 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088."). Some guarantees are available.

<!-- chunk {"id": "body-0313", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

For example, if $\mathbf{C}$ is generic and the constraint set of Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0314", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is a smooth manifold and $R \geq \sqrt{2{({d + 1})}}$, then each second-order critical point of Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

<!-- chunk {"id": "body-0315", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") is a global optimum. A second-order critical point can be located using a Riemannian trust region method. See for additional theoretical analysis.

<!-- chunk {"id": "body-0316", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

The storage and arithmetic costs of solving Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") depend on the factorization rank $R$. Unfortunately, the BM method may fail when $R = {o{(\sqrt{d})}}$.

<!-- chunk {"id": "body-0317", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

Below this threshold, the BM formulation Eq. 8.1 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") can have spurious solutions (second-order critical points that are not globally optimal), and the bad problem instances can form a set of positive measure.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Nonconvex Burer--Monteiro methods", "weight": 1.0} -->

Hence the Burer--Monteiro approach cannot support provably correct algorithms with storage costs better than $\Omega{({n\sqrt{d}})}$. See Section E.4 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA. AY acknowledges the Early Postdoc.Mobility Fellowship P2ELP2_187955 from the Swiss National Science Foundation and partial postdoctoral support from the NSF-CAREER grant IIS-1846088.") for numerical evidence.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented a practical, new approach for solving SDPs at scale. Our algorithm, SketchyCGAL, combines a primal--dual optimization method with randomized linear algebra techniques to achieve unprecedented guarantees when the problem is weakly constrained and the solution is approximately low rank. We hope that our ideas lead to further algorithmic advances and support new applications of semidefinite programming.

<!-- chunk {"id": "body-0320", "role": "body", "section": "Conclusion", "weight": 1.5} -->

SketchyCGAL is currently limited by the arithmetic cost of solving large eigenvalue problems to increasing accuracy. It also falters for SDPs with a large number of constraints because it depends on a primal--dual approach. Moreover, our analysis does not fully explain the observed behavior of the algorithm, including the rate of convergence of the primal variable or the convergence of the dual variable and the surrogate duality gap. These topics merit further research.
