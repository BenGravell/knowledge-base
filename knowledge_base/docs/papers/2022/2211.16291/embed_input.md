<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Controller Reduction in Linear Quadratic Gaussian Control with Performance Bounds

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The problem of controller reduction has a rich history in control theory. Yet, many questions remain open. In particular, there exist very few results on the order reduction of general non-observer based controllers and the subsequent quantification of the closed-loop performance. Recent developments in model-free policy optimization for Linear Quadratic Gaussian (LQG) control have highlighted the importance of this question. In this paper, we first propose a new set of sufficient conditions ensuring that a perturbed controller remains internally stabilizing. Based on this result, we illustrate how to perform order reduction of general non-observer based controllers using balanced truncation and modal truncation. We also provide explicit bounds on the LQG performance of the reduced-order controller. Furthermore, for single-input-single-output (SISO) systems, we introduce a new controller reduction technique by truncating unstable modes. We illustrate our theoretical results with numerical simulations. Our results will serve as valuable tools to design direct policy search algorithms for control problems with partial observations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many control applications, low-order controllers are often preferred over high-order controllers, because they are simpler to maintain, more interpretable, and computationally less demanding. Thus, given a high-order controller, one often would like to approximate it using a lower-order controller that still stabilizes the plant whilst performing similarly on relevant closed-loop performance metrics, such as the Linear Quadratic Gaussian (LQG) cost. This problem is known as *controller reduction*. Traditional approaches to controller reduction in LQG control have typically centered on reducing the order of observer-based controllers and providing error bounds between the performance of the truncated controller and that of the original controller.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the problem of order-reduction for general non-observer based controllers has been less studied, especially in the context of LQG control. Recent progress in model-free policy optimization for linear control has highlighted the importance of order-reduction for general controllers. In particular, a natural problem in model-free policy optimization is to learn an optimal policy iteratively using policy gradient methods. It has recently been shown that the optimization landscape of LQG control may contain saddle points in state-space dynamic controllers. While vanilla policy gradient ensures the convergence to stationary points under mild assumptions, these stationary points may be saddle points that are sub-optimal. As shown very recently, when a saddle point corresponds to a non-minimal controller, it is possible to escape the saddle point by finding a lower-order controller and adding a suitable random perturbation during policy gradient. It is thus natural to consider order-reduction for general non-observer based controllers, such that we find a lower-order controller with approximately equivalent or lower LQG cost.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, policy gradient for LQG control may also meet unstable controllers^11^1A dynamic controller that has unstable modes itself but internally stabilizes the plant., but the results on order-reduction for unstable controllers are far less complete. This motivates the main questions in this paper: Can we perform controller reduction on general, possibly unstable, LQG controllers, such that the reduced-order controller remains internally stabilizing?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Can we provide explicit error bounds on the LQG performance of the reduced-order controller compared to the original controller?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

These questions are not only relevant for the reasons relating to policy optimization of LQG control, but are interesting in their own right for the model and controller reduction literature.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions. In this paper, we provide positive answers to both questions. We first identify a novel set of sufficient conditions that ensure the stability of a perturbed controller (Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")), and then derive a new bound on the LQG cost of a perturbed controller under the assumption that the truncated component is stable and appropriately small (Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For general multiple-input and multiple-output (MIMO) systems, building on Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), we then show (in Section 4; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and Section 5.1 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") respectively) how balanced truncation and modal truncation may be applied to general (non observer-based, possibly unstable) LQG controllers to yield lower-order controllers with bounded LQG performance gap (compared to that of the original controller).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, for single-input and single-output (SISO) systems, we discuss in Section 5.2 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") how internal stability may be preserved even when the reduced-order controller has fewer unstable poles than the original controller.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This opens the path of controller reduction via truncating unstable poles, a novel controller reduction technique which we illustrate both theoretically and empirically. Finally, in Section 6; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), we characterize the connection between the existence of a "small" Jordan block with near pole-zero cancellation in SISO systems. This allows us to connect modal reduction with order reduction for minimal systems that are close to being non-minimal.

