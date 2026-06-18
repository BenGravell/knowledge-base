<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Assume/Guarantee Contracts for Dynamical Systems: Theory and Computational Tools

Topics include Linear programming, Autonomous driving, Vehicles, Safety, Control, Contract theory, Dynamical systems theory, Formal verification.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modern engineering systems include many components of different types and functions. Verifying that these systems satisfy given specifications can be an arduous task, as most formal verification methods are limited to systems of moderate size. Recently, contract theory has been proposed as a modular framework for defining specifications. In this paper, we present a contract theory for discrete-time dynamical control systems relying on assume/guarantee contracts, which prescribe assumptions on the input of the system and guarantees on the output. We then focus on contracts defined by linear constraints, and develop efficient computational tools for verification of satisfaction and refinement based on linear programming. We exemplify these tools in a simulation example, proving a certain safety specification for a two-vehicle autonomous driving setting.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Engineering systems are often comprised of many components having different types and functions, including sensing, control, and actuation. Moreover, systems are subject to many specifications, such as safety and performance. Safety specifications can be captured using the notions of set-invariance (Blanchini and Miani ), while performance specifications are usually defined using a bound on the gain of the system, or using passivity, both can be captured using the framework of dissipativity (Van der Schaft ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, modern systems such as intelligent transportation systems, complex robotics and smart manufacturing systems have more complex specifications which cannot be captured by the safety and dissipativity frameworks, e.g. behaviour, tracking, and temporal logic specifications. Formal methods in control have been developed to address this issue (Belta et al.; Tabuada; Wongpiromsarn et al. ). This framework can be used to express temporal logic specifications (Tabuada and Pappas ). Unfortunately, even if we care only about safety, the sheer size of modern engineering systems implies that formal verification methods are ineffective, as the need to discretize the state-space results in a curse of dimensionality. Such verification processes can also be extremely wasteful, as even a minuscule change to the dynamical system (e.g., a small change in one of its components) requires starting the verification processes from scratch.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we present a verification approach relying on contract theory. Contract theory was first developed in the field of software engineering as a modular approach to system design (Meyer ), and it has proved useful for design of cyber-physical methods, both in theory and in practice (Nuzzo et al.; Naik and Nuzzo; Phan-Minh et al. ). Contracts prescribe assumptions on the environments a software component can act, and guarantees on its behaviour in those environments (Benveniste et al. ). The two main approaches for contract theory in computer science include assume/guarantee contracts, which put assumptions on the input to a software component and prescribe guarantees on its output, and interface theories, which provide specifications on the interaction of a component with its environment. In both cases, computational tools for verifying that a given component satisfies a given contract are needed in order to apply the theory.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, some attempts were made to define a contract theory for dynamical (control) systems. An assume/guarantee framework for continuous-time dynamical systems based on the notion of simulation was considered in Besselink et al., in which an algorithm for verifying that a system satisfies a given contract was provided using geometric control theory methods (Van der Schaft ). Assume/guarantee contracts have also been considered in Saoud et al., in which assumptions are made on the input signals and guarantees are on the state and output signals.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a framework for assume/guarantee contracts prescribing assumptions on the inputs and guarantees on the output, extending the framework of Saoud et al.. First, we allow the requirement on the output to depend on the input, which is natural for sensor systems and tasks like tracking. Second, we do not limit the internal structure of the component, for instance, we do not specify its state. This means that the analysis of a composite system can be conducted at a preliminary design stage, before we even know whether, for example, a sensor is a first- or a second-order system, or before we know the controller will be static or not. We also define satisfaction, refinement, and cascaded composition for contracts. We then focus on contracts in which the assumptions and guarantees are prescribed using linear inequalities, and present efficient computational tools for verifying satisfaction and refinement, which are based on linear programming (LP). This is the main contribution of this paper.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. Section 2 presents assume/guarantee contracts as well as the notions of satisfaction, refinement, and cascaded composition, and gives examples. Section 3 develops computational methods for verification of satisfaction and refinement. Section 4 provides a simulation example.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assume/Guarantee Contracts", "weight": 1.0} -->

In this section, we define the class of systems for which we introduce an abstract framework of assume/guarantee contracts, as well as supporting notions such as satisfaction, refinement, and cascaded composition. This is an adaptation of the framework presented in Benveniste et al.. In section 3, we will specialize to a class of contracts for which efficient computational tools can be introduced.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Definition 1 can be generalized by allowing $\mathcal{X}_{0}$ to be dependent of $d{}$. This is reasonable for systems trying to track $d{( \cdot )}$, assuming their initial tracking error is not too large. This is also reasonable for systems trying to avoid an obstacle whose position is defined by $d{( \cdot )}$, assuming the system does not start on top of the obstacle.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We wish to consider specifications on the behaviour of dynamical systems. A dynamical system can be thought of as a map from input signals ${d{( \cdot )}} \in \mathcal{S}^{n_{d}}$ to output signals ${y{( \cdot )}} \in \mathcal{S}^{n_{y}}$, as in Fig. 1. As such, we can adopt the formulation of assume/guarantee contracts by merely making assumptions on the input variable $d{( \cdot )}$ and demanding guarantees on the output variable $y{( \cdot )}$ given the input $d{( \cdot )}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 2", "weight": 1.0} -->

Let us now define the notion of satisfaction. This notion connects systems and assume/guarantee contracts, by defining when a given system satisfies the specifications defined by a given contract.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Refinement and Composition", "weight": 1.0} -->

One of the greatest perks of contract theory is its modularity, as one can refine a contract on a composite system by "smaller" contracts on subsystems, which can be further refined by even "smaller" contracts on individual components. The two notions supporting this idea are refinement, defining when one contract is stricter than another, and composition, defining the coupling of multiple contracts. In this subsection, we define the notion of refinement for assume/guarantee contracts, as well as a restricted notion of contract composition for cascade systems. Computational tools for these notions will be provided in the next section.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 4", "weight": 1.0} -->

Consider two contracts used for tracking. The first, $\mathcal{C} = {(\mathcal{D},\Omega)}$ defines asymptotic tracking of certain inputs, namely ${d,y} \in \mathcal{S}^{m}$, $\mathcal{D} \subseteq \mathcal{S}^{m}$, and

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 4", "weight": 1.0} -->

The second, $\mathcal{C}^{\prime} = {(\mathcal{D},\Omega^{\prime})}$, defines exponential convergence, i.e.,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 4", "weight": 1.0} -->

By definition, we have $\mathcal{C}^{\prime} \preccurlyeq \mathcal{C}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Computational Tools for Verification", "weight": 1.0} -->

The previous section presented abstract assume/guarantee contracts for discrete-time dynamical systems, as well the notions of satisfaction, refinement and cascaded composition. In this section, we present computational tools for verifying satisfaction and refinement, relying on mathematical induction and linear programming. We rely on linearity of both the systems and specifications. More precisely, we present computational tools for assumptions of the form ${{A^{1}d{({k + 1})}} + {A^{0}d{(k)}}} \leq a^{0}$ for all $k$, and guarantees of the form ${{G^{1}\begin{bmatrix}
\end{bmatrix}} + {G^{0}\begin{bmatrix}
\end{bmatrix}}} \leq g^{0}$ for all $k$, where $A^{0},A^{1},G^{0},G^{1}$ are matrices and $a^{0},g^{0}$ are vectors of appropriate dimensions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Computational Tools for Verification", "weight": 1.0} -->

Specifications of this form include general bounded signals, as well as outputs of dynamical systems (e.g., the input $d$ is the output of a given first-order system). In Section 4, we use specifications of this form to model a contract where the input is assumed to be a (constrained) trajectory of a dynamical system, and the guarantee is a linear inequality defining safe behaviour.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Verifying Satisfaction", "weight": 1.0} -->

Consider a contract $\mathcal{C} = {(\mathcal{D},\Omega)}$ where

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

Theorem 5 shows that $\theta_{{\ell + 1},\ell} = \infty$ if $\ell \leq {\nu - 2}$. Thus, we will use the third part of Theorem 5 for $\ell = {\nu - 1}$ to verify implementation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

This reformulation of is more computationally efficient, as it removes a large number of constraints and variables.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

To conclude this section, we showed one can verify a system $\Sigma$ satisfies a contract $\mathcal{C}$ by solving $\nu + 1$ LP problems, where $\nu$ is the observability index of the system. The first $\nu$ problems assert that $\theta_{n,n} \leq 0$ for $n = {0,\ldots,{\nu - 1}}$, and the last asserts that $\theta_{{\nu + 1},\nu} \leq 0$. The first $\nu$ problems deal with the initial conditions of the system, and the last problem deals with the long-term behaviour of the system. This method can be understood as a version of the k-induction method for model checking (Donaldson et al. ).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Verifying Refinement", "weight": 1.0} -->

In this section, we prescribe computational tools for verifying refinement between contracts defined by linear inequalities. These tools are similar to the ones presented in the work of Sankaranarayanan et al..

<!-- chunk {"id": "body-0024", "role": "body", "section": "Simulation Example", "weight": 1.0} -->

We exemplify the computational tools prescribed in Section 3 using case studies.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

Consider two vehicles driving along a single-lane highway, as in Fig. 3. We are given a headway $h > 0$, and our goal is to verify that the follower keeps at least the given headway from the leader. Denoting the position and velocity of the follower as $p_{1}{(k)}$, $v_{1}{(k)}$, and the position and velocity of the leader as ${p_{2}{(k)}},{v_{2}{(k)}}$, we want to show that ${{p_{2}{(k)}} - {p_{1}{(k)}} - {hv_{1}{(k)}}} \geq 0$ holds at any time $k \in {\mathbb{N}}$. We address this problem using assume/guarantee contracts.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

The input signal to the follower $d{( \cdot )}$ is ${d{(k)}} = {\lbrack{p_{2}{(k)}},{v_{2}{(k)}}\rbrack}$. It is reasonable to assume the leader vehicle follows the kinematic laws, i.e.,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

where $a_{2}{(k)}$ is the acceleration to the leading vehicle and ${\Deltat} > 0$ is the length of a discrete time step. As for guarantees, we want to assure that ${{p_{2}{(k)}} - {p_{1}{(k)}} - {hv_{1}{(k)}}} \geq 0$ holds for any $k \in {\mathbb{N}}$. It is clear that these assumptions and guarantees are given by linear inequalities, meaning that the methods of Section 3 can be applied.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

We must also specify the system.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

We want to prove that $\Sigma \vDash \mathcal{C}$, and we do so using Theorem 5. The system $\Sigma$ is observable, and its observability index is $\nu = 1$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

In the problem defining $\theta_{2,1}$, the parameters with "$+$" correspond to time $k = 2$, and the ones without "$+$" correspond to time $k = 1$. We choose parameters $a_{\min} = a_{\max} = {{9.8m}/s^{2}}$, ${\Deltat} = {0.1\sec}$, $h = {2sec}$, and solve both LP problems using Yalmip (Löfberg ), computing ${\theta_{0,0} = 0},{\theta_{2,1} = {- 0.2}}$, meaning that $\Sigma \vDash \mathcal{C}$ as ${\theta_{0,0},\theta_{2,1}} \leq 0$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Contract Satisfaction", "weight": 1.0} -->

We exemplify that $\Sigma \vDash \mathcal{C}$ through simulation. We consider the following trajectory of the leader - its initial speed is about ${110km}/h$, which is roughly kept for 10 seconds. It then starts to sway wildly for 10 seconds between ${80km}/h$ and ${110km}/h$, braking and accelerating as hard as possible. Finally, it stops swaying and keeps its velocity for 10 more seconds. The velocity and acceleration of the leader can be seen in Fig. 4. The follower starts $45m$ behind the leader, so the headway is kept at time $0$. We run the simulation for both vehicles, and plot the headway $\frac{{p_{2}{(k)}} - {p_{1}{(k)}}}{v_{1}{(k)}}$ and the velocity of the follower in Fig. 5. It can be seen that the headway is kept throughout the run, so the guarantees are satisfied, as predicted by our analysis.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Contract Refinement", "weight": 1.0} -->

As in the previous case study, consider the two-vehicle scenario described in Fig. 3. As before, we consider contracts about the behaviour of the follower vehicle, where the input $d = {\lbrack p_{2},v_{2}\rbrack}$ consists of the position and velocity of the leader vehicle, and the output $y = {\lbrack p_{1},v_{1}\rbrack}$ consists of the position and velocity of the follower vehicle.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Contract Refinement", "weight": 1.0} -->

We now prescribe two contracts $\mathcal{C}_{1},\mathcal{C}_{2}$ on the follower, where $\mathcal{C}_{1} = {(\mathcal{D}_{1},\Omega_{1})}$ and $\mathcal{C}_{2} = {(\mathcal{D}_{2},\Omega_{2})}$. In both, we assume that the leader vehicle satisfies the kinematic relations, with varying bounds on its acceleration, and guarantee that headway is kept.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Contract Refinement", "weight": 1.0} -->

where the parameters $a_{\min,j},a_{\max,j}$ determine the assumed maximum acceleration and deceleration. We also assume that the vehicle is moving forward in both cases, i.e. that ${v_{2}{(k)}} \geq 0$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Contract Refinement", "weight": 1.0} -->

where the parameters $h_{1},h_{2}$ determine the desired headway between the vehicles.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Contract Refinement", "weight": 1.0} -->

It is clear that if $a_{\min,2} \leq a_{\min,1}$ and $a_{\max,2},a_{\max,1}$, then the contract $\mathcal{C}_{1}$ assumes less than the contract $\mathcal{C}_{2}$, as its assumptions allow the leading vehicle the accelerate and decelerate more sharply. Moreover, if $h_{1} \geq h_{2}$, then $\mathcal{C}_{1}$ guarantees more than $\mathcal{C}_{2}$, as the associated headway is larger. Thus, for this parameter setting, we have that $\mathcal{C}_{1} \preccurlyeq \mathcal{C}_{2}$. We wish to verify this refinement using the tools of Section 3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Contract Refinement", "weight": 1.0} -->

First, we note that these contracts are defined by linear inequalities.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions and Future Research", "weight": 1.0} -->

We presented an assume/guarantee contract framework for discrete-time dynamical systems. The framework puts assumptions on the input signal to the system, and prescribes guarantees on the output relative the the input. In particular, as the guarantees do not include the state, systems of different orders can satisfy the same contract. We also defined corresponding fundamental notions such as satisfaction, refinement, and cascaded composition. Perhaps more importantly, we showed that for contracts defined using linear inequalities, satisfaction and refinement can be verified using linear programming, which can be solved efficiently using off-the-shelf optimization software. Finally, we exemplified our methods using a case study on a 2-vehicle leader-follower scenario, where the goal was to obey a certain headway. Future research can extend our results by extending the methods presented in this work for nonlinear, uncertain, or hybrid systems, as well as for verifying compositional refinement, i.e. that a composition of multiple contracts on individual components or subsystems refines a contract on the composite system.
