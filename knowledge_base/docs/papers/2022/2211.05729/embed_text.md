## Introduction

Modern deep nets are often overparametrized and have the capacity to fit even randomly labeled data. Thus, a small training loss does not necessarily imply good generalization. Yet, standard gradient-based training algorithms such as SGD are able to find generalizable models. Recent empirical and theoretical studies suggest that generalization is well-correlated with the sharpness of the loss landscape at the learned parameter. Partly motivated by these studies, Foret et al.; Wu et al.; Zheng et al.; Norton & Royset propose to penalize the sharpness of the landscape to improve the generalization. We refer this method to *Sharpness-Aware Minimization* (SAM) and focus on the version of Foret et al. in this paper.

Despite its empirical success, the underlying working of SAM remains elusive because of the various intriguing approximations made in its derivation and analysis. There are three different notions of sharpness involved --- SAM intends to optimize the first notion, the sharpness along the worst direction, but actually implements a computationally efficient notion, the sharpness along the direction of the gradient. But in the analysis of generalization, a third notion of sharpness is actually used to prove generalization guarantees, which admits the first notion as an upper bound. The subtle difference between the three notions can lead to very different biases (see Figure 1 for demonstration).

More concretely, let $L$ be the training loss, $x$ be the parameter and $\rho$ be the *perturbation radius*, a hyperparameter requiring tuning. The first notion corresponds to the following optimization problem, where we call ${R_{\rho}^{\text{Max}}{(x)}} = {{L_{\rho}^{\text{Max}}{(x)}} - {L{(x)}}}$ the *worst-direction sharpness* at $x$. SAM intends to minimize the original training loss plus the worst-direction sharpness at $x$.

However, even evaluating $L_{\rho}^{\text{Max}}{(x)}$ is computationally expensive, not to mention optimization. Thus Foret et al.; Zheng et al. have introduced a second notion of sharpness, which approximates the worst-case direction in by the direction of gradient, as defined below in. We call ${R_{\rho}^{\text{Asc}}{(x)}} = {{L_{\rho}^{\text{Asc}}{(x)}} - {L{(x)}}}$ the *ascent-direction sharpness* at $x$.

For further acceleration, Foret et al.; Zheng et al. omit the gradient through other occurrence of $x$ and approximate the gradient of ascent-direction sharpness by gradient taken after one-step ascent, *i.e.*, ${{\nabla L_{\rho}^{\text{Asc}}}{(x)}} \approx {{\nabla L}\left( {x + {\rho\frac{{\nabla L}{(x)}}{\left\| {{\nabla L}{(x)}} \right\|_{2}}}} \right)}$ and derive the update rule of SAM, where $\eta$ is the learning rate.

Intriguingly, the generalization bound of SAM upperbounds the generalization error by the third notion of sharpness, called *average-direction sharpness*, $R_{\rho}^{\text{Avg}}{(x)}$ and defined formally below.

The worst-case sharpness is an upper bound of the average case sharpness and thus it is a looser bound for generalization error. In other words, according to the generalization theory in Foret et al.; Wu et al. in fact motivates us to directly minimize the average case sharpness (as opposed to the worst-case sharpness that SAM intends to optimize).

​​Type of Sharpness-Aware Loss
​​​​ Biases (among minimizers)

$L\left( {x + {\rho\frac{{\nabla L}{(x)}}{\left\| {{\nabla L}{(x)}} \right\|_{2}}}} \right)$
minxλmin (∇2L (x)) (Thm E.4)

${\mathbb{E}}_{g \sim {N{(0,I)}}}L{({x + {\rho\frac{g}{\left\| g \right\|_{2}}}})}$

Table 1: Definitions and biases of different notions of sharpness-aware loss. The corresponding sharpness is defined as the difference between sharpness-aware loss and the original loss. Here λ1 denotes the largest eigenvalue and λmin denotes the smallest non-zero eigenvalue.

In this paper, we analyze the biases introduced by penalizing these various notions of sharpness as well as the bias of SAM (Equation 3). Our analysis for SAM is performed for small perturbation radius $\rho$ and learning rate $\eta$ under the setting where the minimizers of loss form a manifold following the setup of Fehrman et al.; Li et al.. In particular, we make the following theoretical contributions.

