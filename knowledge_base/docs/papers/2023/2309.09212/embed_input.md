<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RobotPerf: An Open-Source, Vendor-Agnostic, Benchmarking Suite for Evaluating Robotics Computing System Performance

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce RobotPerf, a vendor-agnostic benchmarking suite designed to evaluate robotics computing performance across a diverse range of hardware platforms using ROS 2 as its common baseline. The suite encompasses ROS 2 packages covering the full robotics pipeline and integrates two distinct benchmarking approaches: black-box testing, which measures performance by eliminating upper layers and replacing them with a test application, and grey-box testing, an application-specific measure that observes internal system states with minimal interference. Our benchmarking framework provides ready-to-use tools and is easily adaptable for the assessment of custom ROS 2 computational graphs. Drawing from the knowledge of leading robot architects and system architecture experts, RobotPerf establishes a standardized approach to robotics benchmarking. As an open-source initiative, RobotPerf remains committed to evolving with community input to advance the future of hardware-accelerated robotics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order for robotic systems to operate safely and effective in dynamic real-world environments, their computations must run at real-time rates while meeting power constraints. Towards this end, accelerating robotic kernels on heterogeneous hardware, such as GPUs and FPGAs, is emerging as a crucial tool for enabling such performance[neuman2021robomorphic,liu2021archytas,makoviychuk2021isaac,plancher2022grid,mayoral2022robotcore,wan2022robotic,liu2021robotic]. This is particularly important given the impending end of Moore's Law and the end of Dennard Scaling, which limits single CPU performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While hardware-accelerated kernels offer immense potential, they necessitate a reliable and standardized infrastructure to be effectively integrated into robotic systems. As the industry leans more into adopting such standard software infrastructure, the Robot Operating System (ROS) [quigley2009ros] has emerged as a favored choice. Serving as an industry-grade middleware, it aids in building robust computational robotics graphs, reinforcing the idea that robotics is more than just individual algorithms. The growing dependency on ROS2[ros-robotics-companies], combined with the computational improvements offered by hardware acceleration, accentuates the community's demand for a standardized, industry-grade benchmark to evaluate varied hardware solutions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, there has been a plethora of workshops and tutorials focusing on benchmarking robotics applications[icra2021,icra2022-metrics,icra2022-sbd,iros2020,iros2021,iros2022,iros2023,rss2020,rss2021,rss2022,rss2023], and while benchmarks for specific robotics algorithms[bakhshalipour2022rtrbench,neuman2019benchmarking] and certain end-to-end robotic applications, such as drones[boroujerdian2018mavbench,krishnan2022automatic,krishnan2022roofline,nikiforov2023rose], do exist, the nuances of analyzing general ROS 2 computational graphs on heterogeneous hardware is yet to be fully understood.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A high level overview of RobotPerf. It targets industry-grade real-time systems with complex and extensible computation graphs using the Robot Operating System (ROS2) as its common baseline. Emphasizing adaptability, portability, and a community-driven approach, RobotPerf aims to provide fair comparisons of ROS 2 computational graphs across CPUs, GPUs, FPGAs and other accelerators.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce RobotPerf, an open-source and community-driven benchmarking tool designed to assess the performance of robotic computing systems in a standardized, architecture-neutral, and reproducible way, accommodating the various combinations of hardware and software in different robotic platforms (see Figure[fig:robotperf\_overview]). RobotPerf focuses on evaluating robotic workloads in the form of ROS2 computational graphs on a wide array of hardware setups, encompassing a complete robotics pipeline and emphasizing real-time critical metrics. The framework incorporates two distinct benchmarking methodologies that utilize various forms of instrumentation and ROS nodesto capture critical metrics in robotic systems. These approaches are: black-box testing, which measures performance by eliminating upper layers and replacing them with a test application, and grey-box testing, an application-specific measure that observes internal system states with minimal interference. The framework is user-friendly, easily extendable for evaluating custom ROS 2 computational graphs, and collaborates with major hardware acceleration vendors for a standardized benchmarking approach. It aims to foster research and innovation as an open-source project.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate the framework's capabilities by conducting benchmarks on diverse hardware platforms, including CPUs, GPUs, and FPGAs, thereby showcasing RobotPerf's utility in drawing valuable performance insights.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

RobotPerf's source code and documentation are available at its methodologies are currently being used in industry to benchmark industry-strength, production-grade systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Robot Operating System (ROS and ROS2)", "weight": 1.0} -->

