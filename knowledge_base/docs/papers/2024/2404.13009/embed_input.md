<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Online Policy Optimization in Unknown Nonlinear Systems

Topics include Gradient descent, Regret bounds, Robustness, Online algorithms, Optimization, Control, Called memoryless GAPS, M-GAPS, Nonlinear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study online policy optimization in nonlinear time-varying dynamical systems where the true dynamical models are unknown to the controller. This problem is challenging because, unlike in linear systems, the controller cannot obtain globally accurate estimations of the ground-truth dynamics using local exploration. We propose a meta-framework that combines a general online policy optimization algorithm (textttALG) with a general online estimator of the dynamical system's model parameters (textttEST). We show that if the hypothetical joint dynamics induced by textttALG with known parameters satisfies several desired properties, the joint dynamics under inexact parameters from textttEST will be robust to errors. Importantly, the final policy regret only depends on textttEST's predictions on the visited trajectory, which relaxes a bottleneck on identifying the true parameters globally. To demonstrate our framework, we develop a computationally efficient variant of Gradient-based Adaptive Policy Selection, called Memoryless GAPS (M-GAPS), and use it to instantiate textttALG. Combining M-GAPS with online gradient descent to instantiate textttEST yields (to our knowledge) the first local regret bound for online policy optimization in nonlinear time-varying systems with unknown dynamics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a class of discrete-time policy optimization problems with unknown time-varying nonlinear dynamics (called nonautonomous systems in nonlinear control theory \[Slotine et al. \]). Our setting specifies a particular functional form of the dynamics and the parameterized policy class that is broad enough to capture applications from drone control to robotic manipulation. Our goal is to optimize the control policy online to minimize the total cost even if the online agent cannot obtain a globally accurate model of the true dynamics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Online policy optimization and the broader field of learning-based control have received significant attention over the last several years due to their ability to leverage data and adapt to time-varying dynamical systems. Online policy optimization faces two major challenges in practice. The first comes from the unknown dynamical model, which increases the difficulties of deciding the right directions for policy improvement. The second comes from the generality of dynamics/policy classes, which requires the algorithm to apply broadly to nonlinear time-varying dynamics and general policy classes. The early works in this field considered the linear-quadratic regulator (LQR) and linear time-invariant dynamics with adversarial disturbances, where the dynamics are known, linear, and time-invariant. Since then, much progress has been made to address challenges arising from considering either the unknown dynamical models or the general nonlinear dynamics, but addressing the two challenges simultaneously is still open.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One line of work focuses on online policy optimization under increasingly general classes of dynamical systems and policies, but under the assumption that the true dynamical models are known. For example, Lin et al. proposes an algorithm with provable regret guarantees that can be applied to nonlinear time-varying dynamical systems with general policy classes. However, assuming exact knowledge of the dynamical systems can be particularly restrictive in many applications when the system is nonlinear and time-varying. Even if the online agent has oracle access to a good dynamical model estimator, it is unclear whether the model estimation errors will accumulate in the policy update.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another line of work about online policy optimization focuses on learning the unknown dynamical models but is generally restricted to linear systems with specific policy classes. A common approach in the literature is random local exploration, where the controller either sets the control input to be a random perturbation or a randomly added perturbation to obtain sufficiently accurate estimations of the true dynamical model with high probability. However, in a more general nonlinear dynamical model, the online agent can no longer rely on small random perturbations to identify the true dynamical model well globally. This is because how the system responds to a small perturbation (approximately) depends on its linearization at the current state, and a nonlinear dynamical model can have different linearizations at different states.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The adaptive control literature also studies a similar problem. Typically, a set of linear parameters over a set of basis functions is dynamically adjusted online to compensate for the effect of time-varying disturbances, in order to stabilize the system and improve its trajectory tracking performance. Yu et al. proposes an adaptive stabilizing algorithm for unknown linear systems without any system identification. Shi et al. and O'Connell et al. recently proposed a meta-online adaptive control algorithm to address the time-varying prediction errors; however, their methods do not optimize the gains in the control policy. Another related work from control theory is online robust control, where the goal is to ensure stability or staying in the safety sets, subject to model uncertainty.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The motivating insight that we take from adaptive control is that the controller does not need to learn the true dynamical model to stabilize a system. The controller only needs to focus on "fitting" the actual trajectory it visited rather than "actively exploring" with the purpose of identifying the true model parameter. This idea of "lazy learning" is shared by some works on online robust control, which maintains a set of possible dynamical models that are consistent with past observations. In this work, we are interested in developing a general approach for online policy optimization that can address the challenges of dealing with both unknown dynamical models and general nonlinear dynamics/policy classes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We make three main contributions. First, we develop a meta-framework that combines an online policy optimization algorithm (ALG) with an online parameter estimator (EST), where ALG focuses on optimizing the policy parameters while EST focuses on estimating the unknown component in the dynamics. We specify a set of properties that, if satisfied, implies that our meta-framework can mimic the behavior of applying ALG with known dynamical models up to an error that depends on the predictions of EST. This setup enables us to reason about how to use existing results in online policy optimization and online regression (for model learning) as subroutines.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we provide a theoretical analysis of our meta-framework, establishing conditions under which we can derive regret guarantees. We study the behavior of our meta-framework in two steps: The first step (Section 3.1) focuses on the behaviors of ALG and treats the predictions of EST as external inputs. We specify a set of properties that make the joint dynamics of applying ALG to the original system robust to the errors injected by using EST instead of the true dynamical models. The second step (Section 3.2) formulates the task of EST as an online regression problem, where the states visited by ALG are treated as adversarial inputs that can adapt to the history, i.e., the adversary is non-oblivious). Compared to a standard online regression problem of minimizing the errors, EST faces the additional challenge of minimizing the errors of the model's partial derivatives with respect to the state. We address this challenge by showing a reduction from the regret of predicting these partial derivatives to the regret of predicting the unknown component when the original dynamics contain a certain level of randomness.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, we provide a concrete instantiation of our meta-framework on matched-disturbance dynamics. For ALG, we develop Memoryless Gradient-based Adaptive Policy Selection (M-GAPS), which extends the GAPS algorithm for online policy optimization to utilize only $O{}$ computational/memory complexity per time step and may be of independent interest. For EST, we utilize standard online regression. Combining these components, we obtain a bound on the local regret, an online analog of the stationary point conditions in nonconvex optimization. To our knowledge, this is the first local regret bound for online policy selection in nonlinear time-varying systems with unknown dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

