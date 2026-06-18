Interactive Joint Planning for Autonomous Vehicles

Topics include Autonomous driving, Interaction-aware planning, Trajectory prediction, Motion planning, Neural networks.

Formulates autonomous-driving planning around ego-conditioned prediction so the planner accounts for how nearby agents may react to the ego plan. The paper contributes a joint planning structure that makes learned interaction models more directly usable in closed-loop decision making.

In highly interactive driving scenarios, the actions of one agent greatly influences those of its neighbors. Planning safe motions for autonomous vehicles in such interactive environments, therefore, requires reasoning about the impact of the ego's intended motion plan on nearby agents' behavior. Deep-learning-based models have recently achieved great success in trajectory prediction and many models in the literature allow for ego-conditioned prediction. However, leveraging ego-conditioned prediction remains challenging in downstream planning due to the complex nature of neural networks, limiting the planner structure to simple ones, e.g., sampling-based planner. Despite their ability to generate fine-grained high-quality motion plans, it is difficult for gradient-based planning algorithms, such as model predictive control (MPC), to leverage ego-conditioned prediction due to their iterative nature and need for gradient. We present Interactive Joint Planning (IJP) that bridges MPC with learned prediction models in a computationally scalable manner to provide us the best of both the worlds.

## Introduction

This demo file is intended to serve as a "starter file" for the Robotics: Science and Systems conference papers produced under LATEX using IEEEtran.cls version 1.7a and later.

## RSS citations

Please make sure to include `natbib.sty` and to use the `plainnat.bst` bibliography style. `natbib` provides additional citation commands, most usefully `\citet`. For example, rather than the awkward construction

rendered as "\[kalman1960new\] demonstrated...," or the inconvenient

rendered as "Kalman \[kalman1960new\] demonstrated...", one can write

which renders as "kalman1960new demonstrated..." and is both easy to write and much easier to read.

## III-A RSS Hyperlinks

This year, we would like to use the ability of PDF viewers to interpret hyperlinks, specifically to allow each reference in the bibliography to be a link to an online version of the reference.

author = {McGeer, Tad},
title = {\href{ Dynamic Walking}},
journal = {The International Journal of Robotics Research}

and

Tad McGeer. Passive Dynamic Walking. The International Journal of Robotics Research, 9:62--82, 1990.

where the title of the article is a link that takes you to the article on IJRR's website.

Linking cited articles will not always be possible, especially for older articles. There are also often several versions of papers online: authors are free to decide what to use as the link destination yet we strongly encourage to link to archival or publisher sites (such as IEEE Xplore or Sage Journals). We encourage all authors to use this feature to the extent possible.
