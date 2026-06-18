Beyond Sparsity: Tree Regularization of Deep Models for Interpretability

Topics include Accuracy, Decision trees.

The lack of interpretability remains a key barrier to the adoption of deep models in many applications. In this work, we explicitly regularize deep models so human users might step through the process behind their predictions in little time. Specifically, we train deep time-series models so their class-probability predictions have high accuracy while being closely modeled by decision trees with few nodes. Using intuitive toy examples as well as medical tasks for treating sepsis and HIV, we demonstrate that this new tree regularization yields models that are easier for humans to simulate than simpler L1 or L2 penalties without sacrificing predictive power.

## Introduction

Deep models have become the de-facto approach for prediction in a variety of applications such as image classification (e.g. (?)) and machine translation (e.g. (?; ?)). However, many practitioners are reluctant to adopt deep models because their predictions are difficult to interpret. In this work, we seek a specific form of interpretability known as *human-simulability*. A human-simulatable model is one in which a human user can "take in input data together with the parameters of the model and in reasonable time step through every calculation required to produce a prediction" (?)....

The question of creating accurate yet human-simulatable models is an important one, because in many domains simulatability is paramount. For example, despite advances in deep learning for clinical decision support (e.g. (?; ?; ?)), the clinical community remains skeptical of machine learning systems (?). Simulatability allows clinicians to audit predictions easily. They can manually inspect changes to outputs under slightly-perturbed inputs, check substeps against their expert knowledge, and identify when predictions are made due to systemic bias in the data rather than real causes....

We have introduced a novel tree-regularization technique that encourages the complex decision boundaries of any differentiable model to be well-approximated by human-simulatable functions, allowing domain experts to quickly understand and approximately *compute* what the more complex model is doing. Overall, our training procedure is robust and efficient; future work could continue to explore and increase the stability of the learned models as well as identify ways to apply our approach to situations in which the inputs are not inherently interpretable (e.g. pixels in an image).

Across three complex, real-world domains -- HIV treatment, sepsis treatment, and human speech processing -- our tree-regularized models provide gains in prediction accuracy in the regime of simpler, approximately human-simulatable models. Future work could apply tree regularization to local, example-specific approximations of a loss (?) or to representation learning tasks (encouraging embeddings with simple boundaries)....

Fig. 2 (b) shows the each trained model as a single point in a 2D fitness space: the x-axis measures model complexity via our average-path-length metric, and the y-axis...
