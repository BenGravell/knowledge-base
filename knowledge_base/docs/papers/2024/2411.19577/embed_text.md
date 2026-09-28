<!-- arxiv-full-text:v1 {"arxiv_id": "2411.19577", "source": "arxiv-html"} -->

## Introduction

Autonomous vehicles have been widely developed in the last decades due to their impact on automotive transportation and their benefit to society (e.g., reducing vehicle collisions, and providing personal mobility to disabled people). It is important to ensure the safety and reliability of autonomous vehicles for world-wide adoption. Therefore, on-road testing is widely used by leading companies. However, autonomous vehicles would have to be driven more than 11 billion miles to demonstrate with 95% confidence that they are 20% safer than human drivers. It is expensive for on-road testing to achieve this goal, and it is also impossible for on-road testing to test corner cases or dangerous situations.

To this end, scenario-based testing is also widely used by leading companies to simulate diverse driving scenarios. As of February 2021, Waymo's autonomous vehicles have been tested with over 15 billion miles of simulated driving. Various approaches have been developed to generate driving scenarios. However, they mainly focus on the diversity in vehicle/pedestrian behaviors and weather conditions, but overlook the diversity in roads. Several recent advances have been proposed on generating road scenarios. However, they either generate basic road components (e.g., highway interchanges) without a complete road network, or build a complete road network but with simple road components (i.e., straight roads and junctions). Therefore, their generated road scenarios lack diversity in both topology and geometry.

To address the problem, we propose RoadGen to systematically generate diverse road scenarios. First, we define and implement eight types of basic road components. Each road component is parameterized to reflect its geometry diversity. Second, we connect road components to form road scenarios. This process is guided by favoring the selection of least used road components so as to ensure the geometry diversity of road scenarios. Third, we remove duplicated road scenarios that have the same topology to ensure the topology diversity of road scenarios. Finally, we convert the generated road scenarios into high-precision (HD) map files and 3D scene files, which can be used for joint simulation by simulators.

To evaluate the effectiveness of RoadGen, we use RoadGen to generate road scenarios that have 4, 5, 6, 7 and 8 road components. Our results have demonstrated that RoadGen can generate more diverse road scenarios than a baseline approach that randomly selects and connects road components. Furthermore, to evaluate the usefulness of RoadGen, we sample road scenarios and convert them into HD map files and 3D scene files for joint simulation on SORA-SVL with Apollo 8.0. Our results have indicated that over 92% of the road scenarios can be useful for joint simulation.

In summary, this work makes the following contributions.

We define and implement eight types of parameterized basic road components.

We propose a guided approach to connect road components to generate diverse road scenarios.

We conduct experiments to demonstrate the effectiveness and usefulness of RoadGen, and build a dataset of road scenarios for simulation testing.

## Related Work and Problem Statement

### II-A Related Work

Scenarios are important for developing and testing autonomous vehicles. To represent scenarios, Bagschik et al. develop a 5-layer model, including road-level (layer 1), traffic infrastructure (layer 2), manipulation of layer 1 and 2 (layer 3), objects (layer 4), and environment (layer 5), while Scholtes et al. extend it by adding digital information as layer 6. To generate scenarios, various approaches have been developed, e.g., extracting scenarios from driving data or crash data, and searching scenarios by evolutionary algorithms or combinatorial interaction testing.

However, recent surveys show that most scenario generation approaches have focused on scenarios at layer 4 and 5 by manipulating vehicles, pedestrians and weather conditions, while little attention has been paid on road topology and geometry, and traffic signs (i.e., layer 1, 2 and 3), which serve as the base of any scenario. Zhou et al. propose a model-driven method to generate highway interchanges that are one basic component in road networks. Rietsch et al. also attempt to generate basic components, i.e., roundabout, intersections, highway entry, drive and exit. Differently, our work aims to compose road networks based on basic components. Tang et al. first extract junction features from HD maps, and then build road networks by connecting the junctions in a grid layout. Paranjape et al. generate road networks with different road sizes and intersections. However, these approaches only consider straight roads and junctions, and thus the generated road networks lack diversity.

### II-B Problem Statement

