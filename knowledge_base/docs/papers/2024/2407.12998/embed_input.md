Surgical Robot Transformer (SRT): Imitation Learning for Surgical Tasks

Topics include Imitation learning, Robotics, Transformers, Learning, Surgical robot transformer, SRT, Surgical robot.

We explore whether surgical manipulation tasks can be learned on the da Vinci robot via imitation learning. However, the da Vinci system presents unique challenges which hinder straight-forward implementation of imitation learning. Notably, its forward kinematics is inconsistent due to imprecise joint measurements, and naively training a policy using such approximate kinematics data often leads to task failure. To overcome this limitation, we introduce a relative action formulation which enables successful policy training and deployment using its approximate kinematics data. A promising outcome of this approach is that the large repository of clinical data, which contains approximate kinematics, may be directly utilized for robot learning without further corrections. We demonstrate our findings through successful execution of three fundamental surgical tasks, including tissue manipulation, needle handling, and knot-tying.

## Introduction

Recently, large-scale imitation learning has shown great promise in creating generalist systems for manipulation tasks \[\]. Prior research in this area has mostly focused on learning day-to-day household activities. However, an under-explored area with high potential is the surgical domain, particularly with the use of Intuitive Surgical's da Vinci robot. These robots are deployed globally and possess immense scaling potential: as of 2021, over 10 million surgeries have been performed using 6,500 da Vinci systems in 67 countries, with 55,000 surgeons trained on the system \[\]....

However, robot learning on the da Vinci presents unique challenges. The hardware suffers from inaccurate forward kinematics due to potentiometer-based joint measurements, hysteresis, and overall flexibility and slack in its mechanism \[\]. These limitations result in the robot's failure to perform simple visual-servoing tasks \[\]. As we discover in this work, naively training a policy using such approximate kinematics data almost always leads to task failure....

In this work, we opt for using off-the-shelf large wrist cameras which are not clinically relevant. However, the cameras may be replaced with much smaller ones (1-2mm diameter) and its mount can be further optimized by integrating quick-release mechanisms for swift transfer between surgical tools. Also, our model is limited as it can only act based on current observations and does not have the ability to modulate different behavior based on human instruction. We hope to address these issues in future work to further advance the autonomy of surgical robots.

In summary, we demonstrated an approach for imitation learning on the dVRK using its approximate kinematics data, without providing further post-processing corrections. The key idea of our approach was to rely on the more consistent relative motion of the robot, achieved by modeling policy actions as relative motion such as tool-centric and hybrid-relative actions. As mentioned in the introduction, we believe that our work is a step towards leveraging the large repository of approximate surgical data for robot learning at scale, without providing further kinematics corrections....

Where the subtraction operation $\ominus$ defined as:

## Technical Approach
