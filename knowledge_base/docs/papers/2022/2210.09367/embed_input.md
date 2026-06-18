Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning

High-level autonomy requires discrete and continuous reasoning to decide both what actions to take and how to execute them. Integrated Task and Motion Planning (TMP) algorithms solve these hybrid problems jointly to consider constraints between the discrete symbolic actions (i.e., the task plan) and their continuous geometric realization (i.e., motion plans). This joint approach solves more difficult problems than approaches that address the task and motion subproblems independently. TMP algorithms combine and extend results from both task and motion planning. TMP has mainly focused on computational performance and completeness and less on solution optimality. Optimal TMP is difficult because the independent optima of the subproblems may not be the optimal integrated solution, which can only be found by jointly optimizing both plans. This paper presents Task and Motion Informed Trees (TMIT*), an optimal TMP algorithm that combines results from makespan-optimal task planning and almost-surely asymptotically optimal motion planning....

## Introduction

Planning solutions to problems described by high-level specifications requires autonomously deciding both *what* to do (i.e., the sequence of high-level actions) and *how* to do it (i.e., the associated motions). This is difficult since both of these decisions can affect later stages of the planning problem by altering the valid and reachable subsets of the search space. Integrated Task and Motion Planning (TMP) is a holistic approach to solve these high-level planning problems by jointly considering the symbolic (i.e., actions) and geometric (i.e., motion) constraints on the solution.

Solving TMP problems is computationally expensive. Evaluating a candidate sequence of actions (i.e., a *task* or *symbolic* plan) requires the computationally expensive operations of finding compatible action parameters and associated valid motion plans. TMP algorithms typically consider multiple symbolic plans to solve a problem and must be efficient because the set of possible symbolic plans is combinatorially large for most real-world scenarios and the sets of possible action parameters and motion plans are uncountably infinite.

Encoding task planning as SMT via a custom theory offers untapped potential performance improvements for TMP. It provides an easy extension point for a "theory of TMP", incorporating geometric information such as reachability or action feasibility into the symbolic planner. We leave exploration of this capacity for future work.

Future work could also investigate accelerating the discovery of initial solutions by explicitly biasing RGG growth toward task-relevant regions.

### IV-A Predicate representation

Discrete actions are defined by their necessary preconditions and their resulting effects (Defs. 6: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), 7: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") and 8: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

A *prefix* of a symbolic plan is a subsequence of the actions in the plan starting with the initial action. The second method forces new plans to avoid *failing prefixes* of symbolic plan candidates by adding constraints of the same form as Eq....