ROS[quigley2009ros] is a widely-used middleware for robot development that serves as a structured communications layer and offers a comprehensive suite of additional functionalities including: open-source packages and drivers for various tasks, sensors, and actuators, as well as a collection of tools that simplify development, deployment, and debugging processes. ROS enables the creation of computational graphs (see Figure [fig:robotperf\_overview]) that connect software processes, known as nodes, through topics, facilitating the development of end-to-end robotic systems. Within this framework, nodes can publish to or subscribe from topics, enhancing the modularity of robotic systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Robot Operating System (ROS and ROS2)", "weight": 1.0} -->

2 builds upon ROS and addresses many of its key limitations. Constructed to be industry-grade, ROS2 adheres to industry Data Distribution Service (DDS) and Real-Time Publish Subscribe (RTPS) standards[OMG-DDSI-RTPS-2.5]. Based on the Data Distribution Service (DDS) standard, it enables fine-grained, direct, inter- and intra-node communication, enhancing performance, reducing latency, and improving scalability. Importantly, these improvements are also designed to support hardware acceleration[mayoral2021adaptivecomputing,mayoral2022robotcore]. Over 600 companies have adopted ROS2 and its predecessor ROS in their production environments, underscoring its significance and widespread adoption in the industry [ros-robotics-companies].

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Robot Operating System (ROS and ROS2)", "weight": 1.0} -->

2 also provides standardized APIs to connect user code through language-specific client libraries, rclcpp and rclpy, which handle the scheduling and invocation of callbacks such as timers, subscriptions, and services. Without a ROS Master, ROS 2 creates a decentralized framework where nodes discover each other and manage their own parameters.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Robot Operating System (ROS and ROS2)", "weight": 1.0} -->

Comparative evaluation of representative existing robotics benchmarks with RobotPerf across essential characteristics for robotic systems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Robotics Benchmarks", "weight": 1.0} -->

There has been much recent development of open-source robotics libraries and associated benchmarks demonstrating their performance as well as a plethora of workshops and tutorials focusing on benchmarking robotics applications [icra2021,icra2022-metrics,icra2022-sbd,iros2020,iros2021,iros2022,iros2023,rss2020,rss2021,rss2022,rss2023].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Robotics Benchmarks", "weight": 1.0} -->

However, most of these robotics benchmarks focus on algorithm correctness (functional testing) in the context of domain specific problems, as well as end-to-end latency on CPUs[sucan2012open,chamzas2021motionbenchmaker,tan2020opencollbench,perille2020benchmarking,mollbenchmarking,nair7dynabarn,kingston2022robowflex,heiden2021bench,ahn2020robel,weisz2016robobench,del2006benchmarks,michel2008rat,murali2019pyrobot,james2020rlbench,leitner2017acrv,zhu2020robosuite,fan2018surreal,althoff2017commonroad]. A few works also analyze some non-functional metrics, such as CPU performance benchmarks, to explore bottleneck behaviors in selected workloads[bakhshalipour2022rtrbench,neuman2019benchmarking,delmerico2018benchmark].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Robotics Benchmarks", "weight": 1.0} -->

Recent work has also explored the implications of operating systems and task schedulers on ROS 2 computational graph performance through benchmarking[reke2020self,barut2021benchmarking,puck2020distributed,yang2020exploring,arafat2022response] as well as by optimizing the scheduling and communication layers of ROS and ROS2 themselves[sugata2017acceleration,ohkawa2019high,choi2021picas,suzuki2018real,gutierrez2018time,gutierrez2018real,gutierrez2018towards,gutierrez2018synch]. These works often focused on a specific context or (set of) performance counter(s).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Robotics Benchmarks", "weight": 1.0} -->

Finally, previous work has leveraged hardware acceleration for select ROS Nodes and adaptive computing to optimize the ROS computational graphs [yamashina2015proposal,yamashina2016crecomp,podlubne2019fpga,eisoldt2021reconfros,lienen2020reconros,9415584,ohkawa2016architecture,panadda2021low,8956928,9397897,ohkawa2018fpga,9355892,amano2021dataset,nitta2018study,chen2021fogros,nvidia2022isaacros,wan2022analyzing]. However, these works do not provide comprehensive frameworks to quickly analyze and evaluate new heterogeneous computational graphs except for two works that are limited to the context of UAVs[boroujerdian2018mavbench,nikiforov2023rose].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Robotics Benchmarks", "weight": 1.0} -->

