<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning

Topics include Reinforcement learning, Online algorithms, Learning, Energy consumption, Sustainable development, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Accurate reporting of energy and carbon usage is essential for understanding the potential climate impacts of machine learning research. We introduce a framework that makes this easier by providing a simple interface for tracking realtime energy consumption and carbon emissions, as well as generating standardized online appendices. Utilizing this framework, we create a leaderboard for energy efficient reinforcement learning algorithms to incentivize responsible research in this area as an example for other areas of machine learning. Finally, based on case studies using our framework, we propose strategies for mitigation of carbon emissions and reduction of energy consumption. By making accounting easier, we hope to further the sustainable development of machine learning experiments and spur more research into energy efficient algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Global climate change is a scientifically well-recognized phenomenon and appears to be accelerated due to greenhouse gas (GHG) emissions such as carbon dioxide or equivalents (CO 2 eq ). The harmful health and safety impacts of global climate change are projected to 'fall disproportionately on the poor and vulnerable'. Energy production remains a large factor in GHG emissions, contributing about ∼ 25 % of GHG emissions in 2010. With the compute and energy demands of many modern machine learning (ML) methods growing exponentially, ML systems have the potential to significantly contribute to carbon emissions. Recent work has demonstrated these potential impacts through case studies and suggested various mitigating strategies.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

©2020 Peter Henderson, Jieru Hu, Joshua Romoff, Emma Brunskill, Dan Jurafsky, Joelle Pineau.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We hypothesize that part of the reason that much research does not report energy and carbon metrics is due to the complexities of collecting them. Collecting carbon emission metrics requires understanding emissions from energy grids, recording power outputs from GPUs and CPUs, and navigating among different tools to accomplish these tasks. To reduce this overhead, we present experiment-impact-tracker 3 -a lightweight framework for consistent, easy, and more accurate reporting of energy, compute, and carbon impacts of ML systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Systematic and accurate measurements are needed to better estimate the broader energy and carbon footprints of ML-in both research and production settings. Accurate accounting of carbon and energy impacts aligns incentives with energy efficiency, raises awareness, and drives mitigation efforts, among other benefits. 1 Yet, most ML research papers do not regularly report energy or carbon emissions metrics. 2 In Section 4, we introduce the design and capabilities of our framework and the issues with accounting we aim to solve with this new framework. Section 5 expands on the challenges of using existing accounting methods and discusses our learnings from analyzing experiments with experiment-impact-tracker. For example, in an empirical case study on image classification algorithms, we demonstrate that floating point operations (FPOs), a common measure of efficiency, are often uncorrelated with energy consumption with energy metrics gathered by experiment-impact-tracker.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 6, we focus on recommendations for promoting energy-efficient research and mitigation strategies for carbon emissions. Using our framework, we present a Reinforcement Learning Energy Leaderboard in Section 6.1.1 to encourage development of energy efficient algorithms. We also present a case study in machine translation to show how regional energy grid differences can result in large variations in CO 2 eq emissions. Emissions can be reduced by up to 30x just by running experiments in locations powered by more renewable energy sources (Section 6.2).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

- incentivizing energy-efficient research through leaderboards (Section 6.1) - running experiments in carbon-friendly regions (Section 6.2) - reducing overheads for utilizing efficient algorithms and resources (Section 7.1) - considering energy-performance trade-offs before deploying energy hungry models (Section 7.2) - selecting efficient test environment especially in RL (Section 7.3) - ensuring reproducibility to reduce energy consumption from replication difficulties (Section 7.4) - consistently reporting energy and carbon metrics (Section 7.5) 1. See Section 4.1 for an extended discussion on the importance of accounting. 2. See Section 3 and Appendix B for more information.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Energy Accounting", "weight": 1.0} -->

Energy accounting is fairly straightforward. The energy consumption of a system can be measured in Joules (J) or Watt-hours (Wh), 6 representing the amount of energy needed to power the system. Life-cycle accounting might also consider the energy required to manufacture components of the system-for example, the production of GPUs or CPUs. However, we largely ignore life-cycle aspects of energy accounting due to the difficulties in attributing manufacturing impacts on a per-experiment basis. Measuring datacenter energy impacts also contain several layers, focusing on hardware-centric and softwarecentric analyses. Many parts contribute to the power consumption of any computational system. Dayarathna et al. survey energy consumption components of a data center and their relative consumption: cooling (50%), lighting (3%), power conversion (11%), network hardware (10%), and server/storage (26%).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Energy Accounting", "weight": 1.0} -->

The server and storage component can further be broken down into contributions from DRAM, CPUs, among other compute components. Accurate accounting for all of these components requires complex modeling and varies depending on workload. In particular, the efficiency of the hardware varies with utilization-often most efficient near maximum utilization-making utilization an important factor in optimization (particularly in large cloud compute systems) Barroso et al.. Since we aim to provide a framework at the per-experiment software level, we only account for aspects of energy consumption which expose interfaces for energy metrics (giving us real-time energy usage and compensating for such workload differences). For the purpose of our work, this is constrained to DRAM, CPUs, and GPUs. To account for all other components, we rely on a power usage effectiveness (PUE) factor. This factor rescales the available power metrics by an average projected overhead of other components. With more available software interfaces, more robust modeling can be performed as reviewed by Dayarathna et al.. 6. One Watt is a unit of power-equivalent to one Joule per second.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Carbon Accounting", "weight": 1.0} -->

