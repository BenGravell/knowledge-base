<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How Does Sharpness-Aware Minimization Minimize Sharpness?

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sharpness-Aware Minimization (SAM) is a highly effective regularization technique for improving the generalization of deep neural networks for various settings. However, the underlying working of SAM remains elusive because of various intriguing approximations in the theoretical characterizations. SAM intends to penalize a notion of sharpness of the model but implements a computationally efficient variant; moreover, a third notion of sharpness was used for proving generalization guarantees. The subtle differences in these notions of sharpness can indeed lead to significantly different empirical results. This paper rigorously nails down the exact sharpness notion that SAM regularizes and clarifies the underlying mechanism. We also show that the two steps of approximations in the original motivation of SAM individually lead to inaccurate local conclusions, but their combination accidentally reveals the correct effect, when full-batch gradients are applied. Furthermore, we also prove that the stochastic version of SAM in fact regularizes the third notion of sharpness mentioned above, which is most likely to be the preferred notion for practical performance. The key mechanism behind this intriguing phenomenon is the alignment between the gradient and the top eigenvector of Hessian when SAM is applied.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern deep nets are often overparametrized and have the capacity to fit even randomly labeled data. Thus, a small training loss does not necessarily imply good generalization. Yet, standard gradient-based training algorithms such as SGD are able to find generalizable models. Recent empirical and theoretical studies suggest that generalization is well-correlated with the sharpness of the loss landscape at the learned parameter. Partly motivated by these studies, Foret et al.; Wu et al.; Zheng et al.; Norton & Royset propose to penalize the sharpness of the landscape to improve the generalization. We refer this method to *Sharpness-Aware Minimization* (SAM) and focus on the version of Foret et al. in this paper.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its empirical success, the underlying working of SAM remains elusive because of the various intriguing approximations made in its derivation and analysis. There are three different notions of sharpness involved --- SAM intends to optimize the first notion, the sharpness along the worst direction, but actually implements a computationally efficient notion, the sharpness along the direction of the gradient. But in the analysis of generalization, a third notion of sharpness is actually used to prove generalization guarantees, which admits the first notion as an upper bound. The subtle difference between the three notions can lead to very different biases (see Figure 1 for demonstration).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

More concretely, let $L$ be the training loss, $x$ be the parameter and $\rho$ be the *perturbation radius*, a hyperparameter requiring tuning. The first notion corresponds to the following optimization problem, where we call ${R_{\rho}^{\text{Max}}{(x)}} = {{L_{\rho}^{\text{Max}}{(x)}} - {L{(x)}}}$ the *worst-direction sharpness* at $x$. SAM intends to minimize the original training loss plus the worst-direction sharpness at $x$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, even evaluating $L_{\rho}^{\text{Max}}{(x)}$ is computationally expensive, not to mention optimization. Thus Foret et al.; Zheng et al. have introduced a second notion of sharpness, which approximates the worst-case direction in by the direction of gradient, as defined below. We call ${R_{\rho}^{\text{Asc}}{(x)}} = {{L_{\rho}^{\text{Asc}}{(x)}} - {L{(x)}}}$ the *ascent-direction sharpness* at $x$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For further acceleration, Foret et al.; Zheng et al. omit the gradient through other occurrence of $x$ and approximate the gradient of ascent-direction sharpness by gradient taken after one-step ascent, *i.e.*, ${{\nabla L_{\rho}^{\text{Asc}}}{(x)}} \approx {{\nabla L}\left( {x + {\rho\frac{{\nabla L}{(x)}}{\left\| {{\nabla L}{(x)}} \right\|_{2}}}} \right)}$ and derive the update rule of SAM, where $\eta$ is the learning rate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intriguingly, the generalization bound of SAM upperbounds the generalization error by the third notion of sharpness, called *average-direction sharpness*, $R_{\rho}^{\text{Avg}}{(x)}$ and defined formally below.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The worst-case sharpness is an upper bound of the average case sharpness and thus it is a looser bound for generalization error. In other words, according to the generalization theory in Foret et al.; Wu et al. in fact motivates us to directly minimize the average case sharpness (as opposed to the worst-case sharpness that SAM intends to optimize).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

