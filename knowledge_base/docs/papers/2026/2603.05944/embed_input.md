<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How to Model Your Crazyflie Brushless

Topics include Reinforcement learning, Neural networks, Accuracy, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Crazyflie quadcopter is widely recognized as a leading platform for nano-quadcopter research. In early 2025, the Crazyflie Brushless was introduced, featuring brushless motors that provide around 50% more thrust compared to the brushed motors of its predecessor, the Crazyflie 2.1. This advancement has opened new opportunities for research in agile nano-quadcopter control. To support researchers utilizing this new platform, this work presents a dynamics model of the Crazyflie Brushless and identifies its key parameters. Through simulations and hardware analyses, we assess the accuracy of our model. We furthermore demonstrate its suitability for reinforcement learning applications by training an end-to-end neural network position controller and learning a backflip controller capable of executing two complete rotations with a vertical movement of just 1.8 meters. This showcases the model's ability to facilitate the learning of controllers and acrobatic maneuvers that successfully transfer from simulation to hardware. Utilizing this application, we investigate the impact of domain randomization on control performance, offering valuable insights into bridging the sim-to-real gap with the presented model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We have open-sourced the entire project, enabling users of the Crazyflie Brushless to swiftly implement and test their own controllers on an accurate simulation platform.
