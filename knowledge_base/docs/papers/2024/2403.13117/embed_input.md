<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Flow Matching: Learning Straight Trajectories in Just One Step

Topics include Learning, Optimal transport, Matching, FM.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Over the several recent years, there has been a boom in development of Flow Matching (FM) methods for generative modeling. One intriguing property pursued by the community is the ability to learn flows with straight trajectories which realize the Optimal Transport (OT) displacements. Straightness is crucial for the fast integration (inference) of the learned flow's paths. Unfortunately, most existing flow straightening methods are based on non-trivial iterative FM procedures which accumulate the error during training or exploit heuristics based on minibatch OT. To address these issues, we develop and theoretically justify the novel \textbf{Optimal Flow Matching} (OFM) approach which allows recovering the straight OT displacement for the quadratic transport in just one FM step. The main idea of our approach is the employment of vector field for FM which are parameterized by convex functions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent success in generative modeling Liu et al.; Esser et al.; Cao et al. is mostly driven by Flow Matching (FM) Lipman et al. models. These models move a known distribution to a target one via ordinary differential equations (ODE) describing the mass movement. However, such processes usually have curved trajectories, resulting in time-consuming ODE integration for sampling. To overcome this issue, researches developed several improvements of the FM Liu; Liu et al.; Pooladian et al., which aim to recover more straight paths.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rectified Flow (RF) method Liu; Liu et al. iteratively solves FM and gradually rectifies trajectories. Unfortunately, in each FM iteration, it accumulates the error, see and. This may spoil the performance of the method. The other popular branch of approaches to straighten trajectories is based on the connection between straight paths and Optimal Transport (OT) Villani. The main goal of OT is to find the way to move one probability distribution to another with the minimal effort. Such OT maps are usually described by ODEs with straight trajectories. In OT Conditional Flow Matching (OT-CFM) Pooladian et al.; Tong et al., the authors propose to apply FM on top of OT solution between batches from considered distributions. Unfortunately, such a heuristic does not guarantee straight paths because of minibatch OT biases, see, e.g., for the practical illustration.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. In this paper, we fix the above-mentioned problems of the straightening methods. We propose a novel Optimal Flow Matching (OFM) approach ($§$3 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) that after a single FM iteration obtains straight trajectories which can be simulated without ODE solving. It recovers OT flow for the quadratic transport cost function, i.e., it solves the Benamou--Brenier problem (Figure 1). We demonstrate the potential of OFM in the series of experiments and benchmarks ($§$4).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main idea of our OFM is to consider during FM only specific vector fields which yield straight paths by design. These vector fields are the gradients of convex functions, which in practice are parametrized by Input Convex Neural Networks Amos et al.. In OFM, one can optionally use minibatch OT or any other transport plan as the input, and this is completely theoretically justified.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Static Optimal Transport", "weight": 1.0} -->

Monge's and Kantorovich's formulations. Consider two distributions ${p_{0},p_{1}} \in {\mathcal{P}_{2,{ac}}{({\mathbb{R}}^{D})}}$ and a cost function $c:{{{\mathbb{R}}^{D} \times {\mathbb{R}}^{D}}\rightarrow{\mathbb{R}}}$. Monge's Optimal Transport formulation is given by where the infimum is taken over measurable functions $T:{{\mathbb{R}}^{D}\rightarrow{\mathbb{R}}^{D}}$ which satisfy the mass-preserving constraint ${T\# p_{0}} = p_{1}$. Such functions are called transport maps. If there exists a transport map $T^{\ast}$ that achieves the infimum, then it is called the optimal transport map.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Static Optimal Transport", "weight": 1.0} -->

Since the optimal transport map $T^{\ast}$ in Monge's formulation may not exist, there is Kantorovich's relaxation for problem which addresses this issue. Consider the set of transport plans $\Pi{(p_{0},p_{1})}$, i.e., the set of joint distributions on ${\mathbb{R}}^{D} \times {\mathbb{R}}^{D}$ which marginals are equal to $p_{0}$ and $p_{1}$, respectively. Kantorovich's Optimal Transport formulation is With mild assumptions on $p_{0},p_{1}$, the infimum is always achieved (possibly not uniquely). An optimal plan $\pi^{\ast} \in {\Pi{(p_{0},p_{1})}}$ is called an optimal transport plan.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Static Optimal Transport", "weight": 1.0} -->

