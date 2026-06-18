Tune: A Research Platform for Distributed Model Selection and Training

Topics include Distributed systems, Learning, Tune, Machine learning, Search algorithm.

Modern machine learning algorithms are increasingly computationally demanding, requiring specialized hardware and distributed computation to achieve high performance in a reasonable time frame. Many hyperparameter search algorithms have been proposed for improving the efficiency of model selection, however their adaptation to the distributed compute environment is often ad-hoc. We propose Tune, a unified framework for model selection and training that provides a narrow-waist interface between training scripts and search algorithms. We show that this interface meets the requirements for a broad range of hyperparameter search algorithms, allows straightforward scaling of search to large clusters, and simplifies algorithm implementation. We demonstrate the implementation of several state-of-the-art hyperparameter search algorithms in Tune. Tune is available at

## Introduction

Machine learning pipelines are growing in complexity and cost. In particular, the model selection stage, which includes model training and hyperparameter tuning, can take the majority of a machine learning practitioner's time and consume vast amounts of computational resources. Take for example a researcher aiming to train ResNet-101, a convolutional neural-network model with millions of parameters. Training this model can take around 24 hours on a single GPU, and performing model selection sequentially will take weeks to complete. Naturally, one would be inclined to train the model on a cluster in a distributed fashion (Goyal et al....

To this end, the research community has developed numerous techniques for accelerating model selection including those that are sequential (Snoek et al. ), parallel (Li et al. ), and both (Jaderberg et al. ). However, each technique is often implemented on its own, tied to a particular framework, is closed source, or perhaps not even reproducible without significant computational resources (Zoph and Le ). Further, often times these techniques require significant investment in software infrastructure for the execution of experiments.

## Conclusion and Future Work

In this work, we explored the design of a general framework for hyperparameter tuning. We proposed the Tune API and System which supports extensible distributed hyperparameter search algorithms while also being easy for end-user model developers to incorporate into their model design processes. We are actively developing new functionality to help not only in the tuning process but also in analyzing and debugging the intermediate results.

Tune can also directly control trial execution if the user extends the trainable model class (Figure 2). Here, training steps, checkpointing, and restore are implemented as class methods which Tune schedulers call to incrementally train models. This mode of execution has some debuggability advantages over cooperative control; we offer both to users. Internally, Tune inserts adapters over the cooperative interface to provide a facade of direct control to trial schedulers.

For a good user experience, the following features are also necessary:

[⬇](data:text/plain;base64,Y2xhc3MgVHJpYWxTY2hlZHVsZXI6CiAgICBkZWYgb25fcmVzdWx0KHNlbGYsIHRyaWFsLCByZXN1bHQpOiAuLi4KICAgIGRlZiBjaG9vc2VfdHJpYWxfdG9fcnVuKHNlbGYpOiAuLi4=){do...
