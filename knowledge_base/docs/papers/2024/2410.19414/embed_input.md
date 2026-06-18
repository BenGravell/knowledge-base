Motion Planning for Robotics: A Review for Sampling-based Planners

Topics include Survey, Motion planning, Robot motion planning, Sampling-based planning, Robotics, Benchmarking.

Reviews ten popular sampling-based motion planners for robotic applications, analyzing their theoretical properties and empirical performance across diverse planning scenarios to highlight ongoing research challenges in the field.

Recent advancements in robotics have transformed industries such as manufacturing, logistics, surgery, and planetary exploration. A key challenge is developing efficient motion planning algorithms that allow robots to navigate complex environments while avoiding collisions and optimizing metrics like path length, sweep area, execution time, and energy consumption. Among the available algorithms, sampling-based methods have gained the most traction in both research and industry due to their ability to handle complex environments, explore free space, and offer probabilistic completeness along with other formal guarantees. Despite their widespread application, significant challenges still remain. To advance future planning algorithms, it is essential to review the current state-of-the-art solutions and their limitations. In this context, this work aims to shed light on these challenges and assess the development and applicability of sampling-based methods. Furthermore, we aim to provide an in-depth analysis of the design and evaluation of ten of the most popular planners across various scenarios....

## Introduction

In recent years, robotics technology has rapidly advanced across various industries, including manufacturing, logistics, robotic surgery, and planetary exploration, bringing profound changes. Among the challenges in robotics, developing efficient and effective motion planning algorithms that help robots navigate complex environments, avoid obstacles, and complete tasks with minimal energy consumption and time is a critical task....

Figure 1: Overview of the most common motion planning techniques in robotics research.

Sampling-based motion planning algorithms are highly effective for exploring continuously-valued spaces, which are commonly encountered in robotics. These algorithms rely on generating samples to approximate and explore the search space. Many sampling-based algorithms are probabilistically complete. But these algorithms do not provide any guarantee on the quality of its solution. In recent years, researchers have focused on addressing this issue. In this article, we have reviewed the progress made....

In summary, by systematically reviewing the state of the art and addressing the remaining challenges, this survey serves as a valuable resource for researchers and practitioners in the field of robotics. It offers a clear understanding of the current landscape of motion planning techniques and provides insights into the future directions of this rapidly evolving area of study.

LaValle and Kuffner's paper "Rapidly-exploring Random Trees: Progress and Prospects" \[\] introduce the basic principles of the standard RRT algorithm and the Extend Tree process, laying the foundation for subsequent advancements. FMT\* \[\] (Fast Marching Tree) leverages the Fast Marching Method (FMM) to enhance the efficiency of RRT in high-dimensional spaces by integrating efficient sampling and searching strategies. Specifically, the FMT\* algorithm uses FMM to quickly evaluate the quality of nodes when building the tree structure, accelerating the convergence of the path planning process....

Kinodynamics, Boeuf et al. \[\] present an incremental state-space sampling technique to avoid generating local trajectories that violate kinodynamic constraints. Other papers prioritize generating samples that maximize clearance, meaning the distance between the robot and its surroundings....
