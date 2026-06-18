CORL: A Continuous-state Offset-dynamics Reinforcement Learner

Topics include Reinforcement learning, Continuous state spaces, Offset dynamics, Sample complexity, Fitted value iteration, Robotic driving, Probably approximately correct learning.

Introduces CORL for learning continuous-state MDPs whose dynamics switch among offset models, giving PAC-style sample-complexity bounds that include the cost of approximate planning. The paper is a bridge between theoretical RL and robotics because it learns a structured transition model, solves it with fitted value iteration, and demonstrates the representation on a robotic car over varying terrain.

Continuous state spaces and stochastic, switching dynamics characterize a number of rich, realworld domains, such as robot navigation across varying terrain. We describe a reinforcementlearning algorithm for learning in these domains and prove for certain environments the algorithm is probably approximately correct with a sample complexity that scales polynomially with the state-space dimension. Unfortunately, no optimal planning techniques exist in general for such problems; instead we use fitted value iteration to solve the learned MDP, and include the error due to approximate planning in our bounds. Finally, we report an experiment using a robotic car driving over varying terrain to demonstrate that these dynamics representations adequately capture real-world dynamics and that our algorithm can be used to efficiently solve such problems.

Learn about arXiv becoming an independent nonprofit.{target="_blank"}

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate

All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text

## quick links

## Computer Science \> Machine Learning

## Title:CORL: A Continuous-state Offset-dynamics Reinforcement Learner

Authors:Emma Brunskill{rel="nofollow"}, Bethany Leffler{rel="nofollow"}, Lihong Li{rel="nofollow"}, Michael L. Littman{rel="nofollow"}, Nicholas Roy{rel="nofollow"}

View a PDF of the paper titled CORL: A Continuous-state Offset-dynamics Reinforcement Learner, by Emma Brunskill and 4 other authors

> Abstract:Continuous state spaces and stochastic, switching dynamics characterize a number of rich, realworld domains, such as robot navigation across varying terrain. We describe a reinforcementlearning algorithm for learning in these domains and prove for certain environments the algorithm is probably approximately correct with a sample complexity that scales polynomially with the state-space dimension. Unfortunately, no optimal planning techniques exist in general for such problems; instead we use fitted value iteration to solve the learned MDP, and include the error due to approximate planning in our bounds. Finally, we report an experiment using a robotic car driving over varying terrain to demonstrate that these dynamics representations adequately capture real-world dynamics and that our algorithm can be used to efficiently solve such problems.

Subjects: Machine Learning (cs.LG); Machine Learning (stat.ML)

## Submission history

From: Emma Brunskill \[view email{rel="nofollow"}\] \[via AUAI proxy\]\
**\[v1\]** Wed, 13 Jun 2012 12:32:13 UTC (425 KB)\

## Access Paper

### Current browse context
