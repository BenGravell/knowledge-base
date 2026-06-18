RoboPianist: Dexterous Piano Playing with Deep Reinforcement Learning

Replicating human-like dexterity in robot hands represents one of the largest open problems in robotics. Reinforcement learning is a promising approach that has achieved impressive progress in the last few years; however, the class of problems it has typically addressed corresponds to a rather narrow definition of dexterity as compared to human capabilities. To address this gap, we investigate piano-playing, a skill that challenges even the human limits of dexterity, as a means to test high-dimensional control, and which requires high spatial and temporal precision, and complex finger coordination and planning. We introduce RoboPianist, a system that enables simulated anthropomorphic hands to learn an extensive repertoire of 150 piano pieces where traditional model-based optimization struggles. We additionally introduce an open-sourced environment, benchmark of tasks, interpretable evaluation metrics, and open challenges for future study. Our website featuring videos, code, and datasets is available at

## Introduction

Despite decades-long research into replicating the dexterity of the human hand, high-dimensional control remains a grand challenge in robotics. This topic has inspired considerable research from both mechanical design and control theoretic points of view. Learning-based approaches have dominated the recent literature, demonstrating proficiency with in-hand cube orientation and manipulation and have scaled to a wide variety of geometries. These tasks, however, correspond to a narrow set of dexterous behaviors relative to the breadth of human capabilities....

In this work, we seek to challenge our methods with tasks commensurate with this complexity and with the goal of emergent human-like dexterous capabilities. To this end, we introduce a family of tasks where success exemplifies many of the properties that we seek in high-dimensional control policies. Our unique desiderata are (i) spatial and temporal precision, (ii) coordination, and (iii) planning....

### Conclusion

In this paper, we introduced RoboPianist, which provides a simulation framework and suite of tasks in the form of a corpus of songs, together with a high-quality baseline and various axes of evaluation, for studying the challenging high-dimensional control problem of mastering piano-playing with two hands. Our results demonstrate the effectiveness of our approach in learning a broad repertoire of musical pieces, and highlight the importance of various design choices required for achieving this performance....

### Constraining the action space

Piano fingering refers to the assignment of fingers to notes, e.g., "C4 played by the index finger of the right hand". Sheet music will typically provide sparse fingering labels for the tricky sections of a piece to help guide pianists, and pianists will often develop their own fingering preferences for a given piece. Since fingering labels aren't available in MIDI files by default, we used annotations from the PIG dataset to create a corpus of $150$ annotated MIDI files for use in the simulated environment....

The quantitative results are shown in Figure 4. We observe that the RoboPianist agent significantly outperforms the MPC baseline, achieving an average F1 score of $0.79$ compared to $0.43$ for MPC....