<!-- chunk {"id": "body-0013", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

Consider a strictly proper linear time-invariant (LTI) plant^22^2For simplicity, we assume that there is a common $B$ in front of both the $u{(t)}$ and $w{(t)}$ terms. where ${{x{(t)}} \in {\mathbb{R}}^{n}},{{{u{(t)}} \in {\mathbb{R}}^{m}},{{y{(t)}} \in {\mathbb{R}}^{p}}}$ are the state vector, control action, and measurement vector at time $t$, respectively; ${w{(t)}} \in {\mathbb{R}}^{m}$ and ${v{(t)}} \in {\mathbb{R}}^{p}$ are external disturbances on the state and measurement vectors at time $t$, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

One basic yet fundamental control problem is to design a feedback controller (or policy) to stabilize the plant 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."). A standard approach for this problem is to use an observer-based controller of the form where ${\xi{(t)}} \in {\mathbb{R}}^{n}$ is an estimated state, $L \in {\mathbb{R}}^{n \times p}$ is an observer gain, and $K \in {\mathbb{R}}^{m \times n}$ is a feedback gain.

<!-- chunk {"id": "body-0015", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

The observer and feedback gains are chosen such that $A - {LC}$ and $A - {BK}$ are stable, and this guarantees the closed-loop internal stability when applying the controller 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") to the plant 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") \[26, Chapter 3.5\]. Note that the order of this observer-based controller must be the same with the system plant (i.e., the controller state $\xi{(t)}$ and the system state $x{(t)}$ have the same dimension).

<!-- chunk {"id": "body-0016", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

Order reduction for controllers in the form of (2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")) is discussed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

In this paper, we consider a general non-observer based dynamic controller of the form where ${\xi{(t)}} \in {\mathbb{R}}^{q}$ is the internal state of the controller, and $A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}}$ are matrices of proper dimensions that specify the dynamics of the controller. The dimension $q$ of the internal control variable $\xi$ is called the order of the dynamical controller 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."). The controller in 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is more suitable for model-free policy optimization as it does not explicitly depend on the system dynamics.

<!-- chunk {"id": "body-0018", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

It is clear that the observer-based controller 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is a special case of 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") by taking $q = n$, and ${A_{\mathsf{K}} = {A - {BK} - {LC}}},{{B_{\mathsf{K}} = L},{C_{\mathsf{K}} = {- K}}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "General non-observer based controllers", "weight": 1.0} -->

By combining 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") with 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), the closed-loop system is internally stable if and only if the closed-loop matrix

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Given an internally stabilizing controller $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$ satisfying (4; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")), the controller reduction problem is to find a new controller $({\hat{A}}_{\mathsf{K}},{\hat{B}}_{\mathsf{K}},{\hat{C}}_{\mathsf{K}})$ of lower order $\hat{q} < q$ such that it still internally stabilizes the plant and does not significantly affect the closed-loop performance. In particular, we consider a normalized LQG control performance, defined as We make the following two assumptions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The plant (1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")) is minimal, i.e., $(A,B)$ is controllable and $(C,A)$ is observable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

In plant (1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")), the signals ${w{(t)}} \in {\mathbb{R}}^{m}$ and ${v{(t)}} \in {\mathbb{R}}^{p}$ are zero mean Gaussian white noise, each with a spectrum equal to the identity.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is standard and guarantees the existence of internally stabilizing controllers^33^3The existence of internally stabilizing controllers only requires stabilizability and detectablity.. If the plant is not minimal, we can always perform a lower-order minimal realization before designing a controller. Assumption 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") was used to define the normalized LQG control problem. As we shall see next, this assumption simplifies the expression of LQG cost 5; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") in the frequency domain.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For the controller reduction problem, it may not be easy to work directly with the internal stability condition 4; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") in the state-space domain due to non-uniqueness of state-space realizations. It is more convenient to consider equivalent conditions in the frequency domain. In particular, the controller 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") can be represented as a transfer function $\mathbf{K}:={C_{\mathsf{K}}{({{sI} - A_{\mathsf{K}}})}^{- 1}B_{\mathsf{K}}}$. Let us define a new performance signal $\overset{\sim}{y} = {Cx}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Some simple manipulations show that the closed-loop transfer function from $(w,v)$ to $(\overset{\sim}{y},u)$ is where ${\mathbf{G}{(s)}} = {C{({{sI} - A})}^{- 1}B}$. Then, we have the following condition for internal stability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Robust stability and LQG performance", "weight": 1.0} -->

Our main goal is to properly perturb the controller $\mathbf{K}$ to get a lower-order controller $\mathbf{K}_{r}$ such that the closed-loop performance remains similar.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Robust stability and LQG performance", "weight": 1.0} -->