This work is focused on the road-level (layer 1) scenario of the 5-layer model, which describes the topology and geometry of road scenarios. Specifically, the topology of a road scenario can be characterized by how different road components (e.g., straight road, curve road, fork road, and intersection) are connected together. The geometry of a road scenario can be characterized by factors like the number of lanes and the type of lane markings. The diversity of road scenarios in both topology and geometry is important for developing and testing autonomous vehicles. Therefore, our problem can be stated as how to systematically generate road scenarios such that they have diverse topology and geometry.

## Methodology

Fig. 1: Approach Overview of RoadGen We propose RoadGen to systematically generate diverse road scenarios. An overview of RoadGen is presented in Fig. 1. Each step of RoadGen is explained below.

### III-A Road Component Implementation

Based on our understanding of real-life roads, we decompose roads into distinct segments, and define eight types of typical road components, as illustrated in Fig. 2. To reflect geometry diversity, each road component can be parameterized by road length ($L$), lane width ($W$), the number of lanes ($LaneNum$), the type of lane markings ($LaneMarks$), the coordinate of the starting point ($Start$), and the direction to position the component from the starting point ($Direction$).

Fig. 2: Eight Types of Typical Road Components Straight. As shown in Fig. 2(a), a straight road follows a linear trajectory without any curves, bends, or turns.

Curve. As shown in Fig. 2(b), a curve road changes its direction as it progresses. We apply Bézier curves to construct the lane curve. A Bézier curve $B(t)$ can be constructed by four control points $P_{0}-P_{3}$, i.e., $B(t)=(1-t)^{3}P_{0}+3(1-t)^{2}tP_{1}+3(1-t)t^{2}P_{2}+t^{3}P_{3},\ t\in$.

Lane Switch. As shown in Fig. 2(c), a lane switch road undergoes a transition about the number of lanes (e.g., changing from 2 lanes to 3 lanes).

Fork. As shown in Fig. 2(d), a fork road is a road segment where a single road splits into two separate roads, or two separate roads merge into a single road.

T-Intersection. As shown in Fig. 2(e), a T-intersection is a junction where one road meets another road at a right angle. It creates a three-way intersection where vehicles on the main road can continue straight, while vehicles on the intersecting road can turn left or right.

Intersection. As shown in Fig. 2(f), intersection is a junction where two roads meet or cross each other.

U-Shaped Road. As shown in Fig. 2(g), a U-shaped road is a road segment where a 180-degree turn is required to go in the opposite direction. It can be considered as being composed of two straight road segments and a circular arc segment.

Roundabout. As shown in Fig. 2(h), a roundabout is a junction where traffic from four roads flows around a central island in a counterclockwise direction (in countries with right-hand traffic).

After defining the eight types of road components, we use Python to implement programming templates for these road components. These templates can be instantiated to generate MATLAB scripts which describe the road components. As illustrated in Listing 1, all templates are primarily composed of the following steps, i.e., initializing the lanes contained in a component according to $LaneNum$, drawing coordinates of lanes and boundaries based on $L$, $W$, $Start$ and $Direction$, setting lane markings according to $LaneMarks$, and combining lanes to form the component by assigning references to lane predecessor and successor.

We provide different templates for each road component based on the number of lanes ($LaneNum$) and the type of lane markings ($LaneMarks$). These templates are distinct from each other, encompassing 1 to 6 lanes and any of the seven types of lane markings based on real-world road rules (i.e., white dashed lane lines, white solid lane lines, white double solid lane lines, yellow dashed lane lines, yellow solid lane lines, yellow double solid lane lines, and yellow dashed-solid lane lines). Specifically, we provide a total of 242 unique templates for these eight types of road components.

When instantiating these templates, we only need to specify the road length ($L$), lane width ($W$), coordinate of starting point ($Start$), and direction to position the road component ($Direction$). For curve road, we also need to specify $P_{0}-P_{3}$. For U-shaped road, we also need to specify $D$ to denote the distance between the two straight road segments, and $X$ to control the arc segment. We can calculate the coordinates of the road and boundaries to fill in the template based on these input parameters, thereby instantiating the component.

