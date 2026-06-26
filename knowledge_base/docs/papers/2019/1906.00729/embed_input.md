<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization Provably Converges to Nash Equilibria in Zero-Sum Linear Quadratic Games

Topics include Nonconvex optimization, Reinforcement learning, Optimization, Control, Learning, Neuroevolution, Zero-sum linear quadratic, Linear quadratic, Saddle point.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the global convergence of policy optimization for finding the Nash equilibria (NE) in zero-sum linear quadratic (LQ) games. To this end, we first investigate the landscape of LQ games, viewing it as a nonconvex-nonconcave saddle-point problem in the policy space. Specifically, we show that despite its nonconvexity and nonconcavity, zero-sum LQ games have the property that the stationary point of the objective function with respect to the linear feedback control policies constitutes the NE of the game. Building upon this, we develop three projected nested-gradient methods that are guaranteed to converge to the NE of the game. Moreover, we show that all of these algorithms enjoy both globally sublinear and locally linear convergence rates. Simulation results are also provided to illustrate the satisfactory convergence properties of the algorithms. To the best of our knowledge, this work appears to be the first one to investigate the optimization landscape of LQ games, and provably show the convergence of policy optimization methods to the Nash equilibria. Our work serves as an initial step toward understanding the theoretical aspects of policy-based reinforcement learning algorithms for zero-sum Markov games in general.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) has achieved sensational progress recently in several prominent decision-making problems, e.g., playing the game of Go and playing real-time strategy games. Interestingly, all of these problems can be formulated as zero-sum Markov games involving two opposing players or teams. Moreover, their algorithmic frameworks are all based upon *policy optimization* (PO) methods such as actor-critic and proximal policy optimization (PPO), where the policies are parametrized and iteratively updated. Such popularity of PO methods are mainly attributed to the facts that: (i) they are easy to implement and can handle high-dimensional and continuous action spaces; (ii) they can readily incorporate advanced optimization results to facilitate the algorithm design. Moreover, empirically, some observations have shown that PO methods usually converge faster than value-based ones.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to the tremendous empirical success, theoretical understanding of policy optimization methods for the multi-agent RL settings, especially the zero-sum Markov game setting, lags behind. Although the convergence of policy optimization algorithms to *locally optimal* policies has been established in the classical RL setting with a *single-agent/player*, extending those theoretical guarantees to *Nash equilibrium* (NE) policies, a common solution concept in game theory also known as the saddle-point equilibrium (SPE) in the zero-sum setting, suffers from the following two caveats.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, since the players simultaneously determine their actions in the games, the decision-making problem faced by each player becomes non-stationary. As a result, single-agent algorithms fail to work due to lack of Markov property. Second, with parametrized policies, the policy optimization for finding NE in a function space is reduced to solving for NE in the policy parameter space, where the underlying game is in general nonconvex-nonconcave. Since nonconvex optimization problems are NP-hard in the worst case, so is finding NE in nonconvex-nonconcave saddle-point problems. In fact, it has been showcased recently that vanilla gradient-based algorithms might have cyclic behaviors and fail to converge to any NE in both zero-sum and general-sum games.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an initial attempt in merging the gap between theory and practice, we study the performance of PO methods on a simple but quintessential example of zero-sum Markov games, namely, zero-sum linear quadratic (LQ) games. In LQ games, the system evolves following linear dynamics controlled by both players, while the cost function is quadratically dependent on the states and joint control actions. Zero-sum LQ games find broad applications in $\mathcal{H}_{\infty}$-control for robust control synthesis, and risk-sensitive control. In fact, such an LQ setting can be used for studying general continuous control problems with adversarial disturbances/opponents, by linearizing the system of interest around the operational point. Therefore, developing theory for the LQ setting may provide some insights into the *local* property of the general control settings. Our study is pertinent to the recent efforts on policy optimization for linear quadratic regulator (LQR) problems, a single-player counterpart of LQ games.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As to be shown later, LQ games are more challenging to solve using PO methods, since they are not only nonconvex in the policy space for one player (as LQR), but also nonconcave for the other. Compared to PO for LQR, such nonconvexity-nonconcavity has caused technical difficulties in showing the stabilizing properties along the iterations, an essential requirement for the iterative PO algorithms to be feasible. Additionally, in contrast to the recent non-asymptotic analyses on gradient methods for nonconvex-nonconcave saddle-point problems, the objective function lacks smoothness in LQ games, as the main challenge identified in for LQR.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these technical challenges, we first investigate the optimization landscape of LQ games, showing that the stationary point of the objective function constitutes the NE of the game, despite its nonconvexity and nonconcavity. We then propose three projected *nested-gradient* methods, which separate the updates into two loops with both gradient-based iterations. Such a nested-loop update mitigates the inherent non-stationarity of learning in games. The projection ensures the stabilizing property of the control along the iterations. The algorithms are guaranteed to converge to the NE, with provably globally sublinear and locally linear rates.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work. There is a huge body of literature on applying *value-based* methods to solve zero-sum Markov games; see, e.g, and the references therein. Specially, for the linear quadratic setting, Al-Tamimi et al. proposed a Q-learning approximate dynamic programming approach. In contrast, the study of PO methods for zero-sum Markov games is limited, which are either empirical without any theoretical guarantees, or developed only for the tabular setting. Within the LQ setting, our work is related to the recent work on the global convergence of policy gradient (PG) methods for LQR. However, our setting is more challenging since it concerns a saddle-point problem with not only nonconvexity on the minimizer, but also nonconcavity on the maximizer.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work also falls into the realm of solving *nonconvex-(non)concave saddle-point* problems, which has recently drawn great attention due to the popularity of training generative adversarial networks (GANs). However, most of the existing results are either for the nonconvex but concave minimax setting, or only have *asymptotic* convergence results. Two recent pieces of results on non-asymptotic analyses for solving this problem have been established under strong assumptions that the objective function is either weakly-convex and weakly-concave, or smooth. However, LQ games satisfy neither of these assumptions. In addition, even asymptotically, basic gradient-based approaches may not converge to (local) Nash equilibria, not even to stationary points, due to the oscillatory behaviors. In contrast to Mazumdar et al.; Jin et al., our results show the *global convergence* to *actual NE* (instead of any surrogate as *local minimax* in Jin et al. ) of the game.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution. Our contribution is two-fold: i) we investigate the optimization landscape of zero-sum LQ games in the parametrized feedback control policy space, showing its desired property that stationary points constitute the Nash equilibria; ii) we develop projected nested-gradient methods that are proved to converge to the NE with globally sublinear and locally linear rates. We also provide several interesting simulation findings on solving this problem with PO methods. To the best of our knowledge, for the first time, policy-based methods are shown to converge to the *global Nash equilibria* in a class of zero-sum Markov games, and also with convergence rate guarantees.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The condition i) in Assumption 2.1 is a standard sufficient condition that ensures the existence of the value of the game. In addition, condition ii) leads to the saddle-point property of the control pair $(K^{\ast},L^{\ast})$, i.e., the controller sequence $({\{ u_{t}^{\ast}\}}_{t \geq 0},{\{ v_{t}^{\ast}\}}_{t \geq 0})$ generated by (2.4) constitutes the NE of the game (2.1), which is also unique. We formally state the arguments regarding (2.2)-(2.6) in the following lemma, whose proof is deferred to §B.1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy Gradient and Landscape", "weight": 1.0} -->

