<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Autonomous Automobile Trajectory Tracking for Off-road Driving: Controller Design, Experimental Validation and Racing

Topics include Autonomous driving, Trajectory tracking, Off-road driving, Vehicle control, Racing, Experimental validation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents and validates the trajectory-tracking controller used by Stanford's autonomous vehicle program for aggressive off-road driving. The paper is valuable because it combines controller design, stability intuition, and real high-speed racing experiments rather than only simulation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a nonlinear control law for an automobile to autonomously track a trajectory, provided in real-time, on rapidly varying, off-road terrain. Existing methods can suffer from a lack of global stability, a lack of tracking accuracy, or a dependence on smooth road surfaces, any one of which could lead to the loss of the vehicle in autonomous off-road driving. This work treats automobile trajectory tracking in a new manner, by considering the orientation of the front wheels - not the vehicle's body - with respect to the desired trajectory, enabling collocated control of the system. A steering control law is designed using the kinematic equations of motion, for which global asymptotic stability is proven. This control law is then augmented to handle the dynamics of pneumatic tires and of the servo-actuated steering wheel. To control vehicle speed, the brake and throttle are actuated by a switching proportional integral (PI) controller. The complete control system consumes a negligible fraction of a computer's resources. It was implemented on a Volkswagen Touareg, "Stanley", the Stanford Racing Team's entry in the DARPA Grand Challenge 2005, a 132 mi autonomous off-road race.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experimental results from Stanley demonstrate the ability of the controller to track trajectories between obstacles, over steep and wavy terrain, through deep mud puddles, and along cliff edges, with a typical root mean square (RMS) crosstrack error of under 0.1 m. In the DARPA National Qualification Event 2005, Stanley was the only vehicle out of 40 competitors to not hit an obstacle or miss a gate, and in the DARPA Grand Challenge 2005 Stanley had the fastest course completion time.
