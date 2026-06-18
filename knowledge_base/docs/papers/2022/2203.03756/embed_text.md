## Introduction

Recent advances in machine learning and artificial intelligence have relied on fitting highly overparameterized models, notably deep neural networks, to observed data tan2019efficientnet; kolesnikov2020big; huang2019gpipe; zhang2021understanding. In such settings, the number of parameters of the model is much greater than the number of data samples, thereby resulting in models that achieve near-zero training error. Although classical learning paradigms caution against overfitting, recent work suggests ubiquity of the "double descent" phenomenon belkin2019reconciling, wherein significant overparameterization actually improves generalization. There is an important caveat, however, that is worth emphasizing. There is typically a continuum of models with zero training error; some of these models generalize well and some do not. Reassuringly, there is evidence that basic algorithms, such as the stochastic gradient method, are implicitly biased towards finding models that do generalize; see for example soudry2018implicit; gunasekar2018implicitNN; jacot2018neural; heckel2020compressive; jastrzkebski2017three; smith2017bayesian; hoffer2017train; masters2018revisiting; neyshabur2014search; gunasekar2018implicit; du2018algorithmic; mulayoff2020unique. Other seminal works bartlett1998sample; bartlett2002rademacher; neyshabur2017exploring seeking to explain generalization have focused on quantifying stability, capacity, and margin bounds. Understanding generalization of overparameterized models remains an active area of research, and is the topic of our work.

Existing literature highlights two intriguing properties---small norm and flat landscape---that correlate with generalization neyshabur2017exploring; dziugaite2017computing; dinh2017sharp. Indeed, it has long been known that the magnitude of the weights plays an important role for neural network training. As a result, one typically incorporates a squared $\ell_{2}$-penalty on the weights---called weight decay---when applying iterative methods. One intuitive explanation is that minimizing the square Frobenius norm of the factors in matrix factorization problems is equivalent to minimizing the nuclear norm---a well-known regularizer for inducing low-rank structure recht2010guaranteed. Far reaching generalizations of this phenomenon for various neural network architectures have been recently pursued in savarese2019infinite; ongie2019function; ongie2022role. In parallel, empirical evidence hochreiter1997flat; Keskar2016; li2017visualizing strongly suggests that those models around which the landscape is flat---meaning the training loss grows slowly---generalize well. See Figure 1 for an illustration of flat and sharp minima. Inspired by this observation, a variety of algorithms have been proposed to explicitly bias the iterates towards flat solutions chaudhari2019entropy; izmailov2018averaging; norton2021diametrical; foret2020sharpness, with impressive observed performance. In contrast to the magnitude of the weights, the theoretic basis for flatness is much less clear even for simple overparameterized nonlinear problems. The goal of our work is to answer the following question:

> Do flat minimizers generalize for a broad family of overparameterized problems?

Figure 1: Flat vs. sharp minima of the training loss.

Putting generalization aside, one would hope that flat solutions are in some sense regular, occurring in a benign region where algorithms perform well. For example, numerical methods for neural network training are strongly influenced by how balanced the parameters appear. Namely, the set of interpolating neural networks contains models with consecutive weight matrices that are poorly scaled relative to each other du2018algorithmic; shamir2018resnets. It has recently been shown that gradient descent in continuous time keeps the factors balanced ye2021global; ma2021beyond for matrix factorization and for deep learning du2018algorithmic; mulayoff2020unique. Despite ubiquity of the three notions discussed so far---small norm, flatness, and balancedness---the exact relationship between them is unclear. Thus our secondary question is as follow:

Are flat minimizers nearly norm-minimal and nearly balanced\
for a broad family of overparameterized problems?

### Problem setting: overparameterized matrix factorization

We answer both questions in the setting of low-rank matrix factorization---a prototypical problem class often used to gain insight into more general deep learning models li2018algorithmic; du2018algorithmic; ye2021global. Setting the stage, consider a ground truth matrix $M_{\natural} \in^{d_{1} \times d_{2}}$ with rank $r_{\natural}$. The goal is to recover $M_{\natural}$ from the observed measurements $b = {\mathcal{A}{(M_{\natural})}}$ under a linear measurement map $\mathcal{A}:{}_{}^{d_{1} \times d_{2}}^{m}$. A common approach to this task is through the nonconvex optimization problem:

The set of minimizers of $f$, which we denote by $\mathcal{S}$, consists of all solutions to the equation ${\mathcal{A}{({LR^{\top}})}} = b$. In order to model overparameterization, we focus on the rank-overparameterized setting $k \geq r_{\natural}$; indeed $k$ can be arbitrarily large. The three notions discussed so for can be formally defined for pairs ${(L,R)} \in \mathcal{S}$ as follows.

$(L,R)$ is norm-minimal if it minimizes over $\mathcal{S}$ the square Frobenius norm $\left\| L \right\|_{\text{F}}^{2} + \left\| R \right\|_{\text{F}}^{2}$.

$(L,R)$ is balanced if it satisfies ${L^{\top}L} = {R^{\top}R}$.

$(L,R)$ is flat if it minimizes over $\mathcal{S}$ the "scaled trace" of the Hessian, $\text{str}{({D^{2}f{(L,R)}})}$.

Thus being norm-minimal means that $(L,R)$ is the closest pair from $\mathcal{S}$ to the origin in Frobenius norm. Being balanced amounts to requiring $L$ and $R$ to have the same singular values and right-singular vectors. Flat solutions are defined in terms of the "scaled trace" of the bilinear form $D^{2}f{(L,R)}$ defined as

where $e_{i}$ and $e_{j}$ are the unit coordinate vectors in ${\mathbb{R}}^{d_{1} + d_{2}}$ and ${\mathbb{R}}^{k}$, respectively. In the square setting $d_{1} = d_{2} = d$, the scaled trace reduces to the usual trace divided by $d$. The scaled trace appears to have not been used previously in the literature, but is important in order to account for a possible mismatch in the dimension of the $L$ and $R$ factors. A number of recent papers use the trace of the Hessian to measure flatness (e.g. dinh2017sharp ). Other alternatives are possible, such as the maximal eigenvalue dinh2017sharp; mulayoff2020unique or the condition number liu2021noisy, but we do not focus on them here. Our main contribution can be succinctly summarized as follows:

For various statistical models, flat solutions of exactly recover $M_{\natural}$.\
Moreover, flat solutions have nearly minimal norm and are almost balanced.

The exact recovery guarantee may be striking at first because flat solutions are distinct from minimal norm solutions, and thus do not correspond to nuclear norm minimization over $\mathcal{S}$. Yet, our main result shows that flat solutions do exactly recover the ground truth $M_{\natural}$ under standard statistical assumptions. The precise statistical models for which this is the case are matrix and bilinear sensing, robust PCA (or PCA with outliers), covariance matrix estimation, and single hidden layer neural networks with quadratic activation functions. Moreover, we prove weak recovery for the matrix completion problem, though our numerical experiments suggest that exact recovery holds here as well.

### Main results and outline of the paper

We next outline our main results and the arguments that underpin them. We begin in Section 2 with the idealized "population level" setting where $\mathcal{A}$ is the identity map. In this case, we show that there is no distinction between flat, norm-minimal, and balanced solutions. As soon as $\mathcal{A}$ deviates from the identity, however, all three notions become distinct in general.

Figure 2: Equivalence between balanced, minimal norm, and flat solutions when 𝒜 = ℐ.

An immediate difficulty with analyzing flat solutions of the problem with a general measurement map $\mathcal{A}$ is that flat solutions are defined as minimizers of a highly nonconvex optimization problem corresponding to minimizing the scaled trace over the solution set. In Section 3, we derive a simple convex relaxation of flat minimizers. Setting the notation, let us write $\mathcal{A}$ as ${\mathcal{A}{(X)}} = {({\langle A_{i},X\rangle},\ldots,{\langle A_{m},X\rangle})}$ for some matrices $A_{i} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ and define the "rescaling" matrices

We will show in Theorem 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") that flat solutions can be identified with minimizers of the problem

It is worthwhile to note that without the $D_{1}$ and $D_{2}$ matrices and without the rank constraint, the problem is classically known to characterize norm-minimal solutions and is known as nuclear norm minimization. Herein, we already see the distinction between the two solution concepts. A natural convex relaxation for flat solutions simply drops the rank constraint:

Summarizing, verifying that flat solutions exactly recover $M_{\natural}$ is reduced to showing that $M_{\natural}$ (which has rank $r_{\natural}$) is the unique solution of the convex problem.

In Section 4, we will show that if the linear map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ or $\ell_{1}/\ell_{2}$ restricted isometry properties (RIP) and the rescaling matrices $D_{1}$ and $D_{2}$ are sufficiently close to the identity, then $M_{\natural}$ is the unique solution of. As a consequence, we deduce that flat solutions exactly recover $M_{\natural}$ for matrix sensing recht2010guaranteed; candes2011tight and bilinear sensing ling2015self; ahmed2013blind problems with Gaussian design. The former corresponds to the setting where the entries of $A_{i}$ are independent standard Gaussian random variables, while the latter corresponds to the setting $A_{i} = {a_{i}b_{i}^{\top}}$ where $a_{i} \in {\mathbb{R}}^{d_{1}}$ and $b_{i} \in {\mathbb{R}}^{d_{2}}$ are independent standard Gaussian vectors. The end result is the following theorem. Simplifying notation, we set $d_{\max} = {\max{\{ d_{1},d_{2}\}}}$ and $d_{\min} = {\min{\{ d_{1},d_{2}\}}}$.

### Theorem 1.1 (Matrix and bilinear sensing (Informal))

Suppose that $\mathcal{A}$ is generated according to a Gaussian matrix sensing or bilinear sensing model. Then as long as we are in the regime $m \gtrsim {r_{\natural}d_{\max}}$ and $d_{\min} \gtrsim {\log m}$, with high probability, any flat solution $(L_{f},R_{f})$ satisfies ${{L_{f}R_{f}^{\top}} = M_{\natural}},$ and is nearly norm-minimal and nearly balanced.

Note that our requirement on the sample size $m \gtrsim {r_{\natural}d_{\max}}$ matches the known regime for exact recovery with nuclear norm minimization candes2011tight; cai2015rop. Since we are interested in the high dimensional regime, the extra condition $d_{\min} \gtrsim {\log{(m)}}$ can be assumed without harm. Appendix A presents a generalization of this result when the measurements $b$ are corrupted by noise.

We next move on to analyzing the matrix completion problem in Section 5. We focus on the Bernoulli model, wherein each matrix $A_{i}$ takes the form $A_{i} = {\xi_{ij}e_{i}e_{j}^{\top}}$, where $e_{i}$ and $e_{j}$ denote the $i$'th and $j$'th coordinate vectors in ${\mathbb{R}}^{d}$ and $\xi_{ij}$ are independent Bernoulli random variables with success probability $p \in {}$. The main difficulty with analyzing the matrix completion problem is that the linear map $\mathcal{A}$ does not have good restricted isometry properties. Moreover, the existing techniques for analyzing the nuclear norm relaxation of the matrix completion problem recht2011simpler; candes2009exact do not directly apply to the problem because of the dependence between the rescaling matrices $D_{1}$, $D_{2}$, and the observation map $\mathcal{A}$. Consequently, we settle for an approximate recovery guarantee.

### Theorem 1.2 (Matrix completion (Informal))

Suppose that $\mathcal{A}$ is generated from the Bernoulli matrix completion model with success probability $p > 0$ and let $\mu > 0$ be the incoherence parameter of $M_{\natural}$.^11^1See for the definition of the incoherence parameter $\mu$. Then provided we are in the regime $p \gtrsim {\frac{1}{\gamma}\sqrt{\frac{r_{\natural}{\log{(d_{\max})}}}{d_{\min}}}}$, with high probability, any flat solution $(L_{f},R_{f})$ satisfies $\left\| {{L_{f}R_{f}^{\top}} - M_{\natural}} \right\|_{\ast} \leq {\gamma\left\| M_{\natural} \right\|_{\ast}}$ and is nearly norm-minimal and nearly balanced.

