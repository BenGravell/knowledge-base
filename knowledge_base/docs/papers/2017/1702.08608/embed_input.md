Towards a Rigorous Science of Interpretable Machine Learning

Topics include Safety, Learning, Machine learning, Position paper.

As machine learning systems become ubiquitous, there has been a surge of interest in interpretable machine learning: systems that provide explanation for their outputs. These explanations are often used to qualitatively assess other criteria such as safety or non-discrimination. However, despite the interest in interpretability, there is very little consensus on what interpretable machine learning is and how it should be measured. In this position paper, we first define interpretability and describe when interpretability is needed (and when it is not). Next, we suggest a taxonomy for rigorous evaluation and expose open questions towards a more rigorous science of interpretable machine learning.

## Interpretability is used to confirm other important desiderata of ML systems

There exist many auxiliary criteria that one may wish to optimize. Notions of *fairness* or *unbiasedness* imply that protected groups (explicit or implicit) are not somehow discriminated against. *Privacy* means the method protects sensitive information in the data. Properties such as *reliability* and *robustness* ascertain whether algorithms reach certain levels of performance in the face of parameter or input variation. *Causality* implies that the predicted change in output due to a perturbation will occur in the real system.

## Why interpretability? Incompleteness

Not all ML systems require interpretability. Ad servers, postal code sorting, air craft collision avoidance systems---all compute their output without human intervention. Explanation is not necessary either because there are no significant consequences for unacceptable results or the problem is sufficiently well-studied and validated in real applications that we trust the system's decision, even if the system is not perfect.

Scientific Understanding: The human's goal is to gain knowledge. We do not have a complete way of stating what knowledge is; thus the best we can do is ask for explanations we can convert into knowledge.

## Conclusion: Recommendations for Researchers

In this work, we have laid the groundwork for a process to rigorously define and evaluate interpretability. There are many open questions in creating the formal links between applications, the science of human understanding, and more traditional machine learning regularizers. In the mean time, we encourage the community to consider some general principles.

*The claim of the research should match the type of the evaluation.* Just as one would be critical of a reliability-oriented paper that only cites accuracy statistics, the choice of evaluation should match the specificity of the claim being made. A contribution that is focused on a particular application should be expected to be evaluated in the context of that application (application-grounded evaluation), or on a human experiment with a closely-related task (human-grounded evaluation).