1 % Initialize lanes in a component using LaneNum. 2 Lanes(LaneNums) = roadrunner.hdmap.Lane; 3 % Draw coordinates of lanes and boundaries. 4 Lanes.Geometry = deal([coordinates of lanes]); 5 LaneBoundaries.Geometry = deal([coordinates of boundaries]); 6 % Set lane markings according to LaneMarks. 7 LaneBoundaries.ParametricAttributes = deal(LaneMarks) 8 % Combine lanes with predecessors and successors 9 % where i,j,k represent the ID of lanes. 10 Lane(i).Predecessors = roadrunner.hdmap.Reference(Lane(j)); 11 Lane(i).Successors = roadrunner.hdmap.Reference(Lane(k)); Listing 1: Part of a Sample Template for Road Components

### III-B Guided Road Component Connection

Input: CompList, TotalCount, Constraints, Candidates 2 while budget is not reached do 5 C = selectFirstComp(CompList, CompCount); 11 EndpointQueue.add(c.getEndpoints); 12 while Count < TotalCount && EndpointQueue ≠ ∅ do 14 if random || isLast(EndpointQueue, p) then 15 Cands = Candidates[p.Type]; 16 while length(Cands) > 0 do 17 D = selectLeastUse(Cands, CompCount); 18 d = inst(p, Constraints, D, CoveredArea); 25 EndpointQueue.add(d.getEndpoints); Algorithm 1 Guided Road Scenario Generation We design a guided algorithm to connect instantiated road components to generate diverse road scenarios, as presented in Algorithm 1. It has four inputs: $CompList$, the 242 programming templates for the road components as implemented in Sec. III-A; $TotolCount$, the number of instantiated road components included in one road scenario; $Constraints$, the constraints about parameters of each road component (e.g., the valid range of road length and lane width), which need to be satisfied, when road components are instantiated, to make the generated road scenarios as realistic as possible; and $Candidates$, the candidate road components from the 242 programming templates that can be connected to each type of endpoints. Each road component has one or multiple endpoints that can be connected to the starting point of other road components. For example, a roundabout has three endpoints. Hence, we summarize the types of different endpoints, and compute their candidate road components. For example, a 2-lane bidirectional solid-line endpoint can be connected to a straight road with 2-lane bidirectional solid-line. The output of Algorithm 1 is a set of road scenarios $RoadScenSet$ in the form of MATLAB scripts.

This algorithm starts by initializing $CompCount$, which records the number of times each of the road components in $CompList$ is used (Line 1). $CompCount$ is used to guide our algorithm to favor the selection of least used road components during generation. Then, it generates one road scenario $RoadScen$ in each loop iteration until certain type of budget is reached, e.g., a time budget of 24 hours is reached (Line 2-35). Specifically, in each iteration, it selects a least used road component $C$ from $CompList$ as the first road component to ensure geometry diversity (Line 5), and instantiates it to get an instance $c$ of $C$ which satisfies $Constraints$ (Line 6). Then, it updates $RoadScen$, updates $Count$ to record the number of used road components, updates $CoveredArea$ to record the occupied area of the road scenario, updates $CompCount$ to record the usage of $C$, and adds the endpoints of $c$ to a queue $EndpointQueue$ (Line 7-11).

As long as the current road scenario can be potentially further connected to other road components, i.e., $Count$ is less than $TotalCount$ and $EndpointQueue$ is not empty (Line 12), it pops from $EndpointQueue$ an endpoint $p$ from which $RoadScen$ is further expanded (Line 13). If $random$ (returning either $true$ or $false$) returns $true$ or $p$ is the last one in $EndpointQueue$ (Line 14), it starts to expand $RoadScen$ at $p$ (Line 15-31). Here, the randomness caused by $random$ is leveraged to ensure topology diversity.

Then, it obtains from $Candidates$ the candidate road components $Cands$ that can be connected to $p$ according to the type of $p$ (Line 15). Next, it selects the least used road component $D$ from $Cands$ to ensure geometry diversity (Line 17), and instantiates it to get an instance $d$ of $D$ which satisfies $Constraints$, matches with $p$, and does not overlap with the current road scenario (Line 18). Specifically, it uses the covered area of $RoadScen$ and the covered area of $d$, i.e., $CoveredArea$ and $d.getCoveredArea$, to determine whether overlap occurs. If such a $d$ is found (Line 19), it updates $RoadScen$ by adding $d$ and connecting to $d$ through $p$ (Line 20-21), updates $Count$, $CoveredArea$, $CompCount$, and $EndpointQueue$ (Line 22-25), and breaks to continue expanding $RoadScen$ at other endpoints (Line 26). If such a $d$ is not found, it removes $D$ from $Cands$ (Line 29), and tries to select the next least used road component from $Cands$.

