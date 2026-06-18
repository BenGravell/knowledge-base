RAFT: Recurrent All-Pairs Field Transforms for Optical Flow

Topics include Optical flow, RAFT, Recurrent refinement, All-pairs correlation, 4D correlation volume, Dense matching, Cross-dataset generalization.

RAFT reframes optical flow around a dense all-pairs correlation volume and a recurrent update operator that repeatedly refines a single high-quality field. Its accuracy, generalization, and compact recurrent design made it a dominant baseline for modern learned optical flow.

We introduce Recurrent All-Pairs Field Transforms (RAFT), a new deep network architecture for optical flow. RAFT extracts per-pixel features, builds multi-scale 4D correlation volumes for all pairs of pixels, and iteratively updates a flow field through a recurrent unit that performs lookups on the correlation volumes. RAFT achieves state-of-the-art performance. On KITTI, RAFT achieves an F1-all error of 5.10%, a 16% error reduction from the best published result (6.10%). On Sintel (final pass), RAFT obtains an end-point-error of 2.855 pixels, a 30% error reduction from the best published result (4.098 pixels). In addition, RAFT has strong cross-dataset generalization as well as high efficiency in inference time, training speed, and parameter count. Code is available at

## Introduction

Optical flow is the task of estimating per-pixel motion between video frames. It is a long-standing vision problem that remains unsolved. The best systems are limited by difficulties including fast-moving objects, occlusions, motion blur, and textureless surfaces.

Optical flow has traditionally been approached as a hand-crafted optimization problem over the space of dense displacement fields between a pair of images. Generally, the optimization objective defines a trade-off between a *data* term which encourages the alignment of visually similar image regions and a *regularization* term which imposes priors on the plausibility of motion. Such an approach has achieved considerable success, but further progress has appeared challenging, due to the difficulties in hand-designing an optimization objective that is robust to a variety of corner cases.

## Conclusions

We have proposed RAFT---Recurrent All-Pairs Field Transforms---a new end-to-end trainable model for optical flow. RAFT is unique in that it operates at a single resolution using a large number of lightweight, recurrent update operators. Our method achieves state-of-the-art accuracy across a diverse range of datasets, strong cross dataset generalization, and is efficient in terms of inference time, parameter count, and training iterations.

Initialization: By default, we initialize the flow field to 0 everywhere, but our iterative approach gives us the flexibility to experiment with alternatives. When applied to video, we test *warm-start* initialization, where optical flow from the previous pair of frames is forward projected to the next pair of frames with occlusion gaps filled in using nearest neighbor interpolation.

We additionally use a context network. The context network extracts features only from the first input image $I_{1}$. The architecture of the context network, $h_{\theta}$ is identical to the feature extraction network. Together, the feature network $g_{\theta}$ and the context network $h_{\theta}$ form the first stage of our approach, which only need to be performed once.

We train our model using the FlyingChairs$\rightarrow$FlyingThings schedule and then evaluate on the Sintel dataset using the *train* split for validation. Results are shown in Table 1 and Figure 3, and we split results based on the data used for training....
