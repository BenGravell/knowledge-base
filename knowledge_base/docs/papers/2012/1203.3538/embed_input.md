<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RAPID: A Reachable Anytime Planner for Imprecisely-Sensed Domains

Topics include Partially observable planning, Factored dynamics, POMDPs, Anytime planning, State envelopes, Tutoring systems, Reachability analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents RAPID, an anytime planner for structured POMDPs that first builds a compact envelope of states reachable under the fully observable optimal policy, then expands that envelope as computation permits. The paper's key value is exploiting topological structure inside factored dynamics, allowing a tutoring-scale domain with enormous flat state space to get useful partially observable plans without enumerating the full model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the intractability of generic optimal partially observable Markov decision process planning, there exist important problems that have highly structured models. Previous researchers have used this insight to construct more efficient algorithms for factored domains, and for domains with topological structure in the flat state dynamics model. In our work, motivated by findings from the education community relevant to automated tutoring, we consider problems that exhibit a form of topological structure in the factored dynamics model. Our Reachable Anytime Planner for Imprecisely-sensed Domains (RAPID) leverages this structure to efficiently compute a good initial envelope of reachable states under the optimal MDP policy in time linear in the number of state variables. RAPID performs partially-observable planning over the limited envelope of states, and slowly expands the state space considered as time allows. RAPID performs well on a large tutoring-inspired problem simulation with 122 state variables, corresponding to a flat state space of over 10^30 states.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

One of the key questions in artificial intelligence research is how to make good decisions in large, stochastic, partially observable environments. Though generic optimal planning for finite-horizon partially observable Markov decision processes (POMDPs) is known to be PSPACEcomplete, fortunately, some important POMDP domains have highly structured models. This insight has been used by previous researchers to design more efficient POMDP algorithms that leverage different types of structure. Focussing on domains that exhibit factored structure has led to POMDP planners that solve some of the largest POMDP problems in the litera-

