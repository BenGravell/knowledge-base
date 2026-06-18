<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Feedback Linearization Using the Koopman Generator

Topics include Online algorithms, Control, KGFL, Feedback linearization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper contributes a theoretical framework for data-driven feedback linearization of nonlinear control-affine systems. We unify the traditional geometric perspective on feedback linearization with an operator-theoretic perspective involving the Koopman operator. We first show that if the distribution of the control vector field and its repeated Lie brackets with the drift vector field is involutive, then there exists an output and a feedback control law for which the Koopman generator is finite-dimensional and locally nilpotent. We use this connection to propose a data-driven algorithm Koopman Generator-based Feedback Linearization (KGFL) for feedback linearization. Particularly, we use experimental data to identify the state transformation and control feedback from a dictionary of functions for which feedback linearization is achieved in a least-squares sense. We also propose a single-step data-driven formula which can be used to compute the linearizing transformations. When the system is feedback linearizable and the chosen dictionary is complete, our data-driven algorithm provides the same solution as model-based feedback linearization. Finally, we provide numerical examples for the data-driven algorithm and compare it with model-based feedback linearization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also numerically study the effect of the richness of the dictionary and the size of the data set on the effectiveness of feedback linearization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonlinear control methods rooted in model-based approaches have received considerable attention. Among these techniques, feedback linearization has emerged as a prominent strategy, offering the implementation of straightforward linear control methodologies to nonlinear systems. However, a notable limitation of this approach is its demand for a comprehensive knowledge of the system dynamics. Consequently, inadequate system identification in the context of complex, high-dimensional cyber-physical systems can lead to poor control performance. On the contrary, machine learning methodologies offer a robust alternative, enabling the utilization of experimental data acquired from the system to facilitate feedback control, even in the absence of prior knowledge regarding the underlying system's dynamics. Nevertheless, these machine learning methods frequently fall short of providing comprehensive insights into both their own performance and the intricate nature of the systems they operate. Furthermore, the full extent of their limitations remains a subject of ongoing investigation. The pursuit of a systematic framework for nonlinear data-driven control remains an unresolved challenge.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, significant attention has been directed towards the Koopman operator due to its capacity to furnish a global (infinite-dimensional) linear representation of autonomous nonlinear systems. It was shown in that the Koopman operator can be approximated in finite dimensions with data using a dictionary of observables, which has been a notable direction of research for nonlinear systems. However, the commonality between the two aforementioned methodologies pertains to the concept of complete linearization, a dimension of inquiry that has hitherto remained unexplored in the existing literature. In this work, we bridge the gap between the conventional technique of feedback linearization and the Koopman operator. Furthermore, leveraging this newfound connection, we develop a data-driven methodology capable of yielding valuable insights into the dynamics inherent to the system.\

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $x \in {\mathbb{X}} \subseteq^{n}$ is the state, $u \in$ is the control input, and $f,g:{\mathbb{X}}\rightarrow^{n}$ are the drift and control vector fields. In the data-driven setting, we do not have access to the drift and control vector fields $f,g$, but instead have access to $N$ data samples collected from a control experiment on System. The state and control trajectory during the experiment is $\left\{ x_{t},u_{t} \right\}$ where $t \in {\mathbb{R}}_{\geq 0}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $x_{i}$ and $u_{i}$ are the sample at the $i$-th instance of the experiment. In the experiment, the control $u$ is assumed to be sufficiently exciting so as to provide data of good quality. For instance, $u_{t}$ could be sampled from a Gaussian distribution.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our objective is to transform system to a target linear system $\overset{˙}{z} = {{Az} + {Bv}}$, where $z$ and $v$ are transformed state and control, respectively. We propose to transform the state as $z = {H{(x)}}$ and the control as $u = {{\alpha{(x)}} + {\beta{(x)}v}}$. We seek to identify the transformations ${H,\alpha},$ and $\beta$ using the data $X,U$.\

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work. A comprehensive introduction to feedback linearization can be found. This technique provides a systematic method to identify the necessary state and control transformations in the model-based case. It is crucial to note that these transformations are dependent on the dynamics of the system and not all systems allow for feedback linearization. An approximate, but still model-based, approach for feedback linearization was proposed. These methods cannot be employed without a prior system identification step. Several works that combine learning methods for feedback linearization have been proposed. The works primarily use neural networks to obtain state and control transformations, whereas proposes a reinforcement learning approach. However, these methods do not provide a clear insight into the control and state transformations. In, a SISO full state-feedback linearizable system is considered and a data-driven solution is proposed by approximating the system using Taylor series. An extension of the Willems fundamental lemma for nonlinear systems is proposed, which is used to present a predictive control methodology with data. However, a systematic approach to finding the state and control transformations in the data-driven setting for feedback linearization has not been addressed in the literature.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we seek to establish a data-driven methodology for feedback linearization which not only provides a convenient solution but also insight into the dynamics of the system.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main advantage of the Koopman operator is its ability to provide a global linear representation of a nonlinear system. However, its main drawback is its infinite-dimensional representation for only autonomous systems. Recent literature has focused on finite-dimensional approximations of the Koopman operator. Of particular interest is the gEDMD algorithm which seeks a finite-dimensional approximation of the infinitesimal generator of the Koopman operator and is based on Extended Dynamic Mode Decomposition (EDMD). The gEDMD algorithm uses a dictionary of functions to lift full-state data from an autonomous system and seeks to find a linear relation in the evolution of the lifted system.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The works in have focused on obtaining accurate finite-dimensional approximations of this linear operator for control. While have extended for control, transforms the nonlinear system as a linear parameter-varying system with the control as the variable parameter. In, linear predictors for the control-affine nonlinear system are considered. However, crucially, the control transformations required for exact linearization and its connection to feedback linearization are absent. A Luenberger observer for the system's nonlinearities is proposed using the Koopman operator. Here the control is considered as a varying parameter, and the overall system is considered as a linear parameter varying system. Hence, existing literature that use the Koopman operator for control have crucially missed the connection to feedback linearization. Bilinearization using the Koopman operator has also been an area of interest. In, the nonlinear system is approximated by interpolated bilinear systems. Then a model predictive control scheme is applied to the identified interpolated bilinear model. Probabilistic error bounds on trajectories predicted by bilinearized models using the Koopman operator are given. Conditions for global bilinearizability using the Koopman operator are given.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, it is important to note that standard linear control techniques cannot be implemented on bilinear models. The model-based feedback linearization approach and the modern data-driven Koopman operator approach are both linearization techniques, yet for controlled and autonomous systems, respectively. In this paper, we focus on showing a connection between these two methods and developing a data-driven scheme for nonlinear control.\

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. The main contributions of this paper are as follows. We first bridge the gap between the geometric framework of feedback linearization and the Koopman operator-theoretic framework. In particular, we show that, when the system is involutive to a certain degree, there exists an observable $h$ and a feedback control $\alpha$ such that the Koopman generator for the closed-loop system under the feedback $\alpha$ is nilpotent at the observable $h$. Furthermore, there exists a finite-dimensional Koopman invariant subspace of the same dimension as the involutive distribution for the system. This connection to the Koopman operator allows us to develop a data-driven method for feedback linearization, by essentially casting the problem of data-driven feedback linearization as one of learning the closed-loop Koopman operator for the nonlinear control-affine system by a linearizing state/control transformation. To this end, we exploit the fact that involutivity permits a representation of the Koopman generator in the finite-dimensional Brunovsky canonical form under the linearizing state/control transformation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This allows us to fix the Brunovsky canonical form as the target linear representation and learn the linearizing transformation using a set of fixed dictionary functions by a least-squares method in our algorithm *Koopman generator-based Feedback Linearization (KGFL)*. We also provide a numerical feedback linearization scheme with only input-output data. With input-output data, we show that the control transformations can be learned in a least-squares sense using a simple data-driven formula. The results, which were developed independently from this work, deal with data-driven feedback linearization with complete dictionaries for fully feedback linearizable systems. In our work, we neither make the assumption of full feedback linearizability nor of complete dictionaries. However, when the system is feedback linearizable and the dictionaries used in KGFL are complete, the solution is exact and is equal to the model-based solution. Finally, we demonstrate the performance of our algorithm with numerical simulations for multiple examples. We perform both full state feedback linearization and output feedback linearization on the Van der Pol oscillator and compare it against existing nonlinear data-driven control techniques.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a higher dimensional system with the control entering nonlinearly and show that our algorithm can be used for complex systems. We also provide insight on the effect of richness of dicitonary and data size on the accuracy of feedback linearization method.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Lie derivative as Koopman generator", "weight": 1.0} -->

