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

In parallel, empirical evidence hochreiter1997flat; Keskar2016; li2017visualizing strongly suggests that those models around which the landscape is flat---meaning the training loss grows slowly---generalize well. See Figure 1 for an illustration of flat and sharp minima. Inspired by this observation, a variety of algorithms have been proposed to explicitly bias the iterates towards flat solutions chaudhari2019entropy; izmailov2018averaging; norton2021diametrical; foret2020sharpness, with impressive observed performance. In contrast to the magnitude of the weights, the theoretic basis for flatness is much less clear even for simple overparameterized nonlinear problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

> Do flat minimizers generalize for a broad family of overparameterized problems?

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Putting generalization aside, one would hope that flat solutions are in some sense regular, occurring in a benign region where algorithms perform well. For example, numerical methods for neural network training are strongly influenced by how balanced the parameters appear. Namely, the set of interpolating neural networks contains models with consecutive weight matrices that are poorly scaled relative to each other du2018algorithmic; shamir2018resnets. It has recently been shown that gradient descent in continuous time keeps the factors balanced ye2021global; ma2021beyond for matrix factorization and for deep learning du2018algorithmic; mulayoff2020unique. Despite ubiquity of the three notions discussed so far---small norm, flatness, and balancedness---the exact relationship between them is unclear.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Are flat minimizers nearly norm-minimal and nearly balanced\
for a broad family of overparameterized problems?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

We answer both questions in the setting of low-rank matrix factorization---a prototypical problem class often used to gain insight into more general deep learning models li2018algorithmic; du2018algorithmic; ye2021global. Setting the stage, consider a ground truth matrix $M_{\natural} \in^{d_{1} \times d_{2}}$ with rank $r_{\natural}$. The goal is to recover $M_{\natural}$ from the observed measurements $b = {\mathcal{A}{(M_{\natural})}}$ under a linear measurement map $\mathcal{A}:{}_{}^{d_{1} \times d_{2}}^{m}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

The set of minimizers of $f$, which we denote by $\mathcal{S}$, consists of all solutions to the equation ${\mathcal{A}{({LR^{\top}})}} = b$. In order to model overparameterization, we focus on the rank-overparameterized setting $k \geq r_{\natural}$; indeed $k$ can be arbitrarily large. The three notions discussed so for can be formally defined for pairs ${(L,R)} \in \mathcal{S}$ as follows.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

$(L,R)$ is flat if it minimizes over $\mathcal{S}$ the "scaled trace" of the Hessian, $\text{str}{({D^{2}f{(L,R)}})}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

Thus being norm-minimal means that $(L,R)$ is the closest pair from $\mathcal{S}$ to the origin in Frobenius norm. Being balanced amounts to requiring $L$ and $R$ to have the same singular values and right-singular vectors. Flat solutions are defined in terms of the "scaled trace" of the bilinear form $D^{2}f{(L,R)}$ defined as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

where $e_{i}$ and $e_{j}$ are the unit coordinate vectors in ${\mathbb{R}}^{d_{1} + d_{2}}$ and ${\mathbb{R}}^{k}$, respectively. In the square setting $d_{1} = d_{2} = d$, the scaled trace reduces to the usual trace divided by $d$. The scaled trace appears to have not been used previously in the literature, but is important in order to account for a possible mismatch in the dimension of the $L$ and $R$ factors. A number of recent papers use the trace of the Hessian to measure flatness (e.g. dinh2017sharp ). Other alternatives are possible, such as the maximal eigenvalue dinh2017sharp; mulayoff2020unique or the condition number liu2021noisy, but we do not focus on them here.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

For various statistical models, flat solutions of exactly recover $M_{\natural}$.\
Moreover, flat solutions have nearly minimal norm and are almost balanced.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem setting: overparameterized matrix factorization", "weight": 1.0} -->

The exact recovery guarantee may be striking at first because flat solutions are distinct from minimal norm solutions, and thus do not correspond to nuclear norm minimization over $\mathcal{S}$. Yet, our main result shows that flat solutions do exactly recover the ground truth $M_{\natural}$ under standard statistical assumptions. The precise statistical models for which this is the case are matrix and bilinear sensing, robust PCA (or PCA with outliers), covariance matrix estimation, and single hidden layer neural networks with quadratic activation functions. Moreover, we prove weak recovery for the matrix completion problem, though our numerical experiments suggest that exact recovery holds here as well.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

We next outline our main results and the arguments that underpin them. We begin in Section 2 with the idealized "population level" setting where $\mathcal{A}$ is the identity map. In this case, we show that there is no distinction between flat, norm-minimal, and balanced solutions. As soon as $\mathcal{A}$ deviates from the identity, however, all three notions become distinct in general.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

An immediate difficulty with analyzing flat solutions of the problem with a general measurement map $\mathcal{A}$ is that flat solutions are defined as minimizers of a highly nonconvex optimization problem corresponding to minimizing the scaled trace over the solution set. In Section 3, we derive a simple convex relaxation of flat minimizers. Setting the notation, let us write $\mathcal{A}$ as ${\mathcal{A}{(X)}} = {({\langle A_{i},X\rangle},\ldots,{\langle A_{m},X\rangle})}$ for some matrices $A_{i} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ and define the "rescaling" matrices

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

