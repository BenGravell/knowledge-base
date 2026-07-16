<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Human-like Autonomy Emerges from Self-play and a Pinch of Human Data

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Self-play reinforcement learning has recently emerged as a way to train driving policies without any human data. It uses cheap, large-scale simulations to substitute expensive, large-scale human driving demonstrations. A key limitation of this approach is that policies trained through pure self-play can learn effective but alien driving conventions incompatible with people. Previous works attempt to mitigate such behavioral misalignments through extensive reward engineering and domain randomization, which are brittle and labor-intensive. Instead of completely discarding human demonstrations, our method treats them as a regularization objective on top of a minimal safe goal-reaching reward. Like the spice in a good stew, we find that a little human data goes a long way: our method uses only 30 minutes of human demonstrations, 2500x fewer than comparable imitation learning approaches. Resulting policies coordinate with held-out human trajectories and complete training in 15 hours on a single consumer-grade GPU. Videos and full source code are available at
