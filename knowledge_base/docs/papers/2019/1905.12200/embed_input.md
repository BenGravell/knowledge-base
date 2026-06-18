A Topology Layer for Machine Learning

Topics include Deep learning, Learning.

Topology applied to real world data using persistent homology has started to find applications within machine learning, including deep learning. We present a differentiable topology layer that computes persistent homology based on level set filtrations and edge-based filtrations. We present three novel applications: the topological layer can (i) regularize data reconstruction or the weights of machine learning models, (ii) construct a loss on the output of a deep generative network to incorporate topological priors, and (iii) perform topological adversarial attacks on deep networks trained with persistence features. The code (www.github.com/bruel-gabrielsson/TopologyLayer) is publicly available and we hope its availability will facilitate the use of persistent homology in deep learning and other gradient based applications.

## Introduction

Persistent homology, or simply persistence, is a well-established tool in applied and computational topology. In a deep learning setting, persistence has mainly been used as preprocessing to provide topological features for learning. There has been work that uses differentiable properties of persistence to incorporate topological information in deep learning and regularization; however, such work has focused on specialized applications and specific functions of the persistence diagrams....

In many deep learning settings there is a natural topological perspective, including images and for 3D data such as point clouds or voxel spaces. In fact, many of the failure cases of generative models are topological in nature. We show how topological priors can be used to improve such models. It has been speculated that models that rely on topological features might have desirable properties besides test accuracy; one such property has been robustness against adversarial attacks. However, to our knowledge, no such attacks have been conducted. With our layer, such attacks are easy to implement, and we provide illustrative examples....

## Discussion

We present three novel applications using a differentiable topology layer which can be used to promote topological structure in Euclidean data, images, the weights of machine learning models, and to compare adversarial attacks. This only scratches the surface of the possible directions leveraging the differentiable properties of persistence. Without doubt such work will tackle problems beyond those we have presented here, including encouraging topological structure in intermediate activations of deep neural networks or using the layer in the middle of deep networks to extract persistence features where they may be more useful....

Figure 7: Left: Original image with pixel values in. Data is generated with n/p = 0.5, with i.i.d. Gaussian noise. Center: ordinary least squares solution. Right: least squares solution with topological penalty ℰ (1,0,2;PD0) + ℰ (1,0,2;PD1).

The second kind of filtration that we consider extends a filtration on the edges of a complex, also called a flag filtration. For sublevel set filtrations, this has the form ${f{({(v_{0},\ldots,v_{k})})}} = {{\max_{{i < j \in 0},{\ldots,k}}f}{({(v_{i},v_{j})})}}$ One example of this is based on pairwise distances of points....
