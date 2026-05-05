## RL
    - Approximate Dynamic Programming (ADP) & Q-learning:
      - Value Iteration (VI):
        - TODO
      - Policy Iteration (PI):
        - TODO
      - Soft Actor-Critic (SAC):
        - TODO

## Optimization

## Acceleration

Nesterov accelerated gradient descent

Tensor methods

Cubic regularized Newton (Nesterov 2006)

## SGD variants

AdaGrad

RmsProp

ADAM: https://arxiv.org/abs/1412.6980


## Least Squares

Gauss-Newton

Levenberg-Marquadt



## Regularized Newton

https://arxiv.org/abs/2112.02089

https://arxiv.org/abs/2208.05888


## Quasi-Newton

### DFP

Title: Variable Metric Method for Minimization
Author: William C. Davidon
Original report: AEC Research and Development Report ANL-5990, Argonne National Laboratory, May 1959 (revised November 1959)
Published version: SIAM Journal on Optimization, Vol. 1, No. 1, pp. 1–17, February 1991
DOI: 10.1137/0801001
PDF (McGill): https://www.math.mcgill.ca/dstephens/680/Papers/Davidon91.pdf
 
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


## ERA

"Identification of Observer/Kalman Filter Markov Parameters: Theory and Experiments"
Juang, Phan, Horta & Longman — Journal of Guidance, Control, and Dynamics, 1993

This is Juang's own follow-on to his 1985 ERA paper. OKID generalizes ERA from pure impulse response data to data driven by arbitrary input signals, by identifying a special set of parameters called Observer Markov Parameters that subsume both the state-space model and an associated Kalman filter gain. (Dartmouth) This is critical: ERA only works on impulse responses (clean, structured experiments), while OKID/ERA works on any input-output time series — which is exactly the setting DMD and SINDy later target.

## MPTree

https://www.sciencedirect.com/science/article/pii/S2405896324004166

Quote
"If a MP violates a collision avoidance or vehicle dynamic constraint (e.g. infeasible longitudinal or lateral acceleration) then the maneuver is discarded (or penalized if it is close to an infeasible region)."

This is notable because, in the context of the success of the whole framework/algorithm, it suggests that rejection of trajectories does not destroy sample efficiency, at least in this autonomous driving setting.



## Optimization and learning for rough terrain legged locomotion

https://journals.sagepub.com/doi/10.1177/0278364910392608

https://www.researchgate.net/publication/220122195_Optimization_and_learning_for_rough_terrain_legged_locomotion


## Crocoddyl

https://arxiv.org/abs/1909.04947

https://github.com/loco-3d/crocoddyl

https://gepettoweb.laas.fr/doc/loco-3d/crocoddyl/devel/doxygen-html/


## GuSTO

https://arxiv.org/abs/1903.00155

https://ieeexplore.ieee.org/document/8794205

https://github.com/StanfordASL/GuSTO.jl




## Expansive space tree (EST)


https://ieeexplore.ieee.org/document/619371


https://www.researchgate.net/publication/4077277_Guided_Expansive_Spaces_Trees_a_search_strategy_for_motion-_and_cost-constrained_state_spaces


https://journals.sagepub.com/doi/10.1177/027836402320556421

## A* graph search

https://en.wikipedia.org/wiki/A*_search_algorithm

https://www.researchgate.net/publication/228785110_Near_optimal_hierarchical_path-finding_HPA

https://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/jogd.pdf


## Primal-dual ilqr

https://ieeexplore.ieee.org/abstract/document/11248841

https://arxiv.org/abs/2506.07823

https://github.com/iit-DLSLab/mpx



## Stochastic gradient descent

https://arxiv.org/abs/2507.02131
https://neurips.cc/virtual/2021/33647
https://arxiv.org/abs/1802.06175
https://arxiv.org/abs/1602.04915
https://proceedings.mlr.press/v49/lee16.pdf
https://proceedings.mlr.press/v70/jin17a.html


# RL

## Cartpole

https://coneural.org/florian/papers/05_cart_pole.pdf

https://underactuated.mit.edu/acrobot.html



## Q-learning

https://en.wikipedia.org/wiki/Q-learning
https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html
https://docs.pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
https://araffin.github.io/post/rl102/



## A Natural Policy Gradient

https://proceedings.neurips.cc/paper_files/paper/2001/hash/4b86abe48d358ecf194c56c69108433e-Abstract.html


## Gradient descent trajectory optimization

https://asmedigitalcollection.asme.org/appliedmechanics/article-abstract/29/2/247/386190/A-Steepest-Ascent-Method-for-Solving-Optimum?redirectedFrom=fulltext

