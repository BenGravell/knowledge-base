DTPP: Differentiable Joint Conditional Prediction and Cost Evaluation for Tree Policy Planning in Autonomous Driving

Motion prediction and cost evaluation are vital components in the decision-making system of autonomous vehicles. However, existing methods often ignore the importance of cost learning and treat them as separate modules. In this study, we employ a tree-structured policy planner and propose a differentiable joint training framework for both ego-conditioned prediction and cost models, resulting in a direct improvement of the final planning performance. For conditional prediction, we introduce a query-centric Transformer model that performs efficient ego-conditioned motion prediction. For planning cost, we propose a learnable context-aware cost function with latent interaction features, facilitating differentiable joint learning. We validate our proposed approach using the real-world nuPlan dataset and its associated planning test platform. Our framework not only matches state-of-the-art planning methods but outperforms other learning-based methods in planning quality, while operating more efficiently in terms of runtime. We show that joint training delivers significantly better performance than separate training of the two modules.

## INTRODUCTION

A fundamental requirement for autonomous vehicles is the ability to make decisions that are safe, informed, and human-like. Achieving this involves accurate prediction of the future behavior of traffic participants and planning that ensures safety, comfort, and adherence to traffic norms. Due to inherent uncertainties in the real world, the decision-making system should be capable of *policy planning* that accounts for different futures and options for the ego vehicle to react.

However, tree-structured planners face two significant challenges. First, in contrast to most neural motion prediction models that only predict unconditional future trajectories of other agents (i.e., without considering bi-directional interactions), tree-structured planners require a prediction model capable of efficiently producing ego-conditioned predictions. The prediction model must be able to handle varying search depths (timesteps) within the planning process, maintain causal relationships, and efficiently process multiple branches.

Our key contributions are threefold. First, we present the DTPP framework that integrates efficient ego-conditioned predictions with the learning of a situation-aware cost function (Fig. 1). Our framework can flexibly leverage both learned and handcrafted cost components, is end-to-end differentiable, and enables joint training with human driving data. Second, we present a novel query-centric, Transformer-based prediction model that enables efficient multi-stage motion predictions conditioned on multiple potential future ego trajectories.

## Methodology

1:Nl expansion stages, fp prediction model, fc cost model, fe node expansion function, s0 initial node.
2:Encode scene context using fp (encoder)
4: Expand the current node(s) si using function fe to obtain the trajectory tree si + 1
5: Query the prediction model fp (decoder) with the trajectory tree to obtain the scenario tree pi + 1
6: Query the cost model fc with the trajectory tree and scenario tree to obtain branch costs ci + 1
7: Prune nodes in si + 1 using ci + 1
9:Compute the optimal first-stage node s1* using dynamic programming
Algorithm 1 Tree Policy Planning with Learned Prediction and Cost Models
