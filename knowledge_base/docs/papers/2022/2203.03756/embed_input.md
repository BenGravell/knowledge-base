<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Flat Minima Generalize for Low-rank Matrix Recovery

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Empirical evidence suggests that for a variety of overparameterized nonlinear models, most notably in neural network training, the growth of the loss around a minimizer strongly impacts its performance. Flat minima - those around which the loss grows slowly - appear to generalize well. This work takes a step towards understanding this phenomenon by focusing on the simplest class of overparameterized nonlinear models: those arising in low-rank matrix recovery. We analyze overparameterized matrix and bilinear sensing, robust PCA, covariance matrix estimation, and single hidden layer neural networks with quadratic activation functions. In all cases, we show that flat minima, measured by the trace of the Hessian, exactly recover the ground truth under standard statistical assumptions. For matrix completion, we establish weak recovery, although empirical evidence suggests exact recovery holds here as well. We conclude with synthetic experiments that illustrate our findings and discuss the effect of depth on flat solutions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in machine learning and artificial intelligence have relied on fitting highly overparameterized models, notably deep neural networks, to observed data tan2019efficientnet; kolesnikov2020big; huang2019gpipe; zhang2021understanding. In such settings, the number of parameters of the model is much greater than the number of data samples, thereby resulting in models that achieve near-zero training error. Although classical learning paradigms caution against overfitting, recent work suggests ubiquity of the "double descent" phenomenon belkin2019reconciling, wherein significant overparameterization actually improves generalization. There is an important caveat, however, that is worth emphasizing. There is typically a continuum of models with zero training error; some of these models generalize well and some do not.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reassuringly, there is evidence that basic algorithms, such as the stochastic gradient method, are implicitly biased towards finding models that do generalize; see for example soudry2018implicit; gunasekar2018implicitNN; jacot2018neural; heckel2020compressive; jastrzkebski2017three; smith2017bayesian; hoffer2017train; masters2018revisiting; neyshabur2014search; gunasekar2018implicit; du2018algorithmic; mulayoff2020unique. Other seminal works bartlett1998sample; bartlett2002rademacher; neyshabur2017exploring seeking to explain generalization have focused on quantifying stability, capacity, and margin bounds. Understanding generalization of overparameterized models remains an active area of research, and is the topic of our work.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing literature highlights two intriguing properties---small norm and flat landscape---that correlate with generalization neyshabur2017exploring; dziugaite2017computing; dinh2017sharp. Indeed, it has long been known that the magnitude of the weights plays an important role for neural network training. As a result, one typically incorporates a squared $\ell_{2}$-penalty on the weights---called weight decay---when applying iterative methods. One intuitive explanation is that minimizing the square Frobenius norm of the factors in matrix factorization problems is equivalent to minimizing the nuclear norm---a well-known regularizer for inducing low-rank structure recht2010guaranteed. Far reaching generalizations of this phenomenon for various neural network architectures have been recently pursued in savarese2019infinite; ongie2019function; ongie2022role.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In parallel, empirical evidence hochreiter1997flat; Keskar2016; li2017visualizing strongly suggests that those models around which the landscape is flat---meaning the training loss grows slowly---generalize well. See Figure 1 for an illustration of flat and sharp minima. Inspired by this observation, a variety of algorithms have been proposed to explicitly bias the iterates towards flat solutions chaudhari2019entropy; izmailov2018averaging; norton2021diametrical; foret2020sharpness, with impressive observed performance. In contrast to the magnitude of the weights, the theoretic basis for flatness is much less clear even for simple overparameterized nonlinear problems. The goal of our work is to answer the following question: > Do flat minimizers generalize for a broad family of overparameterized problems?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Putting generalization aside, one would hope that flat solutions are in some sense regular, occurring in a benign region where algorithms perform well. For example, numerical methods for neural network training are strongly influenced by how balanced the parameters appear. Namely, the set of interpolating neural networks contains models with consecutive weight matrices that are poorly scaled relative to each other du2018algorithmic; shamir2018resnets. It has recently been shown that gradient descent in continuous time keeps the factors balanced ye2021global; ma2021beyond for matrix factorization and for deep learning du2018algorithmic; mulayoff2020unique. Despite ubiquity of the three notions discussed so far---small norm, flatness, and balancedness---the exact relationship between them is unclear. Thus our secondary question is as follow: Are flat minimizers nearly norm-minimal and nearly balanced\for a broad family of overparameterized problems?

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