Carbon accounting can be all-expansive, so we focus on a narrow definition provided by Stechemesser and Guenther: 'carbon accounting at the project scale can be defined as the measuring and non-monetary valuation of carbon and GHG emissions and offsetting from projects, and the monetary assessment of these emissions with offset credits to inform project-owners and investors but also to establish standardized methodologies.' Carbon and GHG emissions are typically measured in some form close to units CO 2 eq. This is the amount of carbon-and other GHG converted to carbon amounts-released into the atmosphere as a result of the project. Carbon offsetting is the amount of carbon emissions saved as a result of the project. For example, a company may purchase renewable energy in excess of the energy required for their project to offset for the carbon emissions they contributed. Since our goal is to inform and assess carbon emissions of machine learning systems, we ignore carbon offsetting. Typical carbon offsetting involves the use of Power Purchase Agreements (PPAs) or other similar agreements which may not reflect the current carbon make-up of the power draw (as they may account for future clean energy).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Carbon Accounting", "weight": 1.0} -->

7 Since carbon effects contribute to feedback loops, cutting emissions now will improve the likelihood of preventing further emissions. 8. We also do not consider carbon accounting in the financial sense, but do provide metrics on monetary impacts through the social cost of carbon (SC-CO2). The U.S. Environment Protection Agency uses this metric when developing administrative rules and regulations. According to the EPA, 'The SC-CO2 is a measure, in dollars, of the long-term damage done by a ton of carbon dioxide (CO2) emissions in a given year. This dollar figure also represents the value of damages avoided for a small emission reduction (i.e., the benefit of a CO2 reduction).' We rely on the per-country social cost of carbon developed by Ricke et al., which accounts for different risk profiles of country-level policies and GDP growth in their estimates of SC-CO2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Carbon Accounting", "weight": 1.0} -->

Carbon emissions from a project can also consider life-cycle emissions (for example, manufacturing of CPUs may emit carbon as part of the process). We do not consider these aspects of emissions. We instead, consider only carbon emissions from energy consumption. A given energy grid powering an experiment will have a carbon intensity: the grams of CO 2 eq emitted per kWh of energy used. This carbon intensity is determined based on the energy sources supplying the grid. Each energy source has its own carbon intensity accounted for through a full life-cycle analysis. For example, coal power has a median carbon intensity of 820 gCO 2 eq / kWh, while hydroelectricity has a mean carbon intensity of 24 gCO 2 eq / kWh. The life-cycle emissions of energy source take into account not just emissions from production, but from waste disposal as well. For example, nuclear energy waste disposal has some carbon emissions associated that would be taken into account in a life-cycle carbon intensity metric. Carbon emissions for a compute system can be estimated by understanding the carbon intensity of the local energy grid and the energy consumption of the system. Similar analyses have been done for bitcoin.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Carbon Accounting", "weight": 1.0} -->

These analyses, however, attempt to extrapolate impacts of bitcoin mining in general, while in this work we attempt to examine machine learning impacts on a per-experiment basis. 7. See discussion in Appendix C for further information. 8. See, e.g., feedback\_loops.pdf

<!-- chunk {"id": "body-0015", "role": "body", "section": "Current State of Reporting in Machine Learning Research", "weight": 1.0} -->

We briefly examine the current state of accounting in the machine learning literature and review commonly reported computational metrics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "· Compute", "weight": 1.0} -->

- -PFLOPs-hr, the floating point operations per second needed to run the experiment in one hour - -Floating Point Operations (FPOs) or Multiply-Additions (Madds), typically reported as the computations required to perform one forward pass through a neural network - -The number of parameters defined by a neural network (often reported together with FPOs) - -GPU/CPU utilization as a percentage - -GPU-hours or CPU-hours, the processor cycles utilized (or in the case of the GPU percentage utilized), times the runtime

<!-- chunk {"id": "body-0017", "role": "body", "section": "· Runtime", "weight": 1.0} -->

- -Inference time, the time it takes to run one forward pass through a neural network, - -Wall clock training time, the total time it takes to train a network. - -Hardware and time together (e.g., 8 v100 GPUs for 5 days) - -US-average carbon emissions Example 1 To get a rough estimate of the prevalence of these metrics, we randomly sampled 100 NeurIPS papers from the 2019 proceedings. In addition to the metrics above, we also investigate whether hardware information was reported (important for extrapolating energy and carbon information with partial information). Of these papers, we found 1 measured energy in some way, 45 measured runtime in some way, 46 provided the hardware used, 17 provided some measure of computational complexity (e.g., compute-time, FPOs, parameters), and 0 provided carbon metrics. See Appendix B for more details on methodology.

<!-- chunk {"id": "body-0018", "role": "body", "section": "· Runtime", "weight": 1.0} -->

Some of these metrics, when combined, can also be used to roughly estimate energy or carbon metrics. For example, the experiment time (h) can be multiplied by the thermal design power (TDP) of the GPUs used (W) 9. This results in a Watt-hour energy metric. This can then be multiplied by the carbon intensity of the local energy grid to assess the amount of CO 2 eq emitted. This method of estimation omits CPU usage and assumes a 100% GPU utilization. Alternatively, Amodei and Hernandez use a utilization factor of 33% for GPUs. Similarly, the PFLOPs-hr metric can by multiplied by TDP (Watts) and divided by the maximum computational throughput of the GPU (in PFLOPs). This once again provides a Watt-hour energy metric. This, however, makes assumptions based on maximum efficiency of a GPU and disregards variations in optimizations made by underlying frameworks (e.g., Tensorflow versus Pytorch; AMD versus NVIDIA drivers).

<!-- chunk {"id": "body-0019", "role": "body", "section": "· Runtime", "weight": 1.0} -->

It is worth noting that some metrics focus on the computational requirements of training (which require additional resources to compute gradients and backpropagate, in the case of neural networks) versus the computational requirements of inference. The former is often more energy and carbon intensive in machine learning research, while the later is more intensive in production systems (the cost of training is insignificant when compared to the lifetime costs of running inference millions of times per day, every day). We will remain largely agnostic to this differentiation until some discussions in Sections 6.2 and 7.2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "· Runtime", "weight": 1.0} -->

