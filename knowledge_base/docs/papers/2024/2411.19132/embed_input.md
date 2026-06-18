<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conformal Prediction for Distribution-free Optimal Control of Linear Stochastic Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We address an optimal control problem for linear stochastic systems with unknown noise distributions and joint chance constraints using conformal prediction. Our approach involves designing a feedback controller to maintain an error system within a prediction region (PR). We define PRs as sublevel sets of a nonconformity score over error trajectories, enabling the handling of joint chance constraints. We propose two methods to design feedback control and PRs: one through direct optimization over error trajectory samples, and the other indirectly using the S-procedure with a disturbance ellipsoid obtained from data. By tightening constraints with PRs, we solve a relaxed problem to synthesize a feedback policy. Our method ensures reliable probabilistic guarantees based on marginal coverage, independent of data size.