In this section, we present two technical results that underpin our controller reduction results in Sections 4; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and 5; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."): 1) a new robust stability result (Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")), and 2) an upper bound on the LQG performance for the new controller $\mathbf{K}_{r}$ (Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na

<!-- chunk {"id": "body-0028", "role": "body", "section": "A novel sufficient condition for internal stability", "weight": 1.0} -->

Classical results on controller reduction often focus on the case when the truncated controller $\mathbf{K}_{r}$ has the same number of unstable poles as the original controller $\mathbf{K}$ (cf. ). Under such a condition, sufficient conditions are available using the $\mathcal{L}_{\infty}$ norm of terms involving the difference $\mathbf{K}_{r} - \mathbf{K}$ such that $\mathbf{K}_{r}$ can still stabilize $\mathbf{G}$ if $\mathbf{K}$ stabilizes $\mathbf{G}$. In particular, a widely-used condition is as follows.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") provide a

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

set of sufficient conditions for a reduced-order controller to internally stabilize the original plant.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

We comment here on some similarities and differences between the two sets of sufficient conditions. First, condition 2 in Lemma 3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is stated in terms of the $\mathcal{L}_{\infty}$ norm, while 7; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

Fazel); and nali@seas.harvard.edu (Na Li).") in Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") requires the $\mathcal{H}_{\infty}$ norm, thus condition 2 in Lemma 3.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is in fact a weaker requirement than 7; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

Li).")^55^5Note that an unstable transfer function may have finite $\mathcal{L}_{\infty}$ norm and only stable transfer functions can have finite $\mathcal{H}_{\infty}$ norm; for the definition of the $\mathcal{L}_{\infty}$ and $\mathcal{H}_{\infty}$ norm, the reader can refer to the notation in Section 1.2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")..

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

In addition, Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") requires that $\mathbf{\Delta}{({I - {\mathbf{G}\mathbf{K}}})}^{- 1}$ should be stable, whilst Lemma 3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") makes no such requirement.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

However, a key advantage of Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") over Lemma 3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is that it does not require $\mathbf{K}$ and its reduced-order counterpart $\mathbf{K}_{r}$ to have the same number of poles in ${Re{(s)}} > 0$ or

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

to have no poles on the imaginary axis.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

This suggests that effective controller reduction may not necessitate preserving all unstable poles of $\mathbf{K}$ --- this intuition will turn out to be useful for Theorem 3.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

‣ 5.2 Modal truncation on unstable component(s) ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") (Section 5.2 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 1 (Lemma 3. ‣ 3.1 A novel sufficient condition for internal stability ‣ 3 Robust stability and LQG performance ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\") versus Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).\"))", "weight": 1.0} -->

2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")), which shows that controller reduction via unstable modal truncation is in fact possible.

<!-- chunk {"id": "body-0044", "role": "body", "section": "A new bound on the perturbed LQG cost", "weight": 1.0} -->

Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") presents sufficient conditions to guarantee the closed-loop stability using the reduced-order controller $\mathbf{K}_{r}$. In many situations (such as policy optimization for LQG in ), we also need to understand the closed-loop performance under this new controller $\mathbf{K}_{r}$. Our next technical result show that if the error $\mathbf{\Delta} ≔ {\mathbf{K}_{r} - \mathbf{K}}$ is stable, the change of the LQG cost 5; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") can also be bounded.

<!-- chunk {"id": "body-0045", "role": "body", "section": "A new bound on the perturbed LQG cost", "weight": 1.0} -->

The proof builds on the analysis techniques in Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0046", "role": "body", "section": "Controller reduction via balanced truncation", "weight": 1.0} -->

In this section, we discuss controller reduction strategies using balanced truncation and apply Theorem 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") to derive stability and performance guarantees.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Balanced truncation", "weight": 1.0} -->

We begin with a result reviewing the following well-known fact about balanced truncation: for asymptotically stable transfer functions, under appropriate assumptions, a reduced-order transfer function resulting from balanced truncation is also asymptotically stable.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Controller reduction", "weight": 1.0} -->

In general, the dynamical controller $\mathbf{K}$ is not stable itself, i.e., $A_{\mathsf{K}}$ in 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") has unstable eigenvalues. The standard balanced truncation procedure cannot be applied to unstable systems directly. Our strategy is to divide the controller $\mathbf{K}$ into a stable part and unstable part where $\mathbf{K}_{<}$ of order $n_{1}$ contains all stable poles (i.e., those on the open left-half plane) and $\mathbf{K}_{\geq}$ of order $n_{2}$ contains the remaining poles (i.e., those on the closed right-half plane), and ${n_{1} + n_{2}} = n$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Controller reduction", "weight": 1.0} -->