As we will demonstrate using our framework (see Section 5.2), the assumptions of these estimation methods lead to significant inaccuracies. However, aggregating all necessary accounting information is not straightforward or easy; it requires finding compatible tools, handling nuances on shared machines, among other challenges.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motivation", "weight": 1.0} -->

The goal of our experiment-impact-tracker framework is to provide an easy to deploy, reproducible, and quickly understood mechanism for all machine learning papers to report carbon impact summaries, along with additional appendices showing detailed energy, carbon, and compute metrics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motivation", "weight": 1.0} -->

Example 2 A carbon impact summary generated by our framework can be found at the end of this paper in the Carbon Impact Statement section. In brief, the experiments in our paper contributed 8.021 kg of CO 2 eq to the atmosphere and used 24.344 kWh of electricity, having a USA-specific social cost of carbon of $0.38 ($0.00, $0.95).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motivation", "weight": 1.0} -->

Such statements and informational reporting are important, among other reasons, awareness, aligning incentives, and enabling accurate cost-benefit analyses.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Motivation", "weight": 1.0} -->

Awareness: Informational labels and awareness campaigns have been shown to be effective drivers of eco-friendly behaviors (depending on the context). Without consistent and accurate accounting, many researchers will simply be unaware of the impacts their models might have and will not pursue mitigating strategies. Consistent reporting also may provide social incentives to reduce carbon impacts in research communities. 9. This is a rough estimate of the maximum operating capacity of a GPU.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Motivation", "weight": 1.0} -->

Aligning Incentives: While current reporting often focuses solely on performance metrics (accuracy in classification, perplexity in language modeling, average return in reinforcement learning, etc), standardized reporting of energy in addition to these metrics aligns incentives towards energy efficient models in research output. Those who accurately report carbon emissions may have more incentive to reduce their carbon footprint. This may also drive traffic to low-emission regions, spurring construction of more carbon-friendly data centers. 10 Cost-Benefit Analysis and Meta-Analysis: Cost-benefit analyses can be conducted with accurate energy metrics reporting, but are impossible without it. For example, the estimated generated revenue of a model can be weighed against the cost of electricity. In the case of models suggested by Rolnick et al., the carbon emissions saved by a model can be weighed against the emissions generated by the model. Consistent reporting also opens the possibility for performing meta-analyses on energy and carbon impacts. Larger extrapolations to field-wide impacts of research conferences can also be assessed with more frequent reporting.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Design Considerations", "weight": 1.0} -->

We consider five main principles when designing the framework for systematic reporting: usability, interpretability, extensibility, reproducibility, and fault tolerance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Design Considerations", "weight": 1.0} -->

Usability: Perceived ease-of-use can be an important factor in adoption of new technologies and methods. Since gathering key energy ( kWh ) and carbon (CO 2 eq ) metrics requires specific knowledge about-and aggregation of-different sources of information, there may be a barrier to the ease-of-use in the current status quo. As a result, a core design consideration in developing tools for these metrics is usability, or ease-of-use. We accomplish this by abstracting away and distilling required knowledge of information sources, keeping amount of required action from the user to a minimum.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Design Considerations", "weight": 1.0} -->

Interpretability: Along with ease-of-use, a key factor in adoption is perceived usefulness. Since we wish for the reporting of carbon and energy metrics to become widespread, we consider perceived usefulness through interpretability. We aim to make reporting tools within the framework useful through simple generation of graphs and web pages from metrics for easy interpretation. We also provide a mechanism to generate a carbon impact statement with the social cost of carbon. This dollar amount represents the projected damage from the experiment's carbon emissions and helps ground results in values that may be more interpretable. As seen in our own statement at the end of this work, we also provide the carbon impact and energy usage directly.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Design Considerations", "weight": 1.0} -->

Extensibility: We design the framework in a modular fashion to handle evolving driver support (see Section 5) and new metrics. To improve the accuracy and accessibility of the framework, the ML community can add new metrics, carbon intensity information, and other capabilities easily. For each metric, a central data router stores a description, the function which gathers metric data, and a list of compatibility checks (e.g., the metric can only be gathered on a Linux system). New metrics can be added to this router. 11 Similarly, new carbon region and electricity grid information can be added as needed to similar centralized locations. 12 10. See discussion in Section 6.2 on regional carbon emission differences. See discussion by LaRiviere et al. on how more accurate carbon accounting can result in reduced carbon emissions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Design Considerations", "weight": 1.0} -->

Fault tolerance: Mistakes in software are inevitable-as is discussed in Sidor and Schulman. We try to log all raw information so that accounting can be recreated and updated based on new information. We also log the version number of the tool itself, to ensure future comparisons do not mismatch information between versions that may have changed.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Design Considerations", "weight": 1.0} -->

Reproducibility: Running an algorithm on different sets of hardware has been shown to affect the reproducibility of algorithmic results. Our framework aides in automating reproducibility by logging additional metrics like hardware information, Python package versions, etc. These metrics can help future work assess statistically significant differences in model energy requirements by accounting for controlled and random variates.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Proposed Framework", "weight": 1.0} -->

The experiment-impact-tracker requires a simple code change to automatically gather available metrics and a script to generate online appendices for reporting the data.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Proposed Framework", "weight": 1.0} -->