We prove that full-batch SAM indeed minimizes worst-direction sharpness. (Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"))

Surprisingly, when batch size is 1, SAM minimizes average-direction sharpness. (Theorem 5.4)​

We provide a characterization (Theorems 4.2 and 5.3) of what a few sharpness regularizers bias towards among the minimizers (including all the three notions of the sharpness in Table 1), when the perturbation radius $\rho$ goes to zero. Surprisingly, both heuristic approximations made for SAM lead to inaccurate conclusions: Minimizing worst-direction sharpness and ascent-direction sharpness induce different biases among minimizers, and SAM doesn't minimize ascent-direction sharpness.

The key mechanism behind this bias of SAM is the alignment between gradient and the top eigenspace of Hessian of the original loss in the latter phase of training---the angle between them decreases gradually to the level of $O{(\rho)}$. It turns out that the worst-direction sharpness starts to decrease once such alignment is established (see Section 4.3). Interestingly, such an alignment is not implied by the minimization problem, but rather, it is an implicit property of the specific update rule of SAM. Interestingly, such an alignment property holds for SAM with full batch and SAM with batch size one, but does not necessarily hold for the mini-batch case.

## Related Works

Figure 1: Visualization of the different biases of different sharpness notions on a 4D-toy example. Let F1, F2: ℝ2 → ℝ+ be two positive functions satisfying that F1 &gt; F2 on 2. For x ∈ ℝ4, consider loss L (x) = F1 (x1,x2) x32 + F2 (x1,x2) x42. The loss L has a zero loss manifold {x3 = x4 = 0} of codimension M = 2 and the two non-zero eigenvalues of ∇2L of any point x on the manifold are λ1 (∇2L (x)) = F1 (x1,x2) and λ2 (∇2L (x)) = F2 (x1,x2). We test three optimization algorithms on this 4D-toy model with small learning rates. They all quickly converge to zero loss, i.e., x3 (t), x4 (t) ≈ 0, and after that x1 (t), x2 (t) still change slowly, i.e., moving along the zero loss manifold. We visualize the loss restricted to (x3,x4) as the 3D shape at various (x1,x2)’s where x1 = x1 (t), x2 = x2 (t) follows the trajectories of the three algorithms. In other words, each of the 3D surface visualize the function g (x3,x4) = L (x1 (t),x2 (t),x3,x4). As our theory predicts, Full-batch SAM (Equation 3) finds the minimizer with the smallest top eigenvalue, F1 (x1,x2); GD on ascent-direction loss LρAsc (Equation 2) finds the minimizer with the smallest bottom eigenvalue, F2 (x1,x2); 1-SAM (Equation 17) (with L0 (x) = F1 (x1,x2) x32 and L1 (x) = F2 (x1,x2) x42) finds the minimizer with the smallest trace of Hessian, F1 (x1,x2) + F2 (x1,x2). See more details in Appendix A.

### Sharpness and Generalization

The study on the connection between sharpness and generalization can be traced back to Hochreiter & Schmidhuber. Keskar et al. observe a positive correlation between the batch size, the generalization error, and the sharpness of the loss landscape when changing the batch size. Jastrzebski et al. extend this by finding a correlation between the sharpness and the ratio between learning rate to batch size. Dinh et al. show that one can easily construct networks with good generalization but with arbitrary large sharpness by reparametrization. Dziugaite & Roy; Neyshabur et al.; Wei & Ma give theoretical guarantees on the generalization error using sharpness-related measures. Jiang et al. perform a large-scale empirical study on various generalization measures and show that sharpness-based measures have the highest correlation with generalization.

### Background on Sharpness-Aware Minimization

Foret et al.; Zheng et al. concurrently propose to minimize the loss at the perturbed from current parameter towards the worst direction to improve generalization. Wu et al. propose an almost identical method for a different purpose, robust generalization of adversarial training. Kwon et al. propose a different metric for SAM to fix the rescaling problem pointed out by Dinh et al.. Liu et al. propose a more computationally efficient version of SAM. Zhuang et al. proposes a variant of SAM, which improves generalization by simultaneously optimizing the surrogate gap and the sharpness-aware loss. Zhao et al. propose to improve generalization by penalizing gradient norm. Their proposed algorithm can be viewed as a generalization of SAM. Andriushchenko & Flammarion study a variant of SAM where the step size of ascent step is $\rho$ instead of $\frac{\rho}{\left\| {{\nabla L}{(x)}} \right\|_{2}}$. They show that for a simple model this variant of SAM has a stronger regularization effect when batch size is 1 compared to the full-batch case and argue that this might be the explanation that SAM generalizes better with small batch sizes.

In a concurrent work, Bartlett et al. prove that on quadratic loss, the iterate of SAM (Equation 13) and its gradient converges to the top eigenvector of Hessian, which is almost the same as our Theorem 4.8. Assuming such alignment for a general loss, the work of Bartlett et al. shows that the largest eigenvalue of Hessian decreases in the next step. This paper also proves such a Hessian-gradient alignment for general loss functions (Lemma G.19 ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) and an end-to-end theorem showing that the largest eigenvalue of Hessian and worst-direction sharpness decrease along the trajectory of SAM (Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")), which are not shown in Bartlett et al.. Moreover, this paper also characterize implicit bias of stochastic SAM with batch size $1$, which is minimizing the average-direction sharpness, while Bartlett et al. only considers the deterministic case.

### Implicit Bias of Sharpness Minimization

Recent theoretical works show that SGD with label noise implicitly biased toward local minimizers with a smaller trace of Hessian under the assumption that the minimizers locally connect as a manifold. Arora et al. show that normalized GD implicitly penalizes the largest eigenvalue of the Hessian. Ma et al. argues that such flatness driven phenomenon can also be caused by a multi-scale loss landscape. Lyu et al. show that GD with weight decay on a scale invariant loss function implicitly decreases penalize the spherical sharpness, *i.e.*, the largest eigenvalue of the Hessian evaluated at the normalized parameter.

Another line of works study the sharpness minimization effect of large learning rate assuming the (stochastic) gradient descent converges in the end of training, where the analysis is mainly based on linear stability. Recent theoretical analysis show that the sharpness minimization effect of large learning rate in gradient descent do not necessarily rely on the convergence assumption and linear stability via a four-phase characterization of the dynamics at the so-called Edge of Stability regime.

### Comparison with Arora et al. (2022)

Our proof uses a similar framework as Arora et al.. However, our analysis has its own difficulty for the following reasons. First, Arora et al. only deal with the deterministic case, while our analysis extends to stochastic SAM as well (Section 5). Second, our analysis for the deterministic case is different from that of Arora et al. in the following two aspects. First, the alignment analysis is more complicated because we have two hyperparameters,learning rate $\eta$ and perturbation radius $\rho$, while Arora et al. only needs to deal with one hyperparameter, learning rate $\eta$. Second, the mechanism of penalizing worst-direction sharpness is different, which can be seen from the dependency of the sharpness-reduction rate over learning rate $\eta$. In Arora et al., normalized GD reduces the sharpness via a second-order effect of GD and thus the sharpness is reduced by $O{(\eta^{2})}$ per step. In our analysis, for fixed small perturbation radius $\rho$, the sharpness is reduced by $O{({\rho^{2}\eta})}$ per step, which is linear in $\eta$.

### Analyzing Discrete-time Dynamics via Continuous-time Approaches

There is a long line of research that shows the trajectory of stochastic discrete iterations with decaying step size eventually tracks the solution of some ODE (see Kushner & Yin; Borkar et al.; Duchi & Ruan and the reference therein). However, those results mainly focus on the convergence property of the stochastic iterates (e.g., convergence to stationary points), while we are interested in characterizing the trajectory especially when the process is running for a long time even after the iterate reaches the neighborhood of the manifold of stationary points.

Recently there has been an effort of modeling the discrete-time trajectory of (stochastic) gradient methods by continuous-time approximations. Notably, Li et al. presents a general and rigorous mathematical framework to prove such continuous-time approximation. More specifically, Li et al. proves for various stochastic gradient-based methods, the discrete-time weakly converges to the continuous-time one when LR $\eta\rightarrow 0$ in $\Theta{({1/\eta})}$ steps. The main difference between our results with these results (e.g., Theorem 9 in Li et al. ) is that we focus on a much longer training regime, *i.e.*, $T = {\Theta{({\eta^{- 1}\rho^{- 2}})}}$ steps where the previous continuous-time approximation results no longer holds throughout the entire training. As a result, their continuous approximation is only equivalent to the Phase I dynamics in our Theorems 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and 5.4 and cannot capture the dynamics of SAM in Phase II, when the sharpness-reduction implicit bias happens. The latter requires a more fine-grained analysis to capture the effects of higher-order terms in $\eta$ and $\rho$ in SAM Equation 3.

## Notations and Assumptions

For any natural number $k$, we say a function is $\mathcal{C}^{k}$ if it is $k$-times continuously differentiable and is ${\overline{\mathcal{C}}}^{k}$ if its $k$th order derivatives are locally lipschitz. We say a subset of ${\mathbb{R}}^{D}$ is compact if each of its open covers has a finite subcover. It is well known that a subset of ${\mathbb{R}}^{D}$ is compact if and only if it is closed and bounded. For any positive definite symmetric matrix $A \in {\mathbb{R}}^{D \times D}$, define ${\{{\lambda_{i}{(A)}},{v_{i}{(A)}}\}}_{i \in {\lbrack D\rbrack}}$ as all its eigenvalues and eigenvectors satisfying ${\lambda_{1}{(A)}} \geq {\lambda_{2}{(A)}\ldots} \geq {\lambda_{D}{(A)}}$ and ${\|{v_{i}{(A)}}\|}_{2} = 1$. For any mapping $F$, we define $\partial{F{(x)}}$ as the Jacobian where ${\lbrack{\partial{F{(x)}}}\rbrack}_{ij} = {\partial_{j}{F_{i}{(x)}}}$. Thus the directional derivative of $F$ along the vector $u$ at $x$ can be written as $\partial{F{(x)}u}$. We further define the second order directional derivative of $F$ along the vectors $u$ and $v$ at $x$, $\partial^{2}{F{(x)}{\lbrack u,v\rbrack}}$, $\partial{{({\partial{F \cdot u}})}{(x)}v}$, that is, the directional derivative of $\partial{F \cdot u}$ along the vector $v$ at $x$.

### Definition 3.1 (Differentiable Submanifold of ${\mathbb{R}}^{D}$)

We call a subset $\Gamma \subset {\mathbb{R}}^{D}$ a $\mathcal{C}^{k}$ submanifold of ${\mathbb{R}}^{D}$ if and only if for every $x \in \Gamma$, there exists a open neighborhood $U$ of $x$ and an invertible $\mathcal{C}^{k}$ map $\psi:{U\rightarrow{\mathbb{R}}^{D}}$, such that ${\psi{({\Gamma \cap U})}} = {{({{\mathbb{R}}^{n} \times {\{ 0\}}})} \cap {\psi{(U)}}}$.

Given a $\mathcal{C}^{1}$ submanifold $\Gamma$ of ${\mathbb{R}}^{D}$ and a point $x \in \Gamma$, define $P_{x,\Gamma}$ as the projection operator onto the manifold of the normal space of $\Gamma$ at $x$ and $P_{x,\Gamma}^{\perp} = {I_{D} - P_{x,\Gamma}}$. We fix our initialization as $x_{\text{init}}$ and our loss function as $L:{{\mathbb{R}}^{D}\rightarrow{\mathbb{R}}}$. Given the loss function, its gradient flow is denoted by mapping $\phi:{{{\mathbb{R}}^{D} \times {\lbrack 0,\infty)}}\rightarrow{\mathbb{R}}^{D}}$. Here, $\phi{(x,\tau)}$ denotes the iterate at time $\tau$ of a gradient flow starting at $x$ and is defined as the unique solution of ${\phi{(x,\tau)}} = {x - {\int_{0}^{\tau}{{\nabla L}{({\phi{(x,t)}})}{dt}}}}$, ${\forall x} \in {\mathbb{R}}^{D}$. We further define the limiting map $\Phi$ as ${\Phi{(x)}} = {\lim_{\tau\rightarrow\infty}{\phi{(x,\tau)}}}$, that is, $\Phi{(x)}$ denotes the convergent point of the gradient flow starting from $x$. When $L{(x)}$ is small, $\Phi{(x)}$ and $x$ are near. Hence in our analysis, we regularly use $\Phi{({x{(t)}})}$ as a surrogate to analyze the dynamics of $x{(t)}$. Lemma 3.2 is an important property of $\Phi$ from Li et al. (Lemma C.2), which is repeatedly used in our analysis. For completeness, we attach its proof below.

### Lemma 3.2

For any $x$ at which $\Phi$ is defined and differentiable, we have that ${\partial{\Phi{(x)}{\nabla L}{(x)}}} = 0$.

### Proof of Lemma 3.2

Since $\Phi$ is defined the limit map of gradient flow, it holds that for any $t \geq 0$, ${\Phi{({\phi{(x,t)}})}} = {\Phi{(x)}}$. Differentiating both sides at $t = 0$, we have ${\partial{\Phi{({\phi{(x,0)}})}\frac{\partial{\phi{(x,t)}}}{\partial t}}} = 0$. The proof is completed by noting that $\frac{\partial{\phi{(x,t)}}}{\partial t} = {- {{\nabla L}{({\phi{(x,t)}})}}}$ by definition of $\phi$. ∎

Recent empirical studies have shown that there are essentially no barriers in loss landscape between different minimizers, that is, the set of minimizers are path-connected. Motivated by this empirical discovery, we make the assumption below following Fehrman et al.; Li et al.; Arora et al., which is theoretically justified by Cooper under a generic setting.

### Assumption 3.3

Assume loss $L:{{\mathbb{R}}^{D}\rightarrow{\mathbb{R}}}$ is $\mathcal{C}^{4}$, and there exists a $\mathcal{C}^{2}$ submanifold $\Gamma$ of ${\mathbb{R}}^{D}$ that is a $({D - M})$-dimensional for some integer $1 \leq M \leq D$, where for all $x \in \Gamma$, $x$ is a local minimizer of $L$ and ${{rank}{({{\nabla^{2}L}{(x)}})}} = M$.

The connectivity of the set of local minimizers implied by the manifold assumption above allows us to take limits of perturbation radius $\rho\rightarrow 0$ while still yield interesting and insightful implicit bias results in the end-to-end analysis. So far almost all analysis of implicit bias for general model parameterizations relies on Taylor expansion, *e.g.* Blanc et al.; Damian et al.; Li et al.; Arora et al., so does the derivation of the SAM algorithm Foret et al.; Wu et al.. Thus it's crucial to consider small perturbation size $\rho$. On the contrary, if the set of global minimizers are a set of discrete points, then with small perturbation radius $\rho$, implicit bias of optimizers is not sufficient to drive the iterate from global minimum to the other one.

It can be shown that for a minimum loss manifold, the rank of Hessian plus the dimension of the manifold is at most the environmental dimension $D$, and thus our assumption about Hessian rank essentially says the the rank is maximal. This assumption is necessary for the analysis to guarantee the differentiability of $\Phi$.

Though our analysis for the full-batch setting are performed under the general and abstract setting, 3.3, our analysis for stochastic setting uses a more concrete one, 5.1, where we can prove that 3.3 holds. (see Theorem 5.2)

### Definition 3.4 (Attraction Set)

Let $U$ be the attraction set of $\Gamma$ under gradient flow, that is, a neighborhood of $\Gamma$ containing all points starting from which gradient flow w.r.t. loss $L$ converges to some point in $\Gamma$, or mathematically, $U \triangleq \left. \{{x \in {\mathbb{R}}^{D}} \middle| {{\Phi{(x)}\text{~exists and~}\Phi{(x)}} \in \Gamma}\} \right.$.

3.3 implies that $U$ is open and $\Phi$ is ${\overline{\mathcal{C}}}^{2}$ on $U$.

By definition, ${\Phi{(x)}} = x$ for any $x \in \Gamma$. Differentiating this equality yields the following important lemma about the property of $\partial\Phi$ on manifold $\Gamma$.

### Lemma 3.5 (Li et al. (2021), Lemma 4.3)

For $x \in \Gamma$, ${\partial{\Phi{(x)}}} = P_{x,\Gamma}^{\perp}$, the orthogonal projection matrix onto the tangent space of $\Gamma$ at $x$. Since $d$ ${\partial{\Phi{(x)}{\nabla^{2}L}{(x)}}} = 0$.

### Implicit versus Explicit Bias

If an algorithm or optimizer has a bias towards certain type of global/local minima of the loss over other minima of the loss, and this bias is not encoded in the loss function, then we call such bias an implicit bias. On the other hand, a bias emerges as solely a consequence of successfully minimizing certain regularized loss regardless of the optimizers (as long as the optimzers minimize the loss), we say such bias is an *explicit bias* of the regularized loss (or the regularizer).

As a concrete example, we will prove that full-batch SAM (Equation 3) prefers local minima with certain sharpness property. The bias stems from the particular update rule of full-batch SAM (Equation 3), and not all optimizers for the intended target loss function $L_{\rho}^{\text{Asc}}$ (Equation 2) has this bias. Therefore, it's considered as an implicit bias. As an example for explicit bias, all optimizers minimizing a loss combined with $\ell_{2}$ regularization will prefer model with smaller parameter norm and this is considered as an explicit bias of $\ell_{2}$ regularization.

### Usage of $O\hspace{0pt}{( \cdot )}$ Notation

Our analysis assumes small $\eta$ and $\rho$ while treating all other problem-dependent parameters as constants, such as the dimension of parameter space and the maximum possible value of derivatives (of different orders) of loss function $L$ and the limit map $\Phi$. In ${O{( \cdot )}},{\Omega{( \cdot )}},{o{( \cdot )}},{\omega{( \cdot )}},{\Theta{( \cdot )}}$, we hide all the dependency related to the problem, e.g., the (unique) initialization $x_{\text{init}}$, the manifold $\Gamma$, compact set $\overline{U^{\prime}}$ in Theorem 4.2, and the continuous time $T_{3}$ in Theorems 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and 5.4, and only keep the dependency on $\rho$ and $\eta$. For example, $O{({f{(\rho)}})}$ is a placeholder for some function $g{(\rho)}$ such that there exists problem-dependent constant $C > 0$, ${{\forall\rho} > 0},{{|{g{(\rho)}}|} \leq {C{|{f{(\rho)}}|}}}$. In informal equations such as Section 4.3) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") in the proof sketch section, we are a bit more sloppy and hide dependency on $x{(t)}$ in $O{( \cdot )}$ notation as well. But these will be formally dealt with in the proofs.