​​Type of Sharpness-Aware Loss
​​​​ Biases (among minimizers)

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we analyze the biases introduced by penalizing these various notions of sharpness as well as the bias of SAM (Equation 3). Our analysis for SAM is performed for small perturbation radius $\rho$ and learning rate $\eta$ under the setting where the minimizers of loss form a manifold following the setup of Fehrman et al.; Li et al.. In particular, we make the following theoretical contributions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove that full-batch SAM indeed minimizes worst-direction sharpness. (Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"))

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Surprisingly, when batch size is 1, SAM minimizes average-direction sharpness. (Theorem 5.4)​

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a characterization (Theorems 4.2 and 5.3) of what a few sharpness regularizers bias towards among the minimizers (including all the three notions of the sharpness in Table 1), when the perturbation radius $\rho$ goes to zero. Surprisingly, both heuristic approximations made for SAM lead to inaccurate conclusions: Minimizing worst-direction sharpness and ascent-direction sharpness induce different biases among minimizers, and SAM doesn't minimize ascent-direction sharpness.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key mechanism behind this bias of SAM is the alignment between gradient and the top eigenspace of Hessian of the original loss in the latter phase of training---the angle between them decreases gradually to the level of $O{(\rho)}$. It turns out that the worst-direction sharpness starts to decrease once such alignment is established (see Section 4.3). Interestingly, such an alignment is not implied by the minimization problem, but rather, it is an implicit property of the specific update rule of SAM. Interestingly, such an alignment property holds for SAM with full batch and SAM with batch size one, but does not necessarily hold for the mini-batch case.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sharpness and Generalization", "weight": 1.0} -->

The study on the connection between sharpness and generalization can be traced back to Hochreiter & Schmidhuber. Keskar et al. observe a positive correlation between the batch size, the generalization error, and the sharpness of the loss landscape when changing the batch size. Jastrzebski et al. extend this by finding a correlation between the sharpness and the ratio between learning rate to batch size. Dinh et al. show that one can easily construct networks with good generalization but with arbitrary large sharpness by reparametrization. Dziugaite & Roy; Neyshabur et al.; Wei & Ma give theoretical guarantees on the generalization error using sharpness-related measures. Jiang et al. perform a large-scale empirical study on various generalization measures and show that sharpness-based measures have the highest correlation with generalization.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Implicit Bias of Sharpness Minimization", "weight": 1.0} -->

Recent theoretical works show that SGD with label noise implicitly biased toward local minimizers with a smaller trace of Hessian under the assumption that the minimizers locally connect as a manifold. Arora et al. show that normalized GD implicitly penalizes the largest eigenvalue of the Hessian. Ma et al. argues that such flatness driven phenomenon can also be caused by a multi-scale loss landscape. Lyu et al. show that GD with weight decay on a scale invariant loss function implicitly decreases penalize the spherical sharpness, *i.e.*, the largest eigenvalue of the Hessian evaluated at the normalized parameter.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Implicit Bias of Sharpness Minimization", "weight": 1.0} -->

Another line of works study the sharpness minimization effect of large learning rate assuming the (stochastic) gradient descent converges in the end of training, where the analysis is mainly based on linear stability. Recent theoretical analysis show that the sharpness minimization effect of large learning rate in gradient descent do not necessarily rely on the convergence assumption and linear stability via a four-phase characterization of the dynamics at the so-called Edge of Stability regime.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Comparison with Arora et al", "weight": 1.0} -->

Our proof uses a similar framework as Arora et al.. However, our analysis has its own difficulty for the following reasons. First, Arora et al. only deal with the deterministic case, while our analysis extends to stochastic SAM as well (Section 5). Second, our analysis for the deterministic case is different from that of Arora et al. in the following two aspects. First, the alignment analysis is more complicated because we have two hyperparameters,learning rate $\eta$ and perturbation radius $\rho$, while Arora et al. only needs to deal with one hyperparameter, learning rate $\eta$. Second, the mechanism of penalizing worst-direction sharpness is different, which can be seen from the dependency of the sharpness-reduction rate over learning rate $\eta$. In Arora et al., normalized GD reduces the sharpness via a second-order effect of GD and thus the sharpness is reduced by $O{(\eta^{2})}$ per step.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Comparison with Arora et al", "weight": 1.0} -->

In our analysis, for fixed small perturbation radius $\rho$, the sharpness is reduced by $O{({\rho^{2}\eta})}$ per step, which is linear in $\eta$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Analyzing Discrete-time Dynamics via Continuous-time Approaches", "weight": 1.0} -->

There is a long line of research that shows the trajectory of stochastic discrete iterations with decaying step size eventually tracks the solution of some ODE (see Kushner & Yin; Borkar et al.; Duchi & Ruan and the reference therein). However, those results mainly focus on the convergence property of the stochastic iterates (e.g., convergence to stationary points), while we are interested in characterizing the trajectory especially when the process is running for a long time even after the iterate reaches the neighborhood of the manifold of stationary points.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analyzing Discrete-time Dynamics via Continuous-time Approaches", "weight": 1.0} -->

Recently there has been an effort of modeling the discrete-time trajectory of (stochastic) gradient methods by continuous-time approximations. Notably, Li et al. presents a general and rigorous mathematical framework to prove such continuous-time approximation. More specifically, Li et al. proves for various stochastic gradient-based methods, the discrete-time weakly converges to the continuous-time one when LR $\eta\rightarrow 0$ in $\Theta{({1/\eta})}$ steps. The main difference between our results with these results (e.g., Theorem 9 in Li et al. ) is that we focus on a much longer training regime, *i.e.*, $T = {\Theta{({\eta^{- 1}\rho^{- 2}})}}$ steps where the previous continuous-time approximation results no longer holds throughout the entire training. As a result, their continuous approximation is only equivalent to the Phase I dynamics in our Theorems 4.5.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Analyzing Discrete-time Dynamics via Continuous-time Approaches", "weight": 1.0} -->

‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and 5.4 and cannot capture the dynamics of SAM in Phase II, when the sharpness-reduction implicit bias happens. The latter requires a more fine-grained analysis to capture the effects of higher-order terms in $\eta$ and $\rho$ in SAM Equation 3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Notations and Assumptions", "weight": 1.0} -->

For any natural number $k$, we say a function is $\mathcal{C}^{k}$ if it is $k$-times continuously differentiable and is ${\overline{\mathcal{C}}}^{k}$ if its $k$th order derivatives are locally lipschitz. We say a subset of ${\mathbb{R}}^{D}$ is compact if each of its open covers has a finite subcover. It is well known that a subset of ${\mathbb{R}}^{D}$ is compact if and only if it is closed and bounded.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Notations and Assumptions", "weight": 1.0} -->

Thus the directional derivative of $F$ along the vector $u$ at $x$ can be written as $\partial{F{(x)}u}$. We further define the second order directional derivative of $F$ along the vectors $u$ and $v$ at $x$, $\partial^{2}{F{(x)}{\lbrack u,v\rbrack}}$, $\partial{{({\partial{F \cdot u}})}{(x)}v}$, that is, the directional derivative of $\partial{F \cdot u}$ along the vector $v$ at $x$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

The connectivity of the set of local minimizers implied by the manifold assumption above allows us to take limits of perturbation radius $\rho\rightarrow 0$ while still yield interesting and insightful implicit bias results in the end-to-end analysis. So far almost all analysis of implicit bias for general model parameterizations relies on Taylor expansion, *e.g.* Blanc et al.; Damian et al.; Li et al.; Arora et al., so does the derivation of the SAM algorithm Foret et al.; Wu et al.. Thus it's crucial to consider small perturbation size $\rho$. On the contrary, if the set of global minimizers are a set of discrete points, then with small perturbation radius $\rho$, implicit bias of optimizers is not sufficient to drive the iterate from global minimum to the other one.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

It can be shown that for a minimum loss manifold, the rank of Hessian plus the dimension of the manifold is at most the environmental dimension $D$, and thus our assumption about Hessian rank essentially says the the rank is maximal. This assumption is necessary for the analysis to guarantee the differentiability of $\Phi$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.3", "weight": 1.0} -->

Though our analysis for the full-batch setting are performed under the general and abstract setting, 3.3, our analysis for stochastic setting uses a more concrete one, 5.1, where we can prove that 3.3 holds. (see Theorem 5.2)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implicit versus Explicit Bias", "weight": 1.0} -->

If an algorithm or optimizer has a bias towards certain type of global/local minima of the loss over other minima of the loss, and this bias is not encoded in the loss function, then we call such bias an implicit bias. On the other hand, a bias emerges as solely a consequence of successfully minimizing certain regularized loss regardless of the optimizers (as long as the optimzers minimize the loss), we say such bias is an *explicit bias* of the regularized loss (or the regularizer).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implicit versus Explicit Bias", "weight": 1.0} -->

As a concrete example, we will prove that full-batch SAM (Equation 3) prefers local minima with certain sharpness property. The bias stems from the particular update rule of full-batch SAM (Equation 3), and not all optimizers for the intended target loss function $L_{\rho}^{\text{Asc}}$ (Equation 2) has this bias. Therefore, it's considered as an implicit bias. As an example for explicit bias, all optimizers minimizing a loss combined with $\ell_{2}$ regularization will prefer model with smaller parameter norm and this is considered as an explicit bias of $\ell_{2}$ regularization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Usage of $O{( \\cdot )}$ Notation", "weight": 1.0} -->

Our analysis assumes small $\eta$ and $\rho$ while treating all other problem-dependent parameters as constants, such as the dimension of parameter space and the maximum possible value of derivatives (of different orders) of loss function $L$ and the limit map $\Phi$. In ${O{( \cdot )}},{\Omega{( \cdot )}},{o{( \cdot )}},{\omega{( \cdot )}},{\Theta{( \cdot )}}$, we hide all the dependency related to the problem, e.g., the (unique) initialization $x_{\text{init}}$, the manifold $\Gamma$, compact set $\overline{U^{\prime}}$ in Theorem 4.2, and the continuous time $T_{3}$ in Theorems 4.5.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Usage of $O{( \\cdot )}$ Notation", "weight": 1.0} -->

‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and 5.4, and only keep the dependency on $\rho$ and $\eta$. For example, $O{({f{(\rho)}})}$ is a placeholder for some function $g{(\rho)}$ such that there exists problem-dependent constant $C > 0$, ${{\forall\rho} > 0},{{|{g{(\rho)}}|} \leq {C{|{f{(\rho)}}|}}}$. In informal equations such as Section 4.3) via Taylor expansion.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Usage of $O{( \\cdot )}$ Notation", "weight": 1.0} -->

‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") in the proof sketch section, we are a bit more sloppy and hide dependency on $x{(t)}$ in $O{( \cdot )}$ notation as well. But these will be formally dealt with in the proofs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Ill-definedness of SAM with Zero Gradient", "weight": 1.0} -->

The update rule of SAM (Equations 3 and 17) is ill-defined when the gradient is zero. However, our analysis in Appendix B shows that when the stationary point of loss $L$, $\{ x\mid{{{\nabla L}{(x)}} = 0}\}$, is a zero-measure set, for any perturbation radius $\rho$, except for countably many learning rates, full-batch SAM is well-defined for almost all initialization and all steps (Theorem B.1). A similar result is shown for stochastic SAM if the stationary points of each stochastic loss form a zero-measure set (Theorem B.2). Thus SAM is generically well-defined. For the sake of rigorousness, when SAM encountering zero gradients, we modify the algorithm via replacing the ill-defined normalized gradient by an arbitrary vector with unit norm and our analysis for implicit bias of SAM still holds.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Explicit and Implicit Bias in the Full-Batch Setting", "weight": 1.0} -->

In this section, we present our main results in the full-batch setting. Section 4.1 provides characterization of explicit bias of *worst-direction*, *ascent-dircetion*, and average-direction sharpness. In particular, we show that ascent-direction sharpness and worst-direction sharpness have different explicit biases. However, it turns out the explicit bias of ascent-direction sharpness is not the effective bias of SAM (that approximately optimizes the ascent-direction sharpness), because the particular implementation of SAM imposes additional, different biases, which is the main focus of Section 4.2. We provide our main theorem in the full-batch setting, that SAM implicitly minimizes the worst-direction sharpness, via characterizing its limiting dynamics as learning rate $\rho$ and $\eta$ goes to $0$ with a Riemmanian gradient flow with respect to the top eigenvalue of the Hessian of the loss on the manifold of local minimizers.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Explicit and Implicit Bias in the Full-Batch Setting", "weight": 1.0} -->

