<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multirobot Coordination with Counting Temporal Logics

Topics include Multi-agent systems, Multi-agent pathfinding, Temporal logic, Formal methods, Mixed-integer programming, Asynchronous coordination, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops counting temporal logics for specifying collective multi-robot behavior without assigning every robot a unique role. The paper combines logic-based planning, optimization, and robustness to bounded asynchrony, making it a bridge between formal methods and scalable multi-agent coordination.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In many multirobot applications, planning trajectories in a way to guarantee that the collective behavior of the robots satisfies a certain high-level specification is crucial. Motivated by this problem, we introduce counting temporal logics-formal languages that enable concise expression of multirobot task specifications over possibly infinite horizons. We first introduce a general logic called counting linear temporal logic plus (cLTL+), and propose an optimization-based method that generates individual trajectories such that satisfaction of a given cLTL+ formula is guaranteed when these trajectories are synchronously executed. We then introduce a fragment of cLTL+, called counting linear temporal logic (cLTL), and show that a solution to planning problem with cLTL constraints can be obtained more efficiently if all robots have identical dynamics. In the second part of the paper, we relax the synchrony assumption and discuss how to generate trajectories that can be asynchronously executed, while preserving the satisfaction of the desired cLTL+ specification. In particular, we show that when the asynchrony between robots is bounded, the method presented in this paper can be modified to generate robust trajectories.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate these ideas with an experiment and provide numerical results that showcase the scalability of the method.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

inline\]It would be a good idea to write about how solution times are sensitive to encoding methods in the introduction, to motivate why so many variants are introduced. Would also be good to add some intuitive explanations around the encodings, for a part there are just new encoding equations without too much explanation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multirobot systems can serve modern societies in a variety of ways, ranging from pure entertainment to critical search and rescue missions, from construction automation to micromanipulation. The number of robots required to achieve a common goal increases each day to improve the effectiveness and efficiency in such applications. Therefore, there is a need for scalable tools to coordinate the collective behavior of large numbers of robots. In this paper, we introduce *counting temporal logics* for specifying desired collective behavior of multirobot systems in a concise manner, and provide an optimization-based algorithm to synthesize trajectories that ensure the satisfaction of specifications given in this formalism. We show that counting temporal logics can capture meaningful and interesting multirobot tasks, and that the solution method proposed in this paper scales better with the number of robots than the existing methods. In fact, we show that our method scales to hundreds of robots under certain conditions. Moreover, we do not require robots to be synchronized perfectly or communicate during runtime.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional algorithms for multirobot coordination tend to focus on relatively simple tasks such as reaching a goal state while avoiding unsafe regions and collisions, or reaching a consensus. Temporal logics, such as Linear Temporal Logic (LTL), provide a powerful framework for defining more complex specifications, for example: *Always avoid collision with obstacles, do not cross into region A before visiting region B, and eventually visit regions A and C repeatedly*. Given requirements in a formal language, existing methods such as can generate correct-by-construction trajectories for single-agent systems. The use of LTL specifications has also been considered for multirobot systems. However, generalizations to multirobot systems suffer from the curse of dimensionality and cannot handle large numbers of robots. Furthermore, LTL does not provide a natural way to define group tasks, hence using LTL in multirobot settings results in long formulas, which are not desired as the complexity of the algorithms depend on the length of the formula.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing methods that use temporal logic to define multirobot specifications, such as, require that each robot be assigned an independent task, a tedious and error-prone process when the number of robots is large. In many applications, completion of a task depends not on identities of robots, but on the number of robots satisfying a property. Take for example an emergency response scenario where hundreds of autonomous vehicles are deployed to locate and help the victims. In such a scenario, it is reasonable to assume that most of the vehicles would have identical capabilities and that the identity of the vehicle is not important to the rescuers, as long as the given tasks are accomplished. On the other hand, tasks might depend on the number of agents satisfying a property. For instance, one might require sufficiently many robots to surveil a particular area to look for victims. Or, one might need to limit the number of rescuers in certain regions to avoid unsafe areas or congestion. We call this type of specification *temporal counting constraints* and propose a novel logic called *counting linear temporal logic plus (cLTL+)* to specify them. This logic is two-layered similar to.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The inner logic defines tasks that can be satisfied by a single robot, for instance *surveiling an area* in the previous emergency response scenario. The outer logic requires *sufficiently many* (or *not too many*) robots to satisfy tasks given as inner logic formulas. For example, one might express a task that "*at least $2$ and not more than $5$ robots* to surveil an area" using cLTL+.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

After introducing the logic, we propose an optimization-based method to generate individual trajectories that collectively satisfy specifications given in cLTL+. The method proposed in this paper uses an integer linear programming (ILP) formulation of temporal specifications with the assumption that robots are perfectly synchronized. We later relax this assumption and show how to generate solutions robust to bounded synchronization errors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also discuss several variants of the cLTL+ syntax. Firstly, we introduce a fragment of cLTL+, namely *counting linear temporal logic (cLTL)*. We show that an alternative solution method could scale to systems with hundreds of robots when specifications are given in cLTL and robots have identical dynamics. The logic cLTL and associated synthesis algorithms can be seen as an extension of a special class of counting problems that deal with invariant specifications, first proposed. Secondly, we present an extension to the syntax of cLTL+ to define tasks that could be carried out only by a certain group of robots. For example, one might require a surveillance task to be conducted by robots that are equipped with suitable cameras. This extension allows us to assign tasks to specific group of robots. Finally, we show that continuous state dynamics can be handled directly within our framework.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