Quadratic cost function. In our paper, we mostly consider the quadratic cost function ${c{(x_{0},x_{1})}} = \frac{{\|{x_{0} - x_{1}}\|}^{2}}{2}$. In this case, infimums in both Monge's and Kantorovich's OT are always uniquely attained. They are related by $\pi^{\ast} = {{\lbrack\text{id},T^{\ast}\rbrack}\# p_{0}}$. Moreover, the optimal values of and are equal to each other. The square root of the optimal value is called the Wasserstein-2 distance ${\mathbb{W}}_{2}{(p_{0},p_{1})}$ between distributions $p_{0}$ and $p_{1}$, i.e., Dual formulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Static Optimal Transport", "weight": 1.0} -->

The term $\text{Const}{(p_{0},p_{1})}$ does not depend on $\Psi$. Therefore, the minimization over transport plans $\pi$ is equivalent to the minimization of $\mathcal{L}_{OT}{(\Psi)}$ from over convex functions $\Psi$. Moreover, the optimal transport map $T^{\ast}$ can be expressed via an optimal $\Psi^{\ast}$ (the Brenier potential Villani ), namely,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dynamic Optimal Transport", "weight": 1.0} -->

In Benamou and Brenier, the authors show that the calculation of Optimal Transport map in for the quadratic cost can be equivalently reformulated in a dynamic form. This form operates with a vector fields defining time-dependent mass transport instead of just static transport maps.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Dynamic Optimal Transport", "weight": 1.0} -->

Let ${{\phi^{u}{(t, \cdot)}} \equiv {\phi_{t}^{u}{(\cdot)}}}:{{{\lbrack 0,1\rbrack} \times {\mathbb{R}}^{D}}\rightarrow{\mathbb{R}}^{D}}$ denote the flow map, i.e., it is the function that maps the initial $z_{0}$ to its position at moment of time $t$ according to the ODE, i.e., If initial points $z_{0}$ of trajectories are distributed according to $p_{0}$, then defines a distribution $p_{t}$ of $z_{t}$ at time $t$, which can be expressed via with the push-forward operator, i.e., $p_{t}^{u}:={\phi_{t}^{u}\# p_{0}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dynamic Optimal Transport", "weight": 1.0} -->

Benamou--Brenier problem. Dynamic OT is the following minimization problem: In, we look for the vector fields $u$ that define the flows which start at $p_{0}$ and end at $p_{1}$. Among such flows, we seek for the one which has the minimal kinetic energy over the entire time interval.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Dynamic Optimal Transport", "weight": 1.0} -->

There is a connection between the static OT map $T^{\ast} = {\nabla\Psi^{\ast}}$ and the dynamic OT solution $u^{\ast}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Continuous Optimal Transport Solvers", "weight": 1.0} -->

There exist a variety of continuous OT solvers Genevay et al.; Seguy et al.; Taghvaei and Jalali; Makkuva et al.; Fan et al.; Daniels et al.; Vargas et al.; De Bortoli et al.; Korotin et al.; Rout et al.; Liu et al.; Korotin et al.; Choi et al.; Fan et al.; Uscidda and Cuturi; Amos; Tong et al.; Gushchin et al.; Mokrov et al.; Asadulaev et al.; Gazdieva et al.. For a survey of solvers designed for OT with quadratic cost, see Korotin et al.. In this paper, we focus only on the most relevant ones, called the ICNN-based solvers Taghvaei and Jalali; Korotin et al.; Makkuva et al.; Amos.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Continuous Optimal Transport Solvers", "weight": 1.0} -->

These solvers directly minimize objective $\mathcal{L}_{OT}$ from parametrizing a class of convex functions with convex in input neural networks called ICNNs Amos et al. (for more details, see "Parametrization of $\Psi$\" in $§$3.2 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")). Solvers details may differ, but the main idea remains the same. To calculate the conjugate function $\overline{\Psi}{(x_{1})}$ at the point $x_{1}$, they solve the convex optimization problem from conjugate definition. Envelope Theorem Afriat allows obtaining closed-form formula for the gradient of the loss.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Flow Matching Framework", "weight": 1.0} -->

In this section, we recall popular approaches Liu et al.; Liu; Pooladian et al. to find fields $u$ which transport a given probability distribution $p_{0}$ to a target $p_{1}$ and their relation to OT.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Flow Matching (FM)", "weight": 1.0} -->

To find such a field, one samples points $x_{0},x_{1}$ from a transport plan $\pi \in {\Pi{(p_{0},p_{1})}}$, e.g., the independent plan $p_{0} \times p_{1}$. The vector field $u$ is encouraged to follow the direction $x_{1} - x_{0}$ of the linear interpolation $x_{t} = {{{({1 - t})}x_{0}} + {tx_{1}}}$ at any moment $t \in {\lbrack 0,1\rbrack}$, i.e., one solves: Figure 2: Flow Matching (FM) obtains a vector field u moving p0 to p1. FM typically operates with the independent transport plan π = p0 × p1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Flow Matching (FM)", "weight": 1.0} -->

We denote the solution of (10 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) and the flow map by $u^{\pi}$ and $\phi^{\pi}$, respectively. The concept of FM is depicted in Figure 2 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step").

<!-- chunk {"id": "body-0020", "role": "body", "section": "Flow Matching (FM)", "weight": 1.0} -->

The intuition of this procedure is as follows: linear interpolation $x_{t} = {{{({1 - t})}x_{0}} + {tx_{1}}}$ is an intuitive way to move $p_{0}$ to $p_{1}$, but it requires knowing $x_{1}$. By fitting $u$ with the direction $x_{1} - x_{0}$, one yields the vector field that can construct this interpolation without any information about $x_{1}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Flow Matching (FM)", "weight": 1.0} -->

To push point $x_{0}$ according to learned $u$, one needs to integrate ODE via numerical solvers. The vector fields with straight (or nearly straight) paths incur much smaller time-discretization error and increase effectiveness of computations, which is in high demand for applications.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Flow Matching (FM)", "weight": 1.0} -->

Researchers noticed that some initial plans $\pi$ can result in more straight paths after FM rather than the standard independent plan $p_{0} \times p_{1}$. The two most popular approaches to choose better plans are Optimal Transport Conditional Flow Matching Pooladian et al.; Tong et al. and Rectified Flow Liu et al..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal Transport Conditional Flow Matching (OT-CFM)", "weight": 1.0} -->

If one uses the OT plan $\pi^{\ast}$ as the initial plan for FM, then it returns the Brenier's vector field $u^{\ast}$, which generates exactly straight trajectories. However, typically, the true OT plan $\pi^{\ast}$ is not available. In such a case, in order to achieve some level of straightness in the learned trajectories, a natural idea is to take the initial plan $\pi$ to be close to the optimal $\pi^{\ast}$. Inspired by this, the authors of OT-CFM Pooladian et al.; Tong et al. take the advantage of minibatch OT plan approximation. Firstly, they independently sample batches of points from $p_{0}$ and $p_{1}$. Secondly, they join the batches together according to the discrete OT plan between them. The resulting joined batch is then used in FM.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimal Transport Conditional Flow Matching (OT-CFM)", "weight": 1.0} -->

The concept of OT-CFM is depicted in Figure 3 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step").

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimal Transport Conditional Flow Matching (OT-CFM)", "weight": 1.0} -->

The main drawback of OT-CFM is that it recovers only biased dynamic OT solution. In order to converge to the true transport plan the batch size should be large, while with a growth of batch size computational time increases drastically. In practice, batch sizes that ensure approximation good enough for applications are nearly infeasible to work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Rectified Flow (RF)", "weight": 1.0} -->

In Liu et al., the authors propose an iterative approach to refine the plan $\pi$, straightening the trajectories more and more with each iteration. Formally, Flow Matching procedure denoted by FM takes the transport plan $\pi$ as input and returns an optimal flow map via solving (10 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")): One can iteratively apply FM to the initial transport plan (e.g., the independent plan), gradually rectifying it. Namely, Rectified Flow Algorithm on $K$-th iteration has the following update rule where $\phi^{K},\pi^{K}$ denote flow map and transport plan on $K$-th iteration, respectively.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Rectified Flow (RF)", "weight": 1.0} -->

With each new FM iteration, the generated trajectories ${\{{\{ z_{t}\}}_{t \in {\lbrack 0,1\rbrack}}\}}^{K}$ provably become more and more straight, i.e., error in approximation ${z_{t}^{K} \approx {{{({1 - t})}z_{0}^{K}} + {tz_{1}^{K}}}},{{\forall t} \in {\lbrack 0,1\rbrack}}$ decreases as the number of iterations $K$ grows. The concept of RF is depicted on Figure 4 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step").

<!-- chunk {"id": "body-0028", "role": "body", "section": "Rectified Flow (RF)", "weight": 1.0} -->

The authors also notice that for any convex cost function $c$ the flow map $\phi_{1}^{\pi}$ from Flow Matching yields lower or equal transport cost than initial transport plan $\pi$: Intuitively, the transport costs are guaranteed to decrease because the trajectories of FM as solutions of well-defined ODE do not intersect each other, even if the initial lines connecting $x_{0}$ and $x_{1}$ can. With each iteration of RF (12 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")), transport costs for all convex cost functions do not increase, but, for a given cost function, convergence to its own OT plan is not guaranteed. In Liu, the authors address this issue and, for any particular convex cost function $c$, modify Rectified Flow to converge to OT map for $c$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Rectified Flow (RF)", "weight": 1.0} -->

In this modification, called $c$-Rectified Flow ($c$-RF), the authors slightly change the FM training objective and restrict the optimization domain only to potential vector fields ${u_{t}{(\cdot)}} = {{\nabla\overline{c}}{({{\nabla f_{t}}{(\cdot)}})}}$, where ${f_{t}{(\cdot)}}:{{\mathbb{R}}^{D}\rightarrow{\mathbb{R}}}$ is an arbitrary time-dependent scalar valued function and $\overline{c}$ is the convex conjugate of the cost function $c$. In case of the quadratic cost function, the training objective remains the same, and the vector field $u_{t}$ is set as the simple gradient ${\nabla f_{t}}{(\cdot)}$ of the scalar valued function $f_{t}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rectified Flow (RF)", "weight": 1.0} -->

Unfortunately, in practice, with each iteration ($c$-)RF accumulates error caused by inexactness from previous iterations, the issue mentioned. Due to neural approximations, we can not get exact solution of FM (e.g., ${\phi_{1}^{K}\# p_{0}} \neq p_{1}$), and this inexactness only grows with iterations. In addition, training of ($c$-)RF becomes non-simulation free after the first iteration, since to calculate the plan $\pi^{K + 1} = {{\lbrack\text{id},\phi^{K + 1}\rbrack}\# p_{0}}$ it has to integrate ODE.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimal Flow Matching (OFM)", "weight": 1.0} -->

In this section, we provide the design of our novel Optimal Flow Matching algorithm (1 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) that fixes main problems of Rectified Flow and OT-CFM approaches described above. In theory, it obtains exactly straight trajectories and recovers the unbiased optimal transport map for the quadratic cost just in one FM iteration with any initial transport plan. Moreover, during inference, our OFM does not require solving ODE to transport points.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimal Flow Matching (OFM)", "weight": 1.0} -->

We discuss the theory behind our approach ($§$3.1 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")), its practical implementation aspects ($§$3.2 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) and the relation to prior works ($§$3.3 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")). All our proofs are located in Appendix A.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Theory: Deriving the Optimization Loss", "weight": 1.0} -->

We want to design a method of moving distribution $p_{0}$ to $p_{1}$ via exactly straight trajectories. Namely, we aim to obtain straight paths from the solution of the dynamic OT. Moreover, we want to limit ourselves to just one minimization iteration. Hence, we propose our novel Optimal Flow Matching (OFM) procedure satisfying the above-mentioned conditions. The main idea of our OFM is to minimize the Flow Matching loss (10 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) not over all possible vector fields $u$, but only over specific optimal ones, which yield straight paths by construction and include the desired dynamic OT field $u^{\ast}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Theory: Deriving the Optimization Loss", "weight": 1.0} -->

Optimal vector fields. We say that a vector field $u^{\Psi}$ is optimal if it generates linear trajectories $\{{\{ z_{t}\}}_{t \in {\lbrack 0,1\rbrack}}\}$ such that there exist a convex function $\Psi:{{\mathbb{R}}^{D}\rightarrow{\mathbb{R}}}$, which for any path ${\{ z_{t}\}}_{t \in {\lbrack 0,1\rbrack}}$ pushes the initial point $z_{0}$ to the final one as $z_{1} = {{\nabla\Psi}{(z_{0})}}$, i.e., The function $\Psi$ defines the ODE Equation (14 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) does not provide a closed formula for $u^{\Psi}$ as it depends on $z_{0}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Theory: Deriving the Optimization Loss", "weight": 1.0} -->

The explicit formula is constructed as follows: for a time $t \in {\lbrack 0,1\rbrack}$ and point $x_{t}$, we can find a trajectory ${\{ z_{t}\}}_{t \in {\lbrack 0,1\rbrack}}$ s.t.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Theory: Deriving the Optimization Loss", "weight": 1.0} -->

We highlight that the solution of dynamic OT lies in the class of optimal vector fields, since it generates linear trajectories with the Brenier potential $\Psi^{\ast}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Theory: Deriving the Optimization Loss", "weight": 1.0} -->

Training objective. Our Optimal Flow Matching (OFM) approach is as follows: we restrict the optimization domain of FM (10 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) with fixed plan $\pi$ only to the optimal vector fields. We put the formula for the vector field $u_{\Psi}$ into FM loss from (10 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")) and define our Optimal Flow Matching loss: Our Theorem 1. ‣ 3.1 Theory: Deriving the Optimization Loss ‣ 3 Optimal Flow Matching (OFM) ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step") states that OFM solves the dynamic OT via single FM minimization for any initial $\pi$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Practical implementation aspects", "weight": 1.0} -->

In this subsection, we explain the details of optimization of our Optimal Flow Matching loss (16 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Practical implementation aspects", "weight": 1.0} -->

Parametrization of $\Psi$. In practice, we parametrize the class of convex functions with Input Convex Neural Networks (ICNNs) Amos et al. $\Psi_{\theta}$ and parameters $\theta$. These are scalar-valued neural networks built in such a way that the network is convex in its input. They consist of fully-connected or convolution blocks, some weights of which are set to be non-negative in order to keep the convexity. In addition, activation functions are considered to be only non-decreasing and convex in each input coordinate. These networks are able to support most of the popular training techniques (e.g., gradient descent optimization, dropout, skip connection, etc.). In Appendix B, we discuss the used architectures.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Practical implementation aspects", "weight": 1.0} -->

OFM loss calculation. We provide an explicit formula for gradient of OFM loss (16 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Relation to Prior Works", "weight": 1.0} -->

In this subsection, we compare our Optimal Flow Matching and previous straightening approaches. One unique feature of OFM is that it works only with flows which have straight paths by design and does not require ODE integration to transport points. Other methods may result in non-straight paths during training, and they still have to solve ODE even with near-straight paths.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Relation to Prior Works", "weight": 1.0} -->

OT Solvers Taghvaei and Jalali; Makkuva et al.; Amos. According to Theorem 1. ‣ 3.1 Theory: Deriving the Optimization Loss ‣ 3 Optimal Flow Matching (OFM) ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step"), our OFM and dual OT solvers basically minimize the same OT loss. However, our OFM actively utilizes the temporal component of the dynamic process. It allows us to pave a novel theoretical bridge between OT and FM. Such a direct connection can lead to the adoption of the strengths of both methods and a deeper understanding of them.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Relation to Prior Works", "weight": 1.0} -->

OT-CFM Pooladian et al.; Tong et al.. Unlike our OFM approach, OT-CFM method retrieves biased OT solution, and the recovery of straight paths is not guaranteed. In OT-CFM, minibatch OT plan appears as a heuristic that helps to get better trajectories in practice. In contrast, usage of any initial transport plan $\pi$ in our OFM is completely justified in Theorem 1. ‣ 3.1 Theory: Deriving the Optimization Loss ‣ 3 Optimal Flow Matching (OFM) ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step").

<!-- chunk {"id": "body-0044", "role": "body", "section": "Relation to Prior Works", "weight": 1.0} -->

Rectified Flow Liu et al.; Liu. In Rectified Flows Liu et al., the authors iteratively apply Flow Matching to refine the obtained trajectories. However, in each iteration, RF accumulates error since one may not learn the exact flow due to neural approximations. In addition, RF does not guarantee convergence to the OT plan for the quadratic cost. The $c$-Rectified Flow Liu modification can converge to the OT plan for any cost function $c$, but still remains iterative. In addition, RF and $c$-RF both requires ODE simulation after the first iteration to continue training. In OFM, we work only with the quadratic cost function, but retrieve its OT solution in just one FM iteration without simulation of the trajectories.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Relation to Prior Works", "weight": 1.0} -->

Light and Optimal Schrödinger Bridge. In Gushchin et al., the authors observe the relation between Entropic Optimal Transport (EOT) Léonard; Chen et al. and Bridge Matching (BM) Shi et al. problems. These are stochastic analogs of OT and FM, respectively. In EOT and BM, instead of deterministic ODE and flows, one considers stochastic processes with non-zero stochasticity. The authors prove that, during BM, one can restrict considered processes only to the specific ones and retrieve the solution of EOT. Hypothetically, our OT/FM case is a limit of their EOT/BM case when the stochasticity tends to zero. Proofs in Gushchin et al. for EOT are based on sophisticated KL divergence properties. We do not know whether our results for OFM can be derived by taking the limit of their stochastic case. To derive the properties of our OFM, we use completely different proof techniques based on computing integrals over curves rather than KL-based techniques.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Relation to Prior Works", "weight": 1.0} -->

Besides, in practice, the authors of Gushchin et al. mostly focus on Gaussian mixture parametrization while our method allows using neural networks (ICNNs).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Theory: properties of OFM", "weight": 1.0} -->

In this subsection, we provide the OFM's theoretical properties, which give an intuition for understanding of its main working principles and behavior.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experimental Illustrations", "weight": 1.0} -->

In this section, we showcase the performance of our Optimal Flow Matching method on illustrative 2D scenario (§4.1) and Wasserstein-2 benchmark Korotin et al. (§4.2). Finally, we apply our approach for solving high-dimensional unpaired image-to-image translation in the latent space of pretrained ALAE autoencoder (§4.3). The PyTorch implementation of our method is publicly available at The technical details of our experiments (architectures, hyperparameters) are in the Appendix B.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Illustrative 2D Example", "weight": 1.0} -->

In this subsection, we illustrate the proof-of-concept of our OFM on 2D setup and demonstrate that OFM's solutions do not depend on the initial transport plan $\pi$. We run our Algorithm 1 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step") between a standard Gaussian $p_{0} = {\mathcal{N}{(0,I)}}$ and a Mixture of eight Gaussians $p_{1}$ depicted in the Figure 6(a). We consider different stochastic plans $\pi$: independent plan $p_{0} \times p_{1}$ (Figure 6(b)), minibatch and antiminibatch (Figures 6(c), 6(d)) discrete OT (quadratic cost) with batch size $B_{\text{mb}} = 64$. In the antiminibatch case, we compose the pairs of source and target points by solving discrete OT with minus quadratic cost $- {\|{x - y}\|}_{2}^{2}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Illustrative 2D Example", "weight": 1.0} -->

The fitted OFM maps and trajectories are presented in Figure 6. We empirically see that our OFM finds the same solution for all initial plans $\pi$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Illustrative 2D Example", "weight": 1.0} -->

For completeness, in Appendix B.2, we apply these plans to the original FM (10 ‣ 2.4 Flow Matching Framework ‣ 2 Background and Related Works ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")), and show that, in comparison with our OFM, the resulting paths obtained by FM considerably depend on the plan.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Illustrative 2D Example", "weight": 1.0} -->

(a) Input and target (b) Our fitted OFM; (c) Our fitted OFM; minibatch π.

<!-- chunk {"id": "body-0053", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

In this subsection, we quantitatively compare our OFM and other methods testing their ability to solve OT. We run our OFM, FM based methods and OT solvers on OT Benchmark Korotin et al.. The authors provide high-dimensional continuous distributions $p_{0},p_{1}$ for which the ground truth OT map $T^{\ast}$ for the quadratic cost is known by the construction. To assess the quality of retrieved transport maps, we use standard unexplained variance percentage $\mathcal{L}^{2}$-UVP${(T)}:={{{100 \cdot {\|{T - T^{\ast}}\|}_{\mathcal{L}^{2}{(p_{0})}}^{2}}/\text{Var}}{{(p_{1})}\%}}$ Korotin et al.. It directly computes the normalized squared error between OT map $T^{\ast}$ and learned map $T$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

Competitors. We evaluate Conditional Flow Matching (OT-CFM), Rectified Flow (RF), $c$-Rectified Flow ($c$-RF), the most relevant OT solver MMv-1 Taghvaei and Jalali and its amortized version from Amos. In Taghvaei and Jalali and Amos, the authors directly minimize the dual formulation loss $\mathcal{L}_{OT}$ by parametrizing $\Psi$ with ICNNs and calculating $\overline{\Psi}{(x_{1})}$ via solving a convex optimization subproblem. The latter is similar to our inversion (17 ‣ Optimal Flow Matching: Learning Straight Trajectories in Just One Step")). Additionally, in Amos, the authors use MLPs to parametrize $\Psi$, and we include these results as well. Following Korotin et al., we also provide results for a linear OT map (baseline) which translates means and variances of distributions to each other.

<!-- chunk {"id": "body-0055", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

For our OFM, we consider two initial plans: independent plan (Ind) and minibatch OT (MB), the batch size for the latter is $B_{\text{mb}} = 64$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

The overall results are presented in Table 1. More details are given in Appendix B.3.

<!-- chunk {"id": "body-0057", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

MMv1*Taghvaei and Jalali Amortization, ICNN** Amos Amortization, MLP** Amos OFM Ind (Ours) Table 1: ℒ2−UVP values of solvers fitted on high-dimensional benchmarks in dimensions D = 2, 4, 8, 16, 32, 64, 128, 256. The best metric over Flow Matching based methods is bolded. * Metrics are taken from Korotin et al.. ** Metrics are taken from Amos.

<!-- chunk {"id": "body-0058", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

Results. Among FM-based methods, our OFM with any plan demonstrates the best results. For all plans, OFM convergences to close final solutions and metrics. Minibatch plan provides a little bit better results, especially in high dimensions. In theory, the OFM results for any plan $\pi$ must be similar. However, in stochastic optimization, plans with large variance yield convergence to slightly worse solutions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

MLP-based OT solver usually beats our OFM, since MLPs do not have ICNNs' limitations in practice. However, usage of MLP is an empirical trick and is not completely justified. We also run OFM with MLP instead ICNN, and, unfortunately, the method fails to converge.

<!-- chunk {"id": "body-0060", "role": "body", "section": "High-dimensional OT Benchmarks", "weight": 1.0} -->

RF demonstrates worse performance than even linear baseline, but it is ok since it is not designed to solve ${\mathbb{W}}_{2}$ OT. In turn, $c$-RF works better, but rapidly deteriorates with increasing dimensions. OT-CFM demonstrates the best results among baseline FM-based methods, but still underperforms compared to our OFM solver in high dimensions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Unpaired Image-to-image Transfer", "weight": 1.0} -->

Another task that involves learning a translation between two distributions is unpaired image-to-image translation. We follow the setup of Korotin et al. where translation is computed in the $512$ dimensional latent space of the pre-trained ALAE autoencoder Pidhorskyi et al. on $1024 \times 1024$ FFHQ dataset. In particular, we split the train FFHQ sample (60K faces) into $children$ and $adults$ subsets and consider the corresponding ALAE latent codes as the source and target distributions $p_{0}$ and $p_{1}$. At the inference stage, we take a new (unseen) $adult$ face from a test FFHQ sample, extract its latent code, process with our learned model and then decode back to the image space. The qualitative translation results and FID metric Heusel et al. are presented in Figure 7 and Table 2, respectively.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Unpaired Image-to-image Transfer", "weight": 1.0} -->

The batch size for minibatch OT methods ($\lfloor$OFM, MB$\rceil$, $\lfloor$OT-CFM$\rceil$) is $B_{\text{mb}} = 128$. Our OFM converges to nearly the same solution for both independent and MB plans, and demonstrates qualitatively plausible translations. The most similar results to our method are demonstrated by $\lfloor$$c$-RF$\rceil$. Similar to OFM, this method (in the limit of RF steps) also recovers the quadratic OT mapping.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion", "weight": 1.5} -->

Potential impact. We believe that our novel theoretical results have a huge potential for improving modern flow matching-based methods and inspiring the community for further studies. We think this is of high importance especially taking into account that modern generative models start to extensively use flow matching methods Yan et al.; Liu et al.; Esser et al..

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion", "weight": 1.5} -->

Limitations and broader impact are discussed in Appendix C.
