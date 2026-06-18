## Introduction

One of the oldest easily-stated nontrivial problems in computational geometry is the Fermat-Weber problem: given a set of $n$ points in $d$ dimensions ${a^{},\ldots,a^{(n)}} \in {\mathbb{R}}^{d}$, find a point $x_{\ast} \in {\mathbb{R}}^{d}$ that minimizes the sum of Euclidean distances to them:

This problem, also known as the *geometric median problem,* is well studied and has numerous applications. It is often considered over low dimensional spaces in the context of the facility location problem and over higher dimensional spaces it has applications to clustering in machine learning and data analysis. For example, computing the geometric median is a subroutine in popular expectation maximization heuristics for $k$-medians clustering.

The problem is also important to robust estimation, where we like to find a point representative of given set of points that is resistant to outliers. The geometric median is a rotation and translation invariant estimator that achieves the optimal *breakdown point* of 0.5, i.e. it is a good estimator even when up to half of the input data is arbitrarily corrupted. Moreover, if a large constant fraction of the points lie in a ball of diameter $\epsilon$ then the geometric median lies in that ball with diameter $O{(\epsilon}$) (see Lemma 23). Consequently, the geometric median can be used to turn expected results into high probability results: e.g. if the $a^{(i)}$ are drawn independently such that ${{\mathbb{E}}{\|{x - a^{(i)}}\|}_{2}} \leq \epsilon$ for some $\epsilon > 0$ and $x \in {\mathbb{R}}^{d}$ then this fact, Markov bound, and Chernoff Bound, imply ${\|{x_{\ast} - x}\|}_{2} = {O{(\epsilon)}}$ with high probability in $n$.

Despite the ancient nature of the Fermat-Weber problem and its many uses there are relatively few theoretical guarantees for solving it (see Table 1). To compute a $({1 + \epsilon})$-approximate solution, i.e. $x \in {\mathbb{R}}^{d}$ with ${f{(x)}} \leq {{({1 + \epsilon})}f{(x_{\ast})}}$, the previous fastest running times were either $O{({{d \cdot n^{4/3}}\epsilon^{- {8/3}}})}$ by, $\overset{\sim}{O}{({d{\exp{\epsilon^{- 4}{\log\epsilon^{- 1}}}}})}$ by, $\overset{\sim}{O}\left( {{nd} + {\text{poly}\left( d,\epsilon^{- 1} \right)}} \right)$ by, or $O{({{({nd})}^{O{}}{\log\frac{1}{\epsilon}}})}$ time by. In this paper we improve upon these running times by providing an $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm^11^1If $z$ is the total number of nonzero entries in the coordinates of the $a^{(i)}$ then a careful analysis of our algorithm improves our running time to $O{({z{\log^{3}\frac{n}{\epsilon}}})}$. as well as an $O{({d/\epsilon^{2}})}$ time algorithm, provided we have an oracle for sampling a random $a^{(i)}$. Picking the faster algorithm for the particular value of $\epsilon$ improves the running time to $O{({nd{\log^{3}\frac{1}{\epsilon}}})}$. We also extend these results to compute a $({1 + \epsilon})$-approximate solution to the more general Weber's problem, $\min_{x \in {\mathbb{R}}^{d}}{\sum_{i \in {\lbrack n\rbrack}}{w_{i}{\|{x - a^{(i)}}\|}_{2}}}$ for non-negative $w_{i}$, in time $O{({nd{\log^{3}\frac{1}{\epsilon}}})}$ (see Appendix F).

Our $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm is a careful modification of standard interior point methods for solving the geometric median problem. We provide a long step interior point method tailored to the geometric median problem for which we can implement every iteration in nearly linear time. While our analysis starts with a simple $O{({{({nd})}^{O{}}{\log\frac{1}{\epsilon}}})}$ time interior point method and shows how to improve it, our final algorithm is quite non-standard from the perspective of interior point literature. Our result is one of very few cases we are aware of outperforming traditional interior point theory and the only we are aware of using interior point methods to obtain a nearly linear time algorithm for a canonical optimization problem that traditionally requires superlinear time. We hope our work leads to further improvements in this line of research.

Our $O{({d\epsilon^{- 2}})}$ algorithm is a relatively straightforward application of sampling techniques and stochastic subgradient descent. Some additional insight is required simply to provide a rigorous analysis of the robustness of the geometric median and use this to streamline our application of stochastic subgradient descent. We include it for completeness however, we defer its proof to Appendix C. The bulk of the work in this paper is focused on developing our $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm which we believe uses a set of techniques of independent interest.

### Previous Work

The geometric median problem was first formulated for the case of three points in the early 1600s by Pierre de Fermat. A simple elegant ruler and compass construction was given in the same century by Evangelista Torricelli. Such a construction does not generalize when a larger number of points is considered: Bajaj has shown the even for five points, the geometric median is not expressible by radicals over the rationals. Hence, the $({1 + \epsilon})$-approximate problem has been studied for larger values of $n$.

