On the Hardness of Learning to Stabilize Linear Systems

Topics include Linear systems, Stabilization, Sample complexity, System identification, Robust control, Machine learning theory, Control theory.

Constructs linear-system classes where learning a stabilizing controller is statistically hard even when identification itself is not the bottleneck. The paper separates stabilization difficulty from estimation difficulty by tying the lower bound to co-stabilizability and robust-control structure.

Inspired by the work of Tsiamis et al. \cite{tsiamis2022learning}, in this paper we study the statistical hardness of learning to stabilize linear time-invariant systems. Hardness is measured by the number of samples required to achieve a learning task with a given probability. The work in \cite{tsiamis2022learning} shows that there exist system classes that are hard to learn to stabilize with the core reason being the hardness of identification. Here we present a class of systems that can be easy to identify, thanks to a non-degenerate noise process that excites all modes, but the sample complexity of stabilization still increases exponentially with the system dimension. We tie this result to the hardness of co-stabilizability for this class of systems using ideas from robust control.

## INTRODUCTION

Learning-based control plays an increasingly important role in many application domains such as power systems, robotics, self-driving cars, where it might be hard to perfectly model the system and its environment. Many learning-based control algorithms assume the existence of an initial stabilizing controller in order to simplify their analysis. Such simplifying assumptions are prevalent both in model-based and model-free learning-based control algorithms. However, learning to stabilize is a fundamental problem in learning-based control, with several algorithms tackling this issue.

Understanding the fundamental limits or the corner cases of learning-to-stabilize algorithms can inform future algorithm design and is crucial for applications of these algorithms in safety-critical domains. Therefore, it is important to understand how the system properties affect the performance of the learning-to-stabilize algorithms. In particular, we are interested in the number of samples required to learn a stabilizing controller with a given probability as a performance measure. We say a class of systems is hard to learn to stabilize if this number grows exponentially with the system dimension, independent of the algorithm choice.

Therefore, we can apply Lemma 5. ‣ -C Proof of Theorem 1 ‣ V Conclusion and Future Work ‣ On the Hardness of Learning to Stabilize Linear Systems") to obtain

Combining and, we have that holds only if

### IV-A Certainty Equivalent LQR

### Remark 2

Consider the following order $n$ single-input controllable system $(\mathbf{A},\mathbf{B})$ with state feedback $\mathbf{K} \in {\mathbb{R}}^{1 \times n}$:

We focus on fully observed linear time-invariant systems and consider the task of learning a static stabilizing linear state-feedback controller from a single trajectory. In this setting, Tsiamis et al. show that when the process noise is degenerate, i.e. the noise covariance matrix being singular, there are some classes of systems that are hard to learn to stabilize, by transferring the hardness of learning-to-stabilize into the hardness of system identification. The system classes constructed in their work are based on a (marginally) stable hard-to-stabilize pair....

Notation: We use lower case, lower case boldface, and upper case boldface letters to denote scalars, vectors, and matrices respectively....