- all python packages and version numbers - CPU and GPU hardware information - experiment start and end-times - the version of the experiment-impact-tracker framework used - the energy grid region the experiment is being run in (based on IP address) - the average carbon intensity in the energy grid region - CPU- and GPU-package power draw - per-process utilization of CPUs and GPUs - GPU performance states - the realtime CPU frequency (in Hz) - realtime carbon intensity (only supported in CA right now) - disk write speed The code change required for immediate logging of metrics can be seen in Listing 1. In the background, the framework launches a thread which polls system supported tools. For example, the thread polls psutil for measuring CPU utilization. All of these metrics are logged in parallel with the main machine learning process as described in Figure 1. A script 13 is provided to generate an HTML web page showing graphs and tables for all these metrics, meant to serve as an online appendix for research papers. 14 Results in the generated appendix can be aggregated across multiple experiments to show averages along with standard error as recommended in prior work.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Proposed Framework", "weight": 1.0} -->

1 from experiment_impact_tracker.compute_tracker import ImpactTracker 2 tracker = ImpactTracker 3 tracker.launch_impact_monitor Listing 1: Simple code addition required to log experiment details via our framework.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Tracking Energy Consumption", "weight": 1.0} -->

Different hardware vendors provide different tooling for tracking energy consumption. Our framework hides these complications from users. We currently use Intel's RAPL tool with the powercap interface or Intel's PowerGadget Tool 15 (depending on availability) to gather CPU/DRAM power draw and Nvidia's nvidia-smi 16 for GPU power draw. We use psutil for gathering per-process CPU utilization and nvidia-smi for per-process GPU utilization. We found that on a shared machine-as when running a job on Slurmusing Intel's RAPL would provide energy metrics for the entire machine (including other jobs running on the worker). If two experiments were launched with Slurm to the same worker, using measurements from RAPL without corrections would double count energy usage from the CPU.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Tracking Energy Consumption", "weight": 1.0} -->

We calculate total energy as: As a result, we assign energy credits on a per-process basis (though we log system-wide information as well). We track the parent process, and any children spawned. Power credits are provided based on relative usage of system resources. If a process uses 25% of the CPU (relative to the entire system's usage), we will credit the process with 25% of the CPU-based power draw. This ensures that any non-experiment-related background processes- software updates, weekly jobs, or multiple experiments on the same machine-will not be taken into account during training. where p resource are the percentages of each system resource used by the attributable processes relative to the total in-use resources and e resource is the energy usage of that resource. This is the per-process equivalent of the method which Strubell et al. use. 14. Appendices generated by our framework for Figure 7 and Figure 3 are available: mitigating\_energy\_and\_carbon\_footprints\_in\_machine\_learning/. Experiments in Figure 5 are available at energy\_leaderboard/index.html.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Tracking Energy Consumption", "weight": 1.0} -->

We assume the same constant power usage effectiveness (PUE) as Strubell et al. to be the framework's default PUE. This value compensates for excess energy from cooling or heating the data-center. Users can customize the PUE value when using the framework if needed.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Carbon Accounting", "weight": 1.0} -->

For calculating carbon emissions, we use the power estimate from the previous section in kilowatt-hours (kWh) and multiply it by the carbon intensity of the local energy grid (g CO 2 eq / kWh). To gather carbon intensity metrics for energy grids, we build on the open-source portions of and define regions based on map-based geometries, using the smallest bounding region for a given location as the carbon intensity estimate of choice. For example, for an experiment run in San Francisco, if the average carbon intensity is available for both the USA and California, the latter will be used. We estimate the region the experiment is conducted in based on the machine's IP address. Carbon intensities are gathered from the average fallback values provided in the code where available and supplemented with additional metrics from various governmental or corporate reports. We note that electricitymap.org estimates are based on a closed-source system and uses the methodology described by Tranberg et al.. All estimates from electricitymap.org are of the regional supply, rather than production (accounting for imports from other regions).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Carbon Accounting", "weight": 1.0} -->

Since provides realtime intensities including imports for free, for experiments run in California, we also provide realtime carbon intensity information. We do this by polling for the current intensity of the California energy grid every five minutes. This helps gather even more accurate estimates of carbon emissions to account for daily shifts in supply. For example, experiments run in California during the day time use roughly 2 3 of night-time experiments. This is because much of California's renewable energy comes from solar plants. Figure 2 is an automatically generated graph showing this phenomenon from an experiment using our framework. We hope that as users find more accurate realtime or average measurements of regional supply-based carbon intensities, they will add them to the tool for even more accurate measurements in the future.

<!-- chunk {"id": "body-0040", "role": "body", "section": "FPOs Can Be Misleading", "weight": 1.0} -->

Floating Point Operations (FPOs) are the de facto standard for reporting 'efficiency' of a deep learning model, and intuitively they should be correlated with energy efficiency-after all, fewer operations should result in faster and more energy efficient processing. However, this is not always the case.

<!-- chunk {"id": "body-0041", "role": "body", "section": "FPOs Can Be Misleading", "weight": 1.0} -->

Previously, Jeon and Kim demonstrated mechanisms for constructing networks with larger FPOs, but lower inference time-discussing the 'Trap of FLOPs'. Similarly, Qin et al. show how Depthwise 3x3 Convolutions comprised just 3.06% of an example network's Multiply-Add operations, while utilizing 82.86% of the total training time in the FPO-efficient MobileNet architecture Howard et al.. Underlying optimizations at the firmware, deep learning framework, memory, or even hardware level can change energy efficiency and run-time. This discrepancy has led to Github Issues where users expect efficiency gains from FPO-efficient operations, but do not observe them. 17 This has also been observed by Chen and Gilbert and Chen et al..

<!-- chunk {"id": "body-0042", "role": "body", "section": "FPOs Can Be Misleading", "weight": 1.0} -->

Example 3 To investigate this empirically, we repeatedly run inference through pre-trained image classification models and measure FPOs, parameters, energy usage, and experiment length using the experiment-impact-tracker framework. As described in Figure 3, we find little correlation between FPOs and energy usage or experiment runtime when comparing across different neural network architectures. However, within an architecture-relying on the same operation types, but with different numbers of operations-FPOs are almost perfectly correlated with energy and runtime efficiency. Thus, while FPOs are useful for measuring relative ordering within architecture classes, they are not adequate on their own to measure energy or even runtime efficiency.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Estimates with Partial Information Can Be Inaccurate", "weight": 1.0} -->

The current state of accounting for energy and carbon varies across fields and papers (see Section 3). Few works, if any, report all of the metrics that our framework collects. However, it is possible to extrapolate energy and carbon impacts from some subsets of these metrics. This can give a very rough approximation of the energy used by an experiment in kWh (see Section 3 for background).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Estimates with Partial Information Can Be Inaccurate", "weight": 1.0} -->

Example 4 We demonstrate how several such estimation methods compare against the more fine-grained accounting methods we describe in Section 4. 18 As seen in Figure 4, we find significant differences from when we track all data (as through the experiment-impact-tracker framework) to when we use partial data to extrapolate energy and carbon emissions. Only using GPUs and the experiment time ignores memory or CPU effects; only using the average case US region ignores regional differences. More details for this experiment can be found in Appendix E. 17. See for example: and 18. We also provide a script to do the rough calculation of energy and carbon footprints based on GPU type, IP address (which is used to retrieve the location of the machine and that region's carbon Figure 3: We run 50,000 rounds of inference on a single sampled image through pre-trained image classification models and record kWh, experiment time, FPOs, and number of parameters (repeating 4 times on different random seeds). References for models, code, and expanded experiment details can be found in Appendix D. We run a similar analysis to Canziani et al. and find (left) that FPOs are not strongly correlated with energy consumption (R 2 = 0.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Estimates with Partial Information Can Be Inaccurate", "weight": 1.0} -->

083, Pearson 0. 289) nor with time (R 2 = 0. 005, Pearson -0. 074) when measured across different architectures. However, within an architecture (right) correlations are much stronger. Only considering different versions of VGG, FPOs are strongly correlated with energy (R 2 =. 999, Pearson 1. 0) and time (R 2 =. 998, Pearson. 999). Comparing parameters against energy yields similar results (see Appendix D for these results and plots against experiment runtime).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Estimates with Partial Information Can Be Inaccurate", "weight": 1.0} -->

We also note that the possible estimation differences in Figure 4 do not include possible errors from counting multiple processes at once, as described in Section 4.3.1. Clearly, without detailed accounting, it is easy to severely over- or underestimate carbon or energy emissions by extrapolating from partial information.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Encouraging Efficiency and Mitigating Carbon Impacts: Immediate Mitigation Strategies", "weight": 1.0} -->

With experiment-impact-tracker, we hope to ease the burden of standardized reporting. We have demonstrated differences in more detailed estimation strategies from the current status quo. In this Section, we examine how accurate reporting can be used to drive immediate mitigating strategies for energy consumption and carbon emissions. intensity), experiment length, and utilization factor.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Energy Efficiency Leaderboards", "weight": 1.0} -->