### Ill-definedness of SAM with Zero Gradient

The update rule of SAM (Equations 3 and 17) is ill-defined when the gradient is zero. However, our analysis in Appendix B shows that when the stationary point of loss $L$, $\{ x\mid{{{\nabla L}{(x)}} = 0}\}$, is a zero-measure set, for any perturbation radius $\rho$, except for countably many learning rates, full-batch SAM is well-defined for almost all initialization and all steps (Theorem B.1). A similar result is shown for stochastic SAM if the stationary points of each stochastic loss form a zero-measure set (Theorem B.2). Thus SAM is generically well-defined. For the sake of rigorousness, when SAM encountering zero gradients, we modify the algorithm via replacing the ill-defined normalized gradient by an arbitrary vector with unit norm and our analysis for implicit bias of SAM still holds.

## Explicit and Implicit Bias in the Full-Batch Setting

In this section, we present our main results in the full-batch setting. Section 4.1 provides characterization of explicit bias of *worst-direction*, *ascent-dircetion*, and average-direction sharpness. In particular, we show that ascent-direction sharpness and worst-direction sharpness have different explicit biases. However, it turns out the explicit bias of ascent-direction sharpness is not the effective bias of SAM (that approximately optimizes the ascent-direction sharpness), because the particular implementation of SAM imposes additional, different biases, which is the main focus of Section 4.2. We provide our main theorem in the full-batch setting, that SAM implicitly minimizes the worst-direction sharpness, via characterizing its limiting dynamics as learning rate $\rho$ and $\eta$ goes to $0$ with a Riemmanian gradient flow with respect to the top eigenvalue of the Hessian of the loss on the manifold of local minimizers. In Section 4.3, we sketch the proof of the implicit bias of SAM and identify a key property behind the implicit bias, which we call the *implicit alignment* between the gradient and the top eigenvector of the Hessian.

