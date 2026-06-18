<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Trajectory-Based Framework for Data-Driven System Analysis and Control

Topics include Data-driven control, Behavioral systems, Trajectory spaces, Persistency of excitation, Data-driven simulation, Nonlinear systems, Kernel methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Recasts behavioral trajectory spanning in state-space language and extends the idea toward nonlinear systems that admit linear input-output coordinates. It helps connect classical control intuition, data-driven simulation, and later kernelized or nonlinear fundamental-lemma variants.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The vector space of all input-output trajectories of a discrete-time linear time-invariant (LTI) system is spanned by time-shifts of a single measured trajectory, given that the respective input signal is persistently exciting. This fact, which was proven in the behavioral control framework, shows that a single measured trajectory can capture the full behavior of an LTI system and might therefore be used directly for system analysis and controller design, without explicitly identifying a model. In this paper, we translate the result from the behavioral context to the classical state-space control framework and we extend it to certain classes of nonlinear systems, which are linear in suitable input-output coordinates. Moreover, we show how this extension can be applied to the data-driven simulation problem, where we introduce kernel-methods to obtain a rich set of basis functions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finding rigorous and efficient ways to integrate data into control theory has been a problem of great interest for many decades. Since most of the classical contributions in control theory rely on model knowledge, the problem of finding such a model from measured data, i.e., system identification, has become a mature research field. More recently, learning controllers directly from data has received increasing interest, not least due to many successful practical applications of reinforcement learning techniques. However, as is thoroughly evaluated, such methods typically require large amounts of data, they are often not reproducible, and their analysis rarely addresses rigorous guarantees, e.g., stability of the closed loop. Also in the control community, several approaches for the direct design of controllers from data have been proposed. Established methods include the Virtual Reference Feedback Tuning paradigm or Iterative Feedback Tuning. However, fundamental problems such as the direct data-driven design of linear quadratic optimal controllers with guarantees from finite noisy data have only been considered recently.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we consider an alternative, unitary framework for data-driven control theory, which allows for the development of various system analysis and controller design methods based directly on measured data. This framework relies on the characterization of all trajectories of an unknown system using a single measured data trajectory. The latter problem has been solved in the context of behavioral systems theory for discrete-time linear time-invariant (LTI) systems. In the behavioral approach, a system is not defined via a differential or difference equation with inputs and outputs, but rather as the space of all system trajectories. Thus, it is naturally well-suited for the development of purely data-driven approaches to system analysis and control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, there have been various contributions, which use the result of for direct data-driven system analysis and control. In, a data-driven MPC scheme relying on is suggested to control unknown systems. A stochastic analysis of this scheme and an application to power systems are detailed in and, respectively. Moreover, provides a first theoretical analysis of stability and robustness of a data-driven MPC scheme based on terminal equality constraints. In, a data-driven closed-loop parametrization under state-feedback is derived and employed to design stabilizing and LQR controllers. This approach is extended to robust design from noisy data. Further, provides a general framework for analyzing data-driven problems with not persistently exciting data. Finally, data-based conditions for dissipativity are suggested. Altogether, this indicates a great potential of the work of for direct data-driven analysis and control. In this paper, we consider the work of in the classical control framework and extend it to certain classes of nonlinear systems. Moreover, we illustrate the usefulness of this extension via a novel kernel-based approach to nonlinear data-driven simulation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is structured as follows. In Section III, we phrase the main theorem of, which uses measured data to characterize all system trajectories, in the classical control setting, and we show how this result can be improved by weaving multiple such trajectories together. In Section IV, we provide a novel extension of to classes of nonlinear systems, which are linear in suitably chosen and known nonlinear coordinates. Building on these results, we solve the data-driven simulation problem for such nonlinear systems in Section V. The paper is concluded in Section VI.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Setting", "weight": 1.0} -->

We denote the set of integers in the interval $\lbrack a,b\rbrack$ by ${\mathbb{I}}_{\lbrack a,b\rbrack}$. The Kronecker product is written as $\otimes$. For a sequence ${\{ x_{k}\}}_{k = 0}^{N - 1}$, we define the Hankel matrix

<!-- chunk {"id": "body-0009", "role": "body", "section": "Setting", "weight": 1.0} -->

For a stacked window of the sequence, we write

<!-- chunk {"id": "body-0010", "role": "body", "section": "Setting", "weight": 1.0} -->

Further, $x$ will denote either the sequence itself or the stacked vector $x_{\lbrack 0,{N - 1}\rbrack}$ containing all of its components. A key assumption for our results will be persistence of excitation of the input signal, as captured in the following standard definition.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Trajectory-based representation of linear systems", "weight": 1.0} -->

In this section, we translate the main result of, which characterizes the trajectory space of an unknown system from measured data, to the classical state-space control framework. While the behavioral theory is naturally well-suited for such a result, we illustrate that it can also be formulated in the classical framework in an elegant way. Further, we show how a required persistence of excitation assumption can be relaxed by weaving multiple trajectories together to achieve an overall larger time horizon.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Trajectory-based representation of linear systems", "weight": 1.0} -->