Many authors have proposed algorithms with runtime polynomial in $n$, $d$ and $1/\epsilon$. The most cited and used algorithm is Weiszfeld's 1937 algorithm. Unfortunately Weiszfeld's algorithm may not converge and if it does it may do so very slowly. There have been many proposed modifications to Weiszfeld's algorithm that generally give non-asymptotic runtime guarantees. In light of more modern multiplicative weights methods his algorithm can be viewed as a re-weighted least squares iteration. Chin et al. considered the more general $L_{2}$ embedding problem: placing the vertices of a graph into ${\mathbb{R}}^{d}$, where some of the vertices have fixed positions while the remaining vertices are allowed to float, with the objective of minimizing the sum of the Euclidean edge lengths. Using the multiplicative weights method, they obtained a run time of $O{({{d \cdot n^{4/3}}\epsilon^{- {8/3}}})}$ for a broad class of problems, including the geometric median problem.^22^2The result of was stated in more general terms than given here. However, it easy to formulate the geometric median problem in their model.

Many authors consider problems that generalize the Fermat-Weber problem, and obtain algorithms for finding the geometric median as a specialization. Badoiu et al. gave an approximate $k$-median algorithm by sub-sampling with the runtime for $k = 1$ of $\overset{\sim}{O}{({d \cdot {\exp{({O{(\epsilon^{- 4})}})}}})}$. Parrilo and Sturmfels demonstrated that the problem can be reduced to semidefinite programming, thus obtaining a runtime of $\overset{\sim}{O}{({\text{poly}{(n,d)}{\log\epsilon^{- 1}}})}$. Furthermore, Bose et al. gave a linear time algorithm for fixed $d$ and $\epsilon^{- 1}$, based on low-dimensional data structures and it has been show how to obtain running times of $\overset{\sim}{O}{({{nd} + {{poly}{(d,\epsilon^{- 1})}}})}$ for this problem and a more general class of problems..

An approach very related to ours was studied by Xue and Ye. They give an interior point method with barrier analysis that runs in time $\overset{\sim}{O}{({{({d^{3} + {d^{2}n}})}\sqrt{n}{\log\epsilon^{- 1}}})}$.

Does not always converge

Chandrasekaran and Tamir
$\overset{\sim}{O}{({{n \cdot \text{poly}}{(d)}{\log\epsilon^{- 1}}})}$

$\overset{\sim}{O}\left( {\left( {d^{3} + {d^{2}n}} \right)\sqrt{n}{\log\epsilon^{- 1}}} \right)$
Interior point with barrier method

$\overset{\sim}{O}\left( {{dn} \cdot \epsilon^{- 2}} \right)$
Optimizes only over x in the input

Parrilo and Sturmfels
$\overset{\sim}{O}\left( {\text{poly}(n,d){\log\epsilon^{- 1}}} \right)$

$\overset{\sim}{O}\left( {d \cdot {\exp\left( {O\left( \epsilon^{- 4} \right)} \right)}} \right)$

Har-Peled and Kushal
$\overset{\sim}{O}\left( {n + {\text{poly}\left( \epsilon^{- 1} \right)}} \right)$

Feldman and Langberg
$\overset{\sim}{O}\left( {{nd} + {\text{poly}\left( d,\epsilon^{- 1} \right)}} \right)$

$\overset{\sim}{O}\left( {{dn^{4/3}} \cdot \epsilon^{- {8/3}}} \right)$

Interior point with custom analysis

Stochastic gradient descent

Table 1: Selected Previous Results.

### Overview of $O\hspace{0pt}{({n\hspace{0pt}d\hspace{0pt}{\log^{3}\frac{n}{\epsilon}}})}$ Time Algorithm

### Interior Point Primer

Our algorithm is broadly inspired by interior point methods, a broad class of methods for efficiently solving convex optimization problems. Given an instance of the geometric median problem we first put the problem in a more natural form for applying interior point methods. Rather than writing the problem as minimizing a convex function over ${\mathbb{R}}^{d}$

we instead write the problem as minimizing a linear function over a convex set:

Clearly, these problems are the same as at optimality $\alpha_{i} = {\|{x^{(i)} - a^{(i)}}\|}_{2}$.

To solve problems of the form (1.2 Time Algorithm ‣ 1 Introduction ‣ Geometric Median in Nearly Linear Time")) interior point methods replace the constraint ${\{\alpha,x\}} \in S$ through the introduction of a *barrier function*. In particular they assume that there is a real valued function $p$ such that as $\{\alpha,x\}$ moves towards the boundary of $S$ the value of $p$ goes to infinity. A popular class of interior point methods known as *path following methods*, they consider relaxations of (1.2 Time Algorithm ‣ 1 Introduction ‣ Geometric Median in Nearly Linear Time")) of the form ${\min_{{\{\alpha,x\}} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}}{{t \cdot 1^{\top}}\alpha}} + {p{(\alpha,x)}}$. The minimizers of this function form a path, known as the central path, parameterized by $t$. The methods then use variants of Newton's method to follow the path until $t$ is large enough that a high quality approximate solution is obtained. The number of iterations of these methods are then typically governed by a property of $p$ known as its self concordance $\nu$. Given a $\nu$-self concordant barrier, typically interior point methods require $O{({\sqrt{\nu}{\log\frac{1}{\epsilon}}})}$ iterations to compute a $({1 + \epsilon})$-approximate solution.