### Worst- and Ascent-direction Sharpness Have Different Explicit Biases

In this subsection, we show that the explicit biases of three notions of sharpness are all different under 3.3. We first recap the heuristic derivation of ascent-direction sharpness $R_{\rho}^{\text{Asc}}$.

The intuition of approximating $R_{\rho}^{\text{Max}}$ by $R_{\rho}^{\text{Asc}}$ comes from the following Taylor expansions. Consider any compact set, for sufficiently small $\rho$, the following holds uniformly for all $x$ in the compact set:

Here, the preference among the local or global minima is what we are mainly concerned with. Since ${\sup_{{\| v\|}_{2} \leq 1}{v^{\top}{\nabla L}{(x)}}} = \left\| {{\nabla L}{(x)}} \right\|_{2}$ when $\left\| {{\nabla L}{(x)}} \right\|_{2} > 0$, the leading terms in Equations 5 and 6 are both the first order term, $\rho\left\| {{\nabla L}{(x)}} \right\|_{2}$, and are the same. However, it is erroneous to think that the first order term decides the explicit bias, as the first order term $\left\| {{\nabla L}{(x)}} \right\|_{2}$ vanishes at the local minimizers of the loss $L$ and thus the second order term becomes the leading term. Any global minimizer $x$ of the original loss $L$ is an $O{(\rho^{2})}$-approximate minimizer of the sharpness-aware loss because ${{\nabla L}{(x)}} = 0$. Therefore, the sharpness-aware loss needs to be of order $\rho^{2}$ so that we can guarantee the second-order terms in Equation 5 and/or Equation 6 to be non-trivially small. Our main result in this subsection (Theorem 4.2) gives an explicit characterization for this phenomenon. The corresponding explicit biases for each type of sharpness is given below in Definition 4.1. As we will see later, they can be derived from a general notion of *limiting regularizer* (Definition 4.3. ‣ 4.1 Worst- and Ascent-direction Sharpness Have Different Explicit Biases ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")).

### Definition 4.1

For $x \in {\mathbb{R}}^{D}$, we define ${S^{\text{Max}}{(x)}} = {{\lambda_{1}{({{\nabla^{2}L}{(x)}})}}/2}$, ${S^{\text{Asc}}{(x)}} = {{\lambda_{M}{({{\nabla^{2}L}{(x)}})}}/2}$ and ${S^{\text{Avg}}{(x)}} = {{{Tr}{({{\nabla^{2}L}{(x)}})}}/{({2D})}}$.

### Theorem 4.2

Under 3.3, let $U^{\prime}$ be any bounded open set such that its closure $\overline{U^{\prime}} \subseteq U$ and ${\overline{U^{\prime}} \cap \Gamma} \subseteq \overline{U^{\prime}\cap\Gamma}$. For any ${type} \in {\{{Max},{Asc},{Avg}\}}$ and any optimality gap $\Delta > 0$, there is a function $\epsilon:{{\mathbb{R}}^{+}\rightarrow{\mathbb{R}}^{+}}$ with ${\lim_{\rho\rightarrow 0}{\epsilon{(\rho)}}} = 0$, such that for all sufficiently small $\rho > 0$ and all $u \in U^{\prime}$ satisfying that

it holds that ${{L{(u)}} - {\inf_{x \in U^{\prime}}{L{(x)}}}} \leq {{({\Delta + {\epsilon{(\rho)}}})}\rho^{2}}$ and that

Theorem 4.2 suggests a sharp phase transition of the property of the solution of ${{\min_{x}L}{(x)}} + {R_{\rho}{(x)}}$ when the optimization error drops from $\omega{(\rho^{2})}$ to $O{(\rho^{2})}$. When the optimization error is larger than $\omega{(\rho^{2})}$, no regularization effect happens and any minimizer satisfies the requirement. When the error becomes $O{(\rho^{2})}$, there is a non-trivial restriction on the coefficients in the second-order term.

Next we give a heuristic derivation for the above defined $S^{type}$. First, for worst- and average-direction sharpness, the calculations are fairly straightforward and well-known in literature, and we sketch them here. In the limit of perturbation radius $\rho\rightarrow 0$, we know that the minimizer of the sharpness-aware loss will also converges to $\Gamma$, the manifold of minimizers of the original loss $L$. Thus to decide to which $x \in \Gamma$ the minimizers will converge to as $\rho\rightarrow 0$, it suffices to take Taylor expansion of $L_{\rho}^{\text{Asc}}$ or $L_{\rho}^{\text{Avg}}$ at each $x \in \Gamma$ and compare the second-order coefficients, *e.g.*, we have that ${R_{\rho}^{\text{Avg}}{(x)}} = {{\frac{\rho^{2}}{2D}{Tr}{({{\nabla^{2}L}{(x)}})}} + {O{(\rho^{3})}}}$ and ${R_{\rho}^{\text{Max}}{(x)}} = {{\frac{\rho^{2}}{2}\lambda_{1}{({{\nabla^{2}L}{(x)}})}} + {O{(\rho^{3})}}}$ by Equation 5.

However, the analysis for ascent-direction sharpness is more tricky because ${R_{\rho}^{\text{Asc}}{(x)}} = \infty$ for any $x \in \Gamma$ and thus is not continuous around such $x$. Thus we have to aggregate information from neighborhood to capture the explicit bias of $R_{\rho}$ around manifold $\Gamma$. This motivates the following definition of *limiting regularizer* which allows us to compare the regularization strength of $R_{\rho}$ around each point on manifold $\Gamma$ as $\rho\rightarrow 0$.

### Definition 4.3 (Limiting Regularizer)

We define the *limiting regularizer* of $\{ R_{\rho}\}$ as the function^22^2Here we implicitly assume the zeroth and first order term varnishes, which holds for all three sharpness notions. If not, then the notion of limiting regularizer is undefined.

To minimize $R_{\rho}^{\text{Asc}}$ around $x$, we can pick $x^{\prime}\rightarrow x$ satisfying that $\left\| {{\nabla L}{(x^{\prime})}} \right\|_{2}\rightarrow 0$ yet strictly being non-zero. By Equation 6, we have ${R_{\rho}^{\text{Asc}}{(x^{\prime})}} \approx {\frac{\rho^{2}}{2}\frac{\cdot \nabla L{(x^{\prime})}^{\top}\nabla^{2}L{(x)}\nabla L{(x^{\prime})}}{{\|{{\nabla L}{(x^{\prime})}}\|}_{2}^{2}}}$. Here the crucial step of the proof is that because of 3.3, ${{\nabla L}{(x)}}/\left\| {{\nabla L}{(x)}} \right\|_{2}$ must almost lie in the column span of ${\nabla^{2}L}{(x)}$, which implies that $\inf_{x^{\prime}}{{{{\nabla L}{(x^{\prime})}^{\top}{\nabla^{2}L}{(x)}{\nabla L}{(x^{\prime})}}/{\|{{\nabla L}{(x^{\prime})}}\|}_{2}^{2}}\overset{\rho\rightarrow 0}{\rightarrow}\lambda_{M}{({{\nabla^{2}L}{(x)}})}}$, where ${{rank}{({{\nabla^{2}L}{(x)}})}} = M$ by 3.3. The above alignment property between the gradient and the column space of Hessian can be checked directly for any non-negative quadratic function. The maximal Hessian rank assumption in 3.3 ensures that this property extends to general losses.

We defer the proof of Theorem 4.2 into Section E.1, where we develop a sufficient condition where the notion of limiting regularizer characterizes the explicit bias of $R_{\rho}$ as $\rho\rightarrow 0$.

### SAM Provably Decreases Worst-direction Sharpness

Though ascent-direction sharpness has different explicit bias from worst-direction sharpness, in this subsection we will show that surprisingly, SAM (Equation 3), a heuristic method designed to minimize ascent-direction sharpness, provably decreases worst-direction sharpness. The main result here is an exact characterization of the trajectory of SAM (Equation 3) via the following ordinary differential equation (ODE) (Equation 7), when learning rate $\eta$ and perturbation radius $\rho$ are small and the initialization ${x{}} = x_{\text{init}}$ is in $U$, the attraction set of manifold $\Gamma$.

We assume ODE (Equation 7) has a solution till time $T_{3}$, that is, Equation 7 holds for all $t \leq T_{3}$. We call the solution of Equation 7 the *limiting flow* of SAM, which is exactly the Riemannian Gradient Flow on the manifold $\Gamma$ with respect to the loss $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$. In other words, the ODE (Equation 7) is essentially a projected gradient descent algorithm with loss $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$ on the constraint set $\Gamma$ and an infinitesimal learning rate. Note $\lambda_{1}{({{\nabla^{2}L}{(x)}})}$ may not be differentiable at $x$ if ${\lambda_{1}{({{\nabla^{2}L}{(x)}})}} = {\lambda_{2}{({{\nabla^{2}L}{(x)}})}}$, thus to ensure Equation 7 is well-defined, we assume there is a positive eigengap for $L$ on $\Gamma$.^33^3In fact we only need to assume the positive eigengap along the solution of the ODE. If $\Gamma$ doesn't satisfy 4.4, we can simply perform the same analysis on its submanifold $\{{x \in \Gamma}\mid{\text{eigengap is positive at~}x}\}$.

### Assumption 4.4

For all $x \in \Gamma$, there exists a positive eigengap, i.e., ${\lambda_{1}{({{\nabla^{2}L}{(x)}})}} > {\lambda_{2}{({{\nabla^{2}L}{(x)}})}}$.

Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") is the main result of this section, which is a direct combination of Theorems G.1. ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and G.3. ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"). The proof is deferred to Section G.3 ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?").

