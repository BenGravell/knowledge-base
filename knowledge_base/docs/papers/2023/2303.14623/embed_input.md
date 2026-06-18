Inverse Reinforcement Learning without Reinforcement Learning

Inverse Reinforcement Learning (IRL) is a powerful set of techniques for imitation learning that aims to learn a reward function that rationalizes expert demonstrations. Unfortunately, traditional IRL methods suffer from a computational weakness: they require repeatedly solving a hard reinforcement learning (RL) problem as a subroutine. This is counter-intuitive from the viewpoint of reductions: we have reduced the easier problem of imitation learning to repeatedly solving the harder problem of RL. Another thread of work has proved that access to the side-information of the distribution of states where a strong policy spends time can dramatically reduce the sample and computational complexities of solving an RL problem. In this work, we demonstrate for the first time a more informed imitation learning reduction where we utilize the state distribution of the expert to alleviate the global exploration component of the RL subroutine, providing an exponential speedup in theory. In practice, we find that we are able to significantly speed up the prior art on continuous control tasks.

## Introduction

Inverse Reinforcement Learning (IRL), also known as Inverse Optimal Control (Kalman Bagnell, ) or Structural Estimation, is the problem of finding a reward function that rationalizes (i.e. makes optimal) demonstrated behavior. Such approaches build on the lengthy history of trying to understand intelligent behavior as approximate optimization of some cost function. While economists and cognitive scientists are often interested in analyzing the recovered reward function, it is more common in machine learning to view IRL algorithms as methods to imitate or forecast expert behavior.

There are three key benefits to the IRL approach to imitation. The first is policy space structuring: effectively, IRL reduces our (often large) policy class to just those policies that are (approximately) optimal under some member of our (relatively small) reward function class.

Another is to address an assumption fundamental to our approach: the ability to reset the learner to an arbitrary initial state. While this is possible in many (if not most) simulators, it is not clear how to do this in the real world or when one only has the \"trace\" model of access (i.e. resets only to a fixed initial state distribution).

Lastly, one could also further investigate where sub-optimal data could be used in our procedure. For example, one could mix it with the expert data and use this mixture distribution for resets if only a limited number of demonstrations are available. As long as we still use the expert data for reward selection, we conjecture that similar guarantees to the ones we prove above would hold.

Input: Sequence of expert visitation distributions ρE1…ρET, Policy class Π, Reward class ℱr
Output: Trained policy π
Sample random time t ∼ Unif([0,T]) and start state st ∼ ρEt.
Execute a random action at ∼ Unif(𝒜) in st.
Follow πi − 1 until the end of the horizon.

### Theorem 3.1

Thus, regardless of the desired $\overline{\epsilon}$, the outer loop will eventually terminate, with $\overline{\epsilon} \propto \frac{1}{\sqrt{N}}$ or $\overline{\epsilon} \propto \frac{\log{(N)}}{N}$ for a wide set of problems, giving us poly-time bounds. There exist two variations of NRMM: one in which the adversary plays a best-response (i.e....
