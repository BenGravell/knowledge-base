<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Presolving for GPU-Accelerated First-Order LP Solvers

Topics include Linear programming, Optimization, PSLP, LP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent research has focused on developing GPU-accelerated first-order solvers for linear programming (LP). This line of work, however, has largely overlooked the role of presolving, and thus prior results do not fully reflect the speedups achievable through GPU acceleration in a realistic end-to-end solver pipeline. At the same time, LP presolving has traditionally been developed for CPU-based solvers, where presolve time rarely dominates the total runtime and the emphasis has been on maximizing the reduction in problem size, even at the expense of costly presolve rules. Given the high performance of modern GPU-accelerated solvers and the inherently sequential nature of presolving, it is unclear whether this traditional approach to presolving remains appropriate. In this paper we revisit LP presolving from the perspective of GPU-accelerated first-order LP solvers. We identify a set of relatively simple presolve rules and show that a carefully engineered collection of these captures most of the reduction achieved by Gurobi's commercial state-of-the-art presolver, at a fraction of the cost.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Moreover, we demonstrate that such lightweight presolving can yield substantial end-to-end speedups for the GPU-accelerated solver cuPDLPx, despite presolving sometimes constituting a significant fraction of the total runtime. These results suggest that lightweight presolving may remain beneficial as GPU performance continues to scale, while the sequential nature of presolving presumably does not. We accompany this paper with an open-source C implementation of an LP presolver, called PSLP (Presolver for Linear Programs). PSLP is battle-tested and has been adopted by the community, with integrations in cuPDLPx, cuOpt (NVIDIA's optimization library), and HPR-LP.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear programming (LP) is arguably the most widely used problem class in mathematical optimization, with applications spanning a broad range of fields. Decades of research and substantial engineering effort have produced highly optimized implementations of the simplex method and its many variants, as well as interior-point methods. As a result, LP solving has become a mature and remarkably efficient technology --- capable of handling instances of a scale and complexity that George Dantzig himself could hardly have imagined, often in a matter of seconds.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Commercial LP solvers consist of three major components: a *presolver* that reduces the size of the problem and later reconstructs a solution to the original problem; a *core step* that runs one or multiple algorithms concurrently to solve the reduced problem; and a *crossover mechanism* (used only for non-simplex algorithms) that takes the approximate solution produced by the core step and converts it into a highly accurate basic feasible solution. While the first and third components are highly sequential in nature (and can take a significant portion of the total solve time), the core step traditionally implements an interior-point method that benefits from CPU multithreading for the computational bottleneck of factorizing and solving large sparse linear systems. However, despite being compute-bound, this bottleneck appears to have an inherent limit to the amount of parallelism that can be effectively exploited (see, for example, ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To fully exploit the computational power of modern hardware accelerators in the context of linear programming, recent research has focused on speeding up the core step by developing first-order methods that rely heavily on matrix-vector multiplications \[ADH+21, ADH+25, CSY+25, LYH+23, \]. While this paradigm shift opens up exciting opportunities for solving extremely large LPs, it also raises important questions about the role of the other traditional components of LP solvers. In this paper we focus on presolving, a critical but often overlooked component, and its impact on GPU-accelerated first-order solvers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Presolving is traditionally performed on CPUs because it involves a large number of sequential, logic-driven, and structurally irregular problem transformations. The application of one problem transformation often enables or invalidates others, creating a chain of data-dependent transformations that are inherently sequential. Many of these transformations require heavy branching, dynamic sparse-matrix modifications, and unpredictable memory access patterns. It is therefore currently believed that CPUs, with their low-latency caches and sophisticated control-flow capabilities, are far better suited for the task than GPUs. Although certain parts of a presolver admit some degree of parallelism, the engineering effort required to map these onto GPU architectures is rarely justified, and we speculate that the potential speedup would at best be modest, in particular if CPU multithreading is used for the parallelizable parts. However, GPU acceleration has a different consequence for presolving: the relative cost of presolving compared to the GPU-accelerated core step has increased significantly, putting very high demands on the implementation and speed of the presolver.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For every extra second spent in presolving, there are thousands of idle GPU cores waiting to get to work, so it is unclear whether LP presolving is still worthwhile in this new context.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The idea of reducing the size of an LP before passing it to a solver has a long history, dating back at least to the 1970s. (We review related work in §1.1.) Over the past decades, a wide range of presolve techniques have been proposed, from simple ones such as eliminating constraints with just one variable to more elaborate procedures such as exploiting symmetry between variables \[ABG+19\]. This body of work has largely been developed for CPU-based solvers, where presolving and the core algorithm run on the same hardware, and where presolve time rarely dominates the overall runtime. In this traditional setting, the emphasis has been on maximizing the reduction in problem size, even at the cost of more costly presolve techniques.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we revisit LP presolving from a different perspective, motivated by GPU-accelerated first-order methods. In this setting, presolving is inherently sequential, runs on different hardware than the core algorithm, and can easily become a bottleneck. This raises a fundamental question: can meaningful performance gains be obtained using only a carefully engineered collection of simple and fast presolve techniques, and how much problem reduction is sacrificed by forgoing the more complex and costly rules found in traditional presolvers? By focusing on rules that are fast and lightweight, we aim to identify those that have the potential to remain effective as GPU performance continues to scale, while the sequential nature of presolving presumably does not.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments show, perhaps surprisingly, that a carefully engineered collection of relatively simple presolve techniques can achieve reductions in problem size comparable to those obtained by the commercial state-of-the-art presolver implemented in Gurobi \[ABG+19\]. Specifically, we find that our open-source C implementation of an LP presolver, called PSLP (Presolver for Linear Programs), on average captures about 90% of the reduction achieved by Gurobi's presolver, while being over 6 and 11 times faster, respectively, on two standard LP datasets. We also investigate the impact of PSLP on the total solve time of cuPDLPx, a GPU-accelerated first-order LP solver based on the primal-dual hybrid gradient (PDHG) method. Our main observation is that PSLP has a strong positive impact on the total solve time of cuPDLPx across a wide range of LP instances.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, on the large problems with more than $10^{7}$ nonzero entries from Mittelmann's LP collection and the MIPLIB 2017 root-node LP relaxations \[GHG+21\], enabling PSLP reduces the shifted geometric mean of the total solve time by more than a factor of 2.5 and 9, respectively. Since PSLP was released, it has been integrated into several solvers by their developers, including cuPDLPx, cuOpt (NVIDIA's GPU-accelerated optimization library ), and HPR-LP \[CSY+25\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper begins with an overview of related work on presolving. Next, we review the main ideas behind LP presolving in §2. Our presentation emphasizes the abstractions of *reductions*, *primal exploration*, and *dual exploration*, which we believe are useful for understanding and implementing presolvers, although the classic literature never presents presolving in this way. In §3, we discuss some of the design choices behind our open-source implementation of a fast and lightweight LP presolver. In §4, we assess how much of the total reduction achieved by the commercial presolver implemented in Gurobi can be captured by the carefully engineered collection of relatively simple presolve techniques implemented in PSLP. We also evaluate the impact of presolving on the total solve time of cuPDLPx. Finally, we discuss our findings in §5.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Reductions", "weight": 1.0} -->

The idea of a presolver is to apply a sequence of *reductions* to the original problem to obtain a smaller, equivalent problem that can be solved more efficiently. The notion of reductions is standard in both the theory and practice of computer science, where it underlies, for example, program rewriting systems in compilers \[ALS+06\] and transformation-based modeling frameworks for optimization such as CVXPY \[AVD+18\].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Reductions", "weight": 1.0} -->

In the context of LP presolving, each reduction consists of a *presolve transformation* and a *postsolve transformation*. The presolve transformation takes as input one problem and outputs an equivalent problem that is, in some sense, smaller or simpler than the input problem. The postsolve transformation takes as input a solution to the reduced problem and maps it to a solution of the original problem. Each reduction is very simple and cheap to apply, and for large LPs several hundreds of thousands of reductions may be applied in sequence.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Reductions", "weight": 1.0} -->

A first example of a reduction is *fixing a variable*. Suppose we for some reason fix a variable $x_{k}$ to some value ${\hat{x}}_{k}$ (we discuss how to identify such variable fixings below), and assume that this is the only reduction we apply. The *presolve* transformation for this reduction consists of removing the variable $x_{k}$ from the original problem by substituting its fixed value into the remaining parts of the problem. The variable $x_{k}$ appears in the original problem but not in the reduced problem, so the *postsolve* transformation must recover an optimal primal variable ${(x_{k}^{\star})}_{\text{original}}$ and an optimal dual variable ${(z_{k}^{\star})}_{\text{original}}$ of the original problem from a solution of the reduced problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reductions", "weight": 1.0} -->

(This choice of ${(z_{k}^{\star})}_{\text{original}}$ follows from the dual feasibility condition, i.e., the second line of.)

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reductions", "weight": 1.0} -->

adding a multiple of an equality constraint to another constraint,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reductions", "weight": 1.0} -->

substituting a variable appearing in only one equality constraint, and

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reductions", "weight": 1.0} -->

While classic papers on presolving, such as \[ ABG+19\], list several more complicated problem transformations as reductions, we use a different abstraction where we break down complex transformations into sequences of simple reductions. In our abstraction, a reduction is the *simplest* atomic rewriting unit of a problem. Most problem transformations described in the literature on LP presolve can be broken down into sequences of the 5 reductions mentioned above. This abstraction does not only make it easier to describe a presolver, but it also simplifies the implementation of one of the most complicated parts of the presolver: recovering optimal dual variables of the original problem from an optimal primal-dual solution of the reduced problem.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reductions", "weight": 1.0} -->

To find valid reductions (i.e., problem transformations that reduce the size of the problem while provably maintaining an equivalence to the original problem), we use *primal exploration* and *dual exploration*, as described next.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Primal exploration", "weight": 1.0} -->

Primal exploration analyzes the *primal* constraints to identify opportunities for reductions. The logical rules applied during this process guarantees that the feasible set of the reduced problem is equivalent to that of the original formulation. Roughly speaking, primal exploration identifies reductions that preserve the feasible set while producing a more compact representation with less redundancy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Primal exploration", "weight": 1.0} -->

A simple example of primal exploration is the *redundant constraint explorer*, which uses variable bounds to identify redundant constraints. For example, consider the bounds $x_{1} \geq 1$ and $x_{2} \geq 2$ together with the constraint ${x_{1} + {2x_{2}}} \geq 5$. Since the variable bounds imply that the constraint is satisfied, the constraint is classified as redundant. Once such a constraint is identified, the redundant constraint explorer invokes the corresponding reduction to remove it from the problem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Primal exploration", "weight": 1.0} -->

Another example is the *doubleton row explorer*, which finds equality constraints with only two variables and substitutes one variable in terms of the other. For example, consider the constraint ${x_{1} + x_{2}} = 1$ together with the bounds ${x_{1},x_{2}} \geq 0$. First, we transfer the bound $x_{1} \geq 0$ to an upper bound on $x_{2}$, giving $x_{2} \leq 1$ and making $x_{1}$ unbounded. (This is done by invoking the reduction that changes variable bounds.) Second, we substitute $x_{1} = {1 - x_{2}}$ in the remaining parts of the problem. (This is done by first repeatedly invoking the reduction that adds a multiple of an equality constraint to another constraint, followed by the reduction that substitutes a variable appearing in only one equality constraint.) Third, we remove the constraint ${x_{1} + x_{2}} = 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Primal exploration", "weight": 1.0} -->

(This is done by invoking the reduction that deletes a constraint.) Once the doubleton row explorer identifies an equality constraint with only two variables, it invokes these reductions in sequence. The reduced problem has one less variable and one less constraint, and the reduced feasible set is equivalent to the feasible set of the original problem in the sense that if $x_{2} = a$ for some $a \in \text{R}$ is feasible for the reduced problem, then ${(x_{1},x_{2})} = {({1 - a},a)}$ is feasible in the original problem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Primal exploration", "weight": 1.0} -->

We list more examples of primal exploration in §3.1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dual exploration", "weight": 1.0} -->

Dual exploration analyzes the *dual* constraints to identify opportunities for reductions based on complementary slackness and dual variable bounds. Unlike primal exploration, dual exploration may identify reductions that do not preserve the feasible set of the original problem. However, the logical rules applied during dual exploration guarantee that any optimal solution of the reduced problem can still be mapped to an optimal solution of the original problem.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dual exploration", "weight": 1.0} -->

Dual exploration is further categorized into *strong* and *weak* exploration. The semantics behind weak dual exploration imply that any reduction it identifies preserves the entire optimal solution set: *every* optimal solution of the original problem can, in principle, be recovered from some optimal solution of the reduced problem. In contrast, the semantics of strong dual exploration are looser: it may yield more aggressive reductions, but these only guarantee that *at least one* optimal solution of the original problem can be recovered from an optimal solution of the reduced problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dual exploration", "weight": 1.0} -->

A simple example of dual exploration is the *variable lock explorer*. An *uplock* of a variable is a constraint that prevents the variable from increasing to infinity. If a variable $x_{k}$ has objective coefficient $c_{k} < 0$ and no uplock, then the dual constraints imply that $z_{k} < 0$ for any dual feasible point. By complementary slackness, this means that $x_{k}$ will be equal to its upper bound ${\overline{x}}_{k}$ at any optimal solution, so the variable lock explorer can invoke the reduction that fixes $x_{k}$ to ${\overline{x}}_{k}$. (If ${\overline{x}}_{k} = {+ \infty}$, then the problem is unbounded.) This is an example of weak dual exploration, since *any* optimal solution of the original problem must have $x_{k} = {\overline{x}}_{k}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dual exploration", "weight": 1.0} -->

If instead $c_{k} = 0$ and $x_{k}$ has no uplock, the variable lock explorer can still invoke the reduction of fixing $x_{k}$ to ${\overline{x}}_{k}$, but not every primal optimal solution $x^{\star}$ of the original problem is guaranteed to have $x_{k}^{\star} = {\overline{x}}_{k}$, so this is an example of strong dual exploration.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dual exploration", "weight": 1.0} -->

The variable lock explorer is a special case of a more general dual exploration phase that propagates the dual constraints to strengthen dual variable bounds and identify reductions based on complementary slackness (see, e.g., \[, §3.4\]). Other examples of dual exploration include searching for *column singletons in inequality constraints* \[, §1.2\] and *dominated columns* \[GKM+15, §4\]. Interestingly, many dual exploration rules can be interpreted as primal explorers applied to the dual problem. For example, both the variable lock explorer and the dominated columns explorer are just special primal redundant constraint explorers applied to the dual problem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Design and implementation", "weight": 1.0} -->

While the main concepts behind LP presolving are straightforward and simple to describe, implementing them in practice involves numerous design choices. In this section, we discuss some of the most important decisions and describe our implementation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Explorers", "weight": 1.0} -->

The most important design choice is which explorers to implement. Each explorer applies a set of logical rules to identify opportunities for reductions. Adding more explorers typically yields smaller reduced problems, but at the cost of increased presolve time. Table 1 describes and groups commonly used explorers into three categories based on their computational cost.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Explorers", "weight": 1.0} -->

*Fast* explorers require minimal computation to identify reductions, as they operate primarily by scanning *internal statistics* maintained by the presolver (we describe what internal statistics are in greater detail in §3.2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Explorers", "weight": 1.0} -->

*Medium* explorers require additional computation and cannot be executed using internal statistics alone. For example, the explorer that detects parallel rows belongs to this category because it requires a two-level hashing algorithm together with pairwise comparison of rows to identify constraints that are parallel \[ABG+19, §5.2\].

<!-- chunk {"id": "body-0036", "role": "body", "section": "Explorers", "weight": 1.0} -->

*Slow* explorers require substantially more computation. For example, one explorer in this category detects linear dependence among equality constraints and requires rank-revealing matrix factorizations. A related explorer identifies opportunities for reducing the number of nonzero entries in the constraint matrix by adding a multiple of an equality constraint to another constraint to make the latter sparser, similar to Gaussian elimination.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Explorers", "weight": 1.0} -->

The categorization in table 1 is based on our experience with presolving and is therefore somewhat subjective.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Explorers", "weight": 1.0} -->

Almost all of the explorers listed in table 1 were proposed over several decades by researchers with either CPU-based simplex or interior-point solvers in mind, so it is natural to ask whether all of them are worthwhile for GPU-accelerated first-order solvers. For example, first-order solvers open up new opportunities for solving extremely large LPs where traditional simplex and interior-point solvers may be too slow or run out of memory when factorizing large sparse matrices. Since the linear dependence explorer requires matrix factorization itself, it seems counterintuitive to include it in the presolve for GPU-accelerated first-order solvers, as one of the main motivations for using such solvers is to *avoid* matrix factorization. Moreover, our experiments in §4 show that most of the problem reduction (on average about 90%) is detected by fast and medium explorers. It is therefore unclear whether the additional reductions detected by slow explorers generally justify the extra presolve time for problems where first-order methods may be the only viable option.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for rows with a single nonzero entry, which can be used to fix the value or update the bounds of a variable [, §1.2].

<!-- chunk {"id": "body-0040", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for equality constraints with two nonzero entries, allowing one variable to be eliminated via substitution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for constraints that are implied by variable bounds and can thus be deleted [, §1.2].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Explorers", "weight": 1.0} -->

Column singleton (P) (in equality constraint)
Searches for equality constraints with a variable appearing in only that constraint, possibly allowing the variable to be substituted and the constraint removed [, §3.2].

<!-- chunk {"id": "body-0043", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for variables whose locks allow them to be fixed [ABG+19, §4.4].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Explorers", "weight": 1.0} -->

Column singleton (D) (in inequality constraint)
Searches for inequality constraints with a singleton column, possibly allowing the variable to be fixed or the inequality constraint converted to an equality constraint [, §1.2].

<!-- chunk {"id": "body-0045", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for constraints that are parallel, allowing many of them to be deleted, [ABG+19, §5.2].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for columns that are parallel, allowing many of them to be aggregated [, §3.6], [ABG+19, §6.3].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for variable bounds implied by the constraints [, §1.2], [ABG+19, §3.2].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for dual variable bounds implied by the dual constraints [, §3.4], [ABG+19, §7.5].

<!-- chunk {"id": "body-0049", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for linearly dependent equality constraints.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for variables that can be eliminated via substitution without introducing excessive fill-in [, §2.2], [ABG+19, §4.5].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for symmetries among variables, allowing variables to be aggregated [GKM+14], [ABG+19, §7.1].

<!-- chunk {"id": "body-0052", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for opportunities to combine constraints to make them sparser, [ABG+19, §5.3].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for opportunities to combine dual constraints to make them sparser [GCW+20].

<!-- chunk {"id": "body-0054", "role": "body", "section": "Explorers", "weight": 1.0} -->

Searches for pairs of variables where one is dominated, i.e., worse than the other with respect to both the constraints and the objective, and can thus possibly be fixed [GKM+15, §4], [ABG+19, §6.4].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Data structures", "weight": 1.0} -->

While most exploration rules are simple to describe, their efficient implementation is often quite involved. To make the exploration phase efficient, a presolver keeps track of several internal statistics, which typically include the number of nonzeros in each row and column of $A$, the variable locks (i.e., the number of constraints that prevent a variable from increasing or decreasing to $\pm \infty$), and the smallest and largest value a constraint can take given the current variable bounds (these are often referred to as the *minimum* and *maximum activity* of a constraint \[ABG+19, §2\]). The internal statistics must be maintained, so they are updated each time a reduction is applied. Furthermore, presolving is arranged in *rounds*. To avoid useless work from re-examining all constraints in every round to identify opportunities for reductions, one option is to keep track of the constraints modified in the previous round and apply operations such as primal propagation only to those constraints.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Data structures", "weight": 1.0} -->

Some of the explorers require fast access to rows while others require fast access to columns. One option is to store the constraint matrix $A$ in compressed sparse row (CSR) format to enable fast and cache-friendly access to rows, and supplement the structure of $A$ by a linked lists superstructure describing its columns. Another option, adopted by PaPILO and our presolver PSLP, is to store $A$ in both CSR and compressed sparse column (CSC) formats. Storing $A$ in CSC format enables fast and cache-friendly access to columns, but care must be taken to ensure that the two representations of $A$ remain consistent once reductions are applied. Furthermore, some reductions require modifying the sparsity pattern of $A$ and may lead to a larger number of nonzero entries in certain rows or columns, so it is useful to append each row in the CSR representation and each column in the CSC representation with a small amount of extra space to allow for new nonzero entries. If the extra space is exhausted for a specific row or column, nearby rows or columns may have more extra space, which can be used after shifting the data for nearby rows or columns.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Our implementation", "weight": 1.0} -->

Our implementation, which is based on the reduction-based abstraction described in §2, is called PSLP (Presolver for Linear Programs) and is available at

<!-- chunk {"id": "body-0058", "role": "body", "section": "Our implementation", "weight": 1.0} -->

PSLP is implemented in C and runs (mostly) single-threaded on the CPU, with certain parts parallelized on two or four POSIX threads. To avoid becoming a bottleneck when used together with a GPU-accelerated LP solver, PSLP is designed to be fast and lightweight. Consequently, it implements only the fast and medium explorers listed in table 1, and omits the slow explorers. For certain problem instances, the additional reductions detected by slow explorers could be large enough to justify their use. However, PSLP does not currently implement slow explorers due to the substantial additional engineering effort required to implement them efficiently, and their marginal benefit in terms of problem-size reduction appears limited. Specifically, PSLP already attains, on average, about a 90% reduction in problem size relative to Gurobi's presolver that implements the slow explorers \[ABG+19\], while being significantly faster (see table 2 in §4).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Our implementation", "weight": 1.0} -->

PSLP is solver independent, meaning that it can be used as a standalone presolver module for any LP solver. Its interface is minimal and just requires the user to provide pointers to the problem data, so solvers that lack a built-in presolver can easily integrate it as an external component with just a few lines of code. PSLP takes in an LP of the form, and emits a reduced LP on the same form. Given an (approximate) solution to the reduced problem, it recovers an (approximate) solution to the original problem, i.e., $(x^{\star},y^{\star},z^{\star})$ (approximately) satisfying.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we first compare the presolve performance of PSLP against the commercial state-of-the-art presolver implemented in Gurobi \[ABG+19\]. There are two main reasons for this comparison. First, we wish to gain insight into the relative importance of fast and medium explorers versus slow explorers, as PSLP implements only the former while Gurobi's presolver implements all three categories. Second, since a central goal of this paper is to assess whether presolving improves the performance of GPU-accelerated first-order LP solvers, it is essential that the presolver itself is reasonably effective. An inefficient presolver would prevent a fair and honest assessment of the impact of presolving and could distort the results. Comparing PSLP to a commercial state-of-the-art presolver therefore also serves to validate that it is adequate for a fair assessment of the impact of presolving.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experiments", "weight": 1.0} -->

After comparing PSLP to Gurobi's presolver, we evaluate how presolving using PSLP or Gurobi affects the performance of cuPDLPx, a GPU-accelerated first-order LP solver based on PDHG.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Benchmark datasets", "weight": 1.0} -->

We conduct numerical experiments on two LP benchmark datasets. First, we consider Mittelmann's LP collection, which consists of 48 publicly available instances with more than $10^{5}$ nonzero entries. Second, we consider 383 instances derived from root-node LP relaxations of MIPLIB 2017 \[GHG+21\], using the filtering criteria described. We categorize problems into three groups based on their size: *small* ($10^{5}$-$10^{6}$ nonzero entries), *medium* ($10^{6}$-$10^{7}$ nonzero entries), and *large* (more than $10^{7}$ nonzero entries).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Hardware", "weight": 1.0} -->

Problems are presolved on the CPU and solved on the GPU. For the presolve step, we use a Macbook M4 pro (14 cores) with 48 GB of unified memory, and then execute cuPDLPx on a NVIDIA H100-SXM-80GB GPU with CUDA 12.4.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Setup", "weight": 1.0} -->

We compare PSLP with Gurobi's presolver (version 13.0,

<!-- chunk {"id": "body-0065", "role": "body", "section": "Setup", "weight": 1.0} -->

Arithmetic and geometric mean of the presolve time, given in seconds (denoted by "AM-T" and "GM-T", respectively). For each problem instance, we average the presolve time over 10 runs.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Setup", "weight": 1.0} -->

The average reduction in the number of nonzero entries, given as the ratio of the number of nonzero entries in the reduced problem to that in the original problem (denoted by "ratio (nnz)").

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results", "weight": 1.0} -->

Table 2 summarizes the results. On Mittelmann's LP collection, the average per-instance ratio of Gurobi's presolve time to PSLP's presolve time is 11.8 (not shown in the table). Despite this substantial speedup of an order of magnitude, PSLP on average achieves 90% of the reduction in the number of nonzero entries achieved by Gurobi's presolver. On the MIPLIB relaxations, the corresponding average time ratio is 6.58 (also not shown in the table), while PSLP on average attains 94% of the reduction in the number of nonzero entries achieved by Gurobi's presolver.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Results", "weight": 1.0} -->

Figures 1 and 2 compare the reductions in the number of nonzero entries achieved by PSLP and Gurobi's presolver across the two datasets, together with the corresponding presolve times. (For the MIPLIB relaxations, results are reported only for the 50 largest instances due to space constraints.) Overall, PSLP achieves reductions comparable to those of Gurobi's presolver on all but five instances (`L1_sixm1000obs`, `scpm1`, and `L1_sixm250obs` from Mittelmann's LP collection, and `neos-3208254-reui` and `scpm2` from the MIPLIB relaxations), while often requiring significantly less presolve time.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Solver", "weight": 1.0} -->

We run cuPDLPx (version 0.2.5) both with and without PSLP and Gurobi's presolver enabled. The termination criterion adopted by cuPDLPx depends on a relative tolerance parameter $\epsilon_{\text{rel}} > 0$. We use $\epsilon_{\text{rel}} = 10^{- 8}$ in all experiments, which corresponds to the default value for higher accuracy.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Time limit", "weight": 1.0} -->

For the MIPLIB relaxations, we set a time limit of 3600 seconds for small and medium-sized problems, and 18000 seconds for large problems. For Mittelmann's LP collection, we set a time limit of 15000 seconds. (These time limits are the same as those used.) If an instance remains unsolved when the time limit is reached, we count it as a failure and set its solve time to the time limit for the purpose of computing average solve times.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

Count: The number of problems solved within the time limit.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

SGM: We use the shifted geometric mean of the total solve time, given in seconds. The shifted geometric mean is defined as ${({\prod_{i = 1}^{K}{({t_{i} + \Delta})}})}^{1/K} - \Delta$, where $t_{i}$ is the total solve time for the $i$th instance (in seconds), $K$ is the total number of instances, and $\Delta > 0$ is the shift. We shift by $\Delta = 1$ and $\Delta = 10$ seconds and denote these metrics as SGM1 and, respectively. Without presolving, the total solve time is simply the time taken by cuPDLPx to solve the original problem. With presolving, the total solve time is the sum of the presolve time and the time taken by cuPDLPx to solve the reduced problem.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

Win rate: The percentage of problem instances for which the total solve time with presolve enabled is less than the total solve time with presolve disabled.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Presolve impact on total solve time", "weight": 1.0} -->

Table 3 summarizes the results. We see that enabling PSLP improves the shifted geometric mean in all three categories for both datasets compared to the case with presolve disabled. The improvement is more significant for the large problems, with almost a three-fold improvement for Mittelmann's LP collection and more than a nine-fold improvement for the MIPLIB relaxations. We also see that the solve times with either PSLP or Gurobi's presolver enabled are similar. Interestingly, given the significant improvement in solve time with presolve enabled, the win rate (i.e., the percentage of instances for which presolve enabled is faster than presolve disabled) is lower than one might expect. One possible explanation is that for problems where cuPDLPx already converges fast with a modest number of iterations, presolving becomes harmful. On the other hand, there exist problems where cuPDLPx is very slow without presolve but becomes fast with presolve, which gives a significant improvement in solve time. We illustrate this in Figure 3, which for each problem instance shows the speedup of enabling PSLP for cuPDLPx.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Presolve impact on total solve time", "weight": 1.0} -->

In the right part of the figure, which corresponds to problems with the longest solve time without presolve, we see that the speedup from presolve can be orders of magnitude.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Time spent in presolve", "weight": 1.0} -->

We analyze the ratio between the time spent in presolve and the time spent on solving the *reduced* problem. Table 4 summarizes the average ratio across different problem categories. We see that the presolve time for PSLP is generally a small fraction of the solve time that tends to be more significant for larger problems. Gurobi's presolve time is even more significant and sometimes dominates the time spent on solving the reduced problem.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have revisited LP presolving, a classical topic in the optimization literature, from the perspective of GPU-accelerated first-order solvers. While a myriad of presolve techniques have been proposed over the decades, a systematic investigation of their cost-effectiveness in the context of GPU-accelerated first-order methods has been lacking. To address this, we organized these techniques into a three-class taxonomy based on computational cost and implemented the two cheaper classes in PSLP, a new open-source presolver designed to be lightweight.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Discussion", "weight": 1.5} -->

A lightweight presolver can achieve reductions comparable to those of a sophisticated state-of-the-art commercial presolver, at a fraction of the computational cost (see table 2 and figures 1 and 2).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Discussion", "weight": 1.5} -->

The time spent in presolve can be significant relative to the time spent on solving the reduced problem (see table 4).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Discussion", "weight": 1.5} -->

Lightweight presolve can substantially improve the end-to-end performance of GPU-accelerated first-order solvers (see table 3). While many problems are largely unaffected by presolve, the speedup can be orders of magnitude for certain larger problems (see figure 3).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion", "weight": 1.5} -->

Presolve has traditionally been regarded as a preprocessing step whose cost is negligible relative to the solve phase. Our first two findings challenge this assumption in the context of GPU-accelerated first-order methods, and together highlight the growing importance of presolve cost. As GPU hardware improves, the solve phase of first-order methods will continue to accelerate, but the sequential nature of presolving means it will not benefit from these advances to the same extent. Over time, presolve therefore risks becoming an increasingly dominant fraction of the total solve time. Our results show that by restricting to cheaper presolve techniques, much of the reduction benefit can be retained without presolve becoming an excessive bottleneck. Nonetheless, even with a lightweight presolver such as PSLP, the presolve time is already non-negligible (see table 4). As first-order solvers become faster, the overall speedup in total solve time may therefore be limited unless the presolve phase itself is accelerated.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion", "weight": 1.5} -->

(For example, if cuPDLPx became twice as fast due to hardware improvements, a rough estimate based on table 4 suggests that the speedup in total solve time for large MIPLIB problems would be about $1.20 \times$ if Gurobi's presolver were used, rather than the expected $2 \times$.) While skipping presolve altogether is possible, our results demonstrate the benefit of presolving with PSLP, suggesting that it should generally not be skipped in solvers similar to cuPDLPx. More broadly, future research should consider accelerating not only the solve phase but also the presolve phase, which has been largely neglected in the literature. Given the substantial engineering effort required to develop an efficient presolver, such research questions have until now been impractical to explore. By open-sourcing PSLP, we hope to enable and encourage research in this direction.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our third finding highlights the continued importance of presolving for linear programming, even in the current era of GPU-accelerated first-order solvers. It also indicates that presolving has a stronger impact on first-order solvers (at least cuPDLPx) than is suggested by the seminal work of \[ADH+21\], where PaPILO was used for presolving and only very marginal reductions in iteration counts were reported when presolving was applied prior to a first-order method. Furthermore, the presolve time (which is significant relative to the solve time for the reduced problem) was not included in the performance metrics reported in \[ADH+21\].

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion", "weight": 1.5} -->

An efficient LP presolver forms the foundation of presolvers for more general problem classes. In ongoing work, we are extending PSLP to support quadratic programs and convex conic programs involving second-order cones and exponential cones.