### Theorem 4.5 (Main)

Let $\{{x{(t)}}\}$ be the iterates of full-batch SAM (Equation 3) with ${x{}} = x_{\text{init}} \in U$. Under Assumptions 3.3 and 4.4, for all $\eta,\rho$ such that $\eta{\ln{({1/\rho})}}$ and $\rho/\eta$ are sufficiently small, the dynamics of SAM can be characterized in the following two phases:

Phase I: (Theorem G.1. ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) Full-batch SAM (Equation 3) follows Gradient Flow with respect to $L$ until entering an $O{({\eta\rho})}$ neighborhood of the manifold $\Gamma$ in $O{({{\ln{({1/\rho})}}/\eta})}$ steps;

Phase II: (Theorem G.3. ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) Under a mild non-degeneracy assumption (G.2 ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) on the initial point of phase II, full-batch SAM (Equation 3) tracks the solution $X$ of Equation 7, the Riemannian Gradient Flow with respect to the loss $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$ in an $O{({\eta\rho})}$ neighborhood of manifold $\Gamma$. Quantitatively, the approximation error between the iterates $x$ and the corresponding limiting flow $X$ is $O{({\eta{\ln{({1/\rho})}}})}$, that is,

Moreover, the angle between $\nabla L\left( x\left. ({\lceil\frac{T_{3}}{\eta\rho^{2}}\rceil} \right) \right.$ and the top eigenspace of ${\nabla^{2}L}{({x{({\lceil\frac{T_{3}}{\eta\rho^{2}}\rceil})}})}$ is at most $O{(\rho)}$.

Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") shows that SAM decreases the largest eigenvalue of Hessian of loss locally around the manifold of local minimizers. Phase I uses standard approximation analysis as in Hairer et al.. In Phase II, as $T_{3}$ is arbitrary, the approximation and alignment properties hold simultaneously for all $X{(t)}$ along the trajectory, provided that $\eta{\ln{({1/\rho})}}$ and $\rho/\eta$ are sufficiently small. The subtlety here is that the threshold of being "sufficiently small" on $\eta{\ln{({1/\rho})}}$ and $\rho/\eta$ actually depends on $T_{3}$, which decreases when $T_{3}\rightarrow 0$ or $\rightarrow\infty$. We defer the proof of Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") to Appendix G ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?").

As a corollary of Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"), we can also show that the largest eigenvalue of the limiting flow closely tracks the worst-direction sharpness.

### Corollary 4.6

In the setting of Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"), the difference between the worst-direction sharpness of the iterates and the corresponding scaled largest eigenvalues along the limiting flow is at most $O{({\eta\rho^{2}{\ln{({1/\rho})}}})}$. That is,

Since $\eta{\ln{({1/\rho})}}$ is assumed to be sufficiently small, the error $O{({{\eta{\ln{({1/\rho})}}} \cdot \rho^{2}})}$ is only $o{(\rho^{2})}$, meaning that penalizing the top eigenvalue on the manifold does lead to non-trivial reduction of worst-direction sharpness, in the sense of Section 4.1.

Hence we can show that full-batch SAM (Equation 3) provably minimizes *worst-direction sharpness* around the manifold if we additionally assume the limiting flow converges to a minimizer of the top eigenvalue of Hessian in the following Corollary 4.7.

### Corollary 4.7

Under Assumptions 3.3 and 4.4, define $U^{\prime}$ as in Theorem 4.2 and suppose ${X{(\infty)}} = {\lim\limits_{t\rightarrow\infty}{X{(t)}}}$ exists and is a minimizer of $\lambda_{1}{({{\nabla^{2}L}{(x)}})}$ in $U^{\prime} \cap \Gamma$. Then for all $\epsilon > 0$, there exists $T_{\epsilon} > 0$, such that for all $\rho,\eta$ such that $\eta{\ln{({1/\rho})}}$ and $\rho/\eta$ are sufficiently small, we have that

