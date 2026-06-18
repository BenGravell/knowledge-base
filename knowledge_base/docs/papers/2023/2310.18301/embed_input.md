<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interactive Joint Planning for Autonomous Vehicles

Topics include Autonomous driving, Interaction-aware planning, Trajectory prediction, Motion planning, Neural networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates autonomous-driving planning around ego-conditioned prediction so the planner accounts for how nearby agents may react to the ego plan. The paper contributes a joint planning structure that makes learned interaction models more directly usable in closed-loop decision making.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In highly interactive driving scenarios, the actions of one agent greatly influences those of its neighbors. Planning safe motions for autonomous vehicles in such interactive environments, therefore, requires reasoning about the impact of the ego's intended motion plan on nearby agents' behavior. Deep-learning-based models have recently achieved great success in trajectory prediction and many models in the literature allow for ego-conditioned prediction. However, leveraging ego-conditioned prediction remains challenging in downstream planning due to the complex nature of neural networks, limiting the planner structure to simple ones, e.g., sampling-based planner. Despite their ability to generate fine-grained high-quality motion plans, it is difficult for gradient-based planning algorithms, such as model predictive control (MPC), to leverage ego-conditioned prediction due to their iterative nature and need for gradient. We present Interactive Joint Planning (IJP) that bridges MPC with learned prediction models in a computationally scalable manner to provide us the best of both the worlds. In particular, IJP jointly optimizes over the behavior of the ego and the surrounding agents and leverages deep-learned prediction models as prediction priors that the join trajectory optimization tries to stay close to.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, by leveraging homotopy classes, our joint optimizer searches over diverse motion plans to avoid getting stuck at local minima. Closed-loop simulation result shows that IJP significantly outperforms the baselines that are either without joint optimization or running sampling-based planning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This demo file is intended to serve as a "starter file" for the Robotics: Science and Systems conference papers produced under LATEX using IEEEtran.cls version 1.7a and later.

<!-- chunk {"id": "body-0006", "role": "body", "section": "RSS citations", "weight": 1.0} -->

Please make sure to include `natbib.sty` and to use the `plainnat.bst` bibliography style. `natbib` provides additional citation commands, most usefully `\citet`. For example, rather than the awkward construction

<!-- chunk {"id": "body-0007", "role": "body", "section": "RSS citations", "weight": 1.0} -->

rendered as "\[kalman1960new\] demonstrated...," or the inconvenient

<!-- chunk {"id": "body-0008", "role": "body", "section": "RSS citations", "weight": 1.0} -->

rendered as "Kalman \[kalman1960new\] demonstrated...", one can write

<!-- chunk {"id": "body-0009", "role": "body", "section": "RSS citations", "weight": 1.0} -->

which renders as "kalman1960new demonstrated..." and is both easy to write and much easier to read.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A RSS Hyperlinks", "weight": 1.0} -->

This year, we would like to use the ability of PDF viewers to interpret hyperlinks, specifically to allow each reference in the bibliography to be a link to an online version of the reference.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A RSS Hyperlinks", "weight": 1.0} -->

author = {McGeer, Tad},
title = {\href{ Dynamic Walking}},
journal = {The International Journal of Robotics Research}

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A RSS Hyperlinks", "weight": 1.0} -->

Tad McGeer. Passive Dynamic Walking. The International Journal of Robotics Research, 9:62--82, 1990.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A RSS Hyperlinks", "weight": 1.0} -->

where the title of the article is a link that takes you to the article on IJRR's website.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A RSS Hyperlinks", "weight": 1.0} -->

Linking cited articles will not always be possible, especially for older articles. There are also often several versions of papers online: authors are free to decide what to use as the link destination yet we strongly encourage to link to archival or publisher sites (such as IEEE Xplore or Sage Journals). We encourage all authors to use this feature to the extent possible.
