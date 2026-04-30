# Waymo AI

This is my personal write-up of [Waymo's 2025 Blog post on "Demonstrably Safe AI For Autonomous Driving"](https://waymo.com/blog/2025/12/demonstrably-safe-ai-for-autonomous-driving/)

## Summary

Waymo frames autonomous driving as a giant reinforcement learning problem and uses **learned models** for each part of the problem:

1. Control Policy / Agent = "Driver"
2. Environment = "Simulator"
3. Reward = "Critic"

Importantly, each of these component models uses a **common large foundation model backbone**. The models that actually run onboard (Driver) and at-scale (Simulator and Critic) are **distilled** from the original large "Teacher" models to small, performant "Student" models.

They mention that the onboard Driver model goes through a separate **safety validator** which is presumably **not learned**.

> Importantly, the Waymo Driver employs a separate and rigorous onboard validation layer, which then verifies the trajectories produced by the Driver’s generative ML model.