It has a known function form $f_{t}$ and an unknown parameter $a_{t}^{\ast} \in \mathcal{A} \subseteq {\mathbb{R}}^{p}$. The disturbance term $w_{t} \in \mathcal{W} \subseteq {\mathbb{R}}^{n}$ does not depend on the states or the control inputs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

To control this system, the online agent adopts a time-varying control policy $\pi_{t}$ that is parameterized by a policy parameter $\theta_{t} \in \Theta \subseteq {\mathbb{R}}^{d}$, where $\Theta$ is a closed convex subset of ${\mathbb{R}}^{d}$. Specifically, the online agent picks the control input from the policy class $u_{t} = {\pi_{t}\left( x_{t},\theta_{t},{f_{t}{(x_{t},{\hat{a}}_{t})}}) \right.}$. Here, function $f_{t}{( \cdot,{\hat{a}}_{t})}$ reflects the online agent's current estimation of the ground true nonlinear residual function $f_{t}{( \cdot,a_{t}^{\ast})}$ at time step $t$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Intuitively, we assume the policy class $\pi_{t}$ cares about predicting the true nonlinear residual $f_{t}{(x_{t},a_{t}^{\ast})}$ rather than the unknown model parameter $a_{t}^{\ast}$. The objective of the online agent is to minimize the total cost $\sum_{t = 0}^{T - 1}c_{t}$ incurred over a finite horizon, where the stage cost at time step $t$ is given by $c_{t} = {h_{t}{(x_{t},u_{t},\theta_{t})}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We provide a simple nonlinear control example that can be captured by our online policy optimization framework to help the readers understand the concepts we discussed.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