In Section 4.3, we sketch the proof of the implicit bias of SAM and identify a key property behind the implicit bias, which we call the *implicit alignment* between the gradient and the top eigenvector of the Hessian.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Worst- and Ascent-direction Sharpness Have Different Explicit Biases", "weight": 1.0} -->

In this subsection, we show that the explicit biases of three notions of sharpness are all different under 3.3. We first recap the heuristic derivation of ascent-direction sharpness $R_{\rho}^{\text{Asc}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Worst- and Ascent-direction Sharpness Have Different Explicit Biases", "weight": 1.0} -->

The intuition of approximating $R_{\rho}^{\text{Max}}$ by $R_{\rho}^{\text{Asc}}$ comes from the following Taylor expansions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Worst- and Ascent-direction Sharpness Have Different Explicit Biases", "weight": 1.0} -->

Here, the preference among the local or global minima is what we are mainly concerned. Since ${\sup_{{\| v\|}_{2} \leq 1}{v^{\top}{\nabla L}{(x)}}} = \left\| {{\nabla L}{(x)}} \right\|_{2}$ when $\left\| {{\nabla L}{(x)}} \right\|_{2} > 0$, the leading terms in Equations 5 and 6 are both the first order term, $\rho\left\| {{\nabla L}{(x)}} \right\|_{2}$, and are the same. However, it is erroneous to think that the first order term decides the explicit bias, as the first order term $\left\| {{\nabla L}{(x)}} \right\|_{2}$ vanishes at the local minimizers of the loss $L$ and thus the second order term becomes the leading term.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Worst- and Ascent-direction Sharpness Have Different Explicit Biases", "weight": 1.0} -->

Any global minimizer $x$ of the original loss $L$ is an $O{(\rho^{2})}$-approximate minimizer of the sharpness-aware loss because ${{\nabla L}{(x)}} = 0$. Therefore, the sharpness-aware loss needs to be of order $\rho^{2}$ so that we can guarantee the second-order terms in Equation 5 and/or Equation 6 to be non-trivially small. Our main result in this subsection (Theorem 4.2) gives an explicit characterization for this phenomenon. The corresponding explicit biases for each type of sharpness is given below in Definition 4.1. As we will see later, they can be derived from a general notion of *limiting regularizer* (Definition 4.3. ‣ 4.1 Worst- and Ascent-direction Sharpness Have Different Explicit Biases ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")).

<!-- chunk {"id": "body-0041", "role": "body", "section": "SAM Provably Decreases Worst-direction Sharpness", "weight": 1.0} -->

Though ascent-direction sharpness has different explicit bias from worst-direction sharpness, in this subsection we will show that surprisingly, SAM (Equation 3), a heuristic method designed to minimize ascent-direction sharpness, provably decreases worst-direction sharpness. The main result here is an exact characterization of the trajectory of SAM (Equation 3) via the following ordinary differential equation (ODE) (Equation 7), when learning rate $\eta$ and perturbation radius $\rho$ are small and the initialization ${x{}} = x_{\text{init}}$ is in $U$, the attraction set of manifold $\Gamma$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "SAM Provably Decreases Worst-direction Sharpness", "weight": 1.0} -->

We assume ODE (Equation 7) has a solution till time $T_{3}$, that is, Equation 7 holds for all $t \leq T_{3}$. We call the solution of Equation 7 the *limiting flow* of SAM, which is exactly the Riemannian Gradient Flow on the manifold $\Gamma$ with respect to the loss $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$. In other words, the ODE (Equation 7) is essentially a projected gradient descent algorithm with loss $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$ on the constraint set $\Gamma$ and an infinitesimal learning rate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "SAM Provably Decreases Worst-direction Sharpness", "weight": 1.0} -->