Hence according to this theorem, in order to conclude that flat solutions achieve a constant relative error, we must be in the regime $p \gtrsim \sqrt{\frac{r_{\natural}{\log d_{\max}}}{d_{\min}}}$. This is a stronger requirement than is needed for exact recovery of the ground truth matrix by nuclear norm minimization chen2015incoherence, which is $p \gtrsim {\mur_{\natural}{\log{({\mur_{\natural}})}}\frac{\log{(d_{\max})}}{d_{\min}}}$. We stress, however, that our numerical results suggest that flat solutions exactly recovery the ground truth matrix in this wider parameter regime.

We next focus on the problem of Robust Principal Component Analysis (PCA) in Section 6 ‣ Flat minima generalize for low-rank matrix recovery"). Though this problem is not of the form, we will see that flat solutions (appropriately defined) exactly recover the ground truth under reasonable assumptions. Specifically, following candes2011robust; chandrasekaran2011rank, the robust PCA problem asks to find a low-rank matrix $M_{\natural} \in^{d_{1} \times d_{2}}$ that has been corrupted by sparse noise $S_{\natural}$. Thus, we observe a matrix $Y \in^{d_{1} \times d_{2}}$ of the form

where the matrix $S_{\natural}$ is assumed to have at most $l_{\natural}$ nonzero entries in any column and in any row. A popular formulation of the problem (see (ha2020equivalence Eqn. ), (ge2017no Eqn. )) takes the form

where ${dist}_{\Omega}^{2}$ is the square Frobenius distance to the sparsity-inducing set $\Omega:={\{ S\mid{\left\| S \right\|_{1,1} \leq \left\| S_{\natural} \right\|_{1,1}}\}}$. The objective function $f$ is $C^{1}$-smooth but not $C^{2}$-smooth. Therefore, in order to measure flatness, we approximate $f$ near a basepoint $(\overset{\sim}{L},\overset{\sim}{S})$ by a certain $C^{2}$-smooth local model $f_{\overset{\sim}{L},\overset{\sim}{R}}{(L,R)}$, introduced in (ha2020equivalence Section 4.2), (ge2017no Section 4.3). See Section 6 ‣ Flat minima generalize for low-rank matrix recovery") for a precise definition of $f_{\overset{\sim}{L},\overset{\sim}{R}}{(L,R)}$. We then define a minimizer of to be flat if it minimizes the scaled trace $\text{str}{({D^{2}f_{L,R}{(L,R)}})}$ over all ${(L,R)} \in \mathcal{S}$. We will prove the following theorem, which largely follows from the results of chen2013low.

### Theorem 1.3 (Robust PCA (Informal))

Let $\mu$ be the strong incoherence parameter of $M_{\natural}$.^22^2 See (48 ‣ Flat minima generalize for low-rank matrix recovery")) for the definition of the strong incoherence parameter $\mu$. Then, in the regime $l_{\natural} \lesssim \frac{d_{\min}}{\mur_{\natural}}$, any flat minimizer $(L_{f},R_{f})$ satisfies ${L_{f}R_{f}^{\top}} = M_{\natural}$.

Section 7 analyzes the last problem class of the paper, motivated by the problems of covariance matrix estimation and training of shallow neural networks. Setting the stage, consider a ground truth matrix $M_{\natural}$ satisfying

for some matrices $U_{1,\natural} \in {\mathbb{R}}^{d \times r_{1}}$ and $U_{2,\natural} \in {\mathbb{R}}^{d \times r_{2}}$. The goal is to recover $M_{\natural}$ from the observations

where $x_{1},\ldots,{x_{m}\overset{\text{iid}}{\sim}N{(0,I_{d})}}$. Note that in the special case $r_{2} = 0$, this problem reduces to covariance matrix estimation chen2015exact and further reduces to phase retrieval when $r_{1} = 1$ candes2013phaselift. The added generality allows to also model shallow neural networks with quadratic activation functions; see details below. A natural optimization formulation of the problem takes the form

where the sensing matrices are $A_{i} = {x_{i}x_{i}^{\top}}$ and $k_{i} \geq r_{i}$ for $i = {1,2}$. Since $\text{str}{(D^{2}f{(U_{1},U_{2})})}) = d\operatorname{tr}(D^{2}f{(U_{1},U_{2})})$, we declare a minimizer $(U_{1,f},U_{2,f})$ to be flat if it has minimal trace $\operatorname{tr}{({D^{2}f{(U_{1},U_{2})}})}$ among all minimizers of. We prove the following.

### Theorem 1.4 (Exact recovery)

In the regime $m \gtrsim {C{({r_{1} + r_{2}})}d}$ and $d \gtrsim {C{\log m}}$, with high probability, any flat solution $(U_{f,1},U_{f,2})$ of satisfies ${{U_{f,1}U_{f,1}^{\top}} - {U_{f,2}U_{f,2}^{\top}}} = M_{\natural}$.

Here, our requirement on the sample size $m \gtrsim {C{({r_{1} + r_{2}})}d}$ coincides with the known requirement for exact recovery by nuclear norm minimization chen2015exact in terms of $r$ and $d$. An interesting example of arises from a model of shallow neural networks, analyzed in soltanolkotabi2018theoretical; li2018algorithmic for the purpose of studying energy landscape around saddle points. Namely, suppose that given an input vector $x \in {\mathbb{R}}^{d}$ a response vector $y{(x)}$ is generated by the "teacher neural network"