As has been recognized in Fazel et al. that the LQR problem is nonconvex with respect to (w.r.t.) the control gain $K$, we note that in general, for some given $L$ (or $K$), the minimization (or maximization) problem is not convex (or concave). This has in fact caused the main challenge for the design of equilibrium-seeking algorithms for zero-sum LQ games. We formally state this in the following lemma, which is proved in §B.2.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

In this section, we propose three PO methods, based on policy gradients, to find the global NE of the LQ game. In particular, we develop *nested-gradient* (NG) methods, which first solve the inner optimization by policy-gradient methods, and then use the stationary-point solution to perform gradient-update for the outer optimization. One way to solve for the NE is to directly address the minimax problem (2.1). Success of this procedure, as pointed out in Fazel et al. for LQR, requires the stability guarantee of the system along the outer policy-gradient updates. However, unlike LQR, it is not clear so far if there exists a stepsize and/or condition on $K$ that ensures such stability of the system along the outer-loop policy-gradient update. Instead, if we solve the maximin problem, which has the same value as (2.1) (see Lemma 2.2), then a simple projection step on the iterate $L$, as to be shown later, can guarantee the stability of the updates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

For some given $L$, the inner minimization problem becomes an LQR problem with equivalent cost matrix ${\overset{\sim}{Q}}_{L} = {Q - {L^{\top}R^{v}L}}$, and state transition matrix ${\overset{\sim}{A}}_{L} = {A - {CL}}$. Motivated by Fazel et al., we propose to find the stationary point of the inner problem, since the stationary point suffices to be the global optimum under certain conditions (see Corollary $4$ in Fazel et al.). Let the stationary-point solution be $K{(L)}$. By setting ${{\nabla_{K}\mathcal{C}}{(K,L)}} = 0$ and by Lemma 3.2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