In this section, we assume the controller contains at least one stable pole ($n_{1} \geq 1$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Controller reduction", "weight": 1.0} -->

We can then perform a balanced truncation on the stable part $\mathbf{K}_{<}$ and get a reduced-order controller where the order is $n_{r} < n_{1}$. The final reduced-order controller becomes which has order $r:={n_{r} + n_{2}} < n$. This process is summarized in Algorithm 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0051", "role": "body", "section": "Controller reduction", "weight": 1.0} -->

0: 1) A controller K with a minimal order-n state-space realization $\mathbf{K} = \begin{bmatrix} \end{bmatrix}$, 2) the post-truncation order r ≥ n2 with n2 defined in 24. 1: Compute the Jordan normal form of AK in 25. 2: Separate the controller K into K = K< + K≥ as 26. 3: Perform balanced truncation on the stable and minimal system K< with post-truncation order parameter nr < n1 to obtain an order-nr system K<,r. 4: return the reduced-order controller Kr = Kr, < + K≥ (of order r = nr + n2 < n).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Controller reduction", "weight": 1.0} -->

Algorithm 2 Balanced truncation for an unstable controller with stable part Based on Theorems 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), under appropriate conditions, the resulting controller $\mathbf{K}_{r}$ from Algorithm 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") remains a stabilizing controller and has a similar LQG cost compared to the original controller $\mathbf{K}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Controller reduction via modal truncation", "weight": 1.0} -->

In this section, we proceed to discuss controller reduction by modal truncation, which may apply to the truncation of either stable or unstable component(s) in a controller.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Controller reduction via modal truncation", "weight": 1.0} -->

In particular, we first apply modal truncation on the stable part of a controller in Section 5.1 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), and then discuss the performance of modal truncation on possibly unstable component(s) for SISO systems in Section 5.2 ‣ 5 Controller reduction via modal truncation ‣ On

<!-- chunk {"id": "body-0055", "role": "body", "section": "Controller reduction via modal truncation", "weight": 1.0} -->

Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Modal truncation on stable component(s)", "weight": 1.0} -->

0: 1) A controller K with a minimal order-n state-space realization $\mathbf{K} = \begin{bmatrix} \end{bmatrix}$; 2) the order reduction parameter rred (a positive integer less than k) 1: Convert AK into the standard Jordan normal form. 2: Decompose K as ${\mathbf{K}{(s)}} = {\sum_{i = 1}^{k}{C_{i}{({{sI} - A_{i}})}^{- 1}B_{i}}}$ that is consistent with the Jordan block 29. 3: For each i, compute the index di. 4: Let oi be the ranking of i according to {di}i = 1k, such that oi = j if di is the j-th smallest value. 6: return the reduced order controller Kr:= K − Δ.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Modal truncation on stable component(s)", "weight": 1.0} -->

Algorithm 3 Modal truncation The basic idea of modal truncation begins with writing the controller $\mathbf{K}$ 3; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") into ${\mathbf{K}{(s)}} = {\sum_{i = 1}^{k}{C_{i}{({{sI} - A_{i}})}^{- 1}B_{i}}}$, where $A_{i}$ contains a mode corresponding to an eigenvalue of $\lambda_{i}$ in $\mathbf{K}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Modal truncation on stable component(s)", "weight": 1.0} -->

This is always possible by considering its standard Jordan form where each $A_{i}$ is a Jordan block of order $n_{i}$, and ${{\sum_{i = 1}^{k}n_{i}} = n}.$ Let $\lambda_{i}$ denote the eigenvalue associated with each Jordan block $A_{i}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Modal truncation on stable component(s)", "weight": 1.0} -->

We then directly remove some modes that are less significant according the criterion defined below The detailed steps are listed in Algorithm 3 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0060", "role": "body", "section": "Modal truncation on stable component(s)", "weight": 1.0} -->

As a counterpart to balanced truncation, we can derive upper bounds the LQG cost change when performing modal truncation on the stable part of a controller $\mathbf{K}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Modal truncation on unstable component(s)", "weight": 1.0} -->

Next, we introduce the following result, which studies the LQG cost change when truncating unstable mode(s) of a controller $\mathbf{K}$, for single-input single-output (SISO) systems.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We note a limitation of our result, namely the requirement that the truncated Jordan blocks have non-zero eigenvalues. Hence, the procedure does not work when we wish to truncate a Jordan block corresponding to an zero eigenvalue. In addition, due to the relative simplicity of defining zeros for SISO systems, we chose to limit our attention to SISO systems. Extending to general MIMO remains future work.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Connecting near pole-zero cancellation to small Jordan block", "weight": 1.0} -->