A body of recent work has emphasized making more computationally efficient models, yet another line of work has focused on the opposite: building larger models with more parameters to tackle more complex tasks. We suggest leaderboards which utilize carbon emissions and energy metrics to promote an informed balance of performance and efficiency. DawnBench, MLPerf, and HULK have done this in terms of runtime and cost. Ethayarajh and Jurafsky have recently critiqued leaderboards for only optimizing for one particular metric. By optimizing for energy and carbon emissions directly in addition to target performance metrics, baseline implementations can converge to more efficient climate-friendly settings. This can also help spread information about the most energy and climate-friendly combinations of hardware, software, and algorithms such that new work can be built on top of these systems instead of more energy-hungry configurations. 19

<!-- chunk {"id": "body-0049", "role": "body", "section": "Deep RL Energy Leaderboard", "weight": 1.0} -->

To demonstrate how energy leaderboards can be used to disseminate information on energy efficiency, we create a Deep RL Energy Leaderboard. 20 The website is generated using the same tool for creating HTML appendices described in Section 4. All information (except for algorithm performance on tasks) comes from the experiment-impact-tracker framework. We populate the leaderboard for two common RL benchmarking environments, PongNoFrameskipv4 and BreakNoFrameskip-v4, and four baseline algorithms, PPO, A2C, A2C with V-Traces, and DQN. The experimental details and results can also be found in Figure 5. We find that no algorithm is the energy efficiency winner across both environments, though the PPO implementation provided by Hill et al. attains balance between efficiency and performance when using default settings across algorithms.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Deep RL Energy Leaderboard", "weight": 1.0} -->

Example 5 To see how such a leaderboard might help save energy, consider a Deep RL class of 235 students. 21 For a homework assignment, each student must run an algorithm 5 times on Pong. The class would save 888 kWh of energy by using PPO versus DQN, while achieving similar performance. 22 This is roughly the same amount needed to power a US home for one month. 23 19. Something to note is that we do not compare carbon efficiency directly-instead focusing on energy specifically. Since running at different times of day and in different regions can affect carbon impacts, these may not have anything to do with the algorithm hardware-software stack and increase the number of confounds when comparing algorithms. While hardware is also immutable to some extent, there may still be information to be gained by finding combinations of efficient low-level optimizations for specific hardware. Hardware can also be held relatively constant by using the same machine for all experimental runs. If comparisons using carbon units are desired, a fixed carbon intensity factor should likely be chosen for approximate comparisons in a given region (rather than using live carbon intensity metrics). See, also, Appendix H. 20.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Deep RL Energy Leaderboard", "weight": 1.0} -->

leaderboard/index.html 21. See for example, Stanford's CS 234.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Deep RL Energy Leaderboard", "weight": 1.0} -->

We, thus, encourage the community to submit more data to the leaderboard to find even more energy efficient algorithms and configurations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Running In Carbon-Friendly Regions", "weight": 1.0} -->

