On the Hardness of Learning to Stabilize Linear Systems

Topics include Linear systems, Stabilization, Sample complexity, System identification, Robust control, Machine learning theory, Control theory.

Constructs linear-system classes where learning a stabilizing controller is statistically hard even when identification itself is not the bottleneck. The paper separates stabilization difficulty from estimation difficulty by tying the lower bound to co-stabilizability and robust-control structure.

Inspired by the work of Tsiamis et al. \cite{tsiamis2022learning}, in this paper we study the statistical hardness of learning to stabilize linear time-invariant systems. Hardness is measured by the number of samples required to achieve a learning task with a given probability. The work in \cite{tsiamis2022learning} shows that there exist system classes that are hard to learn to stabilize with the core reason being the hardness of identification. Here we present a class of systems that can be easy to identify, thanks to a non-degenerate noise process that excites all modes, but the sample complexity of stabilization still increases exponentially with the system dimension. We tie this result to the hardness of co-stabilizability for this class of systems using ideas from robust control.

## INTRODUCTION

Learning-based control plays an increasingly important role in many application domains such as power systems, robotics, self-driving cars, where it might be hard to perfectly model the system and its environment. Many learning-based control algorithms assume the existence of an initial stabilizing controller in order to simplify their analysis. Such simplifying assumptions are prevalent both in model-based and model-free learning-based control algorithms. However, learning to stabilize is a fundamental problem in learning-based control, with several algorithms tackling this issue.

Understanding the fundamental limits or the corner cases of learning-to-stabilize algorithms can inform future algorithm design and is crucial for applications of these algorithms in safety-critical domains. Therefore, it is important to understand how the system properties affect the performance of the learning-to-stabilize algorithms. In particular, we are interested in the number of samples required to learn a stabilizing controller with a given probability as a performance measure. We say a class of systems is hard to learn to stabilize if this number grows exponentially with the system dimension, independent of the algorithm choice.

## Conclusion and Future Work

In this work, we identified an extended class of LTI systems that are hard to learn to stabilize with static state feedback. The main idea in constructing such examples is to find pairs of systems whose parameters become exponentially close to each other as the dimension increases, yet they are not co-stabilizable. One interesting observation is that the entries of stabilizing gains for these pairs are also growing exponentially (see, Eq. ). In the future, we want to investigate the ramifications of this observation in gradient-based learning algorithms used for control as .

*Acknowledgments:* The authors would like to thank Prof. Peter Seiler of University of Michigan for some early discussions that motivated this work.