As another contribution of this paper, we discuss how to relax the synchronous execution assumption and generate trajectories that can be executed asynchronously. Robustness against noise and parameter uncertainty has been extensively studied for single robot systems, and also extended to consensus problems. However, additional factors need to be addressed when dealing with multirobot systems. Unlike single robot systems, multirobot systems might tolerate the failure of individual agents without sacrificing task fulfillment. Such a notion of robustness against failing robots is examined. Another consideration in multirobot coordination problems is the robustness against synchronization errors. Perfect synchronization of robots might not be practical in real-life applications. The authors of characterized a class of LTL formulas that are robust to asynchrony and provided bounds on the deviation from optimality in the presence of asynchrony. However, for general LTL specifications, correctness cannot be guaranteed using this approach. A method that is based on prioritizing robots and planning individual trajectories sequentially was recently proposed.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectories generated with this approach, however, depend highly on how the robots are prioritized---feasible solutions can be missed if priorities are not correctly assigned. In this paper we propose a new definition of robust satisfaction of temporal logic formulas, similar in spirit to. We then provide small modifications to our method to generate trajectories that satisfy this notion of robustness, and show that the method is sound and partially complete.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Preliminary versions of this paper appeared in and. This paper provides a more comprehensive treatment of counting temporal logics and corresponding synthesis problems, including partially complete robust encodings, full proofs and several extensions. Moreover, experimental results implementing the synthesized trajectories in Robotarium are provided. The rest of the paper is organized as follows. Background information is provided in Section II. Section III introduces the syntax and semantics for cLTL+ and cLTL. Section IV formally defines the synchronous coordination problem and proposes a solution. An alternative solution, which can solve a special set of problems more efficiently, is also provided in the same section. Section V introduces a time-robustness concept and presents necessary modifications to the method in order to generate robust solutions. Section VI presents two extensions. We demonstrate the efficacy of the methods presented in this paper via numerical and experimental results in Section VII before concluding the paper in Section VIII.

<!-- chunk {"id": "body-0015", "role": "body", "section": "System and behavior descriptions", "weight": 1.0} -->

This section introduces the notation used in the rest of the paper and provides system and behavior definitions required to formally state the problem we seek to solve.

<!-- chunk {"id": "body-0016", "role": "body", "section": "System and behavior descriptions", "weight": 1.0} -->

The set of nonnegative integers is denoted by $\mathbb{N}$ and the set of positive integers up to $N$ is denoted by ${\lbrack N\rbrack} = {\{ 1,2,\ldots,N\}}$. We use $\mathbf{1}$ to denote the vector of all $1$'s. We define a set membership indicator function such that given a set A, ${\mathbb{1}_{A}{(a)}} = 1$ if $a \in A$ and ${\mathbb{1}_{A}{(a)}} = 0$ otherwise. The cardinality of a set $A$ is denoted by $|A|$. We next define transition systems that are used to model the robot dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1", "weight": 1.0} -->

Let the following three trajectories

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

denote the trajectories of a red, green, and a blue robot, respectively. An arbitrary collective execution is illustrated in Figure 1. Local counters are initially set as ${K{}} = {\lbrack 0\;0\;0\rbrack}$ at time $t = 0$; that is, each robot $\mathcal{R}_{n}$ is initially positioned at $\pi_{n}{}$. Every robot completes a transition by time $t = 1$, so local counters are updated as ${K{}} = {\lbrack 1\;1\;1\rbrack}$. The red and the blue robots move slower than expected and fail to complete two transitions by time $t = 2$. The green robot, on the other hand, successfully completes two transitions by time $t = 2$. Thus, local counters are updated as ${K{}} = {\lbrack 1\;2\;1\rbrack}$. Similarly, the values of the local counters up to $t = 5$ can be seen from Figure 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

As stated before, when robots are allowed to move asynchronously, there are infinitely many collective executions given a collection of trajectories. Without a bound on asynchrony, it might be impossible to achieve meaningful tasks. For this reason, we introduce the following definition.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Counting logics: syntax and semantics", "weight": 1.0} -->

This section provides the syntax and semantics of *counting linear temporal logic plus* (cLTL+), as well as the smaller fragment *counting linear temporal logic* (cLTL) which allows for more efficient solutions under certain conditions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

The logic cLTL+ is a two-layer logic similar to censusSTL. The *inner logic* is identical to LTL and is used to describe tasks that can be satisfied by a single robot. For example, tasks such as *"avoid collisions with obstacles at all times"* or *"eventually visit region $A$"* can be described by the inner logic. The outer layer then specifies the evolution of the number of robots required to satisfy an inner logic formula. Using the earlier examples, we can specify tasks such as *"All robots* must avoid collisions with obstacles" or *"At least five robots* should eventually visit region $A$" using cLTL+.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

where ${ap} \in {AP}$ is an atomic proposition and $\phi,\phi_{1}$ and $\phi_{2}$ are inner logic formulas. The symbols $\neg, \land, ○$ and $\mathcal{U}$ correspond to the logical operators *negation* and *conjunction*, and the temporal operators *next* and *until*, respectively.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

We use $\Phi$ to denote the set of all inner logic formulas defined according to. Although the inner logic is identical to LTL, we present the semantics here for the sake of completeness.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

Let $\sigma \in {(2^{AP})}^{\omega}$ be a trace and let $\phi$ be an inner logic formula.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

for any atomic proposition $a \in {AP}$, ${\sigma,t} \models a$ if and only if $a \in {\sigma{(t)}}$,

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

$\sigma,t \models ○ \varphi$ if and only if ${\sigma,{t + 1}} \models \varphi$, and

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

If ${\sigma,0} \models \varphi$, then we say that $\sigma$ *satisfies* $\varphi$ and write $\sigma \models \varphi$ for short. We say that a trajectory $\pi$ satisfies $\varphi$ if ${\sigma{(\pi)}} \models \varphi$, and write $\pi \models \varphi$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

After defining the inner logic, we now present the syntax for cLTL+ which is based on a new proposition type: a *temporal counting proposition* ($tcp$) is an inner logic formula paired with a nonnegative integer, i.e., ${tcp} = {\lbrack\phi,m\rbrack} \in {\Phi \times {\mathbb{N}}}$. The inner logic formula $\phi$ defines a task and $m$ specifies the number of robots needed to satisfy it. For example, ${tcp} = {\lbrack{◆a},5\rbrack}$ is a temporal counting proposition that evaluates to $True$ if the task "$◆a$" is satisfied by at least five robots.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

