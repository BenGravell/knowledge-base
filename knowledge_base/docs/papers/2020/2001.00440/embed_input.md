<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Drinking Philosophers to Asynchronous Path-Following Robots

Topics include Asynchronous coordination, Path following, Multi-agent systems, Coordination taxonomy, Formal methods, Robotics, Control systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Connects asynchronous robot path following to coordination ideas from the drinking philosophers problem. The contribution is a formal way to reason about progress and resource conflicts when robots execute paths without global synchronization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we consider the multi-robot path execution problem where a group of robots move on predefined paths from their initial to target positions while avoiding collisions and deadlocks in the face of asynchrony. We first show that this problem can be reformulated as a distributed resource allocation problem and, in particular, as an instance of the well-known Drinking Philosophers Problem (DrPP). By careful construction of the drinking sessions capturing shared resources, we show that any existing solutions to DrPP can be used to design robot control policies that are collectively collision and deadlock-free. We then propose modifications to an existing DrPP algorithm to allow more concurrent behavior, and provide conditions under which our method is deadlock-free. Our method does not require robots to know or to estimate the speed profiles of other robots and results in distributed control policies. We demonstrate the efficacy of our method on simulation examples, which show competitive performance against the state-of-the-art.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-robot path planning (MRPP) has been one of the fundamental problems studied by artificial intelligence and robotics communities. Quickly finding paths that take each robot from their initial location to target location, and ensuring that robots execute these paths in a safe manner have applications in many areas from evacuation planning to warehouse robotics, and from formation control to coverage.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are several challenges in multi-robot path planning such as scalability, optimality, trading off centralized versus distributed decisions and corresponding communication loads, and potential asynchrony. Planning optimal collision-free paths is known to be hard even in synchronous centralized settings. Recently developed heuristics aim to address the scalability challenge when optimality is a concern. Arguably, the problem gets even harder when there is non-determinism in the robot motions. One source of non-determinism is asynchrony, that is, the robots can move on their individual paths with different and time-varying speeds and their speed profiles are not known a priori. This might happen due to many factors such as low battery levels, calibration errors, or waiting to give way to humans in the workspace. The goal of this paper is, given a collection of paths, one for each robot, to devise a distributed protocol so that the robots are guaranteed to reach their targets in the face of asynchrony and avoid all collisions along the way. We call this the *Multi-Robot Path Execution (MRPE)* problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study this problem at a discrete-level where the execution policies we generate can be used with any suitably abstracted continuous-dynamics and low-level control policies that allow stopping the robot when needed. Moreover, our execution policies can interface with higher-level decision-making modules that lead to asynchrony by temporarily stopping the individual robots for emergencies, maintenance, or other reasons. In addition to MRPE, our execution policies can also be relevant for other applications such as transportation networks where vehicles travel on fixed tracks or manufacturing processes where workpieces follow complex conveyor networks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key insight of the paper is to recast the MRPE problem as a drinking philosophers problem (DrPP), an extension of the well-known dining philosophers problem. DrPP is a resource allocation problem for distributed and concurrent systems. By partitioning the workspace into a set of discrete cells and treating each cell as a shared resource, we show how to construct drinking sessions such that the MRPE problem can be solved using any DrPP algorithm. Existing DrPP algorithms, such as, can be implemented in distributed manner, and enjoy nice properties such as fairness and deadlock-freeness, while also guaranteeing collision avoidance when applied to multi-robot planning. To allow more concurrent behavior and to improve the overall performance, we further modify, and derive conditions on the collection of paths such that collisions and deadlocks are guaranteed to be avoided.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. Section 2 briefly presents related work. Section 3 formally defines the MRPE problem we are interested in solving. A brief summary of the DrPP and an existing solution is presented in Section 4. Section 5 recasts the MRPE problem as a DrPP, and shows that existing methods can be used to solve MRPE problems. Furthermore, this section provides modifications to that allow more concurrent behavior. Section 6 shows that, when fed by the same paths, our algorithm achieves competitive results with the state-of-the-art. Section 7 concludes the paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We start by providing definitions that are used in the rest of the paper and formally state the problem we are interested in solving. Let a set $\mathcal{R} = {\{ r_{1},\ldots,r_{N}\}}$ of robots share a workspace that is partitioned into set $\mathcal{V}$ of discrete cells. Two robots are said to be in *collision* if they occupy the same cell at the same time. An ordered sequence $\pi = {\{\pi^{0},\pi^{1},\ldots\}}$ of cells, where each $\pi^{t} \in \mathcal{V}$, is called a *path*. The path segment $\{\pi^{t},\pi^{t + 1},\ldots,\pi^{t'}\}$ is denoted by $\pi^{t:t'}$, and we write $v \in \pi$ if there exists a $t$ such that $\pi^{t} = v$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We assume that a path is given for each robot, and $\pi_{n}$ denotes the path associated with $r_{n}$. We allow paths to contain loops but require them to be finite. We use $\pi_{n}^{end}$ and $curr{(r_{n})}$ to denote the final cell of $\pi_{n}$ and the number of successful transitions completed by $r_{n}$, respectively. We also define ${next{(r_{n})}} \doteq {{curr{(r_{n})}} + 1}$. The motion of each robot is governed by a *control policy*, which issues one of the two commands at every time step: $$ $STOP$ and $$ *$GO$*. The $STOP$ action forces a robot to stay in its current cell. If the $GO$ action is chosen, the robot starts moving. This robot might or might not reach to the next cell within one time step, however, we assume that a robot eventually progresses if $GO$ action is chosen constantly.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

This non-determinism models the uncertainties in the environment, such as battery levels or noisy sensors/actuators, which might lead to robots moving faster or slower than intended. It can also be due to a higher-level decision maker that forces the robot to stay put for instance as an emergency stop to give way to humans in the workspace.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given a collection $\Pi = {\{\pi_{1},{\ldots\pi_{N}}\}}$ of paths, design a control policy for each robot such that all robots eventually reach their final cells while avoiding collisions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 1", "weight": 1.0} -->

As stated in the problem definition, we assume that predefined paths are known by every robot prior to the start of execution. There are many control policies that can solve Problem 1. For the sake of performance, policies that allow more concurrent behavior are preferred. In the literature, two metrics are commonly used to measure the performance: *makespan (latest arrival time)* and *flowtime (sum of arrival times)*. Given a set of robots $\mathcal{R} = {\{ r_{1},\ldots,r_{N}\}}$, if robot $r_{n}$ takes $t_{n}$ time steps to reach its final state, makespan and flowtime values are given by $\max_{1 \leq n \leq N}t_{n}$ and $\sum_{n = 1}^{N}t_{n}$, respectively. These values decrease as the amount of concurrency increases. However, it might not be possible to minimize both makespan and flowtime at the same time, and choice of policy might depend on the application.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1", "weight": 1.0} -->

To solve Problem 1, we propose a method that is based on the well-known drinking philosophers problem introduced. For the sake of completeness, this problem is explained briefly in Section 4.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

The drinking philosophers problem is a generalization of the well-known *dining philosophers problem* proposed. These problems capture the essence of conflict resolution, where multiple resources must be allocated to multiple processes. Given a set of processes and a set of resources, it is assumed that each resource can be used by at most one process at any given time. In our setting, processes and resources correspond to robots and discrete cells that partition the workspace, respectively. Similar to mutually exclusive use of the resources, any given cell can be occupied by at most one robot to avoid collisions. In the DrPP setting, processes are called *philosophers*, and shared resources are called *bottles*. A philosopher can be in one of the three *states*: $$ *tranquil*, $$ *thirsty*, or $$ *drinking*. A *tranquil* philosopher may stay in this state for an arbitrary period of time or *become thirsty* at any time it wishes. A thirsty philosopher *needs* a non-empty subset of bottles to drink. This subset, called *drinking session*, is not necessarily fixed, and it could change over time. After acquiring all the bottles in its current drinking session, a thirsty philosopher *starts drinking*.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

After a finite time, when it no longer needs any bottles, the philosopher goes back to tranquil state. The goal of the designer is to find a set of rules for each philosopher for acquiring and releasing bottles. A desired solution would have the following properties. (i) *Liveness:* A thirsty philosopher eventually starts drinking. In our setting liveness implies that each robot is eventually allowed to move. (ii) *Fairness:* No philosopher is consistently favored over another. In multi-robot setting, fairness indicate that there is no fixed priority order between robots. (iii) *Concurrency:* Any pair of philosophers must be allowed to drink at the same time, as long as they wish to drink from different bottles. Analogously, no robot waits unnecessarily.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

We base our method on the DrPP solution of, which is shown in Algorithm 1. This solution ensures liveness, fairness and concurrency. For the sake of completeness, we provide a brief summary of their solution, but refer the reader to for the proof of correctness and additional details.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

Each philosopher $p$ has a unique integer $id_{p}$ and keeps track of two non-decreasing integers: session number $s_num_{p}$ and the highest received session number $max_rec_{p}$. These integers are used to keep a strict priority order between the philosophers. Conflicts are resolved according to this order, in favor of the philosopher with the higher priority. We say that *philosopher $p$ has higher priority than philosopher* $r$ (denoted *$p \prec r$*) if ${({s_num_{p}},{id_{p}})} \prec {({s_num_{r}},{id_{r}})}$ that is ${s_num_{p}} < {s_num_{r}}$, or ${s_num_{p}} = {s_num_{r}}$ and ${id_{p}} < {id_{r}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

That is, smaller session number indicates a higher priority, and in the case of identical session numbers, philosopher with the smaller $id$ has the higher priority. Note that the priority order is not fixed as $s_num$ values change over time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

Philosophers also keep track of several Boolean variables. Let $p$ and $r$ be two philosophers and $b$ be a bottle shared between them. It must be noted that, philosophers $p$ and $r$ can share multiple bottles among each other, but each bottle $b$ is shared by exactly two philosophers. For each bottle $b$ in philosopher $p$'s inventory, we define two booleans $hold_{p}{(b)}$ and $req_{p}{(b)}$, and say that $p$ holds the bottle $b$ (or the request token for the bottle $b$) if the variable $hold_{p}{(b)}$ (or $req_{p}{(b)}$) holds $true$. Similarly, we say that $p$ needs $b$ if $need_{p}{(b)}$ hold $true$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

Algorithm 1 ensures mutual exclusiveness, that is, $hold_{p}{(b)}$ and $hold_{r}{(b)}$ (similarly $req_{p}{(b)}$ and $req_{r}{(b)}$) cannot be $true$ at the same time.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

Philosophers are initialized such that each philosopher is in tranquil state and $s_num$ and $max_rec$ are set to $0$. Bottles and associated request tokens are shared between philosophers such that one philosopher holds the bottle while the other holds the associated request token. Since philosophers are in tranquil state, all $need{(b)}$ variables are initially $false$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

The rules ${R1} - {R6}$ of Algorithm 1 are triggered by events. For example, if a philosopher $p$ wants to drink from a set of bottles $\mathcal{S}$, it needs to *become thirsty* first by executing $R1$. Upon holding all the bottles in $\mathcal{S}$, $R2$ is triggered and $p$ starts drinking. Similarly, $p$ triggers $R4$ when $p$ (i) needs $b$, (ii) does not currently hold $b$, and (iii) holds the associated request token $req_{p}{(b)}$. Then, $p$ requests the bottle from $r$ by sending the message $({req_{b}},{s_num_{p}},{id_{p}})$. Receiving such a message, triggers $R5$ in $r$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

If $r$ does not need $b$ or is thirsty and ${({s_num_{p}},{id_{p}})} \prec {({s_num_{r}},{id_{r}})}$, then it sets $hold_{r}{(b)}$ $false$ and sends the bottle to $p$. Sending a bottle is simply done by sending a message to $p$. Upon receiving such a message, $p$ sets $hold_{p}{(b)}$ $true$ by running $R6$. We refer the reader to for more details.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Drinking philosophers problem", "weight": 1.0} -->

1:R1: becoming_thirsty with session 𝒮 2:for each bottle b ∈ 𝒮 do 8:if holding all needed bottles then 12:R3: becoming_tranquil, honoring deferred requests 13:for each consumed bottle b do 21:if (n e e dp (b) and ¬h o l dp (b) and reqp(b))) then 26:R5: receiving a request from r, resolving a conflict 30:if ((¬needp(b)) or (p is t h i r s t y and (s_numr, idr) < (s_nump, idp))) then Algorithm 1 Drinking Philosopher Algorithm by

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multi-robot navigation as a drinking philosophers problem", "weight": 1.0} -->

In this section we recast the multi-robot path execution problem as an instance of drinking philosophers problem. We first show that naive reformulation using existing DrPP solutions leads to conservative control policies. We then provide a solution that is based on Algorithm 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Multi-robot navigation as a drinking philosophers problem", "weight": 1.0} -->

We first provide an intuitive explanation for the transformation from MRPE to DrPP, and then present the formal procedure. Given a set $\mathcal{V} = {\{ v_{1},\ldots,v_{|\mathcal{V}|}\}}$ of cells and a collection $\Pi = {\{\pi_{1},{\ldots\pi_{N}}\}}$ of paths, cells that appear in more than one path are called *shared* and the rest are called *free*. We denote the set of all shared cells by $\mathcal{V}_{shared}$. We assume that robots know all paths prior to the start of the execution, hence each robot knows which cells are shared and which ones are free. A shared cell must be occupied at most by one robot at any given time to avoid collisions. One can treat the robots as philosophers and shared cells as bottles to enforce this mutual exclusion requirement. In multi-robot setting, the actions *"moving between two free cells"* or *"occupying a free cell"* of a robot are mapped into the *tranquil* state.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Multi-robot navigation as a drinking philosophers problem", "weight": 1.0} -->

Similarly, the *"desire to move into a shared cell"* and *"moving towards or occupying a shared cell* are mapped into the *thirsty* and the *drinking* states, respectively.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Multi-robot navigation as a drinking philosophers problem", "weight": 1.0} -->