where the output weight vector $v \in^{r}$ has $r_{1}$ positive entries and $r_{2}$ negative entries, the hidden layer weight matrix $U_{\natural}$ has dimensions $d \times r_{\natural}$, and we use a quadratic activation ${q{(s)}} = s^{2}$ applied coordinate-wise. We get to observe a set of $m$ pairs ${(x_{i},y_{i})} \in {{\mathbb{R}}^{d} \times {\mathbb{R}}}$, where the features $x_{i}$ are drawn as $x_{i}\overset{\text{iid}}{\sim}N{(0,I_{d})}$ and the output values are $y_{i} = {y{(x_{i})}}$. The goal is to fit the data with an overparameterized "student neural network"

with hidden weights $U \in^{d \times k}$ and output layer weights $u = {(\mathbf{1}_{k_{1}},{- \mathbf{1}_{k_{2}}})}$, where $k_{1} \geq r_{1}$, and $k_{2} \geq r_{2}$. It is straightforward to see that by partitioning the matrix $U = {\lbrack U_{1},U_{2}\rbrack}$, this problem is exactly equivalent to recovering the matrix $M_{\natural} = {U_{\natural}{{diag}{(v)}}U_{\natural}^{\top}}$ from the observations.

Section 8 numerically validates our theoretical results. Section 9 summarizes our findings and speculates about the role of depth on generalization properties of flat solutions.

### Notation

Throughout, we let ${\mathbb{R}}^{d}$ denote the $d$-dimensional Euclidean space, equipped with the usual dot-product ${\langle x,y\rangle} = {x^{\top}y}$ and the induced Euclidean norm $\parallel \cdot \parallel_{2}$. More generally, the symbol $\parallel \cdot \parallel_{p}$ will denote the $\ell_{p}$ norm on ${\mathbb{R}}^{d}$. Given two numbers $d_{1}$ and $d_{2}$, which will be clear from context, we set $d_{\max}:={\max{\{ d_{1},d_{2}\}}}$ and $d_{\min}:={\min{\{ d_{1},d_{2}\}}}$. The Euclidean space of $d_{1} \times d_{2}$ real matrices ${\mathbb{R}}^{d_{1} \times d_{2}}$ will always be equipped with the trace inner product ${\langle X,Y\rangle} = {\operatorname{tr}{({X^{\top}Y})}}$ and the induced Frobenius norm $\left\| X \right\|_{\text{F}} = \sqrt{\langle X,X\rangle}$. The nuclear norm $\left\| X \right\|_{\ast}$ of any matrix $X \in {\mathbb{R}}^{d_{1} \times d_{2}}$ is the sum of its singular values. We will often use the characterization of the nuclear norm (srebro2005rank Lemma 1):

## Norm-minimal, flat, and balanced solutions with an identity measurement map

In this section, we focus on the idealized objective where the measurement map $\mathcal{A}$ is the identity:

Recall that $M_{\natural} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ is a rank $r_{\natural}$ matrix, $k \geq r_{\natural}$ is arbitrary, and the set of minimizers $\mathcal{S}$ of coincides with the solution set of the equation ${LR^{\top}} = M_{\natural}$. We will show in this section that in this setting there is no distinction between norm-minimal, flat, and balanced solutions. As soon as the measurement map $\mathcal{A}$ is not the identity, the three notions become distinct; this remains true even under standard statistical models as our numerical experiments show. Nonetheless, the simplified setting $\mathcal{A} = \mathcal{I}$ explored in this section will serve as motivation for the rest of the paper.

We begin with the following lemma that provides a convenient expression for $\text{str}{({D^{2}f{(L,R)}})}$.

### Lemma 2.1 (Scaled trace)

The second-order derivative of the function $f$ at any ${(L,R)} \in \mathcal{S}$ is the quadratic form:

Consequently, the scaled trace is simply

### Proof

A straightforward computation shows for any pair $(L,R)$ the expression

For pairs ${(L,R)} \in \mathcal{S}$, the first term on the right is zero yielding the claimed expression (12. ‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery")). To see the expression for the scaled trace, let $e_{i} \in {\mathbb{R}}^{d_{1} + d_{2}}$ and $e_{j} \in {\mathbb{R}}^{k}$ be the $i$'th and $j$'th coordinate vectors. A quick computation shows ${D^{2}f{(L,R)}{\lbrack{e_{i}e_{j}^{\top}}\rbrack}} = {2\left\| R_{j} \right\|_{\text{F}}^{2}}$ for $i \leq d_{1}$ and $\left. D^{2}f{(L,R)})\lbrack e_{i}e_{j}^{\top}\rbrack = 2\parallel L_{j}\parallel_{\text{F}}^{2} \right.$ for $i > d_{1}$. Therefore, from the definition, the scaled trace becomes

We are now ready to prove the claimed equivalence between the three properties.

### Lemma 2.2 (Equivalence)

Norm-minimal, flat, and balanced solutions of all coincide.

### Proof

First, the equivalence of flat and norm-minimal solutions follows directly from the expression (13. ‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery")) in Lemma 2.1. ‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery"). Next, we prove the equivalence between minimal norm and balanced solutions. Suppose ${(L,R)} \in S$ is balanced. The equality ${L^{\top}L} = {R^{\top}R}$ implies that $L$ and $R$ have the same nonzero singular values and the same set of right singular vectors. Therefore, we may form compact singular value decompositions $L = {U_{1}\SigmaV^{\top}}$ and $R = {U_{2}\SigmaV^{\top}}$. Since equality ${LR^{\top}} = M_{\natural}$ holds, we see that ${U_{1}\Sigma^{2}U_{2}^{\top}} = M_{\natural}$. Hence, the nuclear norm of $M_{\natural}$ is simply $\left\| M_{\natural} \right\|_{\ast} = {\operatorname{tr}{(\Sigma^{2})}}$. Noting the equality ${\frac{1}{2}\left( {\left\| L \right\|_{\text{F}}^{2} + \left\| R \right\|_{\text{F}}^{2}} \right)} = {\operatorname{tr}{(\Sigma^{2})}}$ along with, we deduce that $(L,R)$ is a minimal norm solution, as claimed. Conversely, suppose that $(L,R)$ is a minimal norm solution. Define the function

over the open set of $k \times k$ invertible matrices $B$. Clearly $B = I_{k}$ is a local minimizer of $\varphi$ and therefore ${\nabla\varphi}{(I_{k})}$ must be the zero matrix. A quick computation yields the expression ${{{\nabla\varphi}{(I_{k})}} = {{L^{\top}L} - {R^{\top}R}}},$ and therefore $(L,R)$ is balanced, as claimed. ∎

## Convex relaxation and regularity of flat solutions

In this section, we begin investigating flat minimizers of the problem with general linear measurement maps $\mathcal{A}$. It will be convenient to write the linear map $\mathcal{A}{(X)}$ in coordinates as

where $A_{i} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ are some matrices. As always, $\mathcal{S}$ denotes the set of solutions to the equation ${\mathcal{A}{({LR^{\top}})}} = b$. We will make use of the following two "rescaling" matrices:

The section presents two main results: Theorems 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") and 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery"). The former presents a convex relaxation for verifying that a solution is flat, while the latter shows that flat solutions are nearly balanced and nearly norm-minimal, whenever the matrices $D_{1}$ and $D_{2}$ are well-conditioned.

