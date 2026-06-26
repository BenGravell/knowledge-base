## Introduction

Averaging dynamics or distributed averaging dynamics has played a fundamental role in the recent studies of various distributed systems and algorithms. Examples of such distributed problems and algorithms include distributed optimization, distributed control of robotic networks, and study of opinion dynamics in social networks.

The study of averaging dynamics is closely related to the study of products of stochastic matrices. Such products have been studied from two perspectives: the theory of Markov chains and the distributed averaging settings. The notable works in the domain of the theory of Markov chain are the early studies of Hajnal and Wolfowitz in and, respectively, where sufficient conditions are derived for the convergence of the products of row-stochastic matrices to a rank one matrix. The exploration of this domain from the distributed averaging perspective was started by the work of and the seminal work of J. Tsitsiklis.

Products of random stochastic matrices have also attracted many mathematicians as such products are examples of convolutions of probability measures on semigroups. Due to the technicalities involved, such studies are confined to identically independently distributed (i.i.d.) random chains or their generalizations in the domain of stationary ergodic chains. From the engineering perspective, this area have been recently explored . In, a necessary and sufficient condition for ergodicity of products of i.i.d. stochastic matrices has been derived. A generalization of such result for stationary and ergodic chains is discussed. In a sequence of papers we have defined fundamental concepts of infinite flow property, infinite flow graph, and $\ell_{1}$-approximation. We have showed that these properties are very closely related to the convergence properties of the product of random stochastic matrices that are not necessarily identically distributed. The current work is a continuation of the line of the aforementioned papers.

In particular, in this paper, we derive a set of necessary and sufficient conditions for ergodicity and convergence of a product of independent random stochastic matrices. Specifically, we study a class of random stochastic matrices, which we refer to as balanced chains and show that this class contains many of the previously studied chains of random and deterministic stochastic matrices. This property was first introduced in our earlier work for discrete-time dynamics and in for continuous-time dynamics. Much research has been done on such a criterion since then (see e.g. ). Unlike the prior work, our work adopts dynamical system point of view for the averaging dynamics: we first draw the connection between the products of random stochastic matrices and the random dynamics driven by such matrices. Then, we show that every dynamics driven by a chain of independent random stochastic matrices admits a time-varying quadratic Lyapunov function. In fact, we show more by establishing that for any convex function, there exists a Lyapunov function adjusted to such a convex function. This result opens up a new window for the study of averaging dynamics and distributed algorithms, as quadratic Lyapunov function has proven to be a powerful tool to study such dynamics for different sub-classes of stochastic chains (see e.g., and ). However, the non-existence of quadratic time-invariant Lyapunov functions was suspected for general class of averaging dynamics, and it was proven later .

After proving the existence of time-varying quadratic Lyapunov functions for averaging dynamics, we introduce a special class of stochastic chains, $\mathcal{P}^{\ast}$ chains, and we show that the products of matrices drawn from this sub-class converge almost surely. We then provide the definition of balanced-ness for random stochastic chains and we show that many previously studied classes of stochastic chains are examples of such balanced chains. Finally, using a geometric property of the balanced chains, we show that such chains are examples of $\mathcal{P}^{\ast}$ chains, which leads to the main result of this paper which can be interpreted as a generalization of the known convergence of $A^{k}$ to a rank-one stochastic matrix (for aperiodic and irreducible stochastic matrix $A$) to the case of inhomogeneous chains of stochastic matrices, as well as independent random chains of such matrices.

The contribution of this work is as follows: 1) we prove the existence of a family of time-varying Lyapunov functions for random averaging dynamics; 2) we introduce class $\mathcal{P}^{\ast}$ of random stochastic chains, and provide necessary and sufficient conditions for the stability of the corresponding dynamics; 3) we introduce balanced chains and we use them to establish some necessary and sufficient conditions for the stability of the resulting dynamics; and 4) we provide an extension of the fundamental convergence result in the non-negative matrix theory.

The paper is organized as follows: in Section 2, we formulate and provide the random setting for our study of the products of random stochastic matrices which will be considered throughout the paper. In Section 3, we study the dynamics related to such matrices and draw the connection between the study of such products and the associated dynamics, and we prove that the dynamics admits a class of time-varying Lyapunov functions, including a quadratic one. Then, we discuss the class $\mathcal{P}^{\ast}$ in Section 4 which plays a central role in our development. We then introduce the class of balanced chains and using the geometric structure of these chains, as well as the developed results in the preceding sections, we characterize the stability of a subclass of those chains. Finally, in Section 6, we apply the developed results to prove an extension of a central result in the non-negative matrix theory on the convergence of $A^{k}$ to a rank-one matrix. We conclude this work by a discussion in Section 7.

## Problem Setting

We work exclusively with row-stochastic matrices, so we simply refer to them as stochastic matrices. Let $(\Omega,\mathcal{F},\Pr)$ be a probability space and let $\{{W{(k)}}\}$ be a chain of $m \times m$ random stochastic matrices, i.e. for all $k \geq 1$, the matrix $W{(k)}$ is a stochastic almost surely and ${W_{ij}{(k)}}:{\Omega\rightarrow{\mathbb{R}}}$ is a Borel-measurable function for all ${i,j} \in {\lbrack m\rbrack}$, where ${\lbrack m\rbrack} = {\{ 1,\ldots,m\}}$. Throughout this paper, we denote random sequences of stochastic matrices by last alphabet letters such as $\{{W{(k)}}\}$ and $\{{U{(k)}}\}$, and we use the first alphabet letters such as $\{{A{(k)}}\}$ and $\{{B{(k)}}\}$ to denote deterministic sequences of stochastic matrices. We also refer to a sequence of stochastic matrices as a stochastic chain, or just simply as a chain.

