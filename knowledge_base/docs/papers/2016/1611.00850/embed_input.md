Optical Flow Estimation Using a Spatial Pyramid Network

Topics include Optical flow, SPyNet, Spatial pyramid, Convolutional networks, Coarse-to-fine estimation, Image warping, Embedded vision.

SPyNet is a compact hybrid of classical coarse-to-fine warping and learned flow-update networks. Its importance is that it demonstrates a smaller, more interpretable neural optical-flow model by pushing large displacement handling back into a spatial pyramid rather than asking a single large CNN to solve everything at once.

We learn to compute optical flow by combining a classical spatial-pyramid formulation with deep learning. This estimates large motions in a coarse-to-fine approach by warping one image of a pair at each pyramid level by the current flow estimate and computing an update to the flow. Instead of the standard minimization of an objective function at each pyramid level, we train one deep network per level to compute the flow update. Unlike the recent FlowNet approach, the networks do not need to deal with large motions; these are dealt with by the pyramid. This has several advantages. First, our Spatial Pyramid Network (SPyNet) is much simpler and 96% smaller than FlowNet in terms of model parameters. This makes it more efficient and appropriate for embedded applications. Second, since the flow at each pyramid level is small (< 1 pixel), a convolutional approach applied to pairs of warped images is appropriate. Third, unlike FlowNet, the learned convolution filters appear similar to classical spatio-temporal filters, giving insight into the method and how to improve it.

## Introduction

Recent years have seen significant progress on the problem of accurately estimating optical flow, as evidenced by improving performance on increasingly challenging benchmarks. Despite this, most flow methods are derived from a "classical formulation" that makes a variety of assumptions about the image, from brightness constancy to spatial smoothness. These assumptions are only coarse approximations to reality and this likely limits performance. The recent history of the field has focused on improving these assumptions or making them more robust to violations. This has led to steady but incremental progress.

Goal. We argue that there is an alternative approach that combines the best of both approaches. Decades of research on flow has produced well engineered systems and principles that are effective. But there are places where these methods make assumptions that limit their performance.

We do not claim to solve the full optical flow problem with SPyNet -- we address the same problem as traditional approaches and inherit some of their limitations. For example, it is well known that large motions of small or thin objects are difficult to capture with a pyramid representation. We see the large motion problem as separate, requiring different solutions. Rather, what we show is that the traditional problem can be reformulated, portions of it can be learned, and performance improves in many scenarios.

Additionally, because our approach connects past methods with new tools, it provides insights into how to move forward. In particular, we find that SPyNet learns spatio-temporal convolutional filters that resemble traditional spatio-temporal derivative or Gabor filters. The learned filters resemble biological models of motion processing filters in MT and V1. This is in contrast to the highly random-looking filters learned by FlowNet. This suggests that it is timely to reexamine older spatio-temporal filtering approaches with new tools.

## Discussion and Future Work

Traditional flow methods linearize the brightness constancy equation resulting in an optical flow constraint equation implemented with spatial and temporal derivative filters. Sometimes methods adopt a more generic filter constancy assumption. Our filters are somewhat different. The filters learned by SPyNet are used in the direct computation of the flow by the feed-forward network.