### III-C Road Scenario Deduplication

The generated road scenarios can be similar in their topology, i.e., the types of road components and the connections between road components in two road scenarios can be similar, thus hurting the topology diversity. Hence, we propose a similarity metric to measure the topology similarity, and use it to remove duplicated road scenarios to ensure diversity.

We first define a road scenario as an undirected graph in Definition 1 to model the topology of a road scenario.

### Definition 1

A generated road scenario can be modeled as an undirected graph $\mathbb{G}=\langle V,E\rangle$, where $V$ is a set of vertices denoting the road components within the road scenario, and $E\subseteq V\times V$ is a set of undirected edges denoting the connections between road components.

### Definition 2

Given two road scenarios $\mathbb{G}=\langle V,E\rangle$ and $\mathbb{G^{\prime}}=\langle V^{\prime},E^{\prime}\rangle$, and $e=(u,v)\in E$, $u,v\in V$, if $\exists~u^{\prime},v^{\prime}\in V^{\prime}$, $(u^{\prime},v^{\prime})\in E^{\prime}$ such that $Type(u,v)=Type(u^{\prime},v^{\prime})$, $e$ is regarded as duplicated in $\mathbb{G^{\prime}}$, denoted as $DE(e,\mathbb{G^{\prime}})=1$; otherwise, $DE(e,\mathbb{G^{\prime}})=0$. Here, $Type(u,v)$ returns the types of road component $u$ and $v$.

### Definition 3

Given two road scenarios $\mathbb{G}=\langle V,E\rangle$ and $\mathbb{G^{\prime}}=\langle V^{\prime},E^{\prime}\rangle$, and $u\in V$, if $\forall~(u,v_{i})\in E$, $v_{i}\in V$ such that $DE((u,v_{i}),\mathbb{G^{\prime}})=1$, $u$ and its connections are regarded as duplicated in $\mathbb{G^{\prime}}$, denoted as $DV(u,\mathbb{G^{\prime}})=1$; otherwise, $DV(u,\mathbb{G^{\prime}})=0$.

Based on Definition 2 and 3, we define a similarity metric $Sim_{(\mathbb{G}_{1},\mathbb{G}_{2})}$ to measure the topology similarity between two road scenarios $\mathbb{G}_{1}$ and $\mathbb{G}_{2}$, as formulated in Equation 1, where $\mathbb{G}_{1}=\langle V_{1},E_{1}\rangle$, $\mathbb{G}_{2}=\langle V_{2},E_{2}\rangle$, $u_{i}\in V_{1}$ and $v_{i}\in V_{2}$.

### Definition 4

Given two road scenarios $\mathbb{G}=\langle V,E\rangle$ and $\mathbb{G^{\prime}}=\langle V^{\prime},E^{\prime}\rangle$, $\mathbb{G}$ and $\mathbb{G^{\prime}}$ are regarded as duplicated in the topology if $Sim_{(\mathbb{G},\mathbb{G^{\prime}})}=1$.

Based on Definition 4, we remove duplicated road scenarios to ensure the topology diversity. Notice that we can also use this similarity metric to keep the road scenarios whose similarity to existing road scenarios is below a threshold.

### III-D Joint Simulation

Given the deduplicated road scenarios in the form of MATLAB scripts, we first adopt MATLAB to compile the scripts into RoadRunner HD map files (i.e., rrhd files). Here we use the rrhd format because RoadRunner provides programmatic interfaces to import rrhd files and export HD map file types needed by various autonomous driving systems (e.g., Apollo and Autoware) as well as 3D scene file types required by various simulators (e.g., SORA-SVL and CARLA). Then, we use RoadRunner to convert rrhd files into target HD map files and 3D scene files for joint simulation on a target simulator with a target autonomous driving system.

## Evaluation

We have implemented a prototype of RoadGen in 354K lines of Python and MATLAB code, and released the source code of our prototype as well as all the experimental data at our website To evaluate the effectiveness and usefulness of RoadGen, we design the following two research questions (RQs).

RQ1 Effectiveness Evaluation: How is the effectiveness of RoadGen in generating diverse road scenarios?

RQ2 Usefulness Evaluation: Can the road scenarios generated by RoadGen be used for simulation?