We answer both questions in the setting of low-rank matrix factorization---a prototypical problem class often used to gain insight into more general deep learning models li2018algorithmic; du2018algorithmic; ye2021global. Setting the stage, consider a ground truth matrix $M_{\natural} \in^{d_{1} \times d_{2}}$ with rank $r_{\natural}$. The goal is to recover $M_{\natural}$ from the observed measurements $b = {\mathcal{A}{(M_{\natural})}}$ under a linear measurement map $\mathcal{A}:{{}_{}^{d_{1} \times d_{2}}\rightarrow}^{m}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

A common approach to this task is through the nonconvex optimization problem: The set of minimizers of $f$, which we denote by $\mathcal{S}$, consists of all solutions to the equation ${\mathcal{A}{({LR^{\top}})}} = b$. In order to model overparameterization, we focus on the rank-overparameterized setting $k \geq r_{\natural}$; indeed $k$ can be arbitrarily large. The three notions discussed so for can be formally defined for pairs ${(L,R)} \in \mathcal{S}$ as follows. $(L,R)$ is norm-minimal if it minimizes over $\mathcal{S}$ the square Frobenius norm $\left\| L \right\|_{\text{F}}^{2} + \left\| R \right\|_{\text{F}}^{2}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

Thus being norm-minimal means that $(L,R)$ is the closest pair from $\mathcal{S}$ to the origin in Frobenius norm. Being balanced amounts to requiring $L$ and $R$ to have the same singular values and right-singular vectors. Flat solutions are defined in terms of the "scaled trace" of the bilinear form $D^{2}f{(L,R)}$ defined as where $e_{i}$ and $e_{j}$ are the unit coordinate vectors in ${\mathbb{R}}^{d_{1} + d_{2}}$ and ${\mathbb{R}}^{k}$, respectively. In the square setting $d_{1} = d_{2} = d$, the scaled trace reduces to the usual trace divided by $d$. The scaled trace appears to have not been used previously in the literature, but is important in order to account for a possible mismatch in the dimension of the $L$ and $R$ factors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

A number of recent papers use the trace of the Hessian to measure flatness (e.g. dinh2017sharp). Other alternatives are possible, such as the maximal eigenvalue dinh2017sharp; mulayoff2020unique or the condition number liu2021noisy, but we do not focus on them here. Our main contribution can be succinctly summarized as follows: For various statistical models, flat solutions of exactly recover $M_{\natural}$.\Moreover, flat solutions have nearly minimal norm and are almost balanced.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

The exact recovery guarantee may be striking at first because flat solutions are distinct from minimal norm solutions, and thus do not correspond to nuclear norm minimization over $\mathcal{S}$. Yet, our main result shows that flat solutions do exactly recover the ground truth $M_{\natural}$ under standard statistical assumptions. The precise statistical models for which this is the case are matrix and bilinear sensing, robust PCA (or PCA with outliers), covariance matrix estimation, and single hidden layer neural networks with quadratic activation functions. Moreover, we prove weak recovery for the matrix completion problem, though our numerical experiments suggest that exact recovery holds here as well.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

We next outline our main results and the arguments that underpin them. We begin in Section 2 with the idealized "population level" setting where $\mathcal{A}$ is the identity map. In this case, we show that there is no distinction between flat, norm-minimal, and balanced solutions. As soon as $\mathcal{A}$ deviates from the identity, however, all three notions become distinct in general.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