Note $\lambda_{1}{({{\nabla^{2}L}{(x)}})}$ may not be differentiable at $x$ if ${\lambda_{1}{({{\nabla^{2}L}{(x)}})}} = {\lambda_{2}{({{\nabla^{2}L}{(x)}})}}$, thus to ensure Equation 7 is well-defined, we assume there is a positive eigengap for $L$ on $\Gamma$.^33^3In fact we only need to assume the positive eigengap along the solution of the ODE. If $\Gamma$ doesn't satisfy 4.4, we can simply perform the same analysis on its submanifold $\{{x \in \Gamma}\mid{\text{eigengap is positive at~}x}\}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 4.4", "weight": 1.0} -->

Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") is the main result of this section, which is a direct combination of Theorems G.1. ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and G.3. ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"). The proof is deferred to Section G.3 ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?").

<!-- chunk {"id": "body-0045", "role": "body", "section": "Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?\")", "weight": 1.0} -->

Now we give an overview of the analysis for the trajectory of full-batch SAM (Equation 3) in Phase II (in Theorem 4.5. ‣ 4.2 SAM Provably Decreases Worst-direction Sharpness ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")). The framework of the analysis is similar to Arora et al.; Lyu et al.; Damian et al., where the high-level idea is to use $\Phi{({x{(t)}})}$ as a proxy for $x{(t)}$ and study the dynamics of $\Phi{({x{(t)}})}$ via Taylor expansion. We will first closely follow the machinery developed in Arora et al. to arrive at Equation 11) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"), starting from which we will discuss the key innovation in this paper regarding implicit Hessian-gradient alignment.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Dynamics of $\\Phi{({x{(t)}})}$ via Taylor expansion", "weight": 1.0} -->

