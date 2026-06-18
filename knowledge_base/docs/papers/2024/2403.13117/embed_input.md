Optimal Flow Matching: Learning Straight Trajectories in Just One Step

Topics include Learning, Optimal transport, Matching, FM.

Over the several recent years, there has been a boom in development of Flow Matching (FM) methods for generative modeling. One intriguing property pursued by the community is the ability to learn flows with straight trajectories which realize the Optimal Transport (OT) displacements. Straightness is crucial for the fast integration (inference) of the learned flow's paths. Unfortunately, most existing flow straightening methods are based on non-trivial iterative FM procedures which accumulate the error during training or exploit heuristics based on minibatch OT. To address these issues, we develop and theoretically justify the novel \textbf{Optimal Flow Matching} (OFM) approach which allows recovering the straight OT displacement for the quadratic transport in just one FM step. The main idea of our approach is the employment of vector field for FM which are parameterized by convex functions.

## Introduction

Recent success in generative modeling Liu et al.; Esser et al.; Cao et al. is mostly driven by Flow Matching (FM) Lipman et al. models. These models move a known distribution to a target one via ordinary differential equations (ODE) describing the mass movement. However, such processes usually have curved trajectories, resulting in time-consuming ODE integration for sampling. To overcome this issue, researches developed several improvements of the FM Liu; Liu et al.; Pooladian et al., which aim to recover more straight paths.

Rectified Flow (RF) method Liu; Liu et al. iteratively solves FM and gradually rectifies trajectories. Unfortunately, in each FM iteration, it accumulates the error, see and. This may spoil the performance of the method. The other popular branch of approaches to straighten trajectories is based on the connection between straight paths and Optimal Transport (OT) Villani. The main goal of OT is to find the way to move one probability distribution to another with the minimal effort. Such OT maps are usually described by ODEs with straight trajectories.

Contributions. In this paper, we fix the above-mentioned problems of the straightening methods. We propose a novel Optimal Flow Matching (OFM) approach ) that after a single FM iteration obtains straight trajectories which can be simulated without ODE solving. It recovers OT flow for the quadratic transport cost function, i.e., it solves the Benamou--Brenier problem. We demonstrate the potential of OFM in the series of experiments and benchmarks.

The main idea of our OFM is to consider during FM only specific vector fields which yield straight paths by design. These vector fields are the gradients of convex functions, which in practice are parametrized by Input Convex Neural Networks Amos et al.. In OFM, one can optionally use minibatch OT or any other transport plan as the input, and this is completely theoretically justified.

## Discussion

Potential impact. We believe that our novel theoretical results have a huge potential for improving modern flow matching-based methods and inspiring the community for further studies. We think this is of high importance especially taking into account that modern generative models start to extensively use flow matching methods Yan et al.; Liu et al.; Esser et al..

Limitations and broader impact are discussed in Appendix C.