An immediate difficulty with analyzing flat solutions of the problem with a general measurement map $\mathcal{A}$ is that flat solutions are defined as minimizers of a highly nonconvex optimization problem corresponding to minimizing the scaled trace over the solution set. In Section 3, we derive a simple convex relaxation of flat minimizers. Setting the notation, let us write $\mathcal{A}$ as ${\mathcal{A}{(X)}} = {({\langle A_{i},X\rangle},\ldots,{\langle A_{m},X\rangle})}$ for some matrices $A_{i} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ and define the "rescaling" matrices We will show in Theorem 3.2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") that flat solutions can be identified with minimizers of the problem It is worthwhile to note that without the $D_{1}$ and $D_{2}$ matrices and without the rank constraint, the problem is classically known to characterize norm-minimal solutions and is known as nuclear norm minimization. Herein, we already see the distinction between the two solution concepts. A natural convex relaxation for flat solutions simply drops the rank constraint: Summarizing, verifying that flat solutions exactly recover $M_{\natural}$ is reduced to showing that $M_{\natural}$ (which has rank $r_{\natural}$) is the unique solution of the convex problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

In Section 4, we will show that if the linear map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ or $\ell_{1}/\ell_{2}$ restricted isometry properties (RIP) and the rescaling matrices $D_{1}$ and $D_{2}$ are sufficiently close to the identity, then $M_{\natural}$ is the unique solution of. As a consequence, we deduce that flat solutions exactly recover $M_{\natural}$ for matrix sensing recht2010guaranteed; candes2011tight and bilinear sensing ling2015self; ahmed2013blind problems with Gaussian design.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Norm-minimal, flat, and balanced solutions with an identity measurement map", "weight": 1.0} -->

In this section, we focus on the idealized objective where the measurement map $\mathcal{A}$ is the identity: Recall that $M_{\natural} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ is a rank $r_{\natural}$ matrix, $k \geq r_{\natural}$ is arbitrary, and the set of minimizers $\mathcal{S}$ of coincides with the solution set of the equation ${LR^{\top}} = M_{\natural}$. We will show in this section that in this setting there is no distinction between norm-minimal, flat, and balanced solutions. As soon as the measurement map $\mathcal{A}$ is not the identity, the three notions become distinct; this remains true even under standard statistical models as our numerical experiments show. Nonetheless, the simplified setting $\mathcal{A} = \mathcal{I}$ explored in this section will serve as motivation for the rest of the paper.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Norm-minimal, flat, and balanced solutions with an identity measurement map", "weight": 1.0} -->

We begin with the following lemma that provides a convenient expression for $\text{str}{({D^{2}f{(L,R)}})}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convex relaxation and regularity of flat solutions", "weight": 1.0} -->

In this section, we begin investigating flat minimizers of the problem with general linear measurement maps $\mathcal{A}$. It will be convenient to write the linear map $\mathcal{A}{(X)}$ in coordinates as where $A_{i} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ are some matrices. As always, $\mathcal{S}$ denotes the set of solutions to the equation ${\mathcal{A}{({LR^{\top}})}} = b$. We will make use of the following two "rescaling" matrices: The section presents two main results: Theorems 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") and 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery").

<!-- chunk {"id": "body-0020", "role": "body", "section": "Convex relaxation and regularity of flat solutions", "weight": 1.0} -->

The former presents a convex relaxation for verifying that a solution is flat, while the latter shows that flat solutions are nearly balanced and nearly norm-minimal, whenever the matrices $D_{1}$ and $D_{2}$ are well-conditioned.

<!-- chunk {"id": "body-0021", "role": "body", "section": "A convex relaxation for flat solutions", "weight": 1.0} -->

Flat solutions are by definition minimizers of the highly nonconvex problem ${{\min_{{(L,R)} \in \mathcal{S}}\text{str}}{({D^{2}f{(L,R)}})}}.$ The main result of this section is to present an appealing convex relaxation of this problem. We begin with a convenient expression for the scaled trace $\text{str}{({D^{2}f{(L,R)}})}$. Namely, recall that Lemma 2.1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "A convex relaxation for flat solutions", "weight": 1.0} -->

‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery") showed the equality ${\text{str}{({D^{2}f{(L,R)}})}} = {{2\left\| L \right\|_{\text{F}}^{2}} + {2\left\| R \right\|_{\text{F}}^{2}}}$ in the simplified setting $\mathcal{A} = \mathcal{I}$. Lemma 3.1. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") provides an analogous statement for general maps $\mathcal{A}$ up to rescaling the factors by $D_{1}$ and $D_{2}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Regularity of flat solutions", "weight": 1.0} -->

In this section, we show that the condition numbers of the rescaling matrices $D_{1}$ and $D_{2}$ determine balancedness and norm minimality of flat solutions. The main result is the following theorem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Flat minima under RIP conditions: matrix and bilinear sensing", "weight": 1.0} -->

The previous section motivates a two-part strategy for showing that flat minima exactly recover the ground truth (Theorem 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")) and are automatically nearly balanced and nearly norm-minimal (Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")). The first step is to argue that the convex relaxation admits $D_{1}M_{\natural}D_{2}$ as its unique minimizer. The second step is to argue that the condition numbers of the matrices $D_{1}$ and $D_{2}$ are close to one. In this section, we follow this recipe for problems satisfying $\ell_{2}/\ell_{2}$ and $\ell_{1}/\ell_{2}$ restricted isometry properties (defined below). The main two examples will be the following random ensembles.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Matrix completion and approximate recovery", "weight": 1.0} -->

In this section, we focus on the matrix completion problem recht2011simpler; candes2009exact. This is an instance of where the linear measurement map $\mathcal{A}$ is generated as follows. For each $i \in {\lbrack d_{1}\rbrack}$ and $j \in {\lbrack d_{2}\rbrack}$, let $\xi_{ij}$ be independent Bernoulli random variables with success probability $p$. The linear map $\mathcal{A}:{{}_{}^{d_{1} \times d_{2}}\rightarrow}^{d_{1} \times d_{2}}$ is then defined by the relation The difficulty of recovering the matrix $M_{\natural}$ is typically measured by an incoherence parameter, which we now define.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Matrix completion and approximate recovery", "weight": 1.0} -->

Given a singular value decomposition $M_{\natural} = {U_{\natural}\Sigma_{\natural}V_{\natural}^{\top}}$ with $\Sigma_{\natural} \in^{r_{\natural} \times r_{\natural}}$, the incoherence parameter is the smallest $\mu > 0$ satisfying Here $\left\| A \right\|_{2,\infty}$ denotes the maximal $\ell_{2}$-norm of the rows of the matrix $A$. The strategies outlined in the previous section do not directly apply for analyzing flat minima of the matrix completion problem because the linear map $\mathcal{A}{({D_{1}^{- 1} \cdot D_{2}^{- 1}})}$ does not satisfy RIP type conditions. Instead we will settle for a weak recovery result.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Robust principal component analysis (PCA)", "weight": 1.0} -->

In this section, we focus on problem of principal component analysis (PCA) with outliers, also known as "robust PCA", following the approach in candes2011robust; chandrasekaran2011rank. Though this problem is not of the form, we will see that flat solutions (appropriately defined) exactly recover the ground truth under reasonable assumptions. The robust PCA problem asks to find a matrix $M_{\natural} \in^{d_{1} \times d_{2}}$ that has been corrupted by sparse noise $S_{\natural}$. More precisely, we observe a matrix $Y \in^{d_{1} \times d_{2}}$ of the form The matrix $S_{\natural}$ is assumed to have at most $l_{\natural}$ many nonzero entries in any column and in any row, and $M_{\natural}$ has rank $r_{\natural}$. Moreover, following existing literature we assume that the matrix $M_{\natural}$ is strongly incoherent with parameter $\mu$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robust principal component analysis (PCA)", "weight": 1.0} -->