It must be noted that for a shared cell $v_{k} \in \mathcal{V}_{m,n}$, there exists a single bottle shared between $r_{n}$ and $r_{m}$, and both $b_{m,n}^{k}$ and $b_{n,m}^{k}$ refer to the same object. Multiple bottles would be defined for a shared cell that is visited by more than two robots, where each bottle is shared between exactly two robots. We use $\mathcal{B}_{m,n}$ and $\mathcal{B}_{m}$ to denote the set of all bottles $r_{m}$ shares with $r_{n}$ and with all other robots, respectively.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1", "weight": 1.0} -->

Bottles are used to indicate the priority order between robots over shared cells. For instance, if $b_{m,n}^{k}$ is currently held by robot $r_{m}$, then *$r_{m}$ has a higher priority than $r_{n}$ over the shared cell $v_{k}$*. Note that, this order is dynamic as bottles are sent back and forth.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1", "weight": 1.0} -->

Collisions can be prevented simply by the following rule: *"to occupy a shared cell $v_{k}$, the robot $r_{n}$ must be drinking from all the bottles in $B_{n}{(v_{k})}$".* That is, $r_{n}$ must set all the bottles in $B_{n}{(v_{k})}$ needed, and be in drinking state. Upon arriving a free cell, a drinking robot would become tranquil. This rule prevents collisions as $r_{n}$ is the only robot allowed to occupy $v_{k}$ while it is drinking from $B_{n}{(v_{k})}$. However, this rule is not sufficient to ensure that all robots reach their final cells. Without the introduction of further rules, robots might end up in a *deadlock*.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Naive Formulation", "weight": 1.0} -->

