On the Value of Preview Information for Safety Control

Topics include Safety control, Preview information, Lookahead, Nonlinear systems, Brunovsky canonical form, Controlled invariance.

Analyzes when predictions of future disturbances or external inputs improve safety-control performance. The paper gives general preview-time guidance for nonlinear systems and sharper structural results for Brunovsky-form systems, clarifying when lookahead is worth using in continuous-state safety controllers.

Incorporating predictions of external inputs, which can otherwise be treated as disturbances, has been widely studied in control and computer science communities. These predictions are commonly referred to as preview in optimal control and lookahead in temporal logic synthesis. However, little work has been done for analyzing the value of preview information for safety control for systems with continuous state spaces. In this work, we start from showing general properties for discrete-time nonlinear systems with preview and strategies on how to determine a good preview time, and then we study a special class of linear systems, called systems in Brunovsky canonical form, and show special properties for this class of systems. In the end, we provide two numerical examples to further illustrate the value of preview in safety control.

## Introduction

In a typical feedback control framework, the control input $u{(t)}$ is determined based on the current state $x{(t)}$, or more generally the initial state $x{}$ and the sequence of the past disturbances^11^1The concept of disturbance in this work can be quite general and it essentially captures any external input for which we might have predictions of future values. For instance, the reference signal in a tracking problem can be treated as "disturbance" if error dynamics are used to include the reference signal in system equations (see examples in ). $d{}$, $d{}$,..., $d{({t - 1})}$....

The above mentioned systems are all safety-critical, where controllers should be designed to ensure safety specifications. The safety specifications considered in this work are to have the system state avoid visiting a user-defined unsafe region, or equivalently have the state stay within a safe region indefinitely. A standard way to achieve safety in this sense is via robust controlled invariant sets. Then, a fundamental question to ask is how to measure the improvement due to preview in safety control and how the change of preview time affects the quality of safety control.

## Conclusion

In the first part of this work, we study general properties of controlled invariant sets for systems with preview and the implications of those properties, including a strategy to choose a preview time. In the second part, we study systems in Brunovsky canonical form with hyperbox safe sets, for which we derive the maximal controlled invariant set of the $p$-augmented system in closed form. The impact of preview on the controlled invariant sets can be directly analyzed using this closed-form expression, by help of which we prove the existence of a critical preview time for this class of systems....

The dynamics of a system $\Sigma_{B}$ in Brunovsky canonical form is

That is, the maximal admissible input set at each state grows as the preview time increases. An important question is then if there exists a critical $p_{0}$ such that the maximal admissible input set stops growing for $p > p_{0}$, that is for all $p > p_{0}$, for all states ${(x,d_{1:p})} \in S_{{xu},p}$,

### Corollary 1

The majority of literature on preview control focuses on incorporating preview information into optimal control formulation....
