Robust and Controllable Object-Centric Learning through Energy-based Models

Topics include Robustness, Neural networks, Transformers, Attention mechanisms, Representation learning, Probabilistic models, Accuracy, Generalization, Control, Learning, Machine learning.

Humans are remarkably good at understanding and reasoning about complex visual scenes. The capability to decompose low-level observations into discrete objects allows us to build a grounded abstract representation and identify the compositional structure of the world. Accordingly, it is a crucial step for machine learning models to be capable of inferring objects and their properties from visual scenes without explicit supervision. However, existing works on object-centric representation learning either rely on tailor-made neural network modules or strong probabilistic assumptions in the underlying generative and inference processes. In this work, we present \ours, a conceptually simple and general approach to learning object-centric representations through an energy-based model. By forming a permutation-invariant energy function using vanilla attention blocks readily available in Transformers, we can infer object-centric latent variables via gradient-based MCMC methods where permutation equivariance is automatically guaranteed.

## Introduction

The ability to recognize objects and infer their properties and relations in a scene is a fundamental capability of human cognition. The central question of how objects are discovered and represented in the brain has been a subject of intense research for decades, and has prompted the field of cognitive science to ask how we might develop intelligent machine agents to learn to represent objects in the same way humans do, without being explicitly taught what those objects are.

In recent years, many works have been proposed to learn object-centric representations from visual scenes without human supervision. A variety of models, in the form of structured generative models or specifically designed neural network modules, have been proposed to tackle the problem of visual scene decomposition and generation. On the other hand, recent progress in large language models and visual-language models shows the huge potential of training expressive neural network models with minimal hand-designed inductive biases.

## Contributions

In this work, we introduce EGO (EnerGy-based Object-centric learning), a conceptually simple yet effective approach to learning object-centric representations without the need for specially-tailored neural network architectures or excessive generative modeling (typically parametric) assumptions. Based on the Energy-based Model (EBM) framework, we propose to learn an energy function that takes as input a visual scene and a set of object-centric latent variables and outputs a scalar value that measures the consistency between the observation and the latent representation (Section 2).

## Conclusion

In this work we present EGO, a novel energy-based object-centric learning model. EGO successfully combines three essential ingredients of object-centric learning: (i) minimal assumptions on the generative process, (ii) minimal usage of potentially unexpressive specifically-designed neural modules, and (iii) explicitly modeling randomness to allow one-to-many mappings to reason about occluded or partially-observed objects. We empirically demonstrate that EGO can achieve state-of-the-art performance on various unsupervised object discovery tasks and excels at generalizing to OOD scenes.
