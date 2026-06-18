RoboPianist: Dexterous Piano Playing with Deep Reinforcement Learning

Replicating human-like dexterity in robot hands represents one of the largest open problems in robotics. Reinforcement learning is a promising approach that has achieved impressive progress in the last few years; however, the class of problems it has typically addressed corresponds to a rather narrow definition of dexterity as compared to human capabilities. To address this gap, we investigate piano-playing, a skill that challenges even the human limits of dexterity, as a means to test high-dimensional control, and which requires high spatial and temporal precision, and complex finger coordination and planning. We introduce RoboPianist, a system that enables simulated anthropomorphic hands to learn an extensive repertoire of 150 piano pieces where traditional model-based optimization struggles. We additionally introduce an open-sourced environment, benchmark of tasks, interpretable evaluation metrics, and open challenges for future study. Our website featuring videos, code, and datasets is available at

## Introduction

Despite decades-long research into replicating the dexterity of the human hand, high-dimensional control remains a grand challenge in robotics. This topic has inspired considerable research from both mechanical design and control theoretic points of view. Learning-based approaches have dominated the recent literature, demonstrating proficiency with in-hand cube orientation and manipulation and have scaled to a wide variety of geometries. These tasks, however, correspond to a narrow set of dexterous behaviors relative to the breadth of human capabilities.

In this work, we seek to challenge our methods with tasks commensurate with this complexity and with the goal of emergent human-like dexterous capabilities. To this end, we introduce a family of tasks where success exemplifies many of the properties that we seek in high-dimensional control policies. Our unique desiderata are (i) spatial and temporal precision, (ii) coordination, and (iii) planning.

We propose RoboPianist, an end-to-end system that leverages deep reinforcement learning (RL) to synthesize policies capable of playing a diverse repertoire of musical pieces on the piano. We show that a combination of careful system design and human priors (in the form of fingering annotations) is crucial to its performance. Furthermore, we introduce RoboPianist-repertoire-150, a benchmark of 150 songs, which allows us to comprehensively evaluate our proposed system and show that it surpasses a strong model-based approach by over $83\%$.

## Experimental Setup

In this section, we introduce the simulated piano-playing environment as well as the musical suite used to train and evaluate our agent.

## Limitations

While RoboPianist produces agents that push the boundaries of bi-manual dexterous control, it does so in a simplified simulation of the real world. For example, the velocity of a note, which modulates the strength of the key press, is ignored in the current reward formulation. Thus, the dynamic markings of the composition are ignored. Furthermore, our RL training approach can be considered wasteful, in that we learn by attempting to play the entire piece at the start of every episode, rather than focusing on the parts of the song that need more practicing.
