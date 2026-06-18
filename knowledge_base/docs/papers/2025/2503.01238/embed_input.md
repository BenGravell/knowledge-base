A Taxonomy for Evaluating Generalist Robot Manipulation Policies

Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks....

## Introduction

Learning-based robotics often comes with the promise of generalization. As an example, an ambitious goal is to train a policy on diverse household data so it can enter a new home and fold laundry. This vision has led to many recent works that train robot policies on diverse datasets via imitation learning with the hope of broad generalization. For example, if a robot encounters an unseen item of clothing in a new home, it should infer how to fold it using its extensive prior experience....

In pursuit of reliable and broad generalization, recent work has focused on scaling up data collection and developing more expressive models, following the successes of other machine learning fields. Although these advances have led to more capable policies that certainly generalize to some novel scenarios, it is often unclear from existing evaluations how generalist these policies truly are.

Limitations and Future Work. Due to constraints imposed by real-world evaluation time (1600+ trials), we only evaluate a subset of factors and their compositions that we believe most effectively demonstrate the benefits of $🟊$-Gen. We hope that future work can build more benchmarks based our taxonomy, such as by considering datasets that support more complex behavior and diverse settings like DROID. Also, we still design our evaluation conditions in BridgeV2-$🟊$ using human oversight, leaving room for possible bias....

While we consider $🟊$-Gen to be a strong starting point, we believe that future work can revise and expand our taxonomy based on the needs of robotics practitioners. Also, while we show that $🟊$-Gen can help prove insights about current generalist policies and their design decisions, we also hope that $🟊$-Gen can help inform data collection efforts to achieve the forms of generalization considered in our taxonomy.

Visual + Behavioral: These factors and axes affect the initial image and required behavior, without changing the language instruction. As we show in Section IV-B, many factors that prior work consider as "behavior" generalization fall into this category. Example factors include manipulated object poses and surface/table heights (see the cyan sector of Fig. 1).

Changes to camera viewpoints.
camera pose, partial occlusion