We noted in Section 4 that it is important to assess which energy grid experiments are run on due to the large differences in carbon emissions between energy grids. Figure 6 shows CO 2 eq intensities for an assortment of locations, cloud-provider regions, and energy production methods. We note that an immediate drop in carbon emission can be made by moving all training jobs to carbon-efficient energy grids. In particular, Quebec is the cleanest available cloud region to our knowledge. Running a job in Quebec would result in carbon emission 30x lower than running a job in Estonia.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Running In Carbon-Friendly Regions", "weight": 1.0} -->

Example 6 To demonstrate this in practice, we run inference on two machine translation models 1000 times and measure energy usage. We extrapolate the amount of emissions and the difference between the two algorithms if run in different energy grids, seen in Figure 7. The absolute difference in emissions between the two models is fairly small (though significant) if run in Quebec (.09 g CO 2 eq ), yet the gap increases as one runs the jobs in less carbon-friendly regions (at 3.04 g CO 2 eq in Estonia).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Running In Carbon-Friendly Regions", "weight": 1.0} -->

We provide a script with our framework to show all cloud provider region with emission statistics to make this decision-making process easier. 24 We note that Lacoste et al. provide a website using partial information estimation to extrapolate carbon emissions based on cloud provider region, GPU type, and experiment length in hours. Their tool may also be used for estimating carbon emissions in cloud-based experiments ahead of time. We've also provided a non-exhaustive list of low emissions energy grids that contain cloud regions in Table 1.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Running In Carbon-Friendly Regions", "weight": 1.0} -->

For companies that train and deploy large models often, shifting these resources is especially important. ML training is not usually latency bound: companies can run training in cloud regions geographically far away since training models usually does not require round trip communication requirements. Contrary to some opinions, 25 there is not a necessary need to eliminate computation-heavy models entirely, as shifting training resources to low carbon regions will immediately reduce carbon emissions with little impact to production systems. For companies seeking to hit climate change policy targets, promotion of carbon neutral regions and shifting of all machine learning systems to those regions would accelerate reaching targets significantly and reduce the amount of offset purchasing required to meet goals (thus saving resources). 26 It is worth noting that some companies like Google already purchase offsets, so it may be unclear why shifting resources is necessary. We provide an extended discussion on this in Appendix C. As a matter of total emissions reductions, running compute in carbon-friendly regions prevents emissions now, while offsets may not come into effect for several years. Moreover, continuing offset purchasing at current levels, while shifting resources to green regions would result in a net-negative carbon footprint. 22. These rankings may change with different code-bases and hyperparameters.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Running In Carbon-Friendly Regions", "weight": 1.0} -->

24. See: get-region-emissions-info script and lookup-cloud-region-info script. 26. See, for example, Amazon's goal: Table 1: A non-exhaustive list of cloud regions in low carbon intensity energy grids (< 150 gCO 2 eq / kWh). All estimates pulled as yearly averages from https: //www.electricitymap.org/map, except for Quebec which utilizes methodology from and Oregon which uses data from electricity/state/oregon/.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Running In Carbon-Friendly Regions", "weight": 1.0} -->

| Power Grid | Cloud Regions | Carbon Intensity (g CO 2 eq / kWh) |

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion: Systemic Changes", "weight": 1.5} -->

We demonstrated several use cases for accounting which can drive immediate mitigation strategies. However, the question remains: how can we encourage systemic changes which lead to energy and carbon efficiency in ML systems?

<!-- chunk {"id": "body-0060", "role": "body", "section": "Green Defaults for Common Platforms and Tools", "weight": 1.0} -->

Energy leaderboards help provide information on energy efficient configurations for the whole stack. However, to truly spread energy efficient configurations, underlying frameworks should by default use the most energy-efficient settings possible. This has been shown to be an effective way to drive pro-environmental behavior. For example, Nvidia apex provides easy mixed-precision computing as an add-on which yields efficiency gains. 27 However, it requires knowing this and using it. Merity also discusses the current difficulties in using highly efficient components. Making such resources supported as defaults in frequently used frameworks, like PyTorch, would immediately improve the efficiency of all downstream projects. We encourage maintainers of large projects to prioritize and support such changes.

<!-- chunk {"id": "body-0061", "role": "body", "section": "How Much Is Your Performance Gain Worth? Balancing Gains With Cost", "weight": 1.0} -->

While training jobs can easily be shifted to run in clean regions, there are often restrictions for inference-time use of machine learning models which prevent such a move. Many companies are deploying large machine learning models powered by GPUs for everyday services. 28 Example 7 Production machine translation services, can process 100B words per day: roughly 4.2 million times our experiment in Figure 7. If all translation traffic were in Estonia, 12,768 kgCO 2 eq (the carbon sequestered by 16.7 acres of forest in one year) would be saved per day by using the more efficient model, yet if all traffic were in Québec, 378 kgCO 2 eq would be saved (the carbon sequestered.5 acres of forest in one year). Considering the amounts of required compute, small differences in efficiency can scale to large emissions and energy impacts.

<!-- chunk {"id": "body-0062", "role": "body", "section": "How Much Is Your Performance Gain Worth? Balancing Gains With Cost", "weight": 1.0} -->

These services are latency-bound at inference time and thus cannot mitigate carbon emissions by shifting to different regions. Instead, deploying energy-efficient models not only reduces carbon emissions but also benefits the companies by bringing the energy costs down. We encourage companies to consider weighing energy costs (both social and monetary) with the performance gains of a new model before deploying it. In the case of our translation experiment in Figure 7, the pre-trained convolutional model we use is significantly more energy hungry across runs than the transformer model we use. When deploying a new energyhungry translation model, we ask companies to consider: is the BLEU score improvement really worth the energy cost of deploying it? Are there ways to route to different models to balance this trade-off? For example, suppose an energy-hungry model only improves performance in some subset of the data. Routing to this model only in that subset would maximize performance while minimizing energy footprint. 29.