We now show that deadlocks can be avoided by constructing the drinking sessions carefully. For the correctness of DrPP solutions, all drinking sessions must end in finite time. If drinking sessions are set such that *a robot entering a shared cell is clear to move until it reaches a free cell without requiring additional bottles along the way*, then all drinking sessions would end in finite time. That is, if a robot is about to enter a segment which consists of consecutive shared cells, it is required to acquire not only the bottles associated with the first cell, but all the bottles on that segment. To formally state this requirement, let $\mathcal{S}_{n}{(t)}$ denote the drinking session associated with cell $\pi_{n}^{t}$ for robot $r_{n}$. That is, $r_{n}$ should be drinking from all the bottles in $\mathcal{B}_{n}{({\mathcal{S}_{n}{(t)}})}$ to occupy $\pi_{n}^{t}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Naive Formulation", "weight": 1.0} -->

Now set where $\pi_{n}^{k} \in \mathcal{V}_{shared}$ for all $k \in {\lbrack t,t'\rbrack}$ and $\pi_{n}^{t' + 1} \in \mathcal{V}_{free}$ is the first free cell after $\pi_{n}^{t}$. As long as it is drinking from $\mathcal{S}_{n}{(t)}$, $r_{n}$ has the highest priority among all robots over the cells $\pi_{n}^{t:t'}$. Then, $r_{n}$ can constantly choose the action $GO$ until eventually reaching the free cell $\pi_{n}^{t' + 1}$ and would stop drinking in finite time. Therefore, any existing DrPP solution, such as, can be used to design the control policies that solve Problem 1 if the drinking sessions are constructed as.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Naive Formulation", "weight": 1.0} -->

