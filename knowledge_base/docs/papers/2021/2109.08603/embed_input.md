Is Curiosity All You Need? On the Utility of Emergent Behaviours from Curious Exploration

Curiosity-based reward schemes can present powerful exploration mechanisms which facilitate the discovery of solutions for complex, sparse or long-horizon tasks. However, as the agent learns to reach previously unexplored spaces and the objective adapts to reward new areas, many behaviours emerge only to disappear due to being overwritten by the constantly shifting objective. We argue that merely using curiosity for fast environment exploration or as a bonus reward for a specific task does not harness the full potential of this technique and misses useful skills. Instead, we propose to shift the focus towards retaining the behaviours which emerge during curiosity-based learning. We posit that these self-discovered behaviours serve as valuable skills in an agent's repertoire to solve related tasks. Our experiments demonstrate the continuous shift in behaviour throughout training and the benefits of a simple policy snapshot method to reuse discovered behaviour for transfer tasks.

## Introduction

Intrinsic motivation can be a powerful concept to endow an agent with an automated mechanism to continuously explore its environment in the absence of task information. One common way to implement intrinsic motivation is to train a predictive model alongside the agent's policy and use the model's prediction error as a reward signal for the agent encouraging the exploration of previously unfamiliar transitions in the environment - a method also known as *curiosity learning*....

However, in environments with multiple possible tasks -- e.g. in manipulation scenarios where objects could be interacted with or re-arranged in different ways -- not only the final behaviour of a curious exploration run might be of interest, but intermediate behaviours can correlate with solutions to different tasks. Naturally, the constantly changing curiosity objective leads to the emergence of diverse behaviours during training -- much akin to the learning process of infants which develop useful skills by playing....

## Conclusion

In this paper we have studied the emerging behaviour when optimising an exploration policy for a curiosity objective derived from a forward-predictive world model. To this end, we have presented SelMo, a curiosity-based, off-policy exploration method and applied it in two continuous control domains: a simulated robotic arm and humanoid robot. We have observed that complex behaviour emerges in both settings and provided a baseline for the utilisation of this self-discovered behaviour in a modular downstream learning scenario....

## Experiments

### World Model

### Emergent Locomotion Behaviour on OP3

Figure 1: Two example timelines depicting the emergence of behaviour while pursuing a curiosity objective on a 9-DoF JACO arm (top) and on a 20-DoF OP3 humanoid robot (bottom). Each timeline represents the evolution of behaviour from a single random seed on a single simulated actor. At each point in time, the agent exhibits a single behaviour which slowly evolves over time as the curiosity objective changes. A detailed description of the emergent behaviour in this experiment is provided in section 4.1 and corresponding quantitative results are shown in figs. 3 and 4. The corresponding videos can be found at:

Despite technical challenges, the discovery of self-induced curricula of skills holds a tantalising prospect for an agent's...
