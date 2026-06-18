Activation Functions: Comparison of Trends in Practice and Research for Deep Learning

Topics include Activation functions, Deep learning, Neural networks, Survey analysis, ReLU activations, Deployment, Survey.

This survey frames activation functions through the gap between research proposals and functions actually used in deployed deep-learning architectures. It is less exhaustive than later catalogs, but it is useful for understanding which nonlinearities had practical uptake around the early post-ReLU period.

Deep neural networks have been successfully used in diverse emerging domains to solve real world complex problems with may more deep learning (DL) architectures, being developed to date. To achieve these state-of-the-art performances, the DL architectures use activation functions (AFs), to perform diverse computations between the hidden layers and the output layers of any given DL architecture. This paper presents a survey on the existing AFs used in deep learning applications and highlights the recent trends in the use of the activation functions for deep learning applications. The novelty of this paper is that it compiles majority of the AFs used in DL and outlines the current trends in the applications and usage of these functions in practical deep learning deployments against the state-of-the-art research results. This compilation will aid in making effective decisions in the choice of the most suitable and appropriate activation function for any given application, ready for deployment....

## Introduction

Deep learning algorithms are multi-level representation learning techniques that allows simple non-linear modules to transform representations from the raw input into the higher levels of abstract representations, with many of these transformations producing learned complex functions. The deep learning research was inspired by the limitations of the conventional learning algorithms especially being limited to processing data in raw form, and the human learning techniques by changing the weights of the simulated neural connections on the basis of experiences, obtained from past data.

The use of representation learning, which is the technique that allow machines to discover relationships from raw data, needed to perform certain tasks likes classification and detection. Deep learning, a subfield of machine learning, is more recently being referred to as representation learning in some literature. The direct relationships between deep learning and her associated fields can be shown using the relationship Venn diagram in Figure 1.

The AFs have the capability to improve the learning of the patterns in data thereby automating the process of features detection and justifying their use in the hidden layers of the neural networks, and usefulness for classification purposes across domains.

These activation functions have developed over the years with the compounded activation functions looking towards the future of activation functions research. Furthermore, it is also worthy to state that there are other activation functions that have not been discussed in this literature as we focused was on the activation functions, used in deep learning applications. A future work would be to compare all these state-of-th-art functions on the award-winning architectures, using standard datasets to observe if there would be improved performance results.

The PReLU can be written in compact form as

The tanh functions have been used mostly in recurrent neural networks for natural language processing and speech recognition tasks.

Solving the equation of the modified ELU by constraining the projection during training given the parametric ELU which is given by the relationship

Figure 1: Venn diagram of the components of artificial intelligence

Over the past six decades, machine learning field, a branch of artificial intelligence started rapid expansion and...