For our particular convex set, the construction of our barrier function is particularly simple, we consider each constraint ${\|{x - a^{(i)}}\|}_{2} \leq \alpha_{i}$ individually. In particular, it is known that the function ${p^{(i)}{(\alpha,x)}} = {- {\ln\left( {\alpha_{i}^{2} - {\|{x - a^{(i)}}\|}_{2}^{2}} \right)}}$ is a 2-self-concordant barrier function for the set $S^{(i)} = \left\{ {{x \in {\mathbb{R}}^{d}},{\alpha \in {\mathbb{R}}^{n}}} \middle| {{\|{x - a^{(i)}}\|}_{2} \leq \alpha_{i}} \right\}$ \[21, Lem 4.3.3\]. Since ${\cap_{i \in {\lbrack n\rbrack}}S^{(i)}} = S$ we can use the barrier $\sum_{i \in {\lbrack n\rbrack}}{p^{(i)}{(\alpha,x)}}$ for $p{(\alpha,x)}$ and standard self-concordance theory shows that this is an $O{(n)}$ self concordant barrier for $S$. Consequently, this easily yields an interior point method for solving the geometric median problem in $O{({{({nd})}^{O{}}{\log\frac{1}{\epsilon}}})}$ time.

### Difficulties

Unfortunately obtaining a nearly linear time algorithm for geometric median using interior point methods as presented poses numerous difficulties. Particularly troubling is the number of iterations required by standard interior point algorithms. The approach outlined in the previous section produced an $O{(n)}$-self concordant barrier and even if we use more advanced self concordance machinery, i.e. the universal barrier, the best known self concordance of barrier for the convex set ${\sum_{i \in {\lbrack n\rbrack}}{\|{x - a^{(i)}}\|}_{2}} \leq c$ is $O{(d)}$. An interesting open question still left open by our work is to determine what is the minimal self concordance of a barrier for this set.

Consequently, even if we could implement every iteration of an interior point scheme in nearly linear time it is unclear whether one should hope for a nearly linear time interior point algorithm for the geometric median. While there are a instances of outperforming standard self-concordance analysis, these instances are few, complex, and to varying degrees specialized to the problems they solve. Moreover, we are unaware of any interior point scheme providing a provable nearly linear time for a general nontrivial convex optimization problem.

### Beyond Standard Interior Point

Despite these difficulties we do obtain a nearly linear time interior point based algorithm that only requires $O{({\log\frac{n}{\epsilon}})}$ iterations, i.e. increases to the path parameter. After choosing the natural penalty functions $p^{(i)}$ described above, we optimize in closed form over the $\alpha_{i}$ to obtain the following penalized objective function:^33^3It is unclear how to extend our proof for the simpler function: $\sum_{i \in {\lbrack n\rbrack}}\sqrt{1 + {t^{2}{\|{x - a^{(i)}}\|}_{2}^{2}}}$.

We then approximately minimize $f_{t}{(x)}$ for increasing $t$. We let $x_{t}\overset{def}{=}{{{\arg\min}_{x \in {\mathbb{R}}^{d}}f_{t}}{(x)}}$ for $x \geq 0$, and thinking of $\left\{ x_{t}:{t \geq 0} \right\}$ as a continuous curve known as the *central path*, we show how to approximately follow this path. As ${\lim_{t\rightarrow\infty}x_{t}} = x_{\ast}$ this approach yields a $({1 + \epsilon})$-approximation.

So far our analysis is standard and interior point theory yields an $\Omega{(\sqrt{n})}$ iteration interior point scheme. To overcome this we take a more detailed look at $x_{t}$. We note that for any $t$ if there is any rapid change in $x_{t}$ it must occur in the direction of the smallest eigenvector of ${\nabla^{2}f_{t}}{(x)}$, denoted $v_{t}$, what we henceforth may refer to as the *bad direction* at $x_{t}.$ More precisely, for all directions $d \perp v_{t}$ it is the case that $d^{\top}{({x_{t} - x_{t^{\prime}}})}$ is small for $t^{\prime} \leq {ct}$ for a small constant $c$.

In fact, we show that this movement over such a *long step,* i.e. a constant increase in $t$, in the directions orthogonal to the bad direction is small enough that for any movement around a ball of this size the Hessian of $f_{t}$ only changes by a small multiplicative constant. In short, starting at $x_{t}$ there exists a point $y$ obtained just by moving from $x_{t}$ in the bad direction, such that $y$ is close enough to $x_{t^{\prime}}$ that standard first order method will converge quickly to $x_{t^{\prime}}$! Thus, we might hope to find such a $y$, quickly converge to $x_{t^{\prime}}$ and repeat. If we increase $t$ by a multiplicative constant in every such iterations, standard interior point theory suggests that $O{({\log\frac{n}{\epsilon}})}$ iterations suffices.

### Building an Algorithm

To turn the structural result in the previous section into a fast algorithm there are several further issues we need to address. We need to

\(1\) Show how to find the point along the bad direction that is close to $x_{t^{\prime}}$

\(2\) Show how to solve linear systems in the Hessian to actually converge quickly to $x_{t^{\prime}}$

\(3\) Show how to find the bad direction

\(4\) Bound the accuracy required by these computations