Using Section 4.3) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") with $x = {x{(t)}}$, plugging in Section 4.3) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") and then rearranging, we have that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Dynamics of $\\Phi{({x{(t)}})}$ via Taylor expansion", "weight": 1.0} -->

By Lemma 3.2, we have that ${\partial{\Phi{({x{(t)}})}{\nabla L}{({x{(t)}})}}} = 0$. Furthermore, by Lemma 3.5, Lemma 4.3). ‣ 3 Notations and Assumptions ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?"), we have that ${\partial{\Phi{({\Phi{({x{(t)}})}})}{\nabla^{2}L}{({\Phi{({x{(t)}})}})}}} = 0$. This implies that

<!-- chunk {"id": "body-0048", "role": "body", "section": "Dynamics of $\\Phi{({x{(t)}})}$ via Taylor expansion", "weight": 1.0} -->

Now, to understand how $\Phi{({x{(t)}})}$ moves over time, we need to understand what the direction of the RHS of Equation 11) via Taylor expansion. ‣ 4.3 Analysis Overview For Sharpness Reduction in Phase II of Theorem 4.5 ‣ 4 Explicit and Implicit Bias in the Full-Batch Setting ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?") corresponds to---we will prove that it corresponds to the Riemannian gradient of the loss function ${\nabla\lambda_{1}}{({{\nabla^{2}L}{(x)}})}$ at $x = {\Phi{({x{(t)}})}}$. To achieve this, the key is to understand the direction $\frac{{\nabla L}{({x{(t)}})}}{\left\| {{\nabla L}{({x{(t)}})}} \right\|_{2}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Dynamics of $\\Phi{({x{(t)}})}$ via Taylor expansion", "weight": 1.0} -->