where ${tcp} \in {\Phi \times {\mathbb{N}}}$ is a temporal counting proposition and $\mu,\mu_{1}$ and $\mu_{2}$ are cLTL+ formulas. Identical to inner logic, other commonly used operators can be derived.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

Let $\Pi = {\{\pi_{1},\ldots,\pi_{N}\}}$ be a collection of trajectories and $K = {\lbrack{k_{1}\ldotsk_{N}}\rbrack}$ be a collective execution. Semantics of the outer logic is similar to the semantics of the inner logic, but they are defined for executions of collections of trajectories.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A cLTL+", "weight": 1.0} -->

If ${{(\Pi,K)},0} \models \mu$, then we say that the pair $(\Pi,K)$ *satisfies* $\mu$ and write ${(\Pi,K)} \models \mu$ for short.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B cLTL", "weight": 1.0} -->

Having defined the cLTL+, we now introduce *counting linear temporal logic* (cLTL), which corresponds to the fragment of cLTL+ where the inner logic is constrained to the grammar $\phi::=a$. Temporal counting propositions in cLTL have the special form ${tcp_{cLTL}} = {\lbrack a,m\rbrack}$ where the inner logic is restricted to atomic propositions instead of an LTL formula, i.e., $a \in {AP}$. As a result of this restriction, cLTL enforces robots to "synchronize".

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 2", "weight": 1.0} -->

Here the inner formula of $\mu_{1}$, "$a$", is an atomic proposition. Hence, $\mu_{1}$ is also a cLTL formula where the task "$a$" can be satisfied by any robot, simply by visiting a state where $a$ holds. The temporal counting proposition "$\lbrack a,m\rbrack$" is satisfied at time $t$ if at least $m$ robots to satisfy $a$ at time $t$. Moreover, the temporal operators "$\square◆$" in the outer layer necessitate that the temporal counting proposition is satisfied infinitely many times. Thus, there should be an infinite number of instances where $a$ is *simultaneously* satisfied by more than $m$ robots in order for $\mu_{1}$ to be satisfied.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 2", "weight": 1.0} -->

On the other hand, neither $\mu_{2}$ nor $\mu_{3}$ can be specified in cLTL. In both formulas, the inner formula contains temporal operators which are not allowed in the cLTL syntax. The difference between $\mu_{1}$ and $\mu_{2}$ is that the latter relaxes the simultaneity requirement. The inner formula $\square◆a$ can be satisfied by any robot if the robot satisfies $a$ infinitely many times. The integer $m$ is the smallest number of robots that needs to satisfy the inner formula. Hence, the cLTL+ formula $\mu_{2}$ requires at least $m$ robots to satisfy $a$ infinitely many times, but as opposed to $\mu_{1}$ they need not do so simultaneously. For any given time the number of robots that satisfy $a$ might never exceed $m$, or even $1$. Note that any collective trajectory that satisfies $\mu_{1}$ also satisfies $\mu_{2}$, but the converse is not true.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 2", "weight": 1.0} -->

The difference between $\mu_{2}$ and $\mu_{3}$ is more subtle. Any collective trajectory that satisfies $\mu_{2}$ would also satisfy $\mu_{3}$. The converse is also true if the number of robots is finite. However, in the hypothetical scenario where there are infinitely many robots, $\mu_{3}$ can be satisfied even if no robot satisfies $a$ more than once. $\blacksquare$

<!-- chunk {"id": "body-0036", "role": "body", "section": "Synchronous coordination problem and its solution", "weight": 1.0} -->

This section provides the formal definition of the synchronous multirobot coordination problem and provides an optimization-based solution for cLTL+ specifications. Subsequently, an alternative solution is proposed for the special case where the specifications are given in cLTL and the robots have identical dynamics. The alternative solution is shown to scale much better with the number of robots. In fact, the number of robots has almost no effect on the solution time and problems with hundreds of robots can be solved with the alternative method as demonstrated in Section VII.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem 1", "weight": 1.0} -->