Research efforts most closely related to our work include ros2\_tracing [bedard2022ros2\_tracing] and RobotCore [mayoral2022robotcore]. ros2\_tracing provided instrumentation that demonstrated integration with the low-overhead LTTng tracer into ROS 2, while RobotCore illuminates the advantages of using vendor-specific tracing to complement ros2\_tracing to assess the performance of hardware-accelerated ROS 2 Nodes. Building on these two specific foundational contributions, RobotPerf offers a comprehensive set of ROS2 kernels spanning the robotics pipeline and evaluates them on diverse hardware. [tab:works]summarizes our unique contributions. It includes a selection of representative benchmarks from above and provides an evaluation of these benchmarks against RobotPerf, focusing on essential characteristics vital for robotic systems. We note that while our current approach focuses only on non-functional performance benchmarking tests, RobotPerf's architecture and methodology can be extended to also measure functional metrics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "RobotPerf: Principles & Methodology", "weight": 1.0} -->

RobotPerf is an open-source, industry-strength robotics benchmark for portability across heterogeneous hardware platforms. This section outlines the important design principles and describes the implementation methodology.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Non-Functional Performance Testing", "weight": 1.0} -->

Currently, RobotPerf specializes in non-functional performance testing, evaluating the efficiency and operational characteristics of robotic systems. Non-functional performance testing measures those aspects not belonging to the system's functions, such as computational latency, memory consumption, and CPU usage.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Non-Functional Performance Testing", "weight": 1.0} -->

In contrast, traditional functional performance testing looks into the system's specific tasks and function, verifying its effectiveness in its primary goals, like the accuracy of the control algorithm in following a planned robot's path. While functional testing confirms a system performs its designated tasks correctly, non-functional testing ensures it operates efficiently and reliably.

<!-- chunk {"id": "body-0022", "role": "body", "section": "ROS 2 Integration & Adaptability", "weight": 1.0} -->

RobotPerf is designed specifically to evaluate ROS 2 computational graphs, rather than focusing on independent robotic algorithms. We emphasize benchmarking ROS2 workloads because the use of ROS2 as middleware allows for the easy composition of complex robotic systems. This makes the benchmark versatile and well-suited for a wide range of robotic applications and enables industry, which is widely using ROS, to rapidly adopt RobotPerf.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Platform Independence & Portability", "weight": 1.0} -->

RobotPerf allows for the evaluation of benchmarks on a variety of hardware platforms, including general-purpose CPUs and GPUs, reconfigurable FPGAs, and specialized accelerators (e.g., ray tracing accelerators [deng2017toward]). Benchmarking robotic workloads on heterogeneous platforms is vital to evaluate their respective capabilities and limitations. This facilitates optimizations for efficiency, speed, and adaptability, as well as fine-tuning of resource allocations, ensuring robust and responsive operation across diverse contexts.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Platform Independence & Portability", "weight": 1.0} -->

Criteria Grey-Box Black-Box Precision Utilizes tracers from in-code instrumentation. Limited to ROS 2 message subscriptions. Performance Low overhead. Driven by kernelspace. Restricted to ROS 2 message callbacks. Recorded by userspace processes. Flexibility Multiple event types. Limited to message subscriptions in current implementation. Portability Requires a valid tracer. Standard format (CTF). Standard ROS 2 APIs. Custom JSON format. Ease of use Requires code modifications and data postprocessing. Tests unmodified software with minor node additions. Real-Robots Does not modify the computational graph. Modifies the computational graph adding extra dataflow.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Flexible Methodology", "weight": 1.0} -->

We offer grey-box and black-box testing methods to suit different needs. Black-box testing provides a quick-to-enable external perspective and measures performance by eliminating the layers above the layer-of-interest and replacing those with a specific test application. Grey-box testing provides more granularity and dives deeper into the internal workings of ROS 2, allowing users to generate more accurate measurements at the cost of increased engineering effort.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Flexible Methodology", "weight": 1.0} -->

As such, each method has its trade-offs, and providing both options enables users flexibility. We describe each method in more detail below and highlight takeaways in Table[tab:tradeoffs].

<!-- chunk {"id": "body-0027", "role": "body", "section": "Grey-Box Testing", "weight": 1.0} -->