where the second to last step we use the property of the derivative of eigenvalue (Lemma I.7). ‣ Appendix I Technical Lemmas ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) and the last step is due to Taylor expansion of $\partial{\Phi{( \cdot )}{\nabla\lambda_{1}}{({{\nabla^{2}L}{( \cdot )}})}}$ at $\Phi{({x{(t)}})}$ and the fact that $\left\| {{\Phi{({x{(t)}})}} - {x{(t)}}} \right\| = {O{({\eta\rho})}}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Implicit Hessian-gradient Alignment", "weight": 1.0} -->

It remains to explain why the gradient implicitly aligns to the top eigenvector of the Hessian, which is the key component of the analysis in Phase II. The proof strategy here is to first show alignment for a quadratic loss function, and then generalize its proof to general loss functions satisfying 3.3. Below we first give the formal statement of the implicit alignment on quadratic loss, Theorem 4.8 and defer the result for general case (Lemma G.19 ‣ Appendix G Analysis for Full-batch SAM on General Loss (Proof of Theorem 4.5) ‣ How Does Sharpness-Aware Minimization Minimize Sharpness?")) to appendix. Note this alignment property is an implicit property of the SAM algorithm as it is not explicitly enforced by the objective that SAM is intended to minimize, $L_{\rho}^{\text{Asc}}$. Indeed optimizing $L_{\rho}^{\text{Asc}}$ would rather explicitly align gradient to the smallest non-zero eigenvector (See proofs of Theorem E.5)!

<!-- chunk {"id": "body-0051", "role": "body", "section": "Explicit and Implicit Biases in the Stochastic Setting", "weight": 1.0} -->

In practice, people usually use SAM in the stochastic mini-batch setting, and the test accuracy improves as the batch size decreases. Towards explaining this phenomenon, Foret et al. argue intuitively that stochastic SAM minimizes stochastic worst-direction sharpness. Given our results in Section 4, it is natural to ask if we can justify the above intuition by showing the Hessian-gradient alignment in the stochastic setting. Unfortunately, such alignment is not possible in the most general setting. Yet when the batch size is 1, we can prove rigorously in Section 5.2 that stochastic SAM minimizes *stochastic worst-direction sharpness*, which is the expectation of the worst-direction sharpness of loss over each data (defined in Section 5.1), which is the main result in this section. We stress that the stochastic worst-direction sharpness has a different explicit bias to the worst-direction sharpness, which full-batch SAM implicitly penalizes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Explicit and Implicit Biases in the Stochastic Setting", "weight": 1.0} -->

When perturbation radius $\rho\rightarrow 0$, the former corresponds to ${Tr}{({{\nabla^{2}L}{( \cdot )}})}$, the same as average-direction sharpness, and the latter corresponds to $\lambda_{1}{({{\nabla^{2}L}{( \cdot )}})}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Explicit and Implicit Biases in the Stochastic Setting", "weight": 1.0} -->

Below we start by introducing our setting for SAM with batch size $1$, or $1$*-SAM*. We still need 3.3 in this section. We first analyze the explicit bias of the stochastic ascent- and worst-direction sharpness in Section 5.1 via the tools developed in Section 4.1. It turns out they are all proportional to the trace of hessian as $\rho\rightarrow 0$. In Section 5.2, we show that 1-SAM penalizes the trace of Hessian. Below we formally state our setting for stochastic loss of batch size one (5.1).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Setting 5.1", "weight": 1.0} -->

We remark that given training data (*i.e.*, ${\{ f_{k}\}}_{k = 1}^{M}$), $\Gamma$ defined above is just equal to the set of global minimizers, $\left\{ {x \in {\mathbb{R}}^{D}}\mid{{{f_{k}{(x)}} = y_{k}},{{\forall k} \in {\lbrack M\rbrack}}} \right\}$, except for a zero measure set of labels ${(y_{k})}_{k = 1}^{M}$ when $f_{k}$ are $\mathcal{C}^{\infty}$ smooth, by Sard's Theorem. Thus Cooper argued that the global minimizers form a differentiable manifold generically if we allow perturbation on the labels. In this work we do not make such an assumption for labels. Instead, we consider the subset of the global minimizers with full-rank Jacobian, $\Gamma$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Setting 5.1", "weight": 1.0} -->

A standard application of implicit function theorem implies that $\Gamma$ defined in 5.1 is indeed a manifold. (See Theorem 5.2, whose proof is deferred into Section C.1)

<!-- chunk {"id": "body-0056", "role": "body", "section": "1-SAM", "weight": 1.0} -->

We use $1$*-SAM* as a shorthand for SAM on a stochastic loss with batch size $1$ as below Equation 17, where $k_{t}$ is sampled i.i.d from uniform distribution on $\lbrack M\rbrack$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Stochastic Worst-, Ascent- and Average- direction Sharpness Have the Same Explicit Biases as Average Direction Sharpness", "weight": 1.0} -->

We further use *stochastic worst-, ascent- and average-direction sharpness* to denote ${{\mathbb{E}}_{k}{\lbrack R_{k,\rho}^{\text{Max}}\rbrack}},{{\mathbb{E}}_{k}{\lbrack R_{k,\rho}^{\text{Asc}}\rbrack}}$ and ${\mathbb{E}}_{k}{\lbrack R_{k,\rho}^{\text{Avg}}\rbrack}$. Unlike the full-batch setting, these three sharpness notions have the same explicit biases, or more precisely, they have the same limiting regularizers (up to some scaling factor).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Stochastic SAM Minimizes Average-direction Sharpness", "weight": 1.0} -->

This subsection aims to show that the implicit bias of 1-SAM (Equation 17) is minimizing the average-direction sharpness for small perturbation radius $\rho$ and learning rate $\eta$, which has the same implicit bias as all three notions of stochastic sharpness do (Theorem 5.3). As an analog of the analysis in Section 4.3, which shows full-batch SAM minimizes worst-direction sharpness, analysis in this section conceptually shows that 1-SAM minimizes the stochastic worst-direction sharpness.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Stochastic SAM Minimizes Average-direction Sharpness", "weight": 1.0} -->

Mathematically, we prove that the trajectory of 1-SAM tracks the following Riemannian gradient flow (Equation 18) with respect to their limiting regularize ${Tr}{({{\nabla^{2}L}{( \cdot )}})}$ on the manifold for sufficiently small $\eta$ and $\rho$ and thus penalizes stochastic worst-direction sharpness (of batch size $1$). We assume the ODE (Equation 18) has a solution till time $T_{3}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have performed a rigorous mathematical analysis of the explicit bias of various notions of sharpness when used as regularizers and the implicit bias of the SAM algorithm. In particular, we show the explicit biases of worst-, ascent- and average-direction sharpness around the manifold of minimizers are minimizing the largest eigenvalue, the smallest nonzero eigenvalue, and the trace of Hessian of the loss function. We show that in the full-batch setting, SAM provably decreases the largest eigenvalue of Hessian, while in the stochastic setting when batch size is 1, SAM provably decreases the trace of Hessian.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The most interesting future work is to generalize the current analysis for stochastic SAM to arbitrary batch size. This is challenging because, without the alignment property which holds automatically with batch size 1, such an analysis essentially requires understanding the stationary distribution of the gradient direction along the SAM trajectory. It is also interesting to incorporate other features of modern deep learning like normalization layers, momentum, and weight decay into the current analysis.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Another interesting open question is to further bridge the difference between generalization bounds and the implicit bias of the optimizers. Currently, the generalization bounds in Wu et al.; Foret et al. only work for the randomly perturbed model. Moreover, the bound depends on the average sharpness with finite $\rho$, whereas the analysis of this paper only works for infinitesimal $\rho$. It's an interesting open question whether the generalization error of the model (without perturbation) can be bounded from above by some function of the training loss, norm of the parameters, and the trace of the Hessian.