<!-- chunk {"id": "body-0063", "role": "body", "section": "How Much Is Your Performance Gain Worth? Balancing Gains With Cost", "weight": 1.0} -->

We note that considering such trade-offs is of increased importance for models aiming to reduce carbon emissions as described by Rolnick et al.. Deploying a large deep learning model, say, improving the energy efficiency of a building, is not worth it if the energy costs of the model outweigh the gains. We also leave an open question to economists to help assess the welfare benefits of gains on a particular machine learning metric (e.g., how much is BLEU score worth in a translation service). This would allow the social welfare of the metric to be balanced against the social cost of carbon for deployment decisions. 28. See for example, search which now uses transformer networks at both Microsoft and Google. and 29. Efficient routing of traffic to regions has been considered before by Nguyen et al. and Berral et al.. It may be worth considering efficient routing of traffic to particular models as well.

<!-- chunk {"id": "body-0064", "role": "body", "section": "How Much Is Your Performance Gain Worth? Balancing Gains With Cost", "weight": 1.0} -->

Similarly, it is important to consider other types of cost-benefit analyses. Perhaps the carbon impacts of a long (energy-intensive) training time for a large model is worth it if it reduces the lifetime carbon footprint in production (for example, if the model doesn't require expensive fine-tuning procedures in the future). Understanding the tradeoff between the lifetime deployment costs and training costs is important before moving on to extended training runs. As such, we also encourage reporting of both estimated training and deployment energy costs so future adopters have a more comprehensive picture when deciding which model to use.

<!-- chunk {"id": "body-0065", "role": "body", "section": "How Much Is Your Performance Gain Worth? Balancing Gains With Cost", "weight": 1.0} -->

Central to all of these cost-benefit analyses are accurate accounting. Our tool provides one step in consistent and accurate accounting for such purposes.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Efficient Testing Environments", "weight": 1.0} -->

In Section 7.1 we discuss the adoption of green default configurations and Section 7.2 discusses cost-benefit analyses for deployments. Another consideration particular to researchespecially RL-is the selection of the most efficient testing environments which assess the mechanism under test. For example, if an RL algorithm solves a particularly complex task in an interesting way, like solving a maze environment, is there a way to demonstrate the same phenomenon in a more efficient environment? Several works have developed efficient versions of RL environments which reduce run-times significantly. In particular, Dalton et al. improve the efficiency of Atari experiments by keeping resources on the GPU (and thus avoiding energy and time overheads from moving memory back and forth). ChevalierBoisvert et al. develop a lightweight Grid World environment with efficient runtimes for low-overhead experiments. An important cost-benefit question for researchers is whether the same point can be proven in a more efficient setting.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Reproducibility", "weight": 1.0} -->

A key aspect to our work is helping to promote reproducibility by aiding in consistent reporting of experimental details. We encourage all researchers to release code and models (when it is socially and ethically responsible to do so), to prevent further carbon emissions. Replicating results is an important, if not required, part of research. If replication resources are not available, then more energy and emissions must be spent to replicate results-in the case of extremely large models, the social cost of carbon may be equivalently large. Thus, we ask researchers to also consider energy and environmental impacts from replication efforts, when weighing model and code release. We note that there may very well be cases where safety makes this trade-off lean in the direction of withholding resources, but this is likely rare in most current research. For production machine learning systems, we encourage developers to release models and codebases internally within a company. This may encourage re-use rather than spending energy resources developing similar products.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Standardized Reporting", "weight": 1.0} -->

We suggest that all papers include standardized reporting of energy and carbon emissions. We also suggest adding a Carbon Impact Statement at the end of papers (just like ours below) which estimates the carbon emissions of the paper. This can be reported in a dollar amount via the country-specific social cost of carbon. We provide a script 30 to parse logs from the experiment-impact-tracker framework and generate such a statement automatically. We suggest this to spread awareness and bring such considerations to the forefront. We encourage this statement to include all emissions from experimentation to build a more realistic picture of total resources spent.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Standardized Reporting", "weight": 1.0} -->

We also emphasize that research, even when compute intensive, is immensely important for progress. It is unknown what sequence of papers may inspire a breakthrough which would reduce emissions by more than any suggestion here. While emissions should be minimized when possible, we suggest that impact statements be only used for awareness. This is especially true since access to clean energy grids or hardware may be limited for some in the community.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Standardized Reporting", "weight": 1.0} -->

We also suggest that, when developing features which visualize compute intensity for cloud or internal workloads, developers consider providing built-in tools to visualize energy usage and carbon emissions. For example, the Colab Research Environment shows RAM and Disk capacity, 31 but could also show and provide access to these other metrics more easily. Providing similar informational labels within internal tooling could mitigate some energy and carbon impacts within companies.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Badging", "weight": 1.0} -->

Informational labeling has had a long history of being used in public policy. In the USA, the 'Energy Star' label has been used to guide customers to eco-friendly products. More recently, 'badges' rewarded by the Psychological Science journal were shown to be effective, with a jump from 3% of articles reporting open data to 39% one year later. ACM has introduced similar reproducibility badges. 32 With consistent reporting of carbon and energy metrics, climate friendly research badges can be introduced by conferences to recognize any paper that demonstrates a significant effort to mitigate its impacts. For example, a compute intensive paper, when showing evidence of explicitly running resources in a clean region can be rewarded with such a badge. Another example badge can be awarded to papers that create energy-friendly algorithms with similar performance as the state-of-the-art 33. The goal of these badges is to draw further attention to efficient versions of state-of-the-art systems and to encourage mitigation efforts while, again, not punishing compute-intensive experiments.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Badging", "weight": 1.0} -->

Of course this may not apply to conferences such as SysML which often focus on making models more efficient, but rather as a motivational tool for other venues where efficiency may not be in focus.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Limitations and Opportunities for Extensions", "weight": 1.5} -->

The experiment-impact-tracker framework abstracts away many of the previously mentioned difficulties in estimating carbon and energy impacts: it handles routing to appropriate tools for collecting information, aggregates information across tools to handle carbon calculations, finds carbon intensity information automatically, and corrects for multiple processes on one machine. Yet, a few other challenges may be hidden by using the framework which remain difficult to circumvent. 33. See, for example, Clark et al. which creates a more efficient version of text encoder pre-training.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Limitations and Opportunities for Extensions", "weight": 1.5} -->

As Khan et al. discuss, and we encounter ourselves, poor driver support makes tracking energy difficult. Not every chipset supports RAPL, nor does every Linux kernel. Intel also does not provide first party supported python libraries for access to measurements. nvidia-smi per-process measurements in docker containers are not supported. 34 A body of work has also looked at improving estimates of energy usage from RAPL by fitting a regression model to real energy usage patterns. The Slurm workload manager provides an energy accounting plugin, 35 but requires administrator access to add. For those without access to Slurm, Intel's RAPL supports access to measurements through three mechanisms, but only one of these (the powercap interface only available on some systems) does not require root access (see more discussion by Khan et al. ). To promote widespread reporting, we avoid any tool which requires administrative access or would not be accessible on most Linux systems. Providing better supported tools for user-level access to power metrics would make it possible to more robustly measure energy usage. Aggregating metrics and handling the intricacies of these downstream tools requires time and knowledge.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Limitations and Opportunities for Extensions", "weight": 1.5} -->

We try to abstract as much of these challenges away in the experiment-impact-tracker, though some driver-related issues require driver developer support. However, these issues make it difficult to support every on-premises or cloud machine. As such, we currently only support instances which have Intel RAPL or PowerGadget capabilities for Mac OS and Linux.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Limitations and Opportunities for Extensions", "weight": 1.5} -->

We also note that carbon intensities for machines in cloud data centers may not reflect the regional carbon intensities. Some providers buy clean energy directly for some data centers, changing the realtime energy mix for that particular data center. We were unable to find any information regarding realtime energy mixes in such cases and thus could not account for these scenarios. If providers exposed realtime APIs for such information this would help in generating more accurate estimates. Moreover, customized hardware in cloud provider regions does not always provide energy accounting mechanisms or interfaces. If cloud providers supported libraries for custom hardware, this could be used for more detailed accounting in a wider range of cloud-based compute scenarios.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Limitations and Opportunities for Extensions", "weight": 1.5} -->

We further discuss other sources of error and issues arising from these difficulties in Appendix G.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Concluding Remarks and Recommendations", "weight": 1.0} -->

We have shown how the experiment-impact-tracker and associated tools can help ease the burden of consistent accounting and reporting of energy, compute, and carbon metrics; we encourage contribution to help expand the framework. We hope the Deep RL Energy Leaderboard helps spread information on energy efficient algorithms and encourages research in efficiency. While we focus on compute impacts of machine learning production and research, a plethora of other work considers costs of transportation for conferences and compute hardware manufacturing. We encourage researchers and companies to consider these other sources of carbon impacts as well. Finally, we recap several points that we have highlighted in mitigating emissions and supporting consistent accountability.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Concluding Remarks and Recommendations", "weight": 1.0} -->

What can machine learning researchers do?

<!-- chunk {"id": "body-0080", "role": "body", "section": "Concluding Remarks and Recommendations", "weight": 1.0} -->

- Run cloud jobs in low carbon regions only (see Section 6.2). - Report metrics as we do here, make energy-efficient configurations more accessible by reporting these results (see Section 7.5). - Work on energy-efficient systems, create energy leaderboards (see Section 6). - Release code and models whenever safe to do so (see Section 7.4). - Integrate energy efficient configurations as defaults in baseline implementations (see Section 7.1). - Encourage climate-friendly initiatives at conferences (see Sections 7.6 and 7.5).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Concluding Remarks and Recommendations", "weight": 1.0} -->

What can industry machine learning developers and framework maintainers do?

<!-- chunk {"id": "body-0082", "role": "body", "section": "Concluding Remarks and Recommendations", "weight": 1.0} -->

- Move training jobs to low carbon regions immediately. Make default launch configurations and documentation point to low carbon regions (see Section 6.2). - Provide more robust tooling for energy tracking and carbon intensities (see Section 7.7). - Integrate energy efficient operations as default in frameworks (see Section 7.1). - Release code and models (even just internally in the case of production systems) whenever safe to do so (see Section 7.4). - Consider energy-based costs versus benefits of deploying new models (see Section 7.2). - Report model-related energy metrics (see Section 7.5).

<!-- chunk {"id": "body-0083", "role": "body", "section": "Concluding Remarks and Recommendations", "weight": 1.0} -->

We hope that regardless of which tool is used to account for carbon and energy emissions, the insights we provide here will help promote responsible machine learning research and practices.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Carbon Impact Statement", "weight": 1.0} -->

This work contributed 8.021 kg of CO 2 eq to the atmosphere and used 24.344 kWh of electricity, having a USA-specific social cost of carbon of $0.38 ($0.00, $0.95). Carbon accounting information located: measuring\_and\_mitigating\_energy\_and\_carbon\_footprints\_in\_machine\_learning/ and leaderboard/index.html. The social cost of carbon uses models from Ricke et al.. This statement and carbon emissions information was generated using experiment-impacttracker described in this paper.