Deferring for the moment, our solution to the rest are relatively straightforward. Careful inspection of the Hessian of $f_{t}$ reveals that it is well approximated by a multiple of the identity matrix minus a rank 1 matrix. Consequently using explicit formulas for the inverse of of matrix under rank 1 updates, i.e. the Sherman-Morrison formula, we can solve such systems in nearly linear time thereby addressing. For, we show that the well known power method carefully applied to the Hessian yields the bad direction if it exists. Finally, for we show that a constant approximate geometric median is near enough to the central path for $t = {\Theta{(\frac{1}{f{(x_{\ast})}})}}$ and that it suffices to compute a central path point at $t = {O{(\frac{n}{f{(x_{\ast})}\epsilon})}}$ to compute a $1 + \epsilon$-geometric median. Moreover, for these values of $t$, the precision needed in other operations is clear.

The more difficult operation is. Given $x_{t}$ and the bad direction exactly, it is still not clear how to find the point along the bad direction line from $x_{t}$ that is close to $x_{t^{\prime}}$. Just performing binary search on the objective function a priori might not yield such a point due to discrepancies between a ball in Euclidean norm and a ball in hessian norm and the size of the distance from the optimal point in euclidean norm. To overcome this issue we still line search on the bad direction, however rather than simply using $f{({x_{t} + {\alpha \cdot v_{t}}})}$ as the objective function to line search on, we use the function ${g{(\alpha)}} = {{\min_{{\|{x - x_{t} - {\alpha \cdot v_{t}}}\|}_{2} \leq c}f}{(x)}}$ for some constant $c$, that is given an $\alpha$ we move $\alpha$ in the bad direction and take the best objective function value in a ball around that point. For appropriate choice of $c$ the minimizers of $\alpha$ will include the optimal point we are looking for. Moreover, we can show that $g$ is convex and that it suffices to perform the minimization approximately.

Putting these pieces together yields our result. We perform $O{({\log\frac{n}{\epsilon}})}$ iterations of interior point (i.e. increasing $t$), where in each iteration we spend $O{({nd{\log\frac{n}{\epsilon}}})}$ time to compute a high quality approximation to the bad direction, and then we perform $O{({\log\frac{n}{\epsilon}})}$ approximate evaluations on $g{(\alpha)}$ to binary search on the bad direction line, and then to approximately evaluate $g$ we perform gradient descent in approximate Hessian norm to high precision which again takes $O{({nd{\log\frac{n}{\epsilon}}})}$ time. Altogether this yields a $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm to compute a $1 + \epsilon$ geometric median. Here we made minimal effort to improve the log factors and plan to investigate this further in future work.

### Overview of $O\hspace{0pt}{({d\hspace{0pt}\epsilon^{- 2}})}$ Time Algorithm

In addition to providing a nearly linear time algorithm we provide a stand alone result on quickly computing a crude $({1 + \epsilon})$-approximate geometric median in Section C. In particular, given an oracle for sampling a random $a^{(i)}$ we provide an $O{({d\epsilon^{- 2}})}$, i.e. sublinear, time algorithm that computes such an approximate median. Our algorithm for this result is fairly straightforward. First, we show that random sampling can be used to obtain some constant approximate information about the optimal point in constant time. In particular we show how this can be used to deduce an Euclidean ball which contains the optimal point. Second, we perform stochastic subgradient descent within this ball to achieve our desired result.

### Paper Organization

The rest of the paper is structured as follows. After covering preliminaries in Section 2, in Section 3 we provide various results about the central path that we use to derive our nearly linear time algorithm. In Section 4 we then provide our nearly linear time algorithm. All the proofs and supporting lemmas for these sections are deferred to Appendix A ‣ Geometric Median in Nearly Linear Time") and Appendix B ‣ Geometric Median in Nearly Linear Time"). In Appendix C we provide our $O{({d/\epsilon^{2}})}$ algorithm, in Appendix D we provide the derivation of our penalized objective function, in Appendix E we provide general technical machinery we use throughout and in Appendix F we show how to extend our results to Weber's problem, i.e. weighted geometric median.

## Notation

### General Notation

We use bold to denote a matrix. For a symmetric positive semidefinite matrix (PSD), $\mathbf{A}$, we let ${\lambda_{1}{(\mathbf{A})}} \geq \ldots \geq {\lambda_{n}{(\mathbf{A})}} \geq 0$ denote the eigenvalues of $\mathbf{A}$ and let ${v_{1}{(\mathbf{A})}},\ldots,{v_{n}{(\mathbf{A})}}$ denote corresponding eigenvectors. We let ${\| x\|}_{\mathbf{A}}\overset{def}{=}\sqrt{x^{\top}\mathbf{A}x}$ and for PSD we use $\mathbf{A} \preceq \mathbf{B}$ and $\mathbf{B} \preceq \mathbf{A}$ to denote the conditions that ${x^{\top}\mathbf{A}x} \leq {x^{\top}\mathbf{B}x}$ for all $x$ and ${x^{\top}\mathbf{B}x} \leq {x^{\top}\mathbf{A}x}$ for all $x$ respectively.

### Problem Notation

