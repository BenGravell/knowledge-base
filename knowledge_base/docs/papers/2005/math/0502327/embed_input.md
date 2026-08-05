<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Decoding by Linear Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers the classical error correcting problem which is frequently discussed in coding theory. We wish to recover an input vector f in R^(n) from corrupted measurements y = A f + e. Here, A is an m by n (coding) matrix and e is an arbitrary and unknown vector of errors. Is it possible to recover f exactly from the data y? We prove that under suitable conditions on the coding matrix A, the input f is the unique solution to the l_1-minimization problem (|x|_l_1: = sum_i |x_i|) min_g in R^(n) | y - Ag |_l_1 provided that the support of the vector of errors is not too large, |e|_l_0: = |i: e_i != 0| <= rho* m for some rho > 0. In short, f can be recovered exactly by solving a simple convex optimization problem (which one can recast as a linear program). In addition, numerical experiments suggest that this recovery procedure works unreasonably well; f is recovered exactly even in situations where a significant fraction of the output is corrupted.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Decoding of linear codes", "weight": 1.0} -->

This paper considers the model problem of recovering an input vector $f \in \mathbf{R}^{n}$ from corrupted measurements $y = {{Af} + e}$. Here, $A$ is an $m$ by $n$ matrix (we will assume throughout the paper that $m > n$), and $e$ is an arbitrary and unknown vector of errors. The problem we consider is whether it is possible to recover $f$ exactly from the data $y$. And if so, how?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Decoding of linear codes", "weight": 1.0} -->

In its abstract form, our problem is of course equivalent to the classical error correcting problem which arises in coding theory as we may think of $A$ as a linear code; a linear code is a given collection of codewords which are vectors ${a_{1},\ldots,a_{n}} \in \mathbf{R}^{m}$---the columns of the matrix $A$. Given a vector $f \in \mathbf{R}^{n}$ (the "plaintext") we can then generate a vector $Af$ in $\mathbf{R}^{m}$ (the "ciphertext"); if $A$ has full rank, then one can clearly recover the plaintext $f$ from the ciphertext $Af$. But now we suppose that the ciphertext $Af$ is corrupted by an arbitrary vector $e \in \mathbf{R}^{m}$ giving rise to the corrupted ciphertext ${Af} + e$. The question is then: given the coding matrix $A$ and ${Af} + e$, can one recover $f$ exactly?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Decoding of linear codes", "weight": 1.0} -->