### A convex relaxation for flat solutions

Flat solutions are by definition minimizers of the highly nonconvex problem ${{\min_{{(L,R)} \in \mathcal{S}}\text{str}}{({D^{2}f{(L,R)}})}}.$ The main result of this section is to present an appealing convex relaxation of this problem. We begin with a convenient expression for the scaled trace $\text{str}{({D^{2}f{(L,R)}})}$. Namely, recall that Lemma 2.1. ‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery") showed the equality ${\text{str}{({D^{2}f{(L,R)}})}} = {{2\left\| L \right\|_{\text{F}}^{2}} + {2\left\| R \right\|_{\text{F}}^{2}}}$ in the simplified setting $\mathcal{A} = \mathcal{I}$. Lemma 3.1. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") provides an analogous statement for general maps $\mathcal{A}$ up to rescaling the factors by $D_{1}$ and $D_{2}$.

### Lemma 3.1 (Scaled trace and the Frobenius norm)

The second-order derivative of the function $f$ at any ${(L,R)} \in \mathcal{S}$ is the quadratic form:

Moreover, the scaled trace can be written as

### Proof

An elementary computation yields for any $(L,R)$ the expression

Noting that for any ${(L,R)} \in \mathcal{S}$ the first term on the right is zero yields the claimed expression (15. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")). Next, we verify (16. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")) by a direct calculation. To this end, the definition of the scaled trace yields the expression

Let us analyze the second term on the right. Letting $A_{l,i}$ denote the $i$'th column of $A_{l}$, we compute

A similar argument shows $\left\| {D_{2}R} \right\|_{\text{F}}^{2} = {\frac{1}{md_{1}}{\sum_{i = 1}^{d_{1}}{\sum_{j = 1}^{k}\left\| {\mathcal{A}{({e_{i}e_{j}^{\top}R^{\top}})}} \right\|_{2}^{2}}}}$, completing the proof. ∎

In particular, Lemma 3.1. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") implies that flat solutions are exactly the minimizers of the problem

In turn, it follows directly from that so long as $D_{1}$, $D_{2}$ are invertible, the problem is equivalent to minimizing the nuclear norm over rank constrained matrices:

Therefore, a natural convex relaxation for finding the flattest solution drops the rank constraint:

The following theorem summarizes these observations.

### Theorem 3.2 (Convex relaxation)

Suppose the matrices $D_{1}$ and $D_{2}$ are invertible. Then the problems are are equivalent in the following sense. Let $l = {\min{(k,d_{\min})}}$.

the optimal values of and are equal,

if $L,R$ solves, then $X = {D_{1}LR^{\top}D_{2}}$ is a minimizer of.

if a solution $X$ of has a singular value decomposition $X = {U\SigmaV^{\top}}$ for some diagonal matrix $\Sigma \in^{l \times l}$ with nonnegative entries, then the matrices $L = {D_{1}^{- 1}U\sqrt{\Sigma}}$ and $R = {D_{2}^{- 1}V\sqrt{\Sigma}}$ are minimizers of when $l \geq k$, and the matrices $L = {\lbrack{D_{1}^{- 1}U\sqrt{\Sigma}},0_{d_{1},{({k - l})}}\rbrack}$ and $R = {\lbrack{D_{2}^{- 1}V\sqrt{\Sigma}},0_{d_{2},{({k - l})}}\rbrack}$ are minimizers of when $l < k$.

Moreover, if $X = {D_{1}M_{\natural}D_{2}}$ is the unique minimizer of the problem, then any flat solution $(L,R)$ satisfies ${LR^{\top}} = M_{\natural}$.

### Proof

The three claims follow directly from making a variable substitution $L^{\prime} = {D_{1}L}$ and $R^{\prime} = {D_{2}R}$ and using. The "moreover" part follows from being a convex relaxation of. ∎

Section 4 will verify that the convex relaxation indeed recovers $M_{\natural}$ under restricted isometry properties on the measurement map $\mathcal{A}$, and therefore flat solutions exactly recover $M_{\natural}$.

### Regularity of flat solutions

In this section, we show that the condition numbers of the rescaling matrices $D_{1}$ and $D_{2}$ determine balancedness and norm minimality of flat solutions. The main result is the following theorem.

### Theorem 3.3 (Regularity of flat solutions)

Suppose that there exist constants ${\alpha_{1},\alpha_{2}} > 0$ satisfying ${\alpha_{1}I} \preceq D_{i} \preceq {\alpha_{2}I}$ for each $i \in {\{ 1,2\}}$. Define the constant $\kappa:=\frac{\alpha_{2}}{\alpha_{1}}$. Then any flat solution $(L_{f},R_{f})$ of satisfies the following properties.

Norm-minimal: the pair $(L_{f},R_{f})$ is approximately norm-minimal:

Balanced: The pair $(L_{f},R_{f})$ is approximately balanced:

The proof of Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") relies on the following simple linear algebraic lemma.

### Lemma 3.4

Consider two symmetric matrices $Q_{1} \in {\mathbb{R}}^{d_{1} \times d_{1}}$ and $Q_{2} \in {\mathbb{R}}^{d_{2} \times d_{2}}$. Suppose that there exist constants ${\alpha_{1},\alpha_{2}} > 0$ satisfying ${\alpha_{1}I} \preceq Q_{i} \preceq {\alpha_{2}I}$ for each $i \in {\{ 1,2\}}$. Define the constant $\kappa = \frac{\alpha_{2}}{\alpha_{1}}$. Then given any matrix $X \in {\mathbb{R}}^{d_{1} \times d_{2}}$, any minimizer $(L,R)$ of the problem

satisfies the inequality:

### Proof

Lemma 2.2. ‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery") implies that the pair $({Q_{1}L},{Q_{2}R})$ is balanced, meaning ${L^{\top}Q_{1}^{2}L} = {R^{\top}Q_{2}^{2}R}$. Hence, we may decompose ${L^{\top}L} - {R^{\top}R}$ in the following way:

We bound the first term on the right as follows,

Here, $(a)$ and $(b)$ follow, respectively, from the basic inequalities: $\left\| {FG} \right\|_{\ast} \leq {\left\| F \right\|_{\text{F}}\left\| G \right\|_{\text{F}}}$ and ${\|{FG}\|}_{F} \leq {\left\| F \right\|_{\text{op}}\left\| G \right\|_{\text{F}}}$, which hold for all matrices $F$ and $G$ with compatible dimensions. A similar argument yields the inequality

The claimed estimate follows immediately. ∎

We are now ready to prove Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery").

### Proof of Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")