‣ 3 Policy Gradient and Landscape ‣ Policy Optimization Provably Converges to Nash Equilibria in Zero-Sum Linear Quadratic Games"), we have We then substitute (4.1) into (3.1) to obtain the Riccati equation for the inner problem: Note that as in Fazel et al., $K{(L)}$ can be obtained using gradient-based algorithms. For example, one can use the basic policy gradient update in the inner-loop, i.e., where $\alpha > 0$ denotes the stepsize, $P_{K,L}$ denotes the solution to (3.1) for given $(K,L)$, and ${\nabla_{K}\mathcal{C}}{(K,L)}$ denotes the partial gradient w.r.t. $K$ given in (3.4. ‣ 3 Policy Gradient and Landscape ‣ Policy Optimization Provably Converges to Nash Equilibria in Zero-Sum Linear Quadratic Games")).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Alternatively, one can also use the approximate second-order information to accelerate the update, which yields the *natural* policy gradient update that utilizes the Fisher's information, and the *Gauss-Newton* update Suppose $K{(L)}$ in (4.1) can be obtained, regardless of the algorithms used. Then, we substitute $K{(L)}$ back to the gradient of ${\overset{\sim}{\mathcal{C}}{(L)}}:={\mathcal{C}{({K{(L)}},L)}}$ to obtain the *nested-gradient*: where ${\nabla_{L}\overset{\sim}{\mathcal{C}}}{(L)}$ denotes the nested-gradient for the outer-loop.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Thus, the convergent point $({K{(L)}},L)$ that makes ${{\nabla_{L}\overset{\sim}{\mathcal{C}}}{(L)}} = 0$ satisfy both conditions ${{\nabla_{K}\mathcal{C}}{({K{(L)}},L)}} = 0$ and ${{\nabla_{L}\mathcal{C}}{({K{(L)}},L)}} = 0$, which implies from Lemma 3.3. ‣ 3 Policy Gradient and Landscape ‣ Policy Optimization Provably Converges to Nash Equilibria in Zero-Sum Linear Quadratic Games") that the convergent control pair $({K{(L)}},L)$ constitutes the Nash equilibrium.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Thus, we propose the following projected nested-gradient update in the outer-loop to find the pair $({K{(L)}},L)$: where is some convex set in $R^{m_{2} \times d}$, and $P^{GD}{\lbrack \cdot \rbrack}$ is the projection operator onto that is defined as i.e., the minimizer of the distance between $\overset{\sim}{L}$ and $L$ in Frobenius norm. It is assumed that the set is large enough such that it contains the Nash equilibrium $(K^{\ast},L^{\ast})$. Under Assumption 2.1, there exists a constant $\zeta$ with $0 < \zeta < {\sigma_{\min}{({\overset{\sim}{Q}}_{L^{\ast}})}}$, with one example of that serves the purpose is which contains $L^{\ast}$ at the NE. Thus, the projection does not exclude the convergence to the NE.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