In operator-theoretic terminology, $\mathcal{L}$ is called the infinitesimal generator of the family ${\{\mathcal{K}_{h}\}}_{h \geq 0}$, and since $\mathcal{K}$ is the Koopman operator, we thereby refer to $\mathcal{L}$ as the *Koopman generator*.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Feedback Linearization", "weight": 1.0} -->

Feedback linearization addresses the problem of designing a linearizing feedback controller in the model-based setting (given vector fields $f$ and $g$). An output function $h \in {C^{1}{({\mathbb{X}})}}$ of system is said to have *relative degree* $r$ if ${L_{g}L_{f}^{k}h{(x)}} = 0$ for $k = {\{ 0,\ldots,{r - 2}\}}$ and ${L_{g}L_{f}^{r - 1}h{(x)}} \neq 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Feedback Linearization", "weight": 1.0} -->

yielding an $r$-dimensional linear system in the transformed state and control $(z,v)$ of the form,

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Feedback Linearization", "weight": 1.0} -->

The above transformation results in an $({n - r})$-dimensional residual dynamics, called *zero dynamics*, which is unobservable and uncontrollable, and the system is said to be *input-output feedback linearizable*. Therefore, this approach to linearization-based control relies crucially on the choice of the output function $h$ which results in a stable zero dynamics.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Feedback Linearization", "weight": 1.0} -->

