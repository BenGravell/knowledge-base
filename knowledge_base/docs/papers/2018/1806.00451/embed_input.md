Do CIFAR-10 Classifiers Generalize to CIFAR-10?

Topics include Deep learning, Classifiers, Accuracy, Learning, Machine learning, Test set.

Machine learning is currently dominated by largely experimental work focused on improvements in a few key tasks. However, the impressive accuracy numbers of the best performing models are questionable because the same test sets have been used to select these models for multiple years now. To understand the danger of overfitting, we measure the accuracy of CIFAR-10 classifiers by creating a new test set of truly unseen images. Although we ensure that the new test set is as close to the original data distribution as possible, we find a large drop in accuracy (4% to 10%) for a broad range of deep learning models. Yet more recent models with higher original accuracy show a smaller drop and better overall performance, indicating that this drop is likely not due to overfitting based on adaptivity. Instead, we view our results as evidence that current accuracy numbers are brittle and susceptible to even minute natural variations in the data distribution.

## Introduction

Over the past five years, machine learning has become a decidedly experimental field. Driven by a surge of research in deep learning, the majority of published papers has embraced a paradigm where the main justification for a new learning technique is its improved performance on a few key benchmarks. At the same time, there are few explanations as to *why* a proposed technique is a reliable improvement over prior work. Instead, our sense of progress largely rests on a small number of standard benchmarks such as CIFAR-10, ImageNet, or MuJoCo. This raises a crucial question:

*How reliable are our current measures of progress in machine learning?*

Concrete future experiments should explore whether the competition approach is similarly resilient to overfitting on other datasets (e.g., ImageNet) and other tasks (such as language modeling). An important aspect here is to ensure that the data distribution of a new test set stays as close to the original dataset as possible. Furthermore, we should understand what types of naturally occurring distribution shifts are challenging for image classifiers. For instance, are there certain sub-populations that the models fail to learn on CIFAR-10 but appear trivial to a human?...

More broadly, we view our results as motivation for a more thorough evaluation of machine learning research. Currently, the dominant paradigm is to propose a new algorithm and evaluate its performance on existing data. Unfortunately, there is often little understanding to what extent the improvements are broadly applicable. To truly understand *generalization* questions, more studies should collect insightful new data and evaluate existing algorithms on such data....

Our main results are summarized in Table 1 and Figure 2. We now describe the two important trends here and then discuss our results in Section 6.

Our overall goal was to create a new test set that is as close as possible to being drawn from the same distribution as the original CIFAR-10 dataset. One crucial aspect here is that the CIFAR-10 dataset did not exhaust any of the Tiny Image keywords it is drawn from. So by collecting new images from the same keywords as CIFAR-10, our new test set can match the sub-class distribution of the original dataset.

## Explaining the Gap