We defer the proof of Corollaries 4.6 and 4.7 to Section G.4 ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?").

### Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")

Now we give an overview of the analysis for the trajectory of full-batch SAM (Equation 3) in Phase II (in Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")). The framework of the analysis is similar to Arora et al.; Lyu et al.; Damian et al., where the high-level idea is to use $\Phi{({x{(t)}})}$ as a proxy for $x{(t)}$ and study the dynamics of $\Phi{({x{(t)}})}$ via Taylor expansion. We will first closely follow the machinery developed in Arora et al. to arrive at Equation 11) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"), starting from which we will discuss the key innovation in this paper regarding implicit Hessian-gradient alignment.

### Dynamics of $\Phi\hspace{0pt}{({x\hspace{0pt}{(t)}})}$ via Taylor expansion

In Phase II, $x{(t)}$ is $O{({\eta\rho})}$-close to the manifold $\Gamma$ and therefore it can be shown that ${\|{{x{(t)}} - {\Phi{({x{(t)}})}}}\|}_{2} = {O{({\eta\rho})}}$ holds for every step in Phase II. This also implies that $\left\| {{x{({t + 1})}} - {x{(t)}}} \right\|_{2} = {O{({\eta\rho})}}$ (See Lemma D.6). Using Taylor expansion around $x{(t)}$, we have that

For any $x \in {\mathbb{R}}^{D}$, applying Taylor expansion on ${\nabla L}\left( {x + {\rho\frac{{\nabla L}{(x)}}{\left\| {{\nabla L}{(x)}} \right\|_{2}}}} \right)$ around $x$, we have that

Using Section 4.3) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") with $x = {x{(t)}}$, plugging in Section 4.3) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and then rearranging, we have that

By Lemma 3.2, we have that ${\partial{\Phi{({x{(t)}})}{\nabla L}{({x{(t)}})}}} = 0$. Furthermore, by Lemma 3.5, Lemma 4.3). ‣ 3 Notations and Assumptions ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"), we have that ${\partial{\Phi{({\Phi{({x{(t)}})}})}{\nabla^{2}L}{({\Phi{({x{(t)}})}})}}} = 0$. This implies that

Thus we conclude that

Now, to understand how $\Phi{({x{(t)}})}$ moves over time, we need to understand what the direction of the RHS of Equation 11) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") corresponds to---we will prove that it corresponds to the Riemannian gradient of the loss function ${\nabla\lambda_{1}}{({{\nabla^{2}L}{(x)}})}$ at $x = {\Phi{({x{(t)}})}}$. To achieve this, the key is to understand the direction $\frac{{\nabla L}{({x{(t)}})}}{\left\| {{\nabla L}{({x{(t)}})}} \right\|_{2}}$. It turns out that we will prove $\frac{{\nabla L}{({x{(t)}})}}{\left\| {{\nabla L}{({x{(t)}})}} \right\|_{2}}$ is close to the top eigenvector of the Hessian up to sign flip, that is ${\|{\frac{{\nabla L}{({x{(t)}})}}{\left\| {{\nabla L}{({x{(t)}})}} \right\|_{2}} - {{s \cdot v_{1}}{({{\nabla^{2}L}{(x)}})}}}\|}_{2} \leq {O{(\rho)}}$ for some $s \in {\{{- 1},1\}}$. We call this phenomenon Hessian-gradient alignment and will discuss it in more detail at the end of this subsection.

Using this property, we can proceed with the derivation:

where the second to last step we use the property of the derivative of eigenvalue (Lemma I.7). ‣ Appendix I Technical Lemmas ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) and the last step is due to Taylor expansion of $\partial{\Phi{( \cdot )}{\nabla\lambda_{1}}{({{\nabla^{2}L}{( \cdot )}})}}$ at $\Phi{({x{(t)}})}$ and the fact that $\left\| {{\Phi{({x{(t)}})}} - {x{(t)}}} \right\| = {O{({\eta\rho})}}$.

### Implicit Hessian-gradient Alignment

It remains to explain why the gradient implicitly aligns to the top eigenvector of the Hessian, which is the key component of the analysis in Phase II. The proof strategy here is to first show alignment for a quadratic loss function, and then generalize its proof to general loss functions satisfying 3.3. Below we first give the formal statement of the implicit alignment on quadratic loss, Theorem 4.8 and defer the result for general case (Lemma G.19 ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) to appendix. Note this alignment property is an implicit property of the SAM algorithm as it is not explicitly enforced by the objective that SAM is intended to minimize, $L_{\rho}^{\text{Asc}}$. Indeed optimizing $L_{\rho}^{\text{Asc}}$ would rather explicitly align gradient to the smallest non-zero eigenvector (See proofs of Theorem E.5)!

### Theorem 4.8

Suppose $A$ is a positive definite symmetric matrix with unique top eigenvalue. Consider running full-batch SAM (Equation 3) on loss ${L{(x)}} ≔ {\frac{1}{2}x^{T}Ax}$ as in Equation 13 below.

Then, for almost every $x{}$, we have $x{(t)}$ converges in direction to $v_{1}{(A)}$ up to a sign flip and ${\lim_{t\rightarrow\infty}{\|{x{(t)}}\|}_{2}} = \frac{\eta\rho\lambda_{1}{(A)}}{2 - {\eta\lambda_{1}{(A)}}}$ with ${\eta\lambda_{1}{(A)}} < 1$.

The proof of Theorem 4.8 relies on a two-phase analysis of the behavior of Equation 13, where we first show that $x{(t)}$ enters an invariant set from any initialization and in the second phase, we construct a potential function to show alignment. The proof is deferred to Appendix F ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?").

Below we briefly discuss why the case with general loss is closely related to the quadratic loss case. We claim that, in the general loss function case, the analog of Equation 13 is the update rule for the gradient:

We first note that indeed in the quadratic case where ${{\nabla L}{(x)}} = {Ax}$ and ${{\nabla^{2}L}{(x)}} = A$, Equation 14 is equivalent to Equation 13 because they only differ by a multiplicative factor $A$ on both sides.

Hence, in the general case, the update of the gradient (Equation 14) can be viewed as an $O{({\eta\rho^{2}})}$-perturbed version of the update of the iterate in the quadratic case. Note $O{({\eta\rho^{2}})}$ is a higher order term comparing to the other two terms, which are on the order of $\Theta{({\eta^{2}\rho})}$ and $\Theta{({\eta\rho})}$ respectively. By controlling the error terms, the mechanism and analysis of the implicit alignment between Hessian and gradient still apply to the general case. We can also show that once this alignment happens, it will be kept until the end of our analysis, which is $\Theta{({\eta^{- 1}\rho^{- 2}})}$ steps.

Finally, we derive Equation 14 by Taylor expansion. We first apply Taylor expansion (Section 4.3) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) on the update rule of the iterate of SAM (Equation 3):

Since phase II happens in an $O{({\eta\rho})}$-neighborhood of manifold $\Gamma$, we have $\left\| {{x{({t + 1})}} - {x{(t)}}} \right\|_{2} = {O{({\eta\rho})}}$. Then by Equation 15 and Taylor expansion on ${\nabla L}{({x{({t + 1})}})}$ at $x{(t)}$, we have that

## Explicit and Implicit Biases in the Stochastic Setting