The following lemma, proved in §B.5, shows that is indeed convex and compact.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Convergence Results", "weight": 1.0} -->

We start by showing the convergence results for the inner optimization problem as follows, which establishes the *globally linear* convergence rates of the inner-loop policy gradient updates in (4.3)-.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Proofs of Main Results", "weight": 1.0} -->

In this section, we provide proofs for the main results on the convergence of the nested-gradient algorithms stated in §5.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Proofs of Main Results", "weight": 1.0} -->

For notational convenience, we (re-)define the following functions where we recall the definitions of $P_{K,L}$ and $W_{L}$ in (3.1) and (4.11), respectively. To simplify the notation, we denote $\zeta_{{K{(L)}},L}$ by $\zeta_{L}^{\ast}$, for any notation $\zeta_{K,L}$, for example, $V_{K,L}$, $Q_{K,L}$, $A_{K,L}$, $P_{K,L}$, etc.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Auxiliary Lemmas", "weight": 1.0} -->

To proceed with the analysis, we first establish several lemmas that are useful in the ensuing analysis. The first lemma links the value function $V_{K,L}$ and the advantage function $A_{K,L}$, when varying $K$ and $L$, which plays a similar role as Lemma $7$ in Fazel et al..

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In this section, we provide some numerical results to show the superior convergence property of several PO methods. We consider two settings referred to as Case $1$ and Case $2$, which are created based on the simulations in Al-Tamimi et al., with and $R^{u} = R^{v} = I$, ${{}_{0}^{} =}0.03 \cdot I.$ We choose $Q = I$ and $C = \lbrack 0.00951892,0.0038373,0.001\rbrack^{\top}$ for Case $1$; while $Q = {0.01 \cdot I}$ and $C = \lbrack 0.00951892,0.0038373,0.2\rbrack^{\top}$ for Case $2$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In both settings, we evaluate the convergence performance of not only our nested-gradient methods, but also two types of their variants, alternating-gradient (AG) and gradient-descent-ascent (GDA) methods. AG methods are based on the nested-gradient methods, but at each outer-loop iteration, the inner-loop gradient-based updates only perform a finite number of iterations, instead of converging to the exact solution $K{(L_{t})}$ as nested-gradient methods, which follows the idea. The GDA methods perform policy gradient descent for the minimizer and ascent for the maximizer simultaneously. Detailed updates of these two types of methods are deferred to §C.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

(b) Grad. Mapp. Norm Square (c) $\lambda_{\min}{({\overset{\sim}{Q}}_{L})}$ Figure 1: Performance of the three projected NG methods for Case 1 where Assumption 2.1 ii) is satisfied. (a) shows the monotone convergence of the expected cost 𝒞 (K (L), L) to the NE cost 𝒞 (K*, L*); (b) shows the convergence of the gradient mapping norm square; (c) shows the change of the smallest eigenvalue of ${\overset{\sim}{Q}}_{L} = {Q - {L^{\top}R^{v}L}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This paper has developed policy optimization methods, specifically, projected nested-gradient methods, to solve for the Nash equilibria of zero-sum LQ games. In spite of the nonconvexity-nonconcavity of the problem, the gradient-based algorithms have been shown to converge to the NE with globally sublinear and locally linear rates. This work appears to be the first one showing that policy optimization methods can converge to the NE of a class of zero-sum Markov games, with finite-iteration analyses. Interesting simulation results have demonstrated the superior convergence property of our algorithms, even without the projection operator, and that of the gradient-descent-ascent algorithms with simultaneous updates of both players, even when Assumption 2.1 ii) is relaxed. Based on both the theory and simulation, future directions include convergence analysis for the setting under a relaxed version of Assumption 2.1, and that for the projection-free versions of the algorithms, which we believe can be done by the techniques in our recent work Zhang et al.. Besides, developing policy optimization methods for general-sum LQ games is another interesting yet challenging future direction.