<!-- chunk {"id": "body-0005", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

Computer Science Department University of California, Berkeley Berkeley, CA ture, including a hand washing assistance program and a RoboCup rescue task. Other recent work has focused on domains where the flat state dynamics model limits the possible backtracking to earlier states, and showed that planning can be performed more efficiently when this topological structure is present.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

In this paper we focus on problems exhibiting both factored structure and a form of topological structure, and demonstrate that we can leverage these properties to scale to very large domains. Such properties are common in a number of important applications ranging from tutoring to dialogue systems. For example, some prior education studies coarsely approximate a student's knowledge as a factored set of binary variables, one for each skill, and infers a precondition graph structure among skills (known as a 'learning hierarchy') from student data: see for example Gagne´ e's and Briggs and Close and Murtagh. Despite this structure, automated tutor action selection remains challenging as the factored state space may consist of hundreds of skills. In addition, the student state is not directly observable, but can be probed through the use of drill exercises and other student responses. Modelling a fairly small curriculum of 100 skills using an atomic-state POMDP framework could require planning over a state space of size 2 100 ≈ 10 30 which is far outside the range of generic, flat POMDP solvers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

Specifically we consider constructing policies for POMDPs that exhibit the following three properties: they are 2. have positive-only effects, and 3. have unique preconditions for each variable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

For compactness, in the rest of the paper we will refer to Positive-Only effects, Factored, with Unique Preconditions (POFUP) POMDPs as POFUPP processes. Factored representations are those in which the world state is represented by a vector of variables. Positive-only effects, commonly leveraged in classical planning, imply that once a binary variable becomes true, it will not later become false. Before we describe the third property, recall that in a factored representation, a given state variable s k 's value on a subsequent time step depends on the action chosen, and the values of a set of the other state variables (which could include s k on the previous time slice): in a dynamic Bayes net (DBN), these would be called the parents of s k. The unique preconditions assumption implies that there is a single set of values of s k 's precondition variables that allow s k to become true. In all the education learning hierarchies we examined, there was always a unique set of preconditions for each variable.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

It is important to note that while there is a unique set of preconditions for each state variable, there are still numerous (potentially exponential in the number of variables) paths to reach each state. We assume that the planning objective is to reach a goal state.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

Our Reachable Anytime Planner for Imprecisely-sensed Domains (RAPID) leverages these three structural properties to construct an initial policy with a computational cost that scales polynomially with the number of domain variables, instead of exponentially. RAPID first computes a solution to the fully observable MDP starting at an initial state sampled from the initial POMDP belief state. This process is very fast, taking only time linear in the number of state variables. RAPID then performs partially-observable planning over the limited envelope of states reached under this MDP policy, and then slowly expands the state space considered as time allows. At most the state space envelope will expand to become the reachable state space given the initial potential starting states, which is typically much smaller than the exponential potential state space.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Stuart Russell", "weight": 1.0} -->

We present promising experimental results on two large tutoring-inspired simulations. The second problem consists of 122 variables, or a potential flat state space of over 10 30. RAPID manages to achieve good performance quickly in both problems, though several comparison planners, including a factored approach, fail to find a good policy.

<!-- chunk {"id": "body-0012", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

We are interested in decision making in POFUP partially observable, stochastic environments that may be specified by the tuple 〈 S, L, A, Z, b 0, E, p (( s i ) ′ | s i, a ),... p ( z | ( s i ) ′, a ), r ( s, a ), s G, s T 〉 where

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

- S is a set of states. The domain consists of L binaryvalued variables s 1, s 2,..., s L, and each state is an assignment of values (true or false) to all the domain variables: s = 〈 s 1, s 2,..., s L 〉. - A is a set of actions. Each action a ij is associated with a particular state variable s i and has the potential to make only that variable true. 1 There will generally be multiple actions associated with the same state variable s i. For example, there could be a drill exercise 1 Actions or operators which have a single effect have been previously described as unary operators.

<!-- chunk {"id": "body-0014", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

(c) States reachable from s 0 = { 0, 0, 0, 0, 0, 0 } Figure 1: The relationship between the precondition variable graph of 6 binary state variables, the possible state space and transitions, and the reachable state space starting at a particular initial state. action and a lesson action to help a student understand two-digit addition.

<!-- chunk {"id": "body-0015", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

- b 0 is the initial belief state which is a sparse representation of the possible initial states and associated probabilities. The sum of the probabilities over all possible initial states is constrained to equal 1. - E is a precondition graph which specifies for each state variable s i the set of state variables s ip 1, s ip 2,... s ipM (equivalent to parents of s i in a DBN) that must be true before state variable s i can become true. We assume there is a unique conjunction of precondition variables for each variable (for example, s 1 ∧ s 2 can be a precondition, but not s 1 ∨ s 2). As a concrete example, the precondition graph for a student to master the multiplication skill would include the addition skill as a prerequisite. - p ((s i) ′ = false | s i = false, a ij) specifies the probability of a state variable s i remaining false even when all s i 's preconditions are satisfied and a relevant action a i ∗ is taken.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

If a state variable s i 's preconditions are not satisfied, and action a i ∗ is applied, s i always remains false. Continuing the prior example, let a ij be a multiplication exercise, and s i be the multiplication skill. Then p ((s i) ′ = false | s i = false, a ij) is the probability that after trying a multiplication exercise, a student still may not yet understand multiplication, even if she has all the necessary preconditions skills (addition, etc.) as specified in E. - p (z | (s i) ′, a ij) specifies the probability of receiving a particular observation given that a particular action a ij is taken, and the resulting value of the action's associated state variable (s i) ′. Note that since an action is only associated with a single variable, only a single p (z | (s i) ′, a ij) will be applicable at each time step. - r (s, a ij) is the reward for taking action a ij in state s.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

The reward is negative, and depends only on the action (aka independent of the state) for all states except the goal state s G and terminal state s T. - s G is the goal state. r (s G, a) is positive or zero. - s T is the terminal state. s G deterministically transitions to s T. s T is a sink state where the reward is 0 and the observation probabilities are identical to the observation probabilities of s G.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PROBLEM DESCRIPTION", "weight": 1.0} -->

As the states are partially observable, we maintain a distribution over states, known as the belief state, which is a sufficient statistic of the history of actions taken and observations received. The planning objective is to maximize the expected sum of rewards given the initial belief state b 0. Due to the reward formulation, this is similar to a partially observable, stochastic shortest path problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "ALGORITHM", "weight": 1.0} -->

Prior flat and factored POMDP approaches typically fail to scale to domains with a large number of variables. This often continues to hold true even when, for particular initial belief states, the reachable state space is significantly smaller than the full state space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "ALGORITHM", "weight": 1.0} -->

Instead we draw inspiration from envelope-based planning algorithms for large fully observable MDPs and extend these ideas to our POFUPP domains. Dean et al. presented the idea of computing a policy for fully observable, flat MDPs by planning only over a smaller envelope of states. As time allowed, the state envelope was expanded to include more of the reachable state space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm 1 RAPID: REACHABLE ANYTIME PLANNING FOR IMPRECISELY-SENSED DOMAINS", "weight": 1.0} -->

- 1: Sample an initial state from the initial belief - 2: Construct an initial envelope using a deterministic MDP relaxation that can be solved efficiently. - 3: while remaining time do - 4: Define & solve a POMDP over the envelope - 5: Expand the envelope To our knowledge RAPID is the first algorithm to take a similar approach in the context of partially-observable planning. There are several key technical challenges that need to be overcome to apply envelope-based planning in partially observable domains that can be characterized as POFUPP problems. First, we require an algorithm for efficiently computing a good initial envelope over the large, factored, partially observable state space. Second, we need a method for converting this envelope into a fully defined POMDP and solving the resulting model. We present solutions for both these challenges, and RAPID's empirical efficiency allows us to scale to very large problem sizes. The RAPID algorithm is summarized in Algorithm 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "INITIAL ENVELOPE CONSTRUCTION", "weight": 1.0} -->

Given a POFUPP process M, we first need to construct an initial envelope of states. Ideally the envelope would include states that have a reasonable probability of being visited given a good policy for the partially observable domain. The states visited along the optimal MDP solution starting with one of the possible initial states would seem intuitively to be reasonable, as the MDP solution forms an upper bound on the POMDP performance. However, standard MDP value iteration will be intractable since it scales as a function of the state space, which in our process is an exponential function of the number of variables. Even alternate factored solvers will typically be too slow.

<!-- chunk {"id": "body-0023", "role": "body", "section": "INITIAL ENVELOPE CONSTRUCTION", "weight": 1.0} -->

Instead we propose an approach which leverages the particular properties of our structured process by first relaxing the process to its deterministic, fully observable equivalent, and use this to very quickly compute a good trajectory between a start state s 0 and the goal s G.

<!-- chunk {"id": "body-0024", "role": "body", "section": "INITIAL ENVELOPE CONSTRUCTION", "weight": 1.0} -->

We first sample a state s 0 from the initial belief state b 0. Given s 0, and the variable precondition graph E, RAPID identifies the state variables whose value is false in s 0 and true in the goal state s G. RAPID then computes a topological order of these state variables given the precondition graph E. A topological order of these variables is any linear ordering such that each state variable comes before all other state variables to which it has outbound arrows in the precondition graph. For example, in Figure 1a, state variable L1 must appear before all other variables, and L2 must appear before L3. As the precondition graph E is a directed acyclic graph (DAG) 2, the topological order can be computed in time linear in the number of state variables and precondition conditions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "INITIAL ENVELOPE CONSTRUCTION", "weight": 1.0} -->

The computed topological state variable ordering (such as 〈 s 2, s 68,... s 16 〉 ) is converted into a state trajectory between the start s 0 and goal state s G by simply adding in order each state variable to the original s 0. Therefore the cost of generating an initial envelope is simply a linear function of the number of state variables. In Section 4.5 we will show that this state trajectory consists of the state variables visited by following an optimal MDP policy for M starting at the sampled state s 0.

<!-- chunk {"id": "body-0026", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

RAPID proceeds by defining a POMDP P ′ over the current state envelope. We supplement the envelope state space defined by the state trajectory sequence by two additional states: a terminal out state s tout, and a terminal goal state s tg. The definition of an out state follows prior work in the fully observable envelope literature. The dynamics of the states within the envelope are the same as in the original process M, except if a state transition lead to a state outside the envelope, then that transition, and associated probability, are set to go to the s out state. The out state itself transitions with probability one to the terminal out sink state s tout which has self-loop dynamics. The separation of s tout and s out is done in order to specify separate reward functions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

To discourage leaving the envelope, the reward for the out state is set to a large negative value. s tout has reward zero. Separating s out from s tout allows there to be a single shot cost for exiting the envelope. 3 The observation model for all states within the envelope is the same as in the POFUPP M. In contrast to envelope planners for fully observable MDPs where all states, including the out state, is fully observed, in POMDP domains the out states are most naturally modeled as partially observable, since they represent the remaining partially observable states that are not in the envelope. This raises the interesting side problem of how to represent the observation probabilities for the out states, which represent the potential observation probabilities of all states outside the envelope. In general there will be an exponential (in the number of variables) states outside of the envelope, and so for now we take the simple approach of approximating the observation probability of s out by averaging the observation models of a sampled set of states lying outside the envelope. The observation model of s tout is identical to s out.

<!-- chunk {"id": "body-0028", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

2 Since actions have positive-only effects, there are also no cycles in the corresponding state dynamics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

3 An alternate strategy would be to define rewards over state, action, next state tuples.

<!-- chunk {"id": "body-0030", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

If there is any initial probability over states outside of the envelope, then a new belief state is defined over only the envelope state space, with all remaining probability mass in the out state s out.

<!-- chunk {"id": "body-0031", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

POMDP P ′ can be solved using any generic POMDP planner with optimality bounds and in our experiments we used the publicly-available HSVI. POMDP planning proceeds until the error bound over the initial belief state drops below a chosen ϵ -threshold, or a specified time limit is reached.

<!-- chunk {"id": "body-0032", "role": "body", "section": "ENVELOPE POMDP POLICY GENERATION", "weight": 1.0} -->

Note that the computed policy for POMDP P ′ can be used to act in the original POFUPP M.

<!-- chunk {"id": "body-0033", "role": "body", "section": "ENVELOPE EXTENSION", "weight": 1.0} -->

If additional planning time is available after the initial policy is computed, then the state envelope can be expanded. There are numerous potential strategies for envelope expansion and in this initial work we used a simple, but empirically effective approach. We consider three possible methods, in order, for identifying a new state to add to the envelope; in other words, we try the first method and see if it identifies a new state to be added, if it does, we stop, else we run the second method, etc.

<!-- chunk {"id": "body-0034", "role": "body", "section": "ENVELOPE EXTENSION", "weight": 1.0} -->

The first method samples any potential initial state s 0 i which has non-zero probability in the initial belief state b 0, but is not yet part of the envelope of states. If all potential initial states are in the envelope, the second method tries to find a new non-envelope state by expanding the envelope fringe. This expansion is performed by starting at a possible initial state and simulating a trajectory using an ϵ r -greedy policy 4 until either a non-envelope state is reached, or a goal state is reached. This process is repeated until a non-envelope state is reached or a set number of iterations pass. If no non-envelope states are found, in the third method, we iterates through each state and tries all applicable actions (given the preconditions the state represents) to see if a new non-envelope state is reachable. This ensures that, given enough time, the envelope will grow to reach the full reachable state space, given the possible initial states defined by the initial belief state.

<!-- chunk {"id": "body-0035", "role": "body", "section": "ENVELOPE EXTENSION", "weight": 1.0} -->

Once a non-envelope state is identified, it must be added to the envelope. In many cases these newly-added states will be multiple state transitions from the existing envelope of states. For example, consider a mathematics tutor domain where to start a student either knows algebra, or algebra and calculus. If the initial envelope is constructed starting from the state where the student knows calculus, and then the state representing the student only knows algebra is added, there are many missing steps between algebra and calculus that need to be added in order to compute a reasonable pol- icy for the newly added initial state. To address this, when a new potential state is added, RAPID re-performs the initial envelope construction of creating a complete state trajectory to the goal, starting from the newly added state. This process is very fast, and the main limitation of this approach is that it can add O ( L ) states to the envelope per state, which slows down the POMDP planning process. However, the benefit of increasing the probability that the new states will immediately improve the computed policy, was thought to outweigh this slight shortcoming.

<!-- chunk {"id": "body-0036", "role": "body", "section": "ENVELOPE EXTENSION", "weight": 1.0} -->

4 The POMDP policy is followed (1 -ϵ r ) fraction of time time, and a random action is taken ϵ r fraction of the time.

<!-- chunk {"id": "body-0037", "role": "body", "section": "PERFORMANCE AND COMPUTATIONAL COMPLEXITY", "weight": 1.0} -->

First, for completeness, we note that RAPID is guaranteed to converge to an ϵ -optimal policy, as long as an ϵ -optimal POMDP planner is used, since RAPID is guaranteed to eventually expand the envelope to include all states reachable from the initial belief state.

<!-- chunk {"id": "body-0038", "role": "body", "section": "PERFORMANCE AND COMPUTATIONAL COMPLEXITY", "weight": 1.0} -->

Computing a state trajectory from an initial to goal state, and associated value computations, takes time linear in the number of variables. The initial envelope will have at most O ( L ) states, which means that the initial POMDP planning will be performed over a state space which is a linear function of the number of variables. The maximum number of states in the envelope is the reachable state space, which is typically much smaller than the potential 2 L state space. The complexity of solving a POMDP depends on the particular technique. HSVI performs a depth-first roll out, and updates an explicit representation of an upper and lower bounds on the POMDP value function along the roll out. Each lower bound backup and belief update is a quadratic function of the number of states, so both operations will be impacted positively by a smaller input state space.

<!-- chunk {"id": "body-0039", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

We will shortly prove that the trajectory of states between a start and the goal state, as computed during envelope initialization and expansion, consists of states visited by following an optimal policy for the fully observable MDP of the POFUPP process. We leverage this property to efficiently compute the fully-observable optimal MDP value of the states within the envelope, which can then be used to calculate an upper bound on the initial belief state b 0. Such bounds can be useful for at least two reasons. First, many POMDP solvers (including HSVI and SARSOP) use upper bounds during planning. Typically these bounds are computed by solving the MDP, which is known to be an upper bound to the POMDP values. However, solving the flat MDP typically requires multiple backup operations, each of which requires time polynomial in the number of states. Second, upper bounds provide useful benchmarks for evaluating RAPID's performance. However, solving the MDP upper bound over the complete factored space of hundreds or more variables is computationally infeasible. In contrast, our approach scales as O ( LN b 0 ) where N b 0 is the number of initial states with non-zero probabilities.

<!-- chunk {"id": "body-0040", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

We now illustrate how we compute the value of the the states along a trajectory between a start and goal state, as returned during envelope initialization and expansion. We first modify the original rewards. Let ˜ r (s -i, a ij) be the new reward for taking action a ij in a state s -i where state variable s i is false but all its preconditions are true. We define the value of this new reward as: Intuitively, ˜ r (s -i, a ij) represents the expected reward/cost of making state variable s i true using action a ij, given the stochasticity of action a ij. To compute the state trajectory values, we start with the goal state, and traverse the trajectory backwards, at each step selecting the action a ij with the minimum expected cost ˜ r required to make the subsequent variable s i in the consecutive state true. The values are computed simultaneously, by summing up the rewards during the traversal: where state s + i is the same as state s -i except now state variable s i is also true. This value computation requires time linear in the number of variables.

<!-- chunk {"id": "body-0041", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

This process can be done at the same time as when the state trajectory is constructed from the topological order.

<!-- chunk {"id": "body-0042", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

Theorem 1. Given a POFUPP M, let M f be the fullyobservable MDP version of M, s 0 be a state sampled from b 0, { s 0, s traj 1,..., s G } be the state trajectory computed by the initial envelope method, π M f be the associated policy, and V ( s 0 ),..., V ( s G ) be the calculated state trajectory values. These values and policy represent an optimal policy and the optimal values of these states in the MDP M f.

<!-- chunk {"id": "body-0043", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

Proof. (Sketch) The initial topological order constructed is an optimal plan to the goal from the start state s 0 for the deterministic, uniform action-cost, fully observable process M duf version of the POFUPP M. This is true due to the particular POFUPP structure assumed. Briefly, the positive-only effects and the presence of unique preconditions to make a single variable true, imply that all permutations (that respect the precondition structure) of the same set of state variables will result in the same final state. As in M duf all rewards are constant except at the goal, all paths of the same length between the same start state and the goal state will have the same cost. Therefore we can arbitrarily select any ordering that respects the preconditions, and its value is guaranteed to be optimal (and equal to all other topological orderings between the same start state and goal).

<!-- chunk {"id": "body-0044", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

To determine the optimal value (and policy) of each state along the corresponding state trajectory in the deterministic (but with the original action costs/rewards) MDP M df version of M requires considering the state-action values of each state. From Bellman the state-action value can be expressed as the immediate reward of taking an action in a state, plus the future expected reward. As we currently assume each action is deterministic, the state action value of a state s -k which is a state where state variable s k is false but all its preconditions are true, can be expressed as where s + k is the state identical to s -k except state variable s k is also true. In the deterministic MDP M, Q (s, a kj) represents the expected cost of making the state variables in s G true which are false in the current state s. However, since in a POFUPP process each variable requires a unique set of precondition variables to be true, the order in which these state variables are acquired is irrelevant: any order that satisfies the precondition structure E is equivalent.

<!-- chunk {"id": "body-0045", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

The only difference in rewards/costs comes from which action a kj out of a set of actions a k ∗ is chosen to achieve a state variable s k; note here that all a k ∗ have the same preconditions, but they may have different costs, different selftransition probabilities, and different observation probabilities. Therefore, the state trajectory obtained from the topological order is equal to any other trajectory of states between s 0 and the goal G. Given this, action selection for each state along the trajectory can be restricted without loss of optimality to only those actions which pertain to the next variable to be acquired along the topological order (as specified by Equation 2). This means that the next state s + k in Equation 4 will be identical for all considered actions a k ∗, and to find the optimal action it suffices to only consider the immediate expected reward ˜ r. Therefore the policy and values in Equation 2 and 3, respectively, represent an optimal policy and the optimal value for the deterministic MDP.

<!-- chunk {"id": "body-0046", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

Finally, the MDP M f falls into the class of stochastic shortest path problems. Therefore the computed value function and policy for the deterministic MDP M df which has noself loops (as just specified) using the modified rewards defined in Equation 1 has an identical policy and value function to the original MDP M f (pg.25, Bertsekas and Tsitsiklis, ). Therefore, the values and policy computed using Equation 2 and 3 for all states along the trajectory are guaranteed to be optimal for MDP M f.

<!-- chunk {"id": "body-0047", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

Theorem 1 shows that we can efficiently compute the optimal MDP values for states inside the constructed envelope.

<!-- chunk {"id": "body-0048", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

Once the envelope includes all possible initial states, we will have a value on each initial state computed using Equation 3. We can then compute an upper bound for initial belief state value (¯ V (b 0)) by taking the weighted sum of the Figure 2: SmallMath Precondition Graph.

<!-- chunk {"id": "body-0049", "role": "body", "section": "UPPER BOUNDS FOR POFUPP PROBLEMS", "weight": 1.0} -->

Note that this provides an upper bound to the original POFUPP process: in contrast, any bounds computed by the POMDP solvers over the envelope only apply to the restricted envelope POMDP P ′. We later calculate ¯ V ( b 0 ) for our two experimental domains. This bound can be computed in time linear in the product of the number of state variables and initial possible states.

<!-- chunk {"id": "body-0050", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Due to our interest in tutoring applications, we performed simulation experiments in two tutoring-inspired domains.

<!-- chunk {"id": "body-0051", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

In both cases, the variable precondition graph construction was informed by literature from the education communities: the transition probabilities, observation probabilities and reward values were chosen by hand.

<!-- chunk {"id": "body-0052", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

The first domain, SmallMath, consisted of 19 elementary math skills, yielding a potential state space of 2 19 ∼ 500, 000 states. The precondition graph for the skills is displayed in Figure 2. There are two possible observations, and 38 actions, 2 for each skill. The first action for a skill, a 'teaching' action, has a high probability of causing the skill to transition to being true ( p = 0. 8 ) if it is not already and the preconditions for that skill are fulfilled; however, it does not provide any feedback about whether the student has successfully acquired the skill. In our experiments we set the probability of each observation is 0. 5 for actions 1,3,5,...,37. The second action for each skill (actions 2,4,...,38) loosely corresponds to a practice exercise, and only causes skill acquisition with probability 0. 5. However, practice exercises provide more useful feedback about whether that skill was acquired: the observation is true with probability 0.9 if the hidden skill is true, and true with probability 0.2 if the skill is false.

<!-- chunk {"id": "body-0053", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

The reward for reaching the state where all skills are true was set to 10000, and there was a reward of -1 for all other states and actions. The initial belief state had three non-zero initial start states.

<!-- chunk {"id": "body-0054", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

In the past there have been a number of papers on 'learning hierarchies' in the education literature. Learning hierarchies consist of ordered hierarchies, or graphs, of skills, which are very similar to our variable precondition graphs. Numerous classroom studies have been done to construct these learning hierarchies from student data, though the analysis historically treats the data as fully observable rather than modeling student knowledge as a hidden state.

<!-- chunk {"id": "body-0055", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

Given this work, for the second domain, BigMath, we constructed a larger tutoring-inspired problem consisting of addition, subtraction, multiplication, and addition and subtraction of fractions skills. The fraction precondition graph was derived from Miller and Phillips and Uprichard and Phillips. We combined the fraction precondition structure with the subtraction hierarchy from Gagn´ e, and the addition, subtraction, multiplication and division hierarchies from Close and Murtagh. The full precondition graph is displayed in Figure 3 and consisted of 122 skills. 5 The flat state space is 2 122 which is over 10 30 states. Similar to the first domain, we created an action space with two potential actions for each skill, one lesson-like action, and one drill-like action. The observation and transition probabilities, given the precondition variables are satisfied, were defined the same way as in the SmallMath domain. The reward for reaching the state where all skills are true was set at 100000, and there was a reward of -1 for all other states and actions. The original belief state had four non-zero probability initial start states, consisting of plausible variable subgroups.

<!-- chunk {"id": "body-0056", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

Note that the horizon of both problems is quite long. Even in the deterministic versions of both problems, if the world state starts with no variables true, the number of steps to reach the goal is 19 in SmallMath and 122 in BigMath.

<!-- chunk {"id": "body-0057", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

5 A file displaying this precondition structure is available at ∼ emma/bigmathpreconditions.pdf Figure 3: Precondition Graph for BigMath. This structure was derived by combining the Miller and Phillips and Uprichard and Phillips learning hierarchies for fractions, with Gagne´ e and Briggs' subtraction hierarchy and Close and Murtagh's addition, subtraction, multiplication and division hierarchy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "DOMAINS", "weight": 1.0} -->

As both problems are stochastic, the expected number of steps can be significantly longer, depending on the initial belief state distribution. Therefore, both domains exhibit what are typically known in the POMDP community as the curse of history, due to the long horizon, and the curse of dimensionality, due to the problem size.

<!-- chunk {"id": "body-0059", "role": "body", "section": "SOLUTION PARAMETERS", "weight": 1.0} -->

As stated earlier, we used HSVI to solve the envelope POMDPs. The maximum horizon for SmallMath was set at a conservative 450 steps, and for BigMath at 1000 steps. Identical horizon limits were used when evaluating the empirical reward of the computed policy. The reward for the out state was set to be -1000 for SmallMath and -100 for BigMath. As there will typically be some probability that the state will transition into an out-of-envelope state, and both problems can require a long horizon of acting to reach the goal, the out state reward was loosely chosen to discourage transitioning to the out state without so severely penalizing the transition that the computed policy conservatively avoids adding any more skills. We did not optimize performance by varying this parameter, and other values might lead to further performance benefits.

<!-- chunk {"id": "body-0060", "role": "body", "section": "SOLUTION PARAMETERS", "weight": 1.0} -->

HSVI terminates when a terminal time limit is reached or a minimum distance ( ϵ ) between the upper and lower bounds on value of the initial belief state is achieved. In SmallMath we set the maximum time limit to 1200 seconds and ϵ = 200. In BigMath we set the maximum time limit to 8000 seconds and ϵ = 1000.

<!-- chunk {"id": "body-0061", "role": "body", "section": "EVALUATION METRICS", "weight": 1.0} -->

After each envelope expansion, we evaluated the envelope policy reward empirically over multiple episodes of the rel- evant problem's max horizon length. For SmallMath we evaluated the empirical reward for 20 episodes after each expansion, and for BigMath we evaluated the empirical reward for 5 episodes after each expansion: BigMath is significantly more computationally intensive to evaluate due to the larger state space, and longer problem horizon. We present results averaged over 5 runs with different initial seeds for SmallMath and 8 runs for BigMath.

<!-- chunk {"id": "body-0062", "role": "body", "section": "BASELINES", "weight": 1.0} -->

Even the smaller of the two problems, SmallMath, still requires over 500,000 states to enumerate the exhaustive set of state variable combinations, which limited the potential alternate algorithms to compare against.

<!-- chunk {"id": "body-0063", "role": "body", "section": "BASELINES", "weight": 1.0} -->

SARSOP is a non-factored stateof-the-art generic POMDP solver which accepts factored input files.

<!-- chunk {"id": "body-0064", "role": "body", "section": "BASELINES", "weight": 1.0} -->

Symbolic Perseus is a factored-statespace POMDP solver. Symbolic Perseus was used to compute a good approximate solution to a factored handwashing assistance problem with 13 variables, and over 50 ∗ 10 6 states.

<!-- chunk {"id": "body-0065", "role": "body", "section": "BASELINES", "weight": 1.0} -->

In some cases the reachable state space may be quite small, and so we also explored first enumerating the reachable space, and then using HSVI to compute a POMDP policy over the reachable states.

<!-- chunk {"id": "body-0066", "role": "body", "section": "BASELINES", "weight": 1.0} -->

We also implemented a simple, very fast, heuristic Fixed Threshold, No-Forgetting (FTNF) policy similar to policies used in prior intelligent tutoring systems. At each step, FTNF identifies the variable with the highest probability of being true below an input threshold probability, whose preconditions have exceeded this threshold probability. FTNF

<!-- chunk {"id": "body-0067", "role": "body", "section": "BASELINES", "weight": 1.0} -->

- (a) SmallMath Reward vs No. Expansions (b) BigMath Reward vs. Cumulative Time

<!-- chunk {"id": "body-0068", "role": "body", "section": "BASELINES", "weight": 1.0} -->

- (c) BigMath Reward vs. No. Expansions Figure 4: Results from both simulations, showing RAPID's average performance after each round of envelope expansion. In (a) and (c) results are averaged over multiple algorithm runs. In (b) each RAPID run is shown in a different color, with circles representing the mean reward of the run's policy at different times. The dotted line is an upper bound on the initial belief state value. executes the action most likely to make that variable true, and updates the belief probability over that variable. Once a variable exceeds the input probability threshold, its value is assumed to be true for the rest of the episode.

<!-- chunk {"id": "body-0069", "role": "body", "section": "BASELINES", "weight": 1.0} -->

Finally, we also computed an upper bound on the value of the initial belief state using Equation 5.

<!-- chunk {"id": "body-0070", "role": "body", "section": "SmallMath", "weight": 1.0} -->

We display the performance of RAPID on SmallMath in Figure 4a. RAPID could generally quickly find a good solution, and its consistency in doing so increased as the computation time increased, as should be expected.

<!-- chunk {"id": "body-0071", "role": "body", "section": "SmallMath", "weight": 1.0} -->

We represented SmallMath in the SARSOP POMDPX format but found that SARSOP problem initialization consistently tried to exceed our limit of available memory (2 gigabytes). We believe this is because the current implementation still uses a non-factored dynamics representation, and a full sized-representation of SmallMath would require 2 19 × 2 19 × 38 entries.

<!-- chunk {"id": "body-0072", "role": "body", "section": "SmallMath", "weight": 1.0} -->

Symbolic Perseus requires specifying the number of sampled belief states to use for planning. When we specified a small number of beliefs (N=20), the algorithm computed a solution in 5150s, but the resulting policy could never find a trajectory to the goal. Using a larger number of beliefs (N=120), Symbolic Perseus was still generating belief points and had yet started computing a policy after 8 hours; as this well exceeded the time necessary to achieve good performance in the SmallMath domain using RAPID, we did not run Symbolic Perseus further.

<!-- chunk {"id": "body-0073", "role": "body", "section": "SmallMath", "weight": 1.0} -->

Given the initial belief selected, the reachable state space of SmallMath is significantly smaller than the potential state space size, at only 109 states. It is computationally tractable to simply enumerate this reachable state space and run HSVI over the resulting states. This approach yielded the best performance, with an average reward of 9962 on 200 trials (each consisting of at most 200 steps). This corresponded to an average of 39 steps to reach the goal state. The heuristic FTNF policy performed worse than the RAPID policy over a number of thresholds, and was significantly worse (t-test, p¡0.001) than the POMDP solution over the reachable state space at even the best threshold (0.925) examined (FTNF average reward=9947, mean number of steps to goal=54). These results highlight the advantage of a POMDP planning approach, which may both infer the value of earlier variables based on later variable values, and revisit an earlier variable if later evidence suggests its value is not yet true.

<!-- chunk {"id": "body-0074", "role": "body", "section": "BigMath", "weight": 1.0} -->

RAPID again was able to fairly quickly achieve good performance in this domain. Figure 4b & c display the average performance after each envelope expansion for different runs versus cumulative running time, and after each envelope expansion, respectively.

<!-- chunk {"id": "body-0075", "role": "body", "section": "BigMath", "weight": 1.0} -->

Due to our experience with SARSOP and Symbolic Perseus on SmallMath, we did not explore their use on BigMath, which is a substantially larger problem.

<!-- chunk {"id": "body-0076", "role": "body", "section": "BigMath", "weight": 1.0} -->

In BigMath, given the chosen initial belief, even the reachable space is over millions of states and the potential state space exceeds 10 30 states. It was therefore not feasible to perform standard planning over the reachable space.

<!-- chunk {"id": "body-0077", "role": "body", "section": "BigMath", "weight": 1.0} -->

We compared FTNF to the performance of RAPID after 4 envelope expansions. Though FTNF is very fast, it generally performed much worse than RAPID over a wide range of thresholds (from 0.8 to 0.9999). FTNF with the best found threshold (0.9999) performed slightly better than RAPID over an 80 episode simulation, but the difference was not significant (t-test, p=0.18). Our experience suggests that it may be hard to identify a good threshold for FTNF in advance, and choosing a too-high value can lead to overly conservative policies.

<!-- chunk {"id": "body-0078", "role": "body", "section": "CONCLUSION & FUTURE WORK", "weight": 1.5} -->

There exist a number of important stochastic, partially observable problems that exhibit a large amount of structure that can be used to perform efficient planning. In this paper we focused on problems exhibiting a form of topological structure in the factored state space: domains which possess such structure include student tutoring, dialogue and potentially assembly tasks. Our RAPID algorithm leverages this structure to compute an initial state envelope based on the optimal MDP policy in time linear in the number of variables. RAPID then performs standard POMDP planning over this restricted envelope, before expanding the envelope and re-solving in an anytime fashion. Our experimental results demonstrate RAPID can quickly produce a good policy for an extremely large factored problem where the problem structure is constructed using prior precondition graphs from the education community.

<!-- chunk {"id": "body-0079", "role": "body", "section": "CONCLUSION & FUTURE WORK", "weight": 1.5} -->

There is ample scope for future work. We intend to explore additional envelope expansion techniques, such as trying to bias the new trajectories to the goal to lie within existing parts of the envelope. In addition, we currently re-solve the POMDP without considering the previously computed solution. We believe it should be possible to achieve further computational gains by re-using the value function ( α -vectors) computed using the prior envelope, by setting the value of the additional states to a lower bound on their potential value. 6 In this paper we have assumed the POMDP model parameters are provided, but to integrate this in a real ITS will necessitate learning the model parameters. We plan to learn model parameters across multiple students' performances, motivated by the success of prior ITSs that use population-level model parameters.
