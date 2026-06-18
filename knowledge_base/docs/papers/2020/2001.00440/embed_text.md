## Introduction

Multi-robot path planning (MRPP) has been one of the fundamental problems studied by artificial intelligence and robotics communities. Quickly finding paths that take each robot from their initial location to target location, and ensuring that robots execute these paths in a safe manner have applications in many areas from evacuation planning to warehouse robotics, and from formation control to coverage.

There are several challenges in multi-robot path planning such as scalability, optimality, trading off centralized versus distributed decisions and corresponding communication loads, and potential asynchrony. Planning optimal collision-free paths is known to be hard even in synchronous centralized settings. Recently developed heuristics aim to address the scalability challenge when optimality is a concern. Arguably, the problem gets even harder when there is non-determinism in the robot motions. One source of non-determinism is asynchrony, that is, the robots can move on their individual paths with different and time-varying speeds and their speed profiles are not known a priori. This might happen due to many factors such as low battery levels, calibration errors, or waiting to give way to humans in the workspace. The goal of this paper is, given a collection of paths, one for each robot, to devise a distributed protocol so that the robots are guaranteed to reach their targets in the face of asynchrony and avoid all collisions along the way. We call this the *Multi-Robot Path Execution (MRPE)* problem. We study this problem at a discrete-level where the execution policies we generate can be used with any suitably abstracted continuous-dynamics and low-level control policies that allow stopping the robot when needed. Moreover, our execution policies can interface with higher-level decision-making modules that lead to asynchrony by temporarily stopping the individual robots for emergencies, maintenance, or other reasons. In addition to MRPE, our execution policies can also be relevant for other applications such as transportation networks where vehicles travel on fixed tracks or manufacturing processes where workpieces follow complex conveyor networks.

The key insight of the paper is to recast the MRPE problem as a drinking philosophers problem (DrPP), an extension of the well-known dining philosophers problem. DrPP is a resource allocation problem for distributed and concurrent systems. By partitioning the workspace into a set of discrete cells and treating each cell as a shared resource, we show how to construct drinking sessions such that the MRPE problem can be solved using any DrPP algorithm. Existing DrPP algorithms, such as, can be implemented in distributed manner, and enjoy nice properties such as fairness and deadlock-freeness, while also guaranteeing collision avoidance when applied to multi-robot planning. To allow more concurrent behavior and to improve the overall performance, we further modify, and derive conditions on the collection of paths such that collisions and deadlocks are guaranteed to be avoided.

The rest of the paper is organized as follows. Section 2 briefly presents related work. Section 3 formally defines the MRPE problem we are interested in solving. A brief summary of the DrPP and an existing solution is presented in Section 4. Section 5 recasts the MRPE problem as a DrPP, and shows that existing methods can be used to solve MRPE problems. Furthermore, this section provides modifications to that allow more concurrent behavior. Section 6 shows that, when fed by the same paths, our algorithm achieves competitive results with the state-of-the-art. Section 7 concludes the paper.

## Related Work

Multi-robot path planning deals with the problem of planning a collection of paths that take a set of robots from their initial position to a goal location without collisions. In this paper, we consider the type of problems where the workspace is partitioned into a set of discrete cells, each of which can hold at most one robot, and time is discretized. Most of the research in this field have been focused on finding optimal or suboptimal paths that minimize either the makespan (last arrival time) or the flowtime (sum of all arrival times). These methods require the duration of each actions to be fixed to show optimality. In real-life, however, robots cannot execute their paths perfectly. They might move slower or faster than intended due to various factors, such as low battery levels, calibration errors and other failures. Methods that deal with such uncertainties, which might lead to collisions or deadlocks if not handled properly, can be divided into two main groups.

In the first group, robots are allowed to replan their paths at run-time. In this case, simpler path planning algorithms can be used, leaving the burden of collision avoidance to the run-time controllers. However, this approach might lead to deadlocks in densely crowded environments. Moreover, when the specifications are complex, changing paths might even lead to violations of the specifications. Therefore, replanning paths on run-time is not always feasible. Alternatively, collisions and deadlocks can be avoided without needing to replan on run-time. For instance, if the synchronization errors can be bounded, and show how to synthesize paths that are collision and deadlock-free. This is achieved by overestimating the positions of robots and treating them as moving obstacles. However, this is a conservative approach as the burden of collision and deadlock avoidance is moved to the offline planning part.

Alternatively, an execution policy can be used to decide when to move, slow down or stop robots on their predefined paths to avoid collisions and deadlocks. Given a collection of paths, which are collision and deadlock free under perfect synchronization, provides a method for robust execution under synchronization errors. This work focuses on how to compute the temporal dependencies between robots and enforce a fixed ordering between each robot pair for all possible conflicts such that collisions and deadlocks are avoided. Same idea is used in, named Minimal Communication Policies (MCP), but the focus is on the planning phase. A delay probability for each agent is used in the planning phase to optimize the expected makespan. This method is later expanded to lifelong missions in warehouse environments. Such a fixed ordering prevents collisions and deadlocks, however, it is limiting as the performance of the multirobot system depends highly on the exact ordering. If one of the robots experiences a failure at run-time and starts moving slowly, it might become the bottleneck of the whole system. In fact, we demonstrate the effects of such a scenario on the system performance and provide numerical results that show the robustness of our method.

When the collection of paths are known a priori, one can also find all possible collision and deadlock configurations, and prevent the system from reaching those. For instance, distributed methods in and find deadlock configurations by abstracting robot paths into an edge-colored directed graph. However, this abstraction step might be conservative. Imagine a long passage which is not wide enough to fit more than one robot, and two robots crossing this passage in the same direction. The entire passage would be abstracted as a single node, and even though robots can enter the passage at the same time and follow each other safely, they would not be allowed to do so. Instead, robots have to wait for the other to clear the entire passage before entering. Moreover, require that no two nodes in the graph are connected by two or more different colored edges. This strong restriction limits the method's applicability to classical multirobot path execution problems where robots move on a graph and the same two nodes might be connected with multiple edges in each direction.

As connectivity and autonomous capabilities of vehicles improve, cooperative intersection management problems draw significant attention from researchers. These problems are similar to MRPE problem as both require coordinating multiple vehicles to prevent collisions and deadlocks. Compared to traditional traffic light-based methods, cooperative intersection management methods offer improved safety, increased traffic flow and lower emissions. We refer the reader to for a recent survey on this topic and main solution approaches. Although they seem similar, the setting of intersection management problems are tailored specifically for the existing road networks, and thus, cannot be easily generalized to MRPE problems where robots/vehicles might be moving in non-structured environments.

Our method is based on reformulating the MRPE problem as a resource allocation problem. There are similar methods such as, which requires a centralized controller, and, which needs cells to be large enough to allow collision-free travel of up to two vehicles, instead of only one. We base our method on the well-known drinking philosopher algorithm. We show that any existing DrPP solution can be used to solve the MRPE problem if drinking sessions are constructed carefully. However, such methods require strong conditions on a collection of paths to hold, and limit the amount of concurrency in the system. To relax the conditions and to improve the performance, we provide a novel approach by taking the special structure of MRPE problems into account. We show that our method is less conservative than the naive approach, and provide numerical results to confirm the theoretical findings. Our approach leads to control policies that can be deployed in a distributed form.

## Problem Definition

