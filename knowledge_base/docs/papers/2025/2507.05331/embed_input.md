<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation

Topics include Imitation learning, Robotics, Robustness, Diffusion models, Foundation models, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robot manipulation has seen tremendous progress in recent years, with imitation learning policies enabling successful performance of dexterous and hard-to-model tasks. Concurrently, scaling data and model size has led to the development of capable language and vision foundation models, motivating large-scale efforts to create general-purpose robot foundation models. While these models have garnered significant enthusiasm and investment, meaningful evaluation of real-world performance remains a challenge, limiting both the pace of development and inhibiting a nuanced understanding of current capabilities. In this paper, we rigorously evaluate multitask robot manipulation policies, referred to as Large Behavior Models (LBMs), by extending the Diffusion Policy paradigm across a corpus of simulated and real-world robot data. We propose and validate an evaluation pipeline to rigorously analyze the capabilities of these models with statistical confidence. We compare against single-task baselines through blind, randomized trials in a controlled setting, using both simulation and real-world experiments. We find that multi-task pretraining makes the policies more successful and robust, and enables teaching complex new tasks more quickly, using a fraction of the data when compared to single-task baselines. Moreover, performance predictably increases as pretraining scale and diversity grows.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Project

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Achieving flexible, generalist robots is a central ambition of robotics research. While modern robots are physically capable of performing a wide array of tasks in myriad settings, reliable autonomy has traditionally been limited to simple tasks or highly structured environments. Recently, visuomotor learning-based methods---trained to condition on robot sensor observations and produce low-level actions---have emerged as promising solutions to bridge this gap between hardware capabilities and autonomous performance. Behavior cloning, the most commonly used approach in this regime, eschews task-specific robot programming in favor of task-specific demonstrations, typically collected via teleoperation. Methods based on behavior cloning can produce complex, reactive, and contact-rich behaviors from hundreds to thousands of demonstrations, are well suited to handle traditionally challenging task attributes such as object deformability, transparency, reflectivity, and bimanual coordination, and offer the promise of producing general-purpose manipulation systems capable of performing arbitrary tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these strengths, single-task behavior-cloned policies remain brittle, exhibiting limited generalization to task variations or environments outside their training distributions. To overcome this brittleness, the field is increasingly adopting Large Behavior Models (LBMs) --visuomotor foundation models trained on large-scale multitask datasets containing action-level demonstrations. Inspired by the success of large-scale generalist models in Computer Vision and Natural Language Processing, these models seek to improve reliability through broad training data support and more robust learned visual and sensory representations. Despite the surge in LBM research and development, significant uncertainty remains regarding the extent to which observed successes primarily stem from multitask pretraining.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To rigorously study the impact of multitask pretraining, we train multiple LBMs on approximately 1,700 hours of robot demonstrations comprised of over 500 internally collected high-diversity tasks as well as publicly available robot data. We comprehensively evaluate these models both in simulation and through 1,800 rigorously controlled real-world trials, including complex multi-step tasks that require tool use and precise manipulation. We design and employ an experimental protocol that incorporates blind A/B testing in the real world, large trial sizes with robust statistical analysis, qualitative and quantitative performance metrics, and carefully controlled initial conditions to ensure our conclusions hold with statistical significance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through these experiments, we find that: LBM pretraining reduces the amount of task-specific data required, enabling finetuned specialist models to match single-task model performance with fewer demonstrations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the same amount of task-specific data, finetuned specialists derived from pretrained LBMs outperform single-task models when aggregating over tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pretrained LBMs demonstrate increased robustness in scenarios diverging from their training conditions, amplifying the benefits described in points 1 and 2 in out-of-distribution evaluation settings.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Robot Learning at Scale", "weight": 1.0} -->

Robot learning is undergoing a paradigm shift towards creating generalist manipulation policies, inspired by the scaling hypothesis successfully applied in Natural Language Processing and Computer Vision. This shift is driven by the creation of large-scale and diverse datasets as well as high-capacity models, particularly transformer-based Vision-Language-Action (VLA) models, which have become central, integrating perception, language, and action within a unified framework trained largely via imitation learning. A key driver of VLA performance is transferring knowledge from large pretrained foundation models bringing semantic understanding, improved reasoning, and strong visual representations, which when finetuned on robotics datasets, enable capabilities like zero-shot task execution. The choice of action representation---whether discretized into tokens, directly regressed as continuous commands, or generated through diffusion models ---affects the policy's ability to produce precise, multimodal, and real-time behaviors. Despite progress in training generalist policies, challenges such as catastrophic forgetting, data heterogeneity, scarcity of high-quality data, multimodal fusion, handling dexterity, and maintaining real-time inference speed remain open research problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Robot Learning at Scale", "weight": 1.0} -->

This work focuses on rigorously evaluating the effects of multi-task pretraining (as opposed to, for example, architectural novelty), and studies a fixed policy architecture (described in Section 4.2.2) throughout.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Datasets for Robot Learning", "weight": 1.0} -->

Training generalist robot policies requires large-scale, diverse datasets, yet acquiring this data poses significant challenges. Unlike large-scale language and vision datasets, which are generally derived from internet sources, collecting robotics data in the real world is inherently slow and expensive. Robot data is most commonly collected via teleoperation, wherein human operators remotely control robots, yielding high-fidelity, embodiment-specific data. Large datasets such as RT-1, Bridge, RH20T, DROID, and AgiBot, among others, have been collected using this approach, often over the course of months or years with multiple robots. Pooled datasets like Open X-Embodiment aggregate teleoperation and other types of robot data from numerous labs (over 1 million trajectories and 22 embodiments) with the hope of training policies that benefit from transfer across robot embodiments. Simulation provides one promising alternative for cost-effectively generating robot manipulation data at scale; however, the differences between simulators and the real world present challenges. One method of overcoming these differences is to simultaneously train ("co-train") on data from both domains.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Datasets for Robot Learning", "weight": 1.0} -->

We use sim and real co-training in this work in order to more effectively evaluate LBMs that were trained primarily on real-world data in simulation. Another approach to quickly and cost-effectively collect data is to circumvent the need for robots entirely through the use of specialized devices manually controlled by people. In this work, we train LBMs on a mixture of data (described in Section 4.4) sourced from openly available datasets as well as from our internal data collection efforts in the real world (using both teleoperated robots and specialized devices ) and in simulation with the goal of better understanding the value of training on these large-scale, multi-task datasets.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Evaluating Robotic Manipulation Policies", "weight": 1.0} -->

Measuring the performance of LBMs, either for research or real-world deployment purposes, requires reproducible, reliable, and scalable evaluation methods and frameworks. Absence of standardized hardware makes consistent benchmarking a challenge. As a result, most benchmarks are simulation-based with notable examples including RLBench, ManiSkill, Meta-World, Robosuite, BEHAVIOR, and RoboTHOR. Evaluation within these benchmarks typically relies on quantitative metrics such as success rate, task completion percentage, and completion time, and emphasizes generalization (for example, to unseen objects, tasks, or scenes) or sample efficiency. While prior work in navigation highlights simulation-to-reality gaps caused by dynamics and visual discrepancies, evaluation of manipulation policies poses additional challenges due to tighter robot and environment coupling and the sensitivity of task outcomes to subtle variations. SIMPLER, a recent simulation framework, mitigates control and visual discrepancies between real and simulated environments through the use of system identification and various image editing and matching techniques. Alternative real-world evaluation approaches focus on establishing standardized object sets, tasks, datasets, and evaluation protocols, remote access to shared robots, or improving evaluation efficiency.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Evaluating Robotic Manipulation Policies", "weight": 1.0} -->

