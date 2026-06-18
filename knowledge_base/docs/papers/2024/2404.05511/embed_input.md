<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A High-Performant Multi-Parametric Quadratic Programming Solver

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a combinatorial method for computing explicit solutions to multi-parametric quadratic programs, which can be used to compute explicit control laws for linear model predictive control. In contrast to classical methods, which are based on geometrical adjacency, the proposed method is based on combinatorial adjacency. After introducing the notion of combinatorial adjacency, we show that the explicit solution forms a connected graph in terms of it. We then leverage this connectedness to propose an algorithm that computes the explicit solution. The purely combinatorial nature of the algorithm leads to computational advantages since it enables demanding geometrical operations (such as computing facets of polytopes) to be avoided. Compared with classical combinatorial methods, the proposed method requires fewer combinations to be considered by exploiting combinatorial connectedness. We show that an implementation of the proposed method can yield a speedup of about two orders of magnitude compared with state-of-the-art software packages such as MPT and POP.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Model Predictive Control (MPC), a control action is determined at each time step by solving an optimization problem. When the dynamics of the system to be controlled is linear, the optimization problems in question can be cast as instances of a multi-parametric quadratic program (mpQP) of the form

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the decision variable $x \in {\mathbb{R}}^{n}$ is related to the control action, and the parameter $\theta \in \Theta_{0} \subseteq {\mathbb{R}}^{p}$ is related to setpoints and the system state. The parameter set $\Theta_{0}$ is assumed to be a polyhedron. For a given linear (and time-invariant) MPC application, the Hessian $H \succ 0$ and the constraint matrix $A \in {\mathbb{R}}^{m \times n}$ are constant. Moreover, both the linear cost $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{n}}$ and the constraint offset $b:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{m}}$ are affine functions of $\theta$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The particular structure of (LABEL:eq:rmpc-mpqp) allows for a closed-form solution $x^{\ast}{(\theta)}$ that is piecewise affine over polyhedral regions. This closed-form, or explicit, solution is used in explicit MPC, where the control law is implemented as a simple lookup table.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Albeit straightforward to theoretically derive the explicit solution, it is not as straightforward to compute the corresponding polyhedral regions efficiently and reliably. As a result, several methods for computing the explicit solution have been developed, which generally fall into two categories: geometrical and combinatorial; an alternative approach for mpQPs that specifically originate from MPC, which is based on dynamic programming, has been proposed. State-of-the-art software packages that can compute the explicit solution to (LABEL:eq:rmpc-mpqp) include MPT, POP, and the Hybrid Toolbox.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this paper is a combinatorial method that efficiently computes the explicit solution of (LABEL:eq:rmpc-mpqp). The method is based on exploring a connected graph, similar to and, to tame the combinatorial nature of computing the explicit solution. In contrast to, the method does not rely on any geometrical operations such as computing the facets of polytopes, which makes the resulting method more efficient and reliable. In contrast to, the proposed method handles degeneracies in a more straightforward manner; the proposed method does not, for example, need to explicitly check if constraints are weakly active/inactive. The method is also related to the complexity-certification method, which produces the explicit solution as a byproduct.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Proving that the explicit solution to an mpQP form a connected graph in a combinatorial sense (Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver")).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A combinatorial mpQP method that builds on exploring combinatorial adjacent active sets (Algorithm 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

An efficient implementation of the proposed method that is often several orders of magnitude faster than state-of-the-art software (Section IV).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows: In Section II we describe how a multi-parametric least-distance problem (mpLDP) can be consider instead of the mpQP in (LABEL:eq:rmpc-mpqp). We then derive the explicit solution to this mpLDP and formalize a combinatorial problem for computing it. The section ends with a brief review of existing methods for computing the explicit solution. In Section III we introduce the concept of geometrical and combinatorial adjacency of active sets, and show that any pair of optimal active sets are connected by a sequence combinatorially adjacent acitve sets. We then leverage this connectedness to propose an algorithm that efficiently computes the explicit solution. In Section IV we show that an implementation of the proposed algorithm is about two orders of magnitude faster than the state-of-the-art mpQP solvers implemented in MPT and POP.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Equivalent least-distance problem", "weight": 1.0} -->

To simplify notation and reduce computations in the proposed algorithm, we first transform the mpQP in (LABEL:eq:rmpc-mpqp) into the equivalent multi-parametric least-distance problem (mpLDP) of the form

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Equivalent least-distance problem", "weight": 1.0} -->

by using the transformation $u = {R{({x + {R^{- T}f{(\theta)}}})}}$, where $R$ is an upper Cholesky factor of $H$; the problem data in is, accordingly, defined as

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Equivalent least-distance problem", "weight": 1.0} -->

The solution $x^{\ast}{(\theta)}$ to (LABEL:eq:rmpc-mpqp) can be retrieved from the solution $u^{\ast}{(\theta)}$ to as

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Equivalent least-distance problem", "weight": 1.0} -->

Importantly, we have that the affine structure of the constraint offset is retained, which we formalize in the following lemma.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1 (Relating mpLDP and mpQP)", "weight": 1.0} -->

Since $d{(\theta)}$ is affine, the LDP in is a special case of an mpQP of the form (LABEL:eq:rmpc-mpqp). Hence, all results for mpQPs directly translate to; for example, that the solution is piecewise affine over a polyhedral partition. This is also evident from the simple affine relationship between $x^{\ast}$ and $u^{\ast}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B The explicit solution", "weight": 1.0} -->

Necessary and sufficient conditions for a solution $u^{\ast}$ to the mpLDP in are the KKT-conditions

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B The explicit solution", "weight": 1.0} -->

with the dual variable $\lambda \in {\mathbb{R}}^{m}$. Both $u^{\ast}{(\theta)}$ and $\lambda{(\theta)}$ are functions of the parameter $\theta$, although we will often skip writing out this parameter dependence explicitly and use the notation $u^{\ast}$ and $\lambda$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B The explicit solution", "weight": 1.0} -->

The main complication with using the KKT-conditions in to find a solution is the complementary slackness condition in (5d), which make solving a combinatorial problem. To make the combinatorial aspect of solving more explicit, we introduce the notion of an active set.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2 (Explicit solution to mpQP)", "weight": 1.0} -->

Note that in combination with directly gives $x^{\ast}{(\theta)}$, and that the critical regions $\Theta_{\mathcal{A}}$ are the same.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2 (Explicit solution to mpQP)", "weight": 1.0} -->

The main challenge for determining the explicit solution in is to find the active sets that define the critical regions. Formally, this corresponds to finding the set ${\mathbb{A}} \triangleq {\{\mathcal{A}:{\Theta_{\mathcal{A}} \neq \varnothing}\}}$. From a practical point of view, however, expressing the explicit solution only requires active sets that define critical regions that cover the parameter space. Therefore, active sets that break the LICQ can be discarded (see, for example, Lemma 1, which ensures that active sets that break LICQ can be discarded, even if they define full-dimensional critical regions). In summary, finding the explicit solution can be formalized as

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Existing methods to compute the explicit solution", "weight": 1.0} -->

Traditionally, Problem 1 has been tackled with geometrical methods. These methods start in a critical region and explore all neighboring regions by moving in the parameter space ${\mathbb{R}}^{p}$. The most efficient geometrical methods exploit the "facet-to-facet" property, which allow neighboring regions to be accessed from the facets of the current critical region. A major challenge for geometrical methods is that this "facet-to-facet" property does not always hold. Another challenge is that they employ geometrical operations such as computing points on lower-dimensional facets, which is a numerically unreliable operation. Therefore, geometrical methods themselves are often unreliable, especially when the dimension of the parameter space increases.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Existing methods to compute the explicit solution", "weight": 1.0} -->

In contrast, combinatorial methods do not explore the parameter space, but instead search directly for active sets that leads to non-empty critical regions. A naive combinatorial method would be to solve feasibility problems to see if $\Theta_{\mathcal{A}} \neq \varnothing$ for all possible $2^{m}$ active sets. Since this would require an exponential number of feasibility problems to be solved, this quickly becomes intractable as the number of constraint $m$ increases. Instead of such a brute-force search, combinatorial methods use properties of the problem to dismiss $\mathcal{A}$ that cannot possibly be optimal based on previously tested active sets (known as fathoming). The first work in this directions was, which used fathoming based on primal feasibility and LICQ violation to prune candidate active sets. Following this work, several works (e.g. ) have introduced additional fathoming strategies, which ultimately requires fewer feasibility problems to be solved.

<!-- chunk {"id": "body-0024", "role": "body", "section": "A combinatorial connected-graph algorithm", "weight": 1.0} -->

In this section, we propose a combinatorial method that solves Problem 1; that is, a combinatorial method that computes the explicit solution to the mpLDP. First, we introduce the concepts of active sets being geometrically and combinatorially adjacent. We then use these concepts to construct a simple algorithm that produces a solution ${\mathbb{A}}^{\ast}$ to Problem 1. Finally, we discuss the method's relationship with the connected-graph methods. The foundation for the proposed method is the concept of combinatorially adjacent active sets, introduced next, which complement the classical concept of geometrical adjacency of critical regions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Geometrical and combinatorial adjacency", "weight": 1.0} -->

As mentioned in Section II-C, both geometrical methods and the connected-graph method in are based on the fact that critical regions are adjacent with other critical regions in the parameter space. Two critical regions are adjacent if they intersect, and we say that the corresponding active sets are geometrically adjacent.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3 (adjacency vs connectedness)", "weight": 1.0} -->

Note that two active sets being geometrically adjacent does not generally imply that they are combinatorially adjacent, but it does imply that they are combinatorially connected. An illustrative example of this distinction is given in Example 1. Geometrical adjacency does, however, imply combinatorial adjacency when no degeneracies occur, which follows directly from Theorem 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3 (adjacency vs connectedness)", "weight": 1.0} -->

Now we are ready to present the main theoretical results of this paper: namely, that any two active set that are optimal and satisfy LICQ are combinatorially connected. This theorem is the foundation of the correctness of the proposed method.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 4 (Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver\") and )", "weight": 1.0} -->

A similar result to Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver") is presented, but their result is, as is pointed out, based on an incorrect premise that weakly active constraints cannot occur. Moreover, the result therein is more loosely proved in terms of "dual simplex steps", which is not as direct as the concept of combinatorial adjacency introduced in Definition 5 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver") that Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver") is based.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 5 (Lower-dimensional regions)", "weight": 1.0} -->

