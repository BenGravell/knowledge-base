Learning to Drive via Asymmetric Self-Play

Large-scale data is crucial for learning realistic and capable driving policies. However, it can be impractical to rely on scaling datasets with real data alone. The majority of driving data is uninteresting, and deliberately collecting new long-tail scenarios is expensive and unsafe. We propose asymmetric self-play to scale beyond real data with additional challenging, solvable, and realistic synthetic scenarios. Our approach pairs a teacher that learns to generate scenarios it can solve but the student cannot, with a student that learns to solve them. When applied to traffic simulation, we learn realistic policies with significantly fewer collisions in both nominal and long-tail scenarios. Our policies further zero-shot transfer to generate training data for end-to-end autonomy, significantly outperforming state-of-the-art adversarial approaches, or using real data alone. For more information, visit.

## Introduction

We are interested in developing policies that drive realistically like a human, reason about complex interactions, and handle safety-critical scenarios. While previous methods have demonstrated improved performance by applying supervised learning with gradually increasing dataset sizes, such an approach has several limitations. Collecting driving datasets at scale is extremely expensive, requiring fleets of vehicles deployed for long stretches of time. Furthermore, a central challenge of self-driving is handling rare edge cases safely, while the majority of nominal driving data is repetitive and contains little learning signal....

One approach is to have policies explore novel states by leveraging closed-loop simulation and methods like reinforcement learning. However, since other actors in simulation typically exhibit nominal behavior, the resulting simulations can still be repetitive and unchallenging. Likewise, leveraging a self-play approach where a policy interacts with itself in multiagent simulation can suffer from the same issue if the policy converges to nominal and cooperative behavior....

## Conclusion and Limitations

We have presented an asymmetric self-play approach for learning to drive, where solvable and realistic scenarios naturally emerge from the interactions of a teacher and student policy. We have shown that the resulting student policy can power more realistic and robust traffic simulation agents across several datasets, and the teacher policy can zero-shot generalize to generating scenarios for unseen end-to-end autonomy policies without needing expensive retraining. While the results are promising, we recognize some existing limitations....

For each actor $i$, our state encoder uses a multi-layer perceptron (MLP) to extract features for its past state $s_{t - H}^{i},\ldots,s_{t}^{i}$ over the past horizon $H \geq 1$,

However, Eq. 9 shows that then $\pi_{S}$ can improve its return (Eq. 6) by simply copying $\pi_{T}$, which contradicts the equilibrium assumption. ∎

Figure 4: Qualitative Comparison. We show TrafficSim (top) and Ours (bottom) on Argoverse2. Our method learns better interaction reasoning to avoid collisions realistically. Colored actors are controlled; gray actors are replayed.

To address these shortcomings, we propose an *asymmetric self-play* mechanism in which challenging, solvable, and...
