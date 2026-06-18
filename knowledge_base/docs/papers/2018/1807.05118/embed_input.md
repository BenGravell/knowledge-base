Tune: A Research Platform for Distributed Model Selection and Training

Topics include Distributed systems, Learning, Tune, Machine learning, Search algorithm.

Modern machine learning algorithms are increasingly computationally demanding, requiring specialized hardware and distributed computation to achieve high performance in a reasonable time frame. Many hyperparameter search algorithms have been proposed for improving the efficiency of model selection, however their adaptation to the distributed compute environment is often ad-hoc. We propose Tune, a unified framework for model selection and training that provides a narrow-waist interface between training scripts and search algorithms. We show that this interface meets the requirements for a broad range of hyperparameter search algorithms, allows straightforward scaling of search to large clusters, and simplifies algorithm implementation. We demonstrate the implementation of several state-of-the-art hyperparameter search algorithms in Tune. Tune is available at

## Introduction

Machine learning pipelines are growing in complexity and cost. In particular, the model selection stage, which includes model training and hyperparameter tuning, can take the majority of a machine learning practitioner's time and consume vast amounts of computational resources. Take for example a researcher aiming to train ResNet-101, a convolutional neural-network model with millions of parameters. Training this model can take around 24 hours on a single GPU, and performing model selection sequentially will take weeks to complete.

To this end, the research community has developed numerous techniques for accelerating model selection including those that are sequential (Snoek et al. ), parallel (Li et al. ), and both (Jaderberg et al. ). However, each technique is often implemented on its own, tied to a particular framework, is closed source, or perhaps not even reproducible without significant computational resources (Zoph and Le ). Further, often times these techniques require significant investment in software infrastructure for the execution of experiments.

The

We introduce Tune, an open source framework for distributed model selection.

We show how Tune's APIs enable the easy reproduction and integration of a wide variety of state-of-the-art hyperparameter search algorithms.

## Conclusion and Future Work

In this work, we explored the design of a general framework for hyperparameter tuning. We proposed the Tune API and System which supports extensible distributed hyperparameter search algorithms while also being easy for end-user model developers to incorporate into their model design processes. We are actively developing new functionality to help not only in the tuning process but also in analyzing and debugging the intermediate results.
