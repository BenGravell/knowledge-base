<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Product of Random Stochastic Matrices

Topics include Stochastic matrices, Random matrix products, Consensus algorithms, Lyapunov functions, Distributed averaging, Ergodicity, Control theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies convergence of products of random row-stochastic matrices through a dynamical-systems lens. The paper introduces balanced chains and related Lyapunov arguments to generalize classical Perron-Frobenius convergence behavior to random, time-varying stochastic matrix sequences relevant to consensus and distributed computation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The paper deals with the convergence properties of the products of random (row-)stochastic matrices. The limiting behavior of such products is studied from a dynamical system point of view. In particular, by appropriately defining a dynamic associated with a given sequence of random (row-)stochastic matrices, we prove that the dynamics admits a class of time-varying Lyapunov functions, including a quadratic one. Then, we discuss a special class of stochastic matrices, a class P-star, which plays a central role in this work. We then introduce balanced chains and using some geometric properties of these chains, we characterize the stability of a subclass of balanced chains. As a special consequence of this stability result, we obtain an extension of a central result in the non-negative matrix theory stating that, for any aperiodic and irreducible row-stochastic matrix A, the limit lim k to infinity A^(k) exists and it is a rank one stochastic matrix. We show that a generalization of this result holds not only for sequences of stochastic matrices but also for independent random sequences of such matrices.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Averaging dynamics or distributed averaging dynamics has played a fundamental role in the recent studies of various distributed systems and algorithms. Examples of such distributed problems and algorithms include distributed optimization, distributed control of robotic networks, and study of opinion dynamics in social networks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The study of averaging dynamics is closely related to the study of products of stochastic matrices. Such products have been studied from two perspectives: the theory of Markov chains and the distributed averaging settings. The notable works in the domain of the theory of Markov chain are the early studies of Hajnal and Wolfowitz in and, respectively, where sufficient conditions are derived for the convergence of the products of row-stochastic matrices to a rank one matrix. The exploration of this domain from the distributed averaging perspective was started by the work of and the seminal work of J. Tsitsiklis.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Products of random stochastic matrices have also attracted many mathematicians as such products are examples of convolutions of probability measures on semigroups. Due to the technicalities involved, such studies are confined to identically independently distributed (i.i.d.) random chains or their generalizations in the domain of stationary ergodic chains. From the engineering perspective, this area have been recently explored. In, a necessary and sufficient condition for ergodicity of products of i.i.d. stochastic matrices has been derived. A generalization of such result for stationary and ergodic chains is discussed. In a sequence of papers we have defined fundamental concepts of infinite flow property, infinite flow graph, and $\ell_{1}$-approximation. We have showed that these properties are very closely related to the convergence properties of the product of random stochastic matrices that are not necessarily identically distributed. The current work is a continuation of the line of the aforementioned papers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, in this paper, we derive a set of necessary and sufficient conditions for ergodicity and convergence of a product of independent random stochastic matrices. Specifically, we study a class of random stochastic matrices, which we refer to as balanced chains and show that this class contains many of the previously studied chains of random and deterministic stochastic matrices. This property was first introduced in our earlier work for discrete-time dynamics and in for continuous-time dynamics. Much research has been done on such a criterion since then (see e.g. ). Unlike the prior work, our work adopts dynamical system point of view for the averaging dynamics: we first draw the connection between the products of random stochastic matrices and the random dynamics driven by such matrices. Then, we show that every dynamics driven by a chain of independent random stochastic matrices admits a time-varying quadratic Lyapunov function. In fact, we show more by establishing that for any convex function, there exists a Lyapunov function adjusted to such a convex function.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This result opens up a new window for the study of averaging dynamics and distributed algorithms, as quadratic Lyapunov function has proven to be a powerful tool to study such dynamics for different sub-classes of stochastic chains (see e.g., and ). However, the non-existence of quadratic time-invariant Lyapunov functions was suspected for general class of averaging dynamics, and it was proven later.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