That is, given a singular value decomposition $M_{\natural} = {U_{\natural}\Sigma_{\natural}V_{\natural}^{\top}}$ with $\Sigma_{\natural} \in^{r_{\natural} \times r_{\natural}}$, we let $\mu > 0$ denote the smallest constant satisfying where $\left. \parallel \cdot \parallel{}_{\infty} \right.$ denotes the entrywise sup-norm.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Robust principal component analysis (PCA)", "weight": 1.0} -->

One common approach for recovering $M_{\natural}$ is to solve the problem: where we define the set and $\left. \parallel \cdot \parallel{}_{1,1} \right.$ is entry-wise $\ell_{1}$-norm used to promote sparsity. The factors $L$ and $R$ vary over ${\mathbb{R}}^{d_{1} \times k}$ and ${\mathbb{R}}^{d_{2} \times k}$, respectively. As usual, we focus on the rank overparameterized setting $k \geq r_{\natural}$. Note that the optimal value of the problem (49 ‣ Flat minima generalize for low-rank matrix recovery")) is clearly zero.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Robust principal component analysis (PCA)", "weight": 1.0} -->

Observe that we may express the problem (51 ‣ Flat minima generalize for low-rank matrix recovery")) more compactly as where ${dist}_{\Omega}^{2}$ denotes the square Frobenius distance to $\Omega$. This is the overparameterized problem that we will focus. As usual, we let $\mathcal{S}$ denote the set of minimizers of $f$; note that $\mathcal{S}$ is simply the set of pairs $(L,R)$ satisfying ${Y - {LR^{\top}}} \in \Omega$. Observe that the objective function $f$ is $C^{1}$-smooth but not $C^{2}$-smooth. Therefore, in order to measure flatness, we proceed via a smoothing technique introduced in (ha2020equivalence Section 4.2), (ge2017no Section 4.3).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Robust principal component analysis (PCA)", "weight": 1.0} -->

Namely, we approximate $f$ near a basepoint $(\overset{\sim}{L},\overset{\sim}{S})$ by the local model: where $P_{\Omega}$ denotes the nearest point projection onto $\Omega$. It is straightforward to see that the $C^{2}$-smooth function $f_{\overset{\sim}{L},\overset{\sim}{R}}{(\cdot, \cdot)}$ majorizes $f$ and agrees with $f{(\cdot, \cdot)}$ up to first order at $(\overset{\sim}{L},\overset{\sim}{R)}$. We may therefore define a minimizer of (50 ‣ Flat minima generalize for low-rank matrix recovery")) to be flat if it solves the problem: The following is the main result of the section.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Neural networks with quadratic activations and covariance matrix estimation", "weight": 1.0} -->

In this section, we investigate flat minimizers of a one hidden layer neural network, considered in the work soltanolkotabi2018theoretical; li2018algorithmic for the purpose of analyzing the energy landscape around saddle points. Though this problem is not in the form, we will see that flat minimizers (naturally defined) exactly recover the ground truth under reasonable statistical assumptions. As a special case, we will obtain guarantees for flat minimizers of the overparameterized covariance matrix estimation problem.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Neural networks with quadratic activations and covariance matrix estimation", "weight": 1.0} -->

The problem setup, following soltanolkotabi2018theoretical; li2018algorithmic, is as follows. We suppose that given an input vector $x \in {\mathbb{R}}^{d}$ a response vector $y{(x)}$ is given by the function We assume that the output weight vector $v \in^{r}$ has $r_{1}$ positive entries and $r_{2}$ negative entries, the hidden layer weight matrix $U_{\natural}$ has dimensions $d \times r_{\natural}$, and we use a quadratic activation ${q{(s)}} = s^{2}$ applied coordinatewise.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Neural networks with quadratic activations and covariance matrix estimation", "weight": 1.0} -->