Grey-box testing enables precise probe placement within a robot's computational graph, generating a chronologically ordered log of critical events using a tracer that could be proprietary or open source, such as LTTng[desnoyers2006lttng]. As this approach is fully integrated with standard ROS 2 layers and tools through ros2\_tracing, it incurs a minimal average latency of only 3.3 [bedard2022ros2\_tracing], making it well-suited for real-time systems. With this approach, optionally, RobotPerf offers specialized input and output nodes that are positioned outside the nodes of interest to avoid the need to instrument them. These nodes generate the message tracepoints upon publish and subscribe events which are processed to calculate end-to-end latency.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Black-Box Testing", "weight": 1.0} -->

The black-box methodology utilizes a user-level node called the MonitorNode to evaluate the performance of a ROS2 node. The MonitorNode subscribes to the target node, recording the timestamp when each message is received. By accessing the propagated ID, the MonitorNode determines the end-to-end latency by comparing its timestamp against the PlaybackNode's recorded timestamp for each message. While this approach does not need extra instrumentation, and is easier to implement, it offers a less detailed analysis and alters the computational graph by introducing new nodes and dataflow.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Opaque Performance Tests", "weight": 1.0} -->

The requirement for packages to be instrumented directly within the source code poses a challenge to many benchmarking efforts. To overcome this hurdle, for most benchmarks, we refrain from altering the workloads of interest and, instead, utilize specialized input and output nodes positioned outside the primary nodes of concern. This setup allows for benchmarking without the need for direct instrumentation of the target layer. We term this methodology opaque tests," a concept that RobotPerf adheres to when possible.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Reproducibility & Consistency", "weight": 1.0} -->

To ensure consistent and reproducible evaluations, RobotPerf adheres to specific common robotic dataformats. In particular, it uses ROS 2 rosbags, including our own available at as well third-party bags (e.g., the r2b dataset[nvidia\_r2bdataset2023]).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reproducibility & Consistency", "weight": 1.0} -->

To ensure consistent data loading and finer control over message delivery rates, we drew inspiration from [ros2\_benchmark]. Our computational graphs incorporate modified and improved DataLoaderNode and PlaybackNode implementations, which can be accessed at These enhanced nodes offer improvements that report worst-case latency and enable the reporting of maximum latency, introduce the ability to profile power consumption and so forth.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Metrics", "weight": 1.0} -->

We focus on three key metrics: latency, throughput and power consumption including energy efficiency. Latency measures the time between the start and the completion of a task. Throughput measures the total amount of work done in a given time for a task. Power measures the electrical energy per unit of time consumed while executing a given task. Measuring energy efficiency (or performance-per-Watt) captures the total amount of work (relative to either throughput or latency) that can be delivered for every watt of power consumed and is directly related to the runtime of battery powered robots[boroujerdian2018mavbench].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Current Benchmarks and Categories", "weight": 1.0} -->

RobotPerf beta[robotperf\_benchmarks\_repo] introduces benchmarks that cover the robotics pipeline from perception, to localization, to control, as well as dedicated benchmarks for manipulation. The full list of benchmarks in the beta release can be found in Table[tab:benchmarks\_table]. Aligned with our principles defined above, each benchmark is a self-contained ROS 2 package which describes all dependencies (generally other ROS packages). To facilitate reproducibility, all benchmarks are designed to be built and run using the common ROS 2 development flows (ament build tools, colcon meta-build tools, etc.). Finally, so that the benchmarks can be easily consumed by other tools, a description of each benchmark, as well as its results, is defined in a machine-readable format. As such, accompanying the package.xml and CMakeLists.txt files required for all ROS packages, a YAML file named benchmark.yamlis in the root of each benchmark which describes the benchmark and includes accepted results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Run Rules", "weight": 1.0} -->

To ensure the reliability and reproducibility of the performance data, we adhere to a stringent set of run rules.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Run Rules", "weight": 1.0} -->

First, tests are performed in a controlled environment to ensure that performance data is not compromised by fluctuating external parameters. As per best practices recommended by ros2\_tracing[bedard2022ros2\_tracing], we record and report settings like clock frequency and core count. Second, we look forward to the possibility of RobotPerf being embraced by the community and have results undergo peer review, which can contribute to enhancing reproducibility and accuracy. Finally, we aim to avoid overfitting to specific hardware setups or software configurations by encompassing a broad spectrum of test scenarios.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We conduct comprehensive benchmarking using RobotPerf to evaluate its capabilities on three key aspects vital for a robotics-focused computing benchmark. First, we validate the framework's capacity to provide comparative insights across divergent heterogeneous platforms from edge devices to server-class hardware. Second, we analyze the results to understand RobotPerf's ability to guide selection of the optimal hardware solution tailored to particular robotic workloads. Finally, we assess how effectively RobotPerf reveals the advantages conferred by hardware and software acceleration techniques relative to general-purpose alternatives.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Fair and Representative Assessment of Heterogeneity", "weight": 1.0} -->