We first prove inequality (22. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")). To this end, for any ${(L,R)} \in \mathcal{S}$, we successively estimate:

where the second inequality follows from the characterization of flat solutions. Taking the infimum over pairs ${(L,R)} \in \mathcal{S}$ completes the proof of (22. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")).

We next verify (23. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")). To this end, define the matrix $X:={D_{1}L_{f}R_{f}^{\top}D_{2}}$. Then clearly $(L_{f},R_{f})$ is a minimizer of the problem

Lemma 3.4 therefore guarantees the estimate

The already established estimate (22. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")) ensures

In particular, minimizing the right hand-side over $L,R$ satisfying $M_{\natural} = {LR^{\top}}$ yields an upper bound of $2\kappa^{2}\left\| M_{\natural} \right\|_{\ast}$. The proof is complete. ∎

## Flat minima under RIP conditions: matrix and bilinear sensing

The previous section motivates a two-part strategy for showing that flat minima exactly recover the ground truth (Theorem 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")) and are automatically nearly balanced and nearly norm-minimal (Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")). The first step is to argue that the convex relaxation admits $D_{1}M_{\natural}D_{2}$ as its unique minimizer. The second step is to argue that the condition numbers of the matrices $D_{1}$ and $D_{2}$ are close to one. In this section, we follow this recipe for problems satisfying $\ell_{2}/\ell_{2}$ and $\ell_{1}/\ell_{2}$ restricted isometry properties (defined below). The main two examples will be the following random ensembles.

### Definition 4.1 (Matrix and bilinear sensing)

We introduce the following definitions.

We say that $\mathcal{A}$ is a Gaussian ensemble if the entries of $A_{i}$ are i.i.d standard normal random variables $N{}$.

We say that $\mathcal{A}$ is a Gaussian bilinear ensemble if the matrices $A_{i}$ take the form $A_{i} = {a_{i}b_{i}^{\top}}$ where the entries of $a_{i}$ and $b_{i}$ are i.i.d. standard normal random variables $N{}$

The main results of the section is the following theorem, stated here informally.

### Theorem 4.2 (Matrix and bilinear sensing (Informal))

Suppose we are in one of the settings:

$\mathcal{A}$ is a Gaussian ensemble and $m \gtrsim {r_{\natural}d_{\max}}$,

$\mathcal{A}$ is a Gaussian bilinear ensemble, $m \gtrsim {r_{\natural}d_{\max}}$, and $d_{\min} \gtrsim {\log m}$.

Then with high probability, any flat solution $(L_{f},R_{f})$ of satisfies ${{L_{f}R_{f}^{\top}} = M_{\natural}},$ and is nearly norm-minimal and nearly balanced:

We begin by formally defining the restricted isometry property of a measurement map $\mathcal{A}{( \cdot )}$.

### Definition 4.3 (Restricted isometry property)

A linear map $\mathcal{A}:{}_{}^{d_{1} \times d_{2}}^{m}$ satisfies an $\ell_{p}/\ell_{2}$ restricted isometry property (RIP) with parameters $(r,\delta_{1},\delta_{2})$ if the estimate

holds for all matrices $X \in^{d_{1} \times d_{2}}$ with rank at most $r$.

In this paper we will be primarily interested in $\ell_{2}/\ell_{2}$ and $\ell_{1}/\ell_{2}$ restricted isometry properties. In particular, the two random measurement models in Theorem 4.2). ‣ 4 Flat minima under RIP conditions: matrix and bilinear sensing ‣ Flat minima generalize for low-rank matrix recovery") satisfy these two properties. The following two lemmas are from (candes2011tight Theorem 2.3), (recht2010guaranteed Theorem 4.2), and (cai2015rop Theorem 2.2).

### Lemma 4.4 ($\ell_{2}/\ell_{2}$ RIP in matrix sensing)

Let $\mathcal{A}$ be a Gaussian ensemble. Then for any $\delta \in {}$, there exist constants ${c,C} > 0$ depending only on $\delta$ such that as long as $m \geq {cr{({d_{1} + d_{2}})}}$, with probability at least $1 - {\exp{({- {Cm}})}}$, the linear map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ RIP with parameters $({2r},{1 - \delta},{1 + \delta})$.

### Lemma 4.5 ($\ell_{1}/\ell_{2}$ RIP in bilinear sensing)

Let $\mathcal{A}$ be a Gaussian bilinear ensemble. For any positive integer $k \geq 2$, there exist constants ${c,C} > 0$ depending only on $k$ and numerical constants ${\delta_{1},\delta_{2}} > 0$ and such that in the regime $m \geq {cr{({d_{1} + d_{2}})}}$, with probability at least $1 - {\exp{({- {Cm}})}}$, the measurement map $\mathcal{A}$ satisfies $\ell_{1}/\ell_{2}$ RIP with parameters $({kr},\delta_{1},\delta_{2})$.

Our goal is to show that under RIP conditions, with reasonable parameters, flat solutions exactly recover the ground truth $M_{\natural}$. We will need the following lemma, whose proof is immediate from definitions.

### Lemma 4.6

Let $\mathcal{A}{( \cdot )}$ be a linear map satisfying an $\ell_{p}/\ell_{2}$ RIP with parameters $(r,\delta_{1},\delta_{2})$. Let $Q_{1},Q_{2}$ be two positive definite matrices satisfying ${\alpha_{1}I} \preceq Q_{i} \preceq {\alpha_{2}I}$ for all $i \in {\{ 1,2\}}$ for some ${\alpha_{1},\alpha_{2}} > 0$. Then the linear map $\mathcal{B}{( \cdot )}: = \mathcal{A}{(Q_{1}^{- 1} \cdot Q_{2}^{- 1})}$ satisfies an $\ell_{p}/\ell_{2}$ RIP with parameters $(r,{\alpha_{2}^{- 2}\delta_{1}},{\alpha_{1}^{- 2}\delta_{2}})$.

The following lemma will be our main technical tool; it establishes that if $\mathcal{A}{( \cdot )}$ satisfies RIP, then so does the perturbed map ${\mathcal{B}{( \cdot )}} = {\mathcal{A}{({Q_{1}^{- 1} \cdot Q_{2}^{- 1}})}}$, provided that the condition numbers of the positive definite matrices $Q_{1}$ and $Q_{2}$ are sufficiently close to one.

### Lemma 4.7

Consider two positive definite matrices $Q_{1},Q_{2}$ and constants ${\alpha_{1},\alpha_{2}} > 0$ satisfying ${\alpha_{1}I} \preceq Q_{i} \preceq {\alpha_{2}I}$ for each $i \in {\{ 1,2\}}$. Define $\kappa = {\alpha_{2}/\alpha_{1}}$ and let $\mathcal{A}{( \cdot )}$ be a linear map satisfying one of the following conditions.

The map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ RIP with parameters $({5r_{\natural}},\delta_{1},\delta_{2})$, where $\delta_{1} \geq \frac{9}{10}$ and ${\delta_{2}\kappa^{2}} \leq \frac{11}{10}$.

The map $\mathcal{A}$ satisfies $\ell_{1}/\ell_{2}$ RIP with parameters $({lr_{\natural}},\delta_{1},\delta_{2})$, where $\frac{\delta_{2}\kappa^{2}}{\delta_{1}} < \sqrt{l}$.

Then $Q_{1}M_{\natural}Q_{2}$ is the unique solution of the following convex program

### Proof

Define the map ${\mathcal{B}{(Z)}} = {\alpha_{2}^{2}\mathcal{A}{({Q_{1}^{- 1}ZQ_{2}^{- 1}})}}$. Then Lemma 4.6 implies that $\mathcal{B}$ in the first case satisfies $\ell_{2}/\ell_{2}$ RIP with parameters $({5r_{\natural}},\delta_{1},{\delta_{2}\kappa^{2}})$ and in the second case satisfies $\ell_{1}/\ell_{2}$ RIP with parameters $({lr_{\natural}},\delta_{1},{\delta_{2}\kappa^{2}})$. An application of (recht2010guaranteed Theorem 3.3) in the first case and (cai2015rop Theorem 2.1) in the second guarantees that $Q_{1}M_{\natural}Q_{2}$ is the unique solution of, as claimed. ∎

It remains to estimate the condition number $\kappa$ of the matrices $D_{1}$ and $D_{2}$ defined in under RIP (or statistical assumptions). The following lemma shows that $D_{1}$ and $D_{2}$ are automatically well conditioned under $\ell_{2}/\ell_{2}$ RIP.

### Lemma 4.8 (Conditioning of $D_{i}$ under $\ell_{2}/\ell_{2}$ RIP)

Suppose that the linear map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ RIP with parameters $(1,\delta_{1},\delta_{2})$. Then the relation ${\delta_{1}I_{d_{i}}} \preceq D_{i} \preceq {\delta_{2}I_{d_{i}}}$ holds for all $i \in {\{ 1,2\}}$

### Proof

In the proof of Lemma 3.1. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") (equation ), we actually showed the expression:

Now for any vector $v \in^{d_{1}}$, we can take the matrix $L = {\lbrack v,0_{d_{1},{k - 1}}\rbrack}$ in the above equation. Appealing to the $\ell_{2}/\ell_{2}$ RIP condition on $\mathcal{A}$, we deduce

A similar argument shows that $D_{2}$ satisfies the analogous inequality with $v \in^{d_{2}}$. ∎

The $\ell_{1}/\ell_{2}$ RIP property does not in general imply a good bound on the condition numbers of $D_{1}$ and $D_{2}$. Instead we will directly show that under the Gaussian design for bilinear sensing, the matrices $D_{1}$ and $D_{2}$ are well-conditioned. This is the content of the following lemma.

### Lemma 4.9 (Conditioning of $D_{i}$ for bilinear sensing)

Let $\mathcal{A}$ be a Gaussian bilinear ensemble. Then there exist constant ${c_{1},c_{2},c_{3},c_{4}} > 0$ such that for any $\delta \in {}$ as long as we are in the regime $m \geq \frac{c_{3}d_{\max}}{\delta^{2}}$ and ${\log{(m)}} \leq {c_{4}\delta^{2}d_{\min}}$, the estimate holds:

### Proof

First observe ${A_{i}A_{i}^{\top}} = {{\| b_{i}\|}_{2}^{2}a_{i}a_{i}^{\top}}$ for each index $i$. Bernstein's inequality (vershynin2018high Theorem 2.8.3) implies

Taking a union bound, we can therefore be sure that with probability at least $1 - {m{\exp{({- {c_{1}d_{2}\delta^{2}}})}}}$ the estimate

holds simultaneously for all $i = {1,\ldots,m}$. In this event, we estimate

Therefore, after summing for $i = {1,\ldots,m}$ we deduce

Concentration of covariance matrices (vershynin2018high Exercise 4.7.3) in turn implies that the estimate

holds with probability at least $1 - {2{\exp{({- u})}}}$. Taking a union bound, we therefore deduce

holds with probability at least $1 - {m{\exp{({- {c_{1}d_{2}\delta^{2}}})}}} - {2{\exp{({- u})}}}$. Setting $u = d_{1}$, we see that there is a constant $c_{3}$ such that as long as $m \geq {c_{3}\frac{\max{\{ d_{1},d_{2}\}}}{\delta^{2}}}$, we have

with probability at least $1 - {m{\exp{({- {c_{1}d_{2}\delta^{2}}})}}} - {2{\exp{({- d_{1}})}}}$. The result follows. ∎

The following are the two main results of the section.

### Theorem 4.10 (Exact recovery in matrix sensing)

Suppose that $\mathcal{A}$ is a Gaussian ensemble. Then there exists a constant $c_{0}$ such that the following hold for any $\delta \in {(0,c_{0})}$. There exist constants ${c,C} > 0$ depending only on $\delta$ such that in the regime $m \geq {cr_{\natural}{({d_{1} + d_{2}})}}$, with probability at least $1 - {\exp{({- {Cm}})}}$, any flat solution $(L_{f},R_{f})$ of satisfies ${L_{f}R_{f}^{\top}} = M_{\natural}$ and is automatically nearly norm-minimal and nearly balanced:

### Proof

Lemma 4.4. ‣ 4 Flat minima under RIP conditions: matrix and bilinear sensing ‣ Flat minima generalize for low-rank matrix recovery") shows that for any $\delta \in {}$, there exist constants ${c_{1},C_{1}} > 0$ depending only on $\delta$ such that as long as $m \geq {c_{1}r{({d_{1} + d_{2}})}}$, with probability at least $1 - {\exp{({- {C_{1}m}})}}$, the linear map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ RIP with parameters $(r,{1 - \delta},{1 + \delta})$. In this event, Lemma 4.8. ‣ 4 Flat minima under RIP conditions: matrix and bilinear sensing ‣ Flat minima generalize for low-rank matrix recovery") ensures that the condition number $\kappa$ of $D_{1}$ and $D_{2}$ is bounded by $\frac{1 + \delta}{1 - \delta}$. Set now $r = {5r_{\natural}}$ and choose any $\delta \leq 0.1$ satisfying ${{({1 + \delta})}\left( \frac{1 + \delta}{1 - \delta} \right)^{2}} \leq \frac{11}{10}$. An application of Lemma 4.7 and Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") completes the proof. ∎

### Theorem 4.11 (Exact recovery in bilinear sensing)

Suppose that $\mathcal{A}$ is a Gaussian bilinear ensemble. Then for any $\delta \in {}$ there exist numerical constants ${c,C,c_{1},c_{2},c_{3},c_{4}} > 0$ depending only on $\delta$ such that in the regime $m \geq {cr_{\natural}{({d_{1} + d_{2}})}}$ and ${\log{(m)}} \leq {c_{4}d_{\min}}$, with probability at least $1 - {c_{3}{\exp{({- {Cd_{\min}}})}}}$ any flat solution $(L_{f},R_{f})$ of satisfies ${L_{f}R_{f}^{\top}} = M_{\natural}$ and is automatically nearly norm-minimal and nearly balanced:

### Proof

For any integer $k \in {\mathbb{N}}$, Lemma 4.5. ‣ 4 Flat minima under RIP conditions: matrix and bilinear sensing ‣ Flat minima generalize for low-rank matrix recovery") ensures that there exist numerical constants ${\delta_{1},\delta_{2}} > 0$ and constants ${c_{0},C_{0}} > 0$ depending only on $l$ such that in the regime $m \geq {c_{0}r{({d_{1} + d_{2}})}}$, with probability at least $1 - {\exp{({- {C_{0}m}})}}$, the measurement map $\mathcal{A}$ satisfies $\ell_{1}/\ell_{2}$ RIP with parameters $({lr_{\natural}},\delta_{1},\delta_{2})$. Lemma 4.9. ‣ 4 Flat minima under RIP conditions: matrix and bilinear sensing ‣ Flat minima generalize for low-rank matrix recovery") in turn ensures there exist numerical constant ${c_{5},c_{6},c_{7},c_{8}} > 0$ such that for any $\delta \in {}$ as along as we are in the regime, $m \geq \frac{c_{7}d_{\max}}{\delta^{2}}$ and ${\log{(m)}} \leq {c_{8}\delta^{2}d_{\min}}$, the estimate holds:

Therefore in this regime, we may upper bound the condition number $\kappa$ of $D_{1}$ and $D_{2}$ by $\frac{1 + \delta}{1 - \delta}$. In light of Lemma 4.7, in order to ensure exact recovery, it remains to simply choose a large enough $l$ such that the inequality ${\frac{\delta_{2}}{\delta_{1}} \cdot {(\frac{1 + \delta}{1 - \delta})}^{2}} \leq \sqrt{l}$ holds (recall $\delta_{1},\delta_{2}$ are numerical constants). An application of Lemma 4.7 and Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") completes the proof. ∎