Let $\{{W{(k)}}\}$ be an independent random chain. Then, we say that $\{{W{(k)}}\}$ is strongly aperiodic if there exists a $\gamma \in {(0,1\rbrack}$ such that Note that if ${W_{ii}{(k)}} \geq \gamma$ almost surely for all $i \in {\lbrack m\rbrack}$ and all $k \geq 1$, then such a chain is strongly aperiodic. Also, note that by summing both sides of the above inequality over $j \neq i$, we obtain Hence, ${\mathsf{E}\left\lbrack {W_{ii}{(k)}} \right\rbrack} \geq \frac{\gamma}{1 - \gamma}$ for all $i \in {\lbrack m\rbrack}$ and all $k \geq 1$. Thus, for a strongly aperiodic chain $\{{W{(k)}}\}$, the expected chain $\{{\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack}\}$ is strongly aperiodic. It follows that a deterministic chain $\{{A{(k)}}\}$ is strongly aperiodic if and only if ${A_{ii}{(k)}} \geq \overset{\sim}{\gamma}$ for some $\overset{\sim}{\gamma} > 0$, and for all $i \in {\lbrack m\rbrack}$ and $k \geq 1$.

For the subsequent use, for an $m \times m$ random (or deterministic) matrix $W$ and a non-trivial index set $S \subset {\lbrack m\rbrack}$ (i.e. $S \neq \varnothing$ and $S \neq {\lbrack m\rbrack}$), we define the quantity $W_{S\overline{S}} = {\sum_{{i \in S},{j \in \overline{S}}}W_{ij}}$, where $\overline{S}$ is the complement of the index set $S$.

We say that an independent random chain $\{{W{(k)}}\}$ is balanced if there exists some $\alpha > 0$ such that From this definition, it can be seen that $\alpha \leq 1$.

Finally, with a given random chain $\{{W{(k)}}\}$, let us associate a random graph $G^{\infty} = {({\lbrack m\rbrack},\mathcal{E}^{\infty})}$ with the vertex set $\lbrack m\rbrack$ and the edge set $\mathcal{E}^{\infty}$ given by We refer to $G^{\infty}$ as the infinite flow graph of $\{{W{(k)}}\}$. By the Kolmogorov's 0-1 law, the infinite flow graph of an independent random chain $\{{W{(k)}}\}$ is almost surely equal to a deterministic graph. It has been shown that this determinstic graph is equal to the infinite flow graph of the expected chain $\{{\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack}\}$ (, Theorem 5).

For a matrix $W$, let $W_{i}$ and $W^{j}$ denote the $i$th row vector and the $j$th column vector of $W$, respectively. Also, for a chain $\{{W{(k)}}\}$, we let with $W{(k:k)} = I$ for all $k \geq 0$. With these preliminary definitions and notation in place, we can state the main result of the current study.

### Theorem 1

Let $\{{W{(k)}}\}$ be an independent random stochastic chain which is balanced and strongly aperiodic. Then, for any $t_{0} \geq 0$, the product $W{(k:t_{0})} = W{(k)}\cdots W{(t_{0} + 1)}$ converges to a random stochastic matrix $W{(\infty:t_{0})}$ almost surely. Furthermore, for all $i,j$ in the same connected component of the infinite flow graph of $\{{W{(k)}}\}$, we have $W_{i}{(\infty:t_{0})} = W_{j}{(\infty:t_{0})}$ almost surely.

To prove Theorem 1, we develop some auxiliary results in the forthcoming sections, while deferring the proof to the last section.

As an immediate consequence of Theorem 1, it follows that $W{(\infty:t_{0})}$ has rank at most $\tau$ where $\tau$ is the number of the connected components of the infinite flow graph $G^{\infty}$ of $\{{W{(k)}}\}$. Thus, if $G^{\infty}$ is a connected graph, the limiting random matrix $W{(\infty:t_{0})} = \lim_{k\rightarrow\infty}W{(k:t_{0})}$ is a rank-one random stochastic matrix almost surely, i.e. $W{(\infty:t_{0})} = ev^{T}{(t_{0})}$ almost surely for some stochastic vector $v{(t_{0})}$. This and Theorem 1 imply that: if an independent random chain $\{{W{(k)}}\}$ is balanced and strongly aperiodic, then $\{{W{(k)}}\}$ is almost surely strongly ergodic (as defined in ) if and only if the infinite flow graph of $\{{W{(k)}}\}$ is connected.

## Dynamic System Perspective

In order to prove Theorem 1, we establish some intermediate results, some of which are applicable to a more general category of random stochastic chains, namely adapted random chains. For this, let $\{{W{(k)}}\}$ be a random chain adapted to a filtration $\{\mathcal{F}_{k}\}$. For an integer $t_{0} \geq 0$ and a vector $v \in {\mathbb{R}}^{m}$, consider the trivial random vector ${x{(t_{0})}}:{\Omega\rightarrow{\mathbb{R}}^{m}}$ defined by ${x{(t_{0},\omega)}} = v$ for all $\omega \in \Omega$. Now, recursively define: Note that $x{(t_{0})}$ is measurable with respect to the trivial $\sigma$-algebra $\{\varnothing,\Omega\}$ and hence, it is measurable with respect to $\mathcal{F}_{t_{0}}$. Also, since $\{{W{(k)}}\}$ is adapted to $\{\mathcal{F}_{k}\}$, it follows that for any $k > t_{0}$, $x{(k)}$ is measurable with respect to $\mathcal{F}_{k}$. We refer to $\{{x{(k)}}\}$ as a random dynamics driven by $\{{W{(k)}}\}$ started at the initial point ${(t_{0},v)} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$. We say that a given property holds for any dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$ if that property holds for any initial point ${(t_{0},v)} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$.

If $\lim_{k\rightarrow\infty}W{(k:t_{0})} = W{(\infty:t_{0})}$ exists almost surely, then the random dynamics $\{{x{(k)}}\}$ converges to $W{(\infty:t_{0})}v$ almost surely for any initial point ${(t_{0},v)} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$. Also, note that for any ${i,j} \in {\lbrack m\rbrack}$, we have ${\lim_{k\rightarrow\infty}{\|{{W_{i}{(k,t_{0})}} - {W_{j}{(k,t_{0})}}}\|}} = 0$ almost surely if and only if ${\lim_{k\rightarrow\infty}\left( {{x_{i}{(k)}} - {x_{j}{(k)}}} \right)} = 0$ almost surely for any initial point. When verifying the latter relation, due to the linearity of the dynamics, it suffices to check that ${\lim_{k\rightarrow\infty}\left( {{x_{i}{(k)}} - {x_{j}{(k)}}} \right)} = 0$ for all the initial points of the form $(t_{0},e_{\ell})$ with $\ell \in {\lbrack m\rbrack}$, where $\{ e_{1},\ldots,e_{m}\}$ is the standard basis for ${\mathbb{R}}^{m}$.

In order to study the limiting behavior of the products $W{(k:t_{0})}$, we study the limiting behavior of the dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$. This enables us to use the dynamic system's tools and its stability theory to draw conclusions about the limiting behavior of the products $W{(k:t_{0})}$.

### Why the Infinite Flow Graph

In this section we provide a result showing the relevance of the infinite flow graph to the study of the product of stochastic matrices. Let us consider a deterministic chain $\{{A{(k)}}\}$ of stochastic matrices and let us define mutual ergodicity and an ergodic index as follows.

### Definition 1

For an $m \times m$ chain $\{{A{(k)}}\}$ of stochastic matrices, we say that an index $i \in {\lbrack m\rbrack}$ is ergodic if $\lim_{k\rightarrow\infty}A_{i}{(k:t_{0})}$ exists for all $t_{0} \geq 0$. Also, we say that two disctinct indices ${i,j} \in {\lbrack m\rbrack}$ are mutually ergodic if $\lim_{k\rightarrow\infty} \parallel A_{i}{(k:t_{0})} - A_{j}{(k:t_{0})} \parallel = 0$.

From the definition it immediately follows that an index $i \in {\lbrack m\rbrack}$ is ergodic for a chain $\{{A{(k)}}\}$ if and only if $\lim_{k\rightarrow\infty}{x_{i}{(k)}}$ exists for any dynamics $\{{x{(k)}}\}$ driven by $\{{A{(k)}}\}$. Similarly, indices ${i,j} \in {\lbrack m\rbrack}$ are mutually ergodic if and only if ${\lim_{k\rightarrow\infty}\left( {{x_{i}{(k)}} - {x_{j}{(k)}}} \right)} = 0$ for any dynamics driven by $\{{A{(k)}}\}$.

The following result illustrates the relevance of the infinite flow graph to the study of the products of stochastic matrices.

### Lemma 1

(, Lemma 2) Two distinct indices ${i,j} \in {\lbrack m\rbrack}$ are mutually ergodic only if $i$ and $j$ belong to the same connected component of the infinite flow graph $G^{\infty}$ of $\{{A{(k)}}\}$.

Generally, if $i$ and $j$ are mutually ergodic indices, it is not necessarily true that they are ergodic indices. As an example, consider the $4 \times 4$ stochastic chain $\{{A{(k)}}\}$ defined: It can be verified that for any starting time $t_{0} \geq 0$ and any $k > t_{0}$, we have $A{(k:t_{0})} = A{(k)}$. Thus, it follows that indices $2$ and $3$ are mutually ergodic, while $\lim_{k\rightarrow\infty}A_{2}{(k:t_{0})}$ and $\lim_{k\rightarrow\infty}A_{3}{(k:t_{0})}$ do not exist.

The following result shows that under special circumstances, we can assert that some indices are ergodic if we know that a certain mutual ergodicity pattern exists in a chain.

### Lemma 2

Let $S$ be a connected component of the infinite flow graph $G^{\infty}$ of a chain $\{{A{(k)}}\}$. Suppose that indices $i$ and $j$ are mutually ergodic for all distinct ${i,j} \in S$. Then, every index $i \in S$ is ergodic.

### Proof

Without loss of generality let us assume that $S = {\{ 1,\ldots,i^{\ast}\}}$ for some $i^{\ast} \in {\lbrack m\rbrack}$. Let $\overline{S}$ be the complement of $S$. For the given chain $\{{A{(k)}}\}$ and the connected component $S$, let the chain $\{{B{(k)}}\}$ be defined: Then, $B{(k)}$ has the block diagonal structure of the following form By construction the chain $\{{B{(k)}}\}$ is stochastic. It can be verified that ${\sum_{k = 1}^{\infty}{|{{A_{ij}{(k)}} - {B_{ij}{(k)}}}|}} < \infty$ for all ${i,j} \in {\lbrack m\rbrack}$. Thus, $\{{B{(k)}}\}$ is an $\ell_{1}$-approximation of $\{{A{(k)}}\}$ as defined. Then, by Lemma 1, it follows that indices $i$ and $j$ are mutually ergodic for the chain $\{{B{(k)}}\}$ for all distinct ${i,j} \in S$. By the block diagonal form of $\{{B{(k)}}\}$, it follows that $i$ and $j$ are mutually ergodic for the ${|S|} \times {|S|}$ chain $\{{B_{1}{(k)}}\}$ and all ${i,j} \in S$. This, however, implies that the chain $\{{B_{1}{(k)}}\}$ is weakly ergodic (as defined in) and, as proven in Theorem 1, this further implies that $\{{B_{1}{(k)}}\}$ is strongly ergodic, i.e. any index $i \in S$ is ergodic for $\{{B_{1}{(k)}}\}$. Again, by the application of Lemma 1, we conclude that any index $i \in S$ is ergodic for $\{{A{(k)}}\}$. Q.E.D.

### Time-varying Lyapunov Functions

Here, we show that under general conditions, a rich family of time-varying Lyapunov functions exists for the dynamics $\{{x{(k)}}\}$ driven by a random chain $\{{W{(k)}}\}$.

Let us define an absolute probability process for an adapted chain $\{{W{(k)}}\}$, which is an extension of the concept of the absolute probability sequence introduced by A. Kolmogorov for deterministic chains .

### Definition 2

We say that a random (vector) process $\{{\pi{(k)}}\}$ is an absolute probability process for a random chain $\{{W{(k)}}\}$ adapted to $\{\mathcal{F}_{k}\}$ if the random process $\{{\pi{(k)}}\}$ is adapted to $\{\mathcal{F}_{k}\}$, the vector $\pi{(k)}$ is stochastic almost surely for all $k \geq 1$, and the following relation holds almost surely When an absolute probability process exists for a chain, we say that the chain admits an absolute probability process.

For a deterministic chain of stochastic matrices $\{{A{(k)}}\}$, Kolmogorov showed in that there exists a sequence of stochastic vectors $\{{v{(k)}}\}$ such that ${v^{T}{({k + 1})}A{({k + 1})}} = {v^{T}{(k)}}$ for all $k \geq 0$. Note that, for an independent random chain, any absolute probability sequence for the expected chain is an absolute probability process for the random chain. Thus, the existence of an absolute probability process for an independent random chain of stochastic matrices follows immediately from the Kolmogorov's existence result. As another non-trivial example of random chains that admit an absolute probability process, one may consider an adapted random chain $\{{W{(k)}}\}$ that is doubly stochastic almost surely. In this case, the static sequence $\{{\frac{1}{m}e}\}$ is an absolute probability process for $\{{W{(k)}}\}$, where $e \in {\mathbb{R}}^{m}$ is the vector with all components equal to 1.

Now, suppose that we have an adapted chain $\{{W{(k)}}\}$ which admits an absolute probability sequence $\{{\pi{(k)}}\}$. Also, let $g:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ be an arbitrary convex function. Let us define the function $V_{g,\pi}:{{{\mathbb{R}}^{m} \times {\mathbb{Z}}^{+}}\rightarrow{\mathbb{R}}}$, as follows: From the definition of an absolute probability process, it follows that $V_{g,\pi}{({x{(k)}},k)}$ is measurable with respect to $\mathcal{F}_{k}$ for any dynamics $\{{x{(k)}}\}$ driven by a chain $\{{W{(k)}}\}$ that is adapted to $\{\mathcal{F}_{k}\}$. Also, since $\pi{(k)}$ is almost surely stochastic vector and $g$ is a convex function, it follows that for any $x \in {\mathbb{R}}^{m}$, we have ${V_{g,\pi}{(x,k)}} \geq 0$ almost surely for all $k \geq 0$.

Next, we show that $V_{g,\pi}$ is a time-varying Lyapunov function for the dynamics for any convex function $g$. In particular, we prove that $\{{V_{g,\pi}{({x{(k)}},k)}}\}$ is a super-martingale sequence irrespective of the initial point for the dynamics $\{{x{(k)}}\}$.

### Theorem 2

Let $\{{W{(k)}}\}$ be an adapted chain that admits an absolute probability process $\{{\pi{(k)}}\}$. Then, for the dynamics started at any initial point ${(t_{0},v)} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$, we have

### Proof

By the definition of $V_{g,\pi}$, we have almost surely where in the second equality we use ${\lbrack \cdot \rbrack}_{i}$ to denote the $i$th component of a vector, while the inequality is obtained by using the convexity of $g{(\cdot)}$ and the fact that matrix $W{(k)}$ is stochastic almost surely. Since $\{{\pi{(k)}}\}$ is an absolute probability process for $\{{W{(k)}}\}$, it follows that ${\mathsf{E}\left\lbrack {{\pi^{T}{({k + 1})}W{({k + 1})}} \mid \mathcal{F}_{k}} \right\rbrack} = {\pi^{T}{(k)}}$. Also, since $x{(k)}$ is measurable with respect to $\mathcal{F}_{k}$, by taking the conditional expectation with respect to $\mathcal{F}_{k}$ on both sides of Eq., we obtain almost surely where the last inequality follows by the convexity of $g$ and Jensen's inequality. The result follows by using ${x{({k + 1})}} = {W{({k + 1})}x{(k)}}$ and the definition of absolute probability process. Q.E.D.

Theorem 2 shows that the dynamics admits infinitely many time-varying Lyapunov functions, provided that $\{{W{(k)}}\}$ admits an absolute probability process.

Since ${V_{g,\pi}{({x{(k)}},k)}} \geq 0$ almost surely for all $k \geq 0$, it follows that $\{{V_{g,\pi}{({x{(k)}},k)}}\}$ is a bounded super-martingale. Hence, it is convergent almost surely irrespective of the initial point of the dynamics $\{{x{(k)}}\}$ and the choice of the convex function $g$.

### Corollary 1

Let $\{{W{(k)}}\}$ be an adapted chain that admits an absolute probability process $\{{\pi{(k)}}\}$. Then, for any dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$ and for any convex function $g:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$, the limit $\lim_{k\rightarrow\infty}{V_{g,\pi}{({x{(k)}},k)}}$ exists almost surely.

### Time-varying Quadratic Lyapunov Function

In the sequel, we focus on the particular choice of function ${g{(s)}} = s^{2}$ in relation. For convenience, we let For this function, we can provide a lower bound for the decrease of the conditional expectations $\mathsf{E}\left\lbrack {{V_{g}{({x{({k + 1})}},{k + 1})}} \mid \mathcal{F}_{k}} \right\rbrack$, which is exact under certain conditions.

### Theorem 3

Let $\{{W{(k)}}\}$ be an adapted random chain with an absolute probability process $\{{\pi{(k)}}\}$. Then, for any dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$, we have almost surely where ${H{(k)}} = {\mathsf{E}\left\lbrack {{W^{T}{({k + 1})}\text{diag}{({\pi{({k + 1})}})}W{({k + 1})}} \mid \mathcal{F}_{k}} \right\rbrack}$ with $\text{diag}{(v)}$ denoting the diagonal matrix induced by a vector $v$ (i.e., with components $v_{i}$ on the main diagonal), and $\sum_{i < j} = {\sum_{i = 1}^{m}\sum_{j = {i + 1}}^{m}}$. Furthermore, if ${\pi^{T}{({k + 1})}W{({k + 1})}} = {\pi^{T}{(k)}}$ almost surely, then the inequality holds as an equality.

### Proof

We have for all $k \geq t_{0}$, Note that the sequence $\{{\pi^{T}{(k)}x{(k)}}\}$ is a martingale, implying that $\{{- {({\pi^{T}{(k)}x{(k)}})}^{2}}\}$ is a super-martingale. Thus, by taking the conditional expectation on both sides of the preceding equality and noticing that $x{(k)}$ is measurable with respect to $\mathcal{F}_{k}$, we have almost surely Further, letting $e \in {\mathbb{R}}^{m}$ be the vector with all components equal to 1, from the definition of $L{(k)}$ we almost surely have for all $k \geq t_{0}$: which holds since $W{(k)}$ is stochastic almost surely and $\{{\pi{(k)}}\}$ is an absolute probability process for $\{{W{(k)}}\}$. Thus, the random matrix $\mathsf{E}\left\lbrack {{L{(k)}} \mid \mathcal{F}_{k}} \right\rbrack$ is symmetric and ${\mathsf{E}\left\lbrack {{L{(k)}} \mid \mathcal{F}_{k}} \right\rbracke} = 0$ almost surely. It can be shown that for a symmetric matrix $A$ with ${Ae} = 0$, we have ${x^{T}Ax} = {- {\sum_{i < j}{A_{ij}{({x_{i} - x_{j}})}^{2}}}}$. Then, it follows that almost surely where ${H{(k)}} = {\mathsf{E}\left\lbrack {{W^{T}{({k + 1})}\text{diag}{({\pi{({k + 1})}})}W{({k + 1})}} \mid \mathcal{F}_{k}} \right\rbrack}$. Using this relation in inequality, we conclude that almost surely In the proof of inequality, the inequality sign appears due to relation only. If ${\pi^{T}{({k + 1})}W{({k + 1})}} = {\pi^{T}{(k)}W{(k)}}$ almost surely, then we have ${\pi^{T}{({k + 1})}x{({k + 1})}} = {\pi^{T}{(k)}x{(k)}}$ almost surely. Thus, relation holds as an equality and, consequently, so does relation. Q.E.D.

One of the important implications of Theorem 3 is the following result.

### Corollary 2

Let $\{{W{(k)}}\}$ be an adapted random chain that admits an absolute probability process $\{{\pi{(k)}}\}$. Then, for any random dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$, we have for all $t_{0} \geq 0$,

### Proof

By taking expectation on both sides of the relation in Theorem 3, we obtain for all $k \geq t_{0}$: Since $x{(k)}$ is measurable with respect to $\mathcal{F}_{k}$, it follows that Using this relation in Eq., we see that for all $k \geq t_{0}$: Hence, ${\sum_{k = t_{0}}^{\infty}{\mathsf{E}\left\lbrack {\sum_{i < j}{L_{ij}{(k)}{({{x_{i}{(k)}} - {x_{j}{(k)}}})}^{2}}} \right\rbrack}} \leq {\mathsf{E}\left\lbrack {V_{\pi}{({x{(t_{0})}},t_{0})}} \right\rbrack}$ for any $t_{0} \geq 0$. Q.E.D.

## Class $\mathcal{P}^{\ast}$

In this section, we introduce a class of random chains, which we refer to as the class $\mathcal{P}^{\ast}$, and we prove one of the central results of this work. In particular, we show that the claim of Theorem 1 holds for any chain that is in the class $\mathcal{P}^{\ast}$ and satisfies some form of aperiodicity.

### Definition 3

The class $\mathcal{P}^{\ast}$ is the class of random adapted chains that admit an absolute probability process $\{{\pi{(k)}}\}$ which is uniformly bounded away from zero almost surely, i.e., ${\pi_{i}{(k)}} \geq p^{\ast}$ almost surely for some scalar $p^{\ast} > 0$, and for all $k \geq 0$ and all $i \in {\lbrack m\rbrack}$. We write this concisely as ${\{{\pi{(k)}}\}} \geq p^{\ast} > 0$.

It may appear that the definition of the class $\mathcal{P}^{\ast}$ is a rather restrictive. Later , we show that in fact the class $\mathcal{P}^{\ast}$ contains a broad family of deterministic and random chains.

To establish the main result of this section, we make use of the following intermediate result.

### Lemma 3

Let $\{{A{(k)}}\}$ be a deterministic chain with the infinite flow graph $G^{\infty} = {({\lbrack m\rbrack},\mathcal{E}^{\infty})}$. Let ${(t_{0},v)} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$ be an initial point for the dynamics driven by $\{{A{(k)}}\}$. If for some $i_{0},j_{0}$ belonging to the same connected component of $G^{\infty}$, then we have

### Proof

Let $i_{0}$ and $j_{0}$ be in the same connected component of $G^{\infty}$ and such that Without loss of generality we may assume that ${x{(t_{0})}} \in {\lbrack{- 1},1\rbrack}^{m}$, for otherwise we can consider the dynamics started at ${y{(t_{0})}} = {\frac{1}{{\|{x{(t_{0})}}\|}_{\infty}}x{(t_{0})}}$. Let $S$ be the vertex set of the connected component in $G^{\infty}$ containing $i_{0},j_{0}$, and without loss of generality assume that $S = {\{ 1,2,\ldots,q\}}$ for some $q \in {\lbrack m\rbrack}$, $q \geq 2$. Then, by the definition of the infinite flow graph, there exists a large enough $K \geq t_{0}$ such that where ${A_{S}{({k + 1})}} = {{A_{S\overline{S}}{({k + 1})}} + {A_{\overline{S}S}{({k + 1})}}}$. Furthermore, since ${\operatorname{lim\ sup}_{k\rightarrow\infty}\left({{x_{i_{0}}{(k)}} - {x_{j_{0}}{(k)}}} \right)} = \alpha > 0$, there exists a time instance $t_{1} \geq K$ such that ${{x_{i_{0}}{(t_{1})}} - {x_{j_{0}}{(t_{1})}}} \geq \frac{\alpha}{2}$.

Let $\sigma:{{\lbrack q\rbrack}\rightarrow{\lbrack q\rbrack}}$ be a permutation such that ${x_{\sigma{}}{(t_{1})}} \geq {x_{\sigma{}}{(t_{1})}} \geq \cdots \geq {x_{\sigma{(q)}}{(t_{1})}}$, i.e. $\sigma$ is an ordering of $\{{x_{i}{(t_{1})}}\mid{i \in {\lbrack q\rbrack}}\}$. Since ${{x_{i_{0}}{(t_{1})}} - {x_{j_{0}}{(t_{1})}}} \geq \frac{\alpha}{2}$, it follows that ${{x_{\sigma{}}{(t_{1})}} - {x_{\sigma{(q)}}{(t_{1})}}} \geq \frac{\alpha}{2}$ and, therefore, there exists $\ell \in {\lbrack q\rbrack}$ such that ${{x_{\sigma{(\ell)}}{(t_{1})}} - {x_{\sigma{({\ell + 1})}}{(t_{1})}}} \geq \frac{\alpha}{2q}$. Let Since $S$ is a connected component of the infinite flow graph $G^{\infty}$, we must have $T_{1} < \infty$; otherwise, $S$ could be decomposed into two disconnected components $\{{\sigma{}},\ldots,{\sigma{(l)}}\}$ and $\{{\sigma{({l + 1})}},\ldots,{\sigma{(q)}}\}$.

Now, let $R = {\{{\sigma{}},\ldots,{\sigma{(l)}}\}}$. We have for any $k \in {\lbrack t_{1},T_{1}\rbrack}$: which follows by the definition of $T_{1}$ and the choice of $t_{1} \geq K$. By Lemma 1, it follows that for $k \in {\lbrack t_{1},T_{1}\rbrack}$, Thus, for any ${i,j} \in {\lbrack q\rbrack}$ with $i \leq l$ and $j \geq {l + 1}$, and for any $k \in {\lbrack t_{1},T_{1}\rbrack}$, we have Further, it follows that: Since ${\operatorname{lim\ sup}_{k\rightarrow\infty}\left({{x_{i_{0}}{(k)}} - {x_{j_{0}}{(k)}}} \right)} = \alpha > 0$, there exists a time $t_{2} > T_{1}$ such that ${{x_{i_{0}}{(t_{2})}} - {x_{j_{0}}{(t_{2})}}} \geq \frac{\alpha}{2}$. Then, using the above argument, there exists $T_{2} > t_{2}$ such that ${\sum_{k = t_{2}}^{T_{2}}{\sum_{i < j}{{({{A_{ij}{({k + 1})}} + {A_{ji}{({k + 1})}}})}{({{x_{i}{(k)}} - {x_{j}{(k)}}})}^{2}}}} \geq \beta$. Hence, using the induction, we can find time instances such that ${\sum_{k = t_{\xi}}^{T_{\xi}}{\sum_{i < j}{{({{A_{ij}{({k + 1})}} + {A_{ji}{({k + 1})}}})}{({{x_{i}{(k)}} - {x_{j}{(k)}}})}^{2}}}} \geq \beta$ for any $\xi \geq 1$. The intervals $\lbrack t_{\xi},T_{\xi}\rbrack$ are non-overlapping subintervals of $\lbrack t_{0},\infty)$, implying that For our main result, let us define the weak aperiodicity for an adapted random chain.

