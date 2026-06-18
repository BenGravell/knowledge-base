A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

Topics include Imitation learning, Online learning, No-regret learning, Structured prediction, Policy learning, DAgger.

Introduces DAgger, reducing imitation learning to no-regret online learning by repeatedly aggregating states visited by the learned policy and querying the expert there. The method directly addresses covariate shift between expert demonstrations and learner rollouts.

Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning. This leads to poor performance in theory and often in practice. Some recent approaches provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train either non-stationary or stochastic policies and require a large number of iterations. In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting. We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings. We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.

## INTRODUCTION

Sequence Prediction problems arise commonly in practice. For instance, most robotic systems must be able to predict/make a sequence of actions given a sequence of observations revealed to them over time. In complex robotic systems where standard control methods fail, we must often resort to learning a controller that can make such predictions. Imitation learning techniques, where expert demonstrations of good behavior are used to learn a controller, have proven very useful in practice and have led to state-of-the art performance in a variety of applications....

Ignoring this issue leads to poor performance both in theory and practice. In particular, a classifier that makes a mistake with probability $\epsilon$ under the distribution of states/observations encountered by the expert can make as many as $T^{2}\epsilon$ mistakes in expectation over $T$-steps under the distribution of states the classifier itself induces. Intuitively this is because as soon as the learner makes a mistake, it may encounter completely different observations than those under expert demonstration, leading to a compounding of errors.

## FUTURE WORK

We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAgger approach can provide a learning reduction with strong performance guarantees in both imitation learning and structured prediction. In future work, we will consider more sophisticated strategies than simple greedy forward decoding for structured prediction, as well as using base classifiers that rely on Inverse Optimal Control techniques to learn a cost function for a planner to aid prediction in imitation learning....

A more refined analysis taking advantage of the strong convexity of the loss function may lead to tighter generalization bounds that require $N$ only of order $\overset{\sim}{O}{({T{\log{({1/\delta})}}})}$. Similarly:

SMILe, proposed by Ross and Bagnell, alleviates this problem and can be applied in practice when $T$ is large or undefined by adopting an approach similar to SEARN where a stochastic stationary policy is trained over several iterations. Initially SMILe starts with a policy $\pi_{0}$ which always queries and executes the expert's action choice....
