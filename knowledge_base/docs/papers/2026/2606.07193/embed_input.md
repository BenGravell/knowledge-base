<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Shield-Loco: Shielding Locomotion Policies with Predictive Safety Filtering

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning (RL) policies enable dynamic legged locomotion but lack mechanisms to avoid violations of safety constraints that are absent during training. Large-scale offline safe learning is impractical for covering all edge cases. Existing safety frameworks either rely on reduced-order models that cannot reason about whole-body behaviors or require conservative recovery controllers that degrade task performance. We propose a predictive safety filter that post-hoc filters the nominal contact locations fed to the RL policy. When a collision is predicted, a sampling-based optimizer asynchronously searches for safer contact sequences using a full-physics model, while a learned value function bootstraps long-horizon returns. Our three algorithmic components (geometric projection of sampled contacts, momentum-augmented updates, and replica-exchange) make the optimization tractable in a discontinuous contact landscape. We validate the filter on a quadruped robot in dense, cluttered environments, both in simulation and in the real world, showing substantial reductions in safety violations with minimal deviation from the nominal input.