After proving the existence of time-varying quadratic Lyapunov functions for averaging dynamics, we introduce a special class of stochastic chains, $\mathcal{P}^{\ast}$ chains, and we show that the products of matrices drawn from this sub-class converge almost surely. We then provide the definition of balanced-ness for random stochastic chains and we show that many previously studied classes of stochastic chains are examples of such balanced chains. Finally, using a geometric property of the balanced chains, we show that such chains are examples of $\mathcal{P}^{\ast}$ chains, which leads to the main result of this paper which can be interpreted as a generalization of the known convergence of $A^{k}$ to a rank-one stochastic matrix (for aperiodic and irreducible stochastic matrix $A$) to the case of inhomogeneous chains of stochastic matrices, as well as independent random chains of such matrices.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contribution of this work is as follows: 1) we prove the existence of a family of time-varying Lyapunov functions for random averaging dynamics; 2) we introduce class $\mathcal{P}^{\ast}$ of random stochastic chains, and provide necessary and sufficient conditions for the stability of the corresponding dynamics; 3) we introduce balanced chains and we use them to establish some necessary and sufficient conditions for the stability of the resulting dynamics; and 4) we provide an extension of the fundamental convergence result in the non-negative matrix theory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows: in Section 2, we formulate and provide the random setting for our study of the products of random stochastic matrices which will be considered throughout the paper. In Section 3, we study the dynamics related to such matrices and draw the connection between the study of such products and the associated dynamics, and we prove that the dynamics admits a class of time-varying Lyapunov functions, including a quadratic one. Then, we discuss the class $\mathcal{P}^{\ast}$ in Section 4 which plays a central role in our development. We then introduce the class of balanced chains and using the geometric structure of these chains, as well as the developed results in the preceding sections, we characterize the stability of a subclass of those chains. Finally, in Section 6, we apply the developed results to prove an extension of a central result in the non-negative matrix theory on the convergence of $A^{k}$ to a rank-one matrix. We conclude this work by a discussion in Section 7.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We work exclusively with row-stochastic matrices, so we simply refer to them as stochastic matrices. Let $(\Omega,\mathcal{F},\Pr)$ be a probability space and let $\{{W{(k)}}\}$ be a chain of $m \times m$ random stochastic matrices, i.e. for all $k \geq 1$, the matrix $W{(k)}$ is a stochastic almost surely and ${W_{ij}{(k)}}:{\Omega\rightarrow{\mathbb{R}}}$ is a Borel-measurable function for all ${i,j} \in {\lbrack m\rbrack}$, where ${\lbrack m\rbrack} = {\{ 1,\ldots,m\}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Throughout this paper, we denote random sequences of stochastic matrices by last alphabet letters such as $\{{W{(k)}}\}$ and $\{{U{(k)}}\}$, and we use the first alphabet letters such as $\{{A{(k)}}\}$ and $\{{B{(k)}}\}$ to denote deterministic sequences of stochastic matrices. We also refer to a sequence of stochastic matrices as a stochastic chain, or just simply as a chain.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Let $\{{W{(k)}}\}$ be an independent random chain. Then, we say that $\{{W{(k)}}\}$ is strongly aperiodic if there exists a $\gamma \in {(0,1\rbrack}$ such that

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Note that if ${W_{ii}{(k)}} \geq \gamma$ almost surely for all $i \in {\lbrack m\rbrack}$ and all $k \geq 1$, then such a chain is strongly aperiodic. Also, note that by summing both sides of the above inequality over $j \neq i$, we obtain

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

For the subsequent use, for an $m \times m$ random (or deterministic) matrix $W$ and a non-trivial index set $S \subset {\lbrack m\rbrack}$ (i.e. $S \neq \varnothing$ and $S \neq {\lbrack m\rbrack}$), we define the quantity $W_{S\overline{S}} = {\sum_{{i \in S},{j \in \overline{S}}}W_{ij}}$, where $\overline{S}$ is the complement of the index set $S$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We say that an independent random chain $\{{W{(k)}}\}$ is balanced if there exists some $\alpha > 0$ such that

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

From this definition, it can be seen that $\alpha \leq 1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Finally, with a given random chain $\{{W{(k)}}\}$, let us associate a random graph $G^{\infty} = {({\lbrack m\rbrack},\mathcal{E}^{\infty})}$ with the vertex set $\lbrack m\rbrack$ and the edge set $\mathcal{E}^{\infty}$ given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We refer to $G^{\infty}$ as the infinite flow graph of $\{{W{(k)}}\}$. By the Kolmogorov's 0-1 law, the infinite flow graph of an independent random chain $\{{W{(k)}}\}$ is almost surely equal to a deterministic graph. It has been shown that this determinstic graph is equal to the infinite flow graph of the expected chain $\{{\mathsf{E}\left\lbrack {W{(k)}} \right\rbrack}\}$ (, Theorem 5).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

For a matrix $W$, let $W_{i}$ and $W^{j}$ denote the $i$th row vector and the $j$th column vector of $W$, respectively. Also, for a chain $\{{W{(k)}}\}$, we let

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

with $W{(k:k)} = I$ for all $k \geq 0$. With these preliminary definitions and notation in place, we can state the main result of the current study.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dynamic System Perspective", "weight": 1.0} -->

In order to prove Theorem 1, we establish some intermediate results, some of which are applicable to a more general category of random stochastic chains, namely adapted random chains. For this, let $\{{W{(k)}}\}$ be a random chain adapted to a filtration $\{\mathcal{F}_{k}\}$. For an integer $t_{0} \geq 0$ and a vector $v \in {\mathbb{R}}^{m}$, consider the trivial random vector ${x{(t_{0})}}:{\Omega\rightarrow{\mathbb{R}}^{m}}$ defined by ${x{(t_{0},\omega)}} = v$ for all $\omega \in \Omega$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dynamic System Perspective", "weight": 1.0} -->

In order to study the limiting behavior of the products $W{(k:t_{0})}$, we study the limiting behavior of the dynamics $\{{x{(k)}}\}$ driven by $\{{W{(k)}}\}$. This enables us to use the dynamic system's tools and its stability theory to draw conclusions about the limiting behavior of the products $W{(k:t_{0})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Why the Infinite Flow Graph", "weight": 1.0} -->

In this section we provide a result showing the relevance of the infinite flow graph to the study of the product of stochastic matrices. Let us consider a deterministic chain $\{{A{(k)}}\}$ of stochastic matrices and let us define mutual ergodicity and an ergodic index as follows.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Time-varying Lyapunov Functions", "weight": 1.0} -->

Here, we show that under general conditions, a rich family of time-varying Lyapunov functions exists for the dynamics $\{{x{(k)}}\}$ driven by a random chain $\{{W{(k)}}\}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Time-varying Lyapunov Functions", "weight": 1.0} -->

Let us define an absolute probability process for an adapted chain $\{{W{(k)}}\}$, which is an extension of the concept of the absolute probability sequence introduced by A. Kolmogorov for deterministic chains.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Time-varying Quadratic Lyapunov Function", "weight": 1.0} -->

In the sequel, we focus on the particular choice of function ${g{(s)}} = s^{2}$ in relation. For convenience, we let

<!-- chunk {"id": "body-0029", "role": "body", "section": "Time-varying Quadratic Lyapunov Function", "weight": 1.0} -->

For this function, we can provide a lower bound for the decrease of the conditional expectations $\mathsf{E}\left\lbrack {{V_{g}{({x{({k + 1})}},{k + 1})}} \mid \mathcal{F}_{k}} \right\rbrack$, which is exact under certain conditions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Class $\\mathcal{P}^{\\ast}$", "weight": 1.0} -->

In this section, we introduce a class of random chains, which we refer to as the class $\mathcal{P}^{\ast}$, and we prove one of the central results of this work. In particular, we show that the claim of Theorem 1 holds for any chain that is in the class $\mathcal{P}^{\ast}$ and satisfies some form of aperiodicity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Balanced Chains", "weight": 1.0} -->

In this section, we characterize a subclass of $\mathcal{P}^{\ast}$ chains, namely the class of strongly aperiodic balanced chains. We first show that this class includes many of the chains that have been studied in the existing literature. Then, we prove that any aperiodic balanced chain belongs to the class $\mathcal{P}^{\ast}$. We also show that a balanced independent random chain is strongly aperiodic, thus concluding Theorem 1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Balanced Chains", "weight": 1.0} -->

Balanced Bidirectional Chains: We say that an independent chain $\{{W{(k)}}\}$ is a balanced bidirectional chain if there exists some $\alpha > 0$ such that ${\mathsf{E}\left\lbrack {W_{ij}{(k)}} \right\rbrack} \geq {\alpha\mathsf{E}\left\lbrack {W_{ji}{(k)}} \right\rbrack}$ for all $k \geq 1$ and ${i,j} \in {\lbrack m\rbrack}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Balanced Chains", "weight": 1.0} -->

Examples of such chains are bounded bidirectional deterministic chains, which are the chains such that ${A_{ij}{(k)}} > 0$ implies ${A_{ji}{(k)}} > 0$ for all $i.{j \in {\lbrack m\rbrack}}$ and all $k \geq 1$, and the positive entries are uniformly bounded from below by some $\gamma > 0$ (i.e., ${A_{ij}{(k)}} > 0$ implies ${A_{ij}{(k)}} \geq \gamma$ for all ${i,j} \in {\lbrack m\rbrack}$ and all $k \geq 1$).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Balanced Chains", "weight": 1.0} -->

In this case, for ${A_{ij}{(k)}} > 0$, we have ${A_{ij}{(k)}} \geq \gamma \geq {\gammaA_{ji}{(k)}}$ and for ${A_{ij}{(k)}} = 0$, we have ${A_{ji}{(k)}} = 0$ and, hence, in either of the cases ${A_{ij}{(k)}} \geq {\gammaA_{ji}{(k)}}$. Therefore, bounded bidirectional chains are examples of balanced bidirectional chains. Such chains have been considered in and, among others, include the Hegselman-Krause model for opinion dynamics.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Balanced Chains", "weight": 1.0} -->

Chains with Common Steady State $\pi > 0$: This ensemble consists of independent random chains $\{{W{(k)}}\}$ such that ${\mathsf{E}\left\lbrack {\pi^{T}W{(k)}} \right\rbrack} = {\mathsf{E}\left\lbrack {\pi^{T}{(k)}} \right\rbrack}$ for some stochastic vector $\pi > 0$ and all $k \geq 1$, which are generalizations of doubly stochastic chains, where we have $\pi = {\frac{1}{m}e}$ ($e$ is a vector of ones). Doubly stochastic chains and the chains with a common steady state $\pi > 0$ have been studied.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Balanced Chains", "weight": 1.0} -->

To show that a chain with a common steady state $\pi > 0$ is a balanced chain, let us prove the following lemma.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Absolute Probability Sequence for Balanced Chains", "weight": 1.0} -->

In this section, we show that any independent random chain that is strongly aperiodic and balanced must be in the class $\mathcal{P}^{\ast}$. The road map to prove this result is as follows: we first show that this result holds for deterministic chains with uniformly bounded positive entries. Then, using this result and geometric properties of the set of strongly aperiodic balanced chains, we prove the statement for deterministic chains, which immediately implies the result for independent random chains. To show the result for deterministic chains with uniformly bounded positive entries, we employ the technique that is used to prove Proposition 4. However, the argument given in needs some extensions to fit in our more general assumption of balanced-ness.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Absolute Probability Sequence for Balanced Chains", "weight": 1.0} -->

Let $\{{A{(k)}}\}$ be a deterministic chain of stochastic matrices. Let $S_{j}{(k)}$ be the set of indices corresponding to the positive entries in the $j$th column of $A{(k:0)}$, i.e.,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Absolute Probability Sequence for Balanced Chains", "weight": 1.0} -->

Also, let $\mu_{j}{(k)}$ be the minimum value of these positive entries, i.e.,

<!-- chunk {"id": "body-0040", "role": "body", "section": "Connection to Non-negative Matrix Theory", "weight": 1.0} -->

In this section, we show that Theorem 1 is a generalization of the following well-known result in the non-negative matrix theory which plays a central role in the theory of ergodic Markov chains.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we studied the limiting behavior of the products of random stochastic matrices from the dynamic system point of view. We showed that any dynamics driven by such products admits time-varying Lyapunov functions. Then, we defined a class $\mathcal{P}^{\ast}$ of random chains which possess a well-behaved limits. We have introduced balanced chains and discussed how many of the previously well-studied random chains are examples of such chains. We have established a general stability result for product of random stochastic matrices and showed that this result extends a classical convergence result for time-homogeneous irreducible and aperiodic Markov chains.