The central problem of this paper is as follows: we are given points ${a^{},\ldots,a^{(n)}} \in {\mathbb{R}}^{d}$ and we wish to compute a geometric median, i.e. $x_{\ast} \in {{{\arg\min}_{x \in {\mathbb{R}}^{d}}f}{(x)}}$ where ${f{(x)}} = {\sum_{i \in {\lbrack n\rbrack}}{\|{a^{(i)} - x}\|}_{2}}$. We call a point $x \in {\mathbb{R}}^{d}$ an $({1 + \epsilon})$-approximate geometric median if ${f{(x)}} \leq {{({1 + \epsilon})}f{(x_{\ast})}}$.

### Penalized Objective Notation

To solve this problem, we smooth the objective function $f$ and instead consider the following family of *penalized objective functions* parameterized by $t > 0$

This penalized objective function is derived from a natural interior point formulation of the geometric median problem (See Section D). For all *path parameters* $t > 0$, we let $x_{t}\overset{def}{=}{{{\arg\min}_{x}f_{t}}{(x)}}$. Our primary goal is to obtain good approximations to the *central path* $\{ x_{t}:{t > 0}\}$ for increasing values of $t$.

We let ${g_{t}^{(i)}{(x)}}\overset{def}{=}\sqrt{1 + {t^{2}{\|{x - a^{(i)}}\|}_{2}^{2}}}$ and ${f_{t}^{(i)}{(x)}}\overset{def}{=}{{g_{t}^{(i)}{(x)}} - {\ln{({1 + {g_{t}^{(i)}{(x)}}})}}}$ so ${f_{t}{(x)}} = {\sum_{i \in {\lbrack n\rbrack}}{f_{t}^{(i)}{(x)}}}$. We refer to the quantity ${w_{t}{(x)}}\overset{def}{=}{\sum_{i \in {\lbrack n\rbrack}}\frac{1}{1 + {g_{t}^{(i)}{(x)}}}}$ as *weight* as it is a natural measure of total contribution of the $a^{(i)}$ to ${\nabla^{2}f_{t}}{(x)}$. We let

denote a weighted harmonic mean of $g$ that helps upper bound the rate of change of the central path. Furthermore, we let $u^{(i)}{(x)}$ denote the unit vector corresonding to $x - a^{(i)}$, i.e. ${u^{(i)}{(x)}}\overset{def}{=}{x - {a^{(i)}/{\|{x - a^{(i)}}\|}_{2}}}$ when ${\|{x - a^{(i)}}\|}_{2} \neq 0$ and ${u^{(i)}{(x)}}\overset{def}{=}0$ otherwise. Finally we let ${\mu_{t}{(x)}}\overset{def}{=}{\lambda_{d}{({{\nabla^{2}f_{t}}{(x)}})}}$ denote the minimum eigenvalue of ${\nabla^{2}f_{t}}{(x)}$, and let $v_{t}{(x)}$ denote a corresponding eigenvector. To simplify notation we often drop the $(x)$ in these definitions when $x = x_{t}$ and $t$ is clear from context.

## Properties of the Central Path

Here provide various facts regarding the penalized objective function and the central path. While we use the lemmas in this section throughout the paper, the main contribution of this section is Lemma 5. ‣ 3.3 Where is the Next Optimal Point? ‣ 3 Properties of the Central Path ‣ Geometric Median in Nearly Linear Time") in Section 3.3. There we prove that with the exception of a single direction, the change in the central path is small over a constant multiplicative change in the path parameter. In addition, we show that our penalized objective function is stable under changes in a $O{(\frac{1}{t})}$ Euclidean ball (Section 3.1), we bound the change in the Hessian over the central path (Section 3.2), and we relate $f{(x_{t})}$ to $f{(x_{\ast})}$ (Section 3.4).

### How Much Does the Hessian Change in General?

Here, we show that the Hessian of the penalized objective function is stable under changes in a $O{(\frac{1}{t})}$ sized Euclidean ball. This shows that if we have a point which is close to a central path point in Euclidean norm, then we can use Newton method to find it.

### Lemma 1

Suppose that ${\|{x - y}\|}_{2} \leq \frac{\epsilon}{t}$ with $\epsilon \leq \frac{1}{20}$. Then, we have

### How Much Does the Hessian Change Along the Path?

Here we bound how much the Hessian of the penalized objective function can change along the central path. First we provide the following lemma bound several aspects of the penalized objective function and proving that the weight, $w_{t}$, only changes by a small amount multiplicatively given small multiplicative changes in the path parameter, $t$.

### Lemma 2

For all $t \geq 0$ and $i \in {\lbrack n\rbrack}$ the following hold

Consequently, for all $t^{\prime} \geq t$ we have that ${\left( \frac{t}{t^{\prime}} \right)^{2}w_{t}} \leq w_{t^{\prime}} \leq {\left( \frac{t^{\prime}}{t} \right)^{2}w_{t}}$.

Next we use this lemma to bound the change in the Hessian with respect to $t$.

### Lemma 3

For all $t \geq 0$ we have

and therefore for all $\beta \in {\lbrack 0,\frac{1}{8}\rbrack}$

### Where is the Next Optimal Point?