The prediction $\hat{y}$ of the neural network on input $x$ is thus given by Thus the overparameterized problem we aim to solve is As usual, we define the solution set $\mathcal{S} = {\{{U \in {\mathbb{R}}^{d \times k}}:{{f{(U)}} = 0}\}}$. We will see shortly that $\mathcal{S}$ is nonempty and therefore coincides with the set of minimizers of $f$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Neural networks with quadratic activations and covariance matrix estimation", "weight": 1.0} -->

Naturally, we declare a matrix $U_{f} \in \mathcal{S}$ to be flat if it minimizes the trace of the Hessian of $f$ over the set of the minimizers of $f$, i.e., it solves the problem In this section, we aim to show: with high probability over the training set ${\{{(x_{i},y_{i})}\}}_{i = {1,\ldots,n}}$ flat solutions $U_{f}$ achieve zero generalization error, that is ${{{\mathbb{E}}_{x \sim {N{(0,I)}}}{({{\hat{y}{(U_{f},x)}} - {y{(U_{\natural},x)}}})}} = 0}.$ Indeed, we will prove a stronger result by relating the problem to low-rank matrix factorization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Neural networks with quadratic activations and covariance matrix estimation", "weight": 1.0} -->

Therefore, the set of minimizers of $f$ is nonempty and it coincides with $\mathcal{S}$. Note that in the special case $r_{2} = k_{2} = 0$, the problem becomes covariance matrix estimation chen2015exact and further reduces to phase retrieval when $k_{1} = r_{1} = 1$ candes2013phaselift.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Neural networks with quadratic activations and covariance matrix estimation", "weight": 1.0} -->

Summarizing, the task of finding a matrix $U$ with a small generalization error, $|{{\mathbb{E}}_{x \sim {N{(0,I)}}}{\lbrack{{\hat{y}{(U,x)}} - {y{(U_{\natural},x)}}}\rbrack}}|$, amounts to implicitly recovering the symmetric matrix $M_{\natural}$, but with the parameterization ${U_{1}U_{1}^{\top}} - {U_{2}U_{2}^{\top}}$ instead of the usual $LR^{\top}$ parameterization. The following is the main theorem of the section.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

Recall that we have proved that for a variety of overparameterized problems, under standard statistical assumptions, in the noiseless setting, flat solutions recover the ground truth and flat solutions are nearly norm-minimal and nearly-balanced (but not exactly). In this section, we numerically validate both of the claims, in order. Note that finding flat solutions in these examples, amounts to solving a convex optimization problem as long as the number of measurements is sufficiently large.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

(d) NN with quadratic activation Figure 3: The empirical probability of successful recovery of M♮ for different combination of dimension d and number of measurements m (p for matrix completion). We use gray scale and the whiter the color, the higher probability of success.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiment setup", "weight": 1.0} -->

We consider four problems described earlier in the paper: (a) matrix sensing, (b) bilinear sensing, (c) matrix completion, and (d) neural networks with quadratic activation. For each setting, we consider different combination of the dimension $d = d_{1} = d_{2}$ and the number of measurements $m$ ($p$ for matrix completion). For each combination $(d,m)$ ( $(d,p)$ for matrix completion), we randomly generate a rank $2$ ground truth unit Frobenius norm matrix $M_{\natural}$ (rank $3$ for the setting of neural network with quadratic activation), then repeatedly generate the linear measurement map $\mathcal{A}$ and solve ten times the convex relaxation associated with being a flat solution and the nuclear norm minimization problem.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Exact Recovery", "weight": 1.0} -->

