EGAD! An Evolved Grasping Analysis Dataset for Diversity and Reproducibility in Robotic Manipulation

Topics include Robotics, Datasets, EGAD, Grasping, Greedy randomized adaptive search procedure.

We present the Evolved Grasping Analysis Dataset (EGAD), comprising over 2000 generated objects aimed at training and evaluating robotic visual grasp detection algorithms. The objects in EGAD are geometrically diverse, filling a space ranging from simple to complex shapes and from easy to difficult to grasp, compared to other datasets for robotic grasping, which may be limited in size or contain only a small number of object classes. Additionally, we specify a set of 49 diverse 3D-printable evaluation objects to encourage reproducible testing of robotic grasping systems across a range of complexity and difficulty. The dataset, code and videos can be found at

## Introduction

The ability to grasp previously unseen objects is a fundamental trait for robots that need to interact with their environments, and underpins many higher-level manipulation capabilities. The last few years have seen a large amount of work focused on visual grasp detection, greatly driven by advanced deep learning techniques. As such, the need for diverse object dataset specific to robotic grasping is crucial for both training and evaluating these systems.

The need for large and diverse datasets for training robust deep learning algorithms that generalise well to unknown conditions is widely recognised. However, many current visual grasp detection algorithms are trained on either very small, manually collected datasets, or datasets of objects adapted from other domains with a small number of semantic classes, which may not be representative of the type of challenges faced in robotic grasping.

We presented EGAD, a dataset of over 2000 evolved 3D objects for training and evaluating robotic grasping and manipulation. The objects uniformly fill a space of shape complexity and grasp difficulty, compared to other similar datasets which are limited in both size and diversity. This provides the necessary diversity for training robust visual grasp detection algorithms. Additionally, we specify a diverse evaluation set of 49 objects which are 3D-printable to allow for reproducible testing of grasping algorithms over a wide range of complexity and difficulty.

Using the EGAD evaluation set, we were able to identify a number of limitations of a state-of-the-art grasping algorithm GG-CNN, which has previously not been possible on simpler sets of "household" objects. In future work we propose to use these insights to improve on the baseline results, and to investigate the effect of diverse training data on the robustness of visual grasp detection algorithms.

Our implementation of MAP-Elites begins with a population of randomly initialised CPPNs, which are queried and placed into their respective cells of the search space. At each subsequent iteration, a population is randomly sampled from the search space to undergo evolution and produce a new population of objects, which are subsequently evaluated and assigned to cells in the search space....
