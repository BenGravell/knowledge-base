A Taxonomy for Evaluating Generalist Robot Manipulation Policies

Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks.

## Introduction

Learning-based robotics often comes with the promise of generalization. As an example, an ambitious goal is to train a policy on diverse household data so it can enter a new home and fold laundry. This vision has led to many recent works that train robot policies on diverse datasets via imitation learning with the hope of broad generalization. For example, if a robot encounters an unseen item of clothing in a new home, it should infer how to fold it using its extensive prior experience.

To work towards more comprehensive and systematic evaluations that better capture progress towards deployability, in this work we develop a taxonomy of generalization to guide policy evaluation efforts. To ground our taxonomy, we observe that policies require generalization when there are *perturbations* to the policy's *inputs* or required *outputs*. Thus, our insight is to structure our taxonomy around each input and output modality of a given policy, to more comprehensively consider the various perturbations a policy may need to generalize to.

To this end, we propose $🟊$-Gen (STAR-Gen) -- a Systematic Taxonomy of the Axes of Robot Generalization. $🟊$-Gen is built around the input and output modalities of visuo-lingual control policies, which have three such modalities: vision, language, and actions. Therefore, we categorize perturbations as visual (changes to visual inputs), semantic (changes in language inputs), and behavioral (changes to action outputs). For each combination of these labels (e.g., visual only, or visual + behavioral), we provide more granular generalization *axes* to guide evaluation.

## Discussion

We present $🟊$-Gen, a taxonomy of generalization for robot manipulation. We hope this taxonomy can help improve the comprehensiveness and preciseness of generalization benchmark design as generalist robot policies improve in capabilities. Our taxonomy not only thoroughly considers the space of visuo-lingual policy generalization, but is also straightforward to instantiate in practice.

Larger LLMs can help generalization to a limited extent, primarily for semantic axes.