To illustrate, let us revisit the scenario in Figure 1. To be able to occupy $v_{1}$, $r_{1}$ needs to acquire all bottles in $\mathcal{B}_{1}{(v_{1},v_{2},v_{4},v_{6})}$. Then, $r_{1}$ is free to move all the way up to the last shared state $v_{6}$ without requiring additional bottles. Note however that, once $r_{1}$ reaches $v_{2}$, bottles $\mathcal{B}_{1}{(v_{1})}$ are no longer needed to avoid deadlocks.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Naive Formulation", "weight": 1.0} -->

However, the control policies resulting from the aforementioned approach are conservative and lead to poor performance in terms of both makespan and flowtime. To illustrate using the scenario shown in Figure 1, if $r_{1}$ is currently at $v_{1}$, $r_{5}$ cannot move into $v_{6}$ since $b_{1,5}^{6}$ is held by $r_{1}$. This is a conservative action as $r_{5}$ cannot cause a deadlock by moving to $v_{6}$, as it moves to a free cell right after.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Naive Formulation", "weight": 1.0} -->

We have seen that *small* drinking sessions might lead to deadlocks, and *large* drinking sessions might lead to unnecessary waits, and thus, bad performance. Our goal is to construct drinking sessions *as small as possible* such that we can guarantee deadlock-freeness while allowing as much concurrent behavior as possible. To achieve this goal, we introduce a new drinking state and rules regarding its operation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "New Drinking State and New Rules", "weight": 1.0} -->

This information is used in conjunction with $id$ and $s_num$ by the receiver to decide whether to grant or defer the request.

<!-- chunk {"id": "body-0038", "role": "body", "section": "New Drinking State and New Rules", "weight": 1.0} -->

