RobotPerf: An Open-Source, Vendor-Agnostic, Benchmarking Suite for Evaluating Robotics Computing System Performance

We introduce RobotPerf, a vendor-agnostic benchmarking suite designed to evaluate robotics computing performance across a diverse range of hardware platforms using ROS 2 as its common baseline. The suite encompasses ROS 2 packages covering the full robotics pipeline and integrates two distinct benchmarking approaches: black-box testing, which measures performance by eliminating upper layers and replacing them with a test application, and grey-box testing, an application-specific measure that observes internal system states with minimal interference. Our benchmarking framework provides ready-to-use tools and is easily adaptable for the assessment of custom ROS 2 computational graphs. Drawing from the knowledge of leading robot architects and system architecture experts, RobotPerf establishes a standardized approach to robotics benchmarking. As an open-source initiative, RobotPerf remains committed to evolving with community input to advance the future of hardware-accelerated robotics.

## Introduction

In order for robotic systems to operate safely and effective in dynamic real-world environments, their computations must run at real-time rates while meeting power constraints. Towards this end, accelerating robotic kernels on heterogeneous hardware, such as GPUs and FPGAs, is emerging as a crucial tool for enabling such performance. This is particularly important given the impending end of Moore's Law and the end of Dennard Scaling, which limits single CPU performance.

While hardware-accelerated kernels offer immense potential, they necessitate a reliable and standardized infrastructure to be effectively integrated into robotic systems. As the industry leans more into adopting such standard software infrastructure, the Robot Operating System (ROS) has emerged as a favored choice. Serving as an industry-grade middleware, it aids in building robust computational robotics graphs, reinforcing the idea that robotics is more than just individual algorithms.

In this paper, we introduce RobotPerf, an open-source and community-driven benchmarking tool designed to assess the performance of robotic computing systems in a standardized, architecture-neutral, and reproducible way, accommodating the various combinations of hardware and software in different robotic platforms (see Figure 1). RobotPerf focuses on evaluating robotic workloads in the form of ROS 2 computational graphs on a wide array of hardware setups, encompassing a complete robotics pipeline and emphasizing real-time critical metrics.

RobotPerf's source code and documentation are available at and its methodologies are currently being used in industry to benchmark industry-strength, production-grade systems.

## Conclusion and Future Work

RobotPerf represents an important step towards standardized benchmarking in robotics. With its comprehensive evaluation across the hardware/software stack and focus on industry-grade ROS 2 deployments, RobotPerf can pave the way for rigorous co-design of robotic hardware and algorithms. As RobotPerf matures with community involvement, we expect it to compare CPU, GPU and FPGA, exploring their power consumption and flexibility in augmenting real-world robotic computations.