In order to solve Problem 1, we generate individual trajectories in a centralized fashion. Robots then follow these trajectories in a distributed fashion, using local controllers without runtime communication. To generate trajectories we encode the robot dynamics and the cLTL+ constraints using integer linear constraints and pose the synthesis problem as an integer linear program (ILP). This approach is inspired by the bounded model-checking literature. In particular, we focus the search on individual trajectories on prefix-suffix form. That is, for a given integer $h$, we aim to construct individual trajectories of the form $\pi_{n} = {\pi_{n}{}\pi_{n}{}\ldots\pi_{n}{(h)}\ldots}$ and find an integer $l \in {\{ 0,\ldots,{h - 1}\}}$ such that for all $k \geq h$, ${\pi_{n}{(k)}} = {\pi_{n}{({{k + l} - h})}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem 1", "weight": 1.0} -->

In the following, we present ILP encodings of dynamic and temporal constraints.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Loop constraints", "weight": 1.0} -->

for all $n \in {\lbrack N\rbrack}$ and for all $t \in {\{ 0,\ldots,{h - 1}\}}$. These constraints guarantee that there exists a unique $t$ such that ${z_{loop}{(t)}} = 1$ and ${w_{n}{(h)}} = {w_{n}{(t)}}$. For all other time instances, the first two inequalities are trivially satisfied.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Inner logic constraints", "weight": 1.0} -->

We next recursively describe how counting temporal logic constraints can be translated into integer constraints. Let $\phi \in \Phi$ be an inner logic formula given according to and $h$ be the horizon length. For each robot $n$, we introduce $h$ binary decision variables ${z_{n}^{\phi}{(t)}} \in {\{ 0,1\}}$ for $t \in {\{ 0,1,\ldots,{h - 1}\}}$ and ILP constraints such that ${z_{n}^{\phi}{(t)}} = 1$ if and only if ${\pi_{n},t} \models \phi$. Hence, satisfaction of an inner formula $\phi$ by the robot $\mathcal{R}_{n}$ is equivalent to ${z_{n}^{\phi}{}} = 1$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Inner logic constraints", "weight": 1.0} -->

*$○$ (next):* Let $\phi = ○ \varphi$, then for all $n \in {\lbrack N\rbrack}$

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Inner logic constraints", "weight": 1.0} -->

where ${\overset{\sim}{z}}_{n}^{\phi}{(t)}$ are auxiliary binary variables. As shown, not introducing auxiliary variables results in trivial satisfaction of the *until* operator.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-D Outer logic constraints", "weight": 1.0} -->

Similar to the inner logic, we proceed by transforming a cLTL+ formula into ILP constraints. Given a cLTL+ formula $\mu$ and a time horizon $h$, we create $h$ binary decision variables $\mathbf{y}^{{\mathbf{c}\mathbf{L}\mathbf{T}\mathbf{L}} +} = {\{{y^{\mu}{(t)}}\}}$, where $t \in {\{ 0,1,\ldots,{h - 1}\}}$ and ILP constraints $ILP{(\mu)}$. While doing so, we ensure that ${y^{\mu}{(t)}} = 1$ if and only if ${{(\Pi,K^{\ast})},t} \models \mu$ where $K^{\ast}$ is the globally synchronous collective execution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-D Outer logic constraints", "weight": 1.0} -->

We remind the reader that since ILP constraints are created recursively, creating the constraints for formula $\mu$ will create the constraints for all the inner logic formulas appearing in $\mu$. We denote by $ILP{(\mu)}$ the set of all resulting constraints that encode the satisfaction of $\mu$, and by ${(\mathbf{z},\mathbf{y})}^{{\mathbf{c}\mathbf{L}\mathbf{T}\mathbf{L}} +}$, the set of all variables created in this process.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Outer logic constraints", "weight": 1.0} -->

We provide encodings only for counting propositions since the rest of the semantics are identical. Let $\mu = {\lbrack\phi,m\rbrack} \in {{AP} \times {\mathbb{N}}}$ be a temporal counting proposition. Then

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Outer logic constraints", "weight": 1.0} -->

where $M$ is a sufficiently large positive number, in particular, $M \geq {N + 1}$. Note that when ${y^{\mu}{(t)}} = 1$, the inequality on the right reduces to ${\sum_{n = 1}^{N}{z_{n}^{\phi}{(t)}}} \geq m$. Moreover, the inequality on the left is trivially satisfied since $M \geq {N + 1}$. Conversely, when ${y^{\mu}{(t)}} = 0$, the inequality on the right is trivially satisfied and the inequality on the left reduces to ${\sum_{n = 1}^{N}{z_{n}^{\phi}{(t)}}} < m$. Therefore, ${y^{\mu}{(t)}} = 1$ if and only if the number of robots that satisfy $\phi$ at time $t$ is greater than or equal to $m$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Outer logic constraints", "weight": 1.0} -->

Conversely, (${y^{\mu}{(t)}} = 0$) if and only if the number of robots that satisfy $\phi$ at time $t$ is less than $m$. Therefore, the ILP constraints in are correct and consistent with the semantics of cLTL+.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-E Overall optimization problem and its analysis", "weight": 1.0} -->

Next we analyze this solution approach. The following theorem shows that the solutions generated by are sound.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The proof of Theorem 2 highlights the advantages of using cLTL+ in scenarios where robot identity is not critical for accomplishing the collective task. Although the problem can be reduced to a standard LTL synthesis problem as the proof suggests, the reduction results in a synthesis problem on a product transition system with size exponential in the number of robots, and with an LTL formula that is combinatorially longer than the cLTL+ formula. Indeed, without a convenient logic, just writing down that LTL formula would be a tedious and error-prone task.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 1", "weight": 1.0} -->

A few remarks on the complexity are in order. An instance of has $\mathcal{O}{({hN{({{|S_{n}|} + {|\mu|}})}})}$ decision variables and constraints where $h$ is the solution horizon, $N$ is the number of robots, $|S_{n}|$ is the number of states of the largest transition system and $|\mu|$ is the length of the cLTL+ formula $\mu$. Enforcing collision avoidance introduces $\mathcal{O}{({hN^{2}{|S_{n}|}})}$ additional constraints.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-F cLTL encodings", "weight": 1.0} -->

Given an instance of Problem 1, if the specification $\mu$ can be expressed in cLTL and all robots have identical dynamics, more efficient encodings could be defined.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Given $N$ robots with identical dynamics $T = {(S,\rightarrow,{AP},L)}$, initial conditions $\{{\pi_{n}{}}\}$, and a cLTL formula $\mu$ over $AP$, synthesize a collection $\Pi = {\{\pi_{1},\ldots,\pi_{N}\}}$ of trajectories such that the globally synchronous collective execution of $\Pi$ satisfies $\mu$, i.e., ${(\Pi,K^{\ast})} \models \mu$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Let the set $S$ of states be enumerated such that $S = {\{ v^{1},v^{2},\ldots,v^{|S|}\}}$. Instead of individually encoding the dynamics of each robot, we define an *aggregate state* vector $\mathbf{w} = {\lbrack w^{1},w^{2},{\ldotsw^{|S|}}\rbrack}^{T}$ where the $i^{th}$ row of $\mathbf{w}$ denotes the number of robots at state $v^{i}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Similarly, the *aggregate input* is defined as a vector $\mathbf{u} = {\lbrack u_{1}^{1},u_{1}^{2},\ldots,u_{1}^{|S|},u_{2}^{1},{\ldotsu_{2}^{|S|}},{\ldotsu_{|S|}^{|S|}}\rbrack}^{T}$ where $u_{i}^{j}$ denotes the number of robots that transition from state $v^{i}$ to $v^{j}$. Note that the aggregate input is state-dependent since the total number of robots sent from a particular state to others cannot be greater than the number of robots in that state. Furthermore, the number of robots sent from a state can only be a non-negative integer.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Problem 2", "weight": 1.0} -->

An input satisfying these conditions is called *admissible* and $\Upsilon{(\mathbf{w})}$ denotes the set of all admissible inputs for a given state $\mathbf{w}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Inner logic constraints are no longer needed since the cLTL inner logic is constrained to the grammar $\phi::=a$ where $a \in {AP}$. In the outer logic, only the encoding of temporal counting propositions in needs modification. Let $\mu = {\lbrack a,m\rbrack}$ be a $tcp_{cLTL}$ and $S = {\{ v^{1},\ldots,v^{|S|}\}}$ be the set of states. We define the vector $\mathbf{v}^{a} \in {\{ 0,1\}}^{|S|}$ similar to, that is, the $i^{th}$ entry of $\mathbf{v}^{a}$ is $1$ if and only if $a \in {L{(v^{i})}}$. Then, for all $t = {0,\ldots,h}$, the constraints

<!-- chunk {"id": "body-0057", "role": "body", "section": "Problem 2", "weight": 1.0} -->

ensure that ${y^{\mu}{(t)}} = 1$ if and only if the number of robots that satisfy $a$ is greater than or equal to $m$. The rest of the outer logic encodings are not modified and used as before.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Problem 2", "weight": 1.0} -->

We now show how a solution of can be mapped to a collection $\{\pi_{n}\}$ of individual trajectories. Given initial conditions $\pi_{n}{}$, and $\mathbf{u}{}$, randomly choose $u_{i}^{j}$ robots from state $v^{i}$ and assign their next state as $v^{j}$. This is always possible since $\mathbf{w}{}$ is well defined and ${\mathbf{u}{}} \in {\Upsilon{({\mathbf{w}{}})}}$. Continuing in this manner, we can generate the collection $\{\pi_{n}\}$ whose globally synchronous collective execution satisfies the specification $\mu$. Details of a similar constructions of individual trajectories can be found.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Before proceeding to the asynchronous problem, we remind the reader of two important things: (i) the ILP constraints in are consistent with cLTL+ semantics, therefore soundness and completeness guarantees follow from Theorems 1 and 2. (ii) An instance of has $\mathcal{O}{(h{(|\rightarrow| + |\mu|)})}$ decision variables and constraints where $|\rightarrow|$ is the number of transitions and $|\mu|$ is the length of the formula. Crucially, the number of decision variables and constraints does not depend on the number of robots. Therefore, it easily scales to very large number of robots as demonstrated in Section VII.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Robustness to asynchrony", "weight": 1.0} -->

Incorporating a concept of time-robustness into our algorithm is useful since it is difficult to perfectly synchronize the motion of robots in real-life applications. This section presents small modifications to the original algorithm that allow one to synthesize trajectories that are robust to bounded synchronization errors.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Robustness to asynchrony", "weight": 1.0} -->

Synchronous execution assumes that multiple robots can transition from one discrete state to another at the same time. However, this is not always possible in reality where robots may move slower or faster than intended, leading to asynchronous switching times as illustrated in Figure 1. To exemplify, consider a task that requires multiple robots to satisfy a certain proposition at the same time. Let $\mu = {◆{\lbrack\phi,m\rbrack}}$ be a $tcp$, $\Pi$ be a collection of trajectories and $K$ be a synchronous collective execution.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Robustness to asynchrony", "weight": 1.0} -->

Assume that $\lbrack\phi,m\rbrack$ holds for a single time step $t$ and fails to hold for all others, i.e., ${{(\Pi,K)},t} \models {\lbrack\phi,m\rbrack}$ for some $t$ and ${{(\Pi,K)},t^{\prime}}\operatorname{\models\not{}}{\lbrack\phi,m\rbrack}$ for all $t^{\prime} \neq t$. While such a $\Pi$ satisfies $\mu$ for the synchronous execution it is not always a desirable collection, because if $K$ becomes asynchronous due to one of the robots moving slower than intended, correctness guarantees would no longer be valid and $\mu$ would not be satisfied. This fact motivates us to generate solutions that are robust to such asynchrony.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Robustness to asynchrony", "weight": 1.0} -->

For most non-trivial specifications however, finding a collection of trajectories that is robust to unbounded asynchrony would be challenging if not impossible. If, however, an upper bound on the asynchrony is known, one can generate robust solutions such that satisfaction of the task is guaranteed even under the worst-case scenario.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Robustness to asynchrony", "weight": 1.0} -->

To reason about asynchronicity we define the concept of *anchor time* for collective executions.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The negation operator can be omitted without loss of generality for two reasons. First, any LTL formula can be transformed into positive normal form (PNF), where the negation operator appears only before atomic propositions. Since the syntax of cLTL+ is identical to LTL, hence any cLTL+ formula can also be written in PNF where negation only appears before $tcp$'s. Second, given an arbitrary temporal counting proposition $\mu = {\lbrack\phi,m\rbrack}$, the statement $\neg\mu$ can be replaced by $\mu^{\prime} = {\lbrack{\neg\phi},{{N + 1} - m}\rbrack}$. Clearly, if there are at least ${N + 1} - m$ robots satisfying $\neg\phi$, then $\phi$ is satisfied by less than $m$ robots; hence, $\mu \equiv \mu^{\prime}$. Thus, the omission of the negation operator is without loss of generality.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Problem 3", "weight": 1.0} -->

We propose slight modifications to the encodings presented in Section IV to generate a collection of trajectories that are $\tau$-robust. Firstly, we define $\tau$ new Boolean vectors ${w_{n}{({h + 1})}},{w_{n}{({h + 2})}\ldotsw_{n}{({h + \tau})}}$ to represent the state of robot $n$ "after the loop" such that ${w_{n}{({h + k})}} = {w_{n}{({l + k})}}$ for some $l < h$ and $k = {0,1,\ldots,\tau}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Problem 3", "weight": 1.0} -->

Note that, $z_{n}^{\phi}{(t)}$ is defined for all $t \leq {h + \tau}$ due to newly defined additional state vectors. These new variables $r_{n}^{\phi}{(t)}$ can be seen as the robust versions of $z_{n}^{\phi}{(t)}$. In order for ${r_{n}^{\phi}{(t)}} = 1$ to hold, robot $n$ needs to satisfy the inner logic formula $\phi$ not only at time step $t$, but also for the next $\tau$ steps. Since at anchor time $t$, the local times are bounded as $t \leq {k_{n}{(t)}} < {t + \tau}$, this robustification ensures that robot $\mathcal{R}_{n}$ satisfies $\phi$ at anchor time $t$, regardless of the asynchrony.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Problem 3", "weight": 1.0} -->

We now define the modified outer logic constraints. As before, these constraints are constructed recursively. Let $\mu = {\lbrack\phi,m\rbrack}$ be a $tcp$ such that $m > 1$. Then is modified as

<!-- chunk {"id": "body-0069", "role": "body", "section": "Problem 3", "weight": 1.0} -->

For the special case where $\mu = {\lbrack\phi,1\rbrack}$, we use

<!-- chunk {"id": "body-0070", "role": "body", "section": "Problem 3", "weight": 1.0} -->

In the synchronous setting, satisfying a temporal counting proposition $\mu$ only for an instant would be enough. However, this is not desirable since robots might not be perfectly synchronized. Equations and ensures that all $\tau$-bounded executions satisfy $\mu$ at all time instances with anchor time $t$, by replacing each $z_{n}^{\phi}{(t)}$ with its robust counterpart $r_{n}^{\phi}{(t)}$. As a result, even in the worst case of asynchrony, there would be an instant where $\mu$ is satisfied.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Problem 3", "weight": 1.0} -->

Disjunction is encoded in two different ways: If all operands are temporal counting propositions, i.e, $\mu = {\bigvee_{i}\mu_{i}}$ where $\mu_{i} = {\lbrack\phi_{i},m_{i}\rbrack}$, then

<!-- chunk {"id": "body-0072", "role": "body", "section": "Problem 3", "weight": 1.0} -->

If the disjunction contains both $tcp$s and other formulas, then it can be re-written to leverage the less conservative encodings.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 3", "weight": 1.0} -->

If $\tau = 1$, the collection $\Pi$ does not robustly satisfy neither $\mu_{1}$ nor $\mu_{2}$ at anchor time $0$. On the other hand, for all time steps with anchor time $t$, any arbitrary $\tau$-bounded asynchronous execution satisfies either $\mu_{1}$ or $\mu_{2}$. This implies that ${\Pi \models_{\tau}\mu}.$

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 3", "weight": 1.0} -->

Equation limits the number of robots who neither satisfy $\phi_{1}$ nor $\phi_{2}$ at anchor time $t$. By doing so, it ensures that either $\mu_{1}$ or $\mu_{2}$ is satisfied by the collection. Observe that reduces to standard encodings for $\tau = 0$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 3", "weight": 1.0} -->

Due to changes in the outer disjunction encodings, the outer "until" operator needs to be modified as well. Let $\eta = {\mu_{1}\mathcal{U}\mu_{2}}$ where $\mu_{i}$ is a cLTL+ formula for $i = {1,2}$. Then

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 3", "weight": 1.0} -->

If $\mu_{2}$ is $\tau$-robustly satisfied at time $t$, then $\eta$ is $\tau$-robustly satisfied at time $t$, by definition of 'until'. In this case both ${y^{\mu_{2}}{(t)}} = 1$ and ${y^{\mu_{1} \vee \mu_{2}}{(t)}} = 1$ would hold, hence $y^{\eta}{(t)}$ would evaluate to $1$, as expected. If $\mu_{2}$ is *not* $\tau$-robustly satisfied at time $t$, enforces $\eta$ and $\mu_{1} \vee \mu_{2}$ (instead of $\mu_{1}$ as in ) to be $\tau$-robustly satisfied at anchor times $t + 1$ and $t$, respectively. This again guarantees that $\eta$ is $\tau$-robustly satisfied at anchor time $t$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 3", "weight": 1.0} -->

Auxiliary variables are used again to ensure $\mu_{2}$ is satisfied at some point. As before, reduces to the standard until encodings when $\tau = 0$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example 3", "weight": 1.0} -->

Furthermore, we provide the encodings for the "release" operator, which is identical to the standard encodings used in the literature: if $\eta = {\mu_{1}\mathcal{R}\mu_{2}}$, then

<!-- chunk {"id": "body-0079", "role": "body", "section": "Example 3", "weight": 1.0} -->

Release encodings guarantees that if $\mu_{1}$ is $\tau$-robustly satisfied for all anchor times $t$, then $\mu_{2}$ is $\tau$-robustly satisfied for all times up to and including $t$. The key difference from the until operator is that $\mu_{1}$ does not have to be satisfied at all if $\mu_{2}$ is satisfied for all times.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Example 3", "weight": 1.0} -->

Given an instance of Problem 3 and a horizon length $h$, let $ILP_{\tau}{(\mu)}$ be the set of ILP constraints and ${(\mathbf{z},\mathbf{r},\mathbf{y})}^{{\mathbf{c}\mathbf{L}\mathbf{T}\mathbf{L}} +}$ the decision variables created by using the robust encodings -.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Example 3", "weight": 1.0} -->

The following theorems show that the solution method proposed for the asynchronous case is sound, and also complete under certain conditions. The proofs are provided in the Appendix.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The alternative solution method proposed in Section IV-F uses more efficient encodings when the specifications are given in $cLTL$. However, these encodings use aggregate dynamics, therefore it is not possible to keep track of identities of the robots during synthesis. Hence, robust solutions cannot be generated with this alternative method.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Robustifying the trajectories increases the complexity as a function of $\tau$. In particular, an instance of has $\mathcal{O}{({\tauN{({{|S_{n}|} + {h{|\mu|}}})}})}$ additional decision variables and $\mathcal{O}{({\tauN^{2}h{|S_{n}|}})}$ additional constraints compared to. The effect of these additional variables and constraints on solution time is shown in Section VII.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Extensions and Discussion", "weight": 1.0} -->

In this section, we discuss two possible extensions of cLTL+. Firstly, we show how to handle continuous-state dynamics directly instead of transition systems. Secondly, we provide an extension of cLTL+ syntax that allows tasks to be assigned to specific robots or robot groups.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-A Extension to Continuous-State Dynamics", "weight": 1.0} -->

Up to now, we assumed that robot dynamics are modeled by transition systems. Given continuous dynamics, discrete abstraction techniques could be used to obtain transition systems. However, abstraction computations are costly and do not scale well with the number of dimensions. This section provides slight modifications to the earlier encodings such that continuous-state discrete-time dynamics can be handled directly.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-A Extension to Continuous-State Dynamics", "weight": 1.0} -->

Assume that the robot dynamics are given as

<!-- chunk {"id": "body-0087", "role": "body", "section": "VI-A Extension to Continuous-State Dynamics", "weight": 1.0} -->

The first modification is to replace the constraints in with for all $n \in {\lbrack N\rbrack}$ and for all $t$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-A Extension to Continuous-State Dynamics", "weight": 1.0} -->

where $M$ is a sufficiently large number. Equation enforces a loop by constraining $w_{n}{(h)}$ to be equal to $w_{n}{(t)}$ for some $t$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-A Extension to Continuous-State Dynamics", "weight": 1.0} -->

where $\epsilon$ is an infinitesimally small and $M$ is a sufficiently large number, and $e_{n}^{a}$ is a binary vector of size $d_{a}$. The $i^{th}$ row of $e_{n}^{a}$ is denoted by $e_{n}^{a,{(i)}}{(t)}$ and is used to check the satisfaction of the $i^{th}$ linear constraint. In equations (33a) and (33b), the $i^{th}$ linear constraint is satisfied if and only if ${e_{n}^{a,{(i)}}{(t)}} = 1$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VI-A Extension to Continuous-State Dynamics", "weight": 1.0} -->

Finally, we modify the optimization problem to account for auxiliary variables. Let $\mathbf{e}^{{cLTL} +}$ denote the set of all auxiliary variables created.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Remark 4", "weight": 1.0} -->

inline\]Maybe cite Vasus paper here too, or write more about continuous-state part in introduction

