<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interaction-Aware Sampling-Based MPC with Learned Local Goal Predictions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning for autonomous robots in tight, interaction-rich, and mixed human-robot environments is challenging. State-of-the-art methods typically separate prediction and planning, predicting other agents' trajectories first and then planning the ego agent's motion in the remaining free space. However, agents' lack of awareness of their influence on others can lead to the freezing robot problem. We build upon Interaction-Aware Model Predictive Path Integral (IA-MPPI) control and combine it with learning-based trajectory predictions, thereby relaxing its reliance on communicated short-term goals for other agents. We apply this framework to Autonomous Surface Vessels (ASVs) navigating urban canals. By generating an artificial dataset in real sections of Amsterdam's canals, adapting and training a prediction model for our domain, and proposing heuristics to extract local goals, we enable effective cooperation in planning. Our approach improves autonomous robot navigation in complex, crowded environments, with potential implications for multi-agent systems and human-robot interaction.