To measure the success of exact recovery, for a solution $\hat{X}$ from the convex relaxation of the scaled trace problem (or from the nuclear norm minimization), we measure the Frobenius norm error $\left\| {{D_{1}^{- 1}\hat{X}D_{2}^{- 1}} - M_{\natural}} \right\|_{\text{F}}$ (or $\left\| {\hat{X} - M_{\natural}} \right\|_{\text{F}}$ for the nuclear norm minimization). Our criterion for exact recovery is whether this error is smaller than $10^{- 6}$ or not. Figure 3 shows the empirical probability of success recovery (averaging over ten times) for each combination of dimension and number of measurements. The figure is in gray scale and the whiter color indicates higher success probability. We observe that the frequency of exact recovery by flat solutions almost matches the frequency of exact recovery by nuclear norm minimization.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Exact Recovery", "weight": 1.0} -->

Notice moreover that flat solutions exactly recover the ground truth matrix, though we are only able to show weak recovery for matrix completion.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Regularity", "weight": 1.0} -->

Next we test the regularity of flat solutions for the (a) matrix sensing, (b) bilinear sensing, (c) matrix completion problems. We only consider the pairs $(d,m)$ such that the matrices $D_{1},D_{2}$ are nonsingular. Let $\hat{X}$ be the solution of the convex relaxation for being a flat solution and let ${\hat{X}}_{\text{nuc}}$ be the solution to the nuclear norm minimization problem. We compute the factors $L_{f} = {D_{1}^{- 1}U\sqrt{\Sigma}}$ and $R_{f} = {D_{2}^{- 1}V\sqrt{\Sigma}}$ using the full SVD of $\hat{X} = {U\SigmaV^{\top}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Regularity", "weight": 1.0} -->

The result (in $\log 10$ scale) is shown in Figure 4. We observe that whenever flat solutions exactly recover the ground truth, both measures are small but not exactly zero. In particular, the norm-minimal and flat solutions are distinct.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion and discussion on depth", "weight": 1.5} -->

In this paper, we analyzed a variety of low rank matrix recovery problems in rank-overparameterized settings. We considered overparameterized matrix and bilinear sensing, robust PCA, covariance matrix estimation, and single hidden layer neural networks with quadratic activation functions. In all cases, we showed that flat minima, measured by the scaled trace of the Hessian, exactly recover the ground truth under standard statistical assumptions. For matrix completion, we established weak recovery, although empirical evidence suggests exact recovery holds here as well.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion and discussion on depth", "weight": 1.5} -->

Matrix factorization problems are suggestive of the behavior one may expect for two layer neural networks. Therefore, an appealing question is to consider the effect that depth may have on generalization properties of flat solutions. In this section, we argue that depth may not bode well for generalization of flat solutions. As a simple model, we consider the setting of sparse recovery under a "deep" overparameterization. Namely, consider a ground truth vector $x_{\natural} \in^{d}$ with at most $r_{\natural}$ nonzero coordinates. The goal is to recover $x_{\natural}$ from the observed measurements $b = {Ax_{\natural}}$ under a linear map $A:{{}_{}^{d}\rightarrow}^{m}$. We assume that $A$ satisfies the restricted isometry property (RIP): there exist $(\delta_{1},\delta_{2})$ such that for all $x \in {\mathbb{R}}^{d}$ that have at most $2r$ nonzero coordinates.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion and discussion on depth", "weight": 1.5} -->

The simple least square formulation for finding consistent dense signals is We introduce overparameterization by parameterizing the variable $x$ as the Hadamard product $\odot$ of $k$ factors $x = {v_{1} \odot v_{2} \odot \cdots \odot v_{k}}$ with $v_{i} \in {\mathbb{R}}^{d}$. Thus, the problem becomes The flat solutions are naturally defined as those ${(v_{i})}_{i = 1}^{k}$ solving the following problem: To compute the Hessian $\operatorname{tr}{({D^{2}f{(v_{1},\ldots,v_{k})}})}$, let $a_{i}$ be the $i$-th column of $A$. Following a similar calculation as in Lemma 3.1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and discussion on depth", "weight": 1.5} -->

‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") yields the expression for any ${(v_{i})}_{i = 1}^{k} \in^{d \times k}$ where The following lemma shows that $D$ is close to the identity matrix.