In the naive formulation, drinking sessions are set such that a robot entering a shared cell is free to move until it reaches a free cell, without requiring additional bottles along the way. The insatiable state is intended to soften this constraint. Assume robot $r_{n}$ wants to move to shared cell $\pi_{n}^{t}$, and the first free cell after $\pi_{n}^{t}$ is $\pi_{n}^{t' + 1}$ for some arbitrary $t' > t$, all the cells in between are shared. If $r_{n}$ enters the first shared cell without acquiring all the bottles until $\pi_{n}^{t' + 1}$, it would need to acquire those bottles at some point along the way. If $r_{n}$ becomes thirsty to acquire those bottles, it risks losing the bottles it currently holds. If another robot $r_{m}$ with a higher priority needs and receives the bottles associated with the cell $r_{n}$ currently occupies, two robots might collide.

<!-- chunk {"id": "body-0039", "role": "body", "section": "New Drinking State and New Rules", "weight": 1.0} -->

Insatiable state allows a robot to request new bottles without risking to lose any of the bottles it currently holds. In this state, the robot does not hold all the bottles it needs to start drinking, similar to thirsty state. The difference between two states is that, an insatiable philosopher always has a higher priority than a thirsty philosopher regardless of their session numbers. Moreover, an insatiable philosopher does not release under any circumstance any of the bottles needed to occupy the cell it is currently.

<!-- chunk {"id": "body-0040", "role": "body", "section": "New Drinking State and New Rules", "weight": 1.0} -->

In other words, if $p$ is insatiable with $(\mathcal{B}_{1},\mathcal{B}_{2})$, then $p$ already has all bottles in $\mathcal{B}_{1}$ and cannot release them. Moreover, $p$ is trying to acquire the bottles in $\mathcal{B}_{2}$ to start drinking, which might be released, if a robot with higher priority requests them. An insatiable robot always has a higher priority than a thirsty robot. In case of identical drinking states, $\prec$ relation is used to resolve the priority order.

<!-- chunk {"id": "body-0041", "role": "body", "section": "New Drinking State and New Rules", "weight": 1.0} -->

The insatiable state and the rules regarding its operation might lead to deadlocks without careful construction of drinking sessions. We now explain how to construct drinking sessions to avoid deadlocks.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

Algorithm 2 needs to find all rainbow cycles of an edge-colored multi-graph at each iteration, which can be done in the following way. Given $G = {(\mathcal{V},\mathcal{E},\mathcal{C})}$, obtain $E \subseteq {\mathcal{V} \times \mathcal{V}}$ from $\mathcal{E}$ by removing the coloring and replacing multiple edges between the same two nodes with a single edge. Then, find all simple cycles in the graph $G' = {(\mathcal{V},E)}$. Finally, check if these cycles can be colored as a rainbow cycle.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

Finding all simple cycles in a directed graph is time bounded by $\mathcal{O}{({{({{|V|} + {|E|}})}{({C + 1})}})}$ and space bounded by $\mathcal{O}{({(|V| + |E|)}}$, where $C$ is the number of cycles. Although the number of cycles in a directed graph grows, in the worst-case, exponentially with the number of nodes, this operation can be done efficiently in practice. Deciding if a cycle can be rainbow colored can be posed as an exact set cover problem, which is NP-complete. This is essentially due to the fact that, in the worst-case, the number of cycles in a multi-graph can be exponential in the number of colors compared to the corresponding directed graph. However, the number of nodes decrease at each iteration of Algorithm 2, making computations easier. Moreover, while the worst-case complexity is high, these operations can usually be performed efficiently in practice.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

We now revisit the example in Figure 1.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 5.3", "weight": 1.0} -->

While all cells except $v_{6}$ get merged into a single cell in Figure 1, constructing drinking sessions as in allows multiple robots to simultaneously occupy $v_{1} - v_{5}$. For instance, the drinking sessions of $r_{1}$ and $r_{3}$ are disconnected since they have no common cells. Therefore, $r_{1}$ and $r_{3}$ can enter cells $v_{1}$ and $v_{3}$, respectively, at the same time. Similarly, such drinking sessions also allow $r_{1}$, $r_{2}$ and $r_{3}$ to simultaneously occupy cells $v_{4}$, $v_{2}$ and $v_{5}$, respectively. Even in this small example, we can see the benefit of using Eq. instead of Eq.. The modification allows $r_{1}$ and $r_{5}$ to be at $v_{4}$ and $v_{6}$, respectively, while it was not possible with the naive formulation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 5.4", "weight": 1.0} -->

Sessions constructed by are always contained in the sessions constructed. That is, when drinking sessions are found as, robots would need fewer bottles to move, and the resulting control policies would be more permissive.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 5.4", "weight": 1.0} -->

We now propose a control policy that prevents collisions and deadlocks when drinking sessions are constructed as.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

We propose Algorithm 3 as a control policy to solve Problem 1. In order to implement Algorithm 3 in a distributed manner, we require the communication graph to be identical to the resource dependency graph. That is, if two robots visit a common cell, there must be a communication channel between them. We also assume that messages from one robot to another are received in the order that they are sent. We now briefly explain the flow of the control policy, which is illustrated in Figure 2, and then provide more details.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

Robots are initialized as follows. If robot $r_{n}$ starts at a shared cell, all bottles in its initial drinking session are given to $r_{n}$ and the related request tokens are given to the corresponding robots. To ensure bottles can be assigned in this way, we require that the initial drinking sessions are disjoint. Robots with shared initial cells are then initialized in drinking state, which is possible since they hold all the required bottles, and the remaining robots are initialized in tranquil state.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

If the final cell is reached, $STOP$ action is chosen as the robot accomplished its task. Otherwise, if a robot is in either tranquil or drinking state, the control policy chooses the action $GO$ until the robot reaches to the next cell. When a robot moves from a free cell to a shared cell, it first becomes thirsty and the control policy issues the action $STOP$ until the robot starts drinking. When moving between shared cells, a robot becomes insatiable if it needs to acquire additional bottles, and $STOP$ action is chosen until the robot starts drinking again. If a robot $r_{n}$ is leaving a shared cell where another robot $r_{m}$'s path terminates, for the last time, $r_{n}$ sends $r_{m}$ a *cleared* message. When a robot's path terminates at a shared cell, it must be careful not to arrive early and block others from progressing. Therefore, when a robot is about to move to a segment of consecutive shared cells which includes its final cell, it needs to wait for others to clear its final cell.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

All robots are initialized as previously described. Let $r_{n}$ be an arbitrary robot. Lines $1 - 2$ of Algorithm 3 ensure that $r_{n}$ does not move after reaching its final cell. Otherwise, let $\pi_{n}^{t}$ denote the next cell on $r_{n}$'s path. If $\pi_{n}^{t}$ is a free cell, the control policy chooses the $GO$ action until the robot reaches $\pi_{n}^{t + 1}$ (lines $5 - 8$). $r_{n}$ goes back to tranquil state if it was drinking and sends a *cleared* message to a corresponding robot $r_{m}$ if (i) $\pi_{n}^{t - 1}$ was the terminal cell for $r_{m}$ and (ii) $\pi_{n}^{t - 1}$ will not be visited by $r_{n}$ again in the future (lines $9 - 13$).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

When $\pi_{n}^{t}$ is a shared cell, there are two possible options: (i) If there is no free cell between the next cell and the final cell of $r_{n}$, i.e., $\pi_{n}^{end} \in {\mathcal{S}_{n}{(t)}}$ where $\mathcal{S}_{n}{(t)}$ is defined as, the robot must wait for all other robots to clear this cell (lines $15 - 18$). This wait is needed, otherwise, $r_{n}$ might block others by arriving and staying indefinitely at its final cell. When all others clear its final state, $r_{n}$ can start moving again. (ii) If the final cell is not included in the drinking session, $r_{n}$ checks its drinking state.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

If tranquil, $r_{n}$ becomes thirsty with the drinking session ${\overset{\sim}{\mathcal{S}}}_{n}{(t)}$ (lines $19 - 20$). If drinking, $r_{n}$ becomes insatiable with $\left( {\mathcal{B}_{n}\left( {{\overset{\sim}{\mathcal{S}}}_{n}{(t)}} \right)},{\mathcal{B}_{n}\left( {{\overset{\sim}{\mathcal{S}}}_{n}{({t + 1})}} \right)} \right)$ (lines $21 - 22$). Then, the robot waits until it starts drinking to move to the next cell (lines $24 - 26$). When the robot starts drinking, it is allowed to move until it reaches $\pi_{n}^{t}$ (lines $27 - 29$).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

Upon reaching $\pi_{n}^{t}$, the robot sends cleared signal if needed (line $31$), as previously explained.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Control Strategy", "weight": 1.0} -->

We now show the correctness of Algorithm 3.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 5.6", "weight": 1.0} -->

the Naive formulation explained in Section 5.1 also solves Problem 1. However, as mentioned in Remark 5.4, drinking sessions constructed by always contain sessions constructed, that is, ${\mathcal{S}_{n}{(t)}} \supseteq {{\overset{\sim}{\mathcal{S}}}_{n}{(t)}}$. Therefore, condition of Theorem 5.5 becomes more restrictive for the Naive implementation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 5.7", "weight": 1.0} -->

The control policy given in Algorithm 3 satisfies liveness, fairness and concurrency properties. The liveness proof is shown in Theorem 5.5, and fairness and concurrency properties follows directly.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we compare our *Rainbow Cycle* based method explained in Sections 5.2-5.4, denoted *DrPP-RC*, with other path execution methods using identical paths. Firstly, we compare DrPP-RC with the *Naive* method, denoted *DrPP-N*, which is explained in Section 5.1. This comparison demonstrates the performance improvement that results from the addition of the new drinking state. As stated in Remark 5.4, DrPP-RC uses smaller drinking sessions, and allows more concurrency. We also provide results for DrPP-N *without* $R7$. This rule is an addition to the original DrPP solution of and exploits the structure of the multi-robot path execution problem by allowing robots to drop bottles while in drinking state.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results", "weight": 1.0} -->

We further compare DrPP-RC with the *Minimal Communication Policy* of, denoted *MCP*, which prevents collisions and deadlocks by maintaining a fixed visiting order for each cell. A robot is allowed to enter a cell only if all the other robots, which are planned to visit the said cell earlier, have already visited and left the said state. It is shown that, under mild conditions on the collection of the paths, keeping this fixed order prevents collisions and deadlocks. We refer the reader to for more details.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results", "weight": 1.0} -->

We also note that, conditions required by are too restrictive for the majority of the examples provided in this section. That is, some nodes in Path-Graph are connected by more than one colored edge, hence cannot be used. On the other hand, merging shared cells as in Equation generates a quotient graph that satisfies the required conditions. Then, the performance of is identical to that of DrPP-N without $R7$. However, as Section 6.1 shows, cannot still solve all problems solved by DrPP-RC, and for the problems it can solve, it is significantly outperformed by both DrPP-RC and DrPP-N.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results", "weight": 1.0} -->

To capture the uncertainty in the robot motions, each robot is assigned a *delay probability*. When the action $GO$ is chosen, a robot either stays in its current cell with this probability, or completes its transition to the next cell before the next time step leading to asynchrony between robots' motion. Our implementation can be accessed from

<!-- chunk {"id": "body-0062", "role": "body", "section": "Randomly Generated Examples", "weight": 1.0} -->

There are $10$ MRPE instances, labelled random 1-10, where $35$ robots navigate in 4-connected grids of size $30 \times 30$. In each example, randomly generated obstacles block $10\%$ of the cells, and robots are assigned random but unique initial and final locations. The first of these randomly generated examples can be seen Figure 3. All control policies use the same paths generated by the Approximate Minimization in Expectation algorithm of. Delay probabilities of robots are sampled from the range $(0,{1 - {1/t_{max}}})$. Note that, higher delay probabilities can be sampled as $t_{max}$ increase, resulting in *slow moving* robots. Figure 4 reports the makespan and flowtime statistics averaged over 1000 runs for varying $t_{max}$ values. The delay probabilities are sampled randomly for each run, but kept identical over different control policies. As expected, both makespan and flowtime statistics increase with $t_{max}$, as higher delay probabilities result in slower robots.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Randomly Generated Examples", "weight": 1.0} -->

An illustrative run of the DrPP-RC algorithm for $t_{max} = 2$ and environment random1 can be seen from From Figure 4, we first observe that the addition of $R7$ improves the flowtime performance of DrPP-N significantly, while its effect on makespan is neglible. Secondly, we observe that DrPP-RC always performs better than DrPP-N. This is expected as drinking sessions for DrPP-N, which are computed, are always larger than the ones of DrPP-RC, which are computed. That is, robots using DrPP-N need more bottles to move, and thus, wait more. Moreover, DrPP-N requires stronger assumptions to hold for a collection of paths. For instance, only one of the ten random examples (random7) satisfy the the assumptions in Theorem 5.5 for DrPP-N. The number of instances that satisfy the assumptions increase to four for DrPP-RC (random 3, 4, 7, 10). The random1 example illustrated in Figure 3 originally violates the assumptions, but this is fixed for both drinking based methods by adding a single cell into a robot's path.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Randomly Generated Examples", "weight": 1.0} -->

We here note that, the set of valid paths for MCP and DrPP algorithms are non-comparable. There are paths that satisfy the assumptions of one algorithm and violate the other, and vice versa.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Randomly Generated Examples", "weight": 1.0} -->

We also observe that makespan values are quite similar for DrPP-RC and MCP methods, although MCP often performs slightly better in this regard. Given a collection of paths, the makespan is largely determined by the *"slowest"* robot, a robot with a long path and/or a high delay probability, regardless of the control policies. Therefore, makespan statistics do not necessarily reflect the amount of concurrency allowed by the control policies. Ideally, in the case of a slow moving robot, we want the control policies not to stop or slow down other robots unnecessarily, but to allow them move freely. The flowtime statistics reflect these properties better. From Figure 4, we see that flowtime values increase more significantly with $t_{max}$ for MCP, compared to DrPP-RC. This trend can be explained with how priority orders are maintained in each of the algorithms. As the delay probabilities increase, there is more uncertainty in the motion of robots. MCP keeps a fixed priority order between robots, which might lead to robots waiting for each other unnecessarily.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Randomly Generated Examples", "weight": 1.0} -->

On the other hand, DrPP-RC dynamically adjusts this order, which leads to more concurrent behavior, hence the smaller flowtime values. Section 6.2 illustrates this phenomenon with a simple example.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Makespan versus Flowtime", "weight": 1.0} -->

As mentioned earlier, assumes that delay probabilities are known a priori, and computes paths to minimize the expected makespan. Once the paths are computed, the priority order between robots is fixed to ensure MCP policies are collision and deadlock-free. We now provide a simple example to illustrate the effect of using inaccurate delay probabilities in the path planning process. Imagine $3$ robots are sharing a $10$ by $10$ grid environment as shown in Figure 5. Assume that the delay probabilites for robots $r_{1}$, $r_{2}$ and $r_{3}$ are known to be $\{ 0,0.4,0.8\}$, respectively. If we compute paths to minimize the expected makespan, resulting paths are straight lines for each robot. Paths $\pi_{1}$ and $\pi_{2}$ intersect at a single cell, for which $r_{1}$ has a priority over $r_{2}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Makespan versus Flowtime", "weight": 1.0} -->

Similarly $\pi_{2}$ and $\pi_{3}$ also intersect at a single cell, for which $r_{2}$ has a priority over $r_{3}$. We run this example using inaccurate delay probabilities $\{ 0.8,0.4,0\}$ to see how the makespan and flowtime statistics are affected.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Makespan versus Flowtime", "weight": 1.0} -->

Over $1000$ runs, makespan values are found to be $48.30$ and $45.77$ steps for MCP and DrPP-RC implementations, respectively. The makespan values are close because of the slow moving $r_{1}$, which becomes the bottleneck of the system. Therefore, it is not possible to improve the makespan statistics by employing different control policies. However, the flowtime statistics are found as $128.78$ and $77.78$ steps for MCP and DrPP-RC implementations, respectively. Significant difference is the result of how a slow moving robot is treated by each policy. For the MCP implementation, $r_{2}$ (resp. $r_{3}$) needs to wait for $r_{1}$ (resp. $r_{2}$) unnecessarily, since the priority order is fixed at the path planning phase. On the other hand, DrPP-RC implementation allows robots to modify the priority order at run-time, resulting in improved flowtime statistics.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Warehouse Example", "weight": 1.0} -->

We also compare the performance of the control policies in a more structured warehouse-like environment. This warehouse example is taken, and it has $35$ robots as shown in Figure 6. The makespan and flowtime statistics are reported in Figure 7, which are averaged over 1000 runs for varying $t_{max}$ values. Due to stronger assumptions on the collection of paths, DrPP-N is not able to handle this example. Similarly, the conditions required by are too restrictive, hence it cannot solve this problem. Although paths can be altered to allow to be used, this requires each aisle to be abstracted as one discrete cell, and limits the number of robots in each aisle to at most one. As a result, the performance of would be significantly worse compared to both DrPP-RC and MCP, no matter how paths are generated.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Warehouse Example", "weight": 1.0} -->

Similar to Section 6.1, we observe that makespan values are better for MCP, but DrPP-RC scales better with $t_{max}$ for flowtime statistics. Upon closer inspection, we see that robots moving in narrow corridors in opposite directions lead to many rainbow cycles. By enforcing a one-way policy in each corridor, similar to, many of these rainbow cycles can be eliminated and the performance of our method can be improved. Indeed, Figure 7 reports the results when paths are modified such that no horizontal corridor has robots moving in opposing directions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Warehouse Example", "weight": 1.0} -->

We further use the same warehouse example to demonstrate how DrPP-RC can be used in conjunction with a higher-level emergency stopping algorithm. In practical examples, robots carry shelves around the warehouse, which might make it dangerous for humans to work in the same space. To guarantee safety for humans, we require robots to stop and give way if there is a human in a predefined radius. As the video in shows, DrPP-RC guarantees that deadlocks and collisions are avoided in such cases.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we presented a method to solve the multi-robot path execution (MRPE) problem. Our method is based on a reformulation of the MRPE problem as an instance of drinking philosophers problem (DrPP). We showed that the existing solutions to the DrPP can be used to solve instances of MRPE problems if drinking sessions are constructed carefully. However, such an approach leads to conservative control policies. To improve the system performance, we provided a less conservative approach where we modified an existing DrPP solution. We provided conditions under which our control policies are shown to be collision and deadlock-free. We further demonstrated the efficacy of this method by comparing it with existing work. We observed that our method provides similar makespan performance to while outperforming it in flowtime statistics, especially as uncertainty in robots' motion increase. This improvement can be explained mainly by our method's ability to change the priority order between robots during run-time, as opposed to keeping a fixed order.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our current method and derived conditions that guarantee collision and deadlock-freeness are limited to the multi-robot path execution problem where robot paths are assumed to be fixed a priori. Using such conditions to guarantee deadlock-freeness of replanning approaches or designing life-long planning algorithms with similar guarantees are interesting directions for future research. We are also interested in finding looser conditions that guarantee collision and deadlock-freeness, as the current conditions are sufficient but might not be necessary.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We thank Hang Ma from Simon Fraser University and Sven Koenig from University of Southern California for sharing their code for MCP implementation in with us. We also thank Ruya Karagulle for pointing out typos in Theorem 1. The last but not least, we thank the reviewers for their valuable comments and suggestions, which improved the clarity and the presentation of the paper greatly. This work is supported in part by ONR grant N00014-18-1-2501, NSF grant ECCS-1553873, and an Early Career Faculty grant from NASA's Space Technology Research Grants Program.