Importantly, note that the critical region $\Theta_{\mathcal{A}}$ for any $\mathcal{A} \in {\mathbb{A}}$ might be lower-dimensional. This is central for connectedness in degenerate cases. As is highlighted, e.g., Example 1, restricting the exploration to full-dimensional critical regions does not lead to the desired connectedness in Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver").

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B A combinatorial algorithm", "weight": 1.0} -->

We are now interested in using the insights from Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver") to construct an algorithm that solves Problem 1. That is, we are interested in constructing an algorithm that produces a collection of active sets ${\mathbb{A}}^{\ast}$ that coincides with ${\mathbb{A}}^{\text{LICQ}}$. We will do this by recursively generating combinatorially adjacent active sets for all active sets that define critical regions that are non-empty.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B A combinatorial algorithm", "weight": 1.0} -->

The proposed algorithm, given in Algorithm 1, considers an unexplored active set $\mathcal{A}$ in each iteration. If LICQ holds for $\mathcal{A}$, the corresponding region of the form is formed and a feasibility problem is solved to check whether $\Theta_{\mathcal{A}} \neq \varnothing$. If $\Theta_{\mathcal{A}}$ is non-empty, we add $\mathcal{A}$ to the set of discovered optimal active sets ${\mathbb{A}}^{\ast}$, and put all its unexplored combinatorially adjacent active sets on the stack $S$ for further exploration. All combinatorially adjacent active sets to $\mathcal{A}$ are formed with the functions ExploreSupersets, which creates candidate active sets by adding an index to $\mathcal{A}$, and with the function ExploreSubsets, which creates candidate active sets by removing an index from $\mathcal{A}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B A combinatorial algorithm", "weight": 1.0} -->

