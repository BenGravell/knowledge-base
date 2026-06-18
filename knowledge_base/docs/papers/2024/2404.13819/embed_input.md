HOIST-Former: Hand-Held Objects Identification, Segmentation, and Tracking in the Wild

Topics include Video understanding, Object segmentation, Object tracking, Hand-object interaction, Transformers, In-the-wild datasets, Instance segmentation, Human-object interaction.

Targets the difficult video problem of identifying, segmenting, and tracking objects being held by hands, where occlusion and hand-offs make standard trackers brittle. HOIST-Former couples hand and object features through iterative pooling and contact-aware training, and the paper also contributes the HOIST in-the-wild video dataset.

We address the challenging task of identifying, segmenting, and tracking hand-held objects, which is crucial for applications such as human action segmentation and performance evaluation. This task is particularly challenging due to heavy occlusion, rapid motion, and the transitory nature of objects being hand-held, where an object may be held, released, and subsequently picked up again. To tackle these challenges, we have developed a novel transformer-based architecture called HOIST-Former. HOIST-Former is adept at spatially and temporally segmenting hands and objects by iteratively pooling features from each other, ensuring that the processes of identification, segmentation, and tracking of hand-held objects depend on the hands' positions and their contextual appearance. We further refine HOIST-Former with a contact loss that focuses on areas where hands are in contact with objects. Moreover, we also contribute an in-the-wild video dataset called HOIST, which comprises 4,125 videos complete with bounding boxes, segmentation masks, and tracking IDs for hand-held objects....

## Introduction

Humans primarily use their hands to interact with their surroundings, making the ability to segment and track hand-held objects crucial for understanding and interpreting human interactions with the environment. From monitoring a factory worker navigating through assembly tasks to evaluating the skill set of a resident doctor performing intricate medical operations, the dynamic interplay between hands and objects forms the core of many activities....

In this paper, we study the problem of jointly segmenting and tracking objects that are held and moved by hands in unconstrained videos, as illustrated in Fig. 1. Specifically, given an input video composed of a sequence of frames, we consider all portable objects that are held by hands at any point within these frames. Suppose there are a number of such object instances. For each object instance, our objective is to produce a series of binary segmentation masks corresponding to each frame, such that the mask for a particular frame is empty if the object instance is not being held by a hand in that frame....

## Conclusions

In this paper, we tackled the task of identifying, segmenting, and tracking hand-held objects. We introduced HOIST-Former, an innovative transformer-based architecture, adept at segmenting hands and objects by pooling features based on their positions and context. This approach is further refined with a contact loss that emphasizes areas where hands contact objects. We also presented the HOIST dataset, comprising 4,125 in-the-wild videos with comprehensive annotations. Our experiments on HOIST and two other public datasets showcased HOIST-Former's effectiveness in hand-held object segmentation and tracking.

Dataset Source. Our goal is to compile a sufficiently large and diverse video dataset to develop methods for detecting, segmenting, and tracking hand-held objects. Specifically, we aim for the dataset to satisfy several criteria. First, it should include videos of everyday activities in diverse indoor and outdoor environments. Second, the videos should feature people interacting with a wide range of objects....

The function $MaskAtt{(\mathbf{X},\left. \mathbf{M} \middle| f \right.)}$ operates with two inputs: the query set $X$ and the collection of spatio-temporal binary masks $\mathbf{M}$....