We will show in Theorem 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") that flat solutions can be identified with minimizers of the problem

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

It is worthwhile to note that without the $D_{1}$ and $D_{2}$ matrices and without the rank constraint, the problem is classically known to characterize norm-minimal solutions and is known as nuclear norm minimization. Herein, we already see the distinction between the two solution concepts.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

Summarizing, verifying that flat solutions exactly recover $M_{\natural}$ is reduced to showing that $M_{\natural}$ (which has rank $r_{\natural}$) is the unique solution of the convex problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Main results and outline of the paper", "weight": 1.0} -->

In Section 4, we will show that if the linear map $\mathcal{A}$ satisfies $\ell_{2}/\ell_{2}$ or $\ell_{1}/\ell_{2}$ restricted isometry properties (RIP) and the rescaling matrices $D_{1}$ and $D_{2}$ are sufficiently close to the identity, then $M_{\natural}$ is the unique solution of. As a consequence, we deduce that flat solutions exactly recover $M_{\natural}$ for matrix sensing recht2010guaranteed; candes2011tight and bilinear sensing ling2015self; ahmed2013blind problems with Gaussian design.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Norm-minimal, flat, and balanced solutions with an identity measurement map", "weight": 1.0} -->

Recall that $M_{\natural} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ is a rank $r_{\natural}$ matrix, $k \geq r_{\natural}$ is arbitrary, and the set of minimizers $\mathcal{S}$ of coincides with the solution set of the equation ${LR^{\top}} = M_{\natural}$. We will show in this section that in this setting there is no distinction between norm-minimal, flat, and balanced solutions. As soon as the measurement map $\mathcal{A}$ is not the identity, the three notions become distinct; this remains true even under standard statistical models as our numerical experiments show. Nonetheless, the simplified setting $\mathcal{A} = \mathcal{I}$ explored in this section will serve as motivation for the rest of the paper.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Norm-minimal, flat, and balanced solutions with an identity measurement map", "weight": 1.0} -->

We begin with the following lemma that provides a convenient expression for $\text{str}{({D^{2}f{(L,R)}})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convex relaxation and regularity of flat solutions", "weight": 1.0} -->

In this section, we begin investigating flat minimizers of the problem with general linear measurement maps $\mathcal{A}$. It will be convenient to write the linear map $\mathcal{A}{(X)}$ in coordinates as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convex relaxation and regularity of flat solutions", "weight": 1.0} -->

The section presents two main results: Theorems 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") and 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery"). The former presents a convex relaxation for verifying that a solution is flat, while the latter shows that flat solutions are nearly balanced and nearly norm-minimal, whenever the matrices $D_{1}$ and $D_{2}$ are well-conditioned.

<!-- chunk {"id": "body-0027", "role": "body", "section": "A convex relaxation for flat solutions", "weight": 1.0} -->

Flat solutions are by definition minimizers of the highly nonconvex problem ${{\min_{{(L,R)} \in \mathcal{S}}\text{str}}{({D^{2}f{(L,R)}})}}.$ The main result of this section is to present an appealing convex relaxation of this problem. We begin with a convenient expression for the scaled trace $\text{str}{({D^{2}f{(L,R)}})}$. Namely, recall that Lemma 2.1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "A convex relaxation for flat solutions", "weight": 1.0} -->

‣ 2 Norm-minimal, flat, and balanced solutions with an identity measurement map ‣ Flat minima generalize for low-rank matrix recovery") showed the equality ${\text{str}{({D^{2}f{(L,R)}})}} = {{2\left\| L \right\|_{\text{F}}^{2}} + {2\left\| R \right\|_{\text{F}}^{2}}}$ in the simplified setting $\mathcal{A} = \mathcal{I}$. Lemma 3.1. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery") provides an analogous statement for general maps $\mathcal{A}$ up to rescaling the factors by $D_{1}$ and $D_{2}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Regularity of flat solutions", "weight": 1.0} -->

In this section, we show that the condition numbers of the rescaling matrices $D_{1}$ and $D_{2}$ determine balancedness and norm minimality of flat solutions. The main result is the following theorem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Flat minima under RIP conditions: matrix and bilinear sensing", "weight": 1.0} -->

The previous section motivates a two-part strategy for showing that flat minima exactly recover the ground truth (Theorem 3.2. ‣ 3.1 A convex relaxation for flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")) and are automatically nearly balanced and nearly norm-minimal (Theorem 3.3. ‣ 3.2 Regularity of flat solutions ‣ 3 Convex relaxation and regularity of flat solutions ‣ Flat minima generalize for low-rank matrix recovery")). The first step is to argue that the convex relaxation admits $D_{1}M_{\natural}D_{2}$ as its unique minimizer. The second step is to argue that the condition numbers of the matrices $D_{1}$ and $D_{2}$ are close to one. In this section, we follow this recipe for problems satisfying $\ell_{2}/\ell_{2}$ and $\ell_{1}/\ell_{2}$ restricted isometry properties (defined below). The main two examples will be the following random ensembles.