### Definition 4

We say that an adapted random chain $\{{W{(k)}}\}$ is weakly aperiodic if for some $\gamma > 0$, and for all distinct ${i,j} \in {\lbrack m\rbrack}$ and all $k \geq 0$, Now, we establish the main result of this section.

### Theorem 4

Let ${\{{W{(k)}}\}} \in \mathcal{P}^{\ast}$ be an adapted chain that is weakly aperiodic. Then, $\lim_{k\rightarrow\infty}W{(k:t_{0})} = W{(\infty:t_{0})}$ exists almost surely for any $t_{0} \geq 0$. Moreover, the event under which $W_{i}{(\infty:t_{0})} = W_{j}{(\infty:t_{0})}$ for all $t_{0} \geq 0$ is almost surely equal to the event that $i,j$ are belonging to the same connected component of the infinite flow graph of $\{{W{(k)}}\}$.

### Proof

Since $\{{W{(k)}}\}$ is in $\mathcal{P}^{\ast}$, $\{{W{(k)}}\}$ admits an absolute probability process $\{{\pi{(k)}}\}$ such that ${\{{\pi{(k)}}\}} \geq p^{\ast} > 0$ almost surely. Thus, it follows that On the other hand, by the weak aperiodicity, we have for some $\gamma \in {(0,1\rbrack}$ and for all distinct ${i,j} \in {\lbrack m\rbrack}$. Thus, we have ${p^{\ast}\gamma\mathsf{E}\left\lbrack {{W_{ij}{({k + 1})}} + {{W_{ji}{({k + 1})}} \mid \mathcal{F}_{k}}} \right\rbrack} \leq {H_{ij}{({k + 1})}}$. By Corollary 2, for the random dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$ and started at arbitrary ${(t_{0},v)} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$, it follows that Therefore, by Lemma 3, we conclude that ${\lim_{k\rightarrow\infty}\left({{x_{i}{(k,\omega)}} - {x_{j}{(k,\omega)}}} \right)} = 0$ for any $i,j$ belonging to the same connected component of $G^{\infty}{(\omega)}$, for almost all $\omega \in \Omega$. By Lemma 2 it follows that every index $i \in {\lbrack m\rbrack}$ is ergodic for almost all $\omega \in \Omega$. By considering the initial conditions ${(t_{0},e_{\ell})} \in {{\mathbb{Z}}^{+} \times {\mathbb{R}}^{m}}$ for all $\ell \in {\lbrack m\rbrack}$, the assertion follows. Q.E.D.

Theorem 4 shows that the dynamics in is convergent almost surely for aperiodic chains ${\{{W{(k)}}\}} \in \mathcal{P}^{\ast}$. Moreover, the theorem also characterizes the limiting points of such a dynamics as well as the limit matrices of the products $W{(k:t_{0})}$ as $k\rightarrow\infty$.

## Balanced Chains

In this section, we characterize a subclass of $\mathcal{P}^{\ast}$ chains, namely the class of strongly aperiodic balanced chains. We first show that this class includes many of the chains that have been studied in the existing literature. Then, we prove that any aperiodic balanced chain belongs to the class $\mathcal{P}^{\ast}$. We also show that a balanced independent random chain is strongly aperiodic, thus concluding Theorem 1.

Before continuing our analysis on balanced chains, let us discuss some of the well-known subclasses of such chains: Balanced Bidirectional Chains: We say that an independent chain $\{{W{(k)}}\}$ is a balanced bidirectional chain if there exists some $\alpha > 0$ such that ${\mathsf{E}\left\lbrack {W_{ij}{(k)}} \right\rbrack} \geq {\alpha\mathsf{E}\left\lbrack {W_{ji}{(k)}} \right\rbrack}$ for all $k \geq 1$ and ${i,j} \in {\lbrack m\rbrack}$. These chains are in fact balanced, since for any $S \subset {\lbrack m\rbrack}$ we have: Examples of such chains are bounded bidirectional deterministic chains, which are the chains such that ${A_{ij}{(k)}} > 0$ implies ${A_{ji}{(k)}} > 0$ for all $i.{j \in {\lbrack m\rbrack}}$ and all $k \geq 1$, and the positive entries are uniformly bounded from below by some $\gamma > 0$ (i.e., ${A_{ij}{(k)}} > 0$ implies ${A_{ij}{(k)}} \geq \gamma$ for all ${i,j} \in {\lbrack m\rbrack}$ and all $k \geq 1$). In this case, for ${A_{ij}{(k)}} > 0$, we have ${A_{ij}{(k)}} \geq \gamma \geq {\gammaA_{ji}{(k)}}$ and for ${A_{ij}{(k)}} = 0$, we have ${A_{ji}{(k)}} = 0$ and, hence, in either of the cases ${A_{ij}{(k)}} \geq {\gammaA_{ji}{(k)}}$. Therefore, bounded bidirectional chains are examples of balanced bidirectional chains. Such chains have been considered in and, among others, include the Hegselman-Krause model for opinion dynamics.

Chains with Common Steady State $\pi > 0$: This ensemble consists of independent random chains $\{{W{(k)}}\}$ such that ${\mathsf{E}\left\lbrack {\pi^{T}W{(k)}} \right\rbrack} = {\mathsf{E}\left\lbrack {\pi^{T}{(k)}} \right\rbrack}$ for some stochastic vector $\pi > 0$ and all $k \geq 1$, which are generalizations of doubly stochastic chains, where we have $\pi = {\frac{1}{m}e}$ ($e$ is a vector of ones). Doubly stochastic chains and the chains with a common steady state $\pi > 0$ have been studied .

To show that a chain with a common steady state $\pi > 0$ is a balanced chain, let us prove the following lemma.

### Lemma 4

Let $A$ be a stochastic matrix and $\pi > 0$ be a stochastic left-eigenvector of $A$ corresponding to the unit eigenvalue, i.e., ${\pi^{T}A} = \pi^{T}$. Then, $A_{S\overline{S}} \geq {\frac{\pi_{\min}}{\pi_{\max}}A_{\overline{S}S}}$ for any non-trivial $S \subset {\lbrack m\rbrack}$, where $\pi_{\max} = {\max_{i \in {\lbrack m\rbrack}}\pi_{i}}$ and $\pi_{\min} = {\min_{i \in {\lbrack m\rbrack}}\pi_{i}}$.

### Proof

Let $S \subset {\lbrack m\rbrack}$. Since ${\pi^{T}A} = \pi^{T}$, we have On the other hand, since $A$ is a stochastic matrix, we have ${\pi_{i}{\sum_{j \in {\lbrack m\rbrack}}A_{ij}}} = \pi_{i}$. Therefore, Comparing Eq. and Eq., we see that ${\sum_{{i \in \overline{S}},{j \in S}}{\pi_{i}A_{ij}}} = {\sum_{{i \in S},{j \in \overline{S}}}{\pi_{i}A_{ij}}}$. Therefore, Hence, we have $A_{S\overline{S}} \geq {\frac{\pi_{\min}}{\pi_{\max}}A_{\overline{S}S}}$ for any non-trivial $S \subset {\lbrack m\rbrack}$. Q.E.D.

The above lemma shows that a chain with a common steady state $\pi > 0$ is balanced with balancedness coefficient $\alpha = \frac{\pi_{\min}}{\pi_{\max}}$. In fact, the lemma yields a much more general result, as provided below.

### Theorem 5

Let $\{{W{(k)}}\}$ be an independent random chain with a sequence $\{{\pi{(k)}}\}$ of stochastic left-eigenvectors for the expected chain corresponding to the unit eigenvalue, i.e., ${\pi^{T}{(k)}\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack} = {\pi^{T}{(k)}}$ for all $k \geq 1$. If ${\{{\pi{(k)}}\}} \geq p^{\ast}$ for some scalar $p^{\ast} > 0$, then $\{{W{(k)}}\}$ is a balanced chain with a balancedness coefficient $\alpha = \frac{p^{\ast}}{1 - {{({m - 1})}p^{\ast}}}$.

### Proof

Since ${\pi^{T}{(k)}\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack} = {\pi^{T}{(k)}}$ for all $k \geq 1$, by Lemma 4 we have By ${\{{\pi{(k)}}\}} \geq p^{\ast} > 0$, it follows that${\pi_{\min}{(k)}} \geq p^{\ast}$ for all $k \geq 1$. Since $\pi{(k)}$ is a stochastic vector, it further follows ${\pi_{\max}{(k)}} \leq {1 - {{({m - 1})}\pi_{\min}{(k)}}} \leq {1 - {{({m - 1})}p^{\ast}}}$. Therefore, for all $k \geq 1$, for any non-trivial $S \subset {\lbrack m\rbrack}$. Thus, $\{{W{(k)}}\}$ is balanced with a balancedness coefficient $\alpha = \frac{p^{\ast}}{1 - {{({m - 1})}p^{\ast}}}$. Q.E.D.

Theorem 5 not only characterizes a class of balanced chains, but it also provides an alternative characterization of the balancedness for these chains. Thus, instead of verifying Definition 1 for every nontrivial subset $S \subset {\lbrack m\rbrack}$, for balancedness of independent random chains, it suffices to find a sequence $\{{\pi{(k)}}\}$ of stochastic (unit) left-eigenvectors of the expected chain $\{{\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack}\}$ such that the entries of the sequence do not vanish as time goes to infinity.

### Absolute Probability Sequence for Balanced Chains

In this section, we show that any independent random chain that is strongly aperiodic and balanced must be in the class $\mathcal{P}^{\ast}$. The road map to prove this result is as follows: we first show that this result holds for deterministic chains with uniformly bounded positive entries. Then, using this result and geometric properties of the set of strongly aperiodic balanced chains, we prove the statement for deterministic chains, which immediately implies the result for independent random chains. To show the result for deterministic chains with uniformly bounded positive entries, we employ the technique that is used to prove Proposition 4 . However, the argument given in needs some extensions to fit in our more general assumption of balanced-ness.

Let $\{{A{(k)}}\}$ be a deterministic chain of stochastic matrices. Let $S_{j}{(k)}$ be the set of indices corresponding to the positive entries in the $j$th column of $A{(k:0)}$, i.e., Also, let $\mu_{j}{(k)}$ be the minimum value of these positive entries, i.e.,

### Lemma 5

Let $\{{A{(k)}}\}$ be a strongly aperiodic balanced chain such that the positive entries in each $A{(k)}$ are uniformly bounded from below by a scalar $\gamma > 0$. Then, ${S_{j}{(k)}} \subseteq {S_{j}{({k + 1})}}$ and ${\mu_{j}{(k)}} \geq \gamma^{{|{S_{j}{(k)}}|} - 1}$ for all $j \in {\lbrack m\rbrack}$ and $k \geq 0$.

### Proof

Let $j \in {\lbrack m\rbrack}$ be arbitrary but fixed. By induction on $k$, we prove that ${S_{j}{(k)}} \subseteq {S_{j}{({k + 1})}}$ for all $k \geq 0$ as well as the desired relation for $\mu_{j}{(k)}$. For $k = 0$, we have $A{(0:0)} = I$ by the definition, so ${S_{j}{}} = {\{ j\}}$. Then, $A{(1:0)} = A{}$ and by the strongly aperiodic assumption on the chain $\{{A{(k)}}\}$ we have ${A_{jj}{}} \geq \gamma$, implying ${\{ j\}} = {S_{j}{}} \subseteq {S_{j}{}}$. Furthermore, we have ${{|{S_{j}{}}|} - 1} = 0$ and ${\mu_{j}{}} = 1 = \gamma^{0}$. Hence, the claim is true for $k = 0$.

Now suppose that the claim is true for some $k \geq 0$, and consider $k + 1$. Then, for any $i \in {S_{j}{(k)}}$, we have: Thus, $i \in {S_{j}{({k + 1})}}$, implying ${S_{j}{(k)}} \subseteq {S_{j}{({k + 1})}}$.

To show the relation for $\mu_{j}{({k + 1})}$, we consider two cases:\Case ${A_{S_{j}{(k)}{\overline{S}}_{j}{(k)}}{({k + 1})}} = 0$: In this case for any $i \in {S_{j}{(k)}}$, we have: where the inequality follows from $i \in {S_{j}{(k)}}$ and ${A_{S_{j}{(k)}{\overline{S}}_{j}{(k)}}{({k + 1})}} = 0$, and the definition of $\mu_{j}{(k)}$. Furthermore, by the balancedness of $A{(k)}$ and ${A_{S_{j}{(k)}{\overline{S}}_{j}{(k)}}{({k + 1})}} = 0$, it follows that $0 = {A_{S_{j}{(k)}{\overline{S}}_{j}{(k)}}{({k + 1})}} \geq {\alphaA_{{\overline{S}}_{j}{(k)}S_{j}{(k)}}{({k + 1})}} \geq 0$. Hence, ${A_{{\overline{S}}_{j}{(k)}S_{j}{(k)}}{({k + 1})}} = 0$. Thus, for any $i \in {{\overline{S}}_{j}{(k)}}$, we have where the second equality follows from $A_{\ellj}{(k:0)} = 0$ for all $\ell \in {{\overline{S}}_{j}{(k)}}$. Therefore, in this case we have ${S_{j}{({k + 1})}} = {S_{j}{(k)}}$, which by implies ${{\mu_{j}{({k + 1})}} \geq {\mu_{j}{(k)}}}.$ In view of ${S_{j}{({k + 1})}} = {S_{j}{(k)}}$ and the inductive hypothesis, we further obtain implying ${\mu_{j}{({k + 1})}} \geq \gamma^{{|{S_{j}{({k + 1})}}|} - 1}$.\Case ${A_{S_{j}{(k)}{\overline{S}}_{j}{(k)}}{({k + 1})}} > 0$: Since the chain is balanced, we have implying that ${A_{{\overline{S}}_{j}{(k)}S_{j}{(k)}}{(k)}} > 0$. Therefore, by the uniform boundedness of $\{{A{(k)}}\}$, there exists $\hat{\xi} \in {{\overline{S}}_{j}{(k)}}$ and $\hat{\ell} \in {S_{j}{(k)}}$ such that ${A_{\hat{\xi}\hat{\ell}}{({k + 1})}} \geq \gamma$. Hence, we have where the equality follows by the induction hypothesis. Thus, $\hat{\xi} \in {S_{j}{({k + 1})}}$ while $\hat{\xi} \notin {S_{j}{(k)}}$, which implies ${|{S_{j}{({k + 1})}}|} \geq {{|{S_{j}{(k)}}|} + 1}$. This, together with $A_{\hat{\xi}j}{(k + 1:0)} \geq \gamma^{|{S_{j}{(k)}}|}$, yields ${\mu_{j}{({k + 1})}} \geq \gamma^{|{S_{j}{(k)}}|} \geq \gamma^{{|{S_{j}{({k + 1})}}|} - 1}$. Q.E.D.

The bound on $\mu_{j}{(k)}$ of Lemma 5 implies that the bound for the nonnegative entries given in Proposition 4 of can be reduced from $\gamma^{{m^{2} - m} + 2}$ to $\gamma^{m - 1}$.

Note that Lemma 5 holds for products $A{(k:t_{0})}$ starting with any $t_{0} \geq 0$, (with appropriately defined $S_{j}{(k)}$ and $\mu_{j}{(k)}$). An immediate corollary of Lemma 5 is the following result.

### Corollary 3

Under the assumptions of Lemma 5, we have for all ${k > t_{0} \geq 0},$ where $e$ is the vector of ones and the inequality is to be understood entry-wise.

### Proof

Without loss of generality, let us assume that $t_{0} = 0$. Then, by Lemma 5 we have $\frac{1}{m}e^{T}A^{j}{(k:0)} \geq \frac{1}{m}|S_{j}{(k)}|\gamma^{{|{S_{j}{(k)}}|} - 1}$ for any $j \in {\lbrack m\rbrack}$, where $A^{j}$ denotes the $j$th column of $A$. For $\gamma \in {\lbrack 0,1\rbrack}$, the function $t\mapsto{t\gamma^{t - 1}}$ defined on $\lbrack 1,m\rbrack$ attains its minimum at either $t = 1$ or $t = m$. Therefore, $\frac{1}{m}e^{T}A{(k:1)} \geq \min{(\frac{1}{m},\gamma^{m - 1})}e^{T}$. Q.E.D.

Now, we relax the assumption on the bounded entries in Corollary 3.

### Theorem 6

Let $\{{A{(k)}}\}$ be a balanced and strongly aperiodic chain. Then, there is a scalar $\gamma \in {(0,1\rbrack}$ such that $\frac{1}{m}e^{T}A{(k:0)} \geq \min{(\frac{1}{m},\gamma^{m - 1})}e^{T}$ for all $k \geq 1$.

### Proof

Let $\alpha > 0$ be a balancedness coefficient for $\{{A{(k)}}\}$ and let ${A_{ii}{(k)}} \geq \beta > 0$ for all $i \in {\lbrack m\rbrack}$ and $k \geq 1$. Further, let $\mathbf{B}_{\alpha,\beta}$ be the set of balanced matrices with the balancedness coefficient $\alpha$ and strongly aperiodic matrices with a coefficient $\beta > 0$, i.e., The description in relation shows that $\mathbf{B}_{\alpha,\beta}$ is a bounded polyhedral set in ${\mathbb{R}}^{m \times m}$. Let $\{{Q^{(\xi)} \in \mathbf{B}_{\alpha,\beta}}\mid{\xi \in {\lbrack n_{\alpha,\beta}\rbrack}}\}$ be the set of extreme points of this polyhedral set indexed by the positive integers between $1$ and $n_{\alpha,\beta},$ which is the total number of extreme points of $\mathbf{B}_{\alpha,\beta}$.

Since ${A{(k)}} \in \mathbf{B}_{\alpha,\beta}$ for all $k \geq 1$, we can write $A{(k)}$ as a convex combination of the extreme points in $\mathbf{B}_{\alpha,\beta}$, i.e., there exist coefficients ${\lambda_{\xi}{(k)}} \in {\lbrack 0,1\rbrack}$ such that Now, consider the following independent random matrix process defined: In view of this definition any sample path of $\{{W{(k)}}\}$ consists of extreme points of $\mathbf{B}_{\alpha,\beta}$. Thus, every sample path of $\{{W{(k)}}\}$ has a coefficient bounded by the minimum positive entry of the matrices in $\{{Q^{(\xi)} \in \mathbf{B}_{\alpha,\beta}}\mid{\xi \in {\lbrack n_{\alpha,\beta}\rbrack}}\}$, denoted by $\gamma = {\gamma{(\alpha,\beta)}} > 0$, where $\gamma > 0$ since $n_{\alpha,\beta}$ is finite. Therefore, by Corollary 3, we have $\frac{1}{m}e^{T}W{(k:t_{0})} \geq \min{(\frac{1}{m},\gamma^{m - 1})}e^{T}$ for all $k > t_{0} \geq 0$. Furthermore, by Eq. we have ${\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack} = {A{(k)}}$ for all $k \geq 1$, implying which follows from $\{{W{(k)}}\}$ being independent. Q.E.D.

Based on the above results, we are ready to prove the main result for deterministic chains.

### Theorem 7

Any balanced and strongly aperiodic chain $\{{A{(k)}}\}$ is in the class $\mathcal{P}^{\ast}$.

### Proof

As pointed out in for any chain $\{{A{(k)}}\}$, there exists a sequence $\{ t_{r}\}$ of time indices, such that for all $k \geq 0$, $\lim_{r\rightarrow\infty}A{(t_{r}:k)} = Q{(k)}$ exists and, for any stochastic vector $\pi \in {\mathbb{R}}^{m}$, the sequence $\{{Q^{T}{(k)}\pi}\}$ is an absolute probability sequence for $\{{A{(k)}}\}$. Since $\{{A{(k)}}\}$ is a balanced and strongly aperiodic chain, by Theorem 6 it follows that with $p^{\ast} = {\min{(\frac{1}{m},\gamma^{m - 1})}} > 0$. Thus, $\{{\frac{1}{m}e^{T}Q{(k)}}\}$ is a uniformly bounded absolute probability sequence for $\{{A{(k)}}\}$. Q.E.D.

The main result of this section follows immediately from Theorem 7.

### Theorem 8

Any balanced and strongly aperiodic independent random chain is in the class $\mathcal{P}^{\ast}$.

### Proof

The proof follows immediately by noticing that, for an independent random chain, $\{{W{(k)}}\}$, any absolute probability sequence for the expected chain $\{{\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack}\}$ is an absolute probability process for $\{{W{(k)}}\}$. Q.E.D.

As a result of Theorem 8 and Theorem 4, the proof of Theorem 1 follows immediately. In particular by Theorem 8, any independent random chain that is balanced and strongly aperiodic belongs to the class $\mathcal{P}^{\ast}$. Thus, the result follows by Theorem 4.

## Connection to Non-negative Matrix Theory

In this section, we show that Theorem 1 is a generalization of the following well-known result in the non-negative matrix theory which plays a central role in the theory of ergodic Markov chains.

### Lemma 6

(, page 46) For an aperiodic and irreducible stochastic matrix $A$, the limit $\lim_{k\rightarrow\infty}A^{k}$ exists and it is equal to a rank one stochastic matrix.

Recall that a stochastic matrix $A$ is irreducible if there is no permutation matrix $P$ such that where $X,Y,Z$ are $i \times i$, $i \times {({m - i})}$, and ${({m - i})} \times {({m - i})}$ matrices for some $i \in {\lbrack{m - 1}\rbrack}$ and $\mathbf{0}$ is the ${({m - i})} \times i$ matrix with all entries equal to zero.

Let us reformulate irreducibility using the tools we have developed in this paper.

### Lemma 7

A stochastic matrix $A$ is an irreducible matrix if and only if the static chain $\{ A\}$ is balanced and its infinite flow graph is connected.

### Proof

By the definition, a matrix $A$ is irreducible if there is no permutation matrix $P$ such that Since $A$ is a non-negative matrix, we have that $A$ is reducible if and only if there exists a subset $S = {\{ 1,\ldots,i\}}$ for some $i \in {\lbrack{m - 1}\rbrack}$, such that where $\sigma_{i} = {\{{j \in {\lbrack m\rbrack}}\mid{{Pe_{i}} = e_{j}}\}}$ (which is a singleton since $P$ is a permutation matrix) and $R = {\{\sigma_{i}\mid{i \in S}\}}$. Thus, $A$ is irreducible if and only if $A_{S\overline{S}} > 0$ for all non-trivial $S \subset {\lbrack m\rbrack}$. Therefore, by letting and noting that $\alpha > 0$, we conclude that $\{ A\}$ is balanced with a balancedness coefficient $\alpha$. Furthermore, since ${A_{S\overline{S}} + A_{\overline{S}S}} \geq A_{S\overline{S}} > 0$ for all nontrivial $S \subset {\lbrack m\rbrack}$, it follows that the infinite flow graph of $\{ A\}$ is connected.

Now, suppose that $\{ A\}$ is balanced and its infinite flow graph of $\{ A\}$ is connected. Then, $A_{S\overline{S}} > 0$ or $A_{\overline{S}S} > 0$ for all non-trivial $S \subset {\lbrack m\rbrack}$. By the balancedness of the chain it follows that ${\min{(A_{S\overline{S}},A_{\overline{S}S})}} > 0$ for any non-trivial $S \subset {\lbrack m\rbrack}$, implying that $A$ is irreducible. Q.E.D.

Note that for an aperiodic $A$, we can always find some $h \geq 1$ such that $A_{ii}^{h} \geq \gamma > 0$ for all $i \in {\lbrack m\rbrack}$. Thus, based on Theorem 1, we have the following extension of Lemma 6 for independent random chains.

### Theorem 9

Let $\{{W{(k)}}\}$ be a balanced and strongly aperiodic independent random chain with a connected infinite flow graph. Then, for any $t_{0} \geq 0$, the product $W{(k:t_{0})}$ converges to a rank one stochastic matrix almost surely (as $k$ goes to infinity). Moreover, if $\{{W{(k)}}\}$ does not have the infinite flow property, the product $W{(k:t_{0})}$ almost surely converges to a (random) matrix that has rank at most $\tau$ for any $t_{0} \geq 0$, where $\tau$ is the number of connected components of the infinite flow graph of $\{{\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack}\}$.

### Proof

The result follows immediately from Theorem 1. Q.E.D.

An immediate consequence of Theorem 9 is a generalization of Lemma 6 to inhomogeneous chains.

### Corollary 4

Let $\{{A{(k)}}\}$ be a balanced and strongly aperiodic stochastic chain. Then, $A{(\infty:t_{0})} = \lim_{k\rightarrow\infty}A{(k:t_{0})}$ exists for all $t_{0} \geq 0$. Moreover, $A{(\infty:t_{0})}$ is a rank one matrix for all $t_{0} \geq 0$ if and only if the infinite flow graph of $\{{A{(k)}}\}$ is connected.

## Conclusion

In this paper we studied the limiting behavior of the products of random stochastic matrices from the dynamic system point of view. We showed that any dynamics driven by such products admits time-varying Lyapunov functions. Then, we defined a class $\mathcal{P}^{\ast}$ of random chains which possess a well-behaved limits. We have introduced balanced chains and discussed how many of the previously well-studied random chains are examples of such chains. We have established a general stability result for product of random stochastic matrices and showed that this result extends a classical convergence result for time-homogeneous irreducible and aperiodic Markov chains.
