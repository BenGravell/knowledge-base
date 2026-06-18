Is Curiosity All You Need? On the Utility of Emergent Behaviours from Curious Exploration

Curiosity-based reward schemes can present powerful exploration mechanisms which facilitate the discovery of solutions for complex, sparse or long-horizon tasks. However, as the agent learns to reach previously unexplored spaces and the objective adapts to reward new areas, many behaviours emerge only to disappear due to being overwritten by the constantly shifting objective. We argue that merely using curiosity for fast environment exploration or as a bonus reward for a specific task does not harness the full potential of this technique and misses useful skills. Instead, we propose to shift the focus towards retaining the behaviours which emerge during curiosity-based learning. We posit that these self-discovered behaviours serve as valuable skills in an agent's repertoire to solve related tasks. Our experiments demonstrate the continuous shift in behaviour throughout training and the benefits of a simple policy snapshot method to reuse discovered behaviour for transfer tasks.

## Introduction

Intrinsic motivation can be a powerful concept to endow an agent with an automated mechanism to continuously explore its environment in the absence of task information. One common way to implement intrinsic motivation is to train a predictive model alongside the agent's policy and use the model's prediction error as a reward signal for the agent encouraging the exploration of previously unfamiliar transitions in the environment - a method also known as *curiosity learning*.

In this paper, we study behaviour which emerges based on a curiosity objective in two continuous control settings: manipulation and locomotion. In contrast to prior work in this domain, we implement curiosity-based exploration in an off-policy learning setting which improves upon on-policy implementations in terms of data-efficiency and presumably increases the diversity of emerging behaviours. Furthermore, we look at the utilisation of the self-discovered behaviour for learning new downstream tasks.

In summary, we make the following two contributions: First, we introduce *SelMo*, an off-policy realisation of a self-motivated, curiosity-based method for exploration which is applied to two robotic manipulation and locomotion domains in simulation. We show that even in those complex, 3D environments, meaningful and diverse behaviour emerges solely based on the optimisation of the curiosity objective.

## Discussion

Our experiments have shown that complex manipulation and locomotion behaviour such as grasping, lifting, balancing, sitting and leaping emerges completely unsupervised in an off-policy curiosity learning setup on a 9 DoF robot arm and a 20 DoF humanoid. This observation supports our hypothesis that self-discovered behaviour can provide a valuable skill repertoire for the learning of new downstream tasks.

## Conclusion

In this paper we have studied the emerging behaviour when optimising an exploration policy for a curiosity objective derived from a forward-predictive world model. To this end, we have presented SelMo, a curiosity-based, off-policy exploration method and applied it in two continuous control domains: a simulated robotic arm and humanoid robot. We have observed that complex behaviour emerges in both settings and provided a baseline for the utilisation of this self-discovered behaviour in a modular downstream learning scenario.
