<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control

Topics include Model predictive path integral control, Sampling-based model predictive control, Whole-body control, Legged locomotion, Contact-rich manipulation, MuJoCo.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses parallel MuJoCo trajectory rollouts and MPPI to synthesize whole-body locomotion and manipulation online for a physical quadruped. A single simple sampling-based control strategy supports uneven-terrain walking, box climbing, and box pushing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a system for enabling real-time synthesis of whole-body locomotion and manipulation policies for real-world legged robots. Motivated by recent advancements in robot simulation, we leverage the efficient parallelization capabilities of the MuJoCo simulator to achieve fast sampling over the robot state and action trajectories. Our results show surprisingly effective real-world locomotion and manipulation capabilities with a very simple control strategy. We demonstrate our approach on several hardware and simulation experiments: robust locomotion over flat and uneven terrains, climbing over a box whose height is comparable to the robot, and pushing a box to a goal position. To our knowledge, this is the first successful deployment of whole-body sampling-based MPC on real-world legged robot hardware. Experiment videos and code can be found : this https URL