We start by providing definitions that are used in the rest of the paper and formally state the problem we are interested in solving. Let a set $\mathcal{R} = {\{ r_{1},\ldots,r_{N}\}}$ of robots share a workspace that is partitioned into set $\mathcal{V}$ of discrete cells. Two robots are said to be in *collision* if they occupy the same cell at the same time. An ordered sequence $\pi = {\{\pi^{0},\pi^{1},\ldots\}}$ of cells, where each $\pi^{t} \in \mathcal{V}$, is called a *path*. The path segment $\{\pi^{t},\pi^{t + 1},\ldots,\pi^{t^{\prime}}\}$ is denoted by $\pi^{t:t^{\prime}}$, and we write $v \in \pi$ if there exists a $t$ such that $\pi^{t} = v$. We assume that a path is given for each robot, and $\pi_{n}$ denotes the path associated with $r_{n}$. We allow paths to contain loops but require them to be finite. We use $\pi_{n}^{end}$ and $curr{(r_{n})}$ to denote the final cell of $\pi_{n}$ and the number of successful transitions completed by $r_{n}$, respectively. We also define ${next{(r_{n})}} \doteq {{curr{(r_{n})}} + 1}$. The motion of each robot is governed by a *control policy*, which issues one of the two commands at every time step: $$ $STOP$ and $$ *$GO$*. The $STOP$ action forces a robot to stay in its current cell. If the $GO$ action is chosen, the robot starts moving. This robot might or might not reach to the next cell within one time step, however, we assume that a robot eventually progresses if $GO$ action is chosen constantly. This non-determinism models the uncertainties in the environment, such as battery levels or noisy sensors/actuators, which might lead to robots moving faster or slower than intended. It can also be due to a higher-level decision maker that forces the robot to stay put for instance as an emergency stop to give way to humans in the workspace. We now formally define the problem we are interested in solving:

### Problem 1

Given a collection $\Pi = {\{\pi_{1},{\ldots\pi_{N}}\}}$ of paths, design a control policy for each robot such that all robots eventually reach their final cells while avoiding collisions.

As stated in the problem definition, we assume that predefined paths are known by every robot prior to the start of execution. There are many control policies that can solve Problem 1. For the sake of performance, policies that allow more concurrent behavior are preferred. In the literature, two metrics are commonly used to measure the performance: *makespan (latest arrival time)* and *flowtime (sum of arrival times)*. Given a set of robots $\mathcal{R} = {\{ r_{1},\ldots,r_{N}\}}$, if robot $r_{n}$ takes $t_{n}$ time steps to reach its final state, makespan and flowtime values are given by $\max_{1 \leq n \leq N}t_{n}$ and $\sum_{n = 1}^{N}t_{n}$, respectively. These values decrease as the amount of concurrency increases. However, it might not be possible to minimize both makespan and flowtime at the same time, and choice of policy might depend on the application.

To solve Problem 1, we propose a method that is based on the well-known drinking philosophers problem introduced by. For the sake of completeness, this problem is explained briefly in Section 4.

## Drinking philosophers problem

The drinking philosophers problem is a generalization of the well-known *dining philosophers problem* proposed by. These problems capture the essence of conflict resolution, where multiple resources must be allocated to multiple processes. Given a set of processes and a set of resources, it is assumed that each resource can be used by at most one process at any given time. In our setting, processes and resources correspond to robots and discrete cells that partition the workspace, respectively. Similar to mutually exclusive use of the resources, any given cell can be occupied by at most one robot to avoid collisions. In the DrPP setting, processes are called *philosophers*, and shared resources are called *bottles*. A philosopher can be in one of the three *states*: $$ *tranquil*, $$ *thirsty*, or $$ *drinking*. A *tranquil* philosopher may stay in this state for an arbitrary period of time or *become thirsty* at any time it wishes. A thirsty philosopher *needs* a non-empty subset of bottles to drink from. This subset, called *drinking session*, is not necessarily fixed, and it could change over time. After acquiring all the bottles in its current drinking session, a thirsty philosopher *starts drinking*. After a finite time, when it no longer needs any bottles, the philosopher goes back to tranquil state. The goal of the designer is to find a set of rules for each philosopher for acquiring and releasing bottles. A desired solution would have the following properties. (i) *Liveness:* A thirsty philosopher eventually starts drinking. In our setting liveness implies that each robot is eventually allowed to move. (ii) *Fairness:* No philosopher is consistently favored over another. In multi-robot setting, fairness indicate that there is no fixed priority order between robots. (iii) *Concurrency:* Any pair of philosophers must be allowed to drink at the same time, as long as they wish to drink from different bottles. Analogously, no robot waits unnecessarily.

We base our method on the DrPP solution of, which is shown in Algorithm 1. This solution ensures liveness, fairness and concurrency. For the sake of completeness, we provide a brief summary of their solution, but refer the reader to for the proof of correctness and additional details.

Each philosopher $p$ has a unique integer $id_{p}$ and keeps track of two non-decreasing integers: session number $s\_num_{p}$ and the highest received session number $max\_rec_{p}$. These integers are used to keep a strict priority order between the philosophers. Conflicts are resolved according to this order, in favor of the philosopher with the higher priority. We say that *philosopher $p$ has higher priority than philosopher* $r$ (denoted *$p \prec r$*) if ${({s\_num_{p}},{id_{p}})} \prec {({s\_num_{r}},{id_{r}})}$ that is ${s\_num_{p}} < {s\_num_{r}}$, or ${s\_num_{p}} = {s\_num_{r}}$ and ${id_{p}} < {id_{r}}$. That is, smaller session number indicates a higher priority, and in the case of identical session numbers, philosopher with the smaller $id$ has the higher priority. Note that the priority order is not fixed as $s\_num$ values change over time.

Philosophers also keep track of several Boolean variables. Let $p$ and $r$ be two philosophers and $b$ be a bottle shared between them. It must be noted that, philosophers $p$ and $r$ can share multiple bottles among each other, but each bottle $b$ is shared by exactly two philosophers. For each bottle $b$ in philosopher $p$'s inventory, we define two booleans $hold_{p}{(b)}$ and $req_{p}{(b)}$, and say that $p$ holds the bottle $b$ (or the request token for the bottle $b$) if the variable $hold_{p}{(b)}$ (or $req_{p}{(b)}$) holds $true$. Similarly, we say that $p$ needs $b$ if $need_{p}{(b)}$ hold $true$. Algorithm 1 ensures mutual exclusiveness, that is, $hold_{p}{(b)}$ and $hold_{r}{(b)}$ (similarly $req_{p}{(b)}$ and $req_{r}{(b)}$) cannot be $true$ at the same time.

Philosophers are initialized such that each philosopher is in tranquil state and $s\_num$ and $max\_rec$ are set to $0$. Bottles and associated request tokens are shared between philosophers such that one philosopher holds the bottle while the other holds the associated request token. Since philosophers are in tranquil state, all $need{(b)}$ variables are initially $false$.

