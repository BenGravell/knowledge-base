Motion Planning through Policy Search

Topics include Motion planning, Policy search, Mobile robotics, Kinodynamic planning, Value functions, Gradient ascent, Learning in planning.

Uses policy search to refine mobile robot plans directly in a higher-dimensional state/control space rather than stopping at a coarse geometric path. The method seeds a waypoint/controller representation from a value-function plan, then improves it with gradient ascent to obtain smoother and less conservative robot motion.

We propose a motion planning algorithm for performing policy search in the full pose and velocity space of a mobile robot. By comparison, existing techniques optimize high-level plans, but fail to optimize the low-level motion controls. We use policy search in a high dimensional control space to find plans that lead to measurably better motion planning. Our experimental results suggest that our approach leads to superior robot motion than many existing techniques.
