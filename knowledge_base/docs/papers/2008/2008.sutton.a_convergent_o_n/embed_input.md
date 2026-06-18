<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Convergent O(n) Temporal-difference Algorithm for Off-policy Learning with Linear Function Approximation

Topics include Temporal difference learning, Off-policy learning, Linear approximation, Gradient method, Reinforcement learning, Convergence.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a convergent linear-time temporal-difference algorithm for off-policy learning with linear function approximation. The paper is a key step toward the gradient-TD family, addressing the instability of classical off-policy TD methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce the first temporal-difference learning algorithm that is stable with linear function approximation and off-policy training, for any finite Markov decision process, target policy, and exciting behavior policy, and whose complexity scales linearly in the number of parameters. We consider an i.i.d.\ policy-evaluation setting in which the data need not come from on-policy experience. The gradient temporal-difference (GTD) algorithm estimates the expected update vector of the TD algorithm and performs stochastic gradient descent on its L_2 norm. Our analysis proves that its expected update is in the direction of the gradient, assuring convergence under the usual stochastic approximation conditions to the same least-squares solution as found by the LSTD, but without its quadratic computational complexity. GTD is online and incremental, and does not involve multiplying by products of likelihood ratios as in importance-sampling methods.