By forming all unexplored active sets that are combinatorially adjacent to $\mathcal{A}$, we will ensure (based on Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver")) that all active sets in ${\mathbb{A}}^{\text{LICQ}}$ are explored. If LICQ does not hold for $\mathcal{A}$, we only form combinatorially adjacent active sets by removing a constraints, since LICQ is guaranteed to be broken for combinatorially adjacent active sets that have more elements. This is sufficient, since, for a valid combinatorial sequence, LICQ does not break consecutively (cf. point (ii) in Definition 6 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver").)

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B A combinatorial algorithm", "weight": 1.0} -->

1:Θ0 ⊆ ℝp, 𝒜0 ∈ 𝔸LICQ, an mpLDP of the form
2:Collection of optimal active sets 𝔸* over Θ
6: if LICQ satisfied for 𝒜 then
8: Compute $\mu_{\overline{\mathcal{A}}}{(\theta)}$ according to and
14: else ExploreSubsets(𝒜, ℰ, S) ⊳ (𝒜 violates LICQ)
16: for $i \in \overline{\mathcal{A}}$ do
18: if 𝒜+ ∉ ℰ then add 𝒜+ to ℰ and S
22: if 𝒜− ∉ ℰ then add 𝒜− to ℰ and S
Algorithm 1 Combinatorial method for solving Problem 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B A combinatorial algorithm", "weight": 1.0} -->

Since Algorithm 1 produces all combinatorially adjacent active sets for any $\mathcal{A} \in {\mathbb{A}}^{\text{LICQ}}$, Definition 7 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver") and Theorem 1 directly guarantees correctness, in the sense that Algorithm 1 solves Problem 1, formalized in the following corollary.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 6 (Finding $\\mathcal{A}_{0}$)", "weight": 1.0} -->

