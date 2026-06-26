<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Near-optimal Local Convergence of Alternating Gradient Descent-Ascent for Minimax Optimization

Topics include Gradient descent, Optimization, SCSC, IQC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Smooth minimax games often proceed by simultaneous or alternating gradient updates. Although algorithms with alternating updates are commonly used in practice, the majority of existing theoretical analyses focus on simultaneous algorithms for convenience of analysis. In this paper, we study alternating gradient descent-ascent (Alt-GDA) in minimax games and show that Alt-GDA is superior to its simultaneous counterpart~(Sim-GDA) in many settings. We prove that Alt-GDA achieves a near-optimal local convergence rate for strongly convex-strongly concave (SCSC) problems while Sim-GDA converges at a much slower rate. To our knowledge, this is the first result of any setting showing that Alt-GDA converges faster than Sim-GDA by more than a constant. We further adapt the theory of integral quadratic constraints (IQC) and show that Alt-GDA attains the same rate globally for a subclass of SCSC minimax problems. Empirically, we demonstrate that alternating updates speed up GAN training significantly and the use of optimism only helps for simultaneous algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Since the seminal work of von Neumann, minimax optimization in the form of ${\min_{\mathbf{x}}{\max_{\mathbf{y}}f}}{(\mathbf{x},\mathbf{y})}$ has been a major focus of research in mathematics, economics and computer science. Recently, minimax optimization has gained tremendous attention in machine learning as it offers a flexible paradigm that goes beyond ordinary loss function minimization. In particular, there is an increasing set of models that can be formulated as minimax problems, including (but not limited to) generative adversarial networks, adversarial training, robust optimization and primal-dual reinforcement learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The most natural and frequently used method for solving minimax problems is a generalization of gradient descent known as gradient descent-ascent (GDA), with either simultaneous or alternating updates of the two players, referred to as Sim-GDA and Alt-GDA, respectively, throughout the sequel. Unlike gradient descent, which converges to a local minimum for minimization problems under a broad range of conditions, it is known that GDA with constant step-sizes can fail to converge for general smooth functions, even for unconstrained bilinear games. Even when it does converge, GDA may exhibit rotational behaviors and hence converge slowly (see Figure 1). To combat these issues, several algorithms have been introduced specifically for smooth minimax games, including consensus optimization, symplectic gradient adjustment, negative momentum (NM), optimistic gradient descent-ascent (OGDA) and extra-gradient (EG).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In theory, many of these algorithms enjoy improved convergence rates compared to GDA. In particular, both OGDA and EG are near-optimal for SCSC minimax problems. However, in practice, GDA and its adaptive variants are still the go-to algorithms for many applications (e.g., GAN optimization and offline policy evaluation ). Here, the catch is that the overwhelming majority of existing theoretical analyses focus on simultaneous algorithms where players update their strategies at the same time, as simultaneous updates are easier to analyze and can often be formulated as solving a variational inequality problem. This is in stark contrast to our common practice where alternating algorithms are actually used. Nonetheless, our understanding of alternating algorithms in minimax optimization is severely limited to simple bilinear games. Despite it being a very natural question to ask, the convergence properties of Alt-GDA for SCSC minimax games and many other settings remain largely unknown. The key difficulty is that every iteration of an alternating algorithm is a composition of two half updates, which greatly complicates analysis.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our contributions. In this paper, we take a step towards understanding Alt-GDA and closing the gap between theory and practice. We first revisit the convergence properties of Alt-GDA in bilinear games for completeness. We then discuss our main contributions on proving near-optimal convergence rates of Alt-GDA. In more detail: We prove that, for SCSC minimax games^11^1The SCSC setting is fundamental. Via reduction, an efficient algorithm for this setting implies efficient algorithms for other settings, including strongly convex-concave, convex-concave, and non-convex-concave settings., Alt-GDA achieves an iteration complexity of $\mathcal{O}{(\kappa)}$ locally ($\kappa$ is the condition number), which is quadratically better than the $\mathcal{O}{(\kappa^{2})}$ bound for Sim-GDA and even matches EG/OGDA. Importantly, the complexity bound for Alt-GDA in this setting is near-optimal as it matches the coarse lower bound.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We further prove that both Sim-GDA and Alt-GDA attain linear convergence when the minimax problem has only strong concavity in $\mathbf{y}$ but no strong convexity in $\mathbf{x}$ by assuming non-singularity of the coupling matrix.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We show that Alt-GDA can converge with the same rate $\mathcal{O}{(\kappa)}$ globally for a class of SCSC minimax games with a bilinear coupling term. This is done by using theory of IQC to automatically search for a Lyapunov function.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Lastly, we validate our theory on quadratic minimax games. Empirically, we demonstrate that alternating updates could speed up GAN training dramatically (which matches the existing results in Goodfellow et al.; Radford et al. ) and perform on par with optimistic updates though GAN objective is generally nonconvex-nonconcave.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Two-player Minimax Games", "weight": 1.0} -->