Here we prove our main result of this section. We prove that over a long step the central path moves very little in directions orthogonal to the smallest eigenvector of the Hessian. We begin by noting the Hessian is approximately a scaled identity minus a rank 1 matrix.

### Lemma 4

For all $t$, we have

Using this and the lemmas of the previous section we bound the amount $x_{t}$ can move in every direction far from $v_{t}$.

### Lemma 5 (The Central Path is Almost Straight)

For all $t \geq 0$, $\beta \in {\lbrack 0,\frac{1}{600}\rbrack}$, and any unit vector $y$ with ${|{\langle y,v_{t}\rangle}|} \leq \frac{1}{t^{2} \cdot \kappa}$ where $\kappa = {\max_{\delta \in {\lbrack t,{{({1 + \beta})}t}\rbrack}}\frac{w_{\delta}}{\mu_{\delta}}}$, we have ${y^{\top}{({x_{{({1 + \beta})}t} - x_{t}})}} \leq \frac{6\beta}{t}$.

### Where is the End?

In this section, we bound the quality of the central path with respect to the geometric median objective. In particular, we show that if we can solve the problem for some $t = \frac{2n}{\epsilonf{(x_{\ast})}}$ then we obtain an $({1 + \epsilon})$-approximate solution. As our algorithm ultimately starts from an initial $t = {{1/O}{({f{(x_{\ast})}})}}$ and increases $t$ by a multiplicative constant in every iteration, this yields an $O{({\log\frac{n}{\epsilon}})}$ iteration algorithm.

### Lemma 6

${{f{(x_{t})}} - {f{(x_{\ast})}}} \leq \frac{2n}{t}$ for all $t > 0$.

## Nearly Linear Time Geometric Median

Here we show how to use the structural results from the previous section to obtain a nearly linear time algorithm for computing the geometric median. Our algorithm follows a simple structure (See Algorithm 1). First we use simply average the $a^{(i)}$ to compute a 2-approximate median, denoted $x^{}$. Then for a number of iterations we repeatedly move closer to $x_{t}$ for some path parameter $t$, compute the minimum eigenvector of the Hessian, and line search in that direction to find an approximation to a point further along the central path. Ultimately, this yields a point $x^{(k)}$ that is precise enough approximation to a point along the central path with large enough $t$ that we can simply out $x^{(k)}$ as our $({1 + \epsilon})$-approximate geometric median.

Input: desired accuracy ϵ ∈

// Compute a 2-approximate geometric median and use it to center
Compute $x^{}:={\frac{1}{n}{\sum_{i \in {\lbrack n\rbrack}}a^{(i)}}}$ and ${\overset{\sim}{f}}_{\ast}:={f{(x^{})}}$ // Note ${\overset{\sim}{f}}_{\ast} \leq {2f{(x_{\ast})}}$ by Lemma 17
Let $t_{i} = {\frac{1}{400{\overset{\sim}{f}}_{\ast}}{({1 + \frac{1}{600}})}^{i - 1}}$, ${\overset{\sim}{\epsilon}}_{\ast} = {\frac{1}{3}\epsilon}$, and ${\overset{\sim}{t}}_{\ast} = \frac{2n}{{\overset{\sim}{\epsilon}}_{\ast} \cdot {\overset{\sim}{f}}_{\ast}}$.
Let $\epsilon_{v} = {\frac{1}{8}{(\frac{{\overset{\sim}{\epsilon}}_{\ast}}{7n})}^{2}}$ and let $\epsilon_{c} = {(\frac{\epsilon_{v}}{36})}^{\frac{3}{2}}$.

// Iteratively improve quality of approximation
Let $k = {\max_{i \in {\mathbb{Z}}}t_{i}} \leq {\overset{\sim}{t}}_{\ast}$

// Compute ϵv-approximate minimum eigenvalue and eigenvector of ∇2fti (x(i))

// Line search to find x(i+1) such that ${\|{x^{({i + 1})} - x_{t_{i + 1}}}\|}_{2} \leq \frac{\epsilon_{c}}{t_{i + 1}}$

Output: ϵ-approximate geometric median x(k+1).

We split the remainder of the algorithm specification and its analysis into several parts. First in Section 4.1 we show how to compute an approximate minimum eigenvector and eigenvalue of the Hessian of the penalized objective function. Then in Section 4.2 we show how to use this eigenvector to line search for the next central path point. Finally, in Section 4.3 we put these results together to obtain our nearly linear time algorithm. Throughout this section we will want an upper bound to $f{(x_{\ast})}$ and a slight lower bound on $\epsilon$, the geometric median accuracy we are aiming for. We use an easily computed ${\overset{\sim}{f}}_{\ast} \leq {2f{(x_{\ast})}}$ for the former and ${\overset{\sim}{\epsilon}}_{\ast} = {\frac{1}{3}\epsilon}$ throughout the section.

### Eigenvector Computation and Hessian Approximation

Here we show how to compute the minimum eigenvector of ${\nabla^{2}f_{t}}{(x)}$ and thereby obtain a concise approximation to ${\nabla^{2}f_{t}}{(x)}$. Our main algorithmic tool is the well known power method and the fact that it converges quickly on a matrix with a large eigenvalue gap. To improve our logarithmic terms we need a slightly non-standard analysis of the method and therefore we provide and analyze this method for completeness in Section B.1 ‣ Geometric Median in Nearly Linear Time"). Using this tool we estimate the top eigenvector as follows.

