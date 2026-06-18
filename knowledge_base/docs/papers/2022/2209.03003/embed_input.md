Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow

Topics include Image generation, Supervised learning, Online algorithms, Optimization, Learning, Fast, Ordinary differential equation.

We present rectified flow, a surprisingly simple approach to learning (neural) ordinary differential equation (ODE) models to transport between two empirically observed distributions π_0 and π_1, hence providing a unified solution to generative modeling and domain transfer, among various other tasks involving distribution transport. The idea of rectified flow is to learn the ODE to follow the straight paths connecting the points drawn from π_0 and π_1 as much as possible. This is achieved by solving a straightforward nonlinear least squares optimization problem, which can be easily scaled to large models without introducing extra parameters beyond standard supervised learning. The straight paths are special and preferred because they are the shortest paths between two points, and can be simulated exactly without time discretization and hence yield computationally efficient models. We show that the procedure of learning a rectified flow from data, called rectification, turns an arbitrary coupling of π_0 and π_1 to a new deterministic coupling with provably non-increasing convex transport costs....

## Introduction

Compared with supervised learning, the shared difficulty of various forms of unsupervised learning is the lack of *paired* input/output data with which standard regression or classification tasks can be invoked. The gist of most unsupervised methods is to find, in one way or another, meaningful correspondences between points from two distributions. For example, generative models such as generative adversarial networks (GAN) and variational autoencoders (VAE) \e.g., seek to map data points to latent codes following a simple elementary (Gaussian) distribution with which the data can be generated and manipulated....

Several lines of techniques have been developed depending on how to represent and train the map $T$. In traditional generative models, $T$ is parameterized as a neural network, and trained with either GAN-type minimax algorithms or (approximate) maximum likelihood estimation (MLE). However, GANs are known to suffer from numerically instability and mode collapse issues, and require substantial engineering efforts and human tuning, which often do not transfer well across different model architecture and datasets....

As demonstrated in Table 2, the 1-rectified flow shows state-of-the-art performance on both DomainNet and OfficeHome. It is better or on par with the previous best approach (Deep CORAL ), while sustainably improve over all other methods.

Table 2: The accuracy of the transferred testing data using different methods, on the OfficeHome and DomainNet dataset. Higher accuracy means the better performance.

Applying it to each rectification step yields

$\bullet$ The canonical linear interpolation $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ should be recommended as a default choice.

*$\bullet$ Probability Flow ODEs.* The method of PF-ODEs and DDIM provides a different approach to learning ODEs that avoids the main disadvantages of the MLE approach, including the expensive likelihood calculation, training-time simulation of the ODE models, and the need of backpropagation through time. However, because PF-ODEs and DDIM were derived as the side product of learning the mathematically more involved diffusion/SDE models, their theories and algorithm forms were made unnecessarily restrictive and complicated....

Recently, advances have been made by representing the transport plan *implicitly as a continuous time process*, such...