Despite progress, challenges remain in evaluating generalist robotic manipulation policies across many diverse tasks, reliably benchmarking complex long-horizon interactions, and assessing robustness and safety critical aspects in dynamic environments.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Results", "weight": 1.0} -->

We aim to achieve a nuanced understanding of LBM performance under a number of real-world conditions. Our main hypotheses are that due to pretraining, 1) new tasks can be learned with less data; 2) policies achieve better performance; and 3) policies are more robust under distribution shift. For each individual task, we compare against a single-task policy trained from scratch. We use simulation and real-world (hardware) experiments to measure LBM performance on tasks for which demonstrations were seen during pretraining ("seen" in the following) as well as on novel tasks that were not used for pretraining ("unseen" in the following). We evaluate the policies under two conditions, nominal and distribution shift; we systematically create distribution shifts as described in Sec. 4.5. Task complexity varies from simple pick-and-place manipulation to long-horizon tasks requiring a high degree of dexterity, such as coring an apple, setting a breakfast tray, or installing a bike rotor. Each real-world task was evaluated with 50 rollouts per task per policy per condition.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Results", "weight": 1.0} -->

Simulation tasks were run 200 times per task per policy per condition; due to missing data, a few tasks were analyzed with fewer than 200 rollouts, see Section 8.4 for details.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Results", "weight": 1.0} -->

Section 4.1 describes our evaluation protocol and our process for creating controlled and repeatable distribution shifts. Our metrics for measuring performance are success rate (SR) and task completion (TC). Success rate, while a useful and important signal that is standard across robot learning publications, does not tell the full story of policy performance. There is a notable difference between a policy that almost, but not quite, succeeds and one that does nothing. To capture and quantify this nuance, we create rubrics for real-world evaluation and predicates for simulation evaluation, as described in Section 4.1.2. Using these, we measure task completion, based on task-specific intermediate milestones. For real-world evaluation, task completion is evaluated by filling out rubrics manually; we created a quality assurance (QA) process to measure the reliability of the rubrics. For simulation, task completion is computed automatically.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Results", "weight": 1.0} -->

Although we report absolute success rates, the most important results are the *relative* success rates of the different methods. The absolute success rates are very task dependent and can easily be shifted up or down based on how difficult we make the task (e.g., by broadening the distribution of initial conditions) and/or by changing the number of task-specific demonstrations. We design our experiments to make tasks quite difficult---targeting policy success rates around 50%---so that the relative success rates are as informative as possible, but in practice end up with significantly higher or lower rates.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Results", "weight": 1.0} -->

In the following, as described in Section 4.1.4, we use violin plots to convey the quantitative results with a horizontal line indicating the mean. For SR, the mean is the empirical success probability (successful runs/all runs) and the violin is the Bayesian posterior of individual success rates under a uniform Beta prior; it represents the uncertainty in the true success probability given the success rate and total number of runs. For TC, the mean is the mean of the task completion across all runs in either individual tasks or the aggregate of all tasks. For individual tasks, the violin represents the full data distribution of TC for that task. In plots where the tasks are aggregated, the violin represents the Bayesian posterior of the mean TC under a uniform Dirichlet prior. We emphasize that these distributions are evaluated for each individual policy checkpoint, and do not capture the randomness from the training process.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Results", "weight": 1.0} -->

For each task we perform multi-task hypothesis checking to test whether the separation observed is statistically significant. We indicate statistical significance in the result plots using the Compact Letter Display (CLD) method, which assigns the same letter to policies that cannot be separated and different letters to indicate separation with statistical significance.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results", "weight": 1.0} -->

In the following we discuss "seen" tasks (Section 3.1), "unseen" tasks (Section 3.2), and the effects of the amount of data used to pretrain and finetune LBMs on the performance (Section 3.3).