Input: Point x ∈ ℝd, path parameter t, and target accuracy ϵ.
Let $u:={{\mathtt{P}\mathtt{o}\mathtt{w}\mathtt{e}\mathtt{r}\mathtt{M}\mathtt{e}\mathtt{t}\mathtt{h}\mathtt{o}\mathtt{d}}{(\mathbf{A},{\Theta{({\log\left( \frac{n}{\epsilon} \right)})}})}}$

### Lemma 7 (Computing Hessian Approximation)

Let $x \in {\mathbb{R}}^{d}$, $t > 0$, and $\epsilon \in {(0,\frac{1}{4})}$. The algorithm ${\mathtt{A}\mathtt{p}\mathtt{p}\mathtt{r}\mathtt{o}\mathtt{x}\mathtt{M}\mathtt{i}\mathtt{n}\mathtt{E}\mathtt{i}\mathtt{g}}{(x,t,\epsilon)}$ outputs $(\lambda,u)$ in $O{({nd{\log\frac{n}{\epsilon}}})}$ time such that if ${\mu_{t}{(x)}} \leq {\frac{1}{4}t^{2}w_{t}{(x)}}$ then ${\langle{v_{t}{(x)}},u\rangle}^{2} \geq {1 - \epsilon}$ with high probability in $n/\epsilon$. Furthermore, if $\epsilon \leq \left( \frac{\mu_{t}{(x)}}{{{8t^{2}} \cdot w_{t}}{(x)}} \right)^{2}$ then ${\frac{1}{4}\mathbf{Q}} \preceq {{\nabla^{2}f_{t}}{(x)}} \preceq {4\mathbf{Q}}$ with high probability in $n/\epsilon$ where $\mathbf{Q}\overset{def}{=}{{{t^{2} \cdot w_{t}}{(x)}} - {\left( {{{t^{2} \cdot w_{t}}{(x)}} - \lambda} \right)uu^{\top}}}$.

Furthermore, we show that the $v^{(i)}$ computed by this algorithm is sufficiently close to the bad direction. Combining 7. ‣ 4.1 Eigenvector Computation and Hessian Approximation ‣ 4 Nearly Linear Time Geometric Median ‣ Geometric Median in Nearly Linear Time") with the structural results from the previous section and Lemma 28, a minor technical lemma regarding the transitivity of large inner products,we provide the following lemma.

### Lemma 8

Let ${(\lambda,u)} = {{\mathtt{A}\mathtt{p}\mathtt{p}\mathtt{r}\mathtt{o}\mathtt{x}\mathtt{M}\mathtt{i}\mathtt{n}\mathtt{E}\mathtt{i}\mathtt{g}}{(x,t,\epsilon_{v})}}$ for $\epsilon_{v} < \frac{1}{8}$ and ${\|{x - x_{t}}\|}_{2} \leq \frac{\epsilon_{c}}{t}$ for $\epsilon_{c} \leq {(\frac{\epsilon_{v}}{36})}^{\frac{3}{2}}$. If $\mu_{t} \leq {{\frac{1}{4}t^{2}} \cdot w_{t}}$ then with high probability in $n/\epsilon_{v}$ for all unit vectors $y \perp u$, we have ${\langle y,v_{t}\rangle}^{2} \leq {8\epsilon_{v}}$.

Note that this lemma assumes $\mu_{t}$ is small. When $\mu_{t}$ is large, we instead show that the next central path point is close to the current point and hence we do not need to compute the bad direction to center quickly.

### Lemma 9

Suppose $\mu_{t} \geq {{\frac{1}{4}t^{2}} \cdot w_{t}}$ and let $t^{\prime} \in {\lbrack t,{{({1 + \frac{1}{600}})}t}\rbrack}$ then ${\|{x_{t^{\prime}} - x_{t}}\|}_{2} \leq \frac{1}{100t}$.

### Line Searching

Here we show how to line search along the bad direction to find the next point on the central path. Unfortunately, simply performing binary search on objective function directly may not suffice. If we search over $\alpha$ to minimize $f_{t_{i + 1}}{({y^{(i)} + {\alphav^{(i)}}})}$ it is unclear if we actually obtain a point close to $x_{t + 1}$. It might be the case that even after minimizing $\alpha$ we would be unable to move towards $x_{t + 1}$ efficiently.

To overcome this difficulty, we use the fact that over the region ${\|{x - y}\|}_{2} = {O{(\frac{1}{t})}}$ the Hessian changes by at most a constant and therefore we can minimize $f_{t}{(x)}$ over this region extremely quickly. Therefore, we instead line search on the following function

and use that we can evaluate $g_{t,y,v}{(\alpha)}$ approximately by using an appropriate centering procedure. We can show (See Lemma 30) that $g_{t,y,v}{(\alpha)}$ is convex and therefore we can minimize it efficiently just by doing an appropriate binary search. By finding the approximately minimizing $\alpha$ and outputting the corresponding approximately minimizing $x$, we can obtain $x^{({i + 1})}$ that is close enough to $x_{t_{i + 1}}$. For notational convenience, we simply write $g{(\alpha)}$ if $t,y,v$ is clear from the context.