We begin by presenting the fundamental two-player zero-sum game that we will consider in the sequel. To be specific, our problem of interest is the following unconstrained minimax optimization problem: We are usually interested in finding a *Nash equilibrium*: a set of parameters from which no player can (unilaterally) improve its objective function. In this work, we focus on the case of $f$ being a convex-concave and smooth function. Here we state the assumption formally.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The function $f$ is continuously differentiable and $L$-smooth in $\mathbf{x}$ and $\mathbf{y}$. Furthermore, we assume $f$ is convex in $\mathbf{x}$ and concave in $\mathbf{y}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For completeness, we state the definition of smooth function. We note that the smoothness assumption is standard for convergence analysis in the literature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Local Convergence Rates", "weight": 1.0} -->

We stress that local convergence analysis has been widely adopted in smooth game optimization (see e.g., Gidel et al.; Wang et al.; Azizian et al.; Zhang and Wang; Liang and Stokes; Fiez and Ratliff ). Under certain conditions on a fixed point operator $F$, linear convergence is guaranteed in a neighborhood around a fixed point $\mathbf{z}^{\ast}$ (i.e. local convergence).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Revisiting Alt-GDA for Bilinear Games", "weight": 1.0} -->

In this section, we revisit the unconstrained bilinear games for which Sim-GDA diverges with any finite step size. Formally, the bilinear game is given by where we ignore the linear terms without loss of generality. Here, the Nash equilibrium is $(\mathbf{x}^{\ast},\mathbf{y}^{\ast})$ satisfying ${\mathbf{B}^{\top}\mathbf{x}^{\ast}} = \mathbf{0}$ and ${\mathbf{B}\mathbf{y}}^{\ast} = \mathbf{0}$. To measure convergence, one could monitor the distance to the equilibrium: We aim to understand the difference between the dynamics of simultaneous and alternating methods. Practitioners have been widely using the latter instead of the former when optimizing GANs despite the rich optimization literature on simultaneous methods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Bilinear games, as discussed previously, are somewhat simplistic in that they obey a conservation law and can be easily solved by performing gradient descent on the Hamiltonian. In this section, we consider a different class of games whose Jacobian has both symmetric and antisymmetric components, and are therefore arguably harder to solve. In particular, we assume $f{(\mathbf{x},\mathbf{y})}$ is SCSC and smooth, which implies We let $L \triangleq {\max{\{ L_{\mathbf{x}},L_{\mathbf{y}},L_{\mathbf{x}\mathbf{y}}\}}}$ and $\mu \triangleq {\min{\{\mu_{\mathbf{x}},\mu_{\mathbf{y}}\}}}$ and define the condition number $\kappa \triangleq {L/\mu}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Accordingly, one can define $\kappa_{\mathbf{x}} \triangleq {L/\mu_{\mathbf{x}}}$ and $\kappa_{\mathbf{y}} \triangleq {L/\mu_{\mathbf{y}}}$. We now briefly summarize some known results about convergence of Sim-GDA in this setting. The worst-case convergence rate of Sim-GDA reduces to $\rho{({\mathbf{I} - {\eta{\nabla V}{(\mathbf{z}^{\ast})}}})}$, which is equivalent to where $\mathcal{K}$ is the support of the eigenvalues of the Jacobian of the gradient vector field $V$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

It can be shown that $\mathcal{K} = \left\{ {\lambda \in {\mathbb{C}}}:{{{|\lambda|} \leq {\sqrt{2}L}},{{\Re\lambda} \geq \mu > 0}} \right\}$ (see Appendix A.2). This set is the intersection between a circle and a halfplane. Eqn. leaves open the choice of $\eta$, and it is known that the presence of large imaginary eigenvalues of the Jacobian forces a small value of $\eta$, thereby limiting the rate of convergence.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In stark contrast to Sim-GDA, for which the complex eigenvalues of $\nabla F_{\eta}^{\text{Sim}}$ can have magnitude as large as $\sqrt{{1 - {2\eta\mu}} + {2\eta^{2}L^{2}}}$, the complex eigenvalues of $\nabla F_{\eta}^{\text{Alt}}$ are much smaller in magnitude and are even smaller than the real eigenvalues as shown in Theorem 5. As a result, we are allowed to use a larger step size, which gives an improved convergence rate (see Figure 2 for details).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Following immediately from Theorem 5, we have the following Corollary. {cor} With $\eta = \frac{1}{2L}$, we have ${\rho{({{\nabla F_{\eta}^{\text{Alt}}}{(\mathbf{z}^{\ast})}})}} \leq {1 - \frac{1}{2\kappa}}$. Hence by Theorem 1). ‣ 2.3 Local Convergence Rates ‣ 2 PRELIMINARIES"), Alt-GDA converges locally at a linear rate $\mathcal{O}\left( \left( {{1 - \frac{1}{2\kappa}} + \epsilon} \right)^{t} \right)$ with $\epsilon > 0$ an arbitrarily small constant.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In particular, this corollary suggests that the iteration complexity of Alt-GDA matches the coarse lower iteration complexity bound^33^3The fine-grained bound is $\Omega{(\sqrt{\kappa_{\mathbf{x}}\kappa_{\mathbf{y}}})}$. One could achieve this bound by using a accelerated proximal point framework with Alt-GDA in the inner-loop. $\Omega{(\kappa)}$ up to a constant, implying Alt-GDA is near-optimal (at least locally). This is the *first* time that one can rigorously show the Alt-GDA converges faster than Sim-GDA by more than a constant, let alone quadratically faster.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Furthermore, it implies that the convergence rate of Alt-GDA is no worse than its rate for pure cooperative games with $\mathbf{B} \triangleq {\nabla_{\mathbf{x}\mathbf{y}}^{2}f} = \mathbf{0}$. Put differently, the adversarial component (the existence of coupling matrix $\mathbf{B}$) does *not* make the optimization any harder for Alt-GDA. We remark that this is *not* true for Sim-GDA because in that case, the coupling matrix $\mathbf{B}$ introduces complex eigenvalues with large imaginary parts, which slow down convergence.

<!-- chunk {"id": "body-0022", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

We have shown that Alt-GDA achieves a near-optimal local convergence rate for SCSC minimax games. In this section, we further consider the case that has only strong concavity in the player $\mathbf{y}$ but *no* strong convexity in $\mathbf{x}$. In particular, it is equivalent to assuming This setting was investigated in empirical policy evaluation where no strong convex regularization is applied on the primal variables. They showed that the non-singularity of the coupling matrix $\mathbf{B} \triangleq {{\nabla_{\mathbf{x}\mathbf{y}}^{2}f}{(\mathbf{x}^{\ast},\mathbf{y}^{\ast})}}$ can help achieve linear convergence for Sim-GDA.

<!-- chunk {"id": "body-0023", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

So far, we derived local convergence rates of Alt-GDA in different settings. Nonetheless, the global convergence results remain largely unknown. Unlike local convergence analysis, we have to switch to Lyapunov theory for global convergence analysis. Finding a right Lyapunov function for Alt-GDA turns out to be extremely hard and we resort to integral quadratic constraints (IQC) theory for a computer-aided proof^44^4See the blog by Adrien Taylor for more details about computer-aided analyses.. Basically, we view the algorithm as an interconnected dynamical system with nonlinear feedback (i.e., the gradient) and model the nonlinear feedback with quadratic constraints^55^5Both convexity and smoothness can be characterized tightly with quadratic constraints.. Then it allows us to *automatically* search for a quadratic Lyapunov function for certifying the worst-case convergence rate by solving a semi-definite program (SDP). Due to space constraints, we refer the reader to Appendix B for all the details.

<!-- chunk {"id": "body-0024", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

In particular, we analyze Alt-GDA for bilinearly-coupled minimax games with the following form: where we assume both $f$ and $g$ are $\mu$-strongly-convex and $L$-smooth, ${\|\mathbf{B}\|}_{2} \leq L$. This problem is a special case of the minimax games that is amenable to IQC analysis. This problem has been studied extensively Chambolle and Pock; Du and Hu; Xie et al.. However, the convergence properties of Alt-GDA again remain unknown.

<!-- chunk {"id": "body-0025", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

Using the IQC framework, we are able to search for the best possible convergence rate of Alt-GDA for every given condition number $\kappa$ by solving a SDP. However, the size of the SDP is proportional to $m$ and $n$. This can be problematic in cases where $m$ (or $n$) is large because it can be computationally costly to solve large SDPs. Fortunately, we prove that the high dimensional problem isn't any harder than than the case of $m = n = 1$, so we can reduce the problem to a SDP with $m = n = 1$, which is easy to solve.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

In this section, we compare the performance of Alt-GDA with Sim-GDA along with other three popular algorithms (EG, OGDA and NM) so as to verify our theoretical results on the convergence rate of Alt-GDA. In particular, we focus on the following quadratic minimax problem: where we set the dimension $d = 100$. We note both linear regression and robust least squares problems admit this minimax formulation. The matrices $\mathbf{A}$ and $\mathbf{C}$ are set to have eigenvalues ${\{\frac{1}{i}\}}_{i = 1}^{d}$. For matrix $\mathbf{B}$, we set it to be a random matrix with entries sampling from a Gaussian distribution (either $\mathcal{N}{(0,0.01)}$ or $\mathcal{N}{}$).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

In the case of $\mathbf{B}$ sampled from $\mathcal{N}{}$, the resulting gradient vector field has a strong rotational force since the off-diagonal blocks of its Jacobian dominates (see in the Appendix). For all algorithms, the iterates start with $\mathbf{x}_{0} = \mathbf{1}$ and $\mathbf{y}_{0} = \mathbf{1}$. Figure 4 shows that the distance to the optimum of Sim-GDA, Alt-GDA, OGDA, EG and NM^66^6We implemented the simultaneous version of negative momentum (NM). For alternating NM, the optimal damping value of NM is roughly zero, making it the same algorithm as Alt-GDA. versus the number of iterations for this problem. For all methods, we tune their hyperparameters by grid-search. We notice that all methods converge linearly to the optimum. As expected, Alt-GDA performs significantly better than Sim-GDA and yields a convergence rate that is better than its worst-case rate (black dashed line).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

Moreover, we find that Alt-GDA outperforms OGDA and EG by a visible margin. This is surprising, in that OGDA and EG take another memory buffer for accelerating the convergence.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

Furthermore, we study how the convergence rates (or iteration complexities) scale with the condition numbers. To this end, we randomly sample^77^7We let the eigenvalues of matrices $\mathbf{A}$ and $\mathbf{C}$ be ${\{\frac{1}{n_{i}}\}}_{i = 1}^{d}$ where $n_{i}$ are evenly spaced from $1$ to $N$, where $N$ is in $\lbrack\sqrt{10},10^{3}\rbrack$. We sample all entries of $\mathbf{B}$ from standard normal distribution $\mathcal{N}{}$ and then normalize it.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

matrices $\mathbf{A},\mathbf{B},\mathbf{C}$ and compute the condition number by $\kappa = \frac{\max{\{{|\lambda_{i}|}\}}}{\min{\{{\Re{(\lambda_{i})}}\}}}$ where $\lambda_{i}$ are eigenvalues of the Jacobian $\mathbf{J}$ of the gradient vector field. Once we have all these three matrices, we can compute the spectral radius $\rho$ of all algorithms with tuned step-sizes and momentum value. We plot $- {1/{\log{(\rho)}}}$ versus the condition number $\kappa$ in Figure 4 (right) to get a sense of how the relative iteration complexity scales as a function of condition number.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

We find that the iteration complexity of Alt-GDA scales linearly with the condition number, matching our prediction in Corollary 3. On the other hand, Sim-GDA takes roughly $\kappa^{2}$ iterations to convergence, as predicted in Theorem 4. In addition, Alt-GDA is slightly better than OGDA and EG as its curve is below that of OGDA and EG, albeit with the same slope.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

In this section, we investigate the effect of alternating updates on training generative adversarial networks. The purpose of this section is to show that the insights gained from our analyses carry over to GAN training despite the fact that the GAN objective is generally nonconvex-nonconcave. In addition, we note that while GAN training is a stochastic problem, stochastic problems are sometimes in a curvature-dominated regime where the convergence behavior resembles that of the deterministic problems.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

We first compare alternating algorithms with their simultaneous counterparts on image generation task with the WGAN-GP objective and a DCGAN architecture. In particular, we choose SGD and AMSGrad as our base optimizers. For more implementation details, please see Appendix D. We evaluate all algorithms with Fréchet Inception Distance^88^8Inception score is also a popular metric, however it was shown by Chavdarova et al. that it is less consistent with the sample quality, so we instead use FID score here. (FID). Figure 5(c) and 5(d) summarize our results. With SGD as our optimizer^99^9We also include the results with exponential moving average (EMA)., we observe that alternating SGD not only converges faster, but also converges to a better point with lower FID score. Although both alternating version and simultaneous version of AMSGrad converges to models with similar FID scores, the alternating version again converges with many fewer iterations, matching our prediction. In addition, we generate samples from trained Generators at iteration 30000 with SGD optimizer (see Figure 5(a) and 5(b)).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

It is easy to see that the model trained with alternating updates generates better samples given the same compute budget.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

Furthermore, we compare simultaneous methods and alternating methods on a deep ResNet. We also include optimistic updates in the training, which is the key component of OGDA^1010^10See Appendix D for detailed update rule.. We report all results in Figure 6. The first observation is that alternating algorithms take fewer iterations to converge regardless of whether optimism is used, and sometimes converge to models with better FID scores (similar to DCGAN results). Second, we observe that the use of optimism only helps for simultaneous algorithms, suggesting that alternating updates and optimistic updates play similar roles in improving GAN training. This could be explained by our theoretical results that Alt-GDA enjoys a similar convergence rate to OGDA.

<!-- chunk {"id": "body-0036", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this paper, we take an important step towards understanding alternating algorithms in minimax optimization by analyzing Alt-GDA in three distinct settings. In particular, we show theoretically that Alt-GDA outperforms its simultaneous counterpart by a big margin in all three settings. Unexpectedly, Alt-GDA achieves a near-optimal convergence rate locally for strongly convex-strongly concave smooth minimax games, matching the known coarse lower bound. Moreover, the acceleration effect of Alt-GDA remains when the minimax problem has only strong concavity in the dual variables.

<!-- chunk {"id": "body-0037", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Our numerical simulations on toy quadratic games verified our claims. Further, we demonstrate empirically that alternating updates could significantly speed up GAN training though GAN objective is generally nonconvex-nonconcave. More interestingly, we show that the use of optimism only helps for simultaneous algorithms. We believe that the default use of alternating update rule in GAN training was an important reason for its success.