The rules ${R1} - {R6}$ of Algorithm 1 are triggered by events. For example, if a philosopher $p$ wants to drink from a set of bottles $\mathcal{S}$, it needs to *become thirsty* first by executing $R1$. Upon holding all the bottles in $\mathcal{S}$, $R2$ is triggered and $p$ starts drinking. Similarly, $p$ triggers $R4$ when $p$ (i) needs $b$, (ii) does not currently hold $b$, and (iii) holds the associated request token $req_{p}{(b)}$. Then, $p$ requests the bottle from $r$ by sending the message $({req_{b}},{s\_num_{p}},{id_{p}})$. Receiving such a message, triggers $R5$ in $r$. If $r$ does not need $b$ or is thirsty and ${({s\_num_{p}},{id_{p}})} \prec {({s\_num_{r}},{id_{r}})}$, then it sets $hold_{r}{(b)}$ $false$ and sends the bottle to $p$. Sending a bottle is simply done by sending a message to $p$. Upon receiving such a message, $p$ sets $hold_{p}{(b)}$ $true$ by running $R6$. We refer the reader to for more details.

1:R1: becoming_thirsty with session 𝒮
2:for each bottle b ∈ 𝒮 do
8:if holding all needed bottles then
12:R3: becoming_tranquil, honoring deferred requests
13:for each consumed bottle b do
21:if (n e e dp (b) and ¬h o l dp (b) and reqp(b))) then
26:R5: receiving a request from r, resolving a conflict
30:if ((¬needp(b)) or (p is t h i r s t y and (s_numr,idr)&lt;(s_nump,idp))) then
Algorithm 1 Drinking Philosopher Algorithm by

## Multi-robot navigation as a drinking philosophers problem

In this section we recast the multi-robot path execution problem as an instance of drinking philosophers problem. We first show that naive reformulation using existing DrPP solutions leads to conservative control policies. We then provide a solution that is based on Algorithm 1.

We first provide an intuitive explanation for the transformation from MRPE to DrPP, and then present the formal procedure. Given a set $\mathcal{V} = {\{ v_{1},\ldots,v_{|\mathcal{V}|}\}}$ of cells and a collection $\Pi = {\{\pi_{1},{\ldots\pi_{N}}\}}$ of paths, cells that appear in more than one path are called *shared* and the rest are called *free*. We denote the set of all shared cells by $\mathcal{V}_{shared}$. We assume that robots know all paths prior to the start of the execution, hence each robot knows which cells are shared and which ones are free. A shared cell must be occupied at most by one robot at any given time to avoid collisions. One can treat the robots as philosophers and shared cells as bottles to enforce this mutual exclusion requirement. In multi-robot setting, the actions *"moving between two free cells"* or *"occupying a free cell"* of a robot are mapped into the *tranquil* state. Similarly, the *"desire to move into a shared cell"* and *"moving towards or occupying a shared cell* are mapped into the *thirsty* and the *drinking* states, respectively.

Given any two arbitrary robots, we define a bottle for each cell that is visited by both. For example, if the $k^{th}$ cell $v_{k} \in \mathcal{V}$ is visited both by $r_{m}$ and $r_{n}$, we define the bottle $b_{m,n}^{k}$. We denote the set of cells visited by both $r_{m}$ and $r_{n}$ by $\mathcal{V}_{m,n} \doteq {\{ v\mid{{{\exists t_{m}},t_{n}}:{\pi_{m}^{t_{m}} = \pi_{n}^{t_{n}} = v \in \mathcal{V}_{shared}}}\}}$. It must be noted that for a shared cell $v_{k} \in \mathcal{V}_{m,n}$, there exists a single bottle shared between $r_{n}$ and $r_{m}$, and both $b_{m,n}^{k}$ and $b_{n,m}^{k}$ refer to the same object. Multiple bottles would be defined for a shared cell that is visited by more than two robots, where each bottle is shared between exactly two robots. We use $\mathcal{B}_{m,n}$ and $\mathcal{B}_{m}$ to denote the set of all bottles $r_{m}$ shares with $r_{n}$ and with all other robots, respectively. We then define $\mathcal{B}_{m}{(V)}$, the set of bottles associated with the cells in $V \subseteq \mathcal{V}$ that $r_{m}$ share with others such that ${\mathcal{B}_{m}{(V)}} \doteq {\{{b_{m,n}^{k} \in \mathcal{B}_{m}}\mid{v_{k} \in V}\}}$. We use the following example to illustrate the concepts above.

Figure 1: An illustrative example showing partial paths of five robots. Robots, each assigned a unique color/pattern pair, are initialized on free cells. Shared cells are shown as hollow black rectangles. Each path eventually reaches a free cell that is not shown for the sake of simplicity.

### Example 1

In the scenario depicted in Figure 1, the robot $r_{1}$ shares one bottle with $r_{2}$, $\mathcal{B}_{1,2} = {\{ b_{1,2}^{2}\}}$, three bottles with $r_{4}$, $\mathcal{B}_{1,4} = {\{ b_{1,4}^{1},b_{1,4}^{2},b_{1,4}^{4}\}}$, and one bottle with $r_{5}$, $\mathcal{B}_{1,5} = {\{ b_{1,5}^{6}\}}$. The set $\mathcal{B}_{1}$ is the union of these three sets, as $r_{1}$ does not share any bottles with $r_{3}$. Given $V = {\{ v_{2}\}}$, we have ${\mathcal{B}_{1}{(V)}} = {\{ b_{1,2}^{2},b_{1,4}^{2}\}}$.

Bottles are used to indicate the priority order between robots over shared cells. For instance, if $b_{m,n}^{k}$ is currently held by robot $r_{m}$, then *$r_{m}$ has a higher priority than $r_{n}$ over the shared cell $v_{k}$*. Note that, this order is dynamic as bottles are sent back and forth.

Collisions can be prevented simply by the following rule: *"to occupy a shared cell $v_{k}$, the robot $r_{n}$ must be drinking from all the bottles in $B_{n}{(v_{k})}$".* That is, $r_{n}$ must set all the bottles in $B_{n}{(v_{k})}$ needed, and be in drinking state. Upon arriving a free cell, a drinking robot would become tranquil. This rule prevents collisions as $r_{n}$ is the only robot allowed to occupy $v_{k}$ while it is drinking from $B_{n}{(v_{k})}$. However, this rule is not sufficient to ensure that all robots reach their final cells. Without the introduction of further rules, robots might end up in a *deadlock*. We formally define deadlocks as follows:

### Definition 1

A deadlock is any configuration where a subset of robots, which have not reached their final cell, wait cyclically and choose $STOP$ action indefinitely.

To exemplify the insufficiency of the aforementioned rule, imagine the scenario shown in Figure 1. Robots $r_{1}$ and $r_{4}$ traverse the neighboring cells $v_{1}$ and $v_{2}$ in the opposite order. Assume $r_{4}$ is at $v_{4}$ and wants to proceed into $v_{2}$, and, at the same time, $r_{1}$ wants to move into $v_{1}$. Using the aforementioned rule, robots must be drinking from the associated bottles in order to move. Since they wish to drink from different bottles, both robots would be allowed to start drinking. After arriving at $v_{1}$, $r_{1}$ has to start drinking from $B_{1}{(v_{2})}$ in order to progress any further. However, $r_{4}$ is currently drinking from $b_{1,4}^{2} \in {B_{1}{(v_{2})}}$ and cannot stop drinking before leaving $v_{2}$. Similarly, $r_{4}$ cannot progress, as $r_{1}$ cannot release $b_{1,4}^{1}$ before leaving $v_{1}$. Consequently, robots would not be able to make any further progress, and would stay in drinking state forever.

### Naive Formulation