Assessing hardware heterogeneity in robotic applications is imperative in the ever-evolving field of robotics. Different robotic workloads demand varying computational resources and efficiency levels. Therefore, comprehensively evaluating performance across diverse hardware platforms We evaluated the RobotPerf benchmarks over a wide list of hardware platforms, including general-purpose CPUs on edge devices (e.g., Qualcomm RB5), server-class CPUs (e.g., Intel i7-8700), and specialized hardware accelerators (e.g., AMD Kria KR260). Figure [fig:colors\_hardware] illustrates benchmark performance in robotics per category of workload (perception, localization, control, and manipulation) using radar plots, wherein the different hardware solutions are depicted together alongside different robotic workloads per category. Each hardware solution is presented with a different color, with smaller values and areas representing better performance in the respective category.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Fair and Representative Assessment of Heterogeneity", "weight": 1.0} -->

Given our ability to benchmark 18 platforms (bottom of Figure[fig:colors\_hardware]), RobotPerf is capable of benchmarking heterogeneous hardware platforms and workloads, paving the way for community-driven co-design and optimization of hardware and software.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Quantitative Approach to Hardware Selection", "weight": 1.0} -->

The rapid evolution and diversity of tasks in robotics means we need to have a meticulous and context-specific approach to computing hardware selection and optimization. A one-size-fits-all hardware strategy would be an easy default selection, but it fails to capitalize on the nuanced differences in workload demands across diverse facets like perception, localization, control, and manipulation, each exhibiting distinctive sensitivities to hardware capabilities. Therefore, a rigorous analysis, guided by tools like RobotPerf, becomes essential to pinpoint the most effective hardware configurations that align well with individual workload requirements.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Quantitative Approach to Hardware Selection", "weight": 1.0} -->

The results in Figure [fig:colors\_hardware] demonstrate the fallacy of a one-size-fits-all solution. For example, focusing in on the latency radar plot for control from Figure [fig:colors\_hardware] (col 3, row 1), we see that the i7-12700H (I7H) outperforms the NVIDIA AGX Orin Dev. Kit (NO) on benchmarks C1, C3, C4, and C5, but is $6.5\times$ slower on benchmark C2. As such, by analyzing data from the RobotPerf benchmarks, roboticists can better determine which hardware option best suits their needs given their specific workloads and performance requirements.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quantitative Approach to Hardware Selection", "weight": 1.0} -->

One general lesson learned while evaluating the data is that each workload is unique, making it hard to generalize across both benchmarks and categories. To that end, RobotPerf results help us understand how the use of various hardware solutions and dedicated domain-specific hardware accelerators significantly improves the performance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Quantitative Approach to Hardware Selection", "weight": 1.0} -->

Benchmark comparison of perception latency (ms) on AMD's Kria KR260 with and without the ROBOTCORE Perception accelerator. The benchmarks used are a1, a2, and a5 as defined in Tabletab:benchmarks\_table. We find that hardware acceleration can enable performance gains of as much as 11.5$\times$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Rigorous Assessment of Acceleration Benefits", "weight": 1.0} -->

In the rapidly advancing field of computing hardware, the optimization of algorithm implementations is a crucial factor in determining the success and efficiency of robotic applications. The need for an analytical tool, like RobotPerf, that facilitates the comparison of various algorithmic implementations on uniform hardware setups becomes important. [fig:robotperf\_perception\_comparison\_KR260] is a simplified version of Figure [fig:colors\_hardware], depicting AMD's Kria KR260 hardware solution in two forms: the usual hardware and a variant that leverages a domain-specific hardware accelerator (ROBOTCORE Perception, a soft-core running in the FPGA for accelerating perception robotic computations). The figure demonstrates that hardware acceleration can enable performance gains of as much as 11.5$\times$ (from 173ms down to 15ms for benchmark a5). We stress that the results obtained here should be interpreted according to each end application and do not represent a generic recommendation on which hardware should be used. Other factors, including availability, the form factor, and community support, are relevant aspects to consider when selecting a hardware solution.
