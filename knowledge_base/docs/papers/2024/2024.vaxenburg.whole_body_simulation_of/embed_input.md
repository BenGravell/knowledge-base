<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Whole-Body Simulation of Realistic Fruit Fly Locomotion with Deep Reinforcement Learning

Topics include Biomechanics, Physics simulation, Reinforcement learning, Locomotion, Motor control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Builds an anatomically detailed fly model in MuJoCo and trains controllers for walking, flight, and visually guided behavior using deep reinforcement learning and added fluid and adhesion forces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The body of an animal influences how its nervous system generates behaviour. Accurately modelling the neural control of sensorimotor behaviour requires an anatomically detailed biomechanical representation of the body. Here we introduce a whole-body model of the fruit fly Drosophila melanogaster in a physics simulator. Designed as a general-purpose framework, our model enables the simulation of diverse fly behaviours, including both terrestrial and aerial locomotion. We validate its versatility by replicating realistic walking and flight behaviours. To support these behaviours, we develop phenomenological models for fluid and adhesion forces. Using data-driven, end-to-end reinforcement learning, we train neural network controllers capable of generating naturalistic locomotion along complex trajectories in response to high-level steering commands. Furthermore, we show the use of visual sensors and hierarchical motor control, training a high-level controller to reuse a pretrained low-level flight controller to perform visually guided flight tasks. Our model serves as an open-source platform for studying the neural control of sensorimotor behaviour in an embodied context.
