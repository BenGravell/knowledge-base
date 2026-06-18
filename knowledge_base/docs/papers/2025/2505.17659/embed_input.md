Plan-R1: Safe and Feasible Trajectory Planning as Language Modeling

Topics include Autonomous driving, Trajectory planning, Language models, Safety, Imitation learning.

Frames safe autonomous-driving trajectory planning as a language-modeling problem with separate stages for behavior learning and principle alignment. The paper is part of the emerging thread that adapts LLM-style training and alignment recipes to structured driving trajectories.

Safe and feasible trajectory planning is critical for real-world autonomous driving systems. However, existing learning-based planners rely heavily on expert demonstrations, which not only lack explicit safety awareness but also risk inheriting undesirable behaviors such as speeding from suboptimal human driving data. Inspired by the success of large language models, we propose Plan-R1, a two-stage trajectory planning framework that decouples principle alignment from behavior learning. In the first stage, a general trajectory predictor is pre-trained on expert data to capture diverse, human-like driving behaviors. In the second stage, the model is fine-tuned with rule-based rewards using Group Relative Policy Optimization (GRPO), explicitly aligning ego planning with principles such as safety, comfort, and traffic rule compliance. This two-stage paradigm retains human-like behaviors while enhancing safety awareness and discarding undesirable patterns from demonstrations.

## Introduction

Trajectory planning is a fundamental component of autonomous driving systems, directly influencing vehicle safety, efficiency, and the ability to navigate complex and dynamic environments. In recent years, learning-based planning approaches have attracted increasing attention due to their strong adaptability, competitive performance, and minimal reliance on manually designed rules. These methods offer promising solutions for generating trajectories that can respond effectively to various traffic scenarios and rapidly changing road conditions.

However, due to the complexity and diversity of real-world driving scenarios, most existing planning methods, whether based on imitation learning (IL) or reinforcement learning (RL), rely heavily on expert demonstrations for supervision. This dependency introduces two key limitations: (i) expert data rarely covers negative scenarios such as collisions or off-road driving, leaving the model unable to explicitly learn how to avoid them, and (ii) demonstrations are not always optimal and may contain undesirable behaviors.

Specifically, we introduce Plan-R1, a two-stage dual-model framework for principle-aligned trajectory planning. In the pre-training stage, trajectories are discretized into motion tokens across time and space, and a general motion predictor is trained with next-motion-token prediction to capture diverse, human-like multi-agent behaviors. In the fine-tuning stage, unlike prior methods that rely on human preference data or additional expert demonstrations, which may introduce biases or undesirable behaviors, we use rule-based rewards that provide consistent and unbiased supervision.

We introduce a new perspective that formulates trajectory planning as a principle-aligned prediction task, decoupling planning principle alignment from behavior learning to overcome the limitations of expert data.

## Conclusion

We presented Plan-R1, a two-stage framework that decouples planning principle alignment from behavior learning for safe and feasible trajectory planning. In the first stage, a motion predictor is pre-trained on expert demonstrations to capture diverse, human-like driving behaviors. In the second stage, the ego policy is fine-tuned with rule-based rewards to explicitly align planning with principles such as safety, comfort, and traffic rule compliance.