Consider the problem of controlling a scalar discrete-time nonlinear system: In this equation, $\Delta$ is the discretization step size. The nonlinear residual takes the form ${\phi{(x_{t})}} \cdot a_{t}^{\ast}$, where $\phi:{{\mathbb{R}}\rightarrow{\mathbb{R}}^{k}}$ is a (nonlinear) feature map and $a_{t}^{\ast}$ is the unknown model parameter. To control this system, the online agent with an estimated model parameter ${\hat{a}}_{t}$ can adopt the policy class: Here, the goal of the second term $- {f_{t}{(x_{t},{\hat{a}}_{t})}}$ is to cancel out the true nonlinear residual $f_{t}{(x_{t},a_{t}^{\ast})}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

In an ideal case where the online agent has access to the true model parameter $a_{t}^{\ast}$, policy achieves the effect of removing the nonlinear residual and directly doing feedback control, resulting in the closed-loop dynamics ${x_{t + 1} = {x_{t} + {\Delta\left({{- {k_{t}x_{t}}} + w_{t}} \right)}}}.$ In this case, the problem reduces to finding the optimal policy parameters (gains) $\{\theta_{t}\}$ in a known time-varying dynamical system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Performance Metrics", "weight": 1.0} -->

In the literature of online optimization, regret is a common performance metric that directly compares the total cost $\sum_{t = 0}^{T - 1}c_{t}$ incurred by the online policy optimization algorithm against the optimal total cost one can achieve in hindsight. Before introducing variants of the regret we study, we first introduce the concept of the surrogate cost. The present formulation extends the similarly named concept of Lin et al. to the setting where the true dynamical models are unknown.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main Results", "weight": 1.0} -->

Our approach is outlined in Section 3, where two modules ALG and EST work together to update the policy and estimated model parameter at each time step (see Figure 2 for an illustration). ALG and EST are responsible for optimizing the policy parameters $\theta_{0:{T - 1}}$ and learning the unknown model parameters $a_{0:{T - 1}}^{\ast}$ respectively: ALG: At time step $t$, ALG receives the current state $x_{t}$, policy parameter $\theta_{t}$, and the known part of the time-varying system $\pi_{t},g_{t},h_{t},f_{t}$. It also receives the current estimation ${\hat{a}}_{t}$ of the unknown model parameter $a_{t}^{\ast}$. Then, ALG outputs the new policy parameter $\theta_{t + 1}$. Note that we allow ALG to leverage/memorize historical inputs by maintaining an internal state $y_{t}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main Results", "weight": 1.0} -->

EST: At time step $t$, EST receives the current state $x_{t}$ and a (noisy) observation ${\overset{\sim}{f}}_{t}$ of the unknown component $f_{t}{(x_{t},a_{t}^{\ast})}$. Then, EST outputs the new estimation ${\hat{a}}_{t + 1}$. Like ALG, we allow EST to keep internal state/memory (e.g., to memorize historical input data).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main Results", "weight": 1.0} -->

The key idea in analyzing our meta-framework (Section 3) is to characterize how the inexact model estimations generated by EST affect the behavior ALG. We start by considering the "ideal" dynamics of applying ALG with exact model parameters $a_{0:{T - 1}}^{\ast}$, which we denote as $\text{ALG}^{\ast}$, and compare them with the actual dynamics of ALG that performs the update with estimated model parameters ${\hat{a}}_{0:{T - 1}}$. We state the key insight of our analysis in the informal lemma below, which connects the performance of the meta-framework with $\text{ALG}^{\ast}$ and the model mismatches.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

In this section, we take a perspective that views the updates performed by ALG as part of a joint dynamics formed together with the original dynamical system. Compared to the common approach of analyzing ALG separately from the dynamical system to which it applies, our dynamical view enables us to compare the differences of applying ALG under different external inputs (i.e. different ${\hat{a}}_{t}$ estimates) more efficiently.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

