<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Data to Safe Mobile Robot Navigation: An Efficient and Modular Robust MPC Design Pipeline

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model predictive control (MPC) is a powerful strategy for planning and control in autonomous mobile robot navigation. However, ensuring safety in real-world deployments remains challenging due to the presence of disturbances and measurement noise. Existing approaches often rely on idealized assumptions, neglect the impact of noisy measurements, and simply heuristically guess unrealistic bounds. In this work, we present an efficient and modular robust MPC design pipeline that systematically addresses these limitations. The pipeline consists of an iterative procedure that leverages closed-loop experimental data to estimate disturbance bounds and synthesize a robust output-feedback MPC scheme. We provide the pipeline in the form of deterministic and reproducible code to synthesize the robust output-feedback MPC from data. We empirically demonstrate robust constraint satisfaction and recursive feasibility in quadrotor simulations using Gazebo.
