# Optimization

## Acceleration

Nesterov accelerated gradient descent

Tensor methods

## SGD variants

AdaGrad

RmsProp

## Least Squares

Gauss-Newton

Levenberg-Marquadt

## Quasi-Newton

### BFGS

### SR1

## AV Safety Concepts

https://iot-automotive.news/rss-explained-the-five-rules-for-autonomous-vehicle-safety/
https://www.mobileye.com/technology/true-redundancy/
https://kodiak.ai/safety-report
https://www.nvidia.com/content/dam/en-zz/Solutions/self-driving-cars/safety-force-field/an-introduction-to-the-safety-force-field-v2.pdf
https://ieeexplore.ieee.org/document/9575420
https://ieeexplore.ieee.org/document/9304563
https://ieeexplore.ieee.org/document/9575928

## A* graph search

https://en.wikipedia.org/wiki/A*_search_algorithm

## Stochastic gradient descent

https://neurips.cc/virtual/2021/33647

# RL

## Cartpole

https://underactuated.mit.edu/acrobot.html

## Q-learning

https://en.wikipedia.org/wiki/Q-learning
https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html
https://docs.pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
https://araffin.github.io/post/rl102/

## Gradient descent trajectory optimization

https://www.argmin.net/p/reticulating-splines

# other

## Clothoids

https://seminariomatematico.polito.it/rendiconti/76-2/47.pdf
https://github.com/ebertolazzi/Clothoids

## Central64

https://github.com/Autodesk/Central64

Lots of good ideas:
"path smoothing" is nothing but "path shortcutting" with a deterministic strategy for choosing the sub-segments.

## Motion Prediction Datasets

### **Waymo**

[About – Waymo Open Dataset](https://waymo.com/open/)

### **Motional**

[nuScenes](https://www.nuscenes.org/nuscenes?externalData=all&mapData=all&modalities=Any)

### **Toyota Woven Planet**

[woven.toyota/en/prediction-dataset](https://woven.toyota/en/prediction-dataset)

# Safety, Testing, Verification, Validation

[A Safety-first Approach to Explainable E2E Autonomous Driving | Einride Engineering](https://einride.engineering/blog/a-safety-first-approach-to-explainable-e2e-autonomous-driving)
[Redundancy in autonomous vehicles: Steering, Braking and Power systems | Einride Engineering](https://einride.engineering/blog/redundancy-in-autonomous-vehicles-steering-braking-and-power-systems)
[Quantifying What-Ifs in Simulation | Nuro](https://www.nuro.ai/blog/quantifying-what-ifs-in-simulation)

# MISC packages

https://github.com/iit-DLSLab/Quadruped-PyMPC
https://dspace.mit.edu/bitstream/handle/1721.1/119149/16-412j-spring-2005/contents/projects/1aslam_blas_repo.pdf 
https://isaac.earth/torchid/

# MISC sections

### UN Regulation on uniform provisions concerning the approval of vehicles with regard to Driver Control Assistance Systems

https://unece.org/sites/default/files/2025-03/R171e.pdf

### Quintic bezier path planning

https://link.springer.com/article/10.1007/s40430-021-02826-8

## Prediction horizon

[2402.03893] Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency

Has a nice Table II of suggested lon decel breakpoints for comfort metrics (with sources cited)

Accel            Comfort level
[-0.89, 0]       Comfortable
[-1.89, -0.89]   Uncomfortable
<-1.89           Highly Unomfortable

### Cartpole

https://underactuated.mit.edu/acrobot.html

### **Data-driven MPC (DeePC)**

Florian Dorfler & Friends

[A Tutorial on Data-Enabled Predictive Control (DeePC) - Speaker Deck](https://speakerdeck.com/floriandoerfler/a-tutorial-on-data-enabled-predictive-control-deepc)

### **trajax: Differentiable Trajectory Optimization using JAX**

[GitHub - google/trajax](https://github.com/google/trajax/tree/main)
[Tutorials – 5th L4DC Conference](https://l4dc.seas.upenn.edu/tutorials/)

## Tesla

Tesla AI Day 2021

Clip related to planning & control: https://youtu.be/j0z4FweCy4M?t=4370 

Neural networks serve as learned heuristics for optimal motion planning in action space, guiding search away from local minima. A neural network planner outputs a trajectory distribution that seeds an explicit planner, combining the generalization of learned models with the optimality guarantees of classical planning.

Experiments show the value of strong heuristics for trajectory search: hand-crafted heuristics improve performance over blind search, but learned, AI-based heuristics outperform both.