We consider the class of online policy optimization algorithms whose joint dynamics with the original system can be written in the following form: When the model parameter $a_{t}$ is given as the input to ALG at time step $t$, the joint dynamics can be written as Here, $y_{t} \in {\mathbb{R}}^{p}$ is an auxiliary state that ALG can use to store something besides the system state $x_{t}$ and the policy parameter $\theta_{t}$ to help it perform the update. For example, $y_{t}$ can be a finite memory buffer that stores information from the past. It can also be the integral of past states in an integral controller. Thus, we introduce $y_{t}$ to allow broader classes of online policy optimization algorithms, and we will provide a concrete example of $y_{t}$ later in Section 4.1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

The goal of formulating joint dynamics is to compare the behaviors of the meta-framework and $\text{ALG}^{\ast}$ with perturbations on policy parameter updates. Specifically, recall that ${\hat{a}}_{0:{T - 1}}$ denote the estimated model parameters of EST. The actual trajectory of the meta-framework is We compare it with the joint dynamics of $\text{ALG}^{\ast}$ (see Figure 2). Recall that $\text{ALG}^{\ast}$ denotes the scenario when ALG has access to exact model parameters $a_{0:{T - 1}}^{\ast}$: Here, $\zeta_{t}$ is an additive perturbation on the update equation of policy parameter $\theta_{t + 1}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

To understand intuitively, it is helpful to draw connections with the process of using a gradient-based optimizer to update the parameter $\theta_{t}$ in ML, where $\zeta_{t} \equiv 0$ corresponds to the case when exact gradients are available. In contrast, nonzero perturbations correspond to the more practical case when the optimizer can only use biased estimations of the gradient, which still performs well in general.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

Note that the estimated model parameters ${\hat{a}}_{0:{T - 1}}$ generated by EST may also depend on the state $x_{t}$ and other parts of the dynamical system. Thus, a natural question is whether we should also incorporate the update rule of EST into the joint dynamical system, where we include ${\hat{a}}_{t}$ as another element of the joint state. However, we still choose to model ${\hat{a}}_{t}$ as an external input in and handle the update of ${\hat{a}}_{t}$ separately in Section 3.2. This is because our approach requires comparing the actual joint dynamics. Since $a_{t}^{\ast}$ is an external input decided by the environment, keeping the joint state space identical in makes the comparison easier. Further, a strength of our proof framework based on the joint dynamics is that we can show the actual trajectory will stay close to.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

However, we know that the estimated model parameter sequence $\{{\hat{a}}_{t}\}$ will not converge to the true sequence $\{ a_{t}^{\ast}\}$ in general.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

We state three important properties of the joint dynamics induced by ALG. The first property is about the Lipschitzness with respect to the model mismatches $\varepsilon_{t}$ and $\varepsilon_{t}'$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Property 3.2", "weight": 1.0} -->

Intuitively, Property 3.2 says that the error brought by the inexact model parameters only "distort" the ideal joint dynamics in the form of zeroth-order and first-order prediction errors. Therefore, to bound the error injected into the joint dynamics at every step, EST only needs to minimize $\varepsilon_{t}$ and $\varepsilon_{t}'$ on the actual state trajectory $x_{0:{T - 1}}$ that the online agent visits. Note that this property can be viewed as a standard assumption about Lipschitzness if ALG is a gradient-based algorithm. This is because all terms that involve the unknown model parameter will take the form $f_{t}{(x_{t},{\hat{a}}_{t})}$ and ${\nabla_{x}f_{t}}{(x_{t},{\hat{a}}_{t})}$ in the joint dynamics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Property 3.2", "weight": 1.0} -->

