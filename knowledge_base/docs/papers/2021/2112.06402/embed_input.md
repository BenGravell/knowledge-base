MotionBenchMaker: A Tool to Generate and Benchmark Motion Planning Datasets

Recently, there has been a wealth of development in motion planning for robotic manipulation new motion planners are continuously proposed, each with their own unique strengths and weaknesses. However, evaluating new planners is challenging and researchers often create their own ad-hoc problems for benchmarking, which is time-consuming, prone to bias, and does not directly compare against other state-of-the-art planners. We present MotionBenchMaker, an open-source tool to generate benchmarking datasets for realistic robot manipulation problems. MotionBenchMaker is designed to be an extensible, easy-to-use tool that allows users to both generate datasets and benchmark them by comparing motion planning algorithms. Empirically, we show the benefit of using MotionBenchMaker as a tool to procedurally generate datasets which helps in the fair evaluation of planners. We also present a suite of 40 prefabricated datasets, with 5 different commonly used robots in 8 environments, to serve as a common ground to accelerate motion planning research.

## Introduction

Motion planning is a core component of robotic manipulation. For example, motion planning is essential in pick-and-place tasks, finding geometrically-constrained motions such as opening drawers and doors, and as a tool in task and motion planners to evaluate the feasibility of long-horizon plans. The multitude of applications of motion planning has given rise to a multitude of motion planners to tackle these specific problems, each employing their own heuristics to address the challenging general problem.

Despite the plethora of planning methods proposed over the years, little emphasis has been placed on creating a common ground to evaluate these planners---there are no shared benchmarking datasets tailored to manipulation problems that are commonly found in the literature. The lack of shared environments for evaluation often forces researchers to create their own, making it challenging for practitioners to understand the advantages or disadvantages of a particular method if not directly compared....

Figure 9: Timing results for three planners (bkpiece, rrtConnect, and biest) in 4 environments from Fig. 6 (both geometric and sensed) on 3 different robots (the Fetch, UR5, Baxter) for a total of 12 datasets. We plan for both arms of the Baxter in the table environment while for only in the rest. In each plot on this matrix, the value of each of the planner’s range parameters (which controls 𝒞-space expansion) is varied between 0 to 7, in increments of 0.25. The average planning time over the 100 problems in the dataset for each range parameter is shown on a log scale, plotted as a line....

V-A Wrong Hypothesis
Undoubtedly, in any research field, it is necessary to compare the performance of different methods. In motion planning research, it is often the case that a practitioner has a specific robot and target application in mind, which begets the need to manually construct an appropriate benchmark. Creating a benchmark from scratch without the appropriate tools is both time-consuming and challenging since a large number of problems might be required to achieve statistical significance....

In-hand manipulation benchmark
\xintFor #1 in 0,0,0,1,0,1 \do \xintifForFirst&amp; ×

Multi-Agent Path-Find Benchmark
\xintFor #1 in 0,1,0,0,0,0 \do \xintifForFirst&amp; ×