<!-- chunk {"id": "body-0092", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The resulting feasibility problem is a *mixed integer linear program (MILP)* if linear continuous-state dynamics are used.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Remark 5", "weight": 1.0} -->

As it is stated before, obtaining discrete abstractions from continuous dynamics is computationally expensive: the size of the transition system typically grows exponentially with the dimensionality of robot states. Since each discrete state in the transition system introduces a binary decision variable in the discrete-space formulation, the size of the optimization problem in can grow quickly. On the other hand each continuous state is represented with a single continuous decision variable. While the number of auxiliary binary decision variables introduced by depends on the specific problem instance, the continuous approach can be favorable when compared to an abstraction approach.

<!-- chunk {"id": "body-0094", "role": "body", "section": "VI-B Extension of cLTL+ Syntax", "weight": 1.0} -->

This section provides a straightforward extension of the cLTL+ syntax inspired by censusSTL proposed. Up to now, the logic is oblivious as to which robot satisfies what atomic proposition, or task. In most multirobot systems, robots have heterogeneous capabilities and certain tasks can only be performed by a specific subset of robots. For example, imagine a collection of drones and a reconnaissance mission that includes, among other things, taking aerial photos of a region. If not all of the drones have cameras, one might want to identify those that can take photos and require subtasks that involve photography to be completed by this subset. Similarly, in a collective of robots where one robot is designated to be the leader it may be desirable to specify that the other robots periodically have to report to the leader.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VI-B Extension of cLTL+ Syntax", "weight": 1.0} -->

To be able to specify such tasks, the temporal counting propositions ($tcp$) can be modified to contain the subset of robots that are designated with satisfying the inner logic formula. Redefine $tcp$ as a tuple consisting of an atomic proposition, a non-empty set of robots and a non-negative integer, i.e., $\mu = {\lbrack\phi,\mathcal{S},m\rbrack} \in {\Phi \times 2^{\lbrack N\rbrack} \times {\mathbb{N}}}$. Here satisfaction of $\mu$ at time $t$ requires at least $m$ robots from the subset $\mathcal{S} \in 2^{\lbrack N\rbrack}$ to satisfy $\phi$ at time $t$. By modifying $tcp$'s in this manner we can assign individual tasks to a specific subset of robots.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VI-B Extension of cLTL+ Syntax", "weight": 1.0} -->

To exemplify, given a collective $\mathcal{S}$ of drones, let $\mathcal{S}_{c} \in \mathcal{S}$ denote those with camera. Then the temporal counting proposition ${tcp} = {\lbrack a,\mathcal{S}_{c},m\rbrack}$ would be satisfied if at least $m$ drones from $\mathcal{S}_{c}$ visit regions marked by $a \in {AP}$ to take aerial photos.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VI-B Extension of cLTL+ Syntax", "weight": 1.0} -->

It is straightforward to see that and preserve all of the soundness and completeness guarantees for this extension.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Results", "weight": 1.0} -->

This section demonstrates the proposed method on an emergency response and presents scalability results. All experiments are run on a laptop with 2.5 GHz Intel Core i7 and 16 GB RAM and Gurobi is used as the underlying ILP solver. Our implementation can be accessed from

<!-- chunk {"id": "body-0099", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

Assume $N = 10$ robots are deployed in a workspace, which can be seen from Figure 2. The workspace is discretized into $10 \times 10$ cells and each robot is modeled with a transition system with $100$ states, each corresponding to a single cell. At each step, robots can either choose to stay put or travel to any of the four neighboring cells without leaving the workspace. We remark that a monolithic LTL solution for this problem would have required constructing a transition system with $100^{10}$ states.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

collision with obstacles, which are marked with $D$, should be avoided ($\mu_{1} = {\square{\neg{\lbrack D,1\rbrack}}}$).

<!-- chunk {"id": "body-0101", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

the bridge, marked by $B$, must not be occupied by more than $2$ robots ($\mu_{2} = {\square{\neg{\lbrack B,3\rbrack}}}$).

<!-- chunk {"id": "body-0102", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

each robot should visit charging stations, marked by $F$, infinitely many times ($\mu_{3} = {\lbrack{\square◆F},N\rbrack}$).

<!-- chunk {"id": "body-0103", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

In addition to these specifications, we require that robots avoid collisions with each other. We posit a time horizon $h = 35$ and solve the optimization problem for the synchronous case $\tau = 0$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

Important frames obtained from the $\tau = 0$ solution are shown in Fig. 3. Even though all specifications are met by this solution for a synchronous execution, it could easily break with the introduction of asynchrony. For instance, note that region $A$ is emptied (resp. region $C$ is populated with more than $5$ robots) only for a single time step at $t = 16$ (resp. $t = 18$). Hence, a single-step delay of a single robot could result in violation of $\mu_{6}$ (resp. $\mu_{5}$). Similarly, a robot enters the bridge for the first time at $t = 11$, which is the exact same time step when the bridge is inspected from both sides. If one of the robots inspecting the bridge moves slower than intended, $\mu_{8}$ would be violated.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

To prevent such violations, we set $\tau = 2$ and solve the resulting optimization problem. As it is shown in Fig. 4, this time the number of robots in $A$ (resp. in $C$) is greater than or equal to $5$, starting from $t = 1$ until $t = 3$ (resp. from $t = 20$ until $t = 22$). Furthermore, when the number of robots in region $A$ is greater than or equal to $5$, there are no robots in region $C$, and vice versa. Therefore, even in the worst case of bounded asynchrony, there will be at least one time instance where $A$ is populated with $5$ robots and another time instance where $A$ is empty. The same arguments hold for region $C$, as well. Additionally, the robots are more careful when crossing and the bridge: the bridge is first inspected at $t = 11$ and no robots enter the bridge until $t = 13$. Thus, the specification $\mu$ is satisfied even in the worst case of asynchrony.

<!-- chunk {"id": "body-0106", "role": "body", "section": "VII-A Emergency response example", "weight": 1.0} -->

We have implemented the trajectories extracted from the robust solution on real ground robots in Robotarium. In this experiment, robots track their respective trajectories using feedback from a top-mounted camera, and do not communicate with each other during runtime. The asynchrony is limited to $2$ discrete transitions. The video of the experiment can be viewed from As can be seen in the video, robots satisfy their tasks and avoid collisions despite the asynchrony.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VII-B Numerical examples", "weight": 1.0} -->

To examine the scalability of the proposed approach, we use the emergency response example explained in the previous section as a base example with the following parameters: the number of robots $N = 10$, solution horizon $h = 35$ and robustness parameter $\tau = 0$. We then vary one of these parameters at a time and report the average solution times over $5$ runs in Table I.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VII-B Numerical examples", "weight": 1.0} -->

We report results for three different implementations in Table I. The first implementation uses the encodings proposed in this paper. The second implementation is a special encoding that can only be used for $4$-connected grid environments. That is, robots move in a two dimensional gridded environment only horizontally or vertically. In this implementation, the number of Boolean variables needed to denote the state of the robot on a $x \times y$ gridded environment is $x + y$ as opposed to $xy$ for a general implementation. A smaller number of decision variables decreases the solution times significantly. We also implement the continuous-state extension proposed in Section VI-A. As can be seen in Table I, solution times can be reduced significantly if the encodings that are most appropriate for the problem at hand are used.

<!-- chunk {"id": "body-0109", "role": "body", "section": "VII-B Numerical examples", "weight": 1.0} -->

Additionally, we examine the solution times for different encodings when specifications are given in cLTL and the robots have identical dynamics. Assume that the transition system $T = {(S,\rightarrow,{AP},L)}$, where $\rightarrow$ is generated from an Erdös-Rényi graph with edge probability 0.25, represents the dynamics of $N$ robots. The set $S$ of states is partitioned into two sets of same size and labeled with $s_{1} \in {AP}$ and $s_{2} \in {AP}$, Each robot is assigned an initial state that is randomly selected from those labeled with $s_{1}$. Three goal regions are created such that each has $\frac{|S|}{10}$ randomly selected states and are labeled with $g_{i} \in {AP}$ for $i = {1,2,3}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VII-B Numerical examples", "weight": 1.0} -->

The specification $\mu$ requires at least half of the robots to reach states marked by $s_{2}$ and stay there indefinitely. Also, each goal region must be populated by at least $N/3$ robots, infinitely often over time. The results in Table II are obtained by varying either the number of robots $N = 10$ or the time horizon $h = 20$ while keeping all the other parameters intact. Solution times in the first and second column are obtained by alternative cLTL encodings proposed in Section IV-F and regular cLTL+ encodings, respectively. Regular cLTL+ encodings could not find solutions for $N = 500$ within the timeout threshold of $60$ minutes. On the other hand, cLTL encodings scale much better with the number of robots and easily handle hundreds of robots in a matter of seconds. In fact, solution times are almost unaffected by the number of robots.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper we presented counting temporal logics (cLTL and cLTL+) that are convenient for specifying desired behaviors for multirobot systems. We also proposed an optimization-based trajectory generation method to synthesize collective behaviors that satisfy specifications given in these formalisms. Furthermore, we showed how to generate trajectories that are robust to bounded asynchrony. We then discussed how to handle continuous-state systems and extended the cLTL+ syntax so that tasks can be assigned to a subset of robots. As numerical results suggest, solution times depend greatly on the specific method for encoding specifications. One possible direction for future research is to discover relevant applications and develop encodings tailored specifically to them. Finally, while the proposed techniques are shown to scale well with the number of robots, scalability with respect to the size of the transition system of the individual robots and with respect to the robustness parameter $\tau$ remains a challenge, which we are working on addressing via hierarchical approaches.
