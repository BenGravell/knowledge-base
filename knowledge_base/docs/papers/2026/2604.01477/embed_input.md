<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Soft MPCritic: Amortized Model Predictive Value Iteration

Topics include Reinforcement learning, Value iteration, Model predictive control, Predictive control, Robustness, Accuracy, Online algorithms, Planning, Control, Learning, Soft MPCritic, Amortized, Model predictive path integral control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning (RL) and model predictive control (MPC) offer complementary strengths, yet combining them at scale remains computationally challenging. We propose soft MPCritic, an RL-MPC framework that learns in (soft) value space while using sample-based planning for both online control and value target generation. soft MPCritic instantiates MPC through model predictive path integral control (MPPI) and trains a terminal Q-function with fitted value iteration, aligning the learned value function with the planner and implicitly extending the effective planning horizon. We introduce an amortized warm-start strategy that recycles planned open-loop action sequences from online observations when computing batched MPPI-based value targets. This makes soft MPCritic computationally practical, while preserving solution quality. soft MPCritic plans in a scenario-based fashion with an ensemble of dynamic models trained for next-step prediction accuracy. Together, these ingredients enable soft MPCritic to learn effectively through robust, short-horizon planning on classic and complex control tasks. These results establish soft MPCritic as a practical and scalable blueprint for synthesizing MPC policies in settings where policy extraction and direct, long-horizon planning may fail.