We now show that deadlocks can be avoided by constructing the drinking sessions carefully. For the correctness of DrPP solutions, all drinking sessions must end in finite time. If drinking sessions are set such that *a robot entering a shared cell is clear to move until it reaches a free cell without requiring additional bottles along the way*, then all drinking sessions would end in finite time. That is, if a robot is about to enter a segment which consists of consecutive shared cells, it is required to acquire not only the bottles associated with the first cell, but all the bottles on that segment. To formally state this requirement, let $\mathcal{S}_{n}{(t)}$ denote the drinking session associated with cell $\pi_{n}^{t}$ for robot $r_{n}$. That is, $r_{n}$ should be drinking from all the bottles in $\mathcal{B}_{n}{({\mathcal{S}_{n}{(t)}})}$ to occupy $\pi_{n}^{t}$. Now set

where $\pi_{n}^{k} \in \mathcal{V}_{shared}$ for all $k \in {\lbrack t,t^{\prime}\rbrack}$ and $\pi_{n}^{t^{\prime} + 1} \in \mathcal{V}_{free}$ is the first free cell after $\pi_{n}^{t}$. As long as it is drinking from $\mathcal{S}_{n}{(t)}$, $r_{n}$ has the highest priority among all robots over the cells $\pi_{n}^{t:t^{\prime}}$. Then, $r_{n}$ can constantly choose the action $GO$ until eventually reaching the free cell $\pi_{n}^{t^{\prime} + 1}$ and would stop drinking in finite time. Therefore, any existing DrPP solution, such as, can be used to design the control policies that solve Problem 1 if the drinking sessions are constructed as in.

To illustrate, let us revisit the scenario in Figure 1. To be able to occupy $v_{1}$, $r_{1}$ needs to acquire all bottles in $\mathcal{B}_{1}{(v_{1},v_{2},v_{4},v_{6})}$. Then, $r_{1}$ is free to move all the way up to the last shared state $v_{6}$ without requiring additional bottles. Note however that, once $r_{1}$ reaches $v_{2}$, bottles $\mathcal{B}_{1}{(v_{1})}$ are no longer needed to avoid deadlocks. To allow more concurrency, we introduce a new rule that lets robots to *drop* bottles they no longer need:

R7: upon leaving a shared state

for each $b \notin {\mathcal{B}_{p}\left( {\mathcal{S}_{p}\left( {curr{(p)}} \right)} \right)}$ do

${need_{p}{(b)}}\leftarrow{false}$

$\lbrack{{hold_{p}{(b)}}\leftarrow{{false};{Send{(b)}}}}\rbrack$

Without $R7$, if $r_{1}$ is at $v_{2}$, $r_{2}$ would need to wait until $r_{1}$ leaves $v_{6}$. With $R7$, $r_{1}$ would release $b_{1,2}^{2}$ upon leaving $v_{2}$. Then, $r_{2}$ can move to $v_{2}$, while $r_{1}$ is at $v_{4}$.

However, the control policies resulting from the aforementioned approach are conservative and lead to poor performance in terms of both makespan and flowtime. To illustrate using the scenario shown in Figure 1, if $r_{1}$ is currently at $v_{1}$, $r_{5}$ cannot move into $v_{6}$ since $b_{1,5}^{6}$ is held by $r_{1}$. This is a conservative action as $r_{5}$ cannot cause a deadlock by moving to $v_{6}$, as it moves to a free cell right after.

We have seen that *small* drinking sessions might lead to deadlocks, and *large* drinking sessions might lead to unnecessary waits, and thus, bad performance. Our goal is to construct drinking sessions *as small as possible* such that we can guarantee deadlock-freeness while allowing as much concurrent behavior as possible. To achieve this goal, we introduce a new drinking state and rules regarding its operation.

### New Drinking State and New Rules

In this subsection, we propose a new drinking state for the philosophers, namely *insatiable*. This new state is used when robot moves from a shared cell to another shared cell. We also add an additional rule $R8$ regarding this new state and modify the existing rules $R4$ and $R5$ of Algorithm 1 as $R^{\prime}4$ and $R^{\prime}5$, respectively:

if $\left( need_{p}{(b)} \right.$ and $\neg{hold_{p}{(b)}}$ and $\left. req_{p}{(b)} \right)$ then

${req_{p}{(b)}}\leftarrow{false}$

$Send{({req_{b}},{s\_num_{p}},{id_{p}},{ds_{p}})}$

R'5: *receiving a request from $r$, and resolving a conflict*

upon reception of $({req_{b}},{s\_num_{r}},{id_{r}},{ds_{r}})$ do

${{req_{p}{(b)}}\leftarrow{true}};$

${max\_rec_{p}}\leftarrow{\max{({max\_rec_{p}},{s\_num_{r}})}}$

if $\left( {} \right.$ or $$ or $\left. {} \right)$

$\lbrack{{hold_{p}{(b)}}\leftarrow{{false};{Send{(b)}}}}\rbrack$

$\left( ds_{r} \right.$ is $thirsty$ and $\left. {(s\_ num_{r},id_{r})} \prec {(s\_ num_{p},id_{p})} \right)$ or,

$p$ is $insatiable$ with $\left( {\mathcal{B}_{p}{(\mathcal{S}_{1})}},{\mathcal{B}_{p}{(\mathcal{S}_{2})}} \right)$ and,

$b \notin {\mathcal{B}_{p}{(\mathcal{S}_{1})}}$ and,

${({s\_num_{r}},{id_{r}})} \prec {({s\_num_{p}},{id_{p}})}$.

R8: becoming insatiable with tuple $\left( {\mathcal{B}_{p}{(\mathcal{S}_{1})}},{\mathcal{B}_{p}{(\mathcal{S}_{2})}} \right)$

for each bottle $b \in {\mathcal{B}_{p}{(\mathcal{S}_{2})}}$ do

${need_{p}{(b)}}\leftarrow{true}$

if not holding all bottles in $\mathcal{B}_{p}{({\mathcal{S}_{1} \cup \mathcal{S}_{2}})}$ then

The message structure used for requesting bottles is modified in $R^{\prime}4$ and now includes the drinking state $ds_{p} \in {\{ tranquil}$, $thirsty$, $drinking$, $insatiable\}$ of the sender. This information is used in conjunction with $id$ and $s\_num$ by the receiver to decide whether to grant or defer the request.

In the naive formulation, drinking sessions are set such that a robot entering a shared cell is free to move until it reaches a free cell, without requiring additional bottles along the way. The insatiable state is intended to soften this constraint. Assume robot $r_{n}$ wants to move to shared cell $\pi_{n}^{t}$, and the first free cell after $\pi_{n}^{t}$ is $\pi_{n}^{t^{\prime} + 1}$ for some arbitrary $t^{\prime} > t$, all the cells in between are shared. If $r_{n}$ enters the first shared cell without acquiring all the bottles until $\pi_{n}^{t^{\prime} + 1}$, it would need to acquire those bottles at some point along the way. If $r_{n}$ becomes thirsty to acquire those bottles, it risks losing the bottles it currently holds. If another robot $r_{m}$ with a higher priority needs and receives the bottles associated with the cell $r_{n}$ currently occupies, two robots might collide.

Insatiable state allows a robot to request new bottles without risking to lose any of the bottles it currently holds. In this state, the robot does not hold all the bottles it needs to start drinking, similar to thirsty state. The difference between two states is that, an insatiable philosopher always has a higher priority than a thirsty philosopher regardless of their session numbers. Moreover, an insatiable philosopher does not release under any circumstance any of the bottles needed to occupy the cell it is currently in.

