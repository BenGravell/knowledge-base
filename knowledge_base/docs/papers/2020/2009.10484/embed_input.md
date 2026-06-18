Asymptotically Optimal Sampling-Based Motion Planning Methods

Topics include Survey, Robotics, Motion planning, Robot motion planning, Sampling-based planning, Optimal motion planning, Asymptotically optimal.

Motion planning is a fundamental problem in autonomous robotics that requires finding a path to a specified goal that avoids obstacles and takes into account a robot's limitations and constraints. It is often desirable for this path to also optimize a cost function, such as path length. Formal path-quality guarantees for continuously valued search spaces are an active area of research interest. Recent results have proven that some sampling-based planning methods probabilistically converge toward the optimal solution as computational effort approaches infinity. This article summarizes the assumptions behind these popular asymptotically optimal techniques and provides an introduction to the significant ongoing research on this topic.

## INTRODUCTION

Planning is an important task in a number of fields, including computer science and robotics. It consists of finding a sequence of valid states (i.e., a path) between specified positions (i.e., a start and goal) in a search space. Many problems have multiple *feasible* solutions and applications often seek the feasible path that optimizes a cost function (i.e., the *optimal* solution). A feasible solution in robot motion planning is a path that avoids hazards in the environment (i.e., obstacles) and can be followed by the robot (e.g., is kinodynamically feasible).

These results have motivated significant recent work on quality guarantees for sampling-based planning algorithms. These include refining the conditions necessary for popular approaches to converge asymptotically to the optimum and designing novel algorithms that find better initial solutions and/or converge faster. This survey summarizes results and algorithms from the field to present an introduction to this exciting work.

## CONCLUSION

Sampling-based motion planning algorithms are powerful tools for searching continuously valued spaces, as often found in robotics. They use samples to approximate and search the space and many popular algorithms have a unity probability of finding a solution, if one exists, with an infinite number of samples (i.e., they are probabilistically complete; Definition 3. ‣ 2.2 Formal Analysis of Sampling-based Motion Planners ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")). The quality of the solutions returned by these algorithms remained an open question until recently.

Karaman and Frazzoli analyze the quality of solutions found by popular sampling-based algorithms and prove that most have zero probability of finding an optimal solution, even with infinite samples. They provide efficient versions of these popular algorithms that instead converge asymptotically to the optimal solution with infinite samples almost surely over all realizations of a sampling distribution (i.e., they are almost-surely asymptotically optimal; Definition 4. ‣ 2.2 Formal Analysis of Sampling-based Motion Planners ‣ 2 SAMPLING-BASED MOTION PLANNING ‣ Asymptotically Optimal Sampling-Based Motion Planning Methods")).