First, we show how we can locally center and provide error analysis for that algorithm.

Input: Point y ∈ ℝd, path parameter t &gt; 0, target accuracy ϵ &gt; 0.
for ${i = {1,\ldots}},{k = {64{\log\frac{1}{\epsilon}}}}$ do

### Lemma 10

Given some $y \in {\mathbb{R}}^{d}$, $t > 0$ and $0 \leq \epsilon \leq \left( \frac{\mu_{t}{(x)}}{{{8t^{2}} \cdot w_{t}}{(x)}} \right)^{2}$. In $O{({nd{\log{(\frac{n}{\epsilon})}}})}$ time ${\mathtt{L}\mathtt{o}\mathtt{c}\mathtt{a}\mathtt{l}\mathtt{C}\mathtt{e}\mathtt{n}\mathtt{t}\mathtt{e}\mathtt{r}}{(y,t,\epsilon)}$ computes $x^{(k)}$ such that with high probability in $n/\epsilon$.

Using this local centering algorithm as well as a general result for minimizing one dimensional convex functions using a noisy oracle (See Section E.3) we obtain our line search algorithm.

Input: Point y ∈ ℝd, current path parameter t, next path parameter t′, bad direction u, target accuracy ϵ
Let $\epsilon_{O} = \left( \frac{\epsilon{\overset{\sim}{\epsilon}}_{\ast}}{160n^{2}} \right)^{2}$, $\ell = {- {6{\overset{\sim}{f}}_{\ast}}}$, $u = {6{\overset{\sim}{f}}_{\ast}}$.
Define the oracle q: ℝ → ℝ by q (α) = ft′ (LocalCenter (y + α u,t′,ϵO))

### Lemma 11

Let $\frac{1}{400f{(x_{\ast})}} \leq t \leq t^{\prime} \leq {{({1 + \frac{1}{600}})}t} \leq \frac{2n}{{\overset{\sim}{\epsilon}}_{\ast} \cdot {\overset{\sim}{f}}_{\ast}}$ and let ${(\lambda,u)} = {{\mathtt{A}\mathtt{p}\mathtt{p}\mathtt{r}\mathtt{o}\mathtt{x}\mathtt{M}\mathtt{i}\mathtt{n}\mathtt{E}\mathtt{i}\mathtt{g}}{(y,t,\epsilon_{v})}}$ for $\epsilon_{v} \leq {\frac{1}{8}{(\frac{{\overset{\sim}{\epsilon}}_{\ast}}{3n})}^{2}}$ and $y \in {\mathbb{R}}^{d}$ such that ${\|{y - x_{t}}\|}_{2} \leq {\frac{1}{t}{(\frac{\epsilon_{v}}{36})}^{\frac{3}{2}}}$. In $O{({nd{\log^{2}{(\frac{n}{{\overset{\sim}{\epsilon}}_{\ast} \cdot \epsilon \cdot \epsilon_{v}})}}})}$ time and $O{({\log{(\frac{n}{{\overset{\sim}{\epsilon}}_{\ast} \cdot \epsilon})}})}$ calls to the $\mathtt{L}\mathtt{o}\mathtt{c}\mathtt{a}\mathtt{l}\mathtt{C}\mathtt{e}\mathtt{n}\mathtt{t}\mathtt{e}\mathtt{r}$, ${\mathtt{L}\mathtt{i}\mathtt{n}\mathtt{e}\mathtt{S}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{c}\mathtt{h}}{(y,t,t^{\prime},u,\epsilon)}$ outputs $x^{\prime}$ such that ${\|{x^{\prime} - x_{t^{\prime}}}\|}_{2} \leq \frac{\epsilon}{t^{\prime}}$ with high probability in $n/\epsilon$.

We also provide the following lemma useful for finding the first center.

### Lemma 12

Let $\frac{1}{400f{(x_{\ast})}} \leq t \leq t^{\prime} \leq {{({1 + \frac{1}{600}})}t} \leq \frac{2n}{{\overset{\sim}{\epsilon}}_{\ast} \cdot {\overset{\sim}{f}}_{\ast}}$ and let $x \in {\mathbb{R}}^{d}$ satisfy ${\|{x - x_{t}}\|}_{2} \leq \frac{1}{100t}$. Then, in $O{({nd{\log^{2}{(\frac{n}{\epsilon \cdot {\overset{\sim}{\epsilon}}_{\ast}})}}})}$ time, ${\mathtt{L}\mathtt{i}\mathtt{n}\mathtt{e}\mathtt{S}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{c}\mathtt{h}}{(x,t,t,u,\epsilon)}$ outputs $y$ such that ${\|{y - x_{t}}\|}_{2} \leq \frac{\epsilon}{t}$ for any vector $u \in {\mathbb{R}}^{d}$.

### Putting It All Together

Combining the results of the previous sections, we prove our main theorem.

### Theorem 1

In $O{({nd{\log^{3}{(\frac{n}{\epsilon})}}})}$ time, Algorithm 1 outputs an $({1 + \epsilon})$-approximate geometric median with constant probability.