An intuitive way of defining "near non-minimality" for a transfer function $\mathbf{G}{(s)}$ is the existence of a pair of pole $p_{i}$ and zero $q_{i}$ which are "close" to each other. Assuming that $p_{i}$ is a simple pole, when this happens, we then conjecture that the coefficient corresponding to the term $\frac{1}{s - p_{i}}$ in the partial fraction decomposition of $\mathbf{G}{(s)}$ is small, i.e. the Jordan block corresponding to the pole $p_{i}$ is small.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Connecting near pole-zero cancellation to small Jordan block", "weight": 1.0} -->

Below, we formalize this idea in the case $p_{i}$ is a simple pole^88^8We believe a similar result holds for the general case when $p_{i}$ is a repeated pole, and leave the precise characterization to future work..

<!-- chunk {"id": "body-0065", "role": "body", "section": "Comparing balanced truncation to modal truncation", "weight": 1.0} -->

We here compare the performance of balanced truncation versus modal truncation. Consider the following plant and controller pair It is easy to check numerically that $\mathbf{K}$ internally stabilize $\mathbf{G}$. Indeed, the closed-loop poles (i.e., eigenvalues of $A_{cl}$ in 4; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")) are (-0.38,-2.53, -2.15), each with multiplicity 2. Note that this controller $\mathbf{K}$ has an unstable mode $\lambda = 0.2$, thus the standard balanced truncation in Lemma 4.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Comparing balanced truncation to modal truncation", "weight": 1.0} -->

‣ 4.1 Balanced truncation ‣ 4 Controller reduction via balanced truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is inapplicable directly.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Comparing balanced truncation to modal truncation", "weight": 1.0} -->

As discussed in Section 4.2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), we separate the controller as $\mathbf{K} = {\mathbf{K}_{<} + \mathbf{K}_{\geq}}$, and perform reduction on the stable part $\mathbf{K}_{<}$ (i.e. Algorithms 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and 3 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF

<!-- chunk {"id": "body-0068", "role": "body", "section": "Comparing balanced truncation to modal truncation", "weight": 1.0} -->

ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).")).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

To illustrate Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and our results in Sections 4; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") and 5; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), we need to consider a plant $\mathbf{G}$ and a (possibly unstable) controller $\mathbf{K}$ that is internally stabilizing. To generate such instances, we first generate a random stable and minimal system, $\mathbf{K}_{<}$ and another unstable part $\mathbf{K}_{\geq}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

We define the augmented system $\mathbf{K} = {\mathbf{K}_{<} + \mathbf{K}_{\geq}}$, and compute a stabilizing controller for $\mathbf{K}$, which we call $\mathbf{G}$. Finally, we treat $\mathbf{G}$ as the system plant and $\mathbf{K}$ as the controller. It is thus clear that $\mathbf{K}$ internally stabilizes $\mathbf{G}$ (duality between plant and controller).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

After performing balanced truncation and modal truncation, we get two reduced-order controllers (of order 2) $\mathbf{K}_{r,{bt}}$ and $\mathbf{K}_{r,{mt}}$ respectively. Both $\mathbf{K}_{r,{bt}}$ and $\mathbf{K}_{r,{mt}}$ satisfy the bound in 16; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), thus internally stabilizes the plant, guaranteed by Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

Indeed, under Assumption 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), the LQG cost of the two truncated controllers are listed in Table 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."). In this example, the LQG cost of the balanced truncation is very close to the original performance, while the modal truncated controller has a slightly higher LQG cost. Note that the quantity $\left. \parallel{\mathbf{K} - \mathbf{K}_{r}}\parallel \right._{\mathcal{H}_{\infty}}$ is significantly smaller in the case of balanced truncation.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

Theorem 2; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") states that the upper bound on ${J{(\mathbf{K}_{r})}} - {J{(\mathbf{K})}}$ is tighter when $\left. \parallel{\mathbf{K} - \mathbf{K}_{r}}\parallel \right._{\mathcal{H}_{\infty}}$ is smaller; since $\left. \parallel{\mathbf{K} - \mathbf{K}_{r,{bt}}}\parallel \right._{\mathcal{H}_{\infty}} < \left.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

\parallel{\mathbf{K} - \mathbf{K}_{r,{mt}}}\parallel \right._{\mathcal{H}_{\infty}}$, this explains why $J{(\mathbf{K}_{r,{bt}})}$ is lower than $J{(\mathbf{K}_{r,{mt}})}$ in this case. We provide more extensive comparisons in Appendix D; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