In practice, people usually use SAM in the stochastic mini-batch setting, and the test accuracy improves as the batch size decreases. Towards explaining this phenomenon, Foret et al. argue intuitively that stochastic SAM minimizes stochastic worst-direction sharpness. Given our results in Section 4, it is natural to ask if we can justify the above intuition by showing the Hessian-gradient alignment in the stochastic setting. Unfortunately, such alignment is not possible in the most general setting. Yet when the batch size is 1, we can prove rigorously in Section 5.2 that stochastic SAM minimizes *stochastic worst-direction sharpness*, which is the expectation of the worst-direction sharpness of loss over each data (defined in Section 5.1), which is the main result in this section. We stress that the stochastic worst-direction sharpness has a different explicit bias to the worst-direction sharpness, which full-batch SAM implicitly penalizes. When perturbation radius $\rho\rightarrow 0$, the former corresponds to ${Tr}{({{\nabla^{2}L}{( \cdot )}})}$, the same as average-direction sharpness, and the latter corresponds to $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$.

Below we start by introducing our setting for SAM with batch size $1$, or $1$*-SAM*. We still need 3.3 in this section. We first analyze the explicit bias of the stochastic ascent- and worst-direction sharpness in Section 5.1 via the tools developed in Section 4.1. It turns out they are all proportional to the trace of hessian as $\rho\rightarrow 0$. In Section 5.2, we show that 1-SAM penalizes the trace of Hessian. Below we formally state our setting for stochastic loss of batch size one (5.1).

### Setting 5.1

Let the total number of data be $M$. Let $f_{k}{(x)}$ be the model output on the $k$-th data where $f_{k}$ is a $\mathcal{C}^{4}$-smooth function and $y_{k}$ be the $k$-th label, for $k = {1,\ldots,M}$. We define the loss on the $k$-th data as ${L_{k}{(x)}} = {\ell{({f_{k}{(x)}},y_{k})}}$ and the total loss $L = {\sum_{k = 1}^{M}{L_{k}/M}}$, where function $\ell{(y^{\prime},y)}$ is $\mathcal{C}^{4}$-smooth in $y^{\prime}$. We also assume for any $y \in {\mathbb{R}}$, it holds that ${{{\arg\min}_{y^{\prime} \in {\mathbb{R}}}\ell}{(y^{\prime},y)}} = y$ and that ${\frac{\partial^{2}{\ell{(y^{\prime},y)}}}{{({\partial y^{\prime}})}^{2}}|}_{y^{\prime} = y} > 0$. Finally, we denote the set of global minimizers of $L$ with full-rank Jacobian by $\Gamma$ and assume that it is non-empty, that is,

We remark that given training data (*i.e.*, ${\{ f_{k}\}}_{k = 1}^{M}$), $\Gamma$ defined above is just equal to the set of global minimizers, $\left\{ {x \in {\mathbb{R}}^{D}}\mid{{{f_{k}{(x)}} = y_{k}},{{\forall k} \in {\lbrack M\rbrack}}} \right\}$, except for a zero measure set of labels ${(y_{k})}_{k = 1}^{M}$ when $f_{k}$ are $\mathcal{C}^{\infty}$ smooth, by Sard's Theorem. Thus Cooper argued that the global minimizers form a differentiable manifold generically if we allow perturbation on the labels. In this work we do not make such an assumption for labels. Instead, we consider the subset of the global minimizers with full-rank Jacobian, $\Gamma$. A standard application of implicit function theorem implies that $\Gamma$ defined in 5.1 is indeed a manifold. (See Theorem 5.2, whose proof is deferred into Section C.1)

### Theorem 5.2

Loss $L$, set $\Gamma$ and integer $M$ defined in 5.1 satisfy 3.3.

### 1-SAM

We use $1$*-SAM* as a shorthand for SAM on a stochastic loss with batch size $1$ as below Equation 17, where $k_{t}$ is sampled i.i.d from uniform distribution on $\lbrack M\rbrack$.

### Stochastic Worst-, Ascent- and Average- direction Sharpness Have the Same Explicit Biases as Average Direction Sharpness

Similar to the full-batch case, we use $L_{k,\rho}^{\text{Max}},L_{k,\rho}^{\text{Asc}},L_{k,\rho}^{\text{Avg}}$ to denote the corresponding sharpness-aware loss for $L_{k}$ and $R_{k,\rho}^{\text{Max}},R_{k,\rho}^{\text{Asc}},R_{k,\rho}^{\text{Avg}}$ to denote corresponding sharpness for $L_{k}$ respectively (defined as Equations 1, 2 and 4 with $L$ replaced by $L_{k}$). We further use *stochastic worst-, ascent- and average-direction sharpness* to denote ${{\mathbb{E}}_{k}{\lbrack R_{k,\rho}^{\text{Max}}\rbrack}},{{\mathbb{E}}_{k}{\lbrack R_{k,\rho}^{\text{Asc}}\rbrack}}$ and ${\mathbb{E}}_{k}{\lbrack R_{k,\rho}^{\text{Avg}}\rbrack}$. Unlike the full-batch setting, these three sharpness notions have the same explicit biases, or more precisely, they have the same limiting regularizers (up to some scaling factor).

### Theorem 5.3

The limiting regularizers of three notions of stochastic sharpness, denoted by ${\overset{\sim}{S}}^{\text{Max}},{\overset{\sim}{S}}^{\text{Asc}},{\overset{\sim}{S}}^{\text{Avg}}$, satisfy that

Furthermore, define $U^{\prime}$ in the same way as in Theorem 4.2. For any ${type} \in {\{{Max},{Asc},{Avg}\}}$, it holds that if for some $u \in U^{\prime}$, ${{L{(u)}} + {{\mathbb{E}}_{k}{\lbrack{R_{k,\rho}^{type}{(u)}}\rbrack}}} \leq {{\inf\limits_{x \in U^{\prime}}\left( {{L{(x)}} + {{\mathbb{E}}_{k}{\lbrack{R_{k,\rho}^{type}{(x)}}\rbrack}}} \right)} + {\epsilon\rho^{2}}}$,^44^4We note that $R_{\rho}^{\text{Asc}}{(x)}$ is undefined when $\left\| {{\nabla L}{(x)}} \right\|_{2} = 0$. In such cases, we set ${R_{\rho}^{\text{Asc}}{(x)}} = \infty$. then we have that ${{L{(u)}} - {\inf_{x \in U^{\prime}}{L{(x)}}}} \leq {{\epsilon\rho^{2}} + {o{(\rho^{2})}}}$ and that $\left| {{{\overset{\sim}{S}}^{type}{(u)}} - {\inf_{x \in {U^{\prime} \cap \Gamma}}{{\overset{\sim}{S}}^{type}{(x)}}}} \right| \leq {\epsilon + {o{}}}$.

We defer the proof of Theorem 5.3 to Section E.4. Unlike in the full-batch setting where the implicit regularizer of ascent-direction sharpness and worst-direction sharpness have different explicit bias, here they are the same because there is no difference between the maximum and minimum of its non-zero eigenvalue for rank-1 Hessian of each individual loss $L_{k}$, and that the average of limiting regularizers is equal to the limiting regularizer of the average regularizer by definition.

### Stochastic SAM Minimizes Average-direction Sharpness

This subsection aims to show that the implicit bias of 1-SAM (Equation 17) is minimizing the average-direction sharpness for small perturbation radius $\rho$ and learning rate $\eta$, which has the same implicit bias as all three notions of stochastic sharpness do (Theorem 5.3). As an analog of the analysis in Section 4.3, which shows full-batch SAM minimizes worst-direction sharpness, analysis in this section conceptually shows that 1-SAM minimizes the stochastic worst-direction sharpness.