https://www.argmin.net/p/reticulating-splines

# other

## Intelligent Driver Model (IDM)

https://en.wikipedia.org/wiki/Intelligent_driver_model

https://journals.aps.org/pre/abstract/10.1103/PhysRevE.62.1805


https://arxiv.org/abs/cond-mat/0002177

Treiber, Martin; Hennecke, Ansgar; Helbing, Dirk (2000-08-01). "Congested traffic states in empirical observations and microscopic simulations". Physical Review E. 62 (2): 1805–1824. arXiv:cond-mat/0002177. Bibcode:2000PhRvE..62.1805T


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

https://www.researchgate.net/publication/277358943_Constrained_Global_Path_Optimization_for_Articulated_Steering_Vehicles

https://www.researchgate.net/publication/379463578_Quintic_Bezier_curve_and_numerical_optimal_solution_based_path_planning_approach_in_seismic_exploration 

https://link.springer.com/article/10.1007/s40430-021-02826-8


### Model predictive contouring control

[2604.24064] Trajectory Planning for an Articulated Commercial Vehicle using Model Predictive Contouring Control


[1711.07300] Optimization-Based Autonomous Racing of 1:43 Scale RC Cars

this is the paper that popularized the approach for vehicle control.
this is the paper that made the transfer from XY stage positioner control (cited original paper from 2009-2010) to vehicle control.





## prediction horizon

[2402.03893] Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency

Has a nice Table II of suggested lon decel breakpoints for comfort metrics (with sources cited)

Accel            Comfort level
[-0.89, 0]       Comfortable
[-1.89, -0.89]   Uncomfortable
<-1.89           Highly Unomfortable



### Cartpole

https://ieeexplore.ieee.org/document/6313077
http://incompleteideas.net/papers/barto-sutton-anderson-83.pdf
https://dl.acm.org/doi/10.5555/104134.104143


https://underactuated.mit.edu/acrobot.html

https://coneural.org/florian/papers/05_cart_pole.pdf



### **Data-driven MPC (DeePC)**

Florian Dorfler & Friends

[A Tutorial on Data-Enabled Predictive Control (DeePC) - Speaker Deck](https://speakerdeck.com/floriandoerfler/a-tutorial-on-data-enabled-predictive-control-deepc)




### **trajax: Differentiable Trajectory Optimization using JAX**

[GitHub - google/trajax](https://github.com/google/trajax/tree/main)

[Tutorials – 5th L4DC Conference](https://l4dc.seas.upenn.edu/tutorials/)


## tesla

Tesla AI Day 2021

Clip related to planning & control: https://youtu.be/j0z4FweCy4M?t=4370 

Neural networks serve as learned heuristics for optimal motion planning in action space, guiding search away from local minima. A neural network planner outputs a trajectory distribution that seeds an explicit planner, combining the generalization of learned models with the optimality guarantees of classical planning.

Experiments show the value of strong heuristics for trajectory search: hand-crafted heuristics improve performance over blind search, but learned, AI-based heuristics outperform both.

## GitHub

https://github.com/open-planning/roboplan

https://github.com/Genesis-Embodied-AI/Genesis 

https://github.com/TUMFTM/PointCloudCrafter

https://github.com/MarcToussaint/KOMO 

## Cool stuff

https://usgs-lidar.gishub.org/

https://geodatakatalogen.naturvardsverket.se/geonetwork/srv/swe/catalog.search#/metadata/8853721d-a466-4c01-afcc-9eae57b17b39

https://rreusser.github.io/

https://en.wikipedia.org/wiki/The_Checklist_Manifesto

https://www.vg.no/nyheter/i/3pkoP9/busser-fast-paa-alexander-kiellands-plass-i-oslo

https://depth-anything-3.github.io/

https://ompl.kavrakilab.org/gallery.html 

https://deepwiki.com/acados/acados/2.1-ocp-nlp-solvers#differential-dynamic-programming-ddp

https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles

## Blogs

https://m0nads.wordpress.com/2021/05/09/are-deep-networks-just-kernel-machines/ 

https://rai-inst.com/resources/blog/dull-dirty-dangerous-redefining-undesirable-work-for-robotics/

https://www.nuro.ai/blog/nuros-universal-autonomy-model

https://developer.nvidia.com/blog/integrate-physical-ai-capabilities-into-existing-apps-with-nvidia-omniverse-libraries/

https://www.openautonomy.com/article/modular-vs-end-to-end-autonomy-architecture-mining

https://badas.nexar.app/