If the relative degree $r = n$, the state space dimension, the system is said to be *full-state feedback linearizable*, which is the case if and only if it is both controllable^22^2The system is said to be *controllable* when the distribution ${\Delta{(x)}} = {{span}\left\{ {g{(x)}},{{ad}_{f}g{(x)}},\ldots,{{ad}_{f}^{k - 1}g{(x)}},\ldots \right\}}$ is such that ${\dim\left( {\Delta{(x)}} \right)} = n$, for all $x \in {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Feedback Linearization", "weight": 1.0} -->

Furthermore, by the Frobenius theorem, a distribution of linearly independent vector fields ${f_{1}{(x)}},{f_{2}{(x)}},\ldots,{f_{m}{(x)}}$ is completely integrable if and only if it is involutive^44^4The distribution $\Delta = {{span}{\{ f_{1},f_{2},\ldots,f_{m}\}}}$ is said to be *involutive* \[27, Definition 6.5\] if and only if ${{ad}_{f_{i}}f_{j}} \in \Delta$ for any ${i,j} \in {\{ 1,\ldots,m\}}$..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1 (*Input-Output Feedback Linearizable System*)", "weight": 1.0} -->

Consider a system with the following vector fields,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1 (*Input-Output Feedback Linearizable System*)", "weight": 1.0} -->

It can be noticed that $\Delta$ has a rank equal to 2 for all $x$. Further, ${{ad}_{f}^{k}g} = 0$ for all $k \geq 2$. Thus $\{ g,{{ad}_{f}g},{{ad}_{f}^{k}g}\}$ has rank 2 for all $k$ and $x$, and $\Delta$ is involutive. However, note that the system is not controllable. Therefore, the system is not full-state feedback linearizable and only input-output feedback linearizable.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data-driven feedback linearization", "weight": 1.0} -->

In this section, we propose a data-driven technique, called Koopman generator-based Feedback Linearization (KGFL), to perform data-driven feedback linearization to stabilize System. We first establish that there exists an observable and feedback control that render the closed-loop Koopman generator finite-dimensional. We then seek to find this transformation using experimental data.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Koopman generator-based feedback linearization", "weight": 1.0} -->

We now establish the connection between feedback linearization and the closed-loop Koopman generator $L_{f + {g\alpha}}$, which will serve as the basis for the numerical algorithm to determine the linearizing state/control transformation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1 (*Multiple Inputs*)", "weight": 1.0} -->

When there are multiple inputs, the observable $h$ has a relative $r_{i}$ for each input $i$. If there are $m$ inputs, the feedback linearizing inputs will now be $\alpha \in {\mathbb{R}}^{m}$ and $\beta \in {\mathbb{R}}^{m \times m}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1 (*Multiple Inputs*)", "weight": 1.0} -->

Here, $r_{i}$ is the relative degree of the observable $h$ with respect to the $i$-th input such that ${r_{1} + r_{2} + \cdots + r_{m}} = n$. This also means that there exists a Koopman-invariant subspace with respect to every input, and also all the inputs considered simultaneously.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

We use a dictionary of functions to identify the Koopman generator to lift full-state data from the nonlinear control-affine system and seek to find a linear relation in the evolution of the lifted system. Furthermore, since we already know the form of the Koopman generator, particularly the matrices $A$ and $B$ as defined in Equation which define the action of the closed-loop Koopman generator, we seek to best approximate this structure. To this end, we first recall the state and control transformations, i.e., $z = {H{(x)}}$ and $u = {{\alpha{(x)}} + {\beta{(x)}v}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

We note that the state transformation $H$ is determined by the observable $h$ for which we seek an estimate $\hat{h}$, expressed using a dictionary $\phi$ (consisting $M$ real functions, i.e., $\phi = \left\lbrack {\phi_{1}\phi_{2}\ldots\phi_{M}} \right\rbrack^{\top}$, where $\phi_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$) as ${\hat{h}{(x)}} = {K^{\top}\phi{(x)}}$, where $K \in {\mathbb{R}}^{M}$. We then invert the control transformation to express the external control $v$ in terms of $u$ as

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

where $\zeta$, $\eta$ are given by

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

where ${G,J} \in {\mathbb{R}}^{k}$ are to be estimated from data. The dictionary of repeated time derivatives of the observable dictionary $\phi$ is represented by D as

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

Here $D{(x)}$ utilizes the structure of $H{(x)}$ as the state transformation $H{(x)}$ contains the observable $h$ and its repeated derivatives. Utilization of this structure for the dictionary is also a novelty of our algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

We know from feedback linearization that the state and control transformation yield the linear system. Here we emphasize the fact that we do not assume that the system is feedback linearizable or the dictionaries contain all the necessary functions for the required transformations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

Problem seeks to obtain the vectors $K,G$ and $J$ simultaneously. It is evident that $K = 0$, $G = 0$ and an arbitrary non-zero $J$ minimizes the cost. Therefore, simple constraints to make $K \neq 0$ and $G \neq 0$ can be imposed. We note that Problem involves a finite difference approximation with sampling interval $\tau$ of the time derivative of $D$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

In the preceding analysis, we had assumed that the system state is directly observable. However, when we only have access to an output $y = {h{(x)}}$, through an observable $h$, whereby the data consists of inputs and outputs in the following matrices

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

the problem becomes one of input-output feedback linearization. The problem of data-driven input-output feedback linearization is to find the necessary transformations $H,$ $\zeta$ and $\eta$ using only input-output data $Y,U$. However, the sub-problem of finding the state transformation $H{(x)}$ in the input-output feedback linearization problem is simpler as $H{(x)}$ is computed directly from data, as $y_{t}$ and its repeated time derivatives, since the observable $h$ is apriori fixed,

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Data-driven algorithm", "weight": 1.0} -->

We now present two methods to obtain the solutions to problems and.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B1 Iterative Algorithm - KGFL", "weight": 1.0} -->

The KGFL algorithm is an iterative algorithm based on gradient descent. The gradients of the cost in Problem with respect to the parameters $K$, $G$ and $J$ can be explicitly computed. These gradients are utilized in an iterative manner to obtain the estimates $\hat{z}$, $\hat{\zeta}$ and $\hat{\eta}$. Algorithm 1 outlines the Koopman Generator-based Feedback Linearization (KGFL) algorithm. The parameters $K$, $G$ and $J$ at iteration $i$ are denoted by $K{(i)}$, $G{(i)}$ and $J{(i)}$ respectively. In the algorithm, the state transformation parameter $K$ is computed while keeping the control transformation parameters $G$ and $J$ fixed from the previous iterations. Subsequently, the control transformation parameters $G$ and $J$ are fixed while keeping the state transformation parameters fixed. In the algorithm, we denote the cost function in Problem as $C$ and its gradient with a parameter $Q$ as $\nabla_{Q}$ C.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B1 Iterative Algorithm - KGFL", "weight": 1.0} -->

We emphasize that the dictionaries $D$, $\theta$ and $\gamma$ may not contain all the nonlinearities of the system's dynamics. Hence, we solve the data-driven feedback linearization problem in a least-squares sense.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B1 Iterative Algorithm - KGFL", "weight": 1.0} -->

1 Data: X and U from System
2 Initialize: Dictionaries ϕ, θ, γ; Number of iterations E; Initial guess for K, G and J; Learning rate ϵ
Algorithm 1 Koopman generator-based Feedback Linearization (KGFL)

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B1 Iterative Algorithm - KGFL", "weight": 1.0} -->

For input-output feedback linearization, step 4 in KGFL need not be performed as the state transformation is fixed apriori.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B2 Single-step method", "weight": 1.0} -->

The solutions to Problems and can also be computed in a single step.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

In this section, we demonstrate the effectiveness of the proposed data-driven feedback linearization technique KGFL. We run the numerical experiments on an i9-9900K CPU with 128GB of RAM. We sample $u_{i}$ from $\mathcal{N}{}$ to collect data, and the state is sampled every $0.01$ seconds. We choose the control task of stabilization. The exogenous input to the linearized system $v$ is chosen to be $v_{t} = {\left\lbrack {{- 2} - 2} \right\rbrack^{\top}z_{t}}$ for full state feedback linearization. This places the poles of system at ${- 1} \pm {1i}$. For input-output feedback linearization with relative degree 1, we choose $v_{t} = {- {2z_{t}}}$. Since the system is controllable, we can arbitrarily place the poles of the system using state feedback.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Hermite polynomials serve as a useful choice for dictionaries as they form an orthogonal basis of the Hilbert space of functions.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Numerical testbeds", "weight": 1.0} -->

We consider two testbed systems for our numerical experiments, to demonstrate the proposed data-driven feedback linearization algorithm. The first testbed system we consider is the classical Van der Pol oscillator but with the input entering the system nonlinearly as

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Numerical testbeds", "weight": 1.0} -->

We demonstrate both full-state feedback linearization and input-output feedback linearization for the Van der Pol oscillator. The second testbed system we consider is an arbitrary feedback linearizable system of 6 dimensions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Numerical testbeds", "weight": 1.0} -->

where the coefficients $a_{i}$, with $i \in {\{ 1,2,\ldots,10\}}$, are sampled from a standard Gaussian $\mathcal{N}{}$. We demonstrate full-state feedback linearization with stabilization at the origin. For System, we choose a dictionary similar to that chosen for the Van der Pol oscillator in Section IV-A. Further, we augment the dictionary with ${\sin{(x_{1})}},{\sin{(x_{2})}}$ and $\sin{(x_{3})}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A1 Full state feedback linearization", "weight": 1.0} -->

The Van der Pol oscillator is full-state feedback linearizable as the system is both controllable and integrable. Particularly, choosing ${h{(x)}} = x_{1}$, ${\alpha{(x)}} = {x_{1} - {0.5{({1 - x_{1}^{2}})}x_{2}}}$, and ${\beta{(x)}} = {({1 - x_{2}^{2}})}^{- 1}$ fully linearizes the system in its normal form. In Figure 1, the dashed lines represent model-based feedback linearization whereas the solid lines represent the learned linearization transformation using the proposed algorithm. In the figure, $x^{m}$ represents the model-based states. In Figure 1(a), we choose a dictionary of Hermite polynomials of order 2 and their mutual Kronecker products. We use KGFL to perform full-state feedback linearization.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A1 Full state feedback linearization", "weight": 1.0} -->

It is clear from the figure that the data-driven algorithm is able to learn a transformation and stabilize the system almost as well as the model-based linearization. We also compare our proposed algorithm against the algorithms in and in Figure 1(b). In, a linear predictor of the nonlinear system is constructed without any control transformations. Hence it cannot achieve exact linearization of the nonlinear system, especially when the control affects the system nonlinearly. The data-driven algorithm proposed in is motivated by an intelligent PID controller that makes use of sampled measurements in an online fashion. The algorithm proposed in bilinearizes the system using offline data and performs model predictive control. To maintain fairness in comparison, we used the same initial conditions and the same offline data for the proposed algorithm and. It is evident from simulations that the proposed algorithm stabilizes faster than the compared algorithms. The online algorithm in uses past measurements to compute piece-wise constant inputs, whereas the algorithm in performs MPC by bilinearizing the system by performing state transformations. Our proposed algorithm linearizes the system using both state and control transformations and applies a state-feedback approach for pole placement which makes our algorithm effective.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A1 Full state feedback linearization", "weight": 1.0} -->

Furthermore, Figure 1(c) shows that the data-driven feedback linearization algorithm performs well even for the high dimensional system with inputs entering nonlinearly.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A2 Output feedback linearization", "weight": 1.0} -->

We now demonstrate data-driven input-output feedback linearization on the Van der Pol oscillator using the single-step method described in Theorem III.2. ‣ III-B2 Single-step method ‣ III-B Data-driven algorithm ‣ III Data-driven feedback linearization ‣ Data-Driven Feedback Linearization using the Koopman Generator"). We choose the output $y = {h{(x)}} = {0.5x_{1}^{2}}$. We make the observation that the system has a relative degree $r = 2$ for the selected output. For the data-driven setting, we choose a dictionaries that contains the Hermite polynomials of the output and its derivatives up to the third degree. We learn the control transformation in problem. In Figure 3(b), it is observed that the proposed data-driven algorithm stabilizes the output at 0. Further, the feedback linearization of the selected output induces no zero dynamics, hence the overall system is also stable, as it can be observed in figure 3(a).

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Effect of richness of dictionary", "weight": 1.0} -->

Here, we investigate the effect of the richness of the dictionary on input-output feedback linearization for the single-step method. We choose the modified Van der Pol oscillator introduced in equation and the output function ${h{(x)}} = x_{1}$. Hence the state transformation becomes $z = \left\lbrack {x_{1}x_{2}} \right\rbrack^{\top}$, and we only learn the control transformations $\hat{\alpha}$ and $\hat{\beta}$. Note that we only use input-output data as described in section III-B. We compare the difference in trajectories between that of model-based feedback linearization and the proposed data-driven algorithm. We look at the loss $Q_{T}$ defined as the sum of the norm difference between the states at every time instance over a horizon $T$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Effect of richness of dictionary", "weight": 1.0} -->

That is, $Q_{T} = {\sum\limits_{t}^{T}{\|{x_{t}^{m} - x_{t}}\|}_{2}^{2}}$. We choose $T = 10$ and use a data set of size $N = 300$. We compare the loss in Figure 2(a) over 40 separate experiments for each size of the dictionary. Figure 2 is a boxplot where the average is denoted by the red line and the $75^{th}$ and $25^{th}$ quartiles are represented by upper and lower edges of the blue box respectively. The red stars represent the outliers. We vary the richness of the dictionary by varying the order of the Hermite polynomials included for learning the control transformation. We see from Figure 2(a) that, as the model complexity increases, the quantity $Q_{T}$ initially decreases but starts to increase again after reaching a minimum. This can be attributed to overfitting.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Effect of dataset size", "weight": 1.0} -->

We study the effect of the size of the dataset on the loss $Q_{T}$ when the size of the dictionary is fixed. Similar to the previous numerical comparisons, we perform output feedback linearization with $y = {h{(x)}} = x_{1}$. The dictionaries for control transformations contain Hermite polynomials up to the second degree. From Figure 2(b) we can see that as the data size increases, the average loss uniformly decreases until 800 data points.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-D Effect of sampling interval", "weight": 1.0} -->

We analyze the effect of sampling interval of the data on the performance of KGFL. For the Van der Pol oscillator considered, we sample the system at rates 0.1, 0.01, and 0.001 respectively. The results of the performance of these numerical experiments are presented in Figure 2(c). It can be seen that the sampling rate does not have a significant effect on the performance of the algorithm. A fast sampling rate of 0.001 seems to perform only marginally better than sampling rates of 0.01 and 0.1. A complete analysis of the sampling rate is beyond the scope of the paper as it is dependent on the nature of the vector fields that describe the system. Typically, systems that evolve fast in the state space require faster sampling rates.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We establish a connection between the traditional model-based feedback linearization technique and the Koopman generator. Particularly, we show that here exists an observable and a state feedback control that renders the Koopman-generator finite-dimensional and nilpotent when the system is feedback linearizable. Using this connection, we develop an algorithm called KGFL to feedback linearize a control-affine system using experimental data. We demonstrate the algorithm numerically on complex dynamical systems and discuss tradeoffs related to the size of the dictionaries and the size of the dataset. We also show that it performs better than existing algorithms in the literature as KGFL exploits the feedback linearizable structure of the system. Directions of future research include the problem of choosing the right observables to obtain stable zero dynamics.
