<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distance Metric Learning for RRT-Based Motion Planning with Constant-Time Inference

Topics include Motion planning, Trajectory planning, Kinodynamic planning, Sampling-based planning, Rapidly-exploring random tree, Distance metric learning, Machine learning, Inference.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Trains a supervised model to approximate the kinodynamic steering distance for RRT-based planners. The motivation is purely for increasing performance in terms of reducing average and worst-case runtime latency; assumes we have a slow-to-compute ground truth perfect steering function used to generate training data. The features are a set of 14 hand-crafted and cheap-to-evaluate metrics, and the labels are a scalar ground truth cost. The learned model is a basis function model (BFM) using quadratic basis functions and trained using Levenberg-Marquadt. The model architecture was selected as the best (in terms of prediction quality and inference runtime latency) out of a ranking comparison against other architectures trained on the same data, including a small neural network, random forest, support vector machine with radial basis function kernel, and locally weighted projection.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The distance metric is a key component in RRT-based motion planning that deeply affects coverage of the state space, path quality and planning time. With the goal to speed up planning time, we introduce a learning approach to approximate the distance metric for RRT-based planners. By exploiting a novel steer function which solves the two-point boundary value problem for wheeled mobile robots, we train a simple nonlinear parametric model with constant-time inference that is shown to predict distances accurately in terms of regression and ranking performance. In an extensive analysis we compare our approach to an Euclidean distance baseline, consider four alternative regression models and study the impact of domain-specific feature expansion. The learning approach is shown to be faster in planning time by several factors at negligible loss of path quality.