### IV-A Evaluation Setup

Fig. 3: The Number of Deduplicated Road Scenarios and Uniqueness Rate of RoadGen and Rand over Time RQ Setup. To answer RQ1, we compare the effectiveness of RoadGen with a baseline approach, referred to as Rand, which randomly selects and connects road components. We set the number of road components included in each road scenario to 4, 5, 6, 7 and 8, respectively, and continuously generate road scenarios for 24 hours using RoadGen and Rand. We record the number of generated road scenarios after deduplication, the uniqueness rate (i.e., the rate between the number of generated road scenarios after and before deduplication), and the time for covering different road components. We run the experiment 5 times, and report the average results.

To answer RQ2, we leverage Apollo 8.0 and SOAR-SVL to demonstrate the usefulness of RoadGen from three perspectives, the usability of 3D scenes, the usability of HD maps, and the usability for joint simulation.

Experimental Environment Setting. We conduct all the experiments on a Ubuntu 20.04.4 LTS server with 4 NVIDIA GeForce RTX 3090 GPUs, Inter Core i9-10980XE CPU with 3.00GHz processor, and 128GB memory.

Road Scenario Size TABLE I: Statistics about Road Scenarios Generated within 24 Hours

### IV-B Effectiveness Evaluation (RQ1)

Overall Results. Table I presents the statistics about the road scenarios generated by RoadGen and Rand within 24 hours. The first column gives the road scenario size in terms of number of road components, the second and third columns show the number of generated road scenarios after deduplication, and the fourth and fifth columns list the uniqueness rate.

Specifically, across the five groups of experiments with respect to different road scenario sizes, RoadGen generate a minimum number of 400 deduplicated road scenarios when road scenario size is set to 4, and a maximum number of 580 deduplicated road scenarios when road scenario size is set to 5. In addition, on average, RoadGen generates 3.9% more deduplicated road scenarios than Rand across all the five groups of experiments, which is statistically significant.

Besides, in terms of uniqueness rate, RoadGen significantly outperforms Rand by 19.3% on average. In the four groups of experiments with road scenario size ranging from 5 to 8, the uniqueness rate of RoadGen fluctuates between 0.5 and 0.7. However, in the group of experiments with road scenario size setting to 4, RoadGen exhibits a relatively low uniqueness rate. This also holds for Rand. It is because the fewer the number of used road components, the more likely the generated road scenarios will have a higher similarity.

Detailed Results over Time. Fig. 3 illustrates a detailed comparison over time between RoadGen and Rand when road scenario size is set to 5 and 7 in terms of the number of deduplicated road scenarios and the uniqueness rate. Due to space limitation, we provide the results when road scenario size is set to 4, 6 and 8 at our website.

Specifically, in the early stages of generation, the number of deduplicated road scenarios generated by RoadGen is smaller than that of Rand. This is because RoadGen consumes more time than Rand due to our guidance computation, and thus generates a smaller number of road scenarios before deduplication. However, as time goes , the number of covered road components increases, and Rand gradually generates more duplicated road scenarios, and thus its deduplicated road scenarios are gradually less than those generated by RoadGen. This results in a gradual decline in the uniqueness rate, while the difference between RoadGen and Rand becomes more significant.

Fig. 4: Comparison of Time for Covering Different Road Components (c) Demonstration of Joint Simulation Fig. 5: A Case Study that Demonstrates the Usability of 3D Scene Files and HD Maps and the Usability for Joint Simulation Time for Covering Road Components. Fig. 4 ‣ IV Evaluation ‣ RoadGen: Generating Road Scenarios for Autonomous Vehicle Testing") presents the number of different road components covered by generated road scenarios over time. The solid lines represent the five groups of experiments of RoadGen, and the dashed lines represent the five groups of experiments of Rand.

Specifically, RoadGen respectively spends 0.89, 1.34, 1.40, 1.23 and 1.38 hours to cover all the 242 road components when road scenario size is respectively set to 4, 5, 6, 7 and 8, while Rand respectively costs 4.53, 10.57, 8.61, 6.64 and 8.42 hours. On average, RoadGen spends 1.24 hours to cover all the 242 road components, while Rand costs 7.75 hours; i.e., RoadGen is 83.9% faster than Rand in covering all the 242 road components.