<!-- chunk {"id": "body-0023", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

(a) Nominal - no distribution shift (b) With distribution shift Figure 2: LBM performance on “seen” tasks in real-world and in simulation without (a) and with (b) distribution shift. We compare single-task with pretrained LBMs and with LBMs after finetuning. The x-axis labels show the task name, scenario name (for simulation tasks), and the number of demonstrations. Violin plots represent Bayesian posteriors of success rates under a uniform Beta prior and the observed success/failure data; policies labeled with different letters are statistically distinguishable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

We first analyze LBM performance on a subset of tasks included in the pretraining dataset (i.e., "seen" tasks), with results summarized in Figure 2. We evaluate LBMs that are only pretrained (Figure 2, teal) as well as pretrained LBMs with additional finetuning on individual tasks (Figure 2, maroon). Since these are relatively simple, short-horizon tasks, we do not present task completion results. The top row represents nominal conditions, and the bottom row represents experiments conducted under distribution shift. Details regarding how we systematically created the distribution shift are in Section 4.5.1 for simulation and in Section 4.5.2 for the real world.

<!-- chunk {"id": "body-0025", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

For "seen" tasks, we expect the pretrained LBM's success rate to be greater than zero since the tasks were in the training data, and we expect the finetuned LBMs to perform better than the single-task baseline, given the information that is encoded as part of the pretraining. In this set of experiments, we find that: Finetuned LBMs perform better on "seen" tasks than the single-task baselines: From Figure 2, we see that when aggregating over tasks, the finetuned LBM performs better than the single-task baseline under nominal and distribution-shift conditions both in simulation and in the real world; the finetuned LBM is statistically distinguishable from single-task in all the aggregate plots.

<!-- chunk {"id": "body-0026", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

When looking at individual tasks, the finetuned LBM is statistically the same or better than the single-task policy (i.e., it is labeled with "a") in 3/3 real-world tasks and 15/16 sim tasks, both for the nominal conditions and the distribution shift. Interestingly, the one sim task in which single-task statistically outperforms the finetuned LBM is different between the experimental conditions, as further discussed below. Overall, the finetuned LBM is statistically better than single-task policies under nominal conditions in 2/3 real-world tasks and 3/16 simulation tasks; under distribution shift, finetuned LBM statistically outperforms single-task policies in 2/5 real-world tasks and 10/16 simulation tasks.

<!-- chunk {"id": "body-0027", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

Finetuned LBMs are more robust to distribution shift on "seen" tasks than the single-task baseline: As expected, and as seen when comparing the two rows of Figure 2, when we introduce distribution shift the overall task performance, here defined as success rate, drops on most tasks. However, we also observe that the finetuned LBMs go from statistically outperforming single-task policies on 3/16 policies in simulation under nominal conditions to 10/16 under distribution shift. Furthermore, for the aggregate simulation plots, the separation between finetuned LBM and single-task widens under distribution shift. These results suggest that finetuned LBM created policies that are more robust to distribution shift than policies trained from scratch; this result also holds for the "unseen" tasks, as described in Sec. 3.2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

LBMs without finetuning have nonzero success rate on "seen" tasks and exhibit similar performance to the single-task baselines: As expected, the pretrained LBM (without any task specific finetuning) has a success rate that is greater than zero on all tasks under nominal conditions. When aggregating over tasks, pretrained LBM is statistically indistinguishable from single-task in simulation (both conditions) and in real-world with object-centric distribution shift. On nominal real-world and station distribution shift, pretrained LBM performs worse than the single-task baseline. For individual tasks, in all real-world tasks, pretrained LBM is either statistically indistinguishable (5/8) or worse than (3/8) the single-task baseline, across both conditions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

In simulation, under nominal conditions, pretrained LBM is statistically better than single-task in 3/16 tasks, and is statistically worse than single-task in 4/16. When considering distribution shift, the situation is similar, with pretrained LBM statistically better than single-task in 4/16 tasks and worse in 2/16 tasks. We make two observations related to the pretrained LBM; first, it performs worse than single-task mainly in the real-world tasks. Second, as discussed in Section 4.4.2, we discovered an error in the pretraining process (data normalization) after the evaluations were complete. This error might also affect the pretrained LBM's performance (see Section 14).

<!-- chunk {"id": "body-0030", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

We further investigate specific task performances that we found surprising.

<!-- chunk {"id": "body-0031", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

There are cases where the finetuned LBM performs statistically worse than the single-task baseline: In each condition, there is one simulation task for which finetuned LBM statistically underperforms the single-task baseline; the under-performing task depends on whether evaluation was conducted under nominal conditions or distribution shift.

<!-- chunk {"id": "body-0032", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

Under nominal conditions, TurnCupUpsideDown finetuned LBM performs substantially worse than both pretrained LBM and the single-task baseline, with a success rate of $0.335$. Here, in almost half (89/200) of the rollouts for finetuned LBM on this task, the robot did not move away from its initial pose before the simulation times out, as shown in Fig. S13(e-left). When introducing distribution shift, we did not observe this behavior (Fig S13(f-left)). Under distribution shift, StackPlatesOnTableFromRack performs worse than the single-task baseline. Inspecting the policy behavior did not reveal a systematic qualitative failure mode as in the previous case but confirmed the poor policy performance in general.

<!-- chunk {"id": "body-0033", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

Performance on the Breakfast scenario (simulation) tasks: Our simulation tasks are grouped into a handful of "scenarios", which start with the same environment assets and contain thematically similar tasks (see Section 4.3.2 for more details). We see that tasks belonging to the Breakfast scenario (denoted by B: in the X-axis caption of Fig 2, right) have higher variance in task success across tasks, compared to other scenarios, and that three tasks have substantially lower performance than the rest. We attribute this to two factors: first, for PutBananaOnSaucer and PutKiwiInCenterOfTable we have only 49 demonstrations; as expected and as discussed in the following sections, the less demonstration data available, the worse the performance. Second, for PushCoasterToMug, we observe that the task is more difficult than the rest because the robot needs to push obstacles out of the way, the goal (mug) can be anywhere on the table, and all the demonstrations use a pushing strategy on the side of coaster, which is sensitive to variance in the height of the end effector. We provide additional details in Section 10.

<!-- chunk {"id": "body-0034", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

A few tasks were more successful in the real world than in simulation: For the "seen" tasks, all the tasks that were evaluated in the real world were also evaluated in simulation. Given the lack of uncertainty in simulation, we would expect under nominal conditions that the success rate of these tasks would be higher in simulation. This is not the case for two tasks: PutKiwiInCenterOfTable (Kiwi for short) and TurnMugRightsideUp (Mug for short); for these tasks, across all policies, the real-world success rate is higher than simulation. One hypothesis for Mug is that the simulation timeout (the maximum time a simulation rollout is run for) is too short for the policy to eventually succeed. In contrast to the real-world evaluation, where the operator decided when to terminate the rollout, in simulation the rollout will be stopped even if the task is about to be completed. Computing success rates on real-world rollouts by truncating to the simulation timeout yields a similarly low success rate. For Kiwi we observe different behavior between simulation and hardware and will continue to explore this discrepancy.

<!-- chunk {"id": "body-0035", "role": "body", "section": "LBM performance on \"seen\" tasks", "weight": 1.0} -->

We present further analysis in Section 10.3. Simulation and real-world evaluations under distribution shifts are not directly comparable due to the differences in how they are introduced respectively.

<!-- chunk {"id": "body-0036", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

We explore LBM performance on tasks that do not appear in the pretraining dataset, i.e., unseen during training. It is straightforward to make "unseen" tasks in simulation. First, we generate additional tasks in the same scenarios as the "seen" tasks and that are similar in complexity, Figure 3. For the real world, generating tasks that are meaningfully distinct from our multi-year data collection effort is more challenging. To address this, we designed several long-horizon, multistep, dexterous tasks that were outside of the scope of previous task collections. For parity, we also added a new simulation scenario, Kitchen, with similarly long-horizon, multistep, dexterous tasks. These complex tasks are designed to test the limits of what our policies are capable of executing. Our results for the complex tasks are summarized in Fig 4 for nominal conditions and in Fig 6 for evaluation with distribution shift (sim only). In both of these figures, we present success rate results on the top row and task completion results on the bottom row.

<!-- chunk {"id": "body-0037", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

Furthermore, in addition to the SR and TC results for policies created (trained or finetuned) with all the task data, we analyze the aggregate performance of the policies when finetuned (LBM) or trained (single-task baseline) with subsets of the data (plots on the right). We provide a similar analysis for one real-world task in Figure 5.

<!-- chunk {"id": "body-0038", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

For our "unseen" tasks, especially the complex tasks, we do not expect the pretrained LBM to succeed; we therefore only compare the finetuned LBM and the single-task baseline. Furthermore, for the complex tasks, we expect low success rates and more intuition gained from the task completion plots.

<!-- chunk {"id": "body-0039", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

Finetuned LBMs perform better on "unseen" tasks than the single-task baseline, both in nominal conditions and under distribution shift: When aggregated across tasks, the finetuned LBM is statistically better than the single-task baseline in the real world and in simulation (both nominal and distribution shift), and across metrics (success rate and task completion).

<!-- chunk {"id": "body-0040", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

For the simpler simulation tasks, finetuned LBM is statistically better than single-task on 2/3 tasks in nominal conditions and all the tasks under distribution shift. For the complex tasks, while as expected the success rate is low, and even lower once considering distribution shift, some tasks still show statistical separation, and in all of those the finetuned LBM is more successful (2/5 tasks for real-world, 3/5 tasks in nominal simulation, and 1/5 tasks in simulation with distribution shift).

<!-- chunk {"id": "body-0041", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

When considering task completion, the conclusion that finetuned LBMs outperform single-task baselines becomes clearer; finetuned LBM is statistically better than the single-task baseline in 4/5 real-world tasks, and in 4/5 simulation tasks both in nominal conditions and under distribution shift. Visually inspecting the data distribution for task completion indicates that the finetuned LBM is able to achieve more steps of the task compared to the single-task baseline. When considering real-world tasks, we see that there is a task, SetBreakfastTable, that the single-task policy never completes,^11^1Due to the Bayesian analysis prior assumptions, the success rate graph appears to have a mean that is greater than 0; the empirical success rate for the single-task baseline of SetBreakfastTable is in fact 0. while the finetuned LBM succeeds and achieves higher task completion; conversely, there are two tasks, BikeRotorInstall and CutAppleInSlices, where in all rollouts the finetuned LBM completed part of the task, while the single-task baseline sometimes completely failed.

<!-- chunk {"id": "body-0042", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

Finetuned LBMs require less task-specific data to achieve similar performance as the single-task baseline: In Figures 4 and 6, the rightmost column shows the finetuned LBM and single-task baseline performances when aggregating across all five simulation tasks; each data point corresponds to finetuning/training with a different fraction (by demonstration) of the available task-specific data. For task completion, across both conditions (nominal and distribution shift), for all fractions of data, finetuned LBM is statistically better than the single-task baseline. For success rate, since the overall success rate is low, especially under distribution shift, the finetuned LBM is statistically better starting at 50% of the data. In aggregate, and interpolating, we see that to achieve similar performance in simulation, when finetuning an LBM we require less than 30% of the data needed for training from scratch.

<!-- chunk {"id": "body-0043", "role": "body", "section": "LBM performance on \"unseen\" tasks", "weight": 1.0} -->

We performed a similar experiment on the SetBreakfastTable real-world task, as shown in Figure 5 where the violin plot represents the full data distribution. LBM finetuned with only 15% of the data, statistically outperforms the single-task baseline (trained on all the data), further supporting our simulation findings.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Pretraining scaling laws", "weight": 1.0} -->

Using simulation, we explore the scaling laws of LBM pretraining--the effects of pretraining dataset size on the performance of LBMs, measured through task completion on "unseen" tasks. Due to the complexity of the tasks, the success rates are low (as seen in Figure 4) and do not provide a statistically distinguishable conclusion, therefore we present only task completion results here.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Pretraining scaling laws", "weight": 1.0} -->

We evaluate on the same five "unseen" simulation tasks as in Sec. 3.2 and perform experiments under nominal conditions, where we compare LBMs that were pretrained with different fractions of the data (Section 4.4) used to train the LBM of the previous subsections. We create four pretraining datasets for this experiment: 1) the full dataset (OXE-Ramen and TRI-Ramen), referred to as LBM finetuned, 2) TRI-Ramen only, referred to as LBM finetuned \[TRI-Ramen\], 3) 50% of all tasks present in the TRI-Ramen dataset, referred to as LBM finetuned \[TRI-Ramen-50%\], and 4) 25% of all tasks present in the TRI-Ramen dataset, referred to as LBM finetuned \[TRI-Ramen-25%\]. The results are shown in Figure 7; each line represents pretraining with a different fraction of data then finetuned, or the single-task baseline.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Pretraining scaling laws", "weight": 1.0} -->

For single-task, the graph starts from 15% of the finetuning data because without data (0%) we do not have a single-task policy. Note that the performance of the single-task and finetuned LBM are consistent with the previously reported results in Sec. 3.2 and specifically in Fig. 4. Similarly to Figures 4 and 6, each point on the X-axis indicates the percentage of total available demonstration data used to finetune the LBM.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Pretraining scaling laws", "weight": 1.0} -->

We note consistent separation with statistical significance between LBM finetuned and the TRI-Ramen version when using 0%, 15% and 50% finetuning data. Interestingly, when using 15% finetuning data, all five models are separable with statistical significance, with performance steadily increasing as we add more pretraining tasks. The same trend holds when using 50% and 100% pretraining data, and all models achieve the best performance when pretraining and finetuning with all available data.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Pretraining scaling laws", "weight": 1.0} -->

Pretraining and finetuning data tradeoff: This experiment suggests that there is a tradeoff between pretraining and task-specific finetuning. If there is limited task-specific data for finetuning, more tasks/data in the pretraining dataset corresponds to better finetuned LBM performance, even if the data is diverse (here the OXE dataset). Conversely, if there is a lot of task-specific data, LBMs pretrained with less data might suffice.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Materials and Methods", "weight": 1.0} -->

In this section we describe our evaluation protocol, the architecture we use to train the models, details regarding the experiments, the tasks, and the data we use to train and evaluate LBMs.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Evaluation Protocol and Analysis", "weight": 1.0} -->

One of the main contributions of this paper is our focus on rigorous robot policy evaluation that goes beyond what is typically done in the robot learning community. We designed an evaluation protocol that aims to ensure repeatable yet diverse initial conditions, and fairness across policy candidates. We evaluate our hypotheses in both simulation and the real world using statistical tools; this section describes the protocol we used, and the statistical methods we employ to test our hypotheses.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Policy comparison protocol", "weight": 1.0} -->

We focus on fair comparison across the different policies (single-task models vs LBMs), that is, we make every effort to minimize bias and subject the different policies to similar testing conditions, including environmental and initial conditions. To do so, in all our evaluations, the evaluators did not know which policy was being tested (blind testing), policy ordering was randomized to maximize fairness for each policy, and the initial conditions were consistent across the policies, within human error for hardware.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Policy comparison protocol", "weight": 1.0} -->

In simulation, we use the same simulation parameters and initial conditions (set via random seed) for all policies being compared. Initial conditions are sampled from the same distribution from which associated training data was generated, unless we are explicitly testing out-of-distribution generalization, but these initial conditions are new samples from the training distribution---we do not reuse exact initial conditions between training and evaluation in simulation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Policy comparison protocol", "weight": 1.0} -->

To ensure fairness when evaluating policies on hardware, we split evaluation into test bundles with the size of each bundle equal to the number of policies being compared. Each bundle corresponds to a single initial condition with a randomized policy ordering. After evaluating each policy, the initial conditions are reset until the bundle is completed and a new initial condition is evaluated. Real-world evaluation is blind--we ensured that the evaluator had no knowledge of which policy was being evaluated during each run. As for ensuring consistent test conditions, running policies in bundles with randomized order mitigates the effects on policy performance from environment changes (e.g., lighting). For initial conditions, we created a workflow where the robot evaluator was given an image overlay of the desired visual scene (see Fig. 8); by matching the robot's environment to the overlay, we mitigate the uncertainty in the initial conditions. The initial conditions come from simulation if the task and conditions are modeled in simulation, or from real pictures of initial robot scenes in the case of real-world tasks. We provide additional details for setting up initial conditions in simulation in Section 8.2 and for real-world in Section 9.3.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Rubrics and predicates", "weight": 1.0} -->

Rubrics are a set of questions that the robot evaluator fills out as they are observing the robot behavior. The questions address task progress (e.g., "robot grasped the apple") and failures (e.g., "robot dropped apple"). The questions are binary yes/no questions that can then be statistically analyzed to enrich our understanding of policy performance. The rubrics include a set of milestone questions per task, where each milestone is a step necessary towards a successful rollout. We calculated a Task Completion rate for the real-world rollouts by assigning a +1 credit to a successfully completed milestone and 0 otherwise, then the credits are summed and divided by the number of milestones.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Rubrics and predicates", "weight": 1.0} -->

Policy evaluation in simulation is automated through predicates that are defined over the simulation state (e.g., a predicate that is True when the apple center is closer than a small threshold to the bin center). A success in simulation corresponds to a set of predicates being True. These predicates also allow us to analyze partial success and failure modes of the policy.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Rubrics and predicates", "weight": 1.0} -->

For more details and example rubrics and predicates, refer to Sections 9.4 and 8.3.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Rubric QA", "weight": 1.0} -->

Considering that the rubric results are provided by reviewers who are prone to human error, we estimated the discrepancy percentage through an additional validation on a smaller subset of the reported rubric answers. To this end, we conducted a quality assurance (QA) round on $\sim {27\%}$ of nearly 2700 real-world evaluation rollouts^22^2Not all real-world rollouts are included in the results, since some came from earlier iterations. All rollouts that were QAed were from evaluation tasks. to estimate the discrepancy in the answers. The subset of people doing rubric QA was separate from the robot evaluators. The QA success rate discrepancy was 2.31% and the overall rubric question discrepancy was 6.25%.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Rubric QA", "weight": 1.0} -->

We performed one round of corrections, based on the discrepancy between the recorded success and the success calculated based on the rubrics. This involved updating five rollouts. We note that the results reported in Section 3 were calculated after the corrections were applied.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Statistical Analysis: Performance Characterization of Individual Policies", "weight": 1.0} -->

Throughout the paper, we report statistical uncertainty of empirical performance of individual policies. Our analysis is based on binary success/failure and on task completion for more challenging, longer-horizon tasks.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Binary Success/Failure Criteria", "weight": 1.0} -->

From the statistical perspective, computing the success rate of a policy is equivalent to estimating the Bernoulli parameter $p$ of the underlying Bernoulli distribution generating the success/failure labels. This assumes that each evaluation trial is independent and identically distributed (i.i.d.). In simulation, this assumption is satisfied by randomizing the initial conditions with seeds. For real-world experiments, we take a set of measures discussed in Section 4.1.1 to mitigate the effect of time-varying randomness and unwanted bias as much as possible.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Binary Success/Failure Criteria", "weight": 1.0} -->

In some cases, we report statistical results that are aggregated over multiple tasks. Strictly speaking, this violates the i.i.d. assumption as the number of trials from each task is fixed a priori instead of a random draw from a uniform distribution over the 3 tasks. Nevertheless, the effect of this violation is negligible in practice and is recommended practice in prior work on policy evaluation. To visualize the uncertainty over the unknown parameter $p$, we perform Bayesian analysis and compute the posterior after observing success/failure data. Specifically, we use a uniform prior over the Bernoulli parameter as suggested by and plot the Bayesian posterior in the form of a violin plot. See Fig. 2 for an example. We use violin plots rather than standard Confidence Intervals (CIs) for two reasons. First, violin plots depict the entire distribution of the parameter $p$ instead of a single interval, thus presenting richer information on statistical uncertainty. Second, CIs can be confusing or misleading when it comes to policy comparison; one may wrongly conclude that two results are not separated with statistical significance if their corresponding CIs overlap. In fact, CIs can overlap while more powerful hypothesis tests may still statistically separate them.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Binary Success/Failure Criteria", "weight": 1.0} -->

In Section 4.1.5, we discuss how we can incorporate such hypothesis tests in our analysis to accompany the individual Bayesian analysis.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Task Completion Criteria", "weight": 1.0} -->

For the task completion criteria based on our rubrics or predicates, the mean of the corresponding categorical distribution may not represent the entire distribution, unlike the Bernoulli case (i.e., variance and other higher-order moments are not uniquely determined by the mean). Therefore, we present the violin plots of the raw data instead of the Bayesian analysis of the mean so they illustrate the full distribution better; see Fig. 4 (bottom row, left and middle) for an example. We will resort to the mean of the distribution only to a) examine the effect of fractional fine-tuning (Fig. 4, bottom row, right) and b) compare the performance of two or more policies. For a), we use a uniform Dirichlet prior, similar to the binary success/failure setting. For b), we discuss the details of policy comparison below.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Statistical Analysis: Performance Comparison of Multiple Policies", "weight": 1.0} -->

We perform hypothesis tests to compare multiple policies; we run ${k{({k - 1})}}/2$ pairwise tests where $k$ is the number of policy models to be compared at once. In each test, the confidence level is adjusted for multiplicity via Bonferroni correction unless otherwise noted, so that a global 95% confidence level is maintained across all the ${k{({k - 1})}}/2$ comparisons. We use the Compact Letter Display (CLD) algorithm to summarize the results. With CLD, each policy is labeled with one or more letters such as "a", "ab" or "bc". Two policies that do not share the same letter are separated with 95% confidence.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Statistical Analysis: Performance Comparison of Multiple Policies", "weight": 1.0} -->

For each pairwise test, we use an appropriate statistical method depending on the type of the data. For the more common binary success/failure criteria, we use a sequential hypothesis testing framework as suggested, which sequentially compares paired outcomes of each evaluation trial until either a decision is reached or all the trials are consumed. Specifically, we adopt the test originally proposed, which yields reasonable statistical power in the small sample size regime while maintining a strict Type-I error control for binary data. (That is, the chance of falsely concluding that the two policies are statistically separated is upper-bounded by 5%). For the task progress, we cannot apply as it does not readily extend to categorical data. Instead, we use the Welch's t-test to compare the means of two distributions. Strictly speaking, the discrete nature of the data violates the underlying assumption of the t-test that the data is normally distributed. Thus, the Type-I error is not controlled. However, we ensure that the sample size is sufficiently large (i.e., about 50 or more) so that the degree of violation is small owing to the central limit theorem.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Statistical Analysis: Performance Comparison of Multiple Policies", "weight": 1.0} -->

Nominally, the aforementioned policy comparison procedure is performed per task. When multiple tasks are considered and plotted at once, we do not further adjust the confidence level of individual pairwise tests, since doing so would yield individual confidence levels that are too stringent. Therefore, we note that the Type-1 error is not globally controlled across tasks when they are presented in one plot. Nevertheless, we do aggregate the results over tasks when we compare the overall multi-task performance of different policies. This yields an exchangeable Bernoulli sequence, approximating an i.i.d. sequence by marginalizing over skills. Exchangeability is weaker than i.i.d., so the underlying assumption of the pairwise test is slightly violated. However, we empirically verified that this difference does not affect the statistical validity of results.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Large Behavior Models", "weight": 1.0} -->

In this section we describe the LBM generative model, training objective, architecture, pretraining and finetuning recipes, and deployment details; see Figure 9 for an overview of our architecture.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Diffusion for Visuomotor Control", "weight": 1.0} -->

We implement generative policies for visuomotor control by employing Denoising Diffusion Implicit Models (DDIM). We choose this class of generative model because it has been shown to be effective at learning visuomotor manipulation policies from human demonstrations. DDIMs transform a simple prior distribution, typically Gaussian noise, into a complex, structured (action) distribution conditioned on input data -- in our case, visual, proprioceptive, and language observations. This transformation uses a deterministic sampling process derived from denoising diffusion probabilistic models (DDPM). Given $K \geq 1$ denoising steps, we start with a noise sample $A_{t}^{K} \sim {\mathcal{N}{(0,I)}}$ at time $t$ and use DDIM to denoise it into a continuous action $A_{t}^{0}$ in $K$ iterative steps.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Diffusion for Visuomotor Control", "weight": 1.0} -->

In order to predict actions conditioned on observation inputs, we modify the original DDIM update as follows: where $A_{t}^{k}$ is a set of noisy actions at the $k$-th denoising step, $O_{t}$ are the observations, and $k$ is the diffusion timestep. Parameters $\alpha$ and $\gamma$ are determined by a noise schedule which varies with the diffusion timestep $k$, and $\epsilon_{\theta}$ is the noise-prediction neural network with weights $\theta$. To train $\epsilon_{\theta}$, we sample an action $A_{t}^{0}$ and a random step $k$, and add a step-dependent Gaussian noise $\varepsilon_{k}$ to form a noisy action $A_{t}^{k} = {A_{t}^{0} + \varepsilon_{k}}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Diffusion for Visuomotor Control", "weight": 1.0} -->

The network is then trained to predict $\varepsilon_{k}$ from $A_{t}^{k}$, enabling it to denoise across the full range of diffusion levels.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Policy Architecture", "weight": 1.0} -->

We parametrize the noise prediction network, $\epsilon_{\theta}$, as a Diffusion Transformer (DiT), which conditions on features extracted from the observations and the diffusion timestep in predicting actions (see Section 4.4.1 for the observation and action spaces). To extract features from the image observations we use the CLS token output from a pretrained CLIP Vision Transformer (ViT) backbone. Language features are similarly computed from the task description using a CLIP text encoder, with a projection layer on top of the pooled End of Sequence token. The language and visual features are concatenated with the proprioception for each observation timestep as well as with the diffusion timestep, $k$, which is encoded with a sinusoidal positional embedding followed by a two-layer MLP. During training, we finetune through the visual feature extractor, which is shared across all camera inputs. We keep the language-feature extractor frozen, but train a projection layer on top of the language features.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Policy Architecture", "weight": 1.0} -->

The DiT conditions on two timesteps of concatenated observation features, which together have a size of $6,732$, and the encoded diffusion timestep via an adaptive layer norm (adaLN) MLP. This model consists of eight DiT blocks with an embedding size of 768. The network predicts 16 timesteps of 20-dimensional actions, for a total output size of $A_{t}$ = 320. All experiments use the architecture described above. In the case of finetuning on single-task data or evaluating from-scratch policies we use the same architecture and only use the language prompts for the task of choice.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Training and Deployment", "weight": 1.0} -->

Our training recipe follows a common pattern for foundation models where we first pretrain policies on the full data mixture and then finetune on narrower data subsets. Hyperparameters for both stages are summarized in tables 1 and 2.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Training and Deployment", "weight": 1.0} -->

We pretrain on the full dataset mixture described in Section 4.4. During training, we first resize images to 256x342, then randomly crop and apply color jitter, which yields 224x224 images. We train for 48k steps with a global batch size of 2560 with a constant learning rate of 3e-4. The vision encoder uses a learning rate one tenth that of the rest of the model.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Training and Deployment", "weight": 1.0} -->

We finetune the pretrained policy on demonstrations from individual tasks. We found that the optimal checkpoint generally occurred earlier in training for simulated tasks than for real tasks. As a result, we finetune for 30k steps for real tasks and for 10k steps for simulated tasks with a global batch size of 320 and a reduced learning rate of 2e-5. We leave co-training, alternate learning rate schedules, and strategies for selecting optimal pretraining and finetuning checkpoints to future work. During finetuning, we use the same image augmentation hyperparameters as during pretraining.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Training and Deployment", "weight": 1.0} -->

While we compute the loss on 16 action steps during training, during deployment we only execute eight timesteps before recomputing actions. As in training, images are resized to 256x342, but then center-cropped to 224x224 rather than randomly cropped. The policy loop executes at a rate of 10 Hz.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Training and Deployment", "weight": 1.0} -->

Global Batch Size Table 1: Hyperparameters used during pretraining, finetuning, and with single-task models.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Training and Deployment", "weight": 1.0} -->

Random Crop (HxW) DiT Embedding Dimension CLIP Image Encoder Table 2: Image Augmentation and Model Architecture Hyperparameters

<!-- chunk {"id": "body-0079", "role": "body", "section": "Platform", "weight": 1.0} -->

We focus here on tabletop bimanual manipulation using two Franka FR3 robot arms with parallel gripper and TRI's finray-style fingers. See Figure 10, top-left, for an overview of the physical platform. We had one major hardware upgrade that changed the gripper model and wrist camera configurations; see Sec. 7.1 for more details. We collected training data on both platforms, and all real-world evaluations presented here are done on the new platform. We used a total of nine robot stations, see details in Table S1. We run the Franka robots using our custom joint impedance controller, with a differential inverse kinematics controller on top to translate end-effector relative SE commands from the human teleoperator or the LBM policy. The differential inverse kinematics controller also handles collision avoidance. For the new platform, we use the -110 gripper on each arm. The workspace contain two FRAMOS D415e scene cameras and each wrist has two FLIR Blackfly S BFS-PGE-23S3C-CS cameras. All policies are run at 10 Hz.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Simulation", "weight": 1.0} -->

Our primary usage for simulation is for evaluation. One of the main bottlenecks for iterating on policy design is evaluation both in terms of throughput and level of control. Relying on real-world testing alone for enough samples to support any meaningful statistical analysis is prohibitively expensive and time consuming. To address this, we have been developing our simulation benchmark, lbm_eval, which is built on top of Drake. lbm_eval uses curated assets and human-authored scenarios and tasks. Each simulation is deterministic given a random seed (however, the GPU-based policies do not have the same guarantee).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Simulation", "weight": 1.0} -->

Our simulation policy evaluations are run against four scenarios, all of which differ in their affordance for task complexity, object types, and object count (see Figures S2, S3 S4 and S5). All scenarios contain a workspace modeled after a real-world robot station (see station details in Table S1). All four scenarios are inspired by kitchen settings and focus on food preparation and organization. All four scenarios contain task-relevant manipulands (objects that are manipulated as part of the task) in addition to varying numbers of distractors. The first two scenarios are modeled after the old hardware platform, and the later two are modeled after the new hardware platform.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Simulation", "weight": 1.0} -->

The DryingRack (D) scenario contains plates, mugs, and spatulas, in addition to a mug holder, utensil crock, and a dish drying rack. This scenario has 13 tasks. The Shelf (S) scenario contains various types of fruits and vegetables, a shelf, fruit bowl, bin, cereal box, and a cutting board. There are 12 tasks in this scenario. The Breakfast (B) scenario contains various types of fruits, a mug, plate, coaster, and a cup. This scenario is designed specifically for testing language conditioning since the initial conditions for different tasks visually appear the same. There are 18 tasks in this scenario. The Kitchen (K) scenario contains bins, various types of fruits and vegetables, and a plate. Scenario K has 5 tasks, and is the only scenario that is entirely absent in the pretraining dataset, as described in Section 4.4. All tasks in this scenario are long horizon, and some require nonprehensile manipulation or understanding of semantic attributes (e.g., vegetable vs fruit, large vs small). Scenarios B and K are somewhat simpler in terms of scene complexity as compared to the first two scenarios.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Simulation", "weight": 1.0} -->

A fifth scenario is used for debugging policies early on during training and consists of just one task where the robot has to move a box to the center of the table. This scenario is not used as part of evaluation, but its demonstration data is included in the pretraining dataset.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Pretraining data", "weight": 1.0} -->

Our pretraining mixture, called Ramen, consists of a large-scale dataset of robot demonstrations totaling $\sim$`<!-- -->`{=html}1695 hours of demonstration, including high-quality data collected at TRI ($\sim$`<!-- -->`{=html}545 hours; TRI-Ramen) combined with curated external robot data ($\sim$`<!-- -->`{=html}1150 hours; OXE-Ramen).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Pretraining data", "weight": 1.0} -->

TRI-Ramen data consists of a total of 545 hours of real data over 532 tasks for a total of 64,262 demonstrations. This is made up of: TRI-Ramen-Real - 468 hours, 362 tasks and 46063 demonstrations collected across 9 hardware stations; TRI-Ramen-Sim - 45 hours, 41 tasks and 7348 demonstrations collected across 2 simulation stations; and TRI-Ramen-UMI (32 hours, 129 tasks, 10851 demonstrations) collected with the Universal Manipulation Interface using 7 pairs of handheld devices in "in-the-wild" environments.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Pretraining data", "weight": 1.0} -->

TRI-Ramen-Sim tasks used in the pretraining set exclude all five tasks from scenario K, and one task each from scenarios D, S and B; results of evaluating these "unseen" tasks can be found in Section 3.2.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Pretraining data", "weight": 1.0} -->

For each of the 40 simulation tasks from scenarios D, S and B that are part of the pretaining set, we collect corresponding real-world demonstrations of the same task in the similar environments (subject to hardware differences across fleet). Scenario B tasks are collected with matched initial conditions as in simulation. Scenarios D and S are collected with manually created initial conditions. These are part of TRI-Ramen-Real (i.e., they are also part of the pretraining set). During real-world data collection, we distributed each task's demonstrations evenly across 2 to 4 robot stations, such that each station produces approximately 100 demonstrations. For each task, one of the stations used to collect real data is the robot station the simulated environment is modeled after.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Pretraining data", "weight": 1.0} -->

OXE-Ramen data is a subset of the OpenX-Embodiment datasets. The subset was chosen based on a set of heuristics such as object and environment diversity and total number of episodes. The observations and actions were mapped to conform to the TRI-Ramen data format. Mappings include standardization of frames of reference and units for end-effector poses and gripper widths, and resizing and cropping images.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Pretraining data", "weight": 1.0} -->

During training, we batch balance the Ramen datasets by a set of empirically found weights to ensure each batch contains samples of all the datasets. See Table S7 for datasets used in pretraining and associated weights.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Observation and Action spaces", "weight": 1.0} -->

The observation space includes i) end-effector poses w.r.t. the station base frame (table center), ii) end-effector poses w.r.t. the other end-effector, iii) continuous gripper width, iv) 6 RGB images (missing cameras are zero-padded), and v) one natural-language instruction. The action space includes i) end-effector poses w.r.t. the station's base frame, and gripper widths. Orientation is represented as a 6D vector that corresponds to the top 2 rows of the rotation matrix. For observations and actions, we use a similar relative trajectory representation as. Additionally, we use a history of observations ($n_{obs} = 2$) and an action prediction horizon ($n_{horizon} = 15$) as. Unimanual data from OXE-Ramen was converted into bimanual by zero padding the missing arm and randomly swapping the arm's side. Each episode in TRI-Ramen contains a list of language instructions that are randomly sampled during inference.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Observation and Action spaces", "weight": 1.0} -->

Such a list includes one instruction written by a human and five instructions generated by prompting a LLM (ChatGPT) to give alternative versions of the human-generated instruction. Missing language annotations in OXE-Ramen were filled with a generic text: "do something useful".

<!-- chunk {"id": "body-0092", "role": "body", "section": "Data Normalization", "weight": 1.0} -->

For data in Ramen, normalization is done on a per-feature dimension (e.g., end-effector pose) and per-timestep (i.e., observation history, and action prediction horizon) basis. Values are normalized to fall within a fixed range of $\lbrack{- 1.5},\, 1.5\rbrack$, by being scaled by the the 2nd and 98th percentiles, $x^{0.02}$ and $x^{0.98}$, and being clipped beyond the range $\lbrack{- 1.5},\, 1.5\rbrack$. For all data samples $x_{i} \in \mathcal{D}$, we compute the corresponding normalized value $y_{i}$: This shifts and scales the percentile range of 2 to 98 to lie from $- 1$ to $1$ while retaining some outliers, but keeps most of the resolution in the high-density center of the data distribution.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Data Normalization", "weight": 1.0} -->

Since we represent actions relative to the current time's observations, actions further into the future have a wider spread than the immediate next actions. Computing normalization parameters for each timestep independently better preserves resolution for near-future actions, which are the more important parts to predict accurately. We avoid this normalization procedure for the 6D rotation in the poses to avoid corrupting the rotation matrix. Note that 6D rotation lies in the range.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Data Normalization", "weight": 1.0} -->

The normalization parameters ($x^{0.02}$ and $x^{0.98}$) were calculated independently per data source for OXE-Ramen and TRI-Ramen-UMI. TRI-Ramen-Real and TRI-Ramen-Sim are used together to compute lbm_robot normalization parameters. At training time, individual datagrams are normalized separately based on their data source. At test time, the lbm_robot normalizer is used to de-normalize actions for our robots. Due to an error in the code, some datagrams were normalized incorrectly (with normalization parameters belonging to a different data source) within each batch during pretraining of the models presented in Section 3. Due to the cost of performing extensive real-world evaluation, we did not repeat the experiments in Section 3, but rather performed a smaller scale experiment on "seen" tasks in simulation to assess the impact of the incorrect normalization. Fig. S21 shows that the difference is small under nominal conditions, and the LBM with the correct normalization parameters performs better under distribution shift.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Dataset filtering", "weight": 1.0} -->

The TRI-Ramen dataset consists of a number of low-motion frames at the start of certain demonstrations. This is due either to operator error or to the teleoperation UI being loaded more slowly than the start of the demonstration logging. We implemented a simple filtering operation, defining a motion threshold to capture when the gripper moved either more than 5 cm in translation or 15 deg in rotation with respect to its starting pose. We then remove all data from the start of the demonstration until the motion threshold is met.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Dataset filtering", "weight": 1.0} -->

In simulation, we analyze the effects of filtering out this data and find that, when trained with unfiltered data, the single-task and LBM policies exhibit difficulty to initiate motion at the beginning of each rollout. The severity of this symptom is policy, task and evaluation conditions (nominal vs distribution shift) dependent. Filtering the low motion data improved single-task performance in simulation; however, it led to a surprising decrease in performance for pretrained LBM, where we observed that it would commit to some uncommanded task more often than before. We therefore made the design choice to pretrain with unfiltered data, but finetune LBMs and train single-task policies using the filtered dataset in simulation tasks. We performed an analysis of training exclusively with filtered data, and our findings are shown in Section 12. Due to the cost of real-world evaluation, we did not study this phenomenon on real world tasks, using the unfiltered version of task-specific finetuning data.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Evaluation Tasks", "weight": 1.0} -->

There are two types of tasks for evaluation, "seen" and "unseen", depending on their presence in the TRI-Ramen dataset during pretraining. For simulation evaluation, we selected 16 "seen" tasks randomly from TRI-Ramen-Sim and 8 "unseen" tasks, all part of lbm_eval. For real-world evaluation, we selected 3 "seen" tasks and 5 "unseen" tasks, where the 3 "seen" tasks are part of the simulation "seen" tasks, i.e., they have matching simulation and real data demonstrations, as described in Section 4.4. The task names and number of demonstrations collected are listed in Tables S2 and S5, while example evaluation tasks shown in Figure 10, bottom.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Evaluation Tasks", "weight": 1.0} -->

We measure performance under several distinct conditions, including nominal in-distribution conditions, as well as conditions exhibiting distribution shift. For each task, we test 200 initial conditions in simulation and 50 in real world. See Appendix 8.2 and 9.3 for sample initial conditions in simulation and in the real world.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Simulation", "weight": 1.0} -->

We select a small subset of our simulation tasks to use for evaluation, covering four scenarios. All tasks in scenarios K as well as many in D and S are designed specifically to be visually ambiguous given their initial conditions, requiring policies to rely on language conditioning to determine what actions to execute. We consider two conditions for simulation experiments: Nominal (Sim) and Distribution Shift (Sim).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Simulation", "weight": 1.0} -->

Nominal (Sim): Under this setting, object poses as well as quantities are drawn from predefined distribution with rejection sampling to obey constraints such as no interpenetration. Additionally, in-distribution scene lighting parameters for a single directional light source are also drawn from predefined distributions. Lighting parameters include color (over the HSV color wheel), intensity, and direction. In addition to the single parameterized light source, a fixed environment map provides additional ambient lighting to the scene.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Simulation", "weight": 1.0} -->

Distribution Shift (Sim): Most of lbm_eval's distribution shift is implemented to test policy robustness against appearance changes. For lighting, we define a secondary directional light source with intensity and direction parameters drawn from shifted distributions. Additionally, the environment map is drawn from a discrete set of twenty choices unseen during training. Scene-camera extrinsics and intrinsics are also randomized. Finally, alternate textures and colors are sampled for objects as well as the table top. The level of distribution shift for colors and textures varies, depending on the specific scenario. In addition to pure appearance variations, we also introduced random distractor objects in scenario B. More details are presented in Section 8.2 and Table S3.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Real", "weight": 1.0} -->

We test model performance on eight real-world tasks. Three are short-horizon tasks for which both real and simulation data was seen at pretraining. The other five tasks are unseen long-horizon, multistep tasks that require sequencing diverse types of manipulation. For example, the CutAppleInSlices task (Figure 6(b) ‣ Figure S6 ‣ 9.2 Real-world evaluation tasks ‣ 9 Real-world evaluation details ‣ A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation")) requires the robot to use an apple corer to core an apple, retrieve a knife from a crock, unsheath the knife to slice the apple into halves, slice the halves into slices, and finally wipe the knife with a cloth before re-sheathing it and placing it back into the crock. We further design three distinct evaluation conditions^33^3To determine axes of distribution shift, we informally evaluated earlier experimental models under a wide variety of distribution shifts.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Real", "weight": 1.0} -->

We selected modes that were operationally easy to implement, avoiding modes for which a large number of initial conditions would fail and therefore provide a less informative signal.: Nominal (Real), Station Distribution Shift (Real), and Object-Centric Distribution Shift (Real); see Figure. 10 for an example.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Real", "weight": 1.0} -->

Nominal (Real): For tasks that have simulation counterparts, the initial conditions of manipulands and distractors are matched to initial conditions generated in simulation via the overlay described in Sec.4.1.1. For tasks without simulation counterparts, the original demonstrator of the task created a new set of initial conditions, using the original objects. The tasks are then tested on an robot station with training data coverage.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Real", "weight": 1.0} -->

Station Distribution Shift (Real): To test cross-station transfer, we evaluate policies on stations not in the finetuning dataset for the task. For this setting, we use the same initial conditions for objects and distractors as in Nominal (Real).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Real", "weight": 1.0} -->

Object-Centric Distribution Shift (Real): We implement two types of object-centric distribution shift in real experiments: manipulands and distractors. Each key manipuland for a given task is tested on at least five novel instantiations (see Figures 10 and S10). Evaluation scenes feature various levels of distractor clutter, where distractors were sampled from a set of both seen and novel objects. To the best of our ability, we sourced novel manipulands and distractors that we believe to not be present in any of the pretraining data. In order to create such initial conditions, we start by populating an empty scene with task-specific manipulands using their initial conditions sampled in simulation, then gradually adding different levels of clutter.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Large Behavior Models move dexterous manipulation away from task-specific engineering and into a scalable and data-driven paradigm similar to recent progress in language and vision. To rigorously quantify the capabilities of current LBMs, we train a series of models on roughly 1,700 hours of heterogeneous demonstration data and analyze their performance on 1,800 blind A/B-style real-world rollouts and over 47,000 simulation rollouts.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We find that finetuning LBMs into task-specific specialists consistently outperforms from-scratch training with a given amount of finetuning data or allow achieving from-scratch-equivalent performance with 3-5x less data required. These differences are also amplified under deployment distribution shift---when test-time conditions differ from those encountered during training. This finding is critical because distribution shift is virtually inescapable in real-world use cases and is often omitted from empirical robotics work, masking important information about real-world utility.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We also find that finetuned performance smoothly improves with increasing pretraining data. At the data scales we examined, we find no evidence of performance discontinuities or sharp inflection points.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Interestingly, we encountered mixed results with non-finetuned LBMs. Encouragingly, we found that a single network is able to learn many tasks simultaneously, but we don't observe consistent outperformance of from-scratch single-task training without finetuning. We expect this is partially due to language-steering brittleness of our models with their small language encoders. We've seen promising early signs that larger VLA prototypes overcome some of this difficulty, but more work is required to rigorously examine this effect in higher-language-capacity models.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Our findings largely support the recent surge in popularity of LBM-style robot foundation models, adding to evidence that large-scale pretraining on diverse robot data is a viable path towards more capable robots. However, we also find evidence for caution in the field. Many of the effects we observe were only measurable with larger-than-standard sample sizes and careful statistical testing that is non-standard for empirical robotics. Due to the size of current effects and the magnitude of experimental noise, there is significant risk that many robotics papers are measuring statistical noise due to insufficient statistical power. Additionally, we find that decisions like data normalization have a large effect on downstream performance, often dominating architectural or algorithmic changes; when comparing methods it is critical that these design choices are studied in isolation to avoid conflating the source of performance changes.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Limitations", "weight": 1.5} -->

One important limitation of our analysis is that we do not explicitly account for the stochasticity across training when we compare two policy architectures (this would be very expensive to do with statistical significance). Specifically, given a fixed dataset, fixed (stochastic) evaluation benchmark, and a policy architecture, we have where $w$ are the parameters (weights) of the policy. Our confidence intervals are computed for the first term, but do not account for the second.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Limitations", "weight": 1.5} -->

We made a decision to run 50 real-world rollouts per task per policy per condition, and to further reduce the measurement uncertainty with hardware displays for reproducible initial conditions. The reproducible initial conditions did mean that each rollout took more time; we intend to continue to optimize the evaluation protocol to improve throughput. Additionally, despite these experimental protocols designed to minimize environment variability and human error, we expect that both initial condition and scoring mistakes are non-zero, likely adding to the noise of our measurements. As a result, our real-world results potentially miss small-magnitude effects due to signal-to-noise limitations.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Limitations", "weight": 1.5} -->

We also study LBMs with modestly-sized language encoders pretrained via CLIP. While we expect many of our findings will generalize to larger VLAs, we expect that some aspects like language steerability will differ in that setting.
