Optimization over Nonnegative and Convex Polynomials with and without Semidefinite Programming

Topics include Polynomial optimization, Sum of squares, Semidefinite programming, DSOS, SDSOS, Nonnegative polynomials, Convex polynomials, Linear programming, Second-order cone programming.

Studies polynomial optimization through both classical SOS/SDP machinery and scalable alternatives based on DSOS and SDSOS certificates. The dissertation is valuable as a bridge between nonnegative-polynomial theory, convex-polynomial structure, and large-scale conic relaxations that trade SDP strength for LP/SOCP tractability.

The problem of optimizing over the cone of nonnegative polynomials is a fundamental problem in computational mathematics, with applications to polynomial optimization, control, machine learning, game theory, and combinatorics, among others. A number of breakthrough papers in the early 2000s showed that this problem, long thought to be out of reach, could be tackled by using sum of squares programming. This technique however has proved to be expensive for large-scale problems, as it involves solving large semidefinite programs (SDPs). In the first part of this thesis, we present two methods for approximately solving large-scale sum of squares programs that dispense altogether with semidefinite programming and only involve solving a sequence of linear or second order cone programs generated in an adaptive fashion. We then focus on the problem of finding tight lower bounds on polynomial optimization problems (POPs), a fundamental task in this area that is most commonly handled through the use of SDP-based sum of squares hierarchies (e.g., due to Lasserre and Parrilo)....

### Introduction

Semidefinite programming is a powerful tool in optimization that is used in many different contexts, perhaps most notably to obtain strong bounds on discrete optimization problems or nonconvex polynomial programs. One difficulty in applying semidefinite programming is that state-of-the-art general-purpose solvers often cannot solve very large instances reliably and in a reasonable amount of time. As a result, at relatively large scales, one has to resort either to specialized solution techniques and algorithms that employ problem structure, or to easier optimization problems that lead to weaker bounds....

At a high level, our goal is to not solve semidefinite programs (SDPs) to optimality, but rather replace them with cheaper conic relaxations---*linear and second order cone relaxations* to be precise---that return useful bounds quickly. Throughout the chapter, we will aim to find lower bounds (for minimization problems); i.e., bounds that certify the distance of a candidate solution to optimality....

Figure 8.8: Comparative performance of testing and training sets for 10 fold cross validation.

The best performing algorithm is the monotonically and convexly constrained degree 2 polynomial with average test RMSE: $250.0$ and standard error $39.2$. The algorithm with the smallest standard error, therefore the one with the most consistent performance is the degree 3 hybrid polynomial with test RMSE: $285.0 \pm 29.9$. In comparison, the CAP and Fast CAP algorithm have test RMSE: $385.7 \pm 20.8$. Our algorithm does not only perform better in terms of RMSE, it also has a better runtime performance....

Identical conditions involving $z_{n,d}$ instead of ${\overset{\sim}{z}}_{n,d}$ define the sets of dsos and sdsos forms.

For the converse, assume that $f_{\gamma}{(x,s,y)}$ is not positive definite. As $f_{\gamma}{(x,s,y)}$ is a sum of squares and hence nonnegative, this means that there exists nonzero $(\overline{x},\overline{s},\overline{y})$ such that ${f{(\overline{x},\overline{s},\overline{y})}} = 0$. We proceed in two cases. If $\overline{y} \neq 0$, it is easy to see that ${({\overline{x}/\overline{y}},{\overline{s}/\overline{y}})} \in T_{s}$ and $T_{s}$ is nonempty. Consider now the case where $\overline{y} = 0$. The third square in $f_{\gamma}$ being equal to zero gives us:
