<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Near-optimal Local Convergence of Alternating Gradient Descent-Ascent for Minimax Optimization

Topics include Gradient descent, Optimization, SCSC, IQC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Smooth minimax games often proceed by simultaneous or alternating gradient updates. Although algorithms with alternating updates are commonly used in practice, the majority of existing theoretical analyses focus on simultaneous algorithms for convenience of analysis. In this paper, we study alternating gradient descent-ascent (Alt-GDA) in minimax games and show that Alt-GDA is superior to its simultaneous counterpart~(Sim-GDA) in many settings. We prove that Alt-GDA achieves a near-optimal local convergence rate for strongly convex-strongly concave (SCSC) problems while Sim-GDA converges at a much slower rate. To our knowledge, this is the first result of any setting showing that Alt-GDA converges faster than Sim-GDA by more than a constant. We further adapt the theory of integral quadratic constraints (IQC) and show that Alt-GDA attains the same rate globally for a subclass of SCSC minimax problems. Empirically, we demonstrate that alternating updates speed up GAN training significantly and the use of optimism only helps for simultaneous algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Since the seminal work of von Neumann[neumann1928theorie], minimax optimization in the form of $\min_\mathbf{x} \max_\mathbf{y} f(\mathbf{x}, \mathbf{y})$ has been a major focus of research in mathematics, economics and computer science[von1944theory, bacsar1998dynamic, roughgarden2010algorithmic]. Recently, minimax optimization has gained tremendous attention in machine learning as it offers a flexible paradigm that goes beyond ordinary loss function minimization. In particular, there is an increasing set of models that can be formulated as minimax problems, including (but not limited to) generative adversarial networks[goodfellow2014generative, arjovsky2017wasserstein], adversarial training[madry2018towards], robust optimization[ben2009robust] and primal-dual reinforcement learning[du2017stochastic, yang2020off].

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The most natural and frequently used method for solving minimax problems is a generalization of gradient descent known as gradient descent-ascent (GDA), with either simultaneous or alternating updates of the two players, referred to as Sim-GDA and Alt-GDA, respectively, throughout the sequel. Unlike gradient descent, which converges to a local minimum for minimization problems under a broad range of conditions [lee2016gradient, lee2017first], it is known that GDA with constant step-sizes can fail to converge for general smooth functions[mescheder2017numerics], even for unconstrained bilinear games[gidel2019negative, bailey2018multiplicative]. Even when it does converge, GDA may exhibit rotational behaviors[mescheder2017numerics, letcher2019differentiable, florian2019competitive] and hence converge slowly (see Figure[fig:fig1]).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To combat these issues, several algorithms have been introduced specifically for smooth minimax games, including consensus optimization[mescheder2017numerics], symplectic gradient adjustment[letcher2019differentiable], negative momentum (NM)[gidel2019negative, zhang2020suboptimality], optimistic gradient descent-ascent (OGDA)[popov1980modification, rakhlin2013optimization, daskalakis2018training, mertikopoulos2018optimistic] and extra-gradient (EG)[korpelevich1976extragradient].

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In theory, many of these algorithms enjoy improved convergence rates compared to GDA. In particular, both OGDA and EG are near-optimal for SCSC minimax problems However, in practice, GDA and its adaptive variants are still the go-to algorithms for many applications (e.g., GAN optimization and offline policy evaluation[yang2020off]). Here, the catch is that the overwhelming majority of existing theoretical analyses focus on simultaneous algorithms where players update their strategies at the same time, as simultaneous updates are easier to analyze and can often be formulated as solving a variational inequality problem[harker1990finite, gidel2018variational, zhang2020unified]. This is in stark contrast to our common practice where alternating algorithms are actually used. Nonetheless, our understanding of alternating algorithms in minimax optimization is severely limited to simple bilinear games. Despite it being a very natural question to ask, the convergence properties of Alt-GDA for SCSC minimax games and many other settings remain largely unknown. The key difficulty is that every iteration of an alternating algorithm is a composition of two half updates, which greatly complicates analysis.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we take a step towards understanding Alt-GDA and closing the gap between theory and practice. We first revisit the convergence properties of Alt-GDA in bilinear games for completeness. We then discuss our main contributions on proving near-optimal convergence rates of Alt-GDA.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- We prove that, for SCSC minimax games The SCSC setting is fundamental. Via reduction, an efficient algorithm for this setting implies efficient algorithms for other settings, including strongly convex-concave, convex-concave, and non-convex-concave settings. -, Alt-GDA achieves an iteration complexity of $\mathcal{O}(\kappa)$ locally ($\kappa$ is the condition number), which is quadratically better than the $\mathcal{O}(\kappa^2)$ bound for Sim-GDA and even matches EG/OGDA. Importantly, the complexity bound for Alt-GDA in this setting is near-optimal as it matches the coarse lower bound in[azizian2020accelerating]. - We further prove that both Sim-GDA and Alt-GDA attain linear convergence when the minimax problem has only strong concavity in $\mathbf{y}$ but no strong convexity in $\mathbf{x}$ by assuming non-singularity of the coupling matrix.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- We show that Alt-GDA can converge with the same rate $\mathcal{O}(\kappa)$ globally for a class of SCSC minimax games with a bilinear coupling term. This is done by using theory of IQC to automatically search for a Lyapunov function. - Lastly, we validate our theory on quadratic minimax games. Empirically, we demonstrate that alternating updates could speed up GAN training dramatically (which matches the existing results in [goodfellow2014generative, radford2015unsupervised]) and perform on par with optimistic updates though GAN objective is generally nonconvex-nonconcave.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Two-player Minimax Games", "weight": 1.0} -->

We begin by presenting the fundamental two-player zero-sum game that we will consider in the sequel. To be specific, our problem of interest is the following unconstrained minimax optimization problem: $$\min_{\mathbf{x} \in \mathbb{R}^m} \max_{\mathbf{y} \in \mathbb{R}^n} f(\mathbf{x}, \mathbf{y}).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Two-player Minimax Games", "weight": 1.0} -->

We are usually interested in finding a Nash equilibrium[von1944theory]: a set of parameters from which no player can (unilaterally) improve its objective function. In this work, we focus on the case of $f$ being a convex-concave and smooth function. Here we state the assumption formally.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Two-player Minimax Games", "weight": 1.0} -->

The function $f$ is continuously differentiable and $L$-smooth in $\mathbf{x}$ and $\mathbf{y}$. Furthermore, we assume $f$ is convex in $\mathbf{x}$ and concave in $\mathbf{y}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Two-player Minimax Games", "weight": 1.0} -->

For completeness, we state the definition of smooth function. We note that the smoothness assumption is standard for convergence analysis in the literature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Two-player Minimax Games", "weight": 1.0} -->

One of the nice properties of working with convex-concave problems is that there often exists at least one global Nash equilibrium $(\mathbf{x}^*, \mathbf{y}^*)$ such that for any $\mathbf{x} \in \mathbb{R}^m, \mathbf{y} \in \mathbb{R}^n$ we have $$f(\mathbf{x}^*, \mathbf{y}) \leq f(\mathbf{x}^*, \mathbf{y}^*) \leq f(\mathbf{x}, \mathbf{y}^*).$$

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gradient Descent-Ascent Family", "weight": 1.0} -->

We now present two algorithms we will discuss in this paper, Sim-GDA and Alt-GDA. The de-facto standard algorithm for finding Nash equilibria of general smooth two-player minimax games is simultaneous gradient descent-ascent (Sim-GDA) which is a direct generalization of gradient descent to minimax games. In particular, it updates both players $\mathbf{x}$ and $\mathbf{y}$ simultaneously: \mathbf{x}_{t+1} &= \mathbf{x}_t - \eta \nabla_\mathbf{x} f(\mathbf{x}_t, \mathbf{y}_t), \\\mathbf{y}_{t+1} &= \mathbf{y}_t + \eta \nabla_\mathbf{y} f(\mathbf{x}_t, \mathbf{y}_t), where $\eta$ is the step size Using separate step sizes for two players does not improve the worst-case convergence rate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gradient Descent-Ascent Family", "weight": 1.0} -->

Succinctly, Sim-GDA updates [eq:sim-gda-update] can be defined as the repeated application of a nonlinear operator in the form of $\mathbf{z}_{t+1} = F_\eta^\textup{Sim}(\mathbf{z}_t) \triangleq \mathbf{z}_t - \eta V(\mathbf{z}_t)$ with $\mathbf{z} = [\mathbf{x}^\top, \mathbf{y}^\top]^\top$ and $V(\mathbf{z}) = [\nabla_\mathbf{x} f(\mathbf{x}, \mathbf{y})^\top, -\nabla_\mathbf{y} f(\mathbf{x}, \mathbf{y})^\top]^\top$, the gradient vector field.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Local Convergence Rates", "weight": 1.0} -->

We stress that local convergence analysis has been widely adopted in smooth game optimization (see e.g.,[gidel2019negative, wang2019solving, azizian2020accelerating, zhang2020suboptimality, liang2019interaction, fiez2020gradient]). Under certain conditions on a fixed point operator $F$, linear convergence is guaranteed in a neighborhood around a fixed point $\mathbf{z}^*$ (i.e. local convergence).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Local Convergence Rates", "weight": 1.0} -->

For a continuously differentiable nonlinear operator $F$ with the fixed point $\mathbf{z}^*$, if the spectral radius $\rho_F \triangleq \rho(\nabla F(\mathbf{z}^*)) < 1$, then for any $\mathbf{z}_0$ in a neighborhood of $\mathbf{z}^*$, the iterates of $\mathbf{z}_t$ converge to $\mathbf{z}^*$ with a linear rate of $\mathcal{O}((\rho_F + \epsilon)^t)$ for any $\epsilon >0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Local Convergence Rates", "weight": 1.0} -->

With this theorem, one can obtain local convergence rate of an algorithm by just computing the spectral radius of $\nabla F_\eta(\mathbf{z}^*)$, which is a constant matrix depending on $\eta$ in our setting. In the paper, we focus on the worst-case convergence rate which is defined (up to a $\epsilon$ difference) as follows: $$\min_\eta \max_{F \in \mathcal{M}} \rho(\nabla F_\eta(\mathbf{z}^*)), where the inner maximization is over all possible instances within the whole problem class $\mathcal{M}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Revisiting Alt-GDA for Bilinear Games", "weight": 1.0} -->

In this section, we revisit the unconstrained bilinear games[gidel2019negative, daskalakis2018last, liang2019interaction, mokhtari2020unified] for which Sim-GDA diverges with any finite step size. Formally, the bilinear game is given by $$\min_{\mathbf{x} \in \mathbb{R}^m} \max_{\mathbf{y} \in \mathbb{R}^n} \mathbf{x}^\top \mathbf{B} \mathbf{y}, where we ignore the linear terms without loss of generality. Here, the Nash equilibrium is $(\mathbf{x}^*, \mathbf{y}^*)$ satisfying $\mathbf{B}^\top \mathbf{x}^* = \mathbf{0}$ and $\mathbf{B}\mathbf{y}^* = \mathbf{0}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Revisiting Alt-GDA for Bilinear Games", "weight": 1.0} -->

We aim to understand the difference between the dynamics of simultaneous and alternating methods. Practitioners have been widely using the latter instead of the former when optimizing GANs despite the rich optimization literature on simultaneous methods.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Revisiting Alt-GDA for Bilinear Games", "weight": 1.0} -->

For Sim-GDA, the eigenvalues of $\mathbf{I} - \nabla F_\eta^\textup{Sim}$ are all pure imaginary. As a result, we have the spectral radius as $\rho(\nabla F_\eta^\textup{Sim}) = 1 + \eta^2\sigma_\text{max}^2(\mathbf{B})$. Therefore, we have For any $\eta > 0$, the iterates of Sim-GDA diverges as $$\Delta_t \in \Omega\left(\Delta_0 (1 + \eta^2 \sigma_\text{max}^2(\mathbf{B}))^t \right)$$ This theorem states that the iterates of Sim-GDA diverge linearly for any positive constant step-size $\eta$. By contrast, the iterates of Alt-GDA stay bounded due to the sequential update rule which significantly shifts the eigenvalues of the Jacobian.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Revisiting Alt-GDA for Bilinear Games", "weight": 1.0} -->

Specifically, the eigenvalues of $\nabla F_\eta^\textup{Alt}$ are roots of the polynomial $ (x - 1)^2 + \eta^2 \lambda x$ with $\lambda \in \text{Sp}(\mathbf{B}^\top \mathbf{B})$. As a consequence, the spectral radius of $\nabla F_\eta^\textup{Alt}$ is upper bounded by $1$ for some $\eta$ and hence the iterates of Alt-GDA stays bounded.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Revisiting Alt-GDA for Bilinear Games", "weight": 1.0} -->

For any $0 < \eta \leq \frac{2}{\sigma_\text{max}(\mathbf{B})}$, the iterates of Alt-GDA stay bounded $$\Delta_t \in \mathcal{O}\left(\Delta_0 \right)$$ Similar results can be found in the literature (see e.g., [gidel2019negative, zhang2019convergence]). In addition, one can show that for bilinear games, Alt-GDA is a symplectic integrator applied on the continuous dynamics[bailey2020finite], which preserves energy and volume.

<!-- chunk {"id": "body-0025", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Bilinear games, as discussed previously, are somewhat simplistic in that they obey a conservation law and can be easily solved by performing gradient descent on the Hamiltonian[letcher2019differentiable, azizian2020accelerating]. In this section, we consider a different class of games whose Jacobian has both symmetric and antisymmetric components, and are therefore arguably harder to solve.

<!-- chunk {"id": "body-0026", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

We let $L \triangleq \max\{L_\mathbf{x}, L_\mathbf{y}, L_{\mathbf{x}\mathbf{y}}\}$ and $\mu \triangleq \min\{\mu_\mathbf{x}, \mu_\mathbf{y}\}$ and define the condition number $\kappa \triangleq L/\mu$. Accordingly, one can define $\kappa_\mathbf{x} \triangleq L / \mu_\mathbf{x}$ and $\kappa_\mathbf{y} \triangleq L / \mu_\mathbf{y}$. We now briefly summarize some known results about convergence of Sim-GDA in this setting.

<!-- chunk {"id": "body-0027", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

The worst-case convergence rate [eq:rate] of Sim-GDA reduces to $\rho(\mathbf{I} - \eta\nabla V(\mathbf{z}^*))$, which is equivalent to $$\min_{\eta} \max_{\lambda \in \mathcal{K}} |1 - \eta \lambda |, where $\mathcal{K}$ is the support of the eigenvalues of the Jacobian of the gradient vector field $V$. It can be shown that $\mathcal{K} = \left\{ \lambda \in \mathbb{C}: |\lambda| \leq \sqrt{2}L, \Re \lambda \geq \mu > 0 \right\}$ (see Appendix[app:B]). This set is the intersection between a circle and a halfplane[azizian2020accelerating].

<!-- chunk {"id": "body-0028", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Eqn.[eq:rate-quad] leaves open the choice of $\eta$, and it is known that the presence of large imaginary eigenvalues of the Jacobian forces a small value of $\eta$, thereby limiting the rate of convergence[mescheder2017numerics]. We summarize the result below: With the step size $\eta = \frac{\mu}{2L^2}$, we have $\rho(\nabla F_\eta^\textup{Sim}(\mathbf{z}^*)) < 1 - \frac{1}{ 4\kappa^2}$. Hence, Sim-GDA converges locally at a linear rate $\mathcal{O}\left(\left(1 - \frac{1}{4\kappa^2}\right)^t\right)$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

This theorem suggests that Sim-GDA converges to the equilibrium linearly with an iteration complexity of $\mathcal{O}(\kappa^2)$, which is known to be tight[azizian2020accelerating] but much slower than the $\mathcal{O}(\kappa)$ iteration complexity of extra-gradient (EG) or optimistic gradient-descent-ascent (OGDA)[gidel2018variational, mokhtari2020unified, azizian2020tight, zhang2020unified].

<!-- chunk {"id": "body-0030", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Eigenvalues of $\nabla F_\eta^\textup{Sim}$ and $\nabla F_\eta^\textup{Alt}$ for a minimax problem with the function $f(x, y) = 0.3 x^2 + 1.2 x y - 0.3 y^2$. For a fixed step-size $\eta$, eigenvalues of Sim-GDA are represented with red dots and eigenvalues of Alt-GDA are green dots. Their trajectories as $\eta$ sweeps in $$ are shown from light colors to dark colors. Convergence circles for Sim-GDA are in red, Alt-GDA in green, and unit circle in black. The convergence circles are optimized over all step-sizes. Alternating updates help as its convergence circle (green) is smaller, due to the fact that it allows us to use much larger step-sizes. Figure inspired.

<!-- chunk {"id": "body-0031", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

To understand why, we note the maximization over $\lambda$ in [eq:rate-quad] is attained by $\lambda = \mu + \sqrt{2L^2 - \mu^2}i$, which has a large imaginary component. It is easy to show (see e.g.,[mescheder2017numerics]) that the largest feasible step size in [eq:rate-quad] is inversely proportional to $(|\lambda|/\Re(\lambda))^2$. Hence, the step size has to be extremely small in the presence of eigenvalues with large imaginary parts, which in turn, leads to slow convergence. In a nutshell, the culprits of slow convergence in Sim-GDA are eigenvalues of the Jacobian of the associated vector field $V$ with large imaginary parts. We stress that eigenvalues with large imaginary components contribute to a strong rotational force. To improve convergence, many algorithms have been introduced to suppress the rotational force, including EG, OGDA, and NM. Indeed, all three of these algorithms improve the convergence rate by some margin in theory.

<!-- chunk {"id": "body-0032", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Nevertheless, GDA (or its adaptive variant) is still the go-to algorithm in practice.

<!-- chunk {"id": "body-0033", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

We believe the reason these alternative algorithms haven't been adopted widely is that practical algorithms for cases such as GANs are typically based on Alt-GDA rather than Sim-GDA. Surprisingly, despite the popularity of Alt-GDA, its convergence properties haven't been analyzed in this setting. While it is perhaps intuitive that Alt-GDA should perform better than Sim-GDA due to its use of fresher gradient information, we show that, in fact, Alt-GDA achieves a quadratic speedup over Sim-GDA locally and matches the convergence rate of EG and OGDA.

<!-- chunk {"id": "body-0034", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Local convergence analyses of Sim-GDA, EG and OGDA are based on matrix spectral calculation, and in principle one can apply this to Alt-GDA as well. However, bounding the spectral radius is much harder for Alt-GDA, since the algorithm involves two half steps, and the spectral radius of the matrix product can't be bounded straightforwardly in terms of the spectral radii of the two factors. This is likely why the convergence rate of Alt-GDA remained unknown.

<!-- chunk {"id": "body-0035", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

By treating complex eigenvalues differently and adopting a fined-grained analysis, we arrive at the following bounds for the eigenvalues of $\nabla F^\textup{Alt}_\eta(\mathbf{z}^*)$: With the step size $\eta \leq \frac{1}{2L}$, the eigenvalues of $\nabla F^\textup{Alt}_\eta(\mathbf{z}^*)$ satisfy \text{if real: } & |\lambda| \leq \max\{1 - \eta \mu_\mathbf{x}, 1 - \eta \mu_\mathbf{y} \}, \\\text{if complex: } & |\lambda| \leq \sqrt{(1 - \eta \mu_\mathbf{x}) (1 - \eta \mu_\mathbf{y})}.

<!-- chunk {"id": "body-0036", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

In stark contrast to Sim-GDA, for which the complex eigenvalues of $\nabla F_\eta^\textup{Sim}$ can have magnitude as large as $\sqrt{1 - 2\eta \mu + 2\eta^2 L^2}$, the complex eigenvalues of $\nabla F_\eta^\textup{Alt}$ are much smaller in magnitude and are even smaller than the real eigenvalues as shown in Theorem[thm:alt-gda]. As a result, we are allowed to use a larger step size, which gives an improved convergence rate (see Figure[fig:sim-alt-comp] for details).

<!-- chunk {"id": "body-0037", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Following immediately from Theorem[thm:alt-gda], we have the following Corollary.

<!-- chunk {"id": "body-0038", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

With $\eta = \frac{1}{2L}$, we have $\rho(\nabla F_\eta^\textup{Alt}(\mathbf{z}^*)) \leq 1 - \frac{1}{2 \kappa}$. Hence by Theorem[thm:local], Alt-GDA converges locally at a linear rate $\mathcal{O} \left(\left(1 - \frac{1}{2\kappa} + \epsilon\right)^t\right)$ with $\epsilon > 0$ an arbitrarily small constant.

<!-- chunk {"id": "body-0039", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

In particular, this corollary suggests that the iteration complexity of Alt-GDA matches the coarse lower iteration complexity bound The fine-grained bound is $\Omega(\sqrt{\kappa_\mathbf{x} \kappa_\mathbf{y}})$. One could achieve this bound by using a accelerated proximal point framework with Alt-GDA in the inner-loop. $\Omega(\kappa)$[azizian2020accelerating] up to a constant, implying Alt-GDA is near-optimal (at least locally). This is the firsttime that one can rigorously show the Alt-GDA converges faster than Sim-GDA by more than a constant, let alone quadratically faster.

<!-- chunk {"id": "body-0040", "role": "body", "section": "NEAR-OPTIMAL LOCAL CONVERGENCE IN SCSC SETTING", "weight": 1.0} -->

Furthermore, it implies that the convergence rate of Alt-GDA is no worse than its rate for pure cooperative games with $\mathbf{B} \triangleq \nabla_{\mathbf{x}\mathbf{y}}^2 f = \mathbf{0}$. Put differently, the adversarial component (the existence of coupling matrix $\mathbf{B}$) does not make the optimization any harder for Alt-GDA. We remark that this is not true for Sim-GDA because in that case, the coupling matrix $\mathbf{B}$introduces complex eigenvalues with large imaginary parts, which slow down convergence.

<!-- chunk {"id": "body-0041", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

We have shown that Alt-GDA achieves a near-optimal local convergence rate for SCSC minimax games. In this section, we further consider the case that has only strong concavity in the player $\mathbf{y}$ but no strong convexity in $\mathbf{x}$. In particular, it is equivalent to assuming \mathbf{0} \preceq \nabla_\mathbf{x}^2 f \preceq L_\mathbf{x} \mathbf{I}, \; &\mu_\mathbf{y} \mathbf{I} \preceq -\nabla_\mathbf{y}^2 f \preceq L_\mathbf{y} \mathbf{I}, \\ \|\nabla_{\mathbf{x}\mathbf{y}}^2 f\|_2 &\leq L_{\mathbf{x}\mathbf{y}}.

<!-- chunk {"id": "body-0042", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

This setting was investigated in empirical policy evaluation where no strong convex regularization is applied on the primal variables[du2017stochastic]. They showed that the non-singularity of the coupling matrix $\mathbf{B} \triangleq \nabla_{\mathbf{x}\mathbf{y}}^2 f(\mathbf{x}^*, \mathbf{y}^*)$ can help achieve linear convergence for Sim-GDA. Technically, the coupling matrix $\mathbf{B}$ has to be full-row rank (i.e., $\lambda_\text{min}(\mathbf{B}\mathbf{B}^\top) > 0$) and we simply assume $\mu_{\mathbf{x}\mathbf{y}} \triangleq \sigma_\text{min}(\mathbf{B}) > 0$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

Then for Sim-GDA, we have the eigenvalues of its Jacobian as follows: Let $\eta \leq \frac{1}{L}$, the eigenvalues of $\nabla F^\textup{Sim}_\eta(\mathbf{z}^*)$ satisfy the following bound \text{if real: }& |\lambda| \leq \max\left\{1 - \tfrac{\eta}{L} \mu_{\mathbf{x}\mathbf{y}}^2, 1- \eta \mu_\mathbf{y} \right\}, \\ \text{if complex: }& |\lambda| \leq \sqrt{1 - \eta \mu_\mathbf{y} + 2\eta^2 L^2}.

<!-- chunk {"id": "body-0044", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

To be noted, our eigenvalue bounds in Theorem[prop:sim-gda] are slightly different from that in [du2017stochastic] as they allow step size separation for player $\mathbf{x}$ and $\mathbf{y}$. As a result, we get the following local convergence rate by optimizing over the step-size $\eta$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

This corollary suggests that the convergence rate of Sim-GDA could match the rate in Theorem[thm:sim-gda] if the coupling matrix is well-conditioned (i.e., $\kappa_{\mathbf{x}\mathbf{y}} \approx 1$), albeit the absence of strong convexity in $\mathbf{x}$. Naturally, this begs the question: whether we can derive similar results for Alt-GDA that improves upon the rate bound of Sim-GDA. We answer this question in the affirmative. In particular, we have the following bounds for the eigenvalues of $\nabla F^\textup{Alt}_\eta$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

Compare the eigenvalue bound of Alt-GDA to Sim-GDA, one may notice that the main difference is the complex eigenvalues. Similar to the SCSC setting, the complex eigenvalues of Alt-GDA are much smaller in magnitude, thus allowing us to use larger step sizes. Consequently, we have a better convergence rate for Alt-GDA (see Figure[fig:fig1] for detailed comparisons).

<!-- chunk {"id": "body-0047", "role": "body", "section": "ACCELERATION WITHOUT STRONG CONVEXITY", "weight": 1.0} -->

Compared with the bound of Sim-GDA in Theorem[thm:sim-gda-no], one can see that Alt-GDA converges much faster than Sim-GDA, especially when $\kappa_\mathbf{y}$is large.

<!-- chunk {"id": "body-0048", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

So far, we derived local convergence rates of Alt-GDA in different settings. Nonetheless, the global convergence results remain largely unknown. Unlike local convergence analysis, we have to switch to Lyapunov theory for global convergence analysis. Finding a right Lyapunov function for Alt-GDA turns out to be extremely hard and we resort to integral quadratic constraints (IQC) theory[lessard2016analysis, zhang2020unified] for a computer-aided proof See the blog by Adrien Taylor for more details about computer-aided analyses.. Basically, we view the algorithm as an interconnected dynamical system with nonlinear feedback (i.e., the gradient) and model the nonlinear feedback with quadratic constraints Both convexity and smoothness can be characterized tightly with quadratic constraints.. Then it allows us to automatically search for a quadratic Lyapunov function for certifying the worst-case convergence rate by solving a semi-definite program (SDP). Due to space constraints, we refer the reader to Appendix[app:iqc]for all the details.

<!-- chunk {"id": "body-0049", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

In particular, we analyze Alt-GDA for bilinearly-coupled minimax games with the following form: $$\min_{\mathbf{x} \in \mathbb{R}^m} \max_{\mathbf{y} \in \mathbb{R}^n} f(\mathbf{x}) + \mathbf{x}^\top \mathbf{B} \mathbf{y} - g(\mathbf{y}),$$ where we assume both $f$ and $g$ are $\mu$-strongly-convex and $L$-smooth, $\|\mathbf{B}\|_2 \leq L$. This problem is a special case of the minimax games that is amenable to IQC analysis. This problem has been studied extensively[chambolle2011first, du2019linear, xie2021dippa]. However, the convergence properties of Alt-GDA again remain unknown.

<!-- chunk {"id": "body-0050", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

Using the IQC framework, we are able to search for the best possible convergence rate of Alt-GDA for every given condition number $\kappa$ by solving a SDP. However, the size of the SDP is proportional to $m$ and $n$. This can be problematic in cases where $m$ (or $n$) is large because it can be computationally costly to solve large SDPs. Fortunately, we prove that the high dimensional problem isn't any harder than than the case of $m = n = 1$, so we can reduce the problem to a SDP with $m = n = 1$, which is easy to solve.

<!-- chunk {"id": "body-0051", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

Using the IQC framework to analyze the convergence rate of Alt-GDA on problem [eq:bilinear-sp], we can simply assume $m = n = 1$ if $\mathbf{B}$ is diagonal. Let $\rho_{m, n}$ be the IQC-certified rate for problem [eq:bilinear-sp] with $\mathbf{x} \in \mathbb{R}^m$ and $\mathbf{y} \in \mathbb{R}^n$, then we have $\rho_{m,n} \leq \rho_{1, 1}$. [fig:iqc], we plot the IQC-certified iteration complexity as a function of condition number. We observe that the bound for Alt-GDA does improve upon that of Sim-GDA, especially when the condition number is large. In particular, the complexity of Alt-GDA scales linearly with the condition number, suggesting its iteration complexity is $\mathcal{O}(\kappa)$. This implies that Alt-GDA does accelerate the convergence globally for this class of problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "GLOBAL CONVERGENCE FOR BILINEARLY-COUPLED MINIMAX GAMES", "weight": 1.0} -->

Certified iteration complexities of Sim-GDA and Alt-GDA for blinearly-coupled minimax games. Observations: Sim-GDA converges with an iteration complexity of $\mathcal{O}(\kappa^2)$; Alt-GDA achieves an improved rate of $\mathcal{O}(\kappa)$, which matches the local rate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

In this section, we compare the performance of Alt-GDA with Sim-GDA along with other three popular algorithms (EG, OGDA and NM) so as to verify our theoretical results on the convergence rate of Alt-GDA. In particular, we focus on the following quadratic minimax problem: $$\min_{\mathbf{x} \in\mathbb{R}^d} \max_{\mathbf{y} \in \mathbb{R}^d} f(\mathbf{x}, \mathbf{y}) = \frac{1}{2}\mathbf{x}^\top \mathbf{A} \mathbf{x} + \mathbf{x}^\top \mathbf{B} \mathbf{y} - \frac{1}{2} \mathbf{y}^\top \mathbf{C} \mathbf{y} where we set the dimension $d = 100$. We note both linear regression[du2019linear] and robust least squares[yang2020global] problems admit this minimax formulation.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

The matrices $\mathbf{A}$ and $\mathbf{C}$ are set to have eigenvalues $\{\tfrac{1}{i}\}_{i=1}^{d}$. For matrix $\mathbf{B}$, we set it to be a random matrix with entries sampling from a Gaussian distribution (either $\mathcal{N}(0, 0.01)$ or $\mathcal{N}$). In the case of $\mathbf{B}$ sampled from $\mathcal{N}$, the resulting gradient vector field has a strong rotational force since the off-diagonal blocks of its Jacobian dominates (see [eq:jacobian] in the Appendix). For all algorithms, the iterates start with $\mathbf{x}_0 = \mathbf{1}$ and $\mathbf{y}_0 = \mathbf{1}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

Figure[fig:simulation] shows that the distance to the optimum of Sim-GDA, Alt-GDA, OGDA, EG and NM We implemented the simultaneous version of negative momentum (NM). For alternating NM, the optimal damping value of NM is roughly zero, making it the same algorithm as Alt-GDA. versus the number of iterations for this problem. For all methods, we tune their hyperparameters by grid-search. We notice that all methods converge linearly to the optimum. As expected, Alt-GDA performs significantly better than Sim-GDA and yields a convergence rate that is better than its worst-case rate (black dashed line). Moreover, we find that Alt-GDA outperforms OGDA and EG by a visible margin. This is surprising, in that OGDA and EG take another memory buffer for accelerating the convergence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

Furthermore, we study how the convergence rates (or iteration complexities) scale with the condition numbers. To this end, we randomly sample We let the eigenvalues of matrices $\mathbf{A}$ and $\mathbf{C}$ be $\{ \tfrac{1}{n_i}\}_{i=1}^d$ where $n_i$ are evenly spaced from $1$ to $N$, where $N$ is in $[\sqrt{10}, 10^3]$. We sample all entries of $\mathbf{B}$ from standard normal distribution $\mathcal{N}$ and then normalize it.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

matrices $\mathbf{A}, \mathbf{B}, \mathbf{C}$ and compute the condition number by $\kappa = \frac{\max\{|\lambda_i|\}}{\min\{\Re(\lambda_i)\}}$ where $\lambda_i$ are eigenvalues of the Jacobian $\mathbf{J}$ of the gradient vector field in [eq:jacobian]. Once we have all these three matrices, we can compute the spectral radius $\rho$ of all algorithms with tuned step-sizes and momentum value. We plot $-1/\log(\rho)$ versus the condition number $\kappa$ in Figure[fig:simulation] (right) to get a sense of how the relative iteration complexity scales as a function of condition number. We find that the iteration complexity of Alt-GDA scales linearly with the condition number, matching our prediction in Corollary[cor:alt-gda].

<!-- chunk {"id": "body-0058", "role": "body", "section": "Quadratic Minimax Games", "weight": 1.0} -->

On the other hand, Sim-GDA takes roughly $\kappa^2$ iterations to convergence, as predicted in Theorem[thm:sim-gda]. In addition, Alt-GDA is slightly better than OGDA and EG as its curve is below that of OGDA and EG, albeit with the same slope.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

In this section, we investigate the effect of alternating updates on training generative adversarial networks. The purpose of this section is to show that the insights gained from our analyses carry over to GAN training despite the fact that the GAN objective is generally nonconvex-nonconcave. In addition, we note that while GAN training is a stochastic problem, stochastic problems are sometimes in a curvature-dominated regime where the convergence behavior resembles that of the deterministic problems[zhang2019algorithmic].

<!-- chunk {"id": "body-0060", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

We first compare alternating algorithms with their simultaneous counterparts on [krizhevsky2009learning] image generation task with the WGAN-GP[gulrajani2017improved] objective and a DCGAN[radford2015unsupervised] architecture. In particular, we choose SGD and AMSGrad[reddi2019convergence] as our base optimizers. For more implementation details, please see Appendix[app:imp]. We evaluate all algorithms with Fréchet Inception Distance Inception score is also a popular metric, however it was shown by that it is less consistent with the sample quality, so we instead use FID score here.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

(FID)[heusel2017gans]. Figure[subfig:sgd] and[subfig:amsgrad] summarize our results. With SGD as our optimizer We also include the results with exponential moving average (EMA)., we observe that alternating SGD not only converges faster, but also converges to a better point with lower FID score. Although both alternating version and simultaneous version of AMSGrad converges to models with similar FID scores, the alternating version again converges with many fewer iterations, matching our prediction. In addition, we generate samples from trained Generators at iteration 30000 with SGD optimizer (see Figure[subfig:sim-gda] and[subfig:alt-gda]). It is easy to see that the model trained with alternating updates generates better samples given the same compute budget.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

(a) ResNet model trained with SGD on CIFAR-10. (b) ResNet model trained with AMSGrad on CIFAR-10. Alternating algorithms dominate simultaneous ones. More interestingly, the use of optimism does not help for alternating algorithms.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Generative Adversarial Networks", "weight": 1.0} -->

Furthermore, we compare simultaneous methods and alternating methods on a deep ResNet[miyato2018spectral]. We also include optimistic updates[daskalakis2018training] in the training, which is the key component of OGDA See Appendixapp:imp for detailed update rule.. We report all results in Figure[fig:resnet-gan]. The first observation is that alternating algorithms take fewer iterations to converge regardless of whether optimism is used, and sometimes converge to models with better FID scores (similar to DCGAN results). Second, we observe that the use of optimism only helps for simultaneous algorithms, suggesting that alternating updates and optimistic updates play similar roles in improving GAN training. This could be explained by our theoretical results that Alt-GDA enjoys a similar convergence rate to OGDA.

<!-- chunk {"id": "body-0064", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this paper, we take an important step towards understanding alternating algorithms in minimax optimization by analyzing Alt-GDA in three distinct settings. In particular, we show theoretically that Alt-GDA outperforms its simultaneous counterpart by a big margin in all three settings. Unexpectedly, Alt-GDA achieves a near-optimal convergence rate locally for strongly convex-strongly concave smooth minimax games, matching the known coarse lower bound. Moreover, the acceleration effect of Alt-GDA remains when the minimax problem has only strong concavity in the dual variables.

<!-- chunk {"id": "body-0065", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Our numerical simulations on toy quadratic games verified our claims. Further, we demonstrate empirically that alternating updates could significantly speed up GAN training though GAN objective is generally nonconvex-nonconcave. More interestingly, we show that the use of optimism only helps for simultaneous algorithms. We believe that the default use of alternating update rule in GAN training was an important reason for its success.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

Borrowing the notations from[lessard2016analysis], we frame various first-order algorithms as a unified linear dynamical system This linear dynamical system can represent any first-order methods. in feedback with a nonlinearity $\phi: \mathbb{R}^d \rightarrow \mathbb{R}^d$, At each iteration $t = 0, 1,...$, $u_t \in \mathbb{R}^d$ is the control input, $y_t \in \mathbb{R}^d$ is the output, and $\xi_t \in \mathbb{R}^{nd}$ is the state for algorithms with $n$ step of memory. The state matrices $A, B, C, D$ differ for various algorithms.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

For most algorithms we consider in the paper, they have the general form: (1 + \beta) \mathbf{I}_d & -\beta \mathbf{I}_d & -\eta \mathbf{I}_d \\\mathbf{I}_d & \mathbf{0}_d & \mathbf{0}_d \\ \hline (1 + \alpha)\mathbf{I}_d & -\alpha \mathbf{I}_d & \mathbf{0}_d where $\mathbf{I}_d$ and $\mathbf{0}_d$ are the identity and zero matrix of size $d \times d$, respectively. Often, the nonlinear function $\phi$ is the troublesome function we wish to analyze. Although we do not know $\phi$ exactly, we assume to have some knowledge of the constraints it imposes on the input-output pair $(y, u)$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

For example, we may assume $\phi$ to be $L$-Lipschitz, which implies $\|u_t - u^*\|_2 \leq L \|y_t - y^* \|_2 $ for all $t$ with $u^* = \phi(y^*)$ as a fixed point. In matrix form, this is \end{bmatrix}^\top \end{bmatrix} \geq 0.$$ We can also characterize strong convexity of $f$ and $g$ by similar quadratic constraints. Notably, the above constraint is very special in that it only manifests itself as separate quadratic constraints on each $(y_t, u_t)$. It is possible to specify quadratic constraints that couple different $t$ values.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

To achieve that, we follow [lessard2016analysis] and adopt auxiliary sequences $\zeta, s$ together with a map $\Psi$ characterized by matrices $(A_\Psi, B_\Psi^y, B_\Psi^u, C_\Psi, D_\Psi^y, D_\Psi^u)$: \zeta_{t+1} &= A_\Psi \zeta_t + B_\Psi^y y_t + B_\Psi^u u_t, \\s_{t} &= C_\Psi \zeta_t + D_\Psi^y y_t + D_\Psi^u u_t.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

The equations[eq:ass-ref] define an affine map $s = \Psi(y, u)$, where $s_t$ could be a function of all past $y_i$ and $u_i$ with $i \leq t$. We consider the quadratic form $(s_t - s^*)^\top M (s_t-s^*)$ for a given matrix $M$ with $s^*$ and $\xi^*$ fixed points of [eq:ass-ref]. We note that the quadratic form is a function of $(y_0,\dots, y_t, u_0,\dots, u_t)$ that is determined by our choice of $(\Psi, M)$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

More succinctly, [eq:dynamics-comb] can be written as \qquad \text{where } x_t \triangleq \begin{bmatrix} \xi_t \\ \zeta_t \end{bmatrix}.$$ With these definitions in hand, we now state the main result of verifying exponential convergence. Basically, we build a Linear Matrix Inequality (LMI) to guide the search for the parameters of a quadratic Lyapunov function in order to establish a rate bound.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

Consider the dynamical system[eq:dynamical-system].

<!-- chunk {"id": "body-0073", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

Suppose the vector field $F$ satisfies the IQC $(\Psi, M)$ and define $(\hat A, \hat B, \hat C, \hat D)$ according to[eq:psi][eq:dynamics-compact], we have the following linear matrix inequality (LMI): \hat{A}^\top P \hat{A} - \rho^2 P & \hat{A}^\top P \hat{B}\\\hat{B}^\top P \hat{A} & \hat{B}^\top P \hat{B} \lambda \begin{bmatrix} \hat{C} & \hat{D} \end{bmatrix}^\top M \begin{bmatrix} \hat{C} & \hat{D} \end{bmatrix} \preceq 0.$$ If this LMI is feasible for some $P \succ 0$, $\lambda \geq 0$ and $\rho > 0$, we have $$(x_{t+1} -

<!-- chunk {"id": "body-0074", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

x^*)^\top (P \otimes \mathbf{I}_d) (x_{t+1} - x^*) \leq \rho^2 (x_t - x^*)^\top (P \otimes \mathbf{I}_d) (x_t - x^*).$$ Consequently, for any $\xi_0$ and $\zeta_0 = \zeta^*$, we obtain The LMI[eq:sdp] can be extended to the case of multiple constraints with $(\Psi_i, M_i)$ (see[lessard2016analysis] for details).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Details about IQC framework", "weight": 1.0} -->

To apply Theorem[thm:main-thm], we seek to solve the semidefinite program (SDP) of finding the minimal $\rho$ such that the LMI[eq:sdp]is feasible. For simple algorithms, one can typically solve the SDP analytically. Nevertheless, one may only get a numerical proof when the algorithm of interest is complicated and the resulting SDP is hard to solve.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Analyzing Alt-GDA with IQC framework", "weight": 1.0} -->

Given that $\mathbf{B}$ is diagonal, one can show that both $\bmat{\hat{A}, \hat{B}}$ and $\bmat{\hat{C}, \hat{D}}$ have very special structure. In particular, we can permute them column-wise and row-wise to get block-diagonal matrices: $$\bmat{\hat{A}, \hat{B}} = \mathbf{U} \underbrace{\bmat{\bsmat{1 & -\eta \mathbf{B}_{11} & 0 & 0 & -\eta & 0 \\\vdots & \ddots & \vdots \\\mathbf{0} & \cdots & \bsmat{1 & 0 & -\eta \\ -L & 0 & 1}}}_{\triangleq \mathbf{Q}_1} \mathbf{V}$$ where both $\mathbf{U}$ and $\mathbf{V}$ are permutation matrices.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Analyzing Alt-GDA with IQC framework", "weight": 1.0} -->

If we further restrict $\mathbf{U}^\top P \mathbf{U}$ to have the same block-diagonal structure as $\mathbf{Q}_1$ and $\mathbf{Q}_2$, then it suffices to pick a $\rho$ so that each diagonal block of the LMI [eq:lmi-2] holds.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Analyzing Alt-GDA with IQC framework", "weight": 1.0} -->

Moreover, the LMI of each diagonal block is the LMI of the case $m = n = 1$, except for the last $n - m$ blocks, for which we have $$\bsmat{1 & 0 & -\eta \\ -L & 0 & 1}^\top P \bsmat{1 & 0 & -\eta \\ -L & 0 & 1} + \bsmat{L & \rho^2 & -1 \\ -\mu & 0 & 1}^\top \bsmat{0 & \lambda_2 \\ \lambda_2 & 0} \bsmat{L & \rho^2 & -1 \\ -\mu & 0 & 1} \preceq \rho^2 \bmat{\mathbf{I}, \mathbf{0} }^\top P \bmat{\mathbf{I}, \mathbf{0}}.$$ This is the LMI for minimizing a $\mu$-strongly convex $L$-smooth function (see[lessard2016analysis]), which has a better convergence rate compared to our minimax problem

<!-- chunk {"id": "body-0079", "role": "body", "section": "Analyzing Alt-GDA with IQC framework", "weight": 1.0} -->

(i.e., any feasible $\rho$ of the LMI for 1-dimension minimax problem is also feasible for [eq:lmi-min]) because it is a special case of [eq:bilinear-sp] with $\mathbf{B} = 0$ in the 1-dimensional case.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Analyzing Alt-GDA with IQC framework", "weight": 1.0} -->

So far, we show that as long as the LMI for the case of $m = n = 1$ holds, then the general case also holds since the general case can be decomposed into many 1-dimensional problems. This completes the proof.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Additional Results on SVHN", "weight": 1.0} -->

(a) ResNet model trained with SGD on SVHN. (b) ResNet model trained with AMSGrad on SVHN. Alternating algorithms dominate simultaneous ones. Again, the use of optimism makes little difference for alternating algorithms.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

For our experiments, we used the PyTorch deep learning framework. For experiments, we compute the FID score using the provided implementation in Tensorflow for consistency with related works.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

Optimistic update rule: the simultaneous version of optimistic gradient descent-ascent takes the following form: \mathbf{x}_{t+1} &= \mathbf{x}_t - 2\eta \nabla_\mathbf{x} f(\mathbf{x}_t, \mathbf{y}_t) + \eta \nabla_\mathbf{x} f(\mathbf{x}_{t-1}, \mathbf{y}_{t-1}) \\\mathbf{y}_{t+1} &= \mathbf{y}_t + 2\eta \nabla_\mathbf{y} f(\mathbf{x}_t, \mathbf{y}_t) - \eta \nabla_\mathbf{y} f(\mathbf{x}_{t-1}, \mathbf{y}_{t-1}) By comparison, the alternating version iterates as follows: \mathbf{x}_{t+1} &= \mathbf{x}_t - 2\eta

<!-- chunk {"id": "body-0084", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

For ResNet experiments, we used the hinge version of the adversarial non-saturating loss, see[miyato2018spectral]. As a reference, our ResNet architectures for CIFAR-10 and SVHN[netzer2011reading] have approximately $85$ layers in total for the generator and discriminator, including the nonlinearity and the normalization layers. This ResNet architecture was also used in[chavdarova2020taming], see Appendix E 2.2 of[chavdarova2020taming].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

Hyperparameters: We conduct grid search over the step size (and $\beta_2$ for AMSGrad) for each setting. For SGD, the search range of step-size is $\{5\mathrm{e}{-4}, 1\mathrm{e}{-3}, 2\mathrm{e}{-3}, 5\mathrm{e}{-3}, 1\mathrm{e}{-2}, 2\mathrm{e}{-2}\}$. For AMSGrad, the search range of step-size is $\{5\mathrm{e}{-5}, 1\mathrm{e}{-4}, 2\mathrm{e}{-4}, 5\mathrm{e}{-4}, 1\mathrm{e}{-3}, 2\mathrm{e}{-3}\}$ while the search range of $\beta_2$ is $\{0.9, 0.99, 0.999\}$. We report the optimal hyperparameters used in the following tables.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

All these hyperparameters are tuned with random seed $1$. We have also tried other seeds (including seed $2$ and $3$) and the optimal hyperparameters could be different with different random seeds. However, the optimal curves across different random seeds look similar.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

| Parameter | Sim-SGD | Alt-SGD | Sim-AMSGrad | Alt-AMSGrad | Hyperparameters for ResNet experiments on CIFAR-10.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Implementation Details for Generative Adversarial Networks", "weight": 1.0} -->

| 2*Parameter | 4cSimultaneous | 4cAlternating | | | | | | | Hyperparameters for ResNet experiments on SVHN.