The following result is the correspondence of \[8, Theorem 1\] in the classical control setting and it will serve as the basis for the remainder of this paper.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Trajectory-based representation of nonlinear systems", "weight": 1.0} -->

In this section, we extend Theorem 3 to certain classes of nonlinear systems. In particular, we consider the special cases of Hammerstein and Wiener systems. More generally, this allows us to extend Theorem 3 to all systems, which are linear in suitably chosen and known input-output coordinates. During the last decades, there have been many contributions to identify Hammerstein and Wiener systems from data. Our results can be seen as an alternative to the identification of such systems, using a single measured trajectory to represent them.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A Hammerstein systems", "weight": 1.0} -->

A Hammerstein system is a nonlinear system, composed of a static nonlinearity followed by an LTI system, i.e.,

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Hammerstein systems", "weight": 1.0} -->

The following result uses the fact that can also be viewed as a linear map from $v$ to $y$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-B Wiener systems", "weight": 1.0} -->

A Wiener system consists of an LTI system followed by a static nonlinearity, i.e., it is of the form

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-B Wiener systems", "weight": 1.0} -->

with a nonlinear function $\phi:{{\mathbb{R}}^{\overset{\sim}{p}}\rightarrow{\mathbb{R}}^{p}}$. Similar to Section IV-A, we consider in the following only the case $\overset{\sim}{p} = 1$. To apply the same reasoning as for Hammerstein systems, we assume that $\phi$ is invertible and that its inverse admits a basis function decomposition as ${\phi^{- 1}{(y)}} = {\sum_{i = 1}^{q}{b_{i}{\overset{\sim}{\phi}}_{i}{(y)}}}$ with $q$ known basis functions ${\overset{\sim}{\phi}}_{i}$. We define an auxiliary output trajectory ${\{ z_{k}\}}_{k = 0}^{N - 1}$ with components

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B Wiener systems", "weight": 1.0} -->

which will serve as the output of an equivalent LTI system. The following result is the correspondence of Proposition 5 for the Wiener system case.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 7", "weight": 1.0} -->

From the perspective of Koopman operator theory, there has recently been a renewed interest in viewing nonlinear systems as linear systems in lifted state coordinates. In a similar fashion, Propositions 5 and 6 can be combined directly to provide trajectory-based representations of nonlinear systems, which are linear in suitable higher-dimensional input-output coordinates. Even if such coordinates do not exist or are not known, one may in practice simply choose sufficiently many basis functions to approximate the unknown nonlinear system. In Section V, we illustrate the effectiveness of this approach for the data-driven simulation problem. Note that considering systems which are linear in suitable input-output coordinates is more restrictive than dealing with systems which are linear in certain lifted state coordinates. On the other hand, in contrast to many methods related to Koopman operator theory, the present setting does not require state measurements, but only input-output data.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Data-driven simulation", "weight": 1.0} -->

The data-driven simulation problem is concerned with the computation of an unknown system's output resulting from the application of a given input, using no model but only a previously measured input-output trajectory. Its solution is described in the behavioral context. Loosely speaking, the idea is to fix $\overline{u}$ in to first solve $\overline{u} = {H_{L}{(u)}\alpha}$ for $\alpha$, in order to then compute the new predicted output $\overline{y} = {H_{L}{(y)}\alpha}$. To fix a unique such output, initial conditions have to be specified. Since a state-space model is not available, we consider an *initial input-output trajectory* over a length of at least $n$, since this induces a unique initial state in *some* minimal realization. The following is the main result of.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 10", "weight": 1.0} -->

We consider a Hammerstein system with nonlinearity ${\psi{(u)}} = {\sin{(u)}}$ and the system matrices

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 10", "weight": 1.0} -->

We assume that the system order $n = 4$ is known, i.e., $\nu = 4$. From an open-loop simulation, a trajectory ${\{ u_{k},y_{k}\}}_{k = 0}^{N - 1}$ of length $N = 1000$ is collected, where the output is subject to multiplicative measurement noise with signal-to-noise ratio $5\%$. Problem with a squared exponential kernel with $\sigma = 1$ is used to compute the output $\overline{y}$ resulting from a uniformly distributed random input $\overline{u}$ in the interval $\lbrack{- 0.3},0.3\rbrack$ of length $L = 50$ with zero initial conditions. The regularization parameter is chosen as $\lambda = 10$. Figure 1 shows the resulting output estimate as well as the true output for comparison. It can be seen that the estimate is good, considering the noise level.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 10", "weight": 1.0} -->

If the regularization term is omitted, i.e., $\lambda = 0$, or a fixed number of polynomial basis functions is chosen, then the estimation accuracy deteriorates significantly, even for smaller noise levels.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper described a purely data-driven framework for system analysis and control. All trajectories of an unknown system can be constructed from a single measured trajectory and thus, this trajectory captures all the required information needed for analysis and controller design, without explicit identification of a model. After describing this result in the classical control framework, we extended it to certain classes of nonlinear systems and we applied this extension to the data-driven simulation problem via kernel methods. Future research should further explore applications of the nonlinear extension presented in Section IV to data-driven system analysis and control problems, as well as connections to more elaborate results from the literature on kernel methods.