Mathematically, we prove that the trajectory of 1-SAM tracks the following Riemannian gradient flow (Equation 18) with respect to their limiting regularize ${Tr}{({{\nabla^{2}L}{( \cdot )}})}$ on the manifold for sufficiently small $\eta$ and $\rho$ and thus penalizes stochastic worst-direction sharpness (of batch size $1$). We assume the ODE (Equation 18) has a solution till time $T_{3}$.

### Theorem 5.4

Let $\{{x{(t)}}\}$ be the iterates of 1-SAM (Equation 17) and ${x{}} = x_{\text{init}} \in U$, then under 5.1, for almost every $x_{\text{init}}$, for all $\eta$ and $\rho$ such that ${({\eta + \rho})}{\ln{({{1/\eta}\rho})}}$ is sufficiently small, with probability at least $1 - {O{(\rho)}}$ over the randomness of the algorithm, the dynamics of 1-SAM (Equation 17) can be split into two phases:

Phase I (Theorem H.1. ‣ Appendix H Analysis for 1-SAM (Proof of Theorem 5.4) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")): 1-SAM follows Gradient Flow with respect to $L$ until entering an $\overset{\sim}{O}{({\eta\rho})}$ neighborhood of the manifold $\Gamma$ in $O{({{\ln{({{1/\rho}\eta})}}/\eta})}$ steps;

Phase II (Theorem H.2. ‣ Appendix H Analysis for 1-SAM (Proof of Theorem 5.4) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")): 1-SAM tracks the solution of Equation 18, $X$, the Riemannian gradient flow with respect to ${Tr}{({{\nabla^{2}L}{( \cdot )}})}$ in an $\overset{\sim}{O}{({\eta\rho})}$ neighborhood of manifold $\Gamma$. Quantitatively, the approximation error between the iterates $x$ and the corresponding limiting flow $X$ is $\overset{\sim}{O}{({\eta^{1/2} + \rho})}$, that is,

The high-level intuition for the Phase II result of Theorem 5.4 is that Hessian-gradient alignment holds true for every stochastic loss $L_{k}$ along the trajectory of 1-SAM and therefore by Taylor expansion (the same argument in Section 4.3), at each step $\Phi{({x{(t)}})}$ moves towards the negative (Riemannian) gradient of $\lambda_{1}{({\nabla^{2}L_{k_{t}}})}$ where $k_{t}$ is the index of randomly sampled data, or the limiting regularizer of the worst-direction sharpness of $L_{k_{t}}$. Averaging over a long time, the moving direction becomes the negative (Riemmanian) gradient of ${\mathbb{E}}_{k_{t}}{\lbrack{\lambda_{1}{({\nabla^{2}L_{k_{t}}})}}\rbrack}$, which is the limiting regularizer of stochastic worst-direction sharpness and equals to ${Tr}{({\nabla^{2}L})}$ by Theorem 5.3.

The reason that Hessian-gradient alignment holds under 5.1 is that the Hessian of each stochastic loss $L_{k}$ at minimizers $p \in \Gamma$, ${{\nabla^{2}L_{k}}{(p)}} = {{\frac{\partial^{2}{\ell{(y^{\prime},y_{k})}}}{{({\partial y^{\prime}})}^{2}}|}_{y^{\prime} = {f_{k}{(p)}}}{\nabla f_{k}}{(p)}{({{\nabla f_{k}}{(p)}})}^{\top}}$(Lemma H.15 ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")), is exactly rank-1, which enforces the gradient ${{\nabla L_{k}}{(x)}} \approx {{\nabla^{2}L_{k}}{({\Phi{(x)}})}{({x - {\Phi{(x)}}})}}$ to (almost) lie in the top (which is also the unique) eigenspace of ${\nabla^{2}L_{k}}{({\Phi{(x)}})}$. Lemma 5.5 formally states this property.

### Lemma 5.5

Under 5.1, for any $p \in \Gamma$ and $k \in {\lbrack M\rbrack}$, it holds that ${{\nabla f_{k}}{(p)}} \neq 0$ and that there is an open set $V$ containing $p$, satisfying that

Corollaries 5.6 and 5.7 below are stochastic counterparts of Corollaries 4.6 and 4.7, saying that the trace of Hessian are close to the stochastic worst-direction sharpness along the limiting flow, and therefore when the limiting flow converges to a local minimizer of trace of Hessian, 1-SAM (Equation 17) minimizes the average-direction sharpness. We defer the proofs of Corollaries 5.6 and 5.7 to Section H.4 ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?").

### Corollary 5.6

Under the condition of Theorem 5.4, we have that with probability $1 - {O{({\sqrt{\eta} + \sqrt{\rho}})}}$, the difference between the stochastic worst-direction sharpness of the iterates and the corresponding scaled trace of Hessian along the limiting flow is at most $O\left( {{({\eta^{1/4} + \rho^{1/4}})}\rho^{2}} \right)$, that is,

### Corollary 5.7

Define $U^{\prime}$ as in Theorem 4.2, suppose ${X{(\infty)}} = {\lim\limits_{t\rightarrow\infty}{X{(t)}}}$ exists and is a minimizer of ${Tr}{(\nabla^{2}L{(x)})})$ in $U^{\prime} \cap \Gamma$. Then for all $\epsilon > 0$, there exists a constant $T_{\epsilon} > 0$, such that for all $\rho,\eta$ such that ${({\eta + \rho})}{\ln{({{1/\eta}\rho})}}$ are sufficiently small, we have that with probability $1 - {O{({\sqrt{\eta} + \sqrt{\rho}})}}$,

Finally we give a concrete counter example to demonstrate why the condition of batch size equal to one is crucial to this alignment property.

### Example 5.8

Take a simple quadratic loss ${L{(x)}} = \frac{{L_{1}{(x)}} + {L_{2}{(x)}}}{2}$, where ${L_{k}{(x)}} = {0.5x^{\top}A_{k}x}$ and $A_{k}$ is a positive definite matrix for $k = {1,2}$. If $A_{1}$ and $A_{2}$ have different top eigenspaces, then no $x$ can simultaneously satisfy that ${{\nabla L_{k}}{(x)}} = {A_{k}x}$ aligns to the top eigenvector of ${{\nabla^{2}L_{k}}{(x)}} = A_{k}$, because this implies $x$ is both an eigenvector of $A_{1}$ and $A_{2}$.

## Conclusion

In this work, we have performed a rigorous mathematical analysis of the explicit bias of various notions of sharpness when used as regularizers and the implicit bias of the SAM algorithm. In particular, we show the explicit biases of worst-, ascent- and average-direction sharpness around the manifold of minimizers are minimizing the largest eigenvalue, the smallest nonzero eigenvalue, and the trace of Hessian of the loss function. We show that in the full-batch setting, SAM provably decreases the largest eigenvalue of Hessian, while in the stochastic setting when batch size is 1, SAM provably decreases the trace of Hessian.

The most interesting future work is to generalize the current analysis for stochastic SAM to arbitrary batch size. This is challenging because, without the alignment property which holds automatically with batch size 1, such an analysis essentially requires understanding the stationary distribution of the gradient direction along the SAM trajectory. It is also interesting to incorporate other features of modern deep learning like normalization layers, momentum, and weight decay into the current analysis.

Another interesting open question is to further bridge the difference between generalization bounds and the implicit bias of the optimizers. Currently, the generalization bounds in Wu et al.; Foret et al. only work for the randomly perturbed model. Moreover, the bound depends on the average sharpness with finite $\rho$, whereas the analysis of this paper only works for infinitesimal $\rho$. It's an interesting open question whether the generalization error of the model (without perturbation) can be bounded from above by some function of the training loss, norm of the parameters, and the trace of the Hessian.