Scaling effect of $\left. \parallel\mathbf{\Delta}\parallel \right._{\mathcal{H}_{\infty}}$. We next study how the performance gap behaves as a function of the size of the truncated component. For this analysis, we (randomly) generate five stable and minimal SISO systems of order 4, $\mathbf{K}_{r}$, and augment the system by adding a stable mode $\mathbf{\Delta}$, where We denote the augmented system as $\mathbf{K}:={\mathbf{K}_{r} + \mathbf{\Delta}}$. We then generate a stabilizing controller, $\mathbf{G}$, which stabilizes $\mathbf{K}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

Viewing $\mathbf{G}$ as the system plant, we then compare the LQG cost of $\mathbf{K}$ and $\mathbf{K}_{r}$ on the system $\mathbf{G}$, as the $\mathcal{H}_{\infty}$ norm of the truncated component, i.e. $\left. \parallel\mathbf{\Delta}\parallel \right._{\mathcal{H}_{\infty}}$, varies (to be precise, we plot 30 $\mathbf{\Delta}$'s, each corresponding to a different $\epsilon$, where we let $\epsilon$ range (equally spaced) between 0.0001 and 0.05).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

As we can see in Figure 1; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), for the five set of controllers, there is close to a linear relationship (with different slopes) between the LQG cost gap ratio $\frac{{J{(\mathbf{K}_{r})}} - {J{(\mathbf{K})}}}{J{(\mathbf{K})}}$ and the $\mathcal{H}_{\infty}$ norm of the truncated component, i.e. $\left. \parallel\mathbf{\Delta}\parallel \right._{\mathcal{H}_{\infty}}$; this is consistent with the upper bound on $J{(\mathbf{K}_{r})}$ in Theorem 3.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 3 (System generation)", "weight": 1.0} -->

‣ 5.2 Modal truncation on unstable component(s) ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0079", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

We here consider an example to illustrate Theorem 3. ‣ 5.2 Modal truncation on unstable component(s) ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).").

<!-- chunk {"id": "body-0080", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

Consider the following plant $\mathbf{G}$ It can be verified that the controller ${\mathbf{K} = \begin{bmatrix} \end{bmatrix}},$ with internally stabilizes $\mathbf{G}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

Applying Algorithm 3 ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), we obtain an order 2 controller $\mathbf{K}_{r}$, which removes the last (unstable) mode of $A_{\mathsf{K}}$, leading to ${\mathbf{K}_{r} =

<!-- chunk {"id": "body-0082", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

\begin{bmatrix} \end{bmatrix}},$ with The truncated component $\mathbf{\Delta}$ is unstable and takes the form which satisfies the bound 32.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

‣ 5.2 Modal truncation on unstable component(s) ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."). Thus, Theorem 3.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

‣ 5.2 Modal truncation on unstable component(s) ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") guarantees that the reduced-order controller $\mathbf{K}_{r}$ still internally stabilizes the plant.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

Indeed, numerical computation shows that the LQG cost of the original controller, $J{(\mathbf{K})}$, is 343.2, while the LQG cost of the truncated controller, $J{(\mathbf{K}_{r})}$, is 58.2. In this case, modal truncation not only yields a stabilizing lower-order controller, but also a cost of lower LQG cost.^1111^11For this instance, the theoretical upper bound posited in Theorem 3.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Truncating unstable mode(s)", "weight": 1.0} -->

‣ 5.2 Modal truncation on unstable component(s) ‣ 5 Controller reduction via modal truncation ‣ On Controller Reduction in Linear Quadratic Gaussian Control with Performance BoundsThe work of Zhaolin Ren and Na Li is supported by NSF CNS 2003111, NSF AI institute 2112085, and ONR YIP N00014-19-1-2217. The work of Yang Zheng is supported by NSF ECCS-2154650. The work of Maryam Fazel was supported by NSF TRIPODS II 2023166, CCF 1839291, CCF 2007036, and CCF 2212261. Emails: zhaolinren@g.harvard.edu (Zhaolin Ren); zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li).") is significantly larger than the original cost.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented on controller reduction for general non observer-based controllers using balanced truncation and modal truncation. For SISO systems, we demonstrate how LQG control may be performed even when there are no stable components in the controller. We hope that our work will be useful not only for policy optimization in LQG control but also for the controller reduction community. Two interesting future directions are 1) extending truncation of unstable modes to MIMO systems and 2) applying the results to escape saddle points in the LQG policy optimization.