In other words, if $p$ is insatiable with $(\mathcal{B}_{1},\mathcal{B}_{2})$, then $p$ already has all bottles in $\mathcal{B}_{1}$ and cannot release them. Moreover, $p$ is trying to acquire the bottles in $\mathcal{B}_{2}$ to start drinking, which might be released, if a robot with higher priority requests them. An insatiable robot always has a higher priority than a thirsty robot. In case of identical drinking states, $\prec$ relation is used to resolve the priority order.

The insatiable state and the rules regarding its operation might lead to deadlocks without careful construction of drinking sessions. We now explain how to construct drinking sessions to avoid deadlocks.

### Constructing Drinking Sessions

To compute drinking sessions, we first need to define a new concept called *Path-Graph*:

### Definition 2

The Path-Graph induced by the collection $\Pi = {\{\pi_{1},{\ldots\pi_{N}}\}}$ of paths is a directed edge-colored multigraph $G_{\Pi} = {(\mathcal{V},\mathcal{E}_{\Pi},\mathcal{C})}$ where $\mathcal{V}$ is a set of nodes, one per each cell in $\Pi$, $\mathcal{E}_{\Pi} = {\{{(\pi_{n}^{t},c_{n},\pi_{n}^{t + 1})}\mid{\pi_{n} \in \Pi}\}}$ is the set of edges, representing transitions of each path, and $\mathcal{C} = {\{ c_{1},\ldots,c_{N}\}}$ is the set of colors, one per each path (i.e., one per each robot).

A Path-Graph is a graphical representation of a collection of paths, overlayed on top of each other. The nodes of this graph correspond to discrete cells that partition the workspace, and edges illustrate the transitions between them. Color coding of edges indicate which robot is responsible for a particular transition. In other words, if $\pi_{n}$ has a transition from $u$ to $v$, then there exists a $c_{n}$ colored edge from $u$ to $v$ in $G_{\Pi}$, i.e., ${(u,c_{n},v)} \in \mathcal{E}_{\Pi}$.

Path-Graphs are useful to detect possible deadlock configurations. Intuitively, deadlocks occur when a subset of robots wait cyclically for each other. We first show that such configurations correspond to a *rainbow cycle* in the corresponding Path-Graph. A rainbow cycle is a closed walk where no color is repeated. Let $\Pi$ be a collection of paths and $G_{\Pi}$ be the Path-Graph induced by it. Assume that a subset ${\{ r_{1},\ldots,r_{K}\}} \subseteq \mathcal{R}$ of robots are in a deadlock configuration such that $r_{n}$ waits for $r_{n + 1}$ for all $n \in {\{ 1,\ldots,K\}}$ where $r_{K + 1} = r_{1}$. That is, $r_{n}$ cannot move any further, because it wants to move to the cell that is currently occupied by $r_{n + 1}$. Let $v_{n}$ denote the current cell of $r_{n}$. Since $r_{n}$ wants to move from $v_{n}$ to $v_{n + 1}$, we have $e_{n} = {(v_{n},c_{n},v_{n + 1})} \in \mathcal{E}_{\Pi}$. Then, $\omega = {\{{(v_{1},c_{1},v_{2})},\ldots,{(v_{K},c_{K},v_{1})}\}}$ is a rainbow cycle of $G_{\Pi}$. For instance, there are two rainbow cycles in Figure 1: $\omega_{1} = {\{{(v_{1},c_{1},v_{2})},{(v_{2},c_{4},v_{1})}\}}$ and $\omega_{2} = {\{{(v_{2},c_{1},v_{4})},{(v_{4},c_{4},v_{2})}\}}$.

The first idea that follows from this observation is to limit the number of robots in each rainbow cycle to avoid deadlocks. However, this is not enough as rainbow cycles can intersect with each other and robots might end up waiting for each other to avoid eventual deadlocks. For instance, in the scenario illustrated in Figure 1, let $r_{1}$ and $r_{4}$ be at $v_{1}$ and $v_{4}$, respectively. The number of robots in each rainbow cycles is limited to one, nonetheless, this configuration will eventually lead to a deadlock.

Input GΠ return ${\overset{\sim}{G}}_{\Pi}$
3: expand ∼ such that (u,u) ∈ ∼
5:𝒲← find_rainbow_cycles(GΠ)
7: ${\overset{\sim}{G}}_{\Pi}\leftarrow G_{\Pi}$
12: expand ∼ such that (u,v) ∈ ∼
15: ${\overset{\sim}{G}}_{\Pi}\leftarrow{find\_quotient{(G_{\Pi}, \sim )}}$
16: $find\_equivalence\_classes{({\overset{\sim}{G}}_{\Pi})}$
Algorithm 2 find_equivalence_classes

We propose Algorithm 2 to construct the drinking sessions, which are used to prevent such deadlocks. Given a collection $\Pi$ of paths let $G_{\Pi} = {(\mathcal{V},\mathcal{E}_{\Pi},\mathcal{C})}$ denote its Path-Graph. We first define equivalence relation $\sim$ on $\mathcal{V}$ such that each node is equivalent only to itself. We then find all rainbow cycles in $G_{\Pi}$. Let $\mathcal{W}$ denote the set of all rainbow cycles. For each rainbow cycle $W \in \mathcal{W}$, we expand the equivalence relation $\sim$ by declaring all nodes in $W$ to be equivalent. That is, if $u$ and $v$ are two nodes of the rainbow cycle $W$, we add the pair $(u,v)$ to the equivalence relation $\sim$. Note that, due to transitivity of the equivalence relation, nodes of two intersecting rainbow cycles would belong to the same equivalence class. The relation $\sim$ partitions $\mathcal{V}$ by grouping the intersecting rainbow cycles together. We then find the quotient set $\left. \mathcal{V}/ \sim \right.$ and define a new graph ${\overset{\sim}{G}}_{\Pi} = \left. (\mathcal{V}/ \sim,{\overset{\sim}{\mathcal{E}}}_{\Pi},\mathcal{C}) \right.$ where ${({\lbrack u\rbrack},c_{m},{\lbrack v\rbrack})} \in {\overset{\sim}{\mathcal{E}}}_{\Pi}$ if ${\lbrack u\rbrack} \neq {\lbrack v\rbrack}$, and there exists $\alpha \in {\lbrack u\rbrack}$, $\beta \in {\lbrack v\rbrack}$ such that ${(\alpha,c_{m},\beta)} \in \mathcal{E}_{\Pi}$. That is, we create a node for each equivalence class. We then add a $c_{m}$ colored edge to ${\overset{\sim}{G}}_{\Pi}$ between the nodes corresponding $\lbrack u\rbrack$ and $\lbrack v\rbrack$ if there is a $c_{m}$ colored edge in $G_{\Pi}$ from a node in $\lbrack u\rbrack$ to a node in $\lbrack v\rbrack$. We repeat the same process with ${\overset{\sim}{G}}_{\Pi}$ in a recursive manner until no more rainbow cycles are found.

### Proposition 1

Algorithm 2 terminates in finite steps.

### Proof 5.1

Since all paths are finite, the number of nodes in the Path-Graph $G_{\Pi}$, $|\mathcal{V}|$, is finite. At each iteration, Algorithm 2 either finds a new graph ${\overset{\sim}{G}}_{\Pi}$ which has a smaller number of nodes, or returns $G_{\Pi}$. Therefore, Algorithm 2 is guaranteed to terminate at most in $|\mathcal{V}|$ steps.

