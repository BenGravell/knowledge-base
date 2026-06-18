<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Let's Make a Splan: Risk-Aware Trajectory Optimization in a Normalized Gaussian Splat

Topics include Trajectory optimization, Gaussian splatting, 3D Gaussian splatting, Risk-aware planning, 3D scene, Representation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes trajectory optimization directly within a Normalized Gaussian Splat (NGS) scene representation, treating Gaussian density as a risk measure to enable risk-aware collision avoidance without requiring explicit geometric extraction.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Neural Radiance Fields and Gaussian Splatting have recently transformed computer vision by enabling photo-realistic representations of complex scenes. However, they have seen limited application in real-world robotics tasks such as trajectory optimization. This is due to the difficulty in reasoning about collisions in radiance models and the computational complexity associated with operating in dense models. This paper addresses these challenges by proposing SPLANNING, a risk-aware trajectory optimizer operating in a Gaussian Splatting model. This paper first derives a method to rigorously upper-bound the probability of collision between a robot and a radiance field. Then, this paper introduces a normalized reformulation of Gaussian Splatting that enables efficient computation of this collision bound. Finally, this paper presents a method to optimize trajectories that avoid collisions in a Gaussian Splat. Experiments show that SPLANNING outperforms state-of-the-art methods in generating collision-free trajectories in cluttered environments. The proposed system is also tested on a real-world robot manipulator. A project page is available at
