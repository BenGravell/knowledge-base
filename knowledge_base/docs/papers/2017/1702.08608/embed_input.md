Towards a Rigorous Science of Interpretable Machine Learning

Topics include Safety, Learning, Machine learning, Position paper.

As machine learning systems become ubiquitous, there has been a surge of interest in interpretable machine learning: systems that provide explanation for their outputs. These explanations are often used to qualitatively assess other criteria such as safety or non-discrimination. However, despite the interest in interpretability, there is very little consensus on what interpretable machine learning is and how it should be measured. In this position paper, we first define interpretability and describe when interpretability is needed (and when it is not). Next, we suggest a taxonomy for rigorous evaluation and expose open questions towards a more rigorous science of interpretable machine learning.

## What is Interpretability?

### Definition

Interpret means *to explain or to present in understandable terms*.^33^3Merriam-Webster dictionary, accessed 2017-02-07 In the context of ML systems, we define interpretability as the *ability to explain or to present in understandable terms to a human*. A formal definition of explanation remains elusive; in the field of psychology, Lombrozo states "explanations are... the currency in which we exchanged beliefs" and notes that questions such as what constitutes an explanation, what makes some explanations better than others, how explanations are generated and when explanations are sought are just beginning to be addressed....

What are method-related relevant factors being explored? (e.g. form of cognitive chunks, number of cognitive chunks, compositionality, monotonicity, uncertainty; Section 4.3)

and of course, adding and refining these factors as our taxonomies evolve. These considerations should move us away from vague claims about the interpretability of a particular model and toward classifying applications by a common set of terms.

## Open Problems in the Science of Interpretability, Theory and Practice

### Human-grounded Metrics: Real humans, simplified tasks

### Hypothesis: task-related latent dimensions of interpretability

### Interpretability is used to confirm other important desiderata of ML systems

There exist many auxiliary criteria that one may wish to optimize. Notions of *fairness* or *unbiasedness* imply that protected groups (explicit or implicit) are not somehow discriminated against. *Privacy* means the method protects sensitive information in the data. Properties such as *reliability* and *robustness* ascertain whether algorithms reach certain levels of performance in the face of parameter or input variation. *Causality* implies that the predicted change in output due to a perturbation will occur in the real system. *Usable* methods provide information that assist users to accomplish a task---e.g....

## Why interpretability? Incompleteness

Not all ML systems require interpretability. Ad servers, postal code sorting, air craft collision avoidance systems---all compute their output without human intervention. Explanation is not necessary either because there are no significant consequences for unacceptable results or the problem is sufficiently well-studied and validated in real...