### Remark 5.2

Algorithm 2 needs to find all rainbow cycles of an edge-colored multi-graph at each iteration, which can be done in the following way. Given $G = {(\mathcal{V},\mathcal{E},\mathcal{C})}$, obtain $E \subseteq {\mathcal{V} \times \mathcal{V}}$ from $\mathcal{E}$ by removing the coloring and replacing multiple edges between the same two nodes with a single edge. Then, find all simple cycles in the graph $G^{\prime} = {(\mathcal{V},E)}$. Finally, check if these cycles can be colored as a rainbow cycle.

Finding all simple cycles in a directed graph is time bounded by $\mathcal{O}{({{({{|V|} + {|E|}})}{({C + 1})}})}$ and space bounded by $\mathcal{O}{({(|V| + |E|)}}$, where $C$ is the number of cycles. Although the number of cycles in a directed graph grows, in the worst-case, exponentially with the number of nodes, this operation can be done efficiently in practice. Deciding if a cycle can be rainbow colored can be posed as an exact set cover problem, which is NP-complete. This is essentially due to the fact that, in the worst-case, the number of cycles in a multi-graph can be exponential in the number of colors compared to the corresponding directed graph. However, the number of nodes decrease at each iteration of Algorithm 2, making computations easier. Moreover, while the worst-case complexity is high, these operations can usually be performed efficiently in practice.

When the Algorithm 2 finds the fixed point, we set

where $\mathcal{S}_{n}{(t)}$ is defined as in and $\lbrack\pi_{n}^{t}\rbrack$ is the equivalence class of $\pi_{n}^{t}$. That is, $r_{n}$ must be drinking from all the bottles in $\mathcal{B}_{n}{({{\overset{\sim}{\mathcal{S}}}_{n}{(t)}})}$ to be able to occupy $\pi_{n}^{t}$.

We now revisit the example in Figure 1.

### Example 5.3

Let $G_{\Pi}$ be given as in Figure 1. After the first recursion of Algorithm 2, ${\lbrack v_{1}\rbrack} = {\{ v_{1},v_{2},v_{4}\}}$ and ${\lbrack v_{i}\rbrack} = {\{ v_{i}\}}$ for $i \in {\{ 3,5,6\}}$. After the second recursion, ${\lbrack v_{1}\rbrack} = {\{ v_{1},v_{2},v_{3},v_{4},v_{5}\}}$ and ${\lbrack v_{6}\rbrack} = {\{ v_{6}\}}$. No rainbow cycles are found after the second recursion, therefore, ${{\overset{\sim}{\mathcal{S}}}_{1}{}} = {{\{ v_{1},v_{2},v_{4},v_{6}\}} \cap {\{ v_{1},v_{2},v_{3},v_{4},v_{5}\}}} = {\{ v_{1},v_{2},v_{4}\}}$.

While all cells except $v_{6}$ get merged into a single cell in Figure 1, constructing drinking sessions as in allows multiple robots to simultaneously occupy $v_{1} - v_{5}$. For instance, the drinking sessions of $r_{1}$ and $r_{3}$ are disconnected since they have no common cells. Therefore, $r_{1}$ and $r_{3}$ can enter cells $v_{1}$ and $v_{3}$, respectively, at the same time. Similarly, such drinking sessions also allow $r_{1}$, $r_{2}$ and $r_{3}$ to simultaneously occupy cells $v_{4}$, $v_{2}$ and $v_{5}$, respectively. Even in this small example, we can see the benefit of using Eq. instead of Eq.. The modification allows $r_{1}$ and $r_{5}$ to be at $v_{4}$ and $v_{6}$, respectively, while it was not possible with the naive formulation.

### Remark 5.4

Sessions constructed by are always contained in the sessions constructed by. That is, when drinking sessions are found as in, robots would need fewer bottles to move, and the resulting control policies would be more permissive.

We now propose a control policy that prevents collisions and deadlocks when drinking sessions are constructed as in.

### Control Strategy

We propose Algorithm 3 as a control policy to solve Problem 1. In order to implement Algorithm 3 in a distributed manner, we require the communication graph to be identical to the resource dependency graph. That is, if two robots visit a common cell, there must be a communication channel between them. We also assume that messages from one robot to another are received in the order that they are sent. We now briefly explain the flow of the control policy, which is illustrated in Figure 2, and then provide more details.

Robots are initialized as follows. If robot $r_{n}$ starts at a shared cell, all bottles in its initial drinking session are given to $r_{n}$ and the related request tokens are given to the corresponding robots. To ensure bottles can be assigned in this way, we require that the initial drinking sessions are disjoint. Robots with shared initial cells are then initialized in drinking state, which is possible since they hold all the required bottles, and the remaining robots are initialized in tranquil state.

If the final cell is reached, $STOP$ action is chosen as the robot accomplished its task. Otherwise, if a robot is in either tranquil or drinking state, the control policy chooses the action $GO$ until the robot reaches to the next cell. When a robot moves from a free cell to a shared cell, it first becomes thirsty and the control policy issues the action $STOP$ until the robot starts drinking. When moving between shared cells, a robot becomes insatiable if it needs to acquire additional bottles, and $STOP$ action is chosen until the robot starts drinking again. If a robot $r_{n}$ is leaving a shared cell where another robot $r_{m}$'s path terminates, for the last time, $r_{n}$ sends $r_{m}$ a *cleared* message. When a robot's path terminates at a shared cell, it must be careful not to arrive early and block others from progressing. Therefore, when a robot is about to move to a segment of consecutive shared cells which includes its final cell, it needs to wait for others to clear its final cell.

All robots are initialized as previously described. Let $r_{n}$ be an arbitrary robot. Lines $1 - 2$ of Algorithm 3 ensure that $r_{n}$ does not move after reaching its final cell. Otherwise, let $\pi_{n}^{t}$ denote the next cell on $r_{n}$'s path. If $\pi_{n}^{t}$ is a free cell, the control policy chooses the $GO$ action until the robot reaches $\pi_{n}^{t + 1}$ (lines $5 - 8$). $r_{n}$ goes back to tranquil state if it was drinking and sends a *cleared* message to a corresponding robot $r_{m}$ if (i) $\pi_{n}^{t - 1}$ was the terminal cell for $r_{m}$ and (ii) $\pi_{n}^{t - 1}$ will not be visited by $r_{n}$ again in the future (lines $9 - 13$). When $\pi_{n}^{t}$ is a shared cell, there are two possible options: (i) If there is no free cell between the next cell and the final cell of $r_{n}$, i.e., $\pi_{n}^{end} \in {\mathcal{S}_{n}{(t)}}$ where $\mathcal{S}_{n}{(t)}$ is defined as in, the robot must wait for all other robots to clear this cell (lines $15 - 18$). This wait is needed, otherwise, $r_{n}$ might block others by arriving and staying indefinitely at its final cell. When all others clear its final state, $r_{n}$ can start moving again. (ii) If the final cell is not included in the drinking session, $r_{n}$ checks its drinking state. If tranquil, $r_{n}$ becomes thirsty with the drinking session ${\overset{\sim}{\mathcal{S}}}_{n}{(t)}$ (lines $19 - 20$). If drinking, $r_{n}$ becomes insatiable with $\left( {\mathcal{B}_{n}\left( {{\overset{\sim}{\mathcal{S}}}_{n}{(t)}} \right)},{\mathcal{B}_{n}\left( {{\overset{\sim}{\mathcal{S}}}_{n}{({t + 1})}} \right)} \right)$ (lines $21 - 22$). Then, the robot waits until it starts drinking to move to the next cell (lines $24 - 26$). When the robot starts drinking, it is allowed to move until it reaches $\pi_{n}^{t}$ (lines $27 - 29$). Upon reaching $\pi_{n}^{t}$, the robot sends cleared signal if needed (line $31$), as previously explained.

We now show the correctness of Algorithm 3.

### Theorem 5.5

Given an instance of Problem 1, using Algorithm 3 as a control policy solves Problem 1 if

Initial drinking sessions are disjoint for each robot, i.e., ${{{\overset{\sim}{\mathcal{S}}}_{m}{}} \cap {{\overset{\sim}{\mathcal{S}}}_{n}{}}} = \varnothing$ for all $m \neq n$ and

Final cells of each robot belong to a different equivalence class, i.e., ${(\pi_{m}^{end},\pi_{n}^{end})} \notin \sim$ for any $m \neq n$ where $\sim$ is computed according to Algorithm 2, and

There exists at least one free cell in each $\pi_{n}$.

The proof of Theorem 5.5 can be found in the Appendix.

The first condition in Theorem 5.5 ensures that robots can be initialized correctly. Imagine a robot $r_{n}$ whose path starts with a shared cell. If $r_{n}$ is initialized in tranquil state, it will momentarily violate the requirement that *"$r_{n}$ must be drinking from all the bottles in $\mathcal{B}_{n}{({{\overset{\sim}{\mathcal{S}}}_{n}{}})}$ to be able to occupy $\pi_{n}^{0}$"*. If initial drinking sessions are disjoint for each robot, $r_{n}$ can immediately start drinking. Therefore, all such robots can be initialized in drinking state if the first condition is satisfied. The second condition is required so that robots whose paths end in a shared cell do not block others from progressing by reaching their final cells early. The last condition is required otherwise and cannot be satisfied at the same time.

### Remark 5.6

the Naive formulation explained in Section 5.1 also solves Problem 1. However, as mentioned in Remark 5.4, drinking sessions constructed by always contain sessions constructed by, that is, ${\mathcal{S}_{n}{(t)}} \supseteq {{\overset{\sim}{\mathcal{S}}}_{n}{(t)}}$. Therefore, condition of Theorem 5.5 becomes more restrictive for the Naive implementation.

Figure 2: Flowchart of the control policy explained in Algorithm 3.

1:if rn.is_final_cell_reached then
12: send_cleared_message_if_needed()
19: else if rn.is_tranquil then
20: rn.get_thirsty(${\overset{\sim}{\mathcal{S}}}_{n}{(t)}$)
21: else if rn.is_drinking then
22: rn.get_insatiable($\mathcal{B}_{n}{({{\overset{\sim}{\mathcal{S}}}_{n}{(t)}},{{\overset{\sim}{\mathcal{S}}}_{n}{({t + 1})}})}$)
31: send_cleared_message_if_needed()
Algorithm 3 Control policy for rn

### Remark 5.7

The control policy given in Algorithm 3 satisfies liveness, fairness and concurrency properties. The liveness proof is shown in Theorem 5.5, and fairness and concurrency properties follows directly from.

## Results

In this section, we compare our *Rainbow Cycle* based method explained in Sections 5.2-5.4, denoted *DrPP-RC*, with other path execution methods using identical paths. Firstly, we compare DrPP-RC with the *Naive* method, denoted *DrPP-N*, which is explained in Section 5.1. This comparison demonstrates the performance improvement that results from the addition of the new drinking state. As stated in Remark 5.4, DrPP-RC uses smaller drinking sessions, and allows more concurrency. We also provide results for DrPP-N *without* $R7$. This rule is an addition to the original DrPP solution of and exploits the structure of the multi-robot path execution problem by allowing robots to drop bottles while in drinking state.

We further compare DrPP-RC with the *Minimal Communication Policy* of, denoted *MCP*, which prevents collisions and deadlocks by maintaining a fixed visiting order for each cell. A robot is allowed to enter a cell only if all the other robots, which are planned to visit the said cell earlier, have already visited and left the said state. It is shown that, under mild conditions on the collection of the paths, keeping this fixed order prevents collisions and deadlocks. We refer the reader to for more details.

We also note that, conditions required by are too restrictive for the majority of the examples provided in this section. That is, some nodes in Path-Graph are connected by more than one colored edge, hence cannot be used. On the other hand, merging shared cells as in Equation generates a quotient graph that satisfies the required conditions. Then, the performance of is identical to that of DrPP-N without $R7$. However, as Section 6.1 shows, cannot still solve all problems solved by DrPP-RC, and for the problems it can solve, it is significantly outperformed by both DrPP-RC and DrPP-N.

To capture the uncertainty in the robot motions, each robot is assigned a *delay probability*. When the action $GO$ is chosen, a robot either stays in its current cell with this probability, or completes its transition to the next cell before the next time step leading to asynchrony between robots' motion. Our implementation can be accessed from https://github.com/sahiny/philosophers.

### Randomly Generated Examples

Figure 3: Randomly generated example, denoted random1, consisting of 35 robots on a 30 × 30 grid with 10% blocked cells, which are shown in black. The path of each robot is shown with a unique color where the solid and hollow circles represent the initial and final cells, respectively. Free (i.e., used by a single robot) and shared (i.e., visited by more than one robot) cells are painted green and red, respectively. Among the cells that are visited by at least one robot, 44% (217/496) are shared cells, and a robot’s path consists of 65% shared cells on average. These statistics are similar for other random examples.

There are $10$ MRPE instances in, labelled random 1-10, where $35$ robots navigate in 4-connected grids of size $30 \times 30$. In each example, randomly generated obstacles block $10\%$ of the cells, and robots are assigned random but unique initial and final locations. The first of these randomly generated examples can be seen Figure 3. All control policies use the same paths generated by the Approximate Minimization in Expectation algorithm of. Delay probabilities of robots are sampled from the range $(0,{1 - {1/t_{max}}})$. Note that, higher delay probabilities can be sampled as $t_{max}$ increase, resulting in *slow moving* robots. Figure 4 reports the makespan and flowtime statistics averaged over 1000 runs for varying $t_{max}$ values. The delay probabilities are sampled randomly for each run, but kept identical over different control policies. As expected, both makespan and flowtime statistics increase with $t_{max}$, as higher delay probabilities result in slower robots. An illustrative run of the DrPP-RC algorithm for $t_{max} = 2$ and environment random1 can be seen from https://youtu.be/tht4ydW5iJA.

From Figure 4, we first observe that the addition of $R7$ improves the flowtime performance of DrPP-N significantly, while its effect on makespan is neglible. Secondly, we observe that DrPP-RC always performs better than DrPP-N. This is expected as drinking sessions for DrPP-N, which are computed by, are always larger than the ones of DrPP-RC, which are computed by. That is, robots using DrPP-N need more bottles to move, and thus, wait more. Moreover, DrPP-N requires stronger assumptions to hold for a collection of paths. For instance, only one of the ten random examples (random7) satisfy the the assumptions in Theorem 5.5 for DrPP-N. The number of instances that satisfy the assumptions increase to four for DrPP-RC (random 3, 4, 7, 10). The random1 example illustrated in Figure 3 originally violates the assumptions, but this is fixed for both drinking based methods by adding a single cell into a robot's path. We here note that, the set of valid paths for MCP and DrPP algorithms are non-comparable. There are paths that satisfy the assumptions of one algorithm and violate the other, and vice versa.

We also observe that makespan values are quite similar for DrPP-RC and MCP methods, although MCP often performs slightly better in this regard. Given a collection of paths, the makespan is largely determined by the *"slowest"* robot, a robot with a long path and/or a high delay probability, regardless of the control policies. Therefore, makespan statistics do not necessarily reflect the amount of concurrency allowed by the control policies. Ideally, in the case of a slow moving robot, we want the control policies not to stop or slow down other robots unnecessarily, but to allow them move freely. The flowtime statistics reflect these properties better. From Figure 4, we see that flowtime values increase more significantly with $t_{max}$ for MCP, compared to DrPP-RC. This trend can be explained with how priority orders are maintained in each of the algorithms. As the delay probabilities increase, there is more uncertainty in the motion of robots. MCP keeps a fixed priority order between robots, which might lead to robots waiting for each other unnecessarily. On the other hand, DrPP-RC dynamically adjusts this order, which leads to more concurrent behavior, hence the smaller flowtime values. Section 6.2 illustrates this phenomenon with a simple example.

Figure 4: Makespan and flowtime statistics averaged over 1000 runs for the randomly generated environments under varying tm a x values. DrPP based method cannot be used in environments where the collection of paths violate the conditions in Theorem 5.5. DrPP-N and DrPP-RC methods can solve 2 and 5 out of 10 randomly generated instances, respectively.

Figure 5: A simple example to show effects of a slow moving robot. Robots r1, r2 and r3 are colored in red, blue and green, respectively. Initial and final cells of the robots are marked with solid and hollow circles of their unique color, respectively.

### Makespan versus Flowtime

As mentioned earlier, assumes that delay probabilities are known a priori, and computes paths to minimize the expected makespan. Once the paths are computed, the priority order between robots is fixed to ensure MCP policies are collision and deadlock-free. We now provide a simple example to illustrate the effect of using inaccurate delay probabilities in the path planning process. Imagine $3$ robots are sharing a $10$ by $10$ grid environment as shown in Figure 5. Assume that the delay probabilites for robots $r_{1}$, $r_{2}$ and $r_{3}$ are known to be $\{ 0,0.4,0.8\}$, respectively. If we compute paths to minimize the expected makespan, resulting paths are straight lines for each robot. Paths $\pi_{1}$ and $\pi_{2}$ intersect at a single cell, for which $r_{1}$ has a priority over $r_{2}$. Similarly $\pi_{2}$ and $\pi_{3}$ also intersect at a single cell, for which $r_{2}$ has a priority over $r_{3}$. We run this example using inaccurate delay probabilities $\{ 0.8,0.4,0\}$ to see how the makespan and flowtime statistics are affected.

Over $1000$ runs, makespan values are found to be $48.30$ and $45.77$ steps for MCP and DrPP-RC implementations, respectively. The makespan values are close because of the slow moving $r_{1}$, which becomes the bottleneck of the system. Therefore, it is not possible to improve the makespan statistics by employing different control policies. However, the flowtime statistics are found as $128.78$ and $77.78$ steps for MCP and DrPP-RC implementations, respectively. Significant difference is the result of how a slow moving robot is treated by each policy. For the MCP implementation, $r_{2}$ (resp. $r_{3}$) needs to wait for $r_{1}$ (resp. $r_{2}$) unnecessarily, since the priority order is fixed at the path planning phase. On the other hand, DrPP-RC implementation allows robots to modify the priority order at run-time, resulting in improved flowtime statistics.

Figure 6: Illustration of a warehouse example on a 22 × 57 grid. Blocked cells are shown in black. Initial and final cells are marked with a solid and a hollow circle of a unique color, respectively.

### Warehouse Example

We also compare the performance of the control policies in a more structured warehouse-like environment. This warehouse example is taken from, and it has $35$ robots as shown in Figure 6. The makespan and flowtime statistics are reported in Figure 7, which are averaged over 1000 runs for varying $t_{max}$ values. Due to stronger assumptions on the collection of paths, DrPP-N is not able to handle this example. Similarly, the conditions required by are too restrictive, hence it cannot solve this problem. Although paths can be altered to allow to be used, this requires each aisle to be abstracted as one discrete cell, and limits the number of robots in each aisle to at most one. As a result, the performance of would be significantly worse compared to both DrPP-RC and MCP, no matter how paths are generated.

Similar to Section 6.1, we observe that makespan values are better for MCP, but DrPP-RC scales better with $t_{max}$ for flowtime statistics. Upon closer inspection, we see that robots moving in narrow corridors in opposite directions lead to many rainbow cycles. By enforcing a one-way policy in each corridor, similar to, many of these rainbow cycles can be eliminated and the performance of our method can be improved. Indeed, Figure 7 reports the results when paths are modified such that no horizontal corridor has robots moving in opposing directions.

We further use the same warehouse example to demonstrate how DrPP-RC can be used in conjunction with a higher-level emergency stopping algorithm. In practical examples, robots carry shelves around the warehouse, which might make it dangerous for humans to work in the same space. To guarantee safety for humans, we require robots to stop and give way if there is a human in a predefined radius. As the video in https://youtu.be/gVSKs1iKsQw shows, DrPP-RC guarantees that deadlocks and collisions are avoided in such cases.

Figure 7: Makespan and flowtime statistics averaged over 1000 runs for the warehouse environment under varying tm a x values. Dashed lines show the improvement obtained by modifying the paths to decrease the number of rainbow cycles. DrPP-N cannot solve this instance as the collection of paths violate the conditions in Theorem 5.5.

## Conclusions

In this paper, we presented a method to solve the multi-robot path execution (MRPE) problem. Our method is based on a reformulation of the MRPE problem as an instance of drinking philosophers problem (DrPP). We showed that the existing solutions to the DrPP can be used to solve instances of MRPE problems if drinking sessions are constructed carefully. However, such an approach leads to conservative control policies. To improve the system performance, we provided a less conservative approach where we modified an existing DrPP solution. We provided conditions under which our control policies are shown to be collision and deadlock-free. We further demonstrated the efficacy of this method by comparing it with existing work. We observed that our method provides similar makespan performance to while outperforming it in flowtime statistics, especially as uncertainty in robots' motion increase. This improvement can be explained mainly by our method's ability to change the priority order between robots during run-time, as opposed to keeping a fixed order.

Our current method and derived conditions that guarantee collision and deadlock-freeness are limited to the multi-robot path execution problem where robot paths are assumed to be fixed a priori. Using such conditions to guarantee deadlock-freeness of replanning approaches or designing life-long planning algorithms with similar guarantees are interesting directions for future research. We are also interested in finding looser conditions that guarantee collision and deadlock-freeness, as the current conditions are sufficient but might not be necessary.

We thank Hang Ma from Simon Fraser University and Sven Koenig from University of Southern California for sharing their code for MCP implementation in with us. We also thank Ruya Karagulle for pointing out typos in Theorem 1. The last but not least, we thank the reviewers for their valuable comments and suggestions, which improved the clarity and the presentation of the paper greatly. This work is supported in part by ONR grant N00014-18-1-2501, NSF grant ECCS-1553873, and an Early Career Faculty grant from NASA's Space Technology Research Grants Program.
