DTPP: Differentiable Joint Conditional Prediction and Cost Evaluation for Tree Policy Planning in Autonomous Driving

Motion prediction and cost evaluation are vital components in the decision-making system of autonomous vehicles. However, existing methods often ignore the importance of cost learning and treat them as separate modules. In this study, we employ a tree-structured policy planner and propose a differentiable joint training framework for both ego-conditioned prediction and cost models, resulting in a direct improvement of the final planning performance. For conditional prediction, we introduce a query-centric Transformer model that performs efficient ego-conditioned motion prediction. For planning cost, we propose a learnable context-aware cost function with latent interaction features, facilitating differentiable joint learning. We validate our proposed approach using the real-world nuPlan dataset and its associated planning test platform. Our framework not only matches state-of-the-art planning methods but outperforms other learning-based methods in planning quality, while operating more efficiently in terms of runtime. We show that joint training delivers significantly better performance than separate training of the two modules....

## INTRODUCTION

A fundamental requirement for autonomous vehicles is the ability to make decisions that are safe, informed, and human-like. Achieving this involves accurate prediction of the future behavior of traffic participants and planning that ensures safety, comfort, and adherence to traffic norms. Due to inherent uncertainties in the real world, the decision-making system should be capable of *policy planning* that accounts for different futures and options for the ego vehicle to react....

Figure 1: Overview of the proposed decision-making framework. A tree-structured planner generates a multi-stage trajectory tree, which is then used by the conditional prediction model to generate a scenario tree. The optimal plan is selected using the cost evaluation of both trees, and the conditional prediction and cost evaluation models are jointly learnable.

## CONCLUSIONS

We propose DTPP, a differentiable joint learning framework for prediction and cost modeling, specifically designed for a tree policy planner. Our prediction model is a query-centric Transformer network with efficient ego conditioning. The cost model combines learned and handcrafted features with learned context-aware weights. The experimental results for planning and prediction on real-world driving data show that our prediction model yields significantly better performance and efficiency....

Note that one could add additional cost terms, e.g., for lane keeping and route following. We did not find this necessary as our planner is constrained to follow a target lane through its trajectory generator (see Section III-A).

Fig. 3 illustrates the decoder for a single agent. It consists of two cross-attention Transformer modules that gather information from the environment context and the ego plan, respectively. The query input for the cross-attention module is derived from three sources: an agent history embedding directly retrieved from the corresponding position in the environment encoding, a learnable time embedding (to differentiate between time steps), and the ego plan embedding (target points of the ego agent that correspond to distinct branches). Multi-axis attention \[\] is applied to address modal and temporal dimensions in the query....

### IV-B Implementation Details