Summary. These results indicate that our guided approach RoadGen is effective in generating more diverse road scenarios in the same time than the baseline random approach, and covers all the different road components more quickly.

Road Scenario Size TABLE II: Success Rate of Compiling Scripts into 3D Scene Files

### IV-C Usefulness Evaluation (RQ2)

Due to the large number of road scenarios in the format of MATLAB scripts generated in RQ1, we evaluate their usefulness by a sampling approach. Specifically, we set the confidence level to 95% and the margin error to 5% to determine the sample size, and randomly sample road scenarios generated by RoadGen in RQ1. The third column of Table II ‣ IV Evaluation ‣ RoadGen: Generating Road Scenarios for Autonomous Vehicle Testing") reports the sample size under each road scenario size.

Usability of 3D Scenes. We leverage RoadRunner to compile the sampled road scenario scripts into 3D scene files. The last column of Table II ‣ IV Evaluation ‣ RoadGen: Generating Road Scenarios for Autonomous Vehicle Testing") lists the success rate of compilation. Specifically, more than 92% of the road scenarios scripts can be successfully compiled into 3D scene files. We investigate the cases where compilation fails, and find that it is caused by the excessive curvature of certain U-shaped road components. We will address this issue in future updates. Moreover, we validate all 3D scene files using the built-in scenario simulation tool in RoadRunner, and the vehicles included therein are able to recognize lane markings, and perform path planning, lane changes and other behaviors with all 3D scene files. One sample demonstration is illustrated in Fig. 5(a) ‣ IV Evaluation ‣ RoadGen: Generating Road Scenarios for Autonomous Vehicle Testing").

Usability of HD Maps. We utilize RoadRunner to convert those sampled road scenario scripts, which are successfully compiled into 3D scene files, into HD map files for the latest Apollo 8.0. We import these HD map files into Apollo, and restart Dreamview (i.e., Apollo's fullstack HMI service) to load the HD maps. We determine the usability of HD maps through manual verification, i.e., running the routing testing in Apollo's built-in sim-control mode, which does not require any third-party simulators. We set points of interest in sim-control, and let Apollo conduct path planning. All HD map files are successfully used in routing testing in sim-control mode. One sample demonstration is shown in Fig. 5(b) ‣ IV Evaluation ‣ RoadGen: Generating Road Scenarios for Autonomous Vehicle Testing").

Usability for Joint Simulation. We first import each 3D scene file into Unity, and manually set the SpawnInfo which contains the starting position and end position of a target vehicle. Then, we import the resulting scene binary file called AssetBundle into SORA-SVL, and bridge it with Apollo 8.0. We use the SORA-SVL's Python API to start joint simulation in Dreamview and SORA-SVL. All the joint simulations are successful. One sample demonstration is shown in Fig. 5(c) ‣ IV Evaluation ‣ RoadGen: Generating Road Scenarios for Autonomous Vehicle Testing").

Summary. These results indicate that more than 92% of the generated road scenarios are useful for joint simulation.

### IV-D Limitations

While the proposed approach demonstrates promising results, it still suffers several limitations. First, we define eight types of typical road components, which is not meant to be exhaustive but is to illustrate the feasibility of our approach. We plan to further extend the types of road components according to regulations in different countries.

Second, we currently only focus on the road-level scenario (i.e., layer 1 of the 5-layer model ) without taking into account traffic signs, static and dynamic objects, etc. in the upper layers. We are integrating these elements into RoadGen.

Third, we evaluate the usefulness of RoadGen only on SORA-SVL with Apollo. However, RoadRunner supports the export of HD map files and 3D scene files in various formats required by various simulators and autonomous driving systems. We believe that RoadGen is still applicable in other simulators and autonomous driving systems.

## Conclusions

This paper propose RoadGen to systematically generate diverse road scenarios in both topology and geometry. First, eight types of typical road components are defined and implemented. Then, RoadGen uses a guided algorithm to connect road components to generate road scenarios, and uses a similarity metric to remove duplicated road scenarios. Our experimental results have demonstrated the promising effectiveness and usefulness of RoadGen in generating diverse road scenarios for joint simulation. Our dataset of road scenarios is also released for fostering simulation testing. In the future, we plan to extend RoadGen to support more types of road components and integrate upper-layer scenario elements, and investigate the applicability of RoadGen in other simulators and autonomous driving systems.
