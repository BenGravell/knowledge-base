<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Geometric Median in Nearly Linear Time

Topics include Geometric median, Gradient descent, Optimization, Nearly linear time, Computational geometry, Running time.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we provide faster algorithms for solving the geometric median problem: given n points in R^(d) compute a point that minimizes the sum of Euclidean distances to the points. This is one of the oldest non-trivial problems in computational geometry yet despite an abundance of research the previous fastest algorithms for computing a (1+epsilon)-approximate geometric median were O(d* n^(4/3)epsilon^(-8/3)) by Chin et. al, tildeO(dexp{epsilon^(-4)logepsilon^(-1)}) by Badoiu et. al, O(nd+poly(d, epsilon^(-1)) by Feldman and Langberg, and O((nd)^(O)logfrac1epsilon) by Parrilo and Sturmfels and Xue and Ye. In this paper we show how to compute a (1+epsilon)-approximate geometric median in time O(ndlog^frac1epsilon) and O(depsilon^(-2)).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While our O(depsilon^(-2)) is a fairly straightforward application of stochastic subgradient descent, our O(ndlog^frac1epsilon) time algorithm is a novel long step interior point method. To achieve this running time we start with a simple O((nd)^(O)logfrac1epsilon) time interior point method and show how to improve it, ultimately building an algorithm that is quite non-standard from the perspective of interior point literature. Our result is one of very few cases we are aware of outperforming traditional interior point theory and the only we are aware of using interior point methods to obtain a nearly linear time algorithm for a canonical optimization problem that traditionally requires superlinear time. We hope our work leads to further improvements in this line of research.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This problem, also known as the *geometric median problem,* is well studied and has numerous applications. It is often considered over low dimensional spaces in the context of the facility location problem and over higher dimensional spaces it has applications to clustering in machine learning and data analysis. For example, computing the geometric median is a subroutine in popular expectation maximization heuristics for $k$-medians clustering.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem is also important to robust estimation, where we like to find a point representative of given set of points that is resistant to outliers. The geometric median is a rotation and translation invariant estimator that achieves the optimal *breakdown point* of 0.5, i.e. it is a good estimator even when up to half of the input data is arbitrarily corrupted. Moreover, if a large constant fraction of the points lie in a ball of diameter $\epsilon$ then the geometric median lies in that ball with diameter $O{(\epsilon}$) (see Lemma 23).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consequently, the geometric median can be used to turn expected results into high probability results: e.g. if the $a^{(i)}$ are drawn independently such that ${{\mathbb{E}}{\|{x - a^{(i)}}\|}_{2}} \leq \epsilon$ for some $\epsilon > 0$ and $x \in {\mathbb{R}}^{d}$ then this fact, Markov bound, and Chernoff Bound, imply ${\|{x_{\ast} - x}\|}_{2} = {O{(\epsilon)}}$ with high probability in $n$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the ancient nature of the Fermat-Weber problem and its many uses there are relatively few theoretical guarantees for solving it (see Table 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we improve upon these running times by providing an $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm^11^1If $z$ is the total number of nonzero entries in the coordinates of the $a^{(i)}$ then a careful analysis of our algorithm improves our running time to $O{({z{\log^{3}\frac{n}{\epsilon}}})}$. as well as an $O{({d/\epsilon^{2}})}$ time algorithm, provided we have an oracle for sampling a random $a^{(i)}$. Picking the faster algorithm for the particular value of $\epsilon$ improves the running time to $O{({nd{\log^{3}\frac{1}{\epsilon}}})}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm is a careful modification of standard interior point methods for solving the geometric median problem. We provide a long step interior point method tailored to the geometric median problem for which we can implement every iteration in nearly linear time. While our analysis starts with a simple $O{({{({nd})}^{O{}}{\log\frac{1}{\epsilon}}})}$ time interior point method and shows how to improve it, our final algorithm is quite non-standard from the perspective of interior point literature. Our result is one of very few cases we are aware of outperforming traditional interior point theory and the only we are aware of using interior point methods to obtain a nearly linear time algorithm for a canonical optimization problem that traditionally requires superlinear time. We hope our work leads to further improvements in this line of research.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our $O{({d\epsilon^{- 2}})}$ algorithm is a relatively straightforward application of sampling techniques and stochastic subgradient descent. Some additional insight is required simply to provide a rigorous analysis of the robustness of the geometric median and use this to streamline our application of stochastic subgradient descent. We include it for completeness however, we defer its proof to Appendix C. The bulk of the work in this paper is focused on developing our $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm which we believe uses a set of techniques of independent interest.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Previous Work", "weight": 1.0} -->

The geometric median problem was first formulated for the case of three points in the early 1600s by Pierre de Fermat. A simple elegant ruler and compass construction was given in the same century by Evangelista Torricelli. Such a construction does not generalize when a larger number of points is considered: Bajaj has shown the even for five points, the geometric median is not expressible by radicals over the rationals. Hence, the $({1 + \epsilon})$-approximate problem has been studied for larger values of $n$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Many authors have proposed algorithms with runtime polynomial in $n$, $d$ and $1/\epsilon$. The most cited and used algorithm is Weiszfeld's 1937 algorithm. Unfortunately Weiszfeld's algorithm may not converge and if it does it may do so very slowly. There have been many proposed modifications to Weiszfeld's algorithm that generally give non-asymptotic runtime guarantees. In light of more modern multiplicative weights methods his algorithm can be viewed as a re-weighted least squares iteration. Chin et al. considered the more general $L_{2}$ embedding problem: placing the vertices of a graph into ${\mathbb{R}}^{d}$, where some of the vertices have fixed positions while the remaining vertices are allowed to float, with the objective of minimizing the sum of the Euclidean edge lengths.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Using the multiplicative weights method, they obtained a run time of $O{({{d \cdot n^{4/3}}\epsilon^{- {8/3}}})}$ for a broad class of problems, including the geometric median problem.^22^2The result of was stated in more general terms than given here. However, it easy to formulate the geometric median problem in their model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Many authors consider problems that generalize the Fermat-Weber problem, and obtain algorithms for finding the geometric median as a specialization. Badoiu et al. gave an approximate $k$-median algorithm by sub-sampling with the runtime for $k = 1$ of $\overset{\sim}{O}{({d \cdot {\exp{({O{(\epsilon^{- 4})}})}}})}$. Parrilo and Sturmfels demonstrated that the problem can be reduced to semidefinite programming, thus obtaining a runtime of $\overset{\sim}{O}{({\text{poly}{(n,d)}{\log\epsilon^{- 1}}})}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Furthermore, Bose et al. gave a linear time algorithm for fixed $d$ and $\epsilon^{- 1}$, based on low-dimensional data structures and it has been show how to obtain running times of $\overset{\sim}{O}{({{nd} + {{poly}{(d,\epsilon^{- 1})}}})}$ for this problem and a more general class of problems..

<!-- chunk {"id": "body-0016", "role": "body", "section": "Previous Work", "weight": 1.0} -->

An approach very related to ours was studied by Xue and Ye. They give an interior point method with barrier analysis that runs in time $\overset{\sim}{O}{({{({d^{3} + {d^{2}n}})}\sqrt{n}{\log\epsilon^{- 1}}})}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Previous Work", "weight": 1.0} -->

$\overset{\sim}{O}\left( {{dn} \cdot \epsilon^{- 2}} \right)$
Optimizes only over x in the input

<!-- chunk {"id": "body-0018", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Interior point with custom analysis

<!-- chunk {"id": "body-0019", "role": "body", "section": "Interior Point Primer", "weight": 1.0} -->

Our algorithm is broadly inspired by interior point methods, a broad class of methods for efficiently solving convex optimization problems. Given an instance of the geometric median problem we first put the problem in a more natural form for applying interior point methods. Rather than writing the problem as minimizing a convex function over ${\mathbb{R}}^{d}$

<!-- chunk {"id": "body-0020", "role": "body", "section": "Interior Point Primer", "weight": 1.0} -->

To solve problems of the form (1.2 Time Algorithm ‣ 1 Introduction ‣ Geometric Median in Nearly Linear Time")) interior point methods replace the constraint ${\{\alpha,x\}} \in S$ through the introduction of a *barrier function*. In particular they assume that there is a real valued function $p$ such that as $\{\alpha,x\}$ moves towards the boundary of $S$ the value of $p$ goes to infinity. A popular class of interior point methods known as *path following methods*, they consider relaxations of (1.2 Time Algorithm ‣ 1 Introduction ‣ Geometric Median in Nearly Linear Time")) of the form ${\min_{{\{\alpha,x\}} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}}{{t \cdot 1^{\top}}\alpha}} + {p{(\alpha,x)}}$. The minimizers of this function form a path, known as the central path, parameterized by $t$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Interior Point Primer", "weight": 1.0} -->

The methods then use variants of Newton's method to follow the path until $t$ is large enough that a high quality approximate solution is obtained. The number of iterations of these methods are then typically governed by a property of $p$ known as its self concordance $\nu$. Given a $\nu$-self concordant barrier, typically interior point methods require $O{({\sqrt{\nu}{\log\frac{1}{\epsilon}}})}$ iterations to compute a $({1 + \epsilon})$-approximate solution.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Difficulties", "weight": 1.0} -->

Unfortunately obtaining a nearly linear time algorithm for geometric median using interior point methods as presented poses numerous difficulties. Particularly troubling is the number of iterations required by standard interior point algorithms. The approach outlined in the previous section produced an $O{(n)}$-self concordant barrier and even if we use more advanced self concordance machinery, i.e. the universal barrier, the best known self concordance of barrier for the convex set ${\sum_{i \in {\lbrack n\rbrack}}{\|{x - a^{(i)}}\|}_{2}} \leq c$ is $O{(d)}$. An interesting open question still left open by our work is to determine what is the minimal self concordance of a barrier for this set.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Difficulties", "weight": 1.0} -->

Consequently, even if we could implement every iteration of an interior point scheme in nearly linear time it is unclear whether one should hope for a nearly linear time interior point algorithm for the geometric median. While there are a instances of outperforming standard self-concordance analysis, these instances are few, complex, and to varying degrees specialized to the problems they solve. Moreover, we are unaware of any interior point scheme providing a provable nearly linear time for a general nontrivial convex optimization problem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Beyond Standard Interior Point", "weight": 1.0} -->

Despite these difficulties we do obtain a nearly linear time interior point based algorithm that only requires $O{({\log\frac{n}{\epsilon}})}$ iterations, i.e. increases to the path parameter. After choosing the natural penalty functions $p^{(i)}$ described above, we optimize in closed form over the $\alpha_{i}$ to obtain the following penalized objective function:^33^3It is unclear how to extend our proof for the simpler function: $\sum_{i \in {\lbrack n\rbrack}}\sqrt{1 + {t^{2}{\|{x - a^{(i)}}\|}_{2}^{2}}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Beyond Standard Interior Point", "weight": 1.0} -->

So far our analysis is standard and interior point theory yields an $\Omega{(\sqrt{n})}$ iteration interior point scheme. To overcome this we take a more detailed look at $x_{t}$. We note that for any $t$ if there is any rapid change in $x_{t}$ it must occur in the direction of the smallest eigenvector of ${\nabla^{2}f_{t}}{(x)}$, denoted $v_{t}$, what we henceforth may refer to as the *bad direction* at $x_{t}.$ More precisely, for all directions $d \perp v_{t}$ it is the case that $d^{\top}{({x_{t} - x_{t^{\prime}}})}$ is small for $t^{\prime} \leq {ct}$ for a small constant $c$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Beyond Standard Interior Point", "weight": 1.0} -->

In fact, we show that this movement over such a *long step,* i.e. a constant increase in $t$, in the directions orthogonal to the bad direction is small enough that for any movement around a ball of this size the Hessian of $f_{t}$ only changes by a small multiplicative constant. In short, starting at $x_{t}$ there exists a point $y$ obtained just by moving from $x_{t}$ in the bad direction, such that $y$ is close enough to $x_{t^{\prime}}$ that standard first order method will converge quickly to $x_{t^{\prime}}$! Thus, we might hope to find such a $y$, quickly converge to $x_{t^{\prime}}$ and repeat. If we increase $t$ by a multiplicative constant in every such iterations, standard interior point theory suggests that $O{({\log\frac{n}{\epsilon}})}$ iterations suffices.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

To turn the structural result in the previous section into a fast algorithm there are several further issues we need to address. We need to

<!-- chunk {"id": "body-0028", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

\(1\) Show how to find the point along the bad direction that is close to $x_{t^{\prime}}$

<!-- chunk {"id": "body-0029", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

\(2\) Show how to solve linear systems in the Hessian to actually converge quickly to $x_{t^{\prime}}$

<!-- chunk {"id": "body-0030", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

\(3\) Show how to find the bad direction

<!-- chunk {"id": "body-0031", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

\(4\) Bound the accuracy required by these computations

<!-- chunk {"id": "body-0032", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

Deferring for the moment, our solution to the rest are relatively straightforward. Careful inspection of the Hessian of $f_{t}$ reveals that it is well approximated by a multiple of the identity matrix minus a rank 1 matrix. Consequently using explicit formulas for the inverse of of matrix under rank 1 updates, i.e. the Sherman-Morrison formula, we can solve such systems in nearly linear time thereby addressing. For, we show that the well known power method carefully applied to the Hessian yields the bad direction if it exists. Finally, for we show that a constant approximate geometric median is near enough to the central path for $t = {\Theta{(\frac{1}{f{(x_{\ast})}})}}$ and that it suffices to compute a central path point at $t = {O{(\frac{n}{f{(x_{\ast})}\epsilon})}}$ to compute a $1 + \epsilon$-geometric median. Moreover, for these values of $t$, the precision needed in other operations is clear.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

The more difficult operation is. Given $x_{t}$ and the bad direction exactly, it is still not clear how to find the point along the bad direction line from $x_{t}$ that is close to $x_{t^{\prime}}$. Just performing binary search on the objective function a priori might not yield such a point due to discrepancies between a ball in Euclidean norm and a ball in hessian norm and the size of the distance from the optimal point in euclidean norm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

To overcome this issue we still line search on the bad direction, however rather than simply using $f{({x_{t} + {\alpha \cdot v_{t}}})}$ as the objective function to line search, we use the function ${g{(\alpha)}} = {{\min_{{\|{x - x_{t} - {\alpha \cdot v_{t}}}\|}_{2} \leq c}f}{(x)}}$ for some constant $c$, that is given an $\alpha$ we move $\alpha$ in the bad direction and take the best objective function value in a ball around that point. For appropriate choice of $c$ the minimizers of $\alpha$ will include the optimal point we are looking. Moreover, we can show that $g$ is convex and that it suffices to perform the minimization approximately.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Building an Algorithm", "weight": 1.0} -->

Putting these pieces together yields our result. We perform $O{({\log\frac{n}{\epsilon}})}$ iterations of interior point (i.e. increasing $t$), where in each iteration we spend $O{({nd{\log\frac{n}{\epsilon}}})}$ time to compute a high quality approximation to the bad direction, and then we perform $O{({\log\frac{n}{\epsilon}})}$ approximate evaluations on $g{(\alpha)}$ to binary search on the bad direction line, and then to approximately evaluate $g$ we perform gradient descent in approximate Hessian norm to high precision which again takes $O{({nd{\log\frac{n}{\epsilon}}})}$ time. Altogether this yields a $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm to compute a $1 + \epsilon$ geometric median. Here we made minimal effort to improve the log factors and plan to investigate this further in future work.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Overview of $O{({d\\epsilon^{- 2}})}$ Time Algorithm", "weight": 1.0} -->

In addition to providing a nearly linear time algorithm we provide a stand alone result on quickly computing a crude $({1 + \epsilon})$-approximate geometric median in Section C. In particular, given an oracle for sampling a random $a^{(i)}$ we provide an $O{({d\epsilon^{- 2}})}$, i.e. sublinear, time algorithm that computes such an approximate median. Our algorithm for this result is fairly straightforward. First, we show that random sampling can be used to obtain some constant approximate information about the optimal point in constant time. In particular we show how this can be used to deduce an Euclidean ball which contains the optimal point. Second, we perform stochastic subgradient descent within this ball to achieve our desired result.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

The rest of the paper is structured as follows. After covering preliminaries in Section 2, in Section 3 we provide various results about the central path that we use to derive our nearly linear time algorithm. In Section 4 we then provide our nearly linear time algorithm. All the proofs and supporting lemmas for these sections are deferred to Appendix A ‣ Geometric Median in Nearly Linear Time") and Appendix B ‣ Geometric Median in Nearly Linear Time"). In Appendix C we provide our $O{({d/\epsilon^{2}})}$ algorithm, in Appendix D we provide the derivation of our penalized objective function, in Appendix E we provide general technical machinery we use throughout and in Appendix F we show how to extend our results to Weber's problem, i.e. weighted geometric median.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Penalized Objective Notation", "weight": 1.0} -->

To solve this problem, we smooth the objective function $f$ and instead consider the following family of *penalized objective functions* parameterized by $t > 0$

<!-- chunk {"id": "body-0039", "role": "body", "section": "Penalized Objective Notation", "weight": 1.0} -->

This penalized objective function is derived from a natural interior point formulation of the geometric median problem (See Section D). For all *path parameters* $t > 0$, we let $x_{t}\overset{def}{=}{{{\arg\min}_{x}f_{t}}{(x)}}$. Our primary goal is to obtain good approximations to the *central path* $\{ x_{t}:{t > 0}\}$ for increasing values of $t$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Properties of the Central Path", "weight": 1.0} -->

Here provide various facts regarding the penalized objective function and the central path. While we use the lemmas in this section throughout the paper, the main contribution of this section is Lemma 5. ‣ 3.3 Where is the Next Optimal Point? ‣ 3 Properties of the Central Path ‣ Geometric Median in Nearly Linear Time") in Section 3.3. There we prove that with the exception of a single direction, the change in the central path is small over a constant multiplicative change in the path parameter. In addition, we show that our penalized objective function is stable under changes in a $O{(\frac{1}{t})}$ Euclidean ball (Section 3.1), we bound the change in the Hessian over the central path (Section 3.2), and we relate $f{(x_{t})}$ to $f{(x_{\ast})}$ (Section 3.4).

<!-- chunk {"id": "body-0041", "role": "body", "section": "How Much Does the Hessian Change in General?", "weight": 1.0} -->

Here, we show that the Hessian of the penalized objective function is stable under changes in a $O{(\frac{1}{t})}$ sized Euclidean ball. This shows that if we have a point which is close to a central path point in Euclidean norm, then we can use Newton method to find it.

<!-- chunk {"id": "body-0042", "role": "body", "section": "How Much Does the Hessian Change Along the Path?", "weight": 1.0} -->

Here we bound how much the Hessian of the penalized objective function can change along the central path. First we provide the following lemma bound several aspects of the penalized objective function and proving that the weight, $w_{t}$, only changes by a small amount multiplicatively given small multiplicative changes in the path parameter, $t$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Where is the Next Optimal Point?", "weight": 1.0} -->

Here we prove our main result of this section. We prove that over a long step the central path moves very little in directions orthogonal to the smallest eigenvector of the Hessian. We begin by noting the Hessian is approximately a scaled identity minus a rank 1 matrix.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Where is the End?", "weight": 1.0} -->

In this section, we bound the quality of the central path with respect to the geometric median objective. In particular, we show that if we can solve the problem for some $t = \frac{2n}{\epsilonf{(x_{\ast})}}$ then we obtain an $({1 + \epsilon})$-approximate solution. As our algorithm ultimately starts from an initial $t = {{1/O}{({f{(x_{\ast})}})}}$ and increases $t$ by a multiplicative constant in every iteration, this yields an $O{({\log\frac{n}{\epsilon}})}$ iteration algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nearly Linear Time Geometric Median", "weight": 1.0} -->

Here we show how to use the structural results from the previous section to obtain a nearly linear time algorithm for computing the geometric median. Our algorithm follows a simple structure (See Algorithm 1). First we use simply average the $a^{(i)}$ to compute a 2-approximate median, denoted $x^{}$. Then for a number of iterations we repeatedly move closer to $x_{t}$ for some path parameter $t$, compute the minimum eigenvector of the Hessian, and line search in that direction to find an approximation to a point further along the central path. Ultimately, this yields a point $x^{(k)}$ that is precise enough approximation to a point along the central path with large enough $t$ that we can simply out $x^{(k)}$ as our $({1 + \epsilon})$-approximate geometric median.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nearly Linear Time Geometric Median", "weight": 1.0} -->

// Compute ϵv-approximate minimum eigenvalue and eigenvector of ∇2fti (x(i))

<!-- chunk {"id": "body-0047", "role": "body", "section": "Nearly Linear Time Geometric Median", "weight": 1.0} -->

We split the remainder of the algorithm specification and its analysis into several parts. First in Section 4.1 we show how to compute an approximate minimum eigenvector and eigenvalue of the Hessian of the penalized objective function. Then in Section 4.2 we show how to use this eigenvector to line search for the next central path point. Finally, in Section 4.3 we put these results together to obtain our nearly linear time algorithm. Throughout this section we will want an upper bound to $f{(x_{\ast})}$ and a slight lower bound on $\epsilon$, the geometric median accuracy we are aiming. We use an easily computed ${\overset{\sim}{f}}_{\ast} \leq {2f{(x_{\ast})}}$ for the former and ${\overset{\sim}{\epsilon}}_{\ast} = {\frac{1}{3}\epsilon}$ throughout the section.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Eigenvector Computation and Hessian Approximation", "weight": 1.0} -->

Here we show how to compute the minimum eigenvector of ${\nabla^{2}f_{t}}{(x)}$ and thereby obtain a concise approximation to ${\nabla^{2}f_{t}}{(x)}$. Our main algorithmic tool is the well known power method and the fact that it converges quickly on a matrix with a large eigenvalue gap. To improve our logarithmic terms we need a slightly non-standard analysis of the method and therefore we provide and analyze this method for completeness in Section B.1 ‣ Geometric Median in Nearly Linear Time"). Using this tool we estimate the top eigenvector as follows.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Line Searching", "weight": 1.0} -->

Here we show how to line search along the bad direction to find the next point on the central path. Unfortunately, simply performing binary search on objective function directly may not suffice. If we search over $\alpha$ to minimize $f_{t_{i + 1}}{({y^{(i)} + {\alphav^{(i)}}})}$ it is unclear if we actually obtain a point close to $x_{t + 1}$. It might be the case that even after minimizing $\alpha$ we would be unable to move towards $x_{t + 1}$ efficiently.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Line Searching", "weight": 1.0} -->

To overcome this difficulty, we use the fact that over the region ${\|{x - y}\|}_{2} = {O{(\frac{1}{t})}}$ the Hessian changes by at most a constant and therefore we can minimize $f_{t}{(x)}$ over this region extremely quickly. Therefore, we instead line search on the following function

<!-- chunk {"id": "body-0051", "role": "body", "section": "Line Searching", "weight": 1.0} -->

and use that we can evaluate $g_{t,y,v}{(\alpha)}$ approximately by using an appropriate centering procedure. We can show (See Lemma 30) that $g_{t,y,v}{(\alpha)}$ is convex and therefore we can minimize it efficiently just by doing an appropriate binary search. By finding the approximately minimizing $\alpha$ and outputting the corresponding approximately minimizing $x$, we can obtain $x^{({i + 1})}$ that is close enough to $x_{t_{i + 1}}$. For notational convenience, we simply write $g{(\alpha)}$ if $t,y,v$ is clear from the context.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Line Searching", "weight": 1.0} -->

First, we show how we can locally center and provide error analysis for that algorithm.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Line Searching", "weight": 1.0} -->

Input: Point y ∈ ℝd, path parameter t &gt; 0, target accuracy ϵ &gt; 0.
for ${i = {1,\ldots}},{k = {64{\log\frac{1}{\epsilon}}}}$ do

<!-- chunk {"id": "body-0054", "role": "body", "section": "Putting It All Together", "weight": 1.0} -->

Combining the results of the previous sections, we prove our main theorem.