As is well-known, if the fraction of the corrupted entries is too large, then of course we have no hope of reconstructing $f$ from ${Af} + e$; for instance, assume that $m = {2n}$ and consider two distinct plaintexts $f,f'$ and form a vector $g \in \mathbf{R}^{m}$ by setting half of its $m$ coefficients equal to those of $Af$ and half of those equal to those of $Af'$. Then $g = {{Af} + e} = {{Af'} + e'}$ where both $e$ and $e'$ are supported on sets of size at most $n = {m/2}$. This simple example shows that accurate decoding is impossible when the size of the support of the error vector is greater or equal to a half of that of the output $Af$. Therefore, a common assumption in the literature is to assume that only a small fraction of the entries are actually damaged For which values of $\rho$ can we hope to reconstruct $e$ with practical algorithms?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Decoding of linear codes", "weight": 1.0} -->

That is, with algorithms whose complexity is at most polynomial in the length $m$ of the code $A$?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Decoding of linear codes", "weight": 1.0} -->

To reconstruct $f$, note that it is obviously sufficient to reconstruct the vector $e$ since knowledge of ${Af} + e$ together with $e$ gives $Af$, and consequently $f$ since $A$ has full rank. Our approach is then as follows. We construct a matrix which annihilates the $m \times n$ matrix $A$ on the left, i.e. such that ${FA} = 0$. This can be done in an obvious fashion by taking a matrix $F$ whose kernel is the range of $A$ in $\mathbf{R}^{m}$, which is an $n$-dimensional subspace (e.g. $F$ could be the orthogonal projection onto the cokernel of $A$). We then apply $F$ to the output $y = {{Af} + e}$ and obtain since ${FA} = 0$. Therefore, the decoding problem is reduced to that of reconstructing a sparse vector $e$ from the observations $Fe$ (by sparse, we mean that only a fraction of the entries of $e$ are nonzero).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Sparse solutions to underdetermined systems", "weight": 1.0} -->

Finding sparse solutions to underdetermined systems of linear equations is in general $NP$-hard. For example, the sparsest solution is given by and to the best of our knowledge, solving this problem essentially require exhaustive searches over all subsets of columns of $F$, a procedure which clearly is combinatorial in nature and has exponential complexity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Sparse solutions to underdetermined systems", "weight": 1.0} -->

This computational intractability has recently led researchers to develop alternatives to $(P_{0})$, and a frequently discussed approach considers a similar program in the $\ell_{1}$-norm which goes by the name of Basis Pursuit: where we recall that ${\| d\|}_{\ell_{1}} = {\sum_{i = 1}^{m}{|d_{i}|}}$. Unlike the $\ell_{0}$-norm which enumerates the nonzero coordinates, the $\ell_{1}$-norm is convex. It is also well-known that $(P_{1})$ can be recast as a linear program (LP).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sparse solutions to underdetermined systems", "weight": 1.0} -->

Motivated by the problem of finding sparse decompositions of special signals in the field of mathematical signal processing and following upon the ground breaking work of Donoho and Huo, a series of beautiful articles showed exact equivalence between the two programs $(P_{0})$ and $(P_{1})$. In a nutshell, this work shows that for $m/2$ by $m$ matrices $F$ obtained by concatenation of two orthonormal bases, the solution to both $(P_{0})$ and $(P_{1})$ are unique and identical provided that in the most favorable case, the vector $e$ has at most $.914\sqrt{m/2}$ nonzero entries. This is of little practical use here since we are interested in procedures that might recover a signal when a constant fraction of the output is unreliable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sparse solutions to underdetermined systems", "weight": 1.0} -->

Using very different ideas and together with Romberg, the authors proved that the equivalence holds with overwhelming probability for various types of random matrices provided that provided that the number of nonzero entries in the vector $e$ be of the order of $m/{\log m}$. In the special case where $F$ is an $m/2$ by $m$ random matrix with independent standard normal entries, proved that the number of nonzero entries may be as large as $\rho \cdot m$, where $\rho > 0$ is some very small and unspecified positive constant independent of $m$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Innovations", "weight": 1.0} -->

This paper introduces the concept of a restrictedly almost orthonormal system---a collection of vectors which behaves like an almost orthonormal system but only for sparse linear combinations. Thinking about these vectors as the columns of the matrix $F$, we show that this condition allows for the exact reconstruction of sparse linear combination of these vectors, i.e. $e$. Our results are significantly different than those mentioned above as they are deterministic and do not involve any kind of randomization, although they can of course be specialized to random matrices. For instance, we shall see that a Gaussian matrix with independent entries sampled from the standard normal distribution is restrictedly almost orthonormal with overwhelming probability, and that minimizing the $\ell_{1}$-norm recovers sparse decompositions with a number of nonzero entries of size $\rho_{0} \cdot m$; we shall actually give numerical values for $\rho_{0}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Innovations", "weight": 1.0} -->

We presented the connection with sparse solutions to underdetermined systems of linear equations merely for pedagogical reasons. There is a more direct approach. To recover $f$ from corrupted data $y = {{Af} + e}$, we consider solving the following $\ell_{1}$-minimization problem Now $f$ is the unique solution of $(P_{1}')$ if and only if $e$ is the unique solution of $(P_{1})$. In other words, $(P_{1})$ and $(P_{1}')$ are equivalent programs. To see why these is true, observe on the one hand that since $y = {{Af} + e}$, we may decompose $g$ as $g = {f + h}$ so that On the other hand, the constraint ${Fx} = {Fe}$ means that $x = {e - {Ah}}$ for some $h \in \mathbf{R}^{n}$ and, therefore, which proves the claim.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Innovations", "weight": 1.0} -->

The program $(P_{1}')$ may also be re-expressed as an LP---hence the title of this paper. Indeed, the $\ell_{1}$-minimization problem is equivalent to where the optimization variables are $t \in R^{m}$ and $g \in \mathbf{R}^{n}$ (as is standard, the generalized vector inequality $x \leq y$ means that $x_{i} \leq y_{i}$ for all $i$). As a result, $(P_{1}')$ is an LP with inequality constraints and can be solved efficiently using standard optimization algorithms, see.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Restricted isometries", "weight": 1.0} -->

In the remainder of this paper, it will be convenient to use some linear algebra notations. We denote by ${(v_{j})}_{j \in J} \in R^{p}$ the columns of the matrix $F$ and by $H$ the Hilbert space spanned by these vectors. Further, for any $T \subseteq J$, we let $F_{T}$ be the submatrix with column indices $j \in T$ so that To introduce the notion of almost orthonormal system, we first observe that if the columns of $F$ are sufficiently "degenerate," the recovery problem cannot be solved. In particular, if there exists a non-trivial sparse linear combination ${\sum_{j \in T}{c_{j}v_{j}}} = 0$ of the $v_{j}$ which sums to zero, and $T = {T_{1} \cup T_{2}}$ is any partition of $T$ into two disjoint sets, then the vector $y$ has two distinct sparse representations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Restricted isometries", "weight": 1.0} -->

On the other hand, linear dependencies ${\sum_{j \in J}{c_{j}v_{j}}} = 0$ which involve a large number of nonzero coefficients $c_{j}$, as opposed to a sparse set of coefficients, do not present an obvious obstruction to sparse recovery. At the other extreme, if the ${(v_{j})}_{j \in J}$ are an orthonormal system, then the recovery problem is easily solved by setting $c_{j} = {\langle f,v_{j}\rangle}_{H}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Restricted isometries", "weight": 1.0} -->

The main result of this paper is that if we impose a "restricted orthonormality hypothesis," which is far weaker than assuming orthonormality, then $(P_{1})$ solves the recovery problem, even if the ${(v_{j})}_{j \in J}$ are highly linearly dependent (for instance, it is possible for $m:={|J|}$ to be much larger than the dimension of the span of the $v_{j}$'s). To make this quantitative we introduce the following definition.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main results", "weight": 1.0} -->

Note that the previous lemma is an abstract existence argument which shows what might theoretically be possible, but does not supply any efficient algorithm to recover $T$ and $c_{j}$ from $f$ and ${(v_{j})}_{j \in J}$ other than by brute force search---as discussed earlier. In contrast, our main theorem result that, by imposing slightly stronger conditions on $\delta_{2S}$, the $\ell_{1}$-minimization program $(P_{1})$ recovers $f$ exactly.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gaussian random matrices", "weight": 1.0} -->

An important question is then to find matrices with good restricted isometry constants, i.e. such that (1.10) holds for large values of $S$. Indeed, such matrices will tolerate a larger fraction of output in error while still allowing exact recovery of the original input by linear programming. How to construct such matrices might be delicate. In section 3, however, we will argue that generic matrices, namely samples from the Gaussian unitary ensemble obey $$ for relatively large values of $S$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Organization of the paper", "weight": 1.0} -->

The paper is organized as follows. Section 2 proves our main claim, namely, Theorem 1.4 (and hence Theorem 1.5) while Section 3 introduces elements from random matrix theory to establish Theorem 1.6. In Section 4, we present numerical experiments which suggest that in practice, $(P_{1}')$ works unreasonably well and recovers the $f$ exactly from $y = {{Af} + e}$ provided that the fraction of the corrupted entries be less than about 17% in the case where $m = {2n}$ and less than about 34% in the case where $m = {4n}$. Section 5 explores the consequences of our results for the recovery of signals from highly incomplete data and ties our findings with some of our earlier work. Finally, we conclude with a short discussion section whose main purpose is to outline areas for improvement.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Exact reconstruction property", "weight": 1.0} -->

We now examine the sparse reconstruction property and begin with coefficients ${\langle w,v_{j}\rangle}_{H}$ for $j \notin T$ being only small in an $\ell_{2}$ sense.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Approximate orthogonality", "weight": 1.0} -->

Lemma 1.2 gives control of the size of the principal angle between subspaces of dimension $S$ and $S'$ respectively. This is useful because it allows to guarantee exact reconstruction from the knowledge of the $\delta$ numbers only.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Approximate orthogonality", "weight": 1.0} -->

Proof \Proof of Lemma [1.2\] We first show that $\theta_{S,S'} \leq \delta_{S + S'}$. By homogeneity it will suffice to show that whenever ${|T|} \leq S$, ${|T'|} \leq S'$, $T,T'$ are disjoint, and ${\sum_{j \in T}{|c_{j}|}^{2}} = {\sum_{j' \in T'}{|c_{j'}'|}^{2}} = 1$. Now (1.7 ‣ 1.4 Restricted isometries ‣ 1 Introduction ‣ Decoding by Linear Programming")) gives and the claim now follows from the parallelogram identity It remains to show that $\delta_{S + S'} \leq {\theta_{S} + \delta_{S}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Approximate orthogonality", "weight": 1.0} -->

(1.7 ‣ 1.4 Restricted isometries ‣ 1 Introduction ‣ Decoding by Linear Programming")) together with (1.8 ‣ 1.4 Restricted isometries ‣ 1 Introduction ‣ Decoding by Linear Programming")) give as claimed. (We note that it is possible to optimize this bound a little further but will not do so here.)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Gaussian Random Matrices", "weight": 1.0} -->

In this section, we argue that with overwhelming probability, Gaussian random matrices have "good" isometry constants. Consider a $p$ by $m$ matrix $F$ whose entries are i.i.d. Gaussian with mean zero and variance $1/p$ and let $T$ be a subset of the columns. We wish to study the extremal eigenvalues of $F_{T}^{\ast}F_{T}$. Following upon the work of Marchenko and Pastur, Geman and Silverstein (see also) proved that in the limit where $p$ and ${|T|}\rightarrow\infty$ with In other words, this says that loosely speaking and in the limit of large $p$, the restricted isometry constant $\delta{(F_{T})}$ for a fixed $T$ behaves like Restricted isometry constants must hold for all sets $T$ of cardinality less or equal to $S$, and we shall make use of concentration inequalities to develop such a uniform bound.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Gaussian Random Matrices", "weight": 1.0} -->

Note that for $T' \subset T$, we obviously have and, therefore, attention may be restricted to matrices of size $S$. Now, there are large deviation results about the singular values of $F_{T}$. For example, letting $\sigma_{\max}{(F_{T})}$ (resp. $\sigma_{\min}$) be the largest singular value of $F_{T}$ so that ${\sigma_{\max}^{2}{(F_{T})}} = {\lambda_{\max}{({F_{T}^{\ast}F_{T}})}}$ (resp.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Gaussian Random Matrices", "weight": 1.0} -->

${\sigma_{\min}^{2}{(F_{T})}} = {\lambda_{\min}{({F_{T}^{\ast}F_{T}})}}$), Ledoux applies the concentration inequality for Gaussian measures, and for a each fixed $t > 0$, obtains the deviation bounds here, $o{}$ is a small term tending to zero as $p\rightarrow\infty$ and which can be calculated explicitly, see. For example, this last reference shows that one can select $o{}$ in (3.1) as ${\frac{1}{2p^{1/3}} \cdot \gamma^{1/6}}{({1 + \sqrt{\gamma}})}^{2/3}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

This section investigates the practical ability of $\ell_{1}$ to recover an object $f \in \mathbf{R}^{n}$ from corrupted data $y = {{Af} + e}$, $y \in \mathbf{R}^{m}$ (or equivalently to recover the sparse vector of errors $e \in \mathbf{R}^{m}$ from the underdetermined system of equations ${Fe} = z \in \mathbf{R}^{m - n}$). The goal here is to evaluate empirically the location of the breakpoint as to get an accurate sense of the performance one might expect in practice.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In order to do this, we performed a series of experiments designed as follows: select $n$ (the size of the input signal) and $m$ so that with the same notations as before, $A$ is an $n$ by $m$ matrix; sample $A$ with independent Gaussian entries; select a support set $T$ of size ${|T|} = S$ uniformly at random, and sample a vector $e$ on $T$ with independent and identically distributed Gaussian entries^11^1Just as, the results presented here do not seem to depend on the actual distribution used to sample the errors.; make $\overset{\sim}{y} = {{Ax} + e}$ (the choice of $x$ does not matter as is clear from the discussion and here, $x$ is also selected at random), solve $(P_{1}')$ and obtain $x^{\ast}$; repeat $100$ times for each $S$ and $A$; repeat for various sizes of $n$ and $m$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The results are presented in Figure 2 and Figure 3. Figure 2 examines the situation in which the length of the code is twice that of the input vector $m = {2n}$, for $m = 512$ and $m = 1024$. Our experiments show that one recovers the input vector all the time as long as the fraction of the corrupted entries is below 17%. This holds for $m = 512$ (Figure 2(a)) and $m = 1024$ (Figure 2(b)). In Figure 3, we investigate how these results change as the length of the codewords increases compared to the length of the input, and examine the situation in which $m = {4n}$, with $m = 512$. Our experiments show that one recovers the input vector all the time as long as the fraction of the corrupted entries is below 34%.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimal Signal Recovery", "weight": 1.0} -->

Our recent work developed a set of ideas showing that it is surprisingly possible to reconstruct interesting classes of signals accurately from highly incomplete measurements. The results in this paper are inspired and improve upon this earlier work and we now elaborate on this connection. Suppose we wish to reconstruct an object $\alpha$ in $\mathbf{R}^{m}$ from the $K$ linear measurements with $\phi_{k}$, the $k$th row of the matrix $F$. Of special interest is the vastly underdetermined case, $K\operatorname{<<}N$, where there are many more unknowns than observations. We choose to formulate the problem abstractly but for concreteness, we might think of $\alpha$ as the coefficients $\alpha = {\Psi^{\ast}f}$ of a digital signal or image $f$ in some nice orthobasis, e.g. a wavelet basis so that the information about the signal is of the form $y = {F\alpha} = {F\Psi^{\ast}f}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimal Signal Recovery", "weight": 1.0} -->

Suppose now that the object of interest is compressible in the sense that the reordered entries of $\alpha$ decay like a power-law; concretely, suppose that the entries of $\alpha$, rearranged in decreasing order of magnitude, ${|\alpha|}_{} \geq {|\alpha|}_{} \geq \cdots \geq {|\alpha|}_{(m)}$, obey for some $s \geq 1$. We will denote by $\mathcal{F}_{s}{(B)}$ the class of all signals $\alpha \in \mathbf{R}^{m}$ obeying (5.2). The claim is that it is possible to reconstruct compressible signals from only a small number of random measurements.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

In our linear programming model, the plaintext and ciphertext had real-valued components. Another intensively studied model occurs when the plaintext and ciphertext take values in the finite field $F_{2}:={\{ 0,1\}}$. In recent work of Feldman et al. linear programming methods (based on relaxing the space of codewords to a convex polytope) were developed to establish a polynomial-time decoder which can correct a constant fraction of errors, and also achieve the information-theoretic capacity of the code. There is thus some intriguing parallels between those works and the results in this paper, however there appears to be no direct overlap as our methods are restricted to real-valued texts, and the work cited above requires texts in $F_{2}$. Also, our error analysis is deterministic and is thus guaranteed to correct arbitrary errors provided that they are sufficiently sparse.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Connections with other works", "weight": 1.0} -->

The ideas presented in this paper may be adapted to recover input vectors taking values from a finite alphabet. We hope to report on work in progress in a follow-up paper.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Improvements", "weight": 1.0} -->

There is little doubt that more elaborate arguments will yield versions of Theorem 1.6 with tighter bounds. Immediately following the proof of Lemma 2.2 ‣ 2.1 Exact reconstruction property ‣ 2 Proof of Main Results ‣ Decoding by Linear Programming"), we already remarked that one might slightly improve the condition ${\delta_{S} + \theta_{S,S} + \theta_{S,{2S}}} < 1$ at the expense of considerable complications. More to the point, we must admit that we used well-established tools from Random Matrix Theory and it is likely that more sophisticated ideas might be deployed successfully. We now discuss some of these.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Improvements", "weight": 1.0} -->

Our main hypothesis reads ${\delta_{S} + \theta_{S,S} + \theta_{S,{2S}}} < 1$ but in order to reduce the problem to the study of those $\delta$ numbers (and use known results), our analysis actually relied upon the more stringent condition ${\delta_{S} + \delta_{2S} + \delta_{3S}} < 1$ instead, since This introduces a gap. Consider a fixed set $T$ of size ${|T|} = S$. Using the notations of that Section 3, we argued that and developed a large deviation bound to quantify the departure from the right hand-side.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Improvements", "weight": 1.0} -->

Now let $T$ and $T'$ be two disjoint sets of respective sizes $S$ and $S'$ and consider $\theta{(F_{T},F_{T'})}$: $\theta{(F_{T},F_{T'})}$ is the cosine of the principal angle between the two random subspaces spanned by the columns of $F_{T}$ and $F_{T'}$ respectively; formally We remark that this quantity plays an important analysis in statistical analysis because of its use to test the significance of correlations between two sets of measurements, compare the literature on Canonical Correlation Analysis. Among other things, it is known that as $p\rightarrow\infty$ with ${S/p}\rightarrow\gamma$ and ${S'/p}\rightarrow\gamma'$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Improvements", "weight": 1.0} -->

In other words, whereas we used the limiting behaviors there is a chance one might employ instead for ${|T|} = {|T'|} = S$ and ${|T'|} = {2{|T|}} = {2S}$ respectively, which is better. Just as in Section 3, one might then look for concentration inequalities transforming this limiting behavior into corresponding large deviation inequalities. We are aware of very recent work of Johnstone and his colleagues which might be here of substantial help.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improvements", "weight": 1.0} -->

Finally, tighter large deviation bounds might exist together with more clever strategies to derive uniform bounds (valid for all $T$ of size less than $S$) from individual bounds (valid for a single $T$). With this in mind, it is interesting to note that our approach hits a limit as where ${J{(r)}}:={{2\sqrt{r}} + r + {{({2 + \sqrt{2}})}\sqrt{r{({1 - r})}}} + \sqrt{r{({1 - {2r}})}}}$. Since $J{(r)}$ is greater than 1 if and only if $r > 2.36$, one would certainly need new ideas to improve Theorem 1.6 beyond cut-off point in the range of about 2%. The lower limit (6.1) is probably not sharp since it does not explicitly take into account the ratio between $m$ and $p$; at best, it might serve as an indication of the limiting behavior when the ration $p/m$ is not too small.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Other coding matrices", "weight": 1.0} -->

This paper introduced general results stating that it is possible to correct for errors by $\ell_{1}$-minimization. We then explained how the results specialize in the case where the coding matrix $A$ is sampled from the Gaussian ensemble. It is clear, however, that one could use other matrices and still obtain similar results; namely, that $(P_{1}')$ recovers $f$ exactly provided that the number of corrupted entries does not exceed $\rho \cdot m$. In fact, our previous work suggests that partial Fourier matrices would enjoy similar properties. Other candidates might be the so-called noiselets of Coifman, Geshwind and Meyer. These alternative might be of great practical interest because they would come with fast algorithms for applying $A$ or $A^{\ast}$ to an arbitrary vector $g$ and, hence, speed up the computations to find the $\ell_{1}$-minimizer.
