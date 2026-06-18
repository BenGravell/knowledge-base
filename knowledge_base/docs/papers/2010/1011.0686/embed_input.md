A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

Topics include Imitation learning, Online learning, No-regret learning, Structured prediction, Policy learning, DAgger.

Introduces DAgger, reducing imitation learning to no-regret online learning by repeatedly aggregating states visited by the learned policy and querying the expert there. The method directly addresses covariate shift between expert demonstrations and learner rollouts.

Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning. This leads to poor performance in theory and often in practice. Some recent approaches provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train either non-stationary or stochastic policies and require a large number of iterations. In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting. We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings. We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.

## INTRODUCTION

Sequence Prediction problems arise commonly in practice. For instance, most robotic systems must be able to predict/make a sequence of actions given a sequence of observations revealed to them over time. In complex robotic systems where standard control methods fail, we must often resort to learning a controller that can make such predictions. Imitation learning techniques, where expert demonstrations of good behavior are used to learn a controller, have proven very useful in practice and have led to state-of-the art performance in a variety of applications.

Recent approaches can guarantee an expected number of mistakes linear (or nearly so) in the task horizon $T$ and error $\epsilon$ by training over several iterations and allowing the learner to influence the input states where expert demonstration is provided (through execution of its own controls in the system). One approach learns a non-stationary policy by training a different policy for each time step in sequence, starting from the first step. Unfortunately this is impractical when $T$ is large or ill-defined.

We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number of mistakes/costs that grows linearly in $T$ and classification cost $\epsilon$). We take a reduction-based approach that enables reusing existing supervised learning algorithms. Our approach is simple to implement, has no free parameters except the supervised learning algorithm sub-routine, and requires a number of iterations that scales nearly linearly with the effective horizon of the problem. It naturally handles continuous as well as discrete predictions.

## FUTURE WORK

We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAgger approach can provide a learning reduction with strong performance guarantees in both imitation learning and structured prediction. In future work, we will consider more sophisticated strategies than simple greedy forward decoding for structured prediction, as well as using base classifiers that rely on Inverse Optimal Control techniques to learn a cost function for a planner to aid prediction in imitation learning.