To find an active set $\mathcal{A}_{0} \in {\mathbb{A}}^{\text{LICQ}}$ to initialize Algorithm 1, one can use a QP solver, such as DAQP, and solve (LABEL:eq:rmpc-mpqp) for a given parameter $\theta \in \Theta_{0}$. Another possibility is to initially perform a combinatorial exploration akin to the method.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Comparison with similar methods", "weight": 1.0} -->

As previously mentioned, the proposed method given in Algorithm 1 is related to the methods in and. To highlight the contributions of this paper, we will now delineate some important differences between and Algorithm 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Comparison with similar methods", "weight": 1.0} -->

The connected-graph approach presented in use Theorem 2 in to characterize the facets of a critical regions and use this to generate new active set candidates. As previously mentioned, geometrical operations that involve facets are often numerically unstable. Moreover, to obtain the facets, redundant half-planes need to be removed from the critical regions, which lead to the main computational burden (as is emphasized in and reported in Figure 6 of ). In contrast, Algorithm 1 does not need to characterize the facets of each critical region, making it more numerically robust and efficient (supported by the results in Section IV.) Moreover, the proof of the correctness of the method in is based on false premises in degenerate cases, see Remark 4 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver"), while Algorithm 1 is based on Theorem 1 ‣ III-A Geometrical and combinatorial adjacency ‣ III A combinatorial connected-graph algorithm ‣ A High-Performant Multi-Parametric Quadratic Programming Solver") that still holds for degenerate problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Comparison with similar methods", "weight": 1.0} -->

In, degeneracies are handled by detecting constraints that are weakly active/inactive. This requires feasibility problems of the form

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Comparison with similar methods", "weight": 1.0} -->

to be solved, where $t = 0$ signifies a degenerate case with weakly active/inactive constraints. Instead of identifying weakly inactive/active constraints as, the proposed method exploit that there always exist a sequence of active sets corresponding to critical regions (possibly lower-dimensional) that are non-empty that connect any two full-dimensional critical regions. The existence of such lower-dimensional critical regions is hinted at in Example 1, but is never proved nor exploited therein.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Comparison with similar methods", "weight": 1.0} -->

Since Algorithm 1 does not have to detect weakly active/inactive constraints, only simple LDPs of the form

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Comparison with similar methods", "weight": 1.0} -->

need to solved in the proposed algorithm. As a result, the dual active-set solver DAQP can be used to efficiently check feasibility for $\Theta_{\mathcal{A}}$. As is illustrated in the results in Section IV, this leads to a significant speedup.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 7 (Dimension of feasibility problems)", "weight": 1.0} -->

The feasibility problems that need to be solved in of the form are carried out over $1 + p + {2m}$ dimensions ($t,\theta,\lambda,\mu$). In contrast, the feasibility problems that need to be solved in Algorithm 1 of the form are carried out over $p$ dimensions ($\theta$).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 7 (Dimension of feasibility problems)", "weight": 1.0} -->

Another advantage of the straightforward degeneracy handling in Algorithm 1 is that the algorithm itself is a lot simpler than the proposed algorithm. This makes it easier to implement efficiently.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To illustrate the efficacy of Algorithm 1, we compare a Julia implementation of it^11^1 with the state-of-the-art mpQP solvers in MPT and POP. For MPT, we use its implementation of the geometrical method presented. For POP, we use its implementation of the connected-graph method. Experiments^22^2 were carried out on the test set provided, which consists of 100 mpQPs, for which the solvers were tasked to compute the explicit solution; for more information about the test set, see. To limit the total execution time for the entire problem set, we terminate a solver after 100 seconds if it has been unable to return a solution up until then.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The results are reported in Figure 1, where the implementation of Algorithm 1 displays a speedup of about two orders of magnitude compared with both MPT and POP. For a fair comparison, we tried several internal LP solvers in both MPT and POP. For MPT, the open-source solver GLPK gave the best performance. For POP, the proprietary solver CPLEX gave the best performance. As presented in Section III-C, the proposed method use the open-source solver DAQP for solving feasibility problems of the form. Note that the execution times for the proposed method includes forming and storing the explicit solution for each active set in ${\mathbb{A}}^{\ast}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have proposed a combinatorial method for computing explicit solutions to multi-parametric quadratic programs. The method builds on optimal active sets being "combinatorially connected", which makes the explicit solution form a combinatorially connected graph. We show that an implementation of the proposed method can yield a speedup of two orders of magnitude compared to state-of-the-art software packages such as MPT and POP.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work include presenting details of how to implement Algorithm 1 efficiently, and to develop a parallelized version of it.