The second property is about contraction stability of $x_{t}$ and $y_{t}$ under exact model parameters $a_{0:{T - 1}}^{\ast}$. As we show in Theorem 3.5, this property guarantees that the dynamical updates of states $x_{t}$ and $y_{t}$ in the joint dynamics are robust to the model mismatches ${\{\varepsilon_{t},\varepsilon_{t}'\}}_{0:{T - 1}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Property 3.3", "weight": 1.0} -->

Intuitively, Property 3.3 guarantees that when the exact model parameters $\{ a_{t}^{\ast}\}$ are replaced by inexact $\{{\hat{a}}_{t}\}$, the resulting trajectory $\{{(x_{t},y_{t})}\}$ still stays close to the trajectory that $\theta_{0:{T - 1}}$ would achieve under exact predictions once the mismatch errors $\varepsilon_{t},\varepsilon_{t}'$ are small or bounded. Property 3.3 can be viewed as an extension of the time-varying stability and contractive perturbation property in Lin et al. to include state $y_{t}$ maintained by ALG. This is required in our framework because $y_{t}$ can be affected by the prediction errors and it is involved in the dynamics of updating $\theta_{t}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Property 3.3", "weight": 1.0} -->

The third property we need is the robustness of the update rule of the policy parameter $\theta_{t}$. Specifically, it requires the regret guarantee achieved by ALG to be robust against a certain level of adversarial disturbances $\{\zeta_{t}\}$ on the update dynamics of $\theta_{t}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Property 3.4", "weight": 1.0} -->

\[Robustness\] Consider the joint dynamics. When $\left. \parallel\zeta_{t}\parallel \right. \leq \overline{\zeta}$ holds for all $t$, the resulting $\{\theta_{t}\}$ satisfies the slowly-time-varying constraint $\left. \parallel{\theta_{t} - \theta_{t - 1}}\parallel \right. \leq \epsilon_{\theta}$ for all time $t$. Further, $\text{ALG}^{\ast}$ with perturbations can achieve a regret guarantee $R{(T,{\sum_{t = 0}^{T - 1}\left. \parallel\zeta_{t}\parallel \right.})}$ that depends on the total magnitude of the perturbation sequence $\zeta_{0:{T - 1}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Property 3.4", "weight": 1.0} -->

To understand Property 3.4, we can think about online gradient descent (OGD) in online optimization problems without state or dynamics. It is known that this approach is robust to (biased) disturbances on the gradient estimation, and the total amount of added disturbances will affect the final regret bound (see, for example, Theorem I.1).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Property 3.4", "weight": 1.0} -->

Now, we present our main results about the stability of applying ALG with inexact model parameters and the regret bound in Theorem 3.5. Besides, Theorem 3.5 also bounds the distances between the actual trajectory and the trajectory achieved by applying the same policy parameter sequence with the exact model parameter sequence.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Online Parameter Estimation", "weight": 1.0} -->

The second part of our meta framework focuses on predicting the unknown model parameter based on possibly noisy observations of the true nonlinear residual $f_{t}{(x_{t},a_{t}^{\ast})}$. A critical difference with prior works on system identification or model-based learning (e.g., Dean et al.) is that we only seek to optimize the zeroth-order and first-order model mismatches $\{\varepsilon_{t},\varepsilon_{t}'\}$ (defined in) on the actual trajectory that the online agent experiences.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Online Parameter Estimation", "weight": 1.0} -->

It is worth noticing that, although learning the ground-truth model parameter $a_{t}^{\ast}$ is impossible for a general nonlinear residual, minimizing the sum of zeroth-order model mismatches incurred on the actual trajectory can be formulated as a classic online regression problem, which we discuss below: Online regression problem: At the beginning, the environment commits a sequence of error functions $e_{t}:{{{{\mathbb{R}}^{n} \times \mathcal{A}}\rightarrow{\mathbb{R}}},{t = {0,\ldots,{T - 1}}}}$, which are defined as ${e_{t}{(x,a)}} ≔ {{f_{t}{(x,a_{t}^{\ast})}} - {f_{t}{(x,a)}}}$ for $t = {0,\ldots,{T - 1}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Online Parameter Estimation", "weight": 1.0} -->

^22^2Thus, the error functions $e_{0:{T - 1}}$ will not adapt to the inputs and online decisions. The relationship between the error function $e_{t}$ and the model mismatches $\{\varepsilon_{t},\varepsilon_{t}'\}$ is ${\varepsilon_{t} = \left. \parallel{e_{t}{(x_{t},{\hat{a}}_{t})}}\parallel \right.},$ and ${\varepsilon_{t}' = \left.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Online Parameter Estimation", "weight": 1.0} -->

Under different sets of assumptions on the error functions and the sequence of true model parameters $\{ a_{t}^{\ast}\}$, existing online algorithms can achieve regret guarantees. We consider a general form of expected regret bound: ${{{\mathbb{E}}\left\lbrack {\sum_{t = 1}^{T}\ell_{t}} \right\rbrack} \leq {R_{0}^{\ell}{(T)}}},$ where the expectation is taken over the randomness of implementing EST and generating $x_{t}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Online Parameter Estimation", "weight": 1.0} -->

While different assumptions and designs of EST can achieve different bounds on $R_{0}^{\ell}{(T)}$, an example we provide in Section 4 shows that a simple gradient estimator can achieve sublinear $R_{0}^{\ell}{(T)}$ when the nonlinear residual can be decomposed as ${f_{t}{(x,a)}} = {{\phi{(x)}} \cdot a}$ under the path length constraint ${\sum_{t = 1}^{T - 1}\left. \parallel{a_{t + 1}^{\ast} - a_{t}^{\ast}}\parallel \right.} \leq C$ (see Section 4.2 for detailed discussions).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

Besides the online policy optimization problem for control, the regret bound that concerns $\left. \parallel{{\nabla_{x}e_{t}}{(x_{t},{\hat{a}}_{t})}}\parallel \right.$ can be of independent interest for the problem of online regression, because it characterizes how sensitive the regression loss is to any perturbations on the input sequence $x_{0:{T - 1}}$ under the same estimations ${\hat{a}}_{0:{T - 1}}$. Intuitively, if gradients of the error functions are small, the estimations ${\hat{a}}_{0:{T - 1}}$ will be robust to small perturbations on the input sequence.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

To enable a reduction from the regret bound $R_{0}^{\ell}{(T)}$ to the gradient error bound, we employ Property 3.7 about the dynamical system that generates the state $x_{t}$. Specifically, we require there to be at least a small level of randomness when choosing $x_{t}$. Recall that ${\hat{a}}_{t + 1}$ is decided based on the history $x_{0:t}$ and ${\hat{a}}_{0:t}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Application: Matched Disturbance", "weight": 1.0} -->

In this section, we consider an instantiation of our setting to demonstrate the effectiveness of our meta-framework. Specifically, we study the matched-disturbance dynamics, where the controller can choose a control input to "cancel out" the nonlinear residual term $f_{t}{(x_{t},a_{t}^{\ast})}$ when the exact model parameter $a_{t}^{\ast}$ is available. The dynamics have the form A ubiquitous application of the matched disturbance dynamics is the general joint-space dynamics of robotic manipulators when the system has actuators for every joint. The matched-disturbance structure also appears in tilted-rotor rotorcraft, which can move in six degrees of freedom. In both cases, due to the second-order structure of the rigid-body dynamics, all external disturbances are equivalent to additional joint torque (resp. rotor tilt/thrust) inputs. Our Example 2.1 also fits into the framework of.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Application: Matched Disturbance", "weight": 1.0} -->

To control a matched-disturbance system, a natural policy class is to first cancel out the nonlinear residual with $- {f_{t}{(x_{t},{\hat{a}}_{t})}}$ and then apply an actuation term $\psi_{t}{(x_{t},\theta_{t})}$ to achieve the optimal costs. This policy class can be expressed as To derive local regret for the meta-framework, we need assumptions (Assumptions C.4-C.8) on the system that includes the dynamics, policy classes, and costs, which we discuss in detail in Appendix H. Note that the matched-disturbance dynamics/policy class we consider can recover the setting as a special case when $f_{t}$ and $w_{t}$ are always zero (so there is no need to estimate $a_{t}^{\ast}$). We recover the same regret bound as Lin et al. in that special case (see Lemma 4.1).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Online Policy Optimization: M-GAPS", "weight": 1.0} -->

This section introduces a general online policy optimization algorithm, Memoryless Gradient-based Adaptive Policy Selection (M-GAPS, Section 4.1), which can serves as ALG in our meta-framework. M-GAPS use ${\hat{a}}_{t}$ to estimate how the current state $x_{t}$ and policy parameter $\theta_{t}$ would affect the next state $x_{t + 1}$ and the current cost. The estimations are characterized by Although M-GAPS can be applied to any online policy optimization problems that fit into the setting we discussed in Section 2, we focus on its application to disturbance-matched dynamics and policy class for theoretical analysis. We verify that the joint dynamics of M-GAPS satisfy the required properties of our meta-framework to derive a concrete regret bound in Appendix C.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Online Policy Optimization: M-GAPS", "weight": 1.0} -->

Memoryless Gradient-based Adaptive Policy Selection (M-GAPS, for ALG) \\DontPrintSemicolonParameters: Learning rate $\eta$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Online Policy Optimization: M-GAPS", "weight": 1.0} -->

The design of M-GAPS takes inspiration from the Gradient-based Adaptive Policy Selection (GAPS) algorithm, but it significantly improves computational efficiency and generality. Specifically, in the setting where the online agent has exact knowledge of the time-varying dynamical models, M-GAPS can achieve the same regret guarantees as GAPS, while the memory/computational complexities are reduced from $O{({\log T})}$ to $O{}$. To understand why this improvement is possible, note that the core problem of GAPS is to design an efficient estimation of ${\nabla F_{t}}{(\theta_{t})}$. GAPS does two steps of approximations: first replacing the imaginary trajectory with the actual trajectory and then doing a bounded-memory truncation. In comparison, M-GAPS only keeps the first approximation step of GAPS but greatly simplifies the computation by introducing the auxiliary internal state $y_{t}$ that accumulates past partial derivatives.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Online Policy Optimization: M-GAPS", "weight": 1.0} -->

Intuitively, the estimation of M-GAPS is even closer to ${\nabla F_{t}}{(\theta_{t})}$ than GAPS, so it can achieve the same regret guarantees as GAPS. A more detailed comparison between M-GAPS and GAPS can be found in Appendix J.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Online Policy Optimization: M-GAPS", "weight": 1.0} -->

A key step of our proof shows that, when exact model parameters $a_{0:{T - 1}}^{\ast}$ are available, M-GAPS is robust against perturbations on policy parameter updates as required by Property 3.4 in Section 3.1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Online Parameter Estimation: Gradient Estimator", "weight": 1.0} -->

We instantiate EST with the gradient estimator (Section 4.2), where ${\overset{\sim}{f}}_{t}$ is a (noisy) observation of $f_{t}{(x_{t},a_{t}^{\ast})}$ provided by the environment. It performs online gradient descent on an estimated prediction loss function constructed from ${\overset{\sim}{f}}_{t}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Online Parameter Estimation: Gradient Estimator", "weight": 1.0} -->

Gradient Estimator (for EST) \\DontPrintSemicolonParameters: Learning rate $\iota$; Initialize: Model parameter estimation ${\hat{a}}_{0}$. $t = {0,1,\ldots,{T - 1}}$ Take inputs $x_{t}$ and ${\overset{\sim}{f}}_{t}$. \\tcc\*Inputs given when meta-framework calls $\text{EST}.\text{update}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Online Parameter Estimation: Gradient Estimator", "weight": 1.0} -->

Using Theorems 3.5 and 3.8, we show a local regret guarantee of our meta-framework in Theorem 4.2 and test it numerically in the setting of Example 2.1. Due to space limit, we defer the proof of Theorem 4.2 to Appendix H and the simulation results to Appendix A.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we study online policy optimization with unknown dynamics. We propose a meta-framework combining an online policy optimization algorithm ALG with an online parameter estimator EST. We specify a set of properties that, if satisfied, imply that ALG can act as if EST is providing the true dynamics models, while EST only needs to minimize the prediction errors on the actual trajectory visited by ALG. To demonstrate our framework, we propose an efficient candidate for ALG called M-GAPS (Algorithm 4.1). When our meta-framework is instantiated with M-GAPS (as ALG) and the gradient estimator (as EST), it achieves the first local regret bound (Theorem 4.2) for online policy optimization in a class of nonlinear time-varying systems with unknown dynamics.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our meta-framework also motivates interesting future work: The structural properties of ALG and EST that we identify can serve as guidelines for the design of improved online policy optimization and dynamics estimations methods. For example, tools from online nonconvex optimization and adaptive control could be leveraged to handle more general classes of dynamics.
