Learning to Drive in a Day

We demonstrate the first application of deep reinforcement learning to autonomous driving. From randomly initialised parameters, our model is able to learn a policy for lane following in a handful of training episodes using a single monocular image as input. We provide a general and easy to obtain reward: the distance travelled by the vehicle without the safety driver taking control. We use a continuous, model-free deep reinforcement learning algorithm, with all exploration and optimisation performed on-vehicle. This demonstrates a new framework for autonomous driving which moves away from reliance on defined logical rules, mapping, and direct supervision. We discuss the challenges and opportunities to scale this approach to a broader range of autonomous driving tasks.

## Introduction

Autonomous driving is a topic that has gathered a great deal of attention from both the research community and companies, due to its potential to radically change mobility and transport. Broadly, most approaches to date focus on formal logic which define driving behaviour in annotated 3D geometric maps. This can be difficult to scale, as it relies heavily on external mapping infrastructure rather than primarily using an understanding of the local scene.

In order to make autonomous driving a truly ubiquitous technology, we advocate for robotic systems which address the ability to drive and navigate in absence of maps and explicit rules, relying - just like humans - on a comprehensive understanding of the immediate environment while following simple higher level directions (e.g., turn-by-turn route commands). Recent work in this area has demonstrated that this is possible on rural country roads, using GPS for coarse localisation and LIDAR to understand the local scene.

In the recent years, reinforcement learning (RL) -- a machine learning subfield focused on solving Markov Decision Problems (MDP) where an agent learns to select actions in an environment in an attempt to maximise some reward function -- has shown an ability to achieve super-human results at games such as Go or chess, a great deal of potential in simulated environments like computer games, and on simple tasks with robotic manipulators. We argue that the generality of reinforcement learning makes it a useful framework to apply to autonomous driving.

## Discussion

This work presents the first application of deep reinforcement learning to a full sized autonomous vehicle. The experiments demonstrate we are able to learn to lane follow with under thirty minutes of training -- all done on on-board computers.

In order to tune hyperparameters, we built a simple simulated driving environment where we experimented with reinforcement learning algorithms, maximising distance before a traffic infraction using DDPG as a canonical algorithm. The parameters found transferred amicably to the real-world, where we rapidly trained a policy to drive a real vehicle on a private road, with a reward signal consisting only of speed and termination upon control driver taking control. Notably, this reward requires no further information or maps of the environment.
